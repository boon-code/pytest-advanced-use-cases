import pytest


pytestmark = [pytest.mark.dut_state('default')]


def test_default_state_1(auto_dut):
    assert auto_dut.get_state() == 'default'



def test_default_state_2(auto_dut):
    assert auto_dut.get_state() == 'default'



def test_default_state_3(auto_dut):
    assert auto_dut.get_state() == 'default'
