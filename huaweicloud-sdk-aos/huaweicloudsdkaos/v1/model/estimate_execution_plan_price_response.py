# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EstimateExecutionPlanPriceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'currency': 'str',
        'items': 'list[ItemsResponse]'
    }

    attribute_map = {
        'currency': 'currency',
        'items': 'items'
    }

    def __init__(self, currency=None, items=None):
        """EstimateExecutionPlanPriceResponse

        The model defined in huaweicloud sdk

        :param currency: 币种，枚举值   * &#x60;CNY&#x60; - 元，中国站返回的币种   * &#x60;USD&#x60; - 美元，国际站返回的币种
        :type currency: str
        :param items: 执行计划中所有资源的询价结果
        :type items: list[:class:`huaweicloudsdkaos.v1.ItemsResponse`]
        """
        
        super(EstimateExecutionPlanPriceResponse, self).__init__()

        self._currency = None
        self._items = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if items is not None:
            self.items = items

    @property
    def currency(self):
        """Gets the currency of this EstimateExecutionPlanPriceResponse.

        币种，枚举值   * `CNY` - 元，中国站返回的币种   * `USD` - 美元，国际站返回的币种

        :return: The currency of this EstimateExecutionPlanPriceResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this EstimateExecutionPlanPriceResponse.

        币种，枚举值   * `CNY` - 元，中国站返回的币种   * `USD` - 美元，国际站返回的币种

        :param currency: The currency of this EstimateExecutionPlanPriceResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def items(self):
        """Gets the items of this EstimateExecutionPlanPriceResponse.

        执行计划中所有资源的询价结果

        :return: The items of this EstimateExecutionPlanPriceResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.ItemsResponse`]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this EstimateExecutionPlanPriceResponse.

        执行计划中所有资源的询价结果

        :param items: The items of this EstimateExecutionPlanPriceResponse.
        :type items: list[:class:`huaweicloudsdkaos.v1.ItemsResponse`]
        """
        self._items = items

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
        if not isinstance(other, EstimateExecutionPlanPriceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
