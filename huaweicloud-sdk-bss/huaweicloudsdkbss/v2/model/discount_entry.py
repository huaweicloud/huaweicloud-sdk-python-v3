# coding: utf-8

import pprint
import re

import six





class DiscountEntry:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'discount_type': 'str',
        'discount_amount': 'float'
    }

    attribute_map = {
        'discount_type': 'discount_type',
        'discount_amount': 'discount_amount'
    }

    def __init__(self, discount_type=None, discount_amount=None):
        """DiscountEntry - a model defined in huaweicloud sdk"""
        
        

        self._discount_type = None
        self._discount_amount = None
        self.discriminator = None

        if discount_type is not None:
            self.discount_type = discount_type
        if discount_amount is not None:
            self.discount_amount = discount_amount

    @property
    def discount_type(self):
        """Gets the discount_type of this DiscountEntry.

        |参数名称：折扣类型：200：促销产品折扣；300：促销折扣券；301：促销代金券；302：促销现金券；500：代理订购指定折扣；501：代理订购指定减免；502：代理订购指定一口价；600：折扣返利合同；601：渠道框架合同；602：专款专用合同；603：线下直签合同；604：电销授权合同；605：商务合同折扣；606：渠道商务合同折扣；607：合作伙伴授权折扣；609：订单调价折扣；700：促销折扣；800：充值帐户折扣；| |参数约束及描述：折扣类型：200：促销产品折扣；300：促销折扣券；301：促销代金券；302：促销现金券；500：代理订购指定折扣；501：代理订购指定减免；502：代理订购指定一口价；600：折扣返利合同；601：渠道框架合同；602：专款专用合同；603：线下直签合同；604：电销授权合同；605：商务合同折扣；606：渠道商务合同折扣；607：合作伙伴授权折扣；609：订单调价折扣；700：促销折扣；800：充值帐户折扣；|

        :return: The discount_type of this DiscountEntry.
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this DiscountEntry.

        |参数名称：折扣类型：200：促销产品折扣；300：促销折扣券；301：促销代金券；302：促销现金券；500：代理订购指定折扣；501：代理订购指定减免；502：代理订购指定一口价；600：折扣返利合同；601：渠道框架合同；602：专款专用合同；603：线下直签合同；604：电销授权合同；605：商务合同折扣；606：渠道商务合同折扣；607：合作伙伴授权折扣；609：订单调价折扣；700：促销折扣；800：充值帐户折扣；| |参数约束及描述：折扣类型：200：促销产品折扣；300：促销折扣券；301：促销代金券；302：促销现金券；500：代理订购指定折扣；501：代理订购指定减免；502：代理订购指定一口价；600：折扣返利合同；601：渠道框架合同；602：专款专用合同；603：线下直签合同；604：电销授权合同；605：商务合同折扣；606：渠道商务合同折扣；607：合作伙伴授权折扣；609：订单调价折扣；700：促销折扣；800：充值帐户折扣；|

        :param discount_type: The discount_type of this DiscountEntry.
        :type: str
        """
        self._discount_type = discount_type

    @property
    def discount_amount(self):
        """Gets the discount_amount of this DiscountEntry.

        |参数名称：折扣金额| |参数的约束及描述：折扣金额|

        :return: The discount_amount of this DiscountEntry.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this DiscountEntry.

        |参数名称：折扣金额| |参数的约束及描述：折扣金额|

        :param discount_amount: The discount_amount of this DiscountEntry.
        :type: float
        """
        self._discount_amount = discount_amount

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
        if not isinstance(other, DiscountEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
