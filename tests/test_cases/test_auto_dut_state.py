import pytest
from ..fixtures import *


@pytest.mark.dut_state("debug")
def test_running_dbg_1(auto_dut):
    assert auto_dut.get_state() == 'debug'


@pytest.mark.dut_state("debug")
def test_running_dbg_2(auto_dut):
    assert auto_dut.get_state() == 'debug'


@pytest.mark.dut_state("default")
def test_running_normal_1(auto_dut):
    auto_dut.params.test = 2
    assert auto_dut.get_state() == 'default'


@pytest.mark.dut_state("debug")
def test_running_dbg_3(auto_dut):
    auto_dut.params.bla = 12
    assert auto_dut.get_state() == 'debug'


@pytest.mark.dut_state("default")
def test_running_normal_2(auto_dut):
    auto_dut.params.hui = 7
    assert auto_dut.get_state() == 'default'


@pytest.mark.dut_state("default")
def test_running_normal_3(auto_dut):
    auto_dut.params.test = 3
    assert auto_dut.get_state() == 'default'


def test_no_state_set_1(auto_dut):
    auto_dut.params.state = 27
    assert auto_dut.get_state() is None


def test_no_state_set_2(auto_dut):
    auto_dut.params.state = 27
    assert auto_dut.get_state() is None


@pytest.mark.dut_state("default")
def test_default_state_again(auto_dut):
    auto_dut.params.var = 2
    assert auto_dut.get_state() == 'default'
