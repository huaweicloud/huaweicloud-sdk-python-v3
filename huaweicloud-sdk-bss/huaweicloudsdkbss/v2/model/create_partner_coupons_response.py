# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePartnerCouponsResponse(SdkResponse):

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
        'coupon_infos': 'list[CouponSimpleInfo]'
    }

    attribute_map = {
        'error_details': 'error_details',
        'coupon_infos': 'coupon_infos'
    }

    def __init__(self, error_details=None, coupon_infos=None):
        """CreatePartnerCouponsResponse

        The model defined in huaweicloud sdk

        :param error_details: 错误的客户列表和错误信息，只有HTTP 200的时候才会返回这个结构体，具体参见表1。
        :type error_details: list[:class:`huaweicloudsdkbss.v2.ErrorDetail`]
        :param coupon_infos: 成功的客户ID和对应的券ID列表，只有HTTP 200的时候才会返回这个结构体，具体参见表2。
        :type coupon_infos: list[:class:`huaweicloudsdkbss.v2.CouponSimpleInfo`]
        """
        
        super(CreatePartnerCouponsResponse, self).__init__()

        self._error_details = None
        self._coupon_infos = None
        self.discriminator = None

        if error_details is not None:
            self.error_details = error_details
        if coupon_infos is not None:
            self.coupon_infos = coupon_infos

    @property
    def error_details(self):
        """Gets the error_details of this CreatePartnerCouponsResponse.

        错误的客户列表和错误信息，只有HTTP 200的时候才会返回这个结构体，具体参见表1。

        :return: The error_details of this CreatePartnerCouponsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.ErrorDetail`]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this CreatePartnerCouponsResponse.

        错误的客户列表和错误信息，只有HTTP 200的时候才会返回这个结构体，具体参见表1。

        :param error_details: The error_details of this CreatePartnerCouponsResponse.
        :type error_details: list[:class:`huaweicloudsdkbss.v2.ErrorDetail`]
        """
        self._error_details = error_details

    @property
    def coupon_infos(self):
        """Gets the coupon_infos of this CreatePartnerCouponsResponse.

        成功的客户ID和对应的券ID列表，只有HTTP 200的时候才会返回这个结构体，具体参见表2。

        :return: The coupon_infos of this CreatePartnerCouponsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.CouponSimpleInfo`]
        """
        return self._coupon_infos

    @coupon_infos.setter
    def coupon_infos(self, coupon_infos):
        """Sets the coupon_infos of this CreatePartnerCouponsResponse.

        成功的客户ID和对应的券ID列表，只有HTTP 200的时候才会返回这个结构体，具体参见表2。

        :param coupon_infos: The coupon_infos of this CreatePartnerCouponsResponse.
        :type coupon_infos: list[:class:`huaweicloudsdkbss.v2.CouponSimpleInfo`]
        """
        self._coupon_infos = coupon_infos

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
        if not isinstance(other, CreatePartnerCouponsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
