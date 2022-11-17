# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiscountItemV2:

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
        """DiscountItemV2

        The model defined in huaweicloud sdk

        :param discount_type: 折扣类型： 200：促销产品折扣300：促销折扣券301：促销代金券302：促销现金券500：代理订购指定折扣501：代理订购指定减免502：代理订购指定一口价600：折扣返利合同601：渠道框架合同602：专款专用合同603：线下直签合同604：电销授权合同605：商务合同折扣606：渠道商务合同折扣607：合作伙伴授权折扣609：订单调价折扣610：免单金额700：促销折扣800：充值帐户折扣900：产品本身折扣901：基准价一口价的折扣
        :type discount_type: str
        :param discount_amount: 折扣金额。
        :type discount_amount: float
        """
        
        

        self._discount_type = None
        self._discount_amount = None
        self.discriminator = None

        if discount_type is not None:
            self.discount_type = discount_type
        if discount_amount is not None:
            self.discount_amount = discount_amount

    @property
    def discount_type(self):
        """Gets the discount_type of this DiscountItemV2.

        折扣类型： 200：促销产品折扣300：促销折扣券301：促销代金券302：促销现金券500：代理订购指定折扣501：代理订购指定减免502：代理订购指定一口价600：折扣返利合同601：渠道框架合同602：专款专用合同603：线下直签合同604：电销授权合同605：商务合同折扣606：渠道商务合同折扣607：合作伙伴授权折扣609：订单调价折扣610：免单金额700：促销折扣800：充值帐户折扣900：产品本身折扣901：基准价一口价的折扣

        :return: The discount_type of this DiscountItemV2.
        :rtype: str
        """
        return self._discount_type

    @discount_type.setter
    def discount_type(self, discount_type):
        """Sets the discount_type of this DiscountItemV2.

        折扣类型： 200：促销产品折扣300：促销折扣券301：促销代金券302：促销现金券500：代理订购指定折扣501：代理订购指定减免502：代理订购指定一口价600：折扣返利合同601：渠道框架合同602：专款专用合同603：线下直签合同604：电销授权合同605：商务合同折扣606：渠道商务合同折扣607：合作伙伴授权折扣609：订单调价折扣610：免单金额700：促销折扣800：充值帐户折扣900：产品本身折扣901：基准价一口价的折扣

        :param discount_type: The discount_type of this DiscountItemV2.
        :type discount_type: str
        """
        self._discount_type = discount_type

    @property
    def discount_amount(self):
        """Gets the discount_amount of this DiscountItemV2.

        折扣金额。

        :return: The discount_amount of this DiscountItemV2.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this DiscountItemV2.

        折扣金额。

        :param discount_amount: The discount_amount of this DiscountItemV2.
        :type discount_amount: float
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
        if not isinstance(other, DiscountItemV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
