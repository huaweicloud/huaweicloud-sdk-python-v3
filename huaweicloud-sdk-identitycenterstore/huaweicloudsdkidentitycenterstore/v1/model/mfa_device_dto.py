# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MfaDeviceDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_id': 'str',
        'device_name': 'str',
        'display_name': 'str',
        'mfa_type': 'str',
        'registered_date': 'int'
    }

    attribute_map = {
        'device_id': 'device_id',
        'device_name': 'device_name',
        'display_name': 'display_name',
        'mfa_type': 'mfa_type',
        'registered_date': 'registered_date'
    }

    def __init__(self, device_id=None, device_name=None, display_name=None, mfa_type=None, registered_date=None):
        r"""MfaDeviceDto

        The model defined in huaweicloud sdk

        :param device_id: MFA设备唯一标识符（ID）
        :type device_id: str
        :param device_name: MFA设备名称
        :type device_name: str
        :param display_name: MFA设备显示名称
        :type display_name: str
        :param mfa_type: MFA类型
        :type mfa_type: str
        :param registered_date: 注册时间
        :type registered_date: int
        """
        
        

        self._device_id = None
        self._device_name = None
        self._display_name = None
        self._mfa_type = None
        self._registered_date = None
        self.discriminator = None

        self.device_id = device_id
        self.device_name = device_name
        self.display_name = display_name
        self.mfa_type = mfa_type
        self.registered_date = registered_date

    @property
    def device_id(self):
        r"""Gets the device_id of this MfaDeviceDto.

        MFA设备唯一标识符（ID）

        :return: The device_id of this MfaDeviceDto.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        r"""Sets the device_id of this MfaDeviceDto.

        MFA设备唯一标识符（ID）

        :param device_id: The device_id of this MfaDeviceDto.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_name(self):
        r"""Gets the device_name of this MfaDeviceDto.

        MFA设备名称

        :return: The device_name of this MfaDeviceDto.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        r"""Sets the device_name of this MfaDeviceDto.

        MFA设备名称

        :param device_name: The device_name of this MfaDeviceDto.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def display_name(self):
        r"""Gets the display_name of this MfaDeviceDto.

        MFA设备显示名称

        :return: The display_name of this MfaDeviceDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this MfaDeviceDto.

        MFA设备显示名称

        :param display_name: The display_name of this MfaDeviceDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def mfa_type(self):
        r"""Gets the mfa_type of this MfaDeviceDto.

        MFA类型

        :return: The mfa_type of this MfaDeviceDto.
        :rtype: str
        """
        return self._mfa_type

    @mfa_type.setter
    def mfa_type(self, mfa_type):
        r"""Sets the mfa_type of this MfaDeviceDto.

        MFA类型

        :param mfa_type: The mfa_type of this MfaDeviceDto.
        :type mfa_type: str
        """
        self._mfa_type = mfa_type

    @property
    def registered_date(self):
        r"""Gets the registered_date of this MfaDeviceDto.

        注册时间

        :return: The registered_date of this MfaDeviceDto.
        :rtype: int
        """
        return self._registered_date

    @registered_date.setter
    def registered_date(self, registered_date):
        r"""Sets the registered_date of this MfaDeviceDto.

        注册时间

        :param registered_date: The registered_date of this MfaDeviceDto.
        :type registered_date: int
        """
        self._registered_date = registered_date

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
        if not isinstance(other, MfaDeviceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
