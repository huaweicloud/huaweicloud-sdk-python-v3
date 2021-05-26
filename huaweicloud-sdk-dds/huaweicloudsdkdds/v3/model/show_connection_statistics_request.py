# coding: utf-8

import pprint
import re

import six





class ShowConnectionStatisticsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_id': 'node_id'
    }

    def __init__(self, instance_id=None, node_id=None):
        """ShowConnectionStatisticsRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._node_id = None
        self.discriminator = None

        self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowConnectionStatisticsRequest.

        实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this ShowConnectionStatisticsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowConnectionStatisticsRequest.

        实例ID，可以调用“查询实例列表”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this ShowConnectionStatisticsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        """Gets the node_id of this ShowConnectionStatisticsRequest.

        节点ID。 - 如取空值，则默认查询实例下所有允许连接的节点的连接数信息。

        :return: The node_id of this ShowConnectionStatisticsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ShowConnectionStatisticsRequest.

        节点ID。 - 如取空值，则默认查询实例下所有允许连接的节点的连接数信息。

        :param node_id: The node_id of this ShowConnectionStatisticsRequest.
        :type: str
        """
        self._node_id = node_id

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
        if not isinstance(other, ShowConnectionStatisticsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
