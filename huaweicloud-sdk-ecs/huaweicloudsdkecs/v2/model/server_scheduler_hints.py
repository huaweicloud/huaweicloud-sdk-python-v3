# coding: utf-8

import pprint
import re

import six


class ServerSchedulerHints(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group': 'list[str]',
        'different_host': 'list[str]',
        'same_host': 'list[str]'
    }

    attribute_map = {
        'group': 'group',
        'different_host': 'different_host',
        'same_host': 'same_host'
    }

    def __init__(self, group=None, different_host=None, same_host=None):  # noqa: E501
        """ServerSchedulerHints - a model defined in huaweicloud sdk"""

        self._group = None
        self._different_host = None
        self._same_host = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if different_host is not None:
            self.different_host = different_host
        if same_host is not None:
            self.same_host = same_host

    @property
    def group(self):
        """Gets the group of this ServerSchedulerHints.

        反亲和性组信息。  UUID格式。

        :return: The group of this ServerSchedulerHints.
        :rtype: list[str]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ServerSchedulerHints.

        反亲和性组信息。  UUID格式。

        :param group: The group of this ServerSchedulerHints.
        :type: list[str]
        """
        self._group = group

    @property
    def different_host(self):
        """Gets the different_host of this ServerSchedulerHints.

        与指定弹性云服务器满足反亲和性。当前不支持该功能。

        :return: The different_host of this ServerSchedulerHints.
        :rtype: list[str]
        """
        return self._different_host

    @different_host.setter
    def different_host(self, different_host):
        """Sets the different_host of this ServerSchedulerHints.

        与指定弹性云服务器满足反亲和性。当前不支持该功能。

        :param different_host: The different_host of this ServerSchedulerHints.
        :type: list[str]
        """
        self._different_host = different_host

    @property
    def same_host(self):
        """Gets the same_host of this ServerSchedulerHints.

        与指定的弹性云服务器满足亲和性。当前不支持该功能。

        :return: The same_host of this ServerSchedulerHints.
        :rtype: list[str]
        """
        return self._same_host

    @same_host.setter
    def same_host(self, same_host):
        """Sets the same_host of this ServerSchedulerHints.

        与指定的弹性云服务器满足亲和性。当前不支持该功能。

        :param same_host: The same_host of this ServerSchedulerHints.
        :type: list[str]
        """
        self._same_host = same_host

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
        if not isinstance(other, ServerSchedulerHints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
