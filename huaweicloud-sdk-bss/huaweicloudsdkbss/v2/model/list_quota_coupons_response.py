# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListQuotaCouponsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'quotas': 'list[CouponQuotaV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'quotas': 'quotas'
    }

    def __init__(self, total_count=None, quotas=None):
        """ListQuotaCouponsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total_count = None
        self._quotas = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if quotas is not None:
            self.quotas = quotas

    @property
    def total_count(self):
        """Gets the total_count of this ListQuotaCouponsResponse.

        |参数名称：查询总数。| |参数的约束及描述：查询总数。|

        :return: The total_count of this ListQuotaCouponsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListQuotaCouponsResponse.

        |参数名称：查询总数。| |参数的约束及描述：查询总数。|

        :param total_count: The total_count of this ListQuotaCouponsResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def quotas(self):
        """Gets the quotas of this ListQuotaCouponsResponse.

        |参数名称：额度记录列表。具体请参见表2 IssuedCouponQuota。| |参数约束以及描述：额度记录列表。具体请参见表2 IssuedCouponQuota。|

        :return: The quotas of this ListQuotaCouponsResponse.
        :rtype: list[CouponQuotaV2]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        """Sets the quotas of this ListQuotaCouponsResponse.

        |参数名称：额度记录列表。具体请参见表2 IssuedCouponQuota。| |参数约束以及描述：额度记录列表。具体请参见表2 IssuedCouponQuota。|

        :param quotas: The quotas of this ListQuotaCouponsResponse.
        :type: list[CouponQuotaV2]
        """
        self._quotas = quotas

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
        if not isinstance(other, ListQuotaCouponsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
