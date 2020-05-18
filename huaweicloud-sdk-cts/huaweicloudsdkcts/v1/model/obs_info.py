# coding: utf-8

import pprint
import re

import six


class ObsInfo(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'bucket_name': 'str',
        'file_prefix_name': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'file_prefix_name': 'file_prefix_name'
    }

    def __init__(self, bucket_name=None, file_prefix_name=None):  # noqa: E501
        """ObsInfo - a model defined in huaweicloud sdk"""

        self._bucket_name = None
        self._file_prefix_name = None
        self.discriminator = None

        if bucket_name is not None:
            self.bucket_name = bucket_name
        if file_prefix_name is not None:
            self.file_prefix_name = file_prefix_name

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ObsInfo.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :return: The bucket_name of this ObsInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ObsInfo.

        标识OBS桶名称。由数字或字母开头，支持小写字母、数字、“-”、“.”，长度为3～63个字符。

        :param bucket_name: The bucket_name of this ObsInfo.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def file_prefix_name(self):
        """Gets the file_prefix_name of this ObsInfo.

        标识需要存储于OBS的日志文件前缀，0-9，a-z，A-Z，'-'，'.'，'_'长度为0～64字符。

        :return: The file_prefix_name of this ObsInfo.
        :rtype: str
        """
        return self._file_prefix_name

    @file_prefix_name.setter
    def file_prefix_name(self, file_prefix_name):
        """Sets the file_prefix_name of this ObsInfo.

        标识需要存储于OBS的日志文件前缀，0-9，a-z，A-Z，'-'，'.'，'_'长度为0～64字符。

        :param file_prefix_name: The file_prefix_name of this ObsInfo.
        :type: str
        """
        self._file_prefix_name = file_prefix_name

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
        if not isinstance(other, ObsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
