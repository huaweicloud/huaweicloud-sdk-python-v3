# coding: utf-8

import pprint
import re

import six





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
        """AdjustCouponQuotasReq - a model defined in huaweicloud sdk"""
        
        

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

        |参数名称：优惠券额度ID。| |参数约束及描述：优惠券额度ID。|

        :return: The quota_id of this AdjustCouponQuotasReq.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this AdjustCouponQuotasReq.

        |参数名称：优惠券额度ID。| |参数约束及描述：优惠券额度ID。|

        :param quota_id: The quota_id of this AdjustCouponQuotasReq.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def indirect_partner_ids(self):
        """Gets the indirect_partner_ids of this AdjustCouponQuotasReq.

        |参数名称：二级分销商伙伴id列表。最大100条| |参数约束以及描述：二级分销商伙伴id列表。最大100条|

        :return: The indirect_partner_ids of this AdjustCouponQuotasReq.
        :rtype: list[str]
        """
        return self._indirect_partner_ids

    @indirect_partner_ids.setter
    def indirect_partner_ids(self, indirect_partner_ids):
        """Sets the indirect_partner_ids of this AdjustCouponQuotasReq.

        |参数名称：二级分销商伙伴id列表。最大100条| |参数约束以及描述：二级分销商伙伴id列表。最大100条|

        :param indirect_partner_ids: The indirect_partner_ids of this AdjustCouponQuotasReq.
        :type: list[str]
        """
        self._indirect_partner_ids = indirect_partner_ids

    @property
    def quota_amount(self):
        """Gets the quota_amount of this AdjustCouponQuotasReq.

        |参数名称：额度值。保留小数点后2位| |参数的约束及描述：额度值。保留小数点后2位|

        :return: The quota_amount of this AdjustCouponQuotasReq.
        :rtype: float
        """
        return self._quota_amount

    @quota_amount.setter
    def quota_amount(self, quota_amount):
        """Sets the quota_amount of this AdjustCouponQuotasReq.

        |参数名称：额度值。保留小数点后2位| |参数的约束及描述：额度值。保留小数点后2位|

        :param quota_amount: The quota_amount of this AdjustCouponQuotasReq.
        :type: float
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdjustCouponQuotasReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
