# coding: utf-8

import pprint
import re

import six





class BackupRestore:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mappings': 'list[BackupRestoreServerMapping]',
        'power_on': 'bool',
        'server_id': 'str',
        'volume_id': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'mappings': 'mappings',
        'power_on': 'power_on',
        'server_id': 'server_id',
        'volume_id': 'volume_id',
        'resource_id': 'resource_id'
    }

    def __init__(self, mappings=None, power_on=True, server_id=None, volume_id=None, resource_id=None):
        """BackupRestore - a model defined in huaweicloud sdk"""
        
        

        self._mappings = None
        self._power_on = None
        self._server_id = None
        self._volume_id = None
        self._resource_id = None
        self.discriminator = None

        if mappings is not None:
            self.mappings = mappings
        if power_on is not None:
            self.power_on = power_on
        if server_id is not None:
            self.server_id = server_id
        if volume_id is not None:
            self.volume_id = volume_id
        if resource_id is not None:
            self.resource_id = resource_id

    @property
    def mappings(self):
        """Gets the mappings of this BackupRestore.

        恢复的映射关系(整机恢复时必填，卷恢复时可选但是不会用到填写的值）

        :return: The mappings of this BackupRestore.
        :rtype: list[BackupRestoreServerMapping]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this BackupRestore.

        恢复的映射关系(整机恢复时必填，卷恢复时可选但是不会用到填写的值）

        :param mappings: The mappings of this BackupRestore.
        :type: list[BackupRestoreServerMapping]
        """
        self._mappings = mappings

    @property
    def power_on(self):
        """Gets the power_on of this BackupRestore.

        恢复后是否开始，默认开机。

        :return: The power_on of this BackupRestore.
        :rtype: bool
        """
        return self._power_on

    @power_on.setter
    def power_on(self, power_on):
        """Sets the power_on of this BackupRestore.

        恢复后是否开始，默认开机。

        :param power_on: The power_on of this BackupRestore.
        :type: bool
        """
        self._power_on = power_on

    @property
    def server_id(self):
        """Gets the server_id of this BackupRestore.

        恢复的目标虚拟机ID（整机恢复时必填）

        :return: The server_id of this BackupRestore.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this BackupRestore.

        恢复的目标虚拟机ID（整机恢复时必填）

        :param server_id: The server_id of this BackupRestore.
        :type: str
        """
        self._server_id = server_id

    @property
    def volume_id(self):
        """Gets the volume_id of this BackupRestore.

        恢复的目标卷ID（卷恢复时必填）

        :return: The volume_id of this BackupRestore.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this BackupRestore.

        恢复的目标卷ID（卷恢复时必填）

        :param volume_id: The volume_id of this BackupRestore.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def resource_id(self):
        """Gets the resource_id of this BackupRestore.

        待恢复的目标资源ID

        :return: The resource_id of this BackupRestore.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BackupRestore.

        待恢复的目标资源ID

        :param resource_id: The resource_id of this BackupRestore.
        :type: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, BackupRestore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
