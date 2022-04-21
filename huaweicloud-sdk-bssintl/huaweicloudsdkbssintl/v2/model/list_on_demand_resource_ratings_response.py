# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOnDemandResourceRatingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'amount': 'float',
        'discount_amount': 'float',
        'official_website_amount': 'float',
        'measure_id': 'int',
        'currency': 'str',
        'product_rating_results': 'list[DemandProductRatingResult]'
    }

    attribute_map = {
        'amount': 'amount',
        'discount_amount': 'discount_amount',
        'official_website_amount': 'official_website_amount',
        'measure_id': 'measure_id',
        'currency': 'currency',
        'product_rating_results': 'product_rating_results'
    }

    def __init__(self, amount=None, discount_amount=None, official_website_amount=None, measure_id=None, currency=None, product_rating_results=None):
        """ListOnDemandResourceRatingsResponse

        The model defined in huaweicloud sdk

        :param amount: 折扣的金额。
        :type amount: float
        :param discount_amount: 优惠额（官网价和总价的差）。
        :type discount_amount: float
        :param official_website_amount: 按需产品的官网价。
        :type official_website_amount: float
        :param measure_id: 度量单位标识。 1：元
        :type measure_id: int
        :param currency: 币种。 USD：美元。 值为空代表美元。
        :type currency: str
        :param product_rating_results: 产品询价结果，具体参见表2。
        :type product_rating_results: list[:class:`huaweicloudsdkbssintl.v2.DemandProductRatingResult`]
        """
        
        super(ListOnDemandResourceRatingsResponse, self).__init__()

        self._amount = None
        self._discount_amount = None
        self._official_website_amount = None
        self._measure_id = None
        self._currency = None
        self._product_rating_results = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency
        if product_rating_results is not None:
            self.product_rating_results = product_rating_results

    @property
    def amount(self):
        """Gets the amount of this ListOnDemandResourceRatingsResponse.

        折扣的金额。

        :return: The amount of this ListOnDemandResourceRatingsResponse.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ListOnDemandResourceRatingsResponse.

        折扣的金额。

        :param amount: The amount of this ListOnDemandResourceRatingsResponse.
        :type amount: float
        """
        self._amount = amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this ListOnDemandResourceRatingsResponse.

        优惠额（官网价和总价的差）。

        :return: The discount_amount of this ListOnDemandResourceRatingsResponse.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this ListOnDemandResourceRatingsResponse.

        优惠额（官网价和总价的差）。

        :param discount_amount: The discount_amount of this ListOnDemandResourceRatingsResponse.
        :type discount_amount: float
        """
        self._discount_amount = discount_amount

    @property
    def official_website_amount(self):
        """Gets the official_website_amount of this ListOnDemandResourceRatingsResponse.

        按需产品的官网价。

        :return: The official_website_amount of this ListOnDemandResourceRatingsResponse.
        :rtype: float
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        """Sets the official_website_amount of this ListOnDemandResourceRatingsResponse.

        按需产品的官网价。

        :param official_website_amount: The official_website_amount of this ListOnDemandResourceRatingsResponse.
        :type official_website_amount: float
        """
        self._official_website_amount = official_website_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this ListOnDemandResourceRatingsResponse.

        度量单位标识。 1：元

        :return: The measure_id of this ListOnDemandResourceRatingsResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this ListOnDemandResourceRatingsResponse.

        度量单位标识。 1：元

        :param measure_id: The measure_id of this ListOnDemandResourceRatingsResponse.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        """Gets the currency of this ListOnDemandResourceRatingsResponse.

        币种。 USD：美元。 值为空代表美元。

        :return: The currency of this ListOnDemandResourceRatingsResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListOnDemandResourceRatingsResponse.

        币种。 USD：美元。 值为空代表美元。

        :param currency: The currency of this ListOnDemandResourceRatingsResponse.
        :type currency: str
        """
        self._currency = currency

    @property
    def product_rating_results(self):
        """Gets the product_rating_results of this ListOnDemandResourceRatingsResponse.

        产品询价结果，具体参见表2。

        :return: The product_rating_results of this ListOnDemandResourceRatingsResponse.
        :rtype: list[:class:`huaweicloudsdkbssintl.v2.DemandProductRatingResult`]
        """
        return self._product_rating_results

    @product_rating_results.setter
    def product_rating_results(self, product_rating_results):
        """Sets the product_rating_results of this ListOnDemandResourceRatingsResponse.

        产品询价结果，具体参见表2。

        :param product_rating_results: The product_rating_results of this ListOnDemandResourceRatingsResponse.
        :type product_rating_results: list[:class:`huaweicloudsdkbssintl.v2.DemandProductRatingResult`]
        """
        self._product_rating_results = product_rating_results

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
        if not isinstance(other, ListOnDemandResourceRatingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
