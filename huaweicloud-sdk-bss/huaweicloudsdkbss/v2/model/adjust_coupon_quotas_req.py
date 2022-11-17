# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdjustCouponQuotasReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_id': 'str',
        'indirect_partner_ids': 'list[str]',
        'quota_amount': 'float'
    }

    attribute_map = {
        'quota_id': 'quota_id',
        'indirect_partner_ids': 'indirect_partner_ids',
        'quota_amount': 'quota_amount'
    }

    def __init__(self, quota_id=None, indirect_partner_ids=None, quota_amount=None):
        """AdjustCouponQuotasReq

        The model defined in huaweicloud sdk

        :param quota_id: 华为云总经销商发放的代金券额度的ID。获取方法请参见查询优惠券额度。
        :type quota_id: str
        :param indirect_partner_ids: 云经销商ID列表。
        :type indirect_partner_ids: list[str]
        :param quota_amount: 华为云总经销商向云经销商发放的代金券额度值。 单位：元。取值大于0且精确到小数点后2位。
        :type quota_amount: float
        """
        
        

        self._quota_id = None
        self._indirect_partner_ids = None
        self._quota_amount = None
        self.discriminator = None

        self.quota_id = quota_id
        self.indirect_partner_ids = indirect_partner_ids
        self.quota_amount = quota_amount

    @property
    def quota_id(self):
        """Gets the quota_id of this AdjustCouponQuotasReq.

        华为云总经销商发放的代金券额度的ID。获取方法请参见查询优惠券额度。

        :return: The quota_id of this AdjustCouponQuotasReq.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this AdjustCouponQuotasReq.

        华为云总经销商发放的代金券额度的ID。获取方法请参见查询优惠券额度。

        :param quota_id: The quota_id of this AdjustCouponQuotasReq.
        :type quota_id: str
        """
        self._quota_id = quota_id

    @property
    def indirect_partner_ids(self):
        """Gets the indirect_partner_ids of this AdjustCouponQuotasReq.

        云经销商ID列表。

        :return: The indirect_partner_ids of this AdjustCouponQuotasReq.
        :rtype: list[str]
        """
        return self._indirect_partner_ids

    @indirect_partner_ids.setter
    def indirect_partner_ids(self, indirect_partner_ids):
        """Sets the indirect_partner_ids of this AdjustCouponQuotasReq.

        云经销商ID列表。

        :param indirect_partner_ids: The indirect_partner_ids of this AdjustCouponQuotasReq.
        :type indirect_partner_ids: list[str]
        """
        self._indirect_partner_ids = indirect_partner_ids

    @property
    def quota_amount(self):
        """Gets the quota_amount of this AdjustCouponQuotasReq.

        华为云总经销商向云经销商发放的代金券额度值。 单位：元。取值大于0且精确到小数点后2位。

        :return: The quota_amount of this AdjustCouponQuotasReq.
        :rtype: float
        """
        return self._quota_amount

    @quota_amount.setter
    def quota_amount(self, quota_amount):
        """Sets the quota_amount of this AdjustCouponQuotasReq.

        华为云总经销商向云经销商发放的代金券额度值。 单位：元。取值大于0且精确到小数点后2位。

        :param quota_amount: The quota_amount of this AdjustCouponQuotasReq.
        :type quota_amount: float
        """
        self._quota_amount = quota_amount

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
        if not isinstance(other, AdjustCouponQuotasReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
