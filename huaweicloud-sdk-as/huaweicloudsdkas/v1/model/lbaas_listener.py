# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LbaasListener:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'listener_id': 'str',
        'pool_id': 'str',
        'protocol_port': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'listener_id': 'listener_id',
        'pool_id': 'pool_id',
        'protocol_port': 'protocol_port',
        'weight': 'weight'
    }

    def __init__(self, listener_id=None, pool_id=None, protocol_port=None, weight=None):
        """LbaasListener

        The model defined in huaweicloud sdk

        :param listener_id: 监听器ID。
        :type listener_id: str
        :param pool_id: 后端云服务器组ID。
        :type pool_id: str
        :param protocol_port: 后端协议端口，指后端云服务器监听的端口。
        :type protocol_port: int
        :param weight: 权重，指后端云服务器分发得到请求的数量比例。
        :type weight: int
        """
        
        

        self._listener_id = None
        self._pool_id = None
        self._protocol_port = None
        self._weight = None
        self.discriminator = None

        if listener_id is not None:
            self.listener_id = listener_id
        if pool_id is not None:
            self.pool_id = pool_id
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if weight is not None:
            self.weight = weight

    @property
    def listener_id(self):
        """Gets the listener_id of this LbaasListener.

        监听器ID。

        :return: The listener_id of this LbaasListener.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this LbaasListener.

        监听器ID。

        :param listener_id: The listener_id of this LbaasListener.
        :type listener_id: str
        """
        self._listener_id = listener_id

    @property
    def pool_id(self):
        """Gets the pool_id of this LbaasListener.

        后端云服务器组ID。

        :return: The pool_id of this LbaasListener.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this LbaasListener.

        后端云服务器组ID。

        :param pool_id: The pool_id of this LbaasListener.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def protocol_port(self):
        """Gets the protocol_port of this LbaasListener.

        后端协议端口，指后端云服务器监听的端口。

        :return: The protocol_port of this LbaasListener.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this LbaasListener.

        后端协议端口，指后端云服务器监听的端口。

        :param protocol_port: The protocol_port of this LbaasListener.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        """Gets the weight of this LbaasListener.

        权重，指后端云服务器分发得到请求的数量比例。

        :return: The weight of this LbaasListener.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this LbaasListener.

        权重，指后端云服务器分发得到请求的数量比例。

        :param weight: The weight of this LbaasListener.
        :type weight: int
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
        if not isinstance(other, LbaasListener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
