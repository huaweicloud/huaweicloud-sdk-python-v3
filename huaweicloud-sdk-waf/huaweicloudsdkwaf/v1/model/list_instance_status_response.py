# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'purchased': 'bool',
        'total': 'int',
        'items': 'list[PremiumWafInstanceStatusResponse]'
    }

    attribute_map = {
        'purchased': 'purchased',
        'total': 'total',
        'items': 'items'
    }

    def __init__(self, purchased=None, total=None, items=None):
        r"""ListInstanceStatusResponse

        The model defined in huaweicloud sdk

        :param purchased: 是否已购买独享引擎
        :type purchased: bool
        :param total: 总数
        :type total: int
        :param items: 引擎实例状态信息列表
        :type items: list[:class:`huaweicloudsdkwaf.v1.PremiumWafInstanceStatusResponse`]
        """
        
        super().__init__()

        self._purchased = None
        self._total = None
        self._items = None
        self.discriminator = None

        if purchased is not None:
            self.purchased = purchased
        if total is not None:
            self.total = total
        if items is not None:
            self.items = items

    @property
    def purchased(self):
        r"""Gets the purchased of this ListInstanceStatusResponse.

        是否已购买独享引擎

        :return: The purchased of this ListInstanceStatusResponse.
        :rtype: bool
        """
        return self._purchased

    @purchased.setter
    def purchased(self, purchased):
        r"""Sets the purchased of this ListInstanceStatusResponse.

        是否已购买独享引擎

        :param purchased: The purchased of this ListInstanceStatusResponse.
        :type purchased: bool
        """
        self._purchased = purchased

    @property
    def total(self):
        r"""Gets the total of this ListInstanceStatusResponse.

        总数

        :return: The total of this ListInstanceStatusResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListInstanceStatusResponse.

        总数

        :param total: The total of this ListInstanceStatusResponse.
        :type total: int
        """
        self._total = total

    @property
    def items(self):
        r"""Gets the items of this ListInstanceStatusResponse.

        引擎实例状态信息列表

        :return: The items of this ListInstanceStatusResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.PremiumWafInstanceStatusResponse`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListInstanceStatusResponse.

        引擎实例状态信息列表

        :param items: The items of this ListInstanceStatusResponse.
        :type items: list[:class:`huaweicloudsdkwaf.v1.PremiumWafInstanceStatusResponse`]
        """
        self._items = items

    def to_dict(self):
        import warnings
        warnings.warn("ListInstanceStatusResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstanceStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
