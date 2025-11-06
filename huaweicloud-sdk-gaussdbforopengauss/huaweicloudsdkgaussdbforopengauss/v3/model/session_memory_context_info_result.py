# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SessionMemoryContextInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'context_name': 'str',
        'amount': 'int',
        'size': 'float'
    }

    attribute_map = {
        'context_name': 'context_name',
        'amount': 'amount',
        'size': 'size'
    }

    def __init__(self, context_name=None, amount=None, size=None):
        r"""SessionMemoryContextInfoResult

        The model defined in huaweicloud sdk

        :param context_name: **参数解释**: 内存上下文名称。 **取值范围**: 不涉及。
        :type context_name: str
        :param amount: **参数解释**: 会话上下文数量。 **取值范围**: 大于等于0。
        :type amount: int
        :param size: **参数解释**: 会话上下文总大小。 **取值范围**: 大于等于0。
        :type size: float
        """
        
        

        self._context_name = None
        self._amount = None
        self._size = None
        self.discriminator = None

        if context_name is not None:
            self.context_name = context_name
        if amount is not None:
            self.amount = amount
        if size is not None:
            self.size = size

    @property
    def context_name(self):
        r"""Gets the context_name of this SessionMemoryContextInfoResult.

        **参数解释**: 内存上下文名称。 **取值范围**: 不涉及。

        :return: The context_name of this SessionMemoryContextInfoResult.
        :rtype: str
        """
        return self._context_name

    @context_name.setter
    def context_name(self, context_name):
        r"""Sets the context_name of this SessionMemoryContextInfoResult.

        **参数解释**: 内存上下文名称。 **取值范围**: 不涉及。

        :param context_name: The context_name of this SessionMemoryContextInfoResult.
        :type context_name: str
        """
        self._context_name = context_name

    @property
    def amount(self):
        r"""Gets the amount of this SessionMemoryContextInfoResult.

        **参数解释**: 会话上下文数量。 **取值范围**: 大于等于0。

        :return: The amount of this SessionMemoryContextInfoResult.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this SessionMemoryContextInfoResult.

        **参数解释**: 会话上下文数量。 **取值范围**: 大于等于0。

        :param amount: The amount of this SessionMemoryContextInfoResult.
        :type amount: int
        """
        self._amount = amount

    @property
    def size(self):
        r"""Gets the size of this SessionMemoryContextInfoResult.

        **参数解释**: 会话上下文总大小。 **取值范围**: 大于等于0。

        :return: The size of this SessionMemoryContextInfoResult.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this SessionMemoryContextInfoResult.

        **参数解释**: 会话上下文总大小。 **取值范围**: 大于等于0。

        :param size: The size of this SessionMemoryContextInfoResult.
        :type size: float
        """
        self._size = size

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
        if not isinstance(other, SessionMemoryContextInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
