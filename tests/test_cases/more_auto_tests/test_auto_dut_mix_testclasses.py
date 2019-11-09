import pytest


class TestDebugCases(object):
    pytestmark = [pytest.mark.dut_state('debug')]

    def test_debug_1(self, auto_dut):
        assert auto_dut.get_state() == 'debug'

    def test_debug_2(self, auto_dut):
        assert auto_dut.get_state() == 'debug'

    def test_debug_3(self, auto_dut):
        assert auto_dut.get_state() == 'debug'


def test_no_marker_1(auto_dut):
    assert auto_dut.get_state() is None


@pytest.mark.dut_state("off")
def test_dut_off_test(auto_dut):
    assert auto_dut.get_state() == 'off'


class TestDefaultCases(object):
    pytestmark = [pytest.mark.dut_state('default')]

    def test_default_1(self, auto_dut):
        assert auto_dut.get_state() == 'default'

    def test_default_2(self, auto_dut):
        assert auto_dut.get_state() == 'default'

    def test_default_3(self, auto_dut):
        assert auto_dut.get_state() == 'default'


def test_no_marker_2(auto_dut):
    assert auto_dut.get_state() is None