#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: JeffreyDin
@license: 
@contact: dingjianfeng15@gmail.com
@software: 
@file: get_all_repository_by_projectid_request.py
@ide: PyCharm
@time: 2021/6/2 16:44
@desc：
"""
import pprint
import re

import six


class GetAllRepositoryByProjectId2Request:
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'page_index': 'int',
        'page_size': 'int',
        'search': 'str',
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'page_index': 'page_index',
        'page_size': 'page_size',
        'search': 'search'
    }

    def __init(self, project_uuid=None, page_index=None, page_size=None, search=None):
        """GetAllRepositoryByProjectId2Request - a model defined in huaweicloud sdk"""

        self._project_uuid = None
        self._page_index = None
        self._page_size = None
        self._search = None
        self.discriminator = None

        if page_index is not None:
            self.page_index = page_index
        if page_size is not None:
            self.page_size = page_size
        if search is not None:
            self.search = search
        self.project_uuid = project_uuid

    @property
    def project_uuid(self):
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        self._project_uuid = project_uuid

    @property
    def page_index(self):
        return self._page_index

    @page_index.setter
    def page_index(self, page_index):
        self._page_index = page_index

    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        self._page_size = page_size

    @property
    def search(self):
        return self._search

    @search.setter
    def search(self, search):
        self._search = search

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
        if not isinstance(other, GetAllRepositoryByProjectId2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
