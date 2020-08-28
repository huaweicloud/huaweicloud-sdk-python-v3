# coding: utf-8

import pprint
import re

import six





class PasswordPolicyOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'maximum_consecutive_identical_chars': 'int',
        'minimum_password_age': 'int',
        'minimum_password_length': 'int',
        'number_of_recent_passwords_disallowed': 'int',
        'password_not_username_or_invert': 'bool',
        'password_validity_period': 'int'
    }

    attribute_map = {
        'maximum_consecutive_identical_chars': 'maximum_consecutive_identical_chars',
        'minimum_password_age': 'minimum_password_age',
        'minimum_password_length': 'minimum_password_length',
        'number_of_recent_passwords_disallowed': 'number_of_recent_passwords_disallowed',
        'password_not_username_or_invert': 'password_not_username_or_invert',
        'password_validity_period': 'password_validity_period'
    }

    def __init__(self, maximum_consecutive_identical_chars=None, minimum_password_age=None, minimum_password_length=None, number_of_recent_passwords_disallowed=None, password_not_username_or_invert=None, password_validity_period=None):
        """PasswordPolicyOption - a model defined in huaweicloud sdk"""
        
        

        self._maximum_consecutive_identical_chars = None
        self._minimum_password_age = None
        self._minimum_password_length = None
        self._number_of_recent_passwords_disallowed = None
        self._password_not_username_or_invert = None
        self._password_validity_period = None
        self.discriminator = None

        self.maximum_consecutive_identical_chars = maximum_consecutive_identical_chars
        self.minimum_password_age = minimum_password_age
        self.minimum_password_length = minimum_password_length
        self.number_of_recent_passwords_disallowed = number_of_recent_passwords_disallowed
        self.password_not_username_or_invert = password_not_username_or_invert
        self.password_validity_period = password_validity_period

    @property
    def maximum_consecutive_identical_chars(self):
        """Gets the maximum_consecutive_identical_chars of this PasswordPolicyOption.

        同一字符连续出现的最大次数，取值范围[0,32]。

        :return: The maximum_consecutive_identical_chars of this PasswordPolicyOption.
        :rtype: int
        """
        return self._maximum_consecutive_identical_chars

    @maximum_consecutive_identical_chars.setter
    def maximum_consecutive_identical_chars(self, maximum_consecutive_identical_chars):
        """Sets the maximum_consecutive_identical_chars of this PasswordPolicyOption.

        同一字符连续出现的最大次数，取值范围[0,32]。

        :param maximum_consecutive_identical_chars: The maximum_consecutive_identical_chars of this PasswordPolicyOption.
        :type: int
        """
        self._maximum_consecutive_identical_chars = maximum_consecutive_identical_chars

    @property
    def minimum_password_age(self):
        """Gets the minimum_password_age of this PasswordPolicyOption.

        密码最短使用时间(分钟)，取值范围[0,1440]。

        :return: The minimum_password_age of this PasswordPolicyOption.
        :rtype: int
        """
        return self._minimum_password_age

    @minimum_password_age.setter
    def minimum_password_age(self, minimum_password_age):
        """Sets the minimum_password_age of this PasswordPolicyOption.

        密码最短使用时间(分钟)，取值范围[0,1440]。

        :param minimum_password_age: The minimum_password_age of this PasswordPolicyOption.
        :type: int
        """
        self._minimum_password_age = minimum_password_age

    @property
    def minimum_password_length(self):
        """Gets the minimum_password_length of this PasswordPolicyOption.

        密码最小字符数，取值范围[6,32]。

        :return: The minimum_password_length of this PasswordPolicyOption.
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """Sets the minimum_password_length of this PasswordPolicyOption.

        密码最小字符数，取值范围[6,32]。

        :param minimum_password_length: The minimum_password_length of this PasswordPolicyOption.
        :type: int
        """
        self._minimum_password_length = minimum_password_length

    @property
    def number_of_recent_passwords_disallowed(self):
        """Gets the number_of_recent_passwords_disallowed of this PasswordPolicyOption.

        密码不能与历史密码重复次数，取值范围[0,10]。

        :return: The number_of_recent_passwords_disallowed of this PasswordPolicyOption.
        :rtype: int
        """
        return self._number_of_recent_passwords_disallowed

    @number_of_recent_passwords_disallowed.setter
    def number_of_recent_passwords_disallowed(self, number_of_recent_passwords_disallowed):
        """Sets the number_of_recent_passwords_disallowed of this PasswordPolicyOption.

        密码不能与历史密码重复次数，取值范围[0,10]。

        :param number_of_recent_passwords_disallowed: The number_of_recent_passwords_disallowed of this PasswordPolicyOption.
        :type: int
        """
        self._number_of_recent_passwords_disallowed = number_of_recent_passwords_disallowed

    @property
    def password_not_username_or_invert(self):
        """Gets the password_not_username_or_invert of this PasswordPolicyOption.

        密码是否可以是用户名或用户名的反序。

        :return: The password_not_username_or_invert of this PasswordPolicyOption.
        :rtype: bool
        """
        return self._password_not_username_or_invert

    @password_not_username_or_invert.setter
    def password_not_username_or_invert(self, password_not_username_or_invert):
        """Sets the password_not_username_or_invert of this PasswordPolicyOption.

        密码是否可以是用户名或用户名的反序。

        :param password_not_username_or_invert: The password_not_username_or_invert of this PasswordPolicyOption.
        :type: bool
        """
        self._password_not_username_or_invert = password_not_username_or_invert

    @property
    def password_validity_period(self):
        """Gets the password_validity_period of this PasswordPolicyOption.

        密码有效期（天），取值范围[0,180]，设置0表示关闭该策略。

        :return: The password_validity_period of this PasswordPolicyOption.
        :rtype: int
        """
        return self._password_validity_period

    @password_validity_period.setter
    def password_validity_period(self, password_validity_period):
        """Sets the password_validity_period of this PasswordPolicyOption.

        密码有效期（天），取值范围[0,180]，设置0表示关闭该策略。

        :param password_validity_period: The password_validity_period of this PasswordPolicyOption.
        :type: int
        """
        self._password_validity_period = password_validity_period

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
        if not isinstance(other, PasswordPolicyOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
