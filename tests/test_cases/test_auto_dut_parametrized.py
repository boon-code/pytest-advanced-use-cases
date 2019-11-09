import pytest


@pytest.mark.dut_state('default')
@pytest.mark.parametrize('msg', [
    'First message', 'Second message', 'Third message'
])
def test_normal_parametrized_1(auto_dut, msg):
    print(msg)
    assert auto_dut.get_state() == 'default'


@pytest.mark.parametrize('msg', [
    'First message', 'Second message', 'Third message'
])
@pytest.mark.dut_state('default')
def test_normal_parametrized_2(auto_dut, msg):
    print(msg)
    assert auto_dut.get_state() == 'default'

@pytest.mark.parametrize('msg,state', [
    pytest.param("Test1 in normal mode", 'default', marks=pytest.mark.dut_state('default')),
    pytest.param("Test2 in normal mode (no reset)", 'default', marks=pytest.mark.dut_state('default')),
    pytest.param("Test3 in normal mode (no reset)", 'default', marks=pytest.mark.dut_state('default')),
    pytest.param("Test4 from power off", 'off', marks=pytest.mark.dut_state('off')),
    pytest.param("Test5 from power off (no reset)", 'off', marks=pytest.mark.dut_state('off')),
    pytest.param("Test6 without any state set", None),
    pytest.param("Test7 in debug mode", 'debug', marks=pytest.mark.dut_state('debug')),
    pytest.param("Test8 in debug mode (no reset)", 'debug', marks=pytest.mark.dut_state('debug')),
    pytest.param("Test9 in debug mode (no reset)", 'debug', marks=pytest.mark.dut_state('debug'))
])
def test_all_states(auto_dut, msg, state):
    print("")
    print(msg)
    if state is None:
        assert auto_dut.get_state() is None
    else:
        assert auto_dut.get_state() == state
