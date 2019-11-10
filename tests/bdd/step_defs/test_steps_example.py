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
    import dummy_mod
    cli_config.cli_class = dummy_mod.DummyCli
    cli_config.params = [cli]


@when(parse('The parameter "{param}" is passed'))
def cli_invoked(cli_config, param):
    cli_config.params.append(param)

@when('No parameter is passed')
def cli_invoked_no_param():
    pass


@then(parse('"{output}" is displayed'))
def check_output(cli_config, output, capsys):
    cli = cli_config.cli_class(cli_config.params)
    cli.run()
    captured = capsys.readouterr()
    assert output == captured.out.rstrip('\n')
