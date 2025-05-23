# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'weight': 'int',
        'protocol_version': 'str'
    }

    attribute_map = {
        'pool_id': 'pool_id',
        'protocol_port': 'protocol_port',
        'weight': 'weight',
        'protocol_version': 'protocol_version'
    }

    def __init__(self, pool_id=None, protocol_port=None, weight=None, protocol_version=None):
        r"""LbaasListeners

        The model defined in huaweicloud sdk

        :param pool_id: 后端云服务器组ID
        :type pool_id: str
        :param protocol_port: 后端协议号，指后端云服务器监听的端口，取值范围[1,65535]
        :type protocol_port: int
        :param weight: 权重，指后端云服务器经分发得到的请求数量的比例，取值范围[0, 100]。
        :type weight: int
        :param protocol_version: 指定ip协议版本
        :type protocol_version: str
        """
        
        

        self._pool_id = None
        self._protocol_port = None
        self._weight = None
        self._protocol_version = None
        self.discriminator = None

        self.pool_id = pool_id
        self.protocol_port = protocol_port
        self.weight = weight
        if protocol_version is not None:
            self.protocol_version = protocol_version

    @property
    def pool_id(self):
        r"""Gets the pool_id of this LbaasListeners.

        后端云服务器组ID

        :return: The pool_id of this LbaasListeners.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this LbaasListeners.

        后端云服务器组ID

        :param pool_id: The pool_id of this LbaasListeners.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this LbaasListeners.

        后端协议号，指后端云服务器监听的端口，取值范围[1,65535]

        :return: The protocol_port of this LbaasListeners.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this LbaasListeners.

        后端协议号，指后端云服务器监听的端口，取值范围[1,65535]

        :param protocol_port: The protocol_port of this LbaasListeners.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        r"""Gets the weight of this LbaasListeners.

        权重，指后端云服务器经分发得到的请求数量的比例，取值范围[0, 100]。

        :return: The weight of this LbaasListeners.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this LbaasListeners.

        权重，指后端云服务器经分发得到的请求数量的比例，取值范围[0, 100]。

        :param weight: The weight of this LbaasListeners.
        :type weight: int
        """
        self._weight = weight

    @property
    def protocol_version(self):
        r"""Gets the protocol_version of this LbaasListeners.

        指定ip协议版本

        :return: The protocol_version of this LbaasListeners.
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        r"""Sets the protocol_version of this LbaasListeners.

        指定ip协议版本

        :param protocol_version: The protocol_version of this LbaasListeners.
        :type protocol_version: str
        """
        self._protocol_version = protocol_version

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
        if not isinstance(other, LbaasListeners):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
