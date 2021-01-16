# coding: utf-8

import pprint
import re

import six





class NodeOrgs:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'node_count': 'int',
        'pvc_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'node_count': 'node_count',
        'pvc_name': 'pvc_name'
    }

    def __init__(self, name=None, node_count=None, pvc_name=None):
        """NodeOrgs - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._node_count = None
        self._pvc_name = None
        self.discriminator = None

        self.name = name
        self.node_count = node_count
        if pvc_name is not None:
            self.pvc_name = pvc_name

    @property
    def name(self):
        """Gets the name of this NodeOrgs.

        组织名称

        :return: The name of this NodeOrgs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeOrgs.

        组织名称

        :param name: The name of this NodeOrgs.
        :type: str
        """
        self._name = name

    @property
    def node_count(self):
        """Gets the node_count of this NodeOrgs.

        组织目标节点数

        :return: The node_count of this NodeOrgs.
        :rtype: int
        """
        return self._node_count

    @node_count.setter
    def node_count(self, node_count):
        """Sets the node_count of this NodeOrgs.

        组织目标节点数

        :param node_count: The node_count of this NodeOrgs.
        :type: int
        """
        self._node_count = node_count

    @property
    def pvc_name(self):
        """Gets the pvc_name of this NodeOrgs.

        pvc名称，添加组织时需要提供pvc_name

        :return: The pvc_name of this NodeOrgs.
        :rtype: str
        """
        return self._pvc_name

    @pvc_name.setter
    def pvc_name(self, pvc_name):
        """Sets the pvc_name of this NodeOrgs.

        pvc名称，添加组织时需要提供pvc_name

        :param pvc_name: The pvc_name of this NodeOrgs.
        :type: str
        """
        self._pvc_name = pvc_name

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
        if not isinstance(other, NodeOrgs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
