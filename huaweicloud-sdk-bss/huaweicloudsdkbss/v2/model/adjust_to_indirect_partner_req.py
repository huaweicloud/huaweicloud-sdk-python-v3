# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        """AdjustToIndirectPartnerReq

        The model defined in huaweicloud sdk

        :param indirect_partner_id: 云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。
        :type indirect_partner_id: str
        :param amount: 华为云总经销商向云经销商拨款的金额。 单位：元。取值大于0且精确到小数点后2位。
        :type amount: float
        """
        
        

        self._indirect_partner_id = None
        self._amount = None
        self.discriminator = None

        self.indirect_partner_id = indirect_partner_id
        self.amount = amount

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this AdjustToIndirectPartnerReq.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。

        :return: The indirect_partner_id of this AdjustToIndirectPartnerReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this AdjustToIndirectPartnerReq.

        云经销商ID。获取方法请参见[查询云经销商列表](https://support.huaweicloud.com/api-bpconsole/espp_00003.html)。

        :param indirect_partner_id: The indirect_partner_id of this AdjustToIndirectPartnerReq.
        :type indirect_partner_id: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def amount(self):
        """Gets the amount of this AdjustToIndirectPartnerReq.

        华为云总经销商向云经销商拨款的金额。 单位：元。取值大于0且精确到小数点后2位。

        :return: The amount of this AdjustToIndirectPartnerReq.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AdjustToIndirectPartnerReq.

        华为云总经销商向云经销商拨款的金额。 单位：元。取值大于0且精确到小数点后2位。

        :param amount: The amount of this AdjustToIndirectPartnerReq.
        :type amount: float
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
        if not isinstance(other, AdjustToIndirectPartnerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
