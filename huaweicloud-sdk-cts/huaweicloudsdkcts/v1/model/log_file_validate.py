# coding: utf-8

import pprint
import re

import six


class LogFileValidate(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'is_support_validate': 'bool'
    }

    attribute_map = {
        'is_support_validate': 'is_support_validate'
    }

    def __init__(self, is_support_validate=None):  # noqa: E501
        """LogFileValidate - a model defined in huaweicloud sdk"""

        self._is_support_validate = None
        self.discriminator = None

        self.is_support_validate = is_support_validate

    @property
    def is_support_validate(self):
        """Gets the is_support_validate of this LogFileValidate.

        是否打开事件文件校验。

        :return: The is_support_validate of this LogFileValidate.
        :rtype: bool
        """
        return self._is_support_validate

    @is_support_validate.setter
    def is_support_validate(self, is_support_validate):
        """Sets the is_support_validate of this LogFileValidate.

        是否打开事件文件校验。

        :param is_support_validate: The is_support_validate of this LogFileValidate.
        :type: bool
        """
        self._is_support_validate = is_support_validate

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
        if not isinstance(other, LogFileValidate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
