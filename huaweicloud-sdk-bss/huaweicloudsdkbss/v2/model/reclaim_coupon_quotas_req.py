# coding: utf-8

import pprint
import re

import six





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
        """ReclaimCouponQuotasReq - a model defined in huaweicloud sdk"""
        
        

        self._quota_ids = None
        self._remark = None
        self.discriminator = None

        self.quota_ids = quota_ids
        if remark is not None:
            self.remark = remark

    @property
    def quota_ids(self):
        """Gets the quota_ids of this ReclaimCouponQuotasReq.

        |参数名称：被回收的代金券额度的ID。| |参数约束以及描述：被回收的代金券额度的ID。|

        :return: The quota_ids of this ReclaimCouponQuotasReq.
        :rtype: list[str]
        """
        return self._quota_ids

    @quota_ids.setter
    def quota_ids(self, quota_ids):
        """Sets the quota_ids of this ReclaimCouponQuotasReq.

        |参数名称：被回收的代金券额度的ID。| |参数约束以及描述：被回收的代金券额度的ID。|

        :param quota_ids: The quota_ids of this ReclaimCouponQuotasReq.
        :type: list[str]
        """
        self._quota_ids = quota_ids

    @property
    def remark(self):
        """Gets the remark of this ReclaimCouponQuotasReq.

        |参数名称：回收时候的备注| |参数约束及描述：回收时候的备注|

        :return: The remark of this ReclaimCouponQuotasReq.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ReclaimCouponQuotasReq.

        |参数名称：回收时候的备注| |参数约束及描述：回收时候的备注|

        :param remark: The remark of this ReclaimCouponQuotasReq.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReclaimCouponQuotasReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
