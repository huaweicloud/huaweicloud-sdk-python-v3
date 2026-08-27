# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShrinkGaussMySqlProxyRequestBody:

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
        'node_ids': 'list[str]'
    }

    attribute_map = {
        'node_num': 'node_num',
        'node_ids': 'node_ids'
    }

    def __init__(self, node_num=None, node_ids=None):
        r"""ShrinkGaussMySqlProxyRequestBody

        The model defined in huaweicloud sdk

        :param node_num: 数据库代理节点缩容操作需要减少的节点数。  缩容的节点数的取值范围：1~30之间的整数。  限制条件：该实例的数据库代理节点的总数量小于等于32，大于等于2。
        :type node_num: int
        :param node_ids: **参数解释**：  数据库代理节点的节点ID。  获取方式请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**：  不传该字段，将随机删除代理节点；传入该字段，将删除指定ID的代理节点。
        :type node_ids: list[str]
        """
        
        

        self._node_num = None
        self._node_ids = None
        self.discriminator = None

        self.node_num = node_num
        if node_ids is not None:
            self.node_ids = node_ids

    @property
    def node_num(self):
        r"""Gets the node_num of this ShrinkGaussMySqlProxyRequestBody.

        数据库代理节点缩容操作需要减少的节点数。  缩容的节点数的取值范围：1~30之间的整数。  限制条件：该实例的数据库代理节点的总数量小于等于32，大于等于2。

        :return: The node_num of this ShrinkGaussMySqlProxyRequestBody.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        r"""Sets the node_num of this ShrinkGaussMySqlProxyRequestBody.

        数据库代理节点缩容操作需要减少的节点数。  缩容的节点数的取值范围：1~30之间的整数。  限制条件：该实例的数据库代理节点的总数量小于等于32，大于等于2。

        :param node_num: The node_num of this ShrinkGaussMySqlProxyRequestBody.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def node_ids(self):
        r"""Gets the node_ids of this ShrinkGaussMySqlProxyRequestBody.

        **参数解释**：  数据库代理节点的节点ID。  获取方式请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**：  不传该字段，将随机删除代理节点；传入该字段，将删除指定ID的代理节点。

        :return: The node_ids of this ShrinkGaussMySqlProxyRequestBody.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        r"""Sets the node_ids of this ShrinkGaussMySqlProxyRequestBody.

        **参数解释**：  数据库代理节点的节点ID。  获取方式请参见[查询数据库代理信息列表](https://support.huaweicloud.com/api-taurusdb/ShowGaussMySqlProxyList.html)。  **约束限制**：  不传该字段，将随机删除代理节点；传入该字段，将删除指定ID的代理节点。

        :param node_ids: The node_ids of this ShrinkGaussMySqlProxyRequestBody.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

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
        if not isinstance(other, ShrinkGaussMySqlProxyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
