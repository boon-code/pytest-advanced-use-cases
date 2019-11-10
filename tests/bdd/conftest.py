

def pytest_configure(config):
    config.addinivalue_line("markers", "bdd_example: Acceptance test examples using BDD")
