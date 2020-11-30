# coding: utf-8

import pprint
import re

import six





class CreateMfaDeviceRespon:


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
        'base32_string_seed': 'str'
    }

    attribute_map = {
        'serial_number': 'serial_number',
        'base32_string_seed': 'base32_string_seed'
    }

    def __init__(self, serial_number=None, base32_string_seed=None):
        """CreateMfaDeviceRespon - a model defined in huaweicloud sdk"""
        
        

        self._serial_number = None
        self._base32_string_seed = None
        self.discriminator = None

        self.serial_number = serial_number
        self.base32_string_seed = base32_string_seed

    @property
    def serial_number(self):
        """Gets the serial_number of this CreateMfaDeviceRespon.

        MFA设备序列号。

        :return: The serial_number of this CreateMfaDeviceRespon.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this CreateMfaDeviceRespon.

        MFA设备序列号。

        :param serial_number: The serial_number of this CreateMfaDeviceRespon.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def base32_string_seed(self):
        """Gets the base32_string_seed of this CreateMfaDeviceRespon.

        密钥信息，用于第三方生成图片验证码。

        :return: The base32_string_seed of this CreateMfaDeviceRespon.
        :rtype: str
        """
        return self._base32_string_seed

    @base32_string_seed.setter
    def base32_string_seed(self, base32_string_seed):
        """Sets the base32_string_seed of this CreateMfaDeviceRespon.

        密钥信息，用于第三方生成图片验证码。

        :param base32_string_seed: The base32_string_seed of this CreateMfaDeviceRespon.
        :type: str
        """
        self._base32_string_seed = base32_string_seed

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
        if not isinstance(other, CreateMfaDeviceRespon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
