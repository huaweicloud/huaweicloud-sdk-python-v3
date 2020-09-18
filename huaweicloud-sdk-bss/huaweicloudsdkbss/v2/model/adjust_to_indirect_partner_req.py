# coding: utf-8

import pprint
import re

import six





class AdjustToIndirectPartnerReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'indirect_partner_id': 'str',
        'amount': 'float'
    }

    attribute_map = {
        'indirect_partner_id': 'indirect_partner_id',
        'amount': 'amount'
    }

    def __init__(self, indirect_partner_id=None, amount=None):
        """AdjustToIndirectPartnerReq - a model defined in huaweicloud sdk"""
        
        

        self._indirect_partner_id = None
        self._amount = None
        self.discriminator = None

        self.indirect_partner_id = indirect_partner_id
        self.amount = amount

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this AdjustToIndirectPartnerReq.

        |参数名称：合作伙伴关联的二级经销商伙伴ID。| |参数约束及描述：必填，最大长度64，合作伙伴关联的二级经销商伙伴ID。|

        :return: The indirect_partner_id of this AdjustToIndirectPartnerReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this AdjustToIndirectPartnerReq.

        |参数名称：合作伙伴关联的二级经销商伙伴ID。| |参数约束及描述：必填，最大长度64，合作伙伴关联的二级经销商伙伴ID。|

        :param indirect_partner_id: The indirect_partner_id of this AdjustToIndirectPartnerReq.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def amount(self):
        """Gets the amount of this AdjustToIndirectPartnerReq.

        |参数名称：授信金额。单位为元不能为负数，精确到小数点后两位。| |参数的约束及描述：授信金额。单位为元不能为负数，精确到小数点后两位。|

        :return: The amount of this AdjustToIndirectPartnerReq.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AdjustToIndirectPartnerReq.

        |参数名称：授信金额。单位为元不能为负数，精确到小数点后两位。| |参数的约束及描述：授信金额。单位为元不能为负数，精确到小数点后两位。|

        :param amount: The amount of this AdjustToIndirectPartnerReq.
        :type: float
        """
        self._amount = amount

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
        if not isinstance(other, AdjustToIndirectPartnerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
