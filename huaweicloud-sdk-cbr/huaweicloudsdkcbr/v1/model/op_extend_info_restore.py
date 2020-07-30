# coding: utf-8

import pprint
import re

import six





class OpExtendInfoRestore:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'backup_name': 'str',
        'target_resource_id': 'str',
        'target_resource_name': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'backup_name': 'backup_name',
        'target_resource_id': 'target_resource_id',
        'target_resource_name': 'target_resource_name'
    }

    def __init__(self, backup_id=None, backup_name=None, target_resource_id=None, target_resource_name=None):
        """OpExtendInfoRestore - a model defined in huaweicloud sdk"""
        
        

        self._backup_id = None
        self._backup_name = None
        self._target_resource_id = None
        self._target_resource_name = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if backup_name is not None:
            self.backup_name = backup_name
        if target_resource_id is not None:
            self.target_resource_id = target_resource_id
        if target_resource_name is not None:
            self.target_resource_name = target_resource_name

    @property
    def backup_id(self):
        """Gets the backup_id of this OpExtendInfoRestore.

        备份副本ID

        :return: The backup_id of this OpExtendInfoRestore.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this OpExtendInfoRestore.

        备份副本ID

        :param backup_id: The backup_id of this OpExtendInfoRestore.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def backup_name(self):
        """Gets the backup_name of this OpExtendInfoRestore.

        备份名称

        :return: The backup_name of this OpExtendInfoRestore.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """Sets the backup_name of this OpExtendInfoRestore.

        备份名称

        :param backup_name: The backup_name of this OpExtendInfoRestore.
        :type: str
        """
        self._backup_name = backup_name

    @property
    def target_resource_id(self):
        """Gets the target_resource_id of this OpExtendInfoRestore.

        恢复目标资源ID

        :return: The target_resource_id of this OpExtendInfoRestore.
        :rtype: str
        """
        return self._target_resource_id

    @target_resource_id.setter
    def target_resource_id(self, target_resource_id):
        """Sets the target_resource_id of this OpExtendInfoRestore.

        恢复目标资源ID

        :param target_resource_id: The target_resource_id of this OpExtendInfoRestore.
        :type: str
        """
        self._target_resource_id = target_resource_id

    @property
    def target_resource_name(self):
        """Gets the target_resource_name of this OpExtendInfoRestore.

        恢复目标资源名称

        :return: The target_resource_name of this OpExtendInfoRestore.
        :rtype: str
        """
        return self._target_resource_name

    @target_resource_name.setter
    def target_resource_name(self, target_resource_name):
        """Sets the target_resource_name of this OpExtendInfoRestore.

        恢复目标资源名称

        :param target_resource_name: The target_resource_name of this OpExtendInfoRestore.
        :type: str
        """
        self._target_resource_name = target_resource_name

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
        if not isinstance(other, OpExtendInfoRestore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
