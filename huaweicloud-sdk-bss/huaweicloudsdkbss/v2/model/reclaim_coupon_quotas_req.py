# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReclaimCouponQuotasReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_ids': 'list[str]',
        'remark': 'str'
    }

    attribute_map = {
        'quota_ids': 'quota_ids',
        'remark': 'remark'
    }

    def __init__(self, quota_ids=None, remark=None):
        r"""ReclaimCouponQuotasReq

        The model defined in huaweicloud sdk

        :param quota_ids: 被回收的云经销商的代金券额度ID。获取方法请参见查询优惠券额度。
        :type quota_ids: list[str]
        :param remark: 回收时的备注。 此参数不携带或携带值为null时，不赋值；携带值为空串时，赋值空串。
        :type remark: str
        """
        
        

        self._quota_ids = None
        self._remark = None
        self.discriminator = None

        self.quota_ids = quota_ids
        if remark is not None:
            self.remark = remark

    @property
    def quota_ids(self):
        r"""Gets the quota_ids of this ReclaimCouponQuotasReq.

        被回收的云经销商的代金券额度ID。获取方法请参见查询优惠券额度。

        :return: The quota_ids of this ReclaimCouponQuotasReq.
        :rtype: list[str]
        """
        return self._quota_ids

    @quota_ids.setter
    def quota_ids(self, quota_ids):
        r"""Sets the quota_ids of this ReclaimCouponQuotasReq.

        被回收的云经销商的代金券额度ID。获取方法请参见查询优惠券额度。

        :param quota_ids: The quota_ids of this ReclaimCouponQuotasReq.
        :type quota_ids: list[str]
        """
        self._quota_ids = quota_ids

    @property
    def remark(self):
        r"""Gets the remark of this ReclaimCouponQuotasReq.

        回收时的备注。 此参数不携带或携带值为null时，不赋值；携带值为空串时，赋值空串。

        :return: The remark of this ReclaimCouponQuotasReq.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this ReclaimCouponQuotasReq.

        回收时的备注。 此参数不携带或携带值为null时，不赋值；携带值为空串时，赋值空串。

        :param remark: The remark of this ReclaimCouponQuotasReq.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, ReclaimCouponQuotasReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
