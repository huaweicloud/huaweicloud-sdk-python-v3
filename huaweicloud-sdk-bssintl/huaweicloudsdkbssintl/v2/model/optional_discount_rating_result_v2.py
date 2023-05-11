# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OptionalDiscountRatingResultV2:

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
        'amount': 'str',
        'official_website_amount': 'str',
        'discount_amount': 'str',
        'discount_type': 'int',
        'discount_name': 'str',
        'best_offer': 'int',
        'installment_official_website_amount': 'str',
        'installment_official_discount_amount': 'str',
        'installment_amount': 'str',
        'installment_period_type': 'int'
    }

    attribute_map = {
        'discount_id': 'discount_id',
        'amount': 'amount',
        'official_website_amount': 'official_website_amount',
        'discount_amount': 'discount_amount',
        'discount_type': 'discount_type',
        'discount_name': 'discount_name',
        'best_offer': 'best_offer',
        'installment_official_website_amount': 'installment_official_website_amount',
        'installment_official_discount_amount': 'installment_official_discount_amount',
        'installment_amount': 'installment_amount',
        'installment_period_type': 'installment_period_type'
    }

    def __init__(self, discount_id=None, amount=None, official_website_amount=None, discount_amount=None, discount_type=None, discount_name=None, best_offer=None, installment_official_website_amount=None, installment_official_discount_amount=None, installment_amount=None, installment_period_type=None):
        """OptionalDiscountRatingResultV2

        The model defined in huaweicloud sdk

        :param discount_id: |参数名称：折扣优惠ID| |参数约束及描述：折扣优惠ID|
        :type discount_id: str
        :param amount: |参数名称：总额，即最终优惠后的金额。单位为元。amount&#x3D; official_website_amount - discount_amount| |参数约束及描述：总额，即最终优惠后的金额。单位为元。amount&#x3D; official_website_amount - discount_amount|
        :type amount: str
        :param official_website_amount: |参数名称：官网价。单位为元| |参数约束及描述：官网价。单位为元|
        :type official_website_amount: str
        :param discount_amount: |参数名称：可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。单位为| |参数约束及描述：可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。单位为|
        :type discount_amount: str
        :param discount_type: |参数名称：折扣优惠类型。合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣伙伴授予折扣：607：合作伙伴授予折扣-折扣率| |参数的约束及描述：折扣优惠类型。合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣伙伴授予折扣：607：合作伙伴授予折扣-折扣率|
        :type discount_type: int
        :param discount_name: |参数名称：折扣名称| |参数约束及描述：折扣名称|
        :type discount_name: str
        :param best_offer: |参数名称：是否为最优折扣。0：不是最优折扣，为缺省值。1：是最优折扣最优折扣：在商务折扣、伙伴折扣中选择（优惠金额最大的折扣为最优，优惠金额相等则按此顺序排优先级），促销折扣，折扣券不参与最优折扣的计算| |参数的约束及描述：是否为最优折扣。0：不是最优折扣，为缺省值。1：是最优折扣最优折扣：在商务折扣、伙伴折扣中选择（优惠金额最大的折扣为最优，优惠金额相等则按此顺序排优先级），促销折扣，折扣券不参与最优折扣的计算|
        :type best_offer: int
        :param installment_official_website_amount: |参数名称：分期金额的官网价。单位为元| |参数约束及描述：分期金额的官网价。单位为元|
        :type installment_official_website_amount: str
        :param installment_official_discount_amount: |参数名称：分期金额的折扣价。单位为元| |参数约束及描述：分期金额的折扣价。单位为元|
        :type installment_official_discount_amount: str
        :param installment_amount: |参数名称：分期金额的成交价。单位为元| |参数约束及描述：分期金额的成交价。单位为元|
        :type installment_amount: str
        :param installment_period_type: |参数名称：分期付款的周期类型。2：月| |参数的约束及描述：分期付款的周期类型。2：月|
        :type installment_period_type: int
        """
        
        

        self._discount_id = None
        self._amount = None
        self._official_website_amount = None
        self._discount_amount = None
        self._discount_type = None
        self._discount_name = None
        self._best_offer = None
        self._installment_official_website_amount = None
        self._installment_official_discount_amount = None
        self._installment_amount = None
        self._installment_period_type = None
        self.discriminator = None

        if discount_id is not None:
            self.discount_id = discount_id
        if amount is not None:
            self.amount = amount
        if official_website_amount is not None:
            self.official_website_amount = official_website_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if discount_type is not None:
            self.discount_type = discount_type
        if discount_name is not None:
            self.discount_name = discount_name
        if best_offer is not None:
            self.best_offer = best_offer
        if installment_official_website_amount is not None:
            self.installment_official_website_amount = installment_official_website_amount
        if installment_official_discount_amount is not None:
            self.installment_official_discount_amount = installment_official_discount_amount
        if installment_amount is not None:
            self.installment_amount = installment_amount
        if installment_period_type is not None:
            self.installment_period_type = installment_period_type

    @property
    def discount_id(self):
        """Gets the discount_id of this OptionalDiscountRatingResultV2.

        |参数名称：折扣优惠ID| |参数约束及描述：折扣优惠ID|

        :return: The discount_id of this OptionalDiscountRatingResultV2.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        """Sets the discount_id of this OptionalDiscountRatingResultV2.

        |参数名称：折扣优惠ID| |参数约束及描述：折扣优惠ID|

        :param discount_id: The discount_id of this OptionalDiscountRatingResultV2.
        :type discount_id: str
        """
        self._discount_id = discount_id

    @property
    def amount(self):
        """Gets the amount of this OptionalDiscountRatingResultV2.

        |参数名称：总额，即最终优惠后的金额。单位为元。amount= official_website_amount - discount_amount| |参数约束及描述：总额，即最终优惠后的金额。单位为元。amount= official_website_amount - discount_amount|

        :return: The amount of this OptionalDiscountRatingResultV2.
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this OptionalDiscountRatingResultV2.

        |参数名称：总额，即最终优惠后的金额。单位为元。amount= official_website_amount - discount_amount| |参数约束及描述：总额，即最终优惠后的金额。单位为元。amount= official_website_amount - discount_amount|

        :param amount: The amount of this OptionalDiscountRatingResultV2.
        :type amount: str
        """
        self._amount = amount

    @property
    def official_website_amount(self):
        """Gets the official_website_amount of this OptionalDiscountRatingResultV2.

        |参数名称：官网价。单位为元| |参数约束及描述：官网价。单位为元|

        :return: The official_website_amount of this OptionalDiscountRatingResultV2.
        :rtype: str
        """
        return self._official_website_amount

    @official_website_amount.setter
    def official_website_amount(self, official_website_amount):
        """Sets the official_website_amount of this OptionalDiscountRatingResultV2.

        |参数名称：官网价。单位为元| |参数约束及描述：官网价。单位为元|

        :param official_website_amount: The official_website_amount of this OptionalDiscountRatingResultV2.
        :type official_website_amount: str
        """
        self._official_website_amount = official_website_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this OptionalDiscountRatingResultV2.

        |参数名称：可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。单位为| |参数约束及描述：可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。单位为|

        :return: The discount_amount of this OptionalDiscountRatingResultV2.
        :rtype: str
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this OptionalDiscountRatingResultV2.

        |参数名称：可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。单位为| |参数约束及描述：可选折扣优惠额，如商务折扣、伙伴折扣、促销折扣和折扣券选用时的优惠额。单位为|

        :param discount_amount: The discount_amount of this OptionalDiscountRatingResultV2.
        :type discount_amount: str
        """
        self._discount_amount = discount_amount

    @property
    def discount_type(self):
        """Gets the discount_type of this OptionalDiscountRatingResultV2.

        |参数名称：折扣优惠类型。合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣伙伴授予折扣：607：合作伙伴授予折扣-折扣率| |参数的约束及描述：折扣优惠类型。合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣伙伴授予折扣：607：合作伙伴授予折扣-折扣率|

        :return: The discount_type of this OptionalDiscountRatingResultV2.
        :rtype: int
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this OptionalDiscountRatingResultV2.

        |参数名称：折扣优惠类型。合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣伙伴授予折扣：607：合作伙伴授予折扣-折扣率| |参数的约束及描述：折扣优惠类型。合同商务折扣：605：华为云BE场景下的合同商务折扣606：分销商BE场景下的合同商务折扣伙伴授予折扣：607：合作伙伴授予折扣-折扣率|

        :param discount_type: The discount_type of this OptionalDiscountRatingResultV2.
        :type discount_type: int
        """
        self._discount_type = discount_type

    @property
    def discount_name(self):
        """Gets the discount_name of this OptionalDiscountRatingResultV2.

        |参数名称：折扣名称| |参数约束及描述：折扣名称|

        :return: The discount_name of this OptionalDiscountRatingResultV2.
        :rtype: str
        """
        return self._discount_name

    @discount_name.setter
    def discount_name(self, discount_name):
        """Sets the discount_name of this OptionalDiscountRatingResultV2.

        |参数名称：折扣名称| |参数约束及描述：折扣名称|

        :param discount_name: The discount_name of this OptionalDiscountRatingResultV2.
        :type discount_name: str
        """
        self._discount_name = discount_name

    @property
    def best_offer(self):
        """Gets the best_offer of this OptionalDiscountRatingResultV2.

        |参数名称：是否为最优折扣。0：不是最优折扣，为缺省值。1：是最优折扣最优折扣：在商务折扣、伙伴折扣中选择（优惠金额最大的折扣为最优，优惠金额相等则按此顺序排优先级），促销折扣，折扣券不参与最优折扣的计算| |参数的约束及描述：是否为最优折扣。0：不是最优折扣，为缺省值。1：是最优折扣最优折扣：在商务折扣、伙伴折扣中选择（优惠金额最大的折扣为最优，优惠金额相等则按此顺序排优先级），促销折扣，折扣券不参与最优折扣的计算|

        :return: The best_offer of this OptionalDiscountRatingResultV2.
        :rtype: int
        """
        return self._best_offer

    @best_offer.setter
    def best_offer(self, best_offer):
        """Sets the best_offer of this OptionalDiscountRatingResultV2.

        |参数名称：是否为最优折扣。0：不是最优折扣，为缺省值。1：是最优折扣最优折扣：在商务折扣、伙伴折扣中选择（优惠金额最大的折扣为最优，优惠金额相等则按此顺序排优先级），促销折扣，折扣券不参与最优折扣的计算| |参数的约束及描述：是否为最优折扣。0：不是最优折扣，为缺省值。1：是最优折扣最优折扣：在商务折扣、伙伴折扣中选择（优惠金额最大的折扣为最优，优惠金额相等则按此顺序排优先级），促销折扣，折扣券不参与最优折扣的计算|

        :param best_offer: The best_offer of this OptionalDiscountRatingResultV2.
        :type best_offer: int
        """
        self._best_offer = best_offer

    @property
    def installment_official_website_amount(self):
        """Gets the installment_official_website_amount of this OptionalDiscountRatingResultV2.

        |参数名称：分期金额的官网价。单位为元| |参数约束及描述：分期金额的官网价。单位为元|

        :return: The installment_official_website_amount of this OptionalDiscountRatingResultV2.
        :rtype: str
        """
        return self._installment_official_website_amount

    @installment_official_website_amount.setter
    def installment_official_website_amount(self, installment_official_website_amount):
        """Sets the installment_official_website_amount of this OptionalDiscountRatingResultV2.

        |参数名称：分期金额的官网价。单位为元| |参数约束及描述：分期金额的官网价。单位为元|

        :param installment_official_website_amount: The installment_official_website_amount of this OptionalDiscountRatingResultV2.
        :type installment_official_website_amount: str
        """
        self._installment_official_website_amount = installment_official_website_amount

    @property
    def installment_official_discount_amount(self):
        """Gets the installment_official_discount_amount of this OptionalDiscountRatingResultV2.

        |参数名称：分期金额的折扣价。单位为元| |参数约束及描述：分期金额的折扣价。单位为元|

        :return: The installment_official_discount_amount of this OptionalDiscountRatingResultV2.
        :rtype: str
        """
        return self._installment_official_discount_amount

    @installment_official_discount_amount.setter
    def installment_official_discount_amount(self, installment_official_discount_amount):
        """Sets the installment_official_discount_amount of this OptionalDiscountRatingResultV2.

        |参数名称：分期金额的折扣价。单位为元| |参数约束及描述：分期金额的折扣价。单位为元|

        :param installment_official_discount_amount: The installment_official_discount_amount of this OptionalDiscountRatingResultV2.
        :type installment_official_discount_amount: str
        """
        self._installment_official_discount_amount = installment_official_discount_amount

    @property
    def installment_amount(self):
        """Gets the installment_amount of this OptionalDiscountRatingResultV2.

        |参数名称：分期金额的成交价。单位为元| |参数约束及描述：分期金额的成交价。单位为元|

        :return: The installment_amount of this OptionalDiscountRatingResultV2.
        :rtype: str
        """
        return self._installment_amount

    @installment_amount.setter
    def installment_amount(self, installment_amount):
        """Sets the installment_amount of this OptionalDiscountRatingResultV2.

        |参数名称：分期金额的成交价。单位为元| |参数约束及描述：分期金额的成交价。单位为元|

        :param installment_amount: The installment_amount of this OptionalDiscountRatingResultV2.
        :type installment_amount: str
        """
        self._installment_amount = installment_amount

    @property
    def installment_period_type(self):
        """Gets the installment_period_type of this OptionalDiscountRatingResultV2.

        |参数名称：分期付款的周期类型。2：月| |参数的约束及描述：分期付款的周期类型。2：月|

        :return: The installment_period_type of this OptionalDiscountRatingResultV2.
        :rtype: int
        """
        return self._installment_period_type

    @installment_period_type.setter
    def installment_period_type(self, installment_period_type):
        """Sets the installment_period_type of this OptionalDiscountRatingResultV2.

        |参数名称：分期付款的周期类型。2：月| |参数的约束及描述：分期付款的周期类型。2：月|

        :param installment_period_type: The installment_period_type of this OptionalDiscountRatingResultV2.
        :type installment_period_type: int
        """
        self._installment_period_type = installment_period_type

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
        if not isinstance(other, OptionalDiscountRatingResultV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
