# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyProxyRouteWeightReadonlyNode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'weight': 'int'
    }

    attribute_map = {
        'id': 'id',
        'weight': 'weight'
    }

    def __init__(self, id=None, weight=None):
        r"""ModifyProxyRouteWeightReadonlyNode

        The model defined in huaweicloud sdk

        :param id: 只读节点ID。
        :type id: str
        :param weight: 只读节点权重： - 如果路由模式为0，取值为0~1000； - 如果路由模式为1或2，取值为0或1。
        :type weight: int
        """
        
        

        self._id = None
        self._weight = None
        self.discriminator = None

        self.id = id
        self.weight = weight

    @property
    def id(self):
        r"""Gets the id of this ModifyProxyRouteWeightReadonlyNode.

        只读节点ID。

        :return: The id of this ModifyProxyRouteWeightReadonlyNode.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModifyProxyRouteWeightReadonlyNode.

        只读节点ID。

        :param id: The id of this ModifyProxyRouteWeightReadonlyNode.
        :type id: str
        """
        self._id = id

    @property
    def weight(self):
        r"""Gets the weight of this ModifyProxyRouteWeightReadonlyNode.

        只读节点权重： - 如果路由模式为0，取值为0~1000； - 如果路由模式为1或2，取值为0或1。

        :return: The weight of this ModifyProxyRouteWeightReadonlyNode.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this ModifyProxyRouteWeightReadonlyNode.

        只读节点权重： - 如果路由模式为0，取值为0~1000； - 如果路由模式为1或2，取值为0或1。

        :param weight: The weight of this ModifyProxyRouteWeightReadonlyNode.
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
        if not isinstance(other, ModifyProxyRouteWeightReadonlyNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
