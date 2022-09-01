# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnbindMfaDevice:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'authentication_code': 'str',
        'serial_number': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'authentication_code': 'authentication_code',
        'serial_number': 'serial_number'
    }

    def __init__(self, user_id=None, authentication_code=None, serial_number=None):
        """UnbindMfaDevice

        The model defined in huaweicloud sdk

        :param user_id: 待解绑MFA设备的IAM用户ID。
        :type user_id: str
        :param authentication_code: 管理员为IAM用户解绑MFA设备：填写6位任意验证码，不做校验。IAM用户为自己解绑MFA设备：填写虚拟MFA验证码。
        :type authentication_code: str
        :param serial_number: MFA设备序列号。
        :type serial_number: str
        """
        
        

        self._user_id = None
        self._authentication_code = None
        self._serial_number = None
        self.discriminator = None

        self.user_id = user_id
        self.authentication_code = authentication_code
        self.serial_number = serial_number

    @property
    def user_id(self):
        """Gets the user_id of this UnbindMfaDevice.

        待解绑MFA设备的IAM用户ID。

        :return: The user_id of this UnbindMfaDevice.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UnbindMfaDevice.

        待解绑MFA设备的IAM用户ID。

        :param user_id: The user_id of this UnbindMfaDevice.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def authentication_code(self):
        """Gets the authentication_code of this UnbindMfaDevice.

        管理员为IAM用户解绑MFA设备：填写6位任意验证码，不做校验。IAM用户为自己解绑MFA设备：填写虚拟MFA验证码。

        :return: The authentication_code of this UnbindMfaDevice.
        :rtype: str
        """
        return self._authentication_code

    @authentication_code.setter
    def authentication_code(self, authentication_code):
        """Sets the authentication_code of this UnbindMfaDevice.

        管理员为IAM用户解绑MFA设备：填写6位任意验证码，不做校验。IAM用户为自己解绑MFA设备：填写虚拟MFA验证码。

        :param authentication_code: The authentication_code of this UnbindMfaDevice.
        :type authentication_code: str
        """
        self._authentication_code = authentication_code

    @property
    def serial_number(self):
        """Gets the serial_number of this UnbindMfaDevice.

        MFA设备序列号。

        :return: The serial_number of this UnbindMfaDevice.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this UnbindMfaDevice.

        MFA设备序列号。

        :param serial_number: The serial_number of this UnbindMfaDevice.
        :type serial_number: str
        """
        self._serial_number = serial_number

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
        if not isinstance(other, UnbindMfaDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
