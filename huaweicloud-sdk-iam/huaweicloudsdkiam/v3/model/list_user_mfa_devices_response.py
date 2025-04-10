# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserMfaDevicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virtual_mfa_devices': 'list[MfaDeviceResult]'
    }

    attribute_map = {
        'virtual_mfa_devices': 'virtual_mfa_devices'
    }

    def __init__(self, virtual_mfa_devices=None):
        r"""ListUserMfaDevicesResponse

        The model defined in huaweicloud sdk

        :param virtual_mfa_devices: 虚拟MFA设备信息列表。
        :type virtual_mfa_devices: list[:class:`huaweicloudsdkiam.v3.MfaDeviceResult`]
        """
        
        super(ListUserMfaDevicesResponse, self).__init__()

        self._virtual_mfa_devices = None
        self.discriminator = None

        if virtual_mfa_devices is not None:
            self.virtual_mfa_devices = virtual_mfa_devices

    @property
    def virtual_mfa_devices(self):
        r"""Gets the virtual_mfa_devices of this ListUserMfaDevicesResponse.

        虚拟MFA设备信息列表。

        :return: The virtual_mfa_devices of this ListUserMfaDevicesResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.MfaDeviceResult`]
        """
        return self._virtual_mfa_devices

    @virtual_mfa_devices.setter
    def virtual_mfa_devices(self, virtual_mfa_devices):
        r"""Sets the virtual_mfa_devices of this ListUserMfaDevicesResponse.

        虚拟MFA设备信息列表。

        :param virtual_mfa_devices: The virtual_mfa_devices of this ListUserMfaDevicesResponse.
        :type virtual_mfa_devices: list[:class:`huaweicloudsdkiam.v3.MfaDeviceResult`]
        """
        self._virtual_mfa_devices = virtual_mfa_devices

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
        if not isinstance(other, ListUserMfaDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
