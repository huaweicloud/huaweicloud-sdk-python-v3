# coding: utf-8

import pprint
import re

import six





class MountConfig:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mount_user': 'MountUser',
        'func_mounts': 'list[FuncMount]'
    }

    attribute_map = {
        'mount_user': 'mount_user',
        'func_mounts': 'func_mounts'
    }

    def __init__(self, mount_user=None, func_mounts=None):
        """MountConfig - a model defined in huaweicloud sdk"""
        
        

        self._mount_user = None
        self._func_mounts = None
        self.discriminator = None

        self.mount_user = mount_user
        self.func_mounts = func_mounts

    @property
    def mount_user(self):
        """Gets the mount_user of this MountConfig.


        :return: The mount_user of this MountConfig.
        :rtype: MountUser
        """
        return self._mount_user

    @mount_user.setter
    def mount_user(self, mount_user):
        """Sets the mount_user of this MountConfig.


        :param mount_user: The mount_user of this MountConfig.
        :type: MountUser
        """
        self._mount_user = mount_user

    @property
    def func_mounts(self):
        """Gets the func_mounts of this MountConfig.

        函数挂载列表。

        :return: The func_mounts of this MountConfig.
        :rtype: list[FuncMount]
        """
        return self._func_mounts

    @func_mounts.setter
    def func_mounts(self, func_mounts):
        """Sets the func_mounts of this MountConfig.

        函数挂载列表。

        :param func_mounts: The func_mounts of this MountConfig.
        :type: list[FuncMount]
        """
        self._func_mounts = func_mounts

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
        if not isinstance(other, MountConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
