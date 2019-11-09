import pytest
import munch

import pytest_bdd
from pytest_bdd import given, when, then
from pytest_bdd.parsers import parse


pytest_bdd.scenarios('../features/hello-world.feature')


@pytest.fixture()
def cli_config():
    return munch.Munch()


@given(parse('{cli} is started'))
def some_cli(cli_config, cli):
    cli_config.prog = cli


@when(parse('The parameter {param} is passed'))
def cli_invoked(cli_config, param):
    cli_config.param = param


@then(parse('"{output}" is displayed'))
def check_output(cli_config, output):
    assert cli_config.prog == 'example-cli'
    assert cli_config.param == '--greet'
    assert output == 'Hello, world'
