# coding: utf-8

import pprint
import re

import six





class BindMfaDevice:


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
        'serial_number': 'str',
        'authentication_code_first': 'str',
        'authentication_code_second': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'serial_number': 'serial_number',
        'authentication_code_first': 'authentication_code_first',
        'authentication_code_second': 'authentication_code_second'
    }

    def __init__(self, user_id=None, serial_number=None, authentication_code_first=None, authentication_code_second=None):
        """BindMfaDevice - a model defined in huaweicloud sdk"""
        
        

        self._user_id = None
        self._serial_number = None
        self._authentication_code_first = None
        self._authentication_code_second = None
        self.discriminator = None

        self.user_id = user_id
        self.serial_number = serial_number
        self.authentication_code_first = authentication_code_first
        self.authentication_code_second = authentication_code_second

    @property
    def user_id(self):
        """Gets the user_id of this BindMfaDevice.

        待绑定MFA设备的IAM用户ID。

        :return: The user_id of this BindMfaDevice.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BindMfaDevice.

        待绑定MFA设备的IAM用户ID。

        :param user_id: The user_id of this BindMfaDevice.
        :type: str
        """
        self._user_id = user_id

    @property
    def serial_number(self):
        """Gets the serial_number of this BindMfaDevice.

        MFA设备序列号。

        :return: The serial_number of this BindMfaDevice.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this BindMfaDevice.

        MFA设备序列号。

        :param serial_number: The serial_number of this BindMfaDevice.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def authentication_code_first(self):
        """Gets the authentication_code_first of this BindMfaDevice.

        第一组验证码。

        :return: The authentication_code_first of this BindMfaDevice.
        :rtype: str
        """
        return self._authentication_code_first

    @authentication_code_first.setter
    def authentication_code_first(self, authentication_code_first):
        """Sets the authentication_code_first of this BindMfaDevice.

        第一组验证码。

        :param authentication_code_first: The authentication_code_first of this BindMfaDevice.
        :type: str
        """
        self._authentication_code_first = authentication_code_first

    @property
    def authentication_code_second(self):
        """Gets the authentication_code_second of this BindMfaDevice.

        第二组验证码。

        :return: The authentication_code_second of this BindMfaDevice.
        :rtype: str
        """
        return self._authentication_code_second

    @authentication_code_second.setter
    def authentication_code_second(self, authentication_code_second):
        """Sets the authentication_code_second of this BindMfaDevice.

        第二组验证码。

        :param authentication_code_second: The authentication_code_second of this BindMfaDevice.
        :type: str
        """
        self._authentication_code_second = authentication_code_second

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
        if not isinstance(other, BindMfaDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
