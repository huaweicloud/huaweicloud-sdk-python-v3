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
        'amount': 'float',
        'official_website_amount': 'float',
        'original_amount': 'float',
        'official_website_discount_amount': 'float',
        'optional_discount_amount': 'float',
        'discount_amount': 'float',
        'per_amount': 'float',
        'per_discount_amount': 'float',
        'per_original_amount': 'float',
        'per_period_type': 'int',
        'measure_id': 'int',
        'product_rating_results': 'list[ProductResult]'
    }

    attribute_map = {
        'amount': 'amount',
        'official_website_amount': 'official_website_amount',
        'original_amount': 'original_amount',
        'official_website_discount_amount': 'official_website_discount_amount',
        'optional_discount_amount': 'optional_discount_amount',
        'discount_amount': 'discount_amount',
        'per_amount': 'per_amount',
        'per_discount_amount': 'per_discount_amount',
        'per_original_amount': 'per_original_amount',
        'per_period_type': 'per_period_type',
        'measure_id': 'measure_id',
        'product_rating_results': 'product_rating_results'
    }

    def __init__(self, amount=None, official_website_amount=None, original_amount=None, official_website_discount_amount=None, optional_discount_amount=None, discount_amount=None, per_amount=None, per_discount_amount=None, per_original_amount=None, per_period_type=None, measure_id=None, product_rating_results=None):
        r"""OfficialWebsiteRatingResult

        The model defined in huaweicloud sdk

        :param amount: 订单总额，即最终优惠后的订单金额(预留实例只包含预付部分)。
        :type amount: float
        :param official_website_amount: 官网价(预留实例只包含预付部分)。
        :type official_website_amount: float
        :param original_amount: 订单原总额，即优惠前订单总额(预留实例只包含预付部分)。
        :type original_amount: float
        :param official_website_discount_amount: 官网价优惠额(预留实例只包含预付部分)。
        :type official_website_discount_amount: float
        :param optional_discount_amount: 可选折扣优惠额(预留实例只包含预付部分)。
        :type optional_discount_amount: float
        :param discount_amount: 总优惠额(预留实例只包含预付部分)。
        :type discount_amount: float
        :param per_amount: 总分期金额(批量询价的商品分期周期类型一致，才会有总分期金额，分期周期类型不一致，该信息没有)。
        :type per_amount: float
        :param per_discount_amount: 总分期金额的优惠额(perDiscountAmount &#x3D; perOriginalAmount - perAmount)。
        :type per_discount_amount: float
        :param per_original_amount: 总分期金额原价。
        :type per_original_amount: float
        :param per_period_type: 分期周期类型 2:月 4:小时。
        :type per_period_type: int
        :param measure_id: 度量单位。
        :type measure_id: int
        :param product_rating_results: 产品询价结果。
        :type product_rating_results: list[:class:`huaweicloudsdkworkspace.v2.ProductResult`]
        """
        
        

        self._amount = None
        self._official_website_amount = None
        self._original_amount = None
        self._official_website_discount_amount = None
        self._optional_discount_amount = None
        self._discount_amount = None
        self._per_amount = None
        self._per_discount_amount = None
        self._per_original_amount = None
        self._per_period_type = None
        self._measure_id = None
        self._product_rating_results = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if original_amount is not None:
            self.original_amount = original_amount
        if official_website_discount_amount is not None:
            self.official_website_discount_amount = official_website_discount_amount
        if optional_discount_amount is not None:
            self.optional_discount_amount = optional_discount_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if per_amount is not None:
            self.per_amount = per_amount
        if per_discount_amount is not None:
            self.per_discount_amount = per_discount_amount
        if per_original_amount is not None:
            self.per_original_amount = per_original_amount
        if per_period_type is not None:
            self.per_period_type = per_period_type
        if measure_id is not None:
            self.measure_id = measure_id
        if product_rating_results is not None:
            self.product_rating_results = product_rating_results

    @property
    def amount(self):
        r"""Gets the amount of this OfficialWebsiteRatingResult.

        订单总额，即最终优惠后的订单金额(预留实例只包含预付部分)。

        :return: The amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this OfficialWebsiteRatingResult.

        订单总额，即最终优惠后的订单金额(预留实例只包含预付部分)。

        :param amount: The amount of this OfficialWebsiteRatingResult.
        :type amount: float
        """
        self._amount = amount

    @property
    def official_website_amount(self):
        r"""Gets the official_website_amount of this OfficialWebsiteRatingResult.

        官网价(预留实例只包含预付部分)。

        :return: The official_website_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        r"""Sets the official_website_amount of this OfficialWebsiteRatingResult.

        官网价(预留实例只包含预付部分)。

        :param official_website_amount: The official_website_amount of this OfficialWebsiteRatingResult.
        :type official_website_amount: float
        """
        self._official_website_amount = official_website_amount

    @property
    def original_amount(self):
        r"""Gets the original_amount of this OfficialWebsiteRatingResult.

        订单原总额，即优惠前订单总额(预留实例只包含预付部分)。

        :return: The original_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        r"""Sets the original_amount of this OfficialWebsiteRatingResult.

        订单原总额，即优惠前订单总额(预留实例只包含预付部分)。

        :param original_amount: The original_amount of this OfficialWebsiteRatingResult.
        :type original_amount: float
        """
        self._original_amount = original_amount

    @property
    def official_website_discount_amount(self):
        r"""Gets the official_website_discount_amount of this OfficialWebsiteRatingResult.

        官网价优惠额(预留实例只包含预付部分)。

        :return: The official_website_discount_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._official_website_discount_amount

    @official_website_discount_amount.setter
    def official_website_discount_amount(self, official_website_discount_amount):
        r"""Sets the official_website_discount_amount of this OfficialWebsiteRatingResult.

        官网价优惠额(预留实例只包含预付部分)。

        :param official_website_discount_amount: The official_website_discount_amount of this OfficialWebsiteRatingResult.
        :type official_website_discount_amount: float
        """
        self._official_website_discount_amount = official_website_discount_amount

    @property
    def optional_discount_amount(self):
        r"""Gets the optional_discount_amount of this OfficialWebsiteRatingResult.

        可选折扣优惠额(预留实例只包含预付部分)。

        :return: The optional_discount_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._optional_discount_amount

    @optional_discount_amount.setter
    def optional_discount_amount(self, optional_discount_amount):
        r"""Sets the optional_discount_amount of this OfficialWebsiteRatingResult.

        可选折扣优惠额(预留实例只包含预付部分)。

        :param optional_discount_amount: The optional_discount_amount of this OfficialWebsiteRatingResult.
        :type optional_discount_amount: float
        """
        self._optional_discount_amount = optional_discount_amount

    @property
    def discount_amount(self):
        r"""Gets the discount_amount of this OfficialWebsiteRatingResult.

        总优惠额(预留实例只包含预付部分)。

        :return: The discount_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        r"""Sets the discount_amount of this OfficialWebsiteRatingResult.

        总优惠额(预留实例只包含预付部分)。

        :param discount_amount: The discount_amount of this OfficialWebsiteRatingResult.
        :type discount_amount: float
        """
        self._discount_amount = discount_amount

    @property
    def per_amount(self):
        r"""Gets the per_amount of this OfficialWebsiteRatingResult.

        总分期金额(批量询价的商品分期周期类型一致，才会有总分期金额，分期周期类型不一致，该信息没有)。

        :return: The per_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._per_amount

    @per_amount.setter
    def per_amount(self, per_amount):
        r"""Sets the per_amount of this OfficialWebsiteRatingResult.

        总分期金额(批量询价的商品分期周期类型一致，才会有总分期金额，分期周期类型不一致，该信息没有)。

        :param per_amount: The per_amount of this OfficialWebsiteRatingResult.
        :type per_amount: float
        """
        self._per_amount = per_amount

    @property
    def per_discount_amount(self):
        r"""Gets the per_discount_amount of this OfficialWebsiteRatingResult.

        总分期金额的优惠额(perDiscountAmount = perOriginalAmount - perAmount)。

        :return: The per_discount_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._per_discount_amount

    @per_discount_amount.setter
    def per_discount_amount(self, per_discount_amount):
        r"""Sets the per_discount_amount of this OfficialWebsiteRatingResult.

        总分期金额的优惠额(perDiscountAmount = perOriginalAmount - perAmount)。

        :param per_discount_amount: The per_discount_amount of this OfficialWebsiteRatingResult.
        :type per_discount_amount: float
        """
        self._per_discount_amount = per_discount_amount

    @property
    def per_original_amount(self):
        r"""Gets the per_original_amount of this OfficialWebsiteRatingResult.

        总分期金额原价。

        :return: The per_original_amount of this OfficialWebsiteRatingResult.
        :rtype: float
        """
        return self._per_original_amount

    @per_original_amount.setter
    def per_original_amount(self, per_original_amount):
        r"""Sets the per_original_amount of this OfficialWebsiteRatingResult.

        总分期金额原价。

        :param per_original_amount: The per_original_amount of this OfficialWebsiteRatingResult.
        :type per_original_amount: float
        """
        self._per_original_amount = per_original_amount

    @property
    def per_period_type(self):
        r"""Gets the per_period_type of this OfficialWebsiteRatingResult.

        分期周期类型 2:月 4:小时。

        :return: The per_period_type of this OfficialWebsiteRatingResult.
        :rtype: int
        """
        return self._per_period_type

    @per_period_type.setter
    def per_period_type(self, per_period_type):
        r"""Sets the per_period_type of this OfficialWebsiteRatingResult.

        分期周期类型 2:月 4:小时。

        :param per_period_type: The per_period_type of this OfficialWebsiteRatingResult.
        :type per_period_type: int
        """
        self._per_period_type = per_period_type

    @property
    def measure_id(self):
        r"""Gets the measure_id of this OfficialWebsiteRatingResult.

        度量单位。

        :return: The measure_id of this OfficialWebsiteRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this OfficialWebsiteRatingResult.

        度量单位。

        :param measure_id: The measure_id of this OfficialWebsiteRatingResult.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def product_rating_results(self):
        r"""Gets the product_rating_results of this OfficialWebsiteRatingResult.

        产品询价结果。

        :return: The product_rating_results of this OfficialWebsiteRatingResult.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ProductResult`]
        """
        return self._product_rating_results

    @product_rating_results.setter
    def product_rating_results(self, product_rating_results):
        r"""Sets the product_rating_results of this OfficialWebsiteRatingResult.

        产品询价结果。

        :param product_rating_results: The product_rating_results of this OfficialWebsiteRatingResult.
        :type product_rating_results: list[:class:`huaweicloudsdkworkspace.v2.ProductResult`]
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
