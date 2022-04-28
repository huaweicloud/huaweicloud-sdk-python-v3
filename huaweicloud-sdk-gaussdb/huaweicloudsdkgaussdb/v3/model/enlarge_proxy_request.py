# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnlargeProxyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_num': 'int',
        'proxy_id': 'str'
    }

    attribute_map = {
        'node_num': 'node_num',
        'proxy_id': 'proxy_id'
    }

    def __init__(self, node_num=None, proxy_id=None):
        """EnlargeProxyRequest

        The model defined in huaweicloud sdk

        :param node_num: proxy节点扩容操作需要扩容的节点数。本次扩容的节点数的取值范围：1~30之间的整数。 限制条件：该实例的proxy节点的总数量小于等于32。
        :type node_num: int
        :param proxy_id: 数据库代理id。 如果实例只开启了一个代理，可不传该参数；如果实例开启了多个代理，则必须指定一个数据库代理，扩容新的代理节点。。
        :type proxy_id: str
        """
        
        

        self._node_num = None
        self._proxy_id = None
        self.discriminator = None

        self.node_num = node_num
        if proxy_id is not None:
            self.proxy_id = proxy_id

    @property
    def node_num(self):
        """Gets the node_num of this EnlargeProxyRequest.

        proxy节点扩容操作需要扩容的节点数。本次扩容的节点数的取值范围：1~30之间的整数。 限制条件：该实例的proxy节点的总数量小于等于32。

        :return: The node_num of this EnlargeProxyRequest.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this EnlargeProxyRequest.

        proxy节点扩容操作需要扩容的节点数。本次扩容的节点数的取值范围：1~30之间的整数。 限制条件：该实例的proxy节点的总数量小于等于32。

        :param node_num: The node_num of this EnlargeProxyRequest.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def proxy_id(self):
        """Gets the proxy_id of this EnlargeProxyRequest.

        数据库代理id。 如果实例只开启了一个代理，可不传该参数；如果实例开启了多个代理，则必须指定一个数据库代理，扩容新的代理节点。。

        :return: The proxy_id of this EnlargeProxyRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        """Sets the proxy_id of this EnlargeProxyRequest.

        数据库代理id。 如果实例只开启了一个代理，可不传该参数；如果实例开启了多个代理，则必须指定一个数据库代理，扩容新的代理节点。。

        :param proxy_id: The proxy_id of this EnlargeProxyRequest.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

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
        if not isinstance(other, EnlargeProxyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
