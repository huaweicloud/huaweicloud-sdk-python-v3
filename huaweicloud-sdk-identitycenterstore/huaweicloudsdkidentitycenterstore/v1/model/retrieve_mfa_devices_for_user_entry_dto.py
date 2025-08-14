# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetrieveMfaDevicesForUserEntryDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mfa_devices': 'list[MfaDeviceDto]',
        'user': 'RetrieveMfaDevicesForUserDto'
    }

    attribute_map = {
        'mfa_devices': 'mfa_devices',
        'user': 'user'
    }

    def __init__(self, mfa_devices=None, user=None):
        r"""RetrieveMfaDevicesForUserEntryDto

        The model defined in huaweicloud sdk

        :param mfa_devices: MFA设备列表
        :type mfa_devices: list[:class:`huaweicloudsdkidentitycenterstore.v1.MfaDeviceDto`]
        :param user: 
        :type user: :class:`huaweicloudsdkidentitycenterstore.v1.RetrieveMfaDevicesForUserDto`
        """
        
        

        self._mfa_devices = None
        self._user = None
        self.discriminator = None

        self.mfa_devices = mfa_devices
        self.user = user

    @property
    def mfa_devices(self):
        r"""Gets the mfa_devices of this RetrieveMfaDevicesForUserEntryDto.

        MFA设备列表

        :return: The mfa_devices of this RetrieveMfaDevicesForUserEntryDto.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.MfaDeviceDto`]
        """
        return self._mfa_devices

    @mfa_devices.setter
    def mfa_devices(self, mfa_devices):
        r"""Sets the mfa_devices of this RetrieveMfaDevicesForUserEntryDto.

        MFA设备列表

        :param mfa_devices: The mfa_devices of this RetrieveMfaDevicesForUserEntryDto.
        :type mfa_devices: list[:class:`huaweicloudsdkidentitycenterstore.v1.MfaDeviceDto`]
        """
        self._mfa_devices = mfa_devices

    @property
    def user(self):
        r"""Gets the user of this RetrieveMfaDevicesForUserEntryDto.

        :return: The user of this RetrieveMfaDevicesForUserEntryDto.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.RetrieveMfaDevicesForUserDto`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this RetrieveMfaDevicesForUserEntryDto.

        :param user: The user of this RetrieveMfaDevicesForUserEntryDto.
        :type user: :class:`huaweicloudsdkidentitycenterstore.v1.RetrieveMfaDevicesForUserDto`
        """
        self._user = user

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
        if not isinstance(other, RetrieveMfaDevicesForUserEntryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
