from .fixtures import *

def pytest_configure(config):
    markers = [
        ("dut_state(state)", "Require a specific DuT state (string)"),
    ]
    for name, desc in markers:
        line = "{0}: {1}".format(name, desc)
        config.addinivalue_line("markers", line)
