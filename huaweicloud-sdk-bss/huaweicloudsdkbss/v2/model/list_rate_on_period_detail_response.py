# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRateOnPeriodDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'official_website_rating_result': 'OfficialWebsiteRatingResult',
        'optional_discount_rating_results': 'list[OptionalDiscountRatingResult]',
        'currency': 'str'
    }

    attribute_map = {
        'official_website_rating_result': 'official_website_rating_result',
        'optional_discount_rating_results': 'optional_discount_rating_results',
        'currency': 'currency'
    }

    def __init__(self, official_website_rating_result=None, optional_discount_rating_results=None, currency=None):
        """ListRateOnPeriodDetailResponse

        The model defined in huaweicloud sdk

        :param official_website_rating_result: 
        :type official_website_rating_result: :class:`huaweicloudsdkbss.v2.OfficialWebsiteRatingResult`
        :param optional_discount_rating_results: 存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果，具体参见表4。
        :type optional_discount_rating_results: list[:class:`huaweicloudsdkbss.v2.OptionalDiscountRatingResult`]
        :param currency: 币种。 CNY：人民币。 值为空代表人民币。
        :type currency: str
        """
        
        super(ListRateOnPeriodDetailResponse, self).__init__()

        self._official_website_rating_result = None
        self._optional_discount_rating_results = None
        self._currency = None
        self.discriminator = None

        if official_website_rating_result is not None:
            self.official_website_rating_result = official_website_rating_result
        if optional_discount_rating_results is not None:
            self.optional_discount_rating_results = optional_discount_rating_results
        if currency is not None:
            self.currency = currency

    @property
    def official_website_rating_result(self):
        """Gets the official_website_rating_result of this ListRateOnPeriodDetailResponse.

        :return: The official_website_rating_result of this ListRateOnPeriodDetailResponse.
        :rtype: :class:`huaweicloudsdkbss.v2.OfficialWebsiteRatingResult`
        """
        return self._official_website_rating_result

    @official_website_rating_result.setter
    def official_website_rating_result(self, official_website_rating_result):
        """Sets the official_website_rating_result of this ListRateOnPeriodDetailResponse.

        :param official_website_rating_result: The official_website_rating_result of this ListRateOnPeriodDetailResponse.
        :type official_website_rating_result: :class:`huaweicloudsdkbss.v2.OfficialWebsiteRatingResult`
        """
        self._official_website_rating_result = official_website_rating_result

    @property
    def optional_discount_rating_results(self):
        """Gets the optional_discount_rating_results of this ListRateOnPeriodDetailResponse.

        存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果，具体参见表4。

        :return: The optional_discount_rating_results of this ListRateOnPeriodDetailResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.OptionalDiscountRatingResult`]
        """
        return self._optional_discount_rating_results

    @optional_discount_rating_results.setter
    def optional_discount_rating_results(self, optional_discount_rating_results):
        """Sets the optional_discount_rating_results of this ListRateOnPeriodDetailResponse.

        存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果，具体参见表4。

        :param optional_discount_rating_results: The optional_discount_rating_results of this ListRateOnPeriodDetailResponse.
        :type optional_discount_rating_results: list[:class:`huaweicloudsdkbss.v2.OptionalDiscountRatingResult`]
        """
        self._optional_discount_rating_results = optional_discount_rating_results

    @property
    def currency(self):
        """Gets the currency of this ListRateOnPeriodDetailResponse.

        币种。 CNY：人民币。 值为空代表人民币。

        :return: The currency of this ListRateOnPeriodDetailResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListRateOnPeriodDetailResponse.

        币种。 CNY：人民币。 值为空代表人民币。

        :param currency: The currency of this ListRateOnPeriodDetailResponse.
        :type currency: str
        """
        self._currency = currency

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
        if not isinstance(other, ListRateOnPeriodDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
