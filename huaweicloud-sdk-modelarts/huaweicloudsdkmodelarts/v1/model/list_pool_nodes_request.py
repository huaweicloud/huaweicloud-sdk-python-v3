# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoolNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_continue': 'str',
        'limit': 'int',
        'pool_name': 'str'
    }

    attribute_map = {
        '_continue': 'continue',
        'limit': 'limit',
        'pool_name': 'pool_name'
    }

    def __init__(self, _continue=None, limit=None, pool_name=None):
        r"""ListPoolNodesRequest

        The model defined in huaweicloud sdk

        :param _continue: **参数解释**：分页查询的偏移标志。 **约束限制**：可选。 **取值范围**：取值来自用户上一次分页查询响应结果中metadata.continue中的值，值为空默认无偏移。 **默认取值**：不涉及。
        :type _continue: str
        :param limit: **参数解释**：分页单次查询返回的资源数量。 **约束限制**：不涉及。 **取值范围**：0 - 500。 **默认取值**：500。
        :type limit: int
        :param pool_name: **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为36-63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type pool_name: str
        """
        
        

        self.__continue = None
        self._limit = None
        self._pool_name = None
        self.discriminator = None

        if _continue is not None:
            self._continue = _continue
        if limit is not None:
            self.limit = limit
        self.pool_name = pool_name

    @property
    def _continue(self):
        r"""Gets the _continue of this ListPoolNodesRequest.

        **参数解释**：分页查询的偏移标志。 **约束限制**：可选。 **取值范围**：取值来自用户上一次分页查询响应结果中metadata.continue中的值，值为空默认无偏移。 **默认取值**：不涉及。

        :return: The _continue of this ListPoolNodesRequest.
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        r"""Sets the _continue of this ListPoolNodesRequest.

        **参数解释**：分页查询的偏移标志。 **约束限制**：可选。 **取值范围**：取值来自用户上一次分页查询响应结果中metadata.continue中的值，值为空默认无偏移。 **默认取值**：不涉及。

        :param _continue: The _continue of this ListPoolNodesRequest.
        :type _continue: str
        """
        self.__continue = _continue

    @property
    def limit(self):
        r"""Gets the limit of this ListPoolNodesRequest.

        **参数解释**：分页单次查询返回的资源数量。 **约束限制**：不涉及。 **取值范围**：0 - 500。 **默认取值**：500。

        :return: The limit of this ListPoolNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPoolNodesRequest.

        **参数解释**：分页单次查询返回的资源数量。 **约束限制**：不涉及。 **取值范围**：0 - 500。 **默认取值**：500。

        :param limit: The limit of this ListPoolNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def pool_name(self):
        r"""Gets the pool_name of this ListPoolNodesRequest.

        **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为36-63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The pool_name of this ListPoolNodesRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this ListPoolNodesRequest.

        **参数解释**：资源池的ID，取值自资源池详情的metadata.name字段。 **约束限制**：只能以小写字母开头，数字、中划线组成，不能以中划线结尾，且长度为36-63个字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param pool_name: The pool_name of this ListPoolNodesRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

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
        if not isinstance(other, ListPoolNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
