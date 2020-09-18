# coding: utf-8

import pprint
import re

import six





class AdjustAccountReq:


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
        'amount': 'float',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'amount': 'amount',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, amount=None, indirect_partner_id=None):
        """AdjustAccountReq - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._amount = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.customer_id = customer_id
        self.amount = amount
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this AdjustAccountReq.

        |参数名称：合作伙伴关联的客户的客户ID。| |参数约束及描述：合作伙伴关联的客户的客户ID。|

        :return: The customer_id of this AdjustAccountReq.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AdjustAccountReq.

        |参数名称：合作伙伴关联的客户的客户ID。| |参数约束及描述：合作伙伴关联的客户的客户ID。|

        :param customer_id: The customer_id of this AdjustAccountReq.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def amount(self):
        """Gets the amount of this AdjustAccountReq.

        |参数名称：授信金额。单位为元不能为负数，精确到小数点后两位。| |参数的约束及描述：授信金额。单位为元不能为负数，精确到小数点后两位。|

        :return: The amount of this AdjustAccountReq.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AdjustAccountReq.

        |参数名称：授信金额。单位为元不能为负数，精确到小数点后两位。| |参数的约束及描述：授信金额。单位为元不能为负数，精确到小数点后两位。|

        :param amount: The amount of this AdjustAccountReq.
        :type: float
        """
        self._amount = amount

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this AdjustAccountReq.

        |参数名称：二级经销商ID。| |参数约束及描述：二级经销商ID，如果一级经销商要给二级经销商的子客户设置折扣，需要携带这个字段。|

        :return: The indirect_partner_id of this AdjustAccountReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this AdjustAccountReq.

        |参数名称：二级经销商ID。| |参数约束及描述：二级经销商ID，如果一级经销商要给二级经销商的子客户设置折扣，需要携带这个字段。|

        :param indirect_partner_id: The indirect_partner_id of this AdjustAccountReq.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, AdjustAccountReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
