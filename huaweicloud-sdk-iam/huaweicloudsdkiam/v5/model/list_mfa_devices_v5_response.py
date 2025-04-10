# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMfaDevicesV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mfa_devices': 'list[MfaDeviceMetadata]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'mfa_devices': 'mfa_devices',
        'page_info': 'page_info'
    }

    def __init__(self, mfa_devices=None, page_info=None):
        r"""ListMfaDevicesV5Response

        The model defined in huaweicloud sdk

        :param mfa_devices: 虚拟MFA设备列表。
        :type mfa_devices: list[:class:`huaweicloudsdkiam.v5.MfaDeviceMetadata`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        
        super(ListMfaDevicesV5Response, self).__init__()

        self._mfa_devices = None
        self._page_info = None
        self.discriminator = None

        if mfa_devices is not None:
            self.mfa_devices = mfa_devices
        if page_info is not None:
            self.page_info = page_info

    @property
    def mfa_devices(self):
        r"""Gets the mfa_devices of this ListMfaDevicesV5Response.

        虚拟MFA设备列表。

        :return: The mfa_devices of this ListMfaDevicesV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.MfaDeviceMetadata`]
        """
        return self._mfa_devices

    @mfa_devices.setter
    def mfa_devices(self, mfa_devices):
        r"""Sets the mfa_devices of this ListMfaDevicesV5Response.

        虚拟MFA设备列表。

        :param mfa_devices: The mfa_devices of this ListMfaDevicesV5Response.
        :type mfa_devices: list[:class:`huaweicloudsdkiam.v5.MfaDeviceMetadata`]
        """
        self._mfa_devices = mfa_devices

    @property
    def page_info(self):
        r"""Gets the page_info of this ListMfaDevicesV5Response.

        :return: The page_info of this ListMfaDevicesV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListMfaDevicesV5Response.

        :param page_info: The page_info of this ListMfaDevicesV5Response.
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListMfaDevicesV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
