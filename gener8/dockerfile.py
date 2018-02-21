import logging
from jinja2 import Environment, PackageLoader, BaseLoader, meta, StrictUndefined
from jinja2.exceptions import UndefinedError
from gener8.file_actions import FileActions


class Dockerfile:

    linux_type = 'alpine'
    base_defaults = {
        'alpine': 'alpine:3.6',
        'ubuntu': 'ubuntu:16.04',
        'debian': 'debian:buster'
    }
    template_name = 'Dockerfile'

    template_variables = {
        "docker_image": ''
    }

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def set_linux_type(self, linux_type):
        self.linux_type = linux_type
        return self.base_defaults[linux_type]

    def set_base_image(self, docker_image):
        self.template_variables["docker_image"] = docker_image

    def render_template(self):
        jinja_environment = Environment(
            loader=PackageLoader('gener8', 'templates/docker'),
            trim_blocks=True,
            keep_trailing_newline=True,
            undefined=StrictUndefined
        )

        try:
            return jinja_environment.get_template('%s.jinja2' % self.template_name).render(self.template_variables)
        except UndefinedError as e:
            self.logger.error("Required template variable missing: " + str(e))

    def write_template(self):
        file_actions = FileActions(path='output')
        file_actions.write_file('Dockerfile', self.render_template())
