# coding: utf-8

import pprint
import re

import six





class AttachInternalIpRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'new_ip': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'new_ip': 'new_ip'
    }

    def __init__(self, node_id=None, new_ip=None):
        """AttachInternalIpRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._node_id = None
        self._new_ip = None
        self.discriminator = None

        self.node_id = node_id
        self.new_ip = new_ip

    @property
    def node_id(self):
        """Gets the node_id of this AttachInternalIpRequestBody.

        节点ID。

        :return: The node_id of this AttachInternalIpRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this AttachInternalIpRequestBody.

        节点ID。

        :param node_id: The node_id of this AttachInternalIpRequestBody.
        :type: str
        """
        self._node_id = node_id

    @property
    def new_ip(self):
        """Gets the new_ip of this AttachInternalIpRequestBody.

        新的Ip需要为用户可用vpc中的网段。只支持IPV4。

        :return: The new_ip of this AttachInternalIpRequestBody.
        :rtype: str
        """
        return self._new_ip

    @new_ip.setter
    def new_ip(self, new_ip):
        """Sets the new_ip of this AttachInternalIpRequestBody.

        新的Ip需要为用户可用vpc中的网段。只支持IPV4。

        :param new_ip: The new_ip of this AttachInternalIpRequestBody.
        :type: str
        """
        self._new_ip = new_ip

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
        if not isinstance(other, AttachInternalIpRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
