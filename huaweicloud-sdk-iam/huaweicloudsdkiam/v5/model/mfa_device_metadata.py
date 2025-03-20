# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MfaDeviceMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'serial_number': 'str',
        'user_id': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'user_id': 'user_id',
        'enabled': 'enabled'
    }

    def __init__(self, serial_number=None, user_id=None, enabled=None):
        """MfaDeviceMetadata

        The model defined in huaweicloud sdk

        :param serial_number: MFA设备序列号。
        :type serial_number: str
        :param user_id: IAM用户ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type user_id: str
        :param enabled: 虚拟MFA设备是否开启。
        :type enabled: bool
        """
        
        

        self._serial_number = None
        self._user_id = None
        self._enabled = None
        self.discriminator = None

        self.serial_number = serial_number
        self.user_id = user_id
        self.enabled = enabled

    @property
    def serial_number(self):
        """Gets the serial_number of this MfaDeviceMetadata.

        MFA设备序列号。

        :return: The serial_number of this MfaDeviceMetadata.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this MfaDeviceMetadata.

        MFA设备序列号。

        :param serial_number: The serial_number of this MfaDeviceMetadata.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def user_id(self):
        """Gets the user_id of this MfaDeviceMetadata.

        IAM用户ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The user_id of this MfaDeviceMetadata.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MfaDeviceMetadata.

        IAM用户ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param user_id: The user_id of this MfaDeviceMetadata.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def enabled(self):
        """Gets the enabled of this MfaDeviceMetadata.

        虚拟MFA设备是否开启。

        :return: The enabled of this MfaDeviceMetadata.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MfaDeviceMetadata.

        虚拟MFA设备是否开启。

        :param enabled: The enabled of this MfaDeviceMetadata.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, MfaDeviceMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
