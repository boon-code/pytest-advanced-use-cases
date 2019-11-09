import pytest
from ..fixtures import *


def test_running_dbg_1(dut_debug):
    assert dut_debug.get_state() == 'debug'


def test_running_dbg_2(dut_debug):
    assert dut_debug.get_state() == 'debug'


def test_running_normal_1(dut_default):
    dut_default.params.test = 2
    assert dut_default.get_state() == 'default'


def test_running_dbg_3(dut_debug):
    dut_debug.params.bla = 12
    assert dut_debug.get_state() == 'debug'


def test_running_normal_2(dut_default):
    dut_default.params.hui = 7
    assert dut_default.get_state() == 'default'
