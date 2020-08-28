# coding: utf-8

import pprint
import re

import six





class SetSubCustomerDiscountV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'discount': 'float',
        'effective_time': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'discount': 'discount',
        'effective_time': 'effective_time',
        'expire_time': 'expire_time'
    }

    def __init__(self, customer_id=None, discount=None, effective_time=None, expire_time=None):
        """SetSubCustomerDiscountV2 - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._discount = None
        self._effective_time = None
        self._expire_time = None
        self.discriminator = None

        self.customer_id = customer_id
        self.discount = discount
        if effective_time is not None:
            self.effective_time = effective_time
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def customer_id(self):
        """Gets the customer_id of this SetSubCustomerDiscountV2.

        |参数名称：客户ID| |参数约束及描述：客户ID|

        :return: The customer_id of this SetSubCustomerDiscountV2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SetSubCustomerDiscountV2.

        |参数名称：客户ID| |参数约束及描述：客户ID|

        :param customer_id: The customer_id of this SetSubCustomerDiscountV2.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def discount(self):
        """Gets the discount of this SetSubCustomerDiscountV2.

        |参数名称：折扣率，最高精确到4位小数。折扣范围：0.8~1。如果折扣率是85%，则折扣率写成0.85。注意：折扣为1表示不打折，相当于删除伙伴折扣。| |参数的约束及描述：折扣率，最高精确到4位小数。折扣范围：0.8~1。如果折扣率是85%，则折扣率写成0.85。注意：折扣为1表示不打折，相当于删除伙伴折扣。|

        :return: The discount of this SetSubCustomerDiscountV2.
        :rtype: float
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """Sets the discount of this SetSubCustomerDiscountV2.

        |参数名称：折扣率，最高精确到4位小数。折扣范围：0.8~1。如果折扣率是85%，则折扣率写成0.85。注意：折扣为1表示不打折，相当于删除伙伴折扣。| |参数的约束及描述：折扣率，最高精确到4位小数。折扣范围：0.8~1。如果折扣率是85%，则折扣率写成0.85。注意：折扣为1表示不打折，相当于删除伙伴折扣。|

        :param discount: The discount of this SetSubCustomerDiscountV2.
        :type: float
        """
        self._discount = discount

    @property
    def effective_time(self):
        """Gets the effective_time of this SetSubCustomerDiscountV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The effective_time of this SetSubCustomerDiscountV2.
        :rtype: str
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        """Sets the effective_time of this SetSubCustomerDiscountV2.

        |参数名称：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：生效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param effective_time: The effective_time of this SetSubCustomerDiscountV2.
        :type: str
        """
        self._effective_time = effective_time

    @property
    def expire_time(self):
        """Gets the expire_time of this SetSubCustomerDiscountV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :return: The expire_time of this SetSubCustomerDiscountV2.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this SetSubCustomerDiscountV2.

        |参数名称：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ| |参数约束及描述：失效时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ|

        :param expire_time: The expire_time of this SetSubCustomerDiscountV2.
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
        if not isinstance(other, SetSubCustomerDiscountV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
