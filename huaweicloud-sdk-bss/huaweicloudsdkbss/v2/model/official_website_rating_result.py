# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OfficialWebsiteRatingResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'official_website_amount': 'decimal.Decimal',
        'installment_official_website_amount': 'str',
        'installment_period_type': 'int',
        'measure_id': 'int',
        'product_rating_results': 'list[PeriodProductOfficialRatingResult]'
    }

    attribute_map = {
        'official_website_amount': 'official_website_amount',
        'installment_official_website_amount': 'installment_official_website_amount',
        'installment_period_type': 'installment_period_type',
        'measure_id': 'measure_id',
        'product_rating_results': 'product_rating_results'
    }

    def __init__(self, official_website_amount=None, installment_official_website_amount=None, installment_period_type=None, measure_id=None, product_rating_results=None):
        """OfficialWebsiteRatingResult

        The model defined in huaweicloud sdk

        :param official_website_amount: 包年/包月产品的官网价。
        :type official_website_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param installment_official_website_amount: 分期金额的官网价。  说明： 暂只支持IES产品。
        :type installment_official_website_amount: str
        :param installment_period_type: 分期付款的周期类型。 2：月  说明： 暂只支持IES产品。
        :type installment_period_type: int
        :param measure_id: 价格度量单位标识。 1：元
        :type measure_id: int
        :param product_rating_results: 产品询价结果，具体参见表5。
        :type product_rating_results: list[:class:`huaweicloudsdkbss.v2.PeriodProductOfficialRatingResult`]
        """
        
        

        self._official_website_amount = None
        self._installment_official_website_amount = None
        self._installment_period_type = None
        self._measure_id = None
        self._product_rating_results = None
        self.discriminator = None

        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if installment_official_website_amount is not None:
            self.installment_official_website_amount = installment_official_website_amount
        if installment_period_type is not None:
            self.installment_period_type = installment_period_type
        if measure_id is not None:
            self.measure_id = measure_id
        if product_rating_results is not None:
            self.product_rating_results = product_rating_results

    @property
    def official_website_amount(self):
        """Gets the official_website_amount of this OfficialWebsiteRatingResult.

        包年/包月产品的官网价。

        :return: The official_website_amount of this OfficialWebsiteRatingResult.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        """Sets the official_website_amount of this OfficialWebsiteRatingResult.

        包年/包月产品的官网价。

        :param official_website_amount: The official_website_amount of this OfficialWebsiteRatingResult.
        :type official_website_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._official_website_amount = official_website_amount

    @property
    def installment_official_website_amount(self):
        """Gets the installment_official_website_amount of this OfficialWebsiteRatingResult.

        分期金额的官网价。  说明： 暂只支持IES产品。

        :return: The installment_official_website_amount of this OfficialWebsiteRatingResult.
        :rtype: str
        """
        return self._installment_official_website_amount

    @installment_official_website_amount.setter
    def installment_official_website_amount(self, installment_official_website_amount):
        """Sets the installment_official_website_amount of this OfficialWebsiteRatingResult.

        分期金额的官网价。  说明： 暂只支持IES产品。

        :param installment_official_website_amount: The installment_official_website_amount of this OfficialWebsiteRatingResult.
        :type installment_official_website_amount: str
        """
        self._installment_official_website_amount = installment_official_website_amount

    @property
    def installment_period_type(self):
        """Gets the installment_period_type of this OfficialWebsiteRatingResult.

        分期付款的周期类型。 2：月  说明： 暂只支持IES产品。

        :return: The installment_period_type of this OfficialWebsiteRatingResult.
        :rtype: int
        """
        return self._installment_period_type

    @installment_period_type.setter
    def installment_period_type(self, installment_period_type):
        """Sets the installment_period_type of this OfficialWebsiteRatingResult.

        分期付款的周期类型。 2：月  说明： 暂只支持IES产品。

        :param installment_period_type: The installment_period_type of this OfficialWebsiteRatingResult.
        :type installment_period_type: int
        """
        self._installment_period_type = installment_period_type

    @property
    def measure_id(self):
        """Gets the measure_id of this OfficialWebsiteRatingResult.

        价格度量单位标识。 1：元

        :return: The measure_id of this OfficialWebsiteRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this OfficialWebsiteRatingResult.

        价格度量单位标识。 1：元

        :param measure_id: The measure_id of this OfficialWebsiteRatingResult.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def product_rating_results(self):
        """Gets the product_rating_results of this OfficialWebsiteRatingResult.

        产品询价结果，具体参见表5。

        :return: The product_rating_results of this OfficialWebsiteRatingResult.
        :rtype: list[:class:`huaweicloudsdkbss.v2.PeriodProductOfficialRatingResult`]
        """
        return self._product_rating_results

    @product_rating_results.setter
    def product_rating_results(self, product_rating_results):
        """Sets the product_rating_results of this OfficialWebsiteRatingResult.

        产品询价结果，具体参见表5。

        :param product_rating_results: The product_rating_results of this OfficialWebsiteRatingResult.
        :type product_rating_results: list[:class:`huaweicloudsdkbss.v2.PeriodProductOfficialRatingResult`]
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
        if not isinstance(other, OfficialWebsiteRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
