# coding: utf-8

import pprint
import re

import six





class VaultMigrateResourceReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'destination_vault_id': 'str',
        'resource_ids': 'list[str]'
    }

    attribute_map = {
        'destination_vault_id': 'destination_vault_id',
        'resource_ids': 'resource_ids'
    }

    def __init__(self, destination_vault_id=None, resource_ids=None):
        """VaultMigrateResourceReq - a model defined in huaweicloud sdk"""
        
        

        self._destination_vault_id = None
        self._resource_ids = None
        self.discriminator = None

        self.destination_vault_id = destination_vault_id
        self.resource_ids = resource_ids

    @property
    def destination_vault_id(self):
        """Gets the destination_vault_id of this VaultMigrateResourceReq.

        目标存储库

        :return: The destination_vault_id of this VaultMigrateResourceReq.
        :rtype: str
        """
        return self._destination_vault_id

    @destination_vault_id.setter
    def destination_vault_id(self, destination_vault_id):
        """Sets the destination_vault_id of this VaultMigrateResourceReq.

        目标存储库

        :param destination_vault_id: The destination_vault_id of this VaultMigrateResourceReq.
        :type: str
        """
        self._destination_vault_id = destination_vault_id

    @property
    def resource_ids(self):
        """Gets the resource_ids of this VaultMigrateResourceReq.

        待迁移的资源ID

        :return: The resource_ids of this VaultMigrateResourceReq.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        """Sets the resource_ids of this VaultMigrateResourceReq.

        待迁移的资源ID

        :param resource_ids: The resource_ids of this VaultMigrateResourceReq.
        :type: list[str]
        """
        self._resource_ids = resource_ids

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
        if not isinstance(other, VaultMigrateResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
