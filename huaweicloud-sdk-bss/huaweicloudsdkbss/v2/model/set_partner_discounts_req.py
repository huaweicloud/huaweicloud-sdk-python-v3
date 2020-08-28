# coding: utf-8

import pprint
import re

import six





class SetPartnerDiscountsReq:


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
        'sub_customer_discounts': 'list[SetSubCustomerDiscountV2]'
    }

    attribute_map = {
        'indirect_partner_id': 'indirect_partner_id',
        'sub_customer_discounts': 'sub_customer_discounts'
    }

    def __init__(self, indirect_partner_id=None, sub_customer_discounts=None):
        """SetPartnerDiscountsReq - a model defined in huaweicloud sdk"""
        
        

        self._indirect_partner_id = None
        self._sub_customer_discounts = None
        self.discriminator = None

        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        self.sub_customer_discounts = sub_customer_discounts

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this SetPartnerDiscountsReq.

        |参数名称：二级经销商ID| |参数约束及描述：一级经销商给二级经销商的子客户设置折扣时需要携带这个字段。|

        :return: The indirect_partner_id of this SetPartnerDiscountsReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this SetPartnerDiscountsReq.

        |参数名称：二级经销商ID| |参数约束及描述：一级经销商给二级经销商的子客户设置折扣时需要携带这个字段。|

        :param indirect_partner_id: The indirect_partner_id of this SetPartnerDiscountsReq.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def sub_customer_discounts(self):
        """Gets the sub_customer_discounts of this SetPartnerDiscountsReq.

        |参数名称：客户折扣信息列表，最大支持10个。| |参数约束以及描述：客户折扣信息列表，最大支持10个。|

        :return: The sub_customer_discounts of this SetPartnerDiscountsReq.
        :rtype: list[SetSubCustomerDiscountV2]
        """
        return self._sub_customer_discounts

    @sub_customer_discounts.setter
    def sub_customer_discounts(self, sub_customer_discounts):
        """Sets the sub_customer_discounts of this SetPartnerDiscountsReq.

        |参数名称：客户折扣信息列表，最大支持10个。| |参数约束以及描述：客户折扣信息列表，最大支持10个。|

        :param sub_customer_discounts: The sub_customer_discounts of this SetPartnerDiscountsReq.
        :type: list[SetSubCustomerDiscountV2]
        """
        self._sub_customer_discounts = sub_customer_discounts

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
        if not isinstance(other, SetPartnerDiscountsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
