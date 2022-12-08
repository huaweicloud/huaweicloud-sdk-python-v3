# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOtpDevicesByUserIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'otp_devices': 'list[OtpDevice]'
    }

    attribute_map = {
        'otp_devices': 'otp_devices'
    }

    def __init__(self, otp_devices=None):
        """ListOtpDevicesByUserIdResponse

        The model defined in huaweicloud sdk

        :param otp_devices: otp设备
        :type otp_devices: list[:class:`huaweicloudsdkworkspace.v2.OtpDevice`]
        """
        
        super(ListOtpDevicesByUserIdResponse, self).__init__()

        self._otp_devices = None
        self.discriminator = None

        if otp_devices is not None:
            self.otp_devices = otp_devices

    @property
    def otp_devices(self):
        """Gets the otp_devices of this ListOtpDevicesByUserIdResponse.

        otp设备

        :return: The otp_devices of this ListOtpDevicesByUserIdResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.OtpDevice`]
        """
        return self._otp_devices

    @otp_devices.setter
    def otp_devices(self, otp_devices):
        """Sets the otp_devices of this ListOtpDevicesByUserIdResponse.

        otp设备

        :param otp_devices: The otp_devices of this ListOtpDevicesByUserIdResponse.
        :type otp_devices: list[:class:`huaweicloudsdkworkspace.v2.OtpDevice`]
        """
        self._otp_devices = otp_devices

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
        if not isinstance(other, ListOtpDevicesByUserIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
