# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PeriodBatchUpChangeResourceRsp:

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
        'extend_params': 'str',
        'official_website_rating_result': 'OfficialWebsiteRatingResult',
        'optional_discount_rating_results': 'list[OptionalDiscountRatingResult]'
    }

    attribute_map = {
        'currency': 'currency',
        'extend_params': 'extend_params',
        'official_website_rating_result': 'official_website_rating_result',
        'optional_discount_rating_results': 'optional_discount_rating_results'
    }

    def __init__(self, currency=None, extend_params=None, official_website_rating_result=None, optional_discount_rating_results=None):
        r"""PeriodBatchUpChangeResourceRsp

        The model defined in huaweicloud sdk

        :param currency: 币种，比如CNY。
        :type currency: str
        :param extend_params: 扩展参数。
        :type extend_params: str
        :param official_website_rating_result: 
        :type official_website_rating_result: :class:`huaweicloudsdkworkspace.v2.OfficialWebsiteRatingResult`
        :param optional_discount_rating_results: 存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果。
        :type optional_discount_rating_results: list[:class:`huaweicloudsdkworkspace.v2.OptionalDiscountRatingResult`]
        """
        
        

        self._currency = None
        self._extend_params = None
        self._official_website_rating_result = None
        self._optional_discount_rating_results = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if extend_params is not None:
            self.extend_params = extend_params
        if official_website_rating_result is not None:
            self.official_website_rating_result = official_website_rating_result
        if optional_discount_rating_results is not None:
            self.optional_discount_rating_results = optional_discount_rating_results

    @property
    def currency(self):
        r"""Gets the currency of this PeriodBatchUpChangeResourceRsp.

        币种，比如CNY。

        :return: The currency of this PeriodBatchUpChangeResourceRsp.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        r"""Sets the currency of this PeriodBatchUpChangeResourceRsp.

        币种，比如CNY。

        :param currency: The currency of this PeriodBatchUpChangeResourceRsp.
        :type currency: str
        """
        self._currency = currency

    @property
    def extend_params(self):
        r"""Gets the extend_params of this PeriodBatchUpChangeResourceRsp.

        扩展参数。

        :return: The extend_params of this PeriodBatchUpChangeResourceRsp.
        :rtype: str
        """
        return self._extend_params

    @extend_params.setter
    def extend_params(self, extend_params):
        r"""Sets the extend_params of this PeriodBatchUpChangeResourceRsp.

        扩展参数。

        :param extend_params: The extend_params of this PeriodBatchUpChangeResourceRsp.
        :type extend_params: str
        """
        self._extend_params = extend_params

    @property
    def official_website_rating_result(self):
        r"""Gets the official_website_rating_result of this PeriodBatchUpChangeResourceRsp.

        :return: The official_website_rating_result of this PeriodBatchUpChangeResourceRsp.
        :rtype: :class:`huaweicloudsdkworkspace.v2.OfficialWebsiteRatingResult`
        """
        return self._official_website_rating_result

    @official_website_rating_result.setter
    def official_website_rating_result(self, official_website_rating_result):
        r"""Sets the official_website_rating_result of this PeriodBatchUpChangeResourceRsp.

        :param official_website_rating_result: The official_website_rating_result of this PeriodBatchUpChangeResourceRsp.
        :type official_website_rating_result: :class:`huaweicloudsdkworkspace.v2.OfficialWebsiteRatingResult`
        """
        self._official_website_rating_result = official_website_rating_result

    @property
    def optional_discount_rating_results(self):
        r"""Gets the optional_discount_rating_results of this PeriodBatchUpChangeResourceRsp.

        存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果。

        :return: The optional_discount_rating_results of this PeriodBatchUpChangeResourceRsp.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.OptionalDiscountRatingResult`]
        """
        return self._optional_discount_rating_results

    @optional_discount_rating_results.setter
    def optional_discount_rating_results(self, optional_discount_rating_results):
        r"""Sets the optional_discount_rating_results of this PeriodBatchUpChangeResourceRsp.

        存在可选折扣优惠时返回折扣优惠维度询价结果，每个折扣优惠一组询价结果。

        :param optional_discount_rating_results: The optional_discount_rating_results of this PeriodBatchUpChangeResourceRsp.
        :type optional_discount_rating_results: list[:class:`huaweicloudsdkworkspace.v2.OptionalDiscountRatingResult`]
        """
        self._optional_discount_rating_results = optional_discount_rating_results

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
        if not isinstance(other, PeriodBatchUpChangeResourceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
