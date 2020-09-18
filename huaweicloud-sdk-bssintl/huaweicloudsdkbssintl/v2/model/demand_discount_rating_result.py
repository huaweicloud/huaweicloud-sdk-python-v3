# coding: utf-8

import pprint
import re

import six





class DemandDiscountRatingResult:


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
        'discount_type': 'int',
        'amount': 'float',
        'measure_id': 'int',
        'discount_name': 'str'
    }

    attribute_map = {
        'discount_id': 'discount_id',
        'discount_type': 'discount_type',
        'amount': 'amount',
        'measure_id': 'measure_id',
        'discount_name': 'discount_name'
    }

    def __init__(self, discount_id=None, discount_type=None, amount=None, measure_id=None, discount_name=None):
        """DemandDiscountRatingResult - a model defined in huaweicloud sdk"""
        
        

        self._discount_id = None
        self._discount_type = None
        self._amount = None
        self._measure_id = None
        self._discount_name = None
        self.discriminator = None

        if discount_id is not None:
            self.discount_id = discount_id
        if discount_type is not None:
            self.discount_type = discount_type
        if amount is not None:
            self.amount = amount
        if measure_id is not None:
            self.measure_id = measure_id
        if discount_name is not None:
            self.discount_name = discount_name

    @property
    def discount_id(self):
        """Gets the discount_id of this DemandDiscountRatingResult.

        |参数名称：优惠标识ID| |参数约束及描述：优惠标识ID|

        :return: The discount_id of this DemandDiscountRatingResult.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        """Sets the discount_id of this DemandDiscountRatingResult.

        |参数名称：优惠标识ID| |参数约束及描述：优惠标识ID|

        :param discount_id: The discount_id of this DemandDiscountRatingResult.
        :type: str
        """
        self._discount_id = discount_id

    @property
    def discount_type(self):
        """Gets the discount_type of this DemandDiscountRatingResult.

        |参数名称：合同商务优惠类型：基于官网价计算优惠605 华为云商务-折扣率，一口价，华为云用户606 渠道商务-折扣率，一口价，BP用户伙伴折扣优惠类型：基于官网价计算优惠607 合作伙伴授予折扣-折扣率|

        :return: The discount_type of this DemandDiscountRatingResult.
        :rtype: int
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this DemandDiscountRatingResult.

        |参数名称：合同商务优惠类型：基于官网价计算优惠605 华为云商务-折扣率，一口价，华为云用户606 渠道商务-折扣率，一口价，BP用户伙伴折扣优惠类型：基于官网价计算优惠607 合作伙伴授予折扣-折扣率|

        :param discount_type: The discount_type of this DemandDiscountRatingResult.
        :type: int
        """
        self._discount_type = discount_type

    @property
    def amount(self):
        """Gets the amount of this DemandDiscountRatingResult.

        优惠金额

        :return: The amount of this DemandDiscountRatingResult.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DemandDiscountRatingResult.

        优惠金额

        :param amount: The amount of this DemandDiscountRatingResult.
        :type: float
        """
        self._amount = amount

    @property
    def measure_id(self):
        """Gets the measure_id of this DemandDiscountRatingResult.

        |参数名称：度量单位标识| |参数约束及描述：1：元|

        :return: The measure_id of this DemandDiscountRatingResult.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this DemandDiscountRatingResult.

        |参数名称：度量单位标识| |参数约束及描述：1：元|

        :param measure_id: The measure_id of this DemandDiscountRatingResult.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def discount_name(self):
        """Gets the discount_name of this DemandDiscountRatingResult.

        |参数名称：折扣名称| |参数约束及描述：折扣名称|

        :return: The discount_name of this DemandDiscountRatingResult.
        :rtype: str
        """
        return self._discount_name

    @discount_name.setter
    def discount_name(self, discount_name):
        """Sets the discount_name of this DemandDiscountRatingResult.

        |参数名称：折扣名称| |参数约束及描述：折扣名称|

        :param discount_name: The discount_name of this DemandDiscountRatingResult.
        :type: str
        """
        self._discount_name = discount_name

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
        if not isinstance(other, DemandDiscountRatingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
