import logging

import pytest


from ..utils.dut import DuT

__all__ = ['session_auto_dut', 'auto_dut']


@pytest.fixture(scope='session')
def session_auto_dut():
    """ Session scoped instance of the DuT"""
    return DuT()


@pytest.fixture(scope='function')
def auto_dut(session_auto_dut, request):
    """ Function scoped fixture for the DuT"""
    log = logging.getLogger('fixture.auto_dut')
    log.info("Prepare auto_dut")
    print(dir(request.node))
    markers = list(request.node.iter_markers('dut_state'))
    num_markers = len(markers)
    if num_markers == 0:
        log.info("No state set -> reset everything")
        session_auto_dut.reset_state()
    elif num_markers == 1:
        m = markers[0]
        assert len(m.args) >= 1, "dut_state requires one argument"
        state_name = m.args[0]
        log.debug("Requesting state: {0}".format(state_name))
        session_auto_dut.ensure_state(state_name)
    else:
        pytest.fail("Only one marker 'dut_state' can be set")
    yield session_auto_dut
    log.info("Tear down dut")
