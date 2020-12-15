# coding: utf-8

import pprint
import re

import six





class NodeManagement:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_group_reference': 'str'
    }

    attribute_map = {
        'server_group_reference': 'serverGroupReference'
    }

    def __init__(self, server_group_reference=None):
        """NodeManagement - a model defined in huaweicloud sdk"""
        
        

        self._server_group_reference = None
        self.discriminator = None

        if server_group_reference is not None:
            self.server_group_reference = server_group_reference

    @property
    def server_group_reference(self):
        """Gets the server_group_reference of this NodeManagement.

        云服务器组ID，若指定，节点池中所有节点将创建在该云服务器组下，节点池的云服务器组只能在创建时指定，无法修改。指定云服务器组时节点池中的节点数量不允许超出云服务器组的配额限制。 

        :return: The server_group_reference of this NodeManagement.
        :rtype: str
        """
        return self._server_group_reference

    @server_group_reference.setter
    def server_group_reference(self, server_group_reference):
        """Sets the server_group_reference of this NodeManagement.

        云服务器组ID，若指定，节点池中所有节点将创建在该云服务器组下，节点池的云服务器组只能在创建时指定，无法修改。指定云服务器组时节点池中的节点数量不允许超出云服务器组的配额限制。 

        :param server_group_reference: The server_group_reference of this NodeManagement.
        :type: str
        """
        self._server_group_reference = server_group_reference

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
        if not isinstance(other, NodeManagement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
