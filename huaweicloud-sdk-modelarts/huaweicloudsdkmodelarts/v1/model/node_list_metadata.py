# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeListMetadata:

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
        'remaining_item_count': 'int'
    }

    attribute_map = {
        '_continue': 'continue',
        'remaining_item_count': 'remainingItemCount'
    }

    def __init__(self, _continue=None, remaining_item_count=None):
        r"""NodeListMetadata

        The model defined in huaweicloud sdk

        :param _continue: **参数解释**：分页查询的偏移标志。 **取值范围**：取值来自用户上一次分页查询响应结果中metadata.continue中的值，值为空默认无偏移。
        :type _continue: str
        :param remaining_item_count: **参数解释**：分页查询中剩余资源的数量。 **默认取值**：不涉及。
        :type remaining_item_count: int
        """
        
        

        self.__continue = None
        self._remaining_item_count = None
        self.discriminator = None

        if _continue is not None:
            self._continue = _continue
        if remaining_item_count is not None:
            self.remaining_item_count = remaining_item_count

    @property
    def _continue(self):
        r"""Gets the _continue of this NodeListMetadata.

        **参数解释**：分页查询的偏移标志。 **取值范围**：取值来自用户上一次分页查询响应结果中metadata.continue中的值，值为空默认无偏移。

        :return: The _continue of this NodeListMetadata.
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        r"""Sets the _continue of this NodeListMetadata.

        **参数解释**：分页查询的偏移标志。 **取值范围**：取值来自用户上一次分页查询响应结果中metadata.continue中的值，值为空默认无偏移。

        :param _continue: The _continue of this NodeListMetadata.
        :type _continue: str
        """
        self.__continue = _continue

    @property
    def remaining_item_count(self):
        r"""Gets the remaining_item_count of this NodeListMetadata.

        **参数解释**：分页查询中剩余资源的数量。 **默认取值**：不涉及。

        :return: The remaining_item_count of this NodeListMetadata.
        :rtype: int
        """
        return self._remaining_item_count

    @remaining_item_count.setter
    def remaining_item_count(self, remaining_item_count):
        r"""Sets the remaining_item_count of this NodeListMetadata.

        **参数解释**：分页查询中剩余资源的数量。 **默认取值**：不涉及。

        :param remaining_item_count: The remaining_item_count of this NodeListMetadata.
        :type remaining_item_count: int
        """
        self._remaining_item_count = remaining_item_count

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
        if not isinstance(other, NodeListMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
