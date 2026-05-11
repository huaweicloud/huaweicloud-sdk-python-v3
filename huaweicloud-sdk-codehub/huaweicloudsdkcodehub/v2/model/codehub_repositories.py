#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: JeffreyDin
@license: 
@contact: dingjianfeng15@gmail.com
@software: 
@file: codehub_repositories.py
@ide: PyCharm
@time: 2021/6/2 18:49
@desc：
"""
import pprint
import re
from typing import Any

import six


class CodeHubRepositories:
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'creator_name': 'str',
        'domain_name': 'str',
        'group_name': 'str',
        'https_url': 'str',
        'iam_user_uuid': 'str',
        'is_owner': 'int',
        'lfs_size': 'str',
        'project_is_deleted': 'str',
        'project_uuid': 'str',
        'repository_id': 'int',
        'repository_name': 'str',
        'repository_size': 'str',
        'repository_uuid': 'str',
        'ssh_url': 'str',
        'star': 'bool',
        'status': 'int',
        'updated_at': 'str',
        'userRole': 'int',
        'visibility_level': 'int',
        'web_url': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'creator_name': 'creator_name',
        'domain_name': 'domain_name',
        'group_name': 'group_name',
        'https_url': 'https_url',
        'iam_user_uuid': 'iam_user_uuid',
        'is_owner': 'is_owner',
        'lfs_size': 'lfs_size',
        'project_is_deleted': 'project_is_deleted',
        'project_uuid': 'project_uuid',
        'repository_id': 'repository_id',
        'repository_name': 'repository_name',
        'repository_size': 'repository_size',
        'repository_uuid': 'repository_uuid',
        'ssh_url': 'ssh_url',
        'star': 'star',
        'status': 'status',
        'updated_at': 'updated_at',
        'userRole': 'userRole',
        'visibility_level': 'visibility_level',
        'web_url': 'web_url'
    }

    def __init__(self, created_at=None, creator_name=None, domain_name=None, group_name=None, https_url=None,
                 iam_user_uuid=None, is_owner=None, lfs_size=None, project_is_deleted=None, project_uuid=None,
                 repository_id=None, repository_name=None, repository_size=None, repository_uuid=None, ssh_url=None,
                 star=None, status=None, updated_at=None, userRole=None, visibility_level=None, web_url=None):
        """CodeHubRepositories - a model defined in huaweicloud sdk"""

        self._created_at = None
        self._creator_name = None
        self._domain_name = None
        self._group_name = None
        self._https_url = None

        self._iam_user_uuid = None
        self._is_owner = None
        self._lfs_size = None
        self._project_is_deleted = None
        self._project_uuid = None

        self._repository_id = None
        self._repository_name = None
        self._repository_size = None
        self._repository_uuid = None
        self._ssh_url = None

        self._star = None
        self._status = None
        self._updated_at = None
        self._userRole = None
        self._visibility_level = None
        self._web_url = None


        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if creator_name is not None:
            self.creator_name = creator_name
        if domain_name is not None:
            self.domain_name = domain_name
        if group_name is not None:
            self.group_name = group_name
        if https_url is not None:
            self.https_url = https_url

        if iam_user_uuid is not None:
            self.iam_user_uuid = iam_user_uuid
        if is_owner is not None:
            self.is_owner = is_owner
        if lfs_size is not None:
            self.lfs_size = lfs_size
        if project_is_deleted is not None:
            self.project_is_deleted = project_is_deleted
        if project_uuid is not None:
            self.project_uuid = project_uuid

        if repository_id is not None:
            self.repository_id = repository_id
        if repository_name is not None:
            self.repository_name = repository_name
        if repository_size is not None:
            self.repository_size = repository_size
        if repository_uuid is not None:
            self.repository_uuid = repository_uuid
        if ssh_url is not None:
            self.ssh_url = ssh_url

        if star is not None:
            self.star = star
        if status is not None:
            self.status = status
        if updated_at is not None:
            self.updated_at = updated_at
        if userRole is not None:
            self.userRole = userRole
        if visibility_level is not None:
            self.visibility_level = visibility_level
        if web_url is not None:
            self.web_url = web_url

    @property
    def userRole(self):
        return self._userRole

    @userRole.setter
    def userRole(self, userRole):
        self._userRole = userRole


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
        if not isinstance(other, CodeHubRepositories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other