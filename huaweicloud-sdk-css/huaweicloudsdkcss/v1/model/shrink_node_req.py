# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShrinkNodeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reduced_node_num': 'int',
        'type': 'str'
    }

    attribute_map = {
        'reduced_node_num': 'reducedNodeNum',
        'type': 'type'
    }

    def __init__(self, reduced_node_num=None, type=None):
        """ShrinkNodeReq

        The model defined in huaweicloud sdk

        :param reduced_node_num: 需要缩容的节点数量。  - 对节点缩容后，请确保每个节点类型在每个AZ中的数量至少为1。  - 关于跨AZ的集群，在不同AZ中同类型节点个数的差值要小于等于1。  - 关于没有Master节点的集群，每次缩容的数据节点个数(包含冷数据节点和其他类型节点)要小于当前数据节点总数的一半，缩容后的数据节点个数要大于索引的最大副本个数。  - 关于有Master节点的集群，每次缩容的Master节点个数要小于当前Master节点总数的一半，缩容后的Master节点个数必须是奇数且不小于3。
        :type reduced_node_num: int
        :param type: 指定节点类型。 - ess：数据节点。 - ess-cold：冷数据节点。 - ess-client：Client节点。 - ess-master：Master节点。
        :type type: str
        """
        
        

        self._reduced_node_num = None
        self._type = None
        self.discriminator = None

        self.reduced_node_num = reduced_node_num
        self.type = type

    @property
    def reduced_node_num(self):
        """Gets the reduced_node_num of this ShrinkNodeReq.

        需要缩容的节点数量。  - 对节点缩容后，请确保每个节点类型在每个AZ中的数量至少为1。  - 关于跨AZ的集群，在不同AZ中同类型节点个数的差值要小于等于1。  - 关于没有Master节点的集群，每次缩容的数据节点个数(包含冷数据节点和其他类型节点)要小于当前数据节点总数的一半，缩容后的数据节点个数要大于索引的最大副本个数。  - 关于有Master节点的集群，每次缩容的Master节点个数要小于当前Master节点总数的一半，缩容后的Master节点个数必须是奇数且不小于3。

        :return: The reduced_node_num of this ShrinkNodeReq.
        :rtype: int
        """
        return self._reduced_node_num

    @reduced_node_num.setter
    def reduced_node_num(self, reduced_node_num):
        """Sets the reduced_node_num of this ShrinkNodeReq.

        需要缩容的节点数量。  - 对节点缩容后，请确保每个节点类型在每个AZ中的数量至少为1。  - 关于跨AZ的集群，在不同AZ中同类型节点个数的差值要小于等于1。  - 关于没有Master节点的集群，每次缩容的数据节点个数(包含冷数据节点和其他类型节点)要小于当前数据节点总数的一半，缩容后的数据节点个数要大于索引的最大副本个数。  - 关于有Master节点的集群，每次缩容的Master节点个数要小于当前Master节点总数的一半，缩容后的Master节点个数必须是奇数且不小于3。

        :param reduced_node_num: The reduced_node_num of this ShrinkNodeReq.
        :type reduced_node_num: int
        """
        self._reduced_node_num = reduced_node_num

    @property
    def type(self):
        """Gets the type of this ShrinkNodeReq.

        指定节点类型。 - ess：数据节点。 - ess-cold：冷数据节点。 - ess-client：Client节点。 - ess-master：Master节点。

        :return: The type of this ShrinkNodeReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShrinkNodeReq.

        指定节点类型。 - ess：数据节点。 - ess-cold：冷数据节点。 - ess-client：Client节点。 - ess-master：Master节点。

        :param type: The type of this ShrinkNodeReq.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShrinkNodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
