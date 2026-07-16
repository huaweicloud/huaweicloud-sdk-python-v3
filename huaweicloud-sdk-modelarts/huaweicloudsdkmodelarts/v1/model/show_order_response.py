# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'items': 'list[OrderDetailItem]'
    }

    attribute_map = {
        'count': 'count',
        'items': 'items'
    }

    def __init__(self, count=None, items=None):
        r"""ShowOrderResponse

        The model defined in huaweicloud sdk

        :param count: **参数解释**：订单关联的资源数量。 **取值范围**：不涉及。
        :type count: int
        :param items: **参数解释**：订单关联的资源信息列表。
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.OrderDetailItem`]
        """
        
        super().__init__()

        self._count = None
        self._items = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if items is not None:
            self.items = items

    @property
    def count(self):
        r"""Gets the count of this ShowOrderResponse.

        **参数解释**：订单关联的资源数量。 **取值范围**：不涉及。

        :return: The count of this ShowOrderResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowOrderResponse.

        **参数解释**：订单关联的资源数量。 **取值范围**：不涉及。

        :param count: The count of this ShowOrderResponse.
        :type count: int
        """
        self._count = count

    @property
    def items(self):
        r"""Gets the items of this ShowOrderResponse.

        **参数解释**：订单关联的资源信息列表。

        :return: The items of this ShowOrderResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.OrderDetailItem`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ShowOrderResponse.

        **参数解释**：订单关联的资源信息列表。

        :param items: The items of this ShowOrderResponse.
        :type items: list[:class:`huaweicloudsdkmodelarts.v1.OrderDetailItem`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ShowOrderResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowOrderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
