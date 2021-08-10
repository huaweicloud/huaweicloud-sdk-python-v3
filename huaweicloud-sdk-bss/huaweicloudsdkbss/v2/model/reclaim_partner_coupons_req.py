# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReclaimPartnerCouponsReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'coupon_id': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, coupon_id=None, indirect_partner_id=None):
        """ReclaimPartnerCouponsReq - a model defined in huaweicloud sdk"""
        
        

        self._coupon_id = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.coupon_id = coupon_id
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def coupon_id(self):
        """Gets the coupon_id of this ReclaimPartnerCouponsReq.

        待回收的代金券ID。 请从“发放优惠券”或“查询已发放的优惠券”接口的响应参数中获取。

        :return: The coupon_id of this ReclaimPartnerCouponsReq.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this ReclaimPartnerCouponsReq.

        待回收的代金券ID。 请从“发放优惠券”或“查询已发放的优惠券”接口的响应参数中获取。

        :param coupon_id: The coupon_id of this ReclaimPartnerCouponsReq.
        :type: str
        """
        self._coupon_id = coupon_id

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ReclaimPartnerCouponsReq.

        精英服务商ID。获取方法请参见查询精英服务商列表。 精英服务商回收给子客户发放的优惠券时，需要携带该字段。

        :return: The indirect_partner_id of this ReclaimPartnerCouponsReq.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ReclaimPartnerCouponsReq.

        精英服务商ID。获取方法请参见查询精英服务商列表。 精英服务商回收给子客户发放的优惠券时，需要携带该字段。

        :param indirect_partner_id: The indirect_partner_id of this ReclaimPartnerCouponsReq.
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
        if not isinstance(other, ReclaimPartnerCouponsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
