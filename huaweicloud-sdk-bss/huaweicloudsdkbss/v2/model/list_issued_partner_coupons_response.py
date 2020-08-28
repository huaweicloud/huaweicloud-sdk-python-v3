# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListIssuedPartnerCouponsResponse(SdkResponse):


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
        'user_coupons': 'list[IQueryUserPartnerCouponsResultV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'user_coupons': 'user_coupons'
    }

    def __init__(self, total_count=None, user_coupons=None):
        """ListIssuedPartnerCouponsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total_count = None
        self._user_coupons = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if user_coupons is not None:
            self.user_coupons = user_coupons

    @property
    def total_count(self):
        """Gets the total_count of this ListIssuedPartnerCouponsResponse.

        |参数名称：个数| |参数的约束及描述：个数|

        :return: The total_count of this ListIssuedPartnerCouponsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListIssuedPartnerCouponsResponse.

        |参数名称：个数| |参数的约束及描述：个数|

        :param total_count: The total_count of this ListIssuedPartnerCouponsResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def user_coupons(self):
        """Gets the user_coupons of this ListIssuedPartnerCouponsResponse.

        |参数名称：优惠券记录。具体请参见表 IQueryUserCouponsResult。| |参数约束以及描述：优惠券记录。具体请参见表 IQueryUserCouponsResult。|

        :return: The user_coupons of this ListIssuedPartnerCouponsResponse.
        :rtype: list[IQueryUserPartnerCouponsResultV2]
        """
        return self._user_coupons

    @user_coupons.setter
    def user_coupons(self, user_coupons):
        """Sets the user_coupons of this ListIssuedPartnerCouponsResponse.

        |参数名称：优惠券记录。具体请参见表 IQueryUserCouponsResult。| |参数约束以及描述：优惠券记录。具体请参见表 IQueryUserCouponsResult。|

        :param user_coupons: The user_coupons of this ListIssuedPartnerCouponsResponse.
        :type: list[IQueryUserPartnerCouponsResultV2]
        """
        self._user_coupons = user_coupons

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
        if not isinstance(other, ListIssuedPartnerCouponsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
