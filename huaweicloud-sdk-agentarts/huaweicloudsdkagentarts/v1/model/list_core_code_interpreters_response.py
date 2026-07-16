# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreCodeInterpretersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'items': 'list[CoreToolBasic]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'items': 'items'
    }

    def __init__(self, total_count=None, items=None):
        r"""ListCoreCodeInterpretersResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释：** 总记录数。 **取值范围：** 正整数。
        :type total_count: int
        :param items: **参数解释：** 查询列表数组 **取值范围：** 不涉及
        :type items: list[:class:`huaweicloudsdkagentarts.v1.CoreToolBasic`]
        """
        
        super().__init__()

        self._total_count = None
        self._items = None
        self.discriminator = None

        self.total_count = total_count
        self.items = items

    @property
    def total_count(self):
        r"""Gets the total_count of this ListCoreCodeInterpretersResponse.

        **参数解释：** 总记录数。 **取值范围：** 正整数。

        :return: The total_count of this ListCoreCodeInterpretersResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListCoreCodeInterpretersResponse.

        **参数解释：** 总记录数。 **取值范围：** 正整数。

        :param total_count: The total_count of this ListCoreCodeInterpretersResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def items(self):
        r"""Gets the items of this ListCoreCodeInterpretersResponse.

        **参数解释：** 查询列表数组 **取值范围：** 不涉及

        :return: The items of this ListCoreCodeInterpretersResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreToolBasic`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListCoreCodeInterpretersResponse.

        **参数解释：** 查询列表数组 **取值范围：** 不涉及

        :param items: The items of this ListCoreCodeInterpretersResponse.
        :type items: list[:class:`huaweicloudsdkagentarts.v1.CoreToolBasic`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListCoreCodeInterpretersResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListCoreCodeInterpretersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
