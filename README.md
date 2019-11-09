Pytest Advanced use cases
=========================

A collection of ideas how to use *Pytest* in more advanced scenarios


# Manual DuT setup

Very simple idea declaring multiple fixtures to represent the state

## Setup

1. Declare multiple fixtures for different operating states (`manual_duts.py`)
2. Derive different fixtures that are used in the test cases

    - `dut_default` to represent the _normal_ operation condition
    - `dut_debug`   on special operating mode for extended testability
    - `dut_off`     DuT is powered down before starting the test case

3. Manual tests can be found in `test_dut_state_manual.py`


## Conclusion

Works fine, but quite cumbersome to in the test cases and in the fixtures:
- Duplication
- Different names for the DuT's
- Less protection against mistakes like messing up the state in a test case that uses `dut`
  or `session_dut`

# DuT setup using markers

Use only one fixture for the DuT and define the requested state via a marker

## Setup

1. Declare a marker `dut_state(state_name)` (in `conftest.py`) and one fixture for the DuT
   `auto_dut` (based on `session_auto_dut`) in `auto_dut.py`
2. Check markers of the *function*-scoped `auto_dut` fixture.

    - if not set, reset to off state
    - if `dut_state` marker was found, ensure the DuT is in that state
    
3. Automatic tests can be found in `test_auto_dut_state.py`


## Conclusion

It seems like the better approach:
- Only one fixture and less code duplication
- Automatically handle the case when no state is specified
- Mixing function and module scoped tests works as expected:

    - If marker is set on module scope, it's not allowed to defined another marker. An error
      will be raised and inform about the problem (see `auto_dut` fixture)
    - Class level markers can also be used to structure test runs and avoid having to repeat
      the declaration of `dut_state` over and over

## Open questions

- How does it mix with other markers and `pytest.mark.parametrize`
