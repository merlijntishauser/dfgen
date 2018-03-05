import pytest
from dfgen.dockerfile import Dockerfile


def setup():
    pass


def teardown():
    pass


def test_set_linux_type_returns_base_image():
    assert Dockerfile().set_linux_type('alpine') == 'alpine:3.6'


def test_set_command_splits_string_at_spaces():
    dockerfile = Dockerfile()
    dockerfile.set_command("should --be --splitted")
    assert dockerfile.template_variables["command"] == ['should', '--be', '--splitted']


def test_set_description():
    dockerfile = Dockerfile()
    dockerfile.set_description("a description")
    dockerfile.render_template()
    assert 'org.label-schema.description="a description"' == dockerfile.labels["description"]


def test_setting_description_sets_default_labels():
    dockerfile = Dockerfile()
    dockerfile.set_description("a description")
    dockerfile.render_template()
    assert 'org.label-schema.schema-version="1.0.0-rc1"' == dockerfile.labels["schema-version"]
