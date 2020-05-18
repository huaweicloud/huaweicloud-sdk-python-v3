# coding: utf-8

import pprint
import re

import six


class NovaSnapshotServerOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'name': 'str',
        'metadata': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'metadata': 'metadata'
    }

    def __init__(self, name=None, metadata=None):  # noqa: E501
        """NovaSnapshotServerOption - a model defined in huaweicloud sdk"""

        self._name = None
        self._metadata = None
        self.discriminator = None

        self.name = name
        if metadata is not None:
            self.metadata = metadata

    @property
    def name(self):
        """Gets the name of this NovaSnapshotServerOption.

        镜像名称，长度大于0小于243字节

        :return: The name of this NovaSnapshotServerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NovaSnapshotServerOption.

        镜像名称，长度大于0小于243字节

        :param name: The name of this NovaSnapshotServerOption.
        :type: str
        """
        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this NovaSnapshotServerOption.

        镜像属性，属性名称的长度大于0小于255字节

        :return: The metadata of this NovaSnapshotServerOption.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this NovaSnapshotServerOption.

        镜像属性，属性名称的长度大于0小于255字节

        :param metadata: The metadata of this NovaSnapshotServerOption.
        :type: dict(str, str)
        """
        self._metadata = metadata

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
        if not isinstance(other, NovaSnapshotServerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
