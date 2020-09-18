# coding: utf-8

import pprint
import re

import six





class QuerySubCustomerDiscountV2:


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
        'discount': 'float',
        'effective_time': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'discount_id': 'discount_id',
        'discount': 'discount',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time'
    }

    def __init__(self, discount_id=None, discount=None, effective_time=None, expire_time=None):
        """QuerySubCustomerDiscountV2 - a model defined in huaweicloud sdk"""
        
        

        self._discount_id = None
        self._discount = None
        self._effective_time = None
        self._expire_time = None
        self.discriminator = None

        if discount_id is not None:
            self.discount_id = discount_id
        if discount is not None:
            self.discount = discount
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def discount_id(self):
        """Gets the discount_id of this QuerySubCustomerDiscountV2.

        |参数名称：折扣ID，唯一的表示一条折扣信息。| |参数约束及描述：折扣ID，唯一的表示一条折扣信息。|

        :return: The discount_id of this QuerySubCustomerDiscountV2.
        :rtype: str
        """
        return self._discount_id

    @discount_id.setter
    def discount_id(self, discount_id):
        """Sets the discount_id of this QuerySubCustomerDiscountV2.

        |参数名称：折扣ID，唯一的表示一条折扣信息。| |参数约束及描述：折扣ID，唯一的表示一条折扣信息。|

        :param discount_id: The discount_id of this QuerySubCustomerDiscountV2.
        :type: str
        """
        self._discount_id = discount_id

    @property
    def discount(self):
        """Gets the discount of this QuerySubCustomerDiscountV2.

        |参数名称：折扣率，精确到4位小数。如果折扣率是22%，则折扣率写成0.22。| |参数的约束及描述：折扣率，精确到4位小数。如果折扣率是22%，则折扣率写成0.22。|

        :return: The discount of this QuerySubCustomerDiscountV2.
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this QuerySubCustomerDiscountV2.

        |参数名称：折扣率，精确到4位小数。如果折扣率是22%，则折扣率写成0.22。| |参数的约束及描述：折扣率，精确到4位小数。如果折扣率是22%，则折扣率写成0.22。|

        :param discount: The discount of this QuerySubCustomerDiscountV2.
        :type: float
        """
        self._discount = discount

    @property
    def effective_time(self):
        """Gets the effective_time of this QuerySubCustomerDiscountV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”|

        :return: The effective_time of this QuerySubCustomerDiscountV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this QuerySubCustomerDiscountV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”|

        :param effective_time: The effective_time of this QuerySubCustomerDiscountV2.
        :type: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this QuerySubCustomerDiscountV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”|

        :return: The expire_time of this QuerySubCustomerDiscountV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this QuerySubCustomerDiscountV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”|

        :param expire_time: The expire_time of this QuerySubCustomerDiscountV2.
        :type: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, QuerySubCustomerDiscountV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
