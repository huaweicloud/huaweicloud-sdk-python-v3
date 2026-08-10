#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: JeffreyDin
@license: 
@contact: dingjianfeng15@gmail.com
@software: 
@file: codehub_result.py
@ide: PyCharm
@time: 2021/6/2 18:48
@desc：
"""

import pprint
import re

import six


class CodeHubResult:
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'repositories': 'list[CodeHubRepositories]'
    }

    attribute_map = {
        'total': 'total',
        'repositories': 'repositories',
    }

    def __init__(self, total=None, repositories=None):
        """CodeHubResult - a model defined in huaweicloud sdk"""

        self._total = None
        self._repositories = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if repositories is not None:
            self.repositories = repositories

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, total):
        self._total = total

    @property
    def repositories(self):
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        self._repositories = repositories

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
        if not isinstance(other, CodeHubResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other