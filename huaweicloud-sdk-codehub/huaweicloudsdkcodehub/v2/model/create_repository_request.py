#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: JeffreyDin
@license: 
@contact: dingjianfeng15@gmail.com
@software: 
@file: create_repository_request.py
@ide: PyCharm
@time: 2021/5/26 15:17
@desc：
"""

import pprint
import re

import six


class CreateRepositoryRequest:
    sensitive_list = []

    openapi_types = {

        'body': 'CreateRepositoryRequestBody'
    }

    attribute_map = {

        'body': 'body'
    }

    def __init(self, body=None):
        """CreateRepositoryRequest - a model defined in huaweicloud sdk"""

        self._body = None
        self.discriminator = None

        if body is not None:
            self.body = body

    @property
    def body(self):
        """

        :return:
        :rtype: CreateRepositoryRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """

        :param body:
        :type: CreateRepositoryRequestBody
        """
        self._body = body

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
        if not isinstance(other, CreateRepositoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
