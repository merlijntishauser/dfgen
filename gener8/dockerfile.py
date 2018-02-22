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
        "docker_image": '',
        "labels": '',
        "enable_package_manager": False,
        "package_manager_type": ''
    }

    labels = {}

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def set_linux_type(self, linux_type):
        self.linux_type = linux_type
        return self.base_defaults[linux_type]

    def set_base_image(self, docker_image):
        self.template_variables["docker_image"] = docker_image

    def set_maintainer(self, maintainer):
        if maintainer is not '':
            self.labels["maintainer"] = 'maintainer=' + maintainer

    def set_description(self, description):
        if description is not '':
            self.labels["description"] = 'org.label-schema.description="' + description + '"'

    def _set_labels(self):
        if len(self.labels) > 0:
            self.template_variables["labels"] = " \\\n\t".join(self.labels.values())

    def set_package_manager(self, add_package_manager):
        if add_package_manager == 'yes':
            self.template_variables["enable_package_manager"] = True
            self.template_variables["package_manager_type"] = 'apt-get'
            if self.linux_type == 'alpine':
                self.template_variables["package_manager_type"] = 'apk'

    def render_template(self):
        jinja_environment = Environment(
            loader=PackageLoader('gener8', 'templates/docker'),
            trim_blocks=True,
            keep_trailing_newline=True,
            undefined=StrictUndefined
        )

        try:
            self._set_labels()
            return jinja_environment.get_template('%s.jinja2' % self.template_name).render(self.template_variables)
        except UndefinedError as e:
            self.logger.error("Required template variable missing: " + str(e))

    def write_template(self):
        file_actions = FileActions(path='output')
        return file_actions.write_file('Dockerfile', self.render_template())
