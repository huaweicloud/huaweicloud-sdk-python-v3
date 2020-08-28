# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ReclaimCouponQuotasResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_details': 'list[ErrorDetail]',
        'simple_quota_infos': 'list[QuotaReclaim]'
    }

    attribute_map = {
        'error_details': 'error_details',
        'simple_quota_infos': 'simple_quota_infos'
    }

    def __init__(self, error_details=None, simple_quota_infos=None):
        """ReclaimCouponQuotasResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._error_details = None
        self._simple_quota_infos = None
        self.discriminator = None

        if error_details is not None:
            self.error_details = error_details
        if simple_quota_infos is not None:
            self.simple_quota_infos = simple_quota_infos

    @property
    def error_details(self):
        """Gets the error_details of this ReclaimCouponQuotasResponse.

        |参数名称：响应信息| |参数约束以及描述：响应信息|

        :return: The error_details of this ReclaimCouponQuotasResponse.
        :rtype: list[ErrorDetail]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this ReclaimCouponQuotasResponse.

        |参数名称：响应信息| |参数约束以及描述：响应信息|

        :param error_details: The error_details of this ReclaimCouponQuotasResponse.
        :type: list[ErrorDetail]
        """
        self._error_details = error_details

    @property
    def simple_quota_infos(self):
        """Gets the simple_quota_infos of this ReclaimCouponQuotasResponse.

        |参数名称：响应信息| |参数约束以及描述：响应信息|

        :return: The simple_quota_infos of this ReclaimCouponQuotasResponse.
        :rtype: list[QuotaReclaim]
        """
        return self._simple_quota_infos

    @simple_quota_infos.setter
    def simple_quota_infos(self, simple_quota_infos):
        """Sets the simple_quota_infos of this ReclaimCouponQuotasResponse.

        |参数名称：响应信息| |参数约束以及描述：响应信息|

        :param simple_quota_infos: The simple_quota_infos of this ReclaimCouponQuotasResponse.
        :type: list[QuotaReclaim]
        """
        self._simple_quota_infos = simple_quota_infos

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
        if not isinstance(other, ReclaimCouponQuotasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
