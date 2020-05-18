# coding: utf-8

import pprint
import re

import six


class BatchUpdateServersNameResponse(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'response': 'list[ServerId]'
    }

    attribute_map = {
        'response': 'response'
    }

    def __init__(self, response=None):  # noqa: E501
        """BatchUpdateServersNameResponse - a model defined in huaweicloud sdk"""

        self._response = None
        self.discriminator = None

        if response is not None:
            self.response = response

    @property
    def response(self):
        """Gets the response of this BatchUpdateServersNameResponse.

        提交请求成功后返回的响应列表。

        :return: The response of this BatchUpdateServersNameResponse.
        :rtype: list[ServerId]
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this BatchUpdateServersNameResponse.

        提交请求成功后返回的响应列表。

        :param response: The response of this BatchUpdateServersNameResponse.
        :type: list[ServerId]
        """
        self._response = response

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
        if not isinstance(other, BatchUpdateServersNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
