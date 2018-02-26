import pytest
from gener8.dockerfile import Dockerfile


def setup():
    pass


def teardown():
    pass


def test_set_linux_type_returns_base_image():
    assert Dockerfile().set_linux_type('alpine') == 'alpine:3.6'
