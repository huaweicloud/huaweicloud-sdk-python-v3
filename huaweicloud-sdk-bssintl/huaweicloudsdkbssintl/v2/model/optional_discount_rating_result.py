# coding: utf-8

import pprint
import re

import six





class OptionalDiscountRatingResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'discount_id': 'str',
        'amount': 'float',
        'official_website_amount': 'float',
        'discount_amount': 'float',
        'measure_id': 'int',
        'discount_type': 'int',
        'discount_name': 'str',
        'best_offer': 'int',
        'product_rating_results': 'list[PeriodProductRatingResult]'
    }

    attribute_map = {
        'discount_id': 'discount_id',
        'amount': 'amount',
        'official_website_amount': 'official_website_amount',
        'discount_amount': 'discount_amount',
        'measure_id': 'measure_id',
        'discount_type': 'discount_type',
        'discount_name': 'discount_name',
        'best_offer': 'best_offer',
        'product_rating_results': 'product_rating_results'
    }

    def __init__(self, discount_id=None, amount=None, official_website_amount=None, discount_amount=None, measure_id=None, discount_type=None, discount_name=None, best_offer=None, product_rating_results=None):
        """OptionalDiscountRatingResult - a model defined in huaweicloud sdk"""
        
        

        self._discount_id = None
        self._amount = None
        self._official_website_amount = None
        self._discount_amount = None
        self._measure_id = None
        self._discount_type = None
        self._discount_name = None
        self._best_offer = None
        self._product_rating_results = None
        self.discriminator = None

        if discount_id is not None:
            self.discount_id = discount_id
        if amount is not None:
            self.amount = amount
        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if discount_type is not None:
            self.discount_type = discount_type
        if discount_name is not None:
            self.discount_name = discount_name
        if best_offer is not None:
            self.best_offer = best_offer
        if product_rating_results is not None:
            self.product_rating_results = product_rating_results

    @property
    def discount_id(self):
        """Gets the discount_id of this OptionalDiscountRatingResult.

        |参数名称：折扣优惠Id| |参数约束及描述：折扣优惠Id|

        :return: The discount_id of this OptionalDiscountRatingResult.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        """Sets the discount_id of this OptionalDiscountRatingResult.

        |参数名称：折扣优惠Id| |参数约束及描述：折扣优惠Id|

        :param discount_id: The discount_id of this OptionalDiscountRatingResult.
        :type: str
        """
        self._discount_id = discount_id

    @property
    def amount(self):
        """Gets the amount of this OptionalDiscountRatingResult.

        |参数名称：总额，即最终优惠后的金额，amount= official_website_amount - discountAmount|

        :return: The amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OptionalDiscountRatingResult.

        |参数名称：总额，即最终优惠后的金额，amount= official_website_amount - discountAmount|

        :param amount: The amount of this OptionalDiscountRatingResult.
        :type: float
        """
        self._amount = amount

    @property
    def official_website_amount(self):
        """Gets the official_website_amount of this OptionalDiscountRatingResult.

        |参数名称：官网价| |参数约束及描述：官网价|

        :return: The official_website_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        """Sets the official_website_amount of this OptionalDiscountRatingResult.

        |参数名称：官网价| |参数约束及描述：官网价|

        :param official_website_amount: The official_website_amount of this OptionalDiscountRatingResult.
        :type: float
        """
        self._official_website_amount = official_website_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this OptionalDiscountRatingResult.

        |参数名称：优惠额| |参数约束及描述：（官网价和总价的差）|

        :return: The discount_amount of this OptionalDiscountRatingResult.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this OptionalDiscountRatingResult.

        |参数名称：优惠额| |参数约束及描述：（官网价和总价的差）|

        :param discount_amount: The discount_amount of this OptionalDiscountRatingResult.
        :type: float
        """
        self._discount_amount = discount_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this OptionalDiscountRatingResult.

        |参数名称：度量单位标识| |参数约束及描述：1：元|

        :return: The measure_id of this OptionalDiscountRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this OptionalDiscountRatingResult.

        |参数名称：度量单位标识| |参数约束及描述：1：元|

        :param measure_id: The measure_id of this OptionalDiscountRatingResult.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def discount_type(self):
        """Gets the discount_type of this OptionalDiscountRatingResult.

        |参数名称：折扣优惠类型：合同商务折扣：605(华为云BE场景下的合同商务折扣)、606(分销商BE场景下的合同商务折扣)伙伴授予折扣：607|

        :return: The discount_type of this OptionalDiscountRatingResult.
        :rtype: int
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this OptionalDiscountRatingResult.

        |参数名称：折扣优惠类型：合同商务折扣：605(华为云BE场景下的合同商务折扣)、606(分销商BE场景下的合同商务折扣)伙伴授予折扣：607|

        :param discount_type: The discount_type of this OptionalDiscountRatingResult.
        :type: int
        """
        self._discount_type = discount_type

    @property
    def discount_name(self):
        """Gets the discount_name of this OptionalDiscountRatingResult.

        |参数名称：折扣名称| |参数约束及描述：折扣名称|

        :return: The discount_name of this OptionalDiscountRatingResult.
        :rtype: str
        """
        return self._discount_name

    @discount_name.setter
    def discount_name(self, discount_name):
        """Sets the discount_name of this OptionalDiscountRatingResult.

        |参数名称：折扣名称| |参数约束及描述：折扣名称|

        :param discount_name: The discount_name of this OptionalDiscountRatingResult.
        :type: str
        """
        self._discount_name = discount_name

    @property
    def best_offer(self):
        """Gets the best_offer of this OptionalDiscountRatingResult.

        |参数名称：是否为最优折扣| |参数约束及描述：0：不是最优折扣；为缺省值。1：是最优折扣；最优折扣：在商务折扣、伙伴折扣中选择（优惠金额最大的折扣为最优，优惠金额相等则按此顺序排优先级），促销折扣，折扣券不参与最优折扣的计算|

        :return: The best_offer of this OptionalDiscountRatingResult.
        :rtype: int
        """
        return self._best_offer

    @best_offer.setter
    def best_offer(self, best_offer):
        """Sets the best_offer of this OptionalDiscountRatingResult.

        |参数名称：是否为最优折扣| |参数约束及描述：0：不是最优折扣；为缺省值。1：是最优折扣；最优折扣：在商务折扣、伙伴折扣中选择（优惠金额最大的折扣为最优，优惠金额相等则按此顺序排优先级），促销折扣，折扣券不参与最优折扣的计算|

        :param best_offer: The best_offer of this OptionalDiscountRatingResult.
        :type: int
        """
        self._best_offer = best_offer

    @property
    def product_rating_results(self):
        """Gets the product_rating_results of this OptionalDiscountRatingResult.

        |参数名称：产品询价结果| |参数的约束及描述：产品询价结果|

        :return: The product_rating_results of this OptionalDiscountRatingResult.
        :rtype: list[PeriodProductRatingResult]
        """
        return self._product_rating_results

    @product_rating_results.setter
    def product_rating_results(self, product_rating_results):
        """Sets the product_rating_results of this OptionalDiscountRatingResult.

        |参数名称：产品询价结果| |参数的约束及描述：产品询价结果|

        :param product_rating_results: The product_rating_results of this OptionalDiscountRatingResult.
        :type: list[PeriodProductRatingResult]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OptionalDiscountRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
