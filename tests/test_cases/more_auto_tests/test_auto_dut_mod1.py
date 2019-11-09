import pytest


pytestmark = [pytest.mark.dut_state('debug')]


def test_debug_state_1(auto_dut):
    assert auto_dut.get_state() == 'debug'



def test_debug_state_2(auto_dut):
    assert auto_dut.get_state() == 'debug'



def test_debug_state_3(auto_dut):
    assert auto_dut.get_state() == 'debug'
