# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_ip': 'str',
        'node_name': 'str'
    }

    attribute_map = {
        'node_ip': 'node_ip',
        'node_name': 'node_name'
    }

    def __init__(self, node_ip=None, node_name=None):
        """NodeConfig

        The model defined in huaweicloud sdk

        :param node_ip: 节点IP
        :type node_ip: str
        :param node_name: 节点名称
        :type node_name: str
        """
        
        

        self._node_ip = None
        self._node_name = None
        self.discriminator = None

        if node_ip is not None:
            self.node_ip = node_ip
        if node_name is not None:
            self.node_name = node_name

    @property
    def node_ip(self):
        """Gets the node_ip of this NodeConfig.

        节点IP

        :return: The node_ip of this NodeConfig.
        :rtype: str
        """
        return self._node_ip

    @node_ip.setter
    def node_ip(self, node_ip):
        """Sets the node_ip of this NodeConfig.

        节点IP

        :param node_ip: The node_ip of this NodeConfig.
        :type node_ip: str
        """
        self._node_ip = node_ip

    @property
    def node_name(self):
        """Gets the node_name of this NodeConfig.

        节点名称

        :return: The node_name of this NodeConfig.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        """Sets the node_name of this NodeConfig.

        节点名称

        :param node_name: The node_name of this NodeConfig.
        :type node_name: str
        """
        self._node_name = node_name

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
