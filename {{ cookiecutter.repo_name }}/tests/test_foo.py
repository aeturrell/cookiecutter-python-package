from {{ cookiecutter.project_slug }}.foo import foo
import pytest


def test_foo():
    assert foo("foo") == "foo"
