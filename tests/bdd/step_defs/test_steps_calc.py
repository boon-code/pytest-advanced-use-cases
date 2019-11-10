import pytest
import munch

import pytest_bdd
from pytest_bdd import given, when, then
from pytest_bdd.parsers import parse


pytest_bdd.scenarios('../features/calculator.feature')


@pytest.fixture()
def result_store():
    return munch.Munch()


@given("Bla")
def bla():
    pass


@when(parse("Values are <A> and <B>"))
def bla_values(result_store, A, B):
    result_store.result = int(A) + int(B)


@then(parse("Result is <R>"))
def bla_result(result_store, R):
    assert int(R) == result_store.result
