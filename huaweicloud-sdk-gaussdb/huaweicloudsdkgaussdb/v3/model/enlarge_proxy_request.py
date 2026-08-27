# coding: utf-8

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
        'proxy_id': 'str',
        'proxy_nodes_az_list': 'list[str]'
    }

    attribute_map = {
        'node_num': 'node_num',
        'proxy_id': 'proxy_id',
        'proxy_nodes_az_list': 'proxy_nodes_az_list'
    }

    def __init__(self, node_num=None, proxy_id=None, proxy_nodes_az_list=None):
        r"""EnlargeProxyRequest

        The model defined in huaweicloud sdk

        :param node_num: proxy节点扩容操作需要扩容的节点数。  扩容的节点数的取值范围：1~30之间的整数。  限制条件：该实例的proxy节点的总数量小于等于32。
        :type node_num: int
        :param proxy_id: 数据库代理ID。  如果实例只开启了一个代理，可不传该参数；如果实例开启了多个代理，则必须指定一个数据库代理，扩容新的代理节点。
        :type proxy_id: str
        :param proxy_nodes_az_list: **参数解释**：  数据库代理节点的可用区设置。  **约束限制**：  不传该字段，代理节点可用区将随机设置，优先与数据库节点可用区保持一致；传入该字段，代理节点将设置在指定可用区。
        :type proxy_nodes_az_list: list[str]
        """
        
        

        self._node_num = None
        self._proxy_id = None
        self._proxy_nodes_az_list = None
        self.discriminator = None

        self.node_num = node_num
        if proxy_id is not None:
            self.proxy_id = proxy_id
        if proxy_nodes_az_list is not None:
            self.proxy_nodes_az_list = proxy_nodes_az_list

    @property
    def node_num(self):
        r"""Gets the node_num of this EnlargeProxyRequest.

        proxy节点扩容操作需要扩容的节点数。  扩容的节点数的取值范围：1~30之间的整数。  限制条件：该实例的proxy节点的总数量小于等于32。

        :return: The node_num of this EnlargeProxyRequest.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this EnlargeProxyRequest.

        proxy节点扩容操作需要扩容的节点数。  扩容的节点数的取值范围：1~30之间的整数。  限制条件：该实例的proxy节点的总数量小于等于32。

        :param node_num: The node_num of this EnlargeProxyRequest.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this EnlargeProxyRequest.

        数据库代理ID。  如果实例只开启了一个代理，可不传该参数；如果实例开启了多个代理，则必须指定一个数据库代理，扩容新的代理节点。

        :return: The proxy_id of this EnlargeProxyRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this EnlargeProxyRequest.

        数据库代理ID。  如果实例只开启了一个代理，可不传该参数；如果实例开启了多个代理，则必须指定一个数据库代理，扩容新的代理节点。

        :param proxy_id: The proxy_id of this EnlargeProxyRequest.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def proxy_nodes_az_list(self):
        r"""Gets the proxy_nodes_az_list of this EnlargeProxyRequest.

        **参数解释**：  数据库代理节点的可用区设置。  **约束限制**：  不传该字段，代理节点可用区将随机设置，优先与数据库节点可用区保持一致；传入该字段，代理节点将设置在指定可用区。

        :return: The proxy_nodes_az_list of this EnlargeProxyRequest.
        :rtype: list[str]
        """
        return self._proxy_nodes_az_list

    @proxy_nodes_az_list.setter
    def proxy_nodes_az_list(self, proxy_nodes_az_list):
        r"""Sets the proxy_nodes_az_list of this EnlargeProxyRequest.

        **参数解释**：  数据库代理节点的可用区设置。  **约束限制**：  不传该字段，代理节点可用区将随机设置，优先与数据库节点可用区保持一致；传入该字段，代理节点将设置在指定可用区。

        :param proxy_nodes_az_list: The proxy_nodes_az_list of this EnlargeProxyRequest.
        :type proxy_nodes_az_list: list[str]
        """
        self._proxy_nodes_az_list = proxy_nodes_az_list

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
