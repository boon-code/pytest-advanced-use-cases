import pytest
import logging

from ..utils.dut import DuT


__all__ = ['dut', 'dut_debug', 'dut_default', 'dut_off', 'session_dut']


@pytest.fixture(scope='session')
def session_dut():
    """ Session scoped instance of the DuT"""
    d = DuT()
    log = logging.getLogger('fixture.session_dut')
    log.info("Setup DuT {0}".format(d))
    yield DuT()
    log.info("Clean up DuT {0}".format(d))


@pytest.fixture()
def dut(session_dut):
    """ Function scoped fixture for the DuT for state dependend fixtures"""
    log = logging.getLogger("fixture.dut")
    d = session_dut
    log.info("Clear DuT parameters")
    d.params.clear()
    log.debug("DuT params before test: {0}".format(d.params))
    yield d
    log.debug("DuT params after test: {0}".format(d.params))


@pytest.fixture()
def dut_default(dut):
    """ Fixture requiring the DuT in default state"""
    dut.ensure_state("default")
    return dut


@pytest.fixture()
def dut_debug(dut):
    """ Fixture requiring the DuT in debug state"""
    dut.ensure_state("debug")
    return dut


@pytest.fixture()
def dut_off(dut):
    """ Fixture requiring the DuT in off state"""
    log = logging.getLogger('fixture.dut_off')
    log.info("Set state to 'dirty' and power dut off")
    dut.reset_state()
    return dut
