# coding: utf-8

import pprint
import re

import six





class LbaasListeners:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pool_id': 'str',
        'protocol_port': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'protocol_port': 'protocol_port',
        'weight': 'weight'
    }

    def __init__(self, pool_id=None, protocol_port=None, weight=None):
        """LbaasListeners - a model defined in huaweicloud sdk"""
        
        

        self._pool_id = None
        self._protocol_port = None
        self._weight = None
        self.discriminator = None

        self.pool_id = pool_id
        self.protocol_port = protocol_port
        if weight is not None:
            self.weight = weight

    @property
    def pool_id(self):
        """Gets the pool_id of this LbaasListeners.

        后端云服务器组ID

        :return: The pool_id of this LbaasListeners.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this LbaasListeners.

        后端云服务器组ID

        :param pool_id: The pool_id of this LbaasListeners.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def protocol_port(self):
        """Gets the protocol_port of this LbaasListeners.

        后端协议号，指后端云服务器监听的端口，取值范围[1,65535]

        :return: The protocol_port of this LbaasListeners.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this LbaasListeners.

        后端协议号，指后端云服务器监听的端口，取值范围[1,65535]

        :param protocol_port: The protocol_port of this LbaasListeners.
        :type: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        """Gets the weight of this LbaasListeners.

        权重，指后端云服务器经分发得到的请求数量比例，取值范围[0,1]，默认为1。

        :return: The weight of this LbaasListeners.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this LbaasListeners.

        权重，指后端云服务器经分发得到的请求数量比例，取值范围[0,1]，默认为1。

        :param weight: The weight of this LbaasListeners.
        :type: int
        """
        self._weight = weight

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
        if not isinstance(other, LbaasListeners):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
