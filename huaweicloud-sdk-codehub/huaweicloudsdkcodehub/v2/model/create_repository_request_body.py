#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: JeffreyDin
@license:
@contact: dingjianfeng15@gmail.com
@software:
@file: create_repository_request_body.py
@ide: PyCharm
@time: 2021/5/26 15:17
@desc：
"""

import pprint
import re

import six


class CreateRepositoryRequestBody:

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'enable_readme': 'int',
        'gitignore_id': 'str',
        'import_members': 'int',
        'import_url': 'str',
        'license_id': 'int',
        'name': 'str',
        'project_uuid': 'str',
        'template_id': 'str',
        'visibility_level': 'int'
    }

    attribute_map = {
        'description': 'description',
        'enable_readme': 'enable_readme',
        'gitignore_id': 'gitignore_id',
        'import_members': 'import_members',
        'import_url': 'import_url',
        'license_id': 'license_id',
        'name': 'name',
        'project_uuid': 'project_uuid',
        'template_id': 'template_id',
        'visibility_level': 'visibility_level'
    }

    def __init__(self, name=None, project_uuid=None, description=None,
                 enable_readme=None, gitignore_id=None, import_members=None,
                 import_url=None, license_id=None, template_id=None,
                 visibility_level=None
                 ):
        """CreateRepositoryOption - a model defined in huaweicloud sdk"""

        self._name = None
        self._project_uuid = None
        self._description = None
        self._enable_readme = None
        self._gitignore_id = None
        self._import_members = None
        self._import_url = None
        self._license_id = None
        self._template_id = None
        self._visibility_level = None
        self.discriminator = None

        self.name = name
        self.project_uuid = project_uuid

        if description is not None:
            self.description = description
        if enable_readme is not None:
            self.enable_readme = enable_readme
        if gitignore_id is not None:
            self.gitignore_id = gitignore_id
        if import_members is not None:
            self.import_members = import_members
        if import_url is not None:
            self.import_url = import_url
        if license_id is not None:
            self.license_id = license_id
        if template_id is not None:
            self.template_id = template_id
        if visibility_level is not None:
            self.visibility_level = visibility_level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def project_uuid(self):
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        self._project_uuid = project_uuid

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def enable_readme(self):
        return self._enable_readme

    @enable_readme.setter
    def enable_readme(self, enable_readme):
        self._enable_readme = enable_readme

    @property
    def gitignore_id(self):
        return self._gitignore_id

    @gitignore_id.setter
    def gitignore_id(self, gitignore_id):
        self._gitignore_id = gitignore_id


    @property
    def import_members(self):
        return self._import_members

    @import_members.setter
    def import_members(self, import_members):
        self._import_members = import_members

    @property
    def import_url(self):
        return self._import_url

    @import_url.setter
    def import_url(self, import_url):
        self._import_url = import_url

    @property
    def license_id(self):
        return self._license_id

    @license_id.setter
    def license_id(self, license_id):
        self._license_id = license_id

    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        self._template_id = template_id

    @property
    def visibility_level(self):
        return self._visibility_level

    @visibility_level.setter
    def visibility_level(self, visibility_level):
        self._visibility_level = visibility_level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRepositoryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
