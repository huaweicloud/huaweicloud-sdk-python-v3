# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PasswordPolicyResult:

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
        'maximum_password_length': 'int',
        'minimum_password_age': 'int',
        'minimum_password_length': 'int',
        'number_of_recent_passwords_disallowed': 'int',
        'password_not_username_or_invert': 'bool',
        'password_requirements': 'str',
        'password_validity_period': 'int',
        'password_char_combination': 'int'
    }

    attribute_map = {
        'maximum_consecutive_identical_chars': 'maximum_consecutive_identical_chars',
        'maximum_password_length': 'maximum_password_length',
        'minimum_password_age': 'minimum_password_age',
        'minimum_password_length': 'minimum_password_length',
        'number_of_recent_passwords_disallowed': 'number_of_recent_passwords_disallowed',
        'password_not_username_or_invert': 'password_not_username_or_invert',
        'password_requirements': 'password_requirements',
        'password_validity_period': 'password_validity_period',
        'password_char_combination': 'password_char_combination'
    }

    def __init__(self, maximum_consecutive_identical_chars=None, maximum_password_length=None, minimum_password_age=None, minimum_password_length=None, number_of_recent_passwords_disallowed=None, password_not_username_or_invert=None, password_requirements=None, password_validity_period=None, password_char_combination=None):
        """PasswordPolicyResult

        The model defined in huaweicloud sdk

        :param maximum_consecutive_identical_chars: 同一字符连续出现的最大次数。
        :type maximum_consecutive_identical_chars: int
        :param maximum_password_length: 密码最大字符数。
        :type maximum_password_length: int
        :param minimum_password_age: 密码最短使用时间（分钟）。
        :type minimum_password_age: int
        :param minimum_password_length: 密码最小字符数。
        :type minimum_password_length: int
        :param number_of_recent_passwords_disallowed: 密码不能与历史密码重复次数。
        :type number_of_recent_passwords_disallowed: int
        :param password_not_username_or_invert: 密码是否可以是用户名或用户名的反序。
        :type password_not_username_or_invert: bool
        :param password_requirements: 设置密码必须包含的字符要求。
        :type password_requirements: str
        :param password_validity_period: 密码有效期（天）。
        :type password_validity_period: int
        :param password_char_combination: 至少包含字符种类的个数，取值区间[2,4]。
        :type password_char_combination: int
        """
        
        

        self._maximum_consecutive_identical_chars = None
        self._maximum_password_length = None
        self._minimum_password_age = None
        self._minimum_password_length = None
        self._number_of_recent_passwords_disallowed = None
        self._password_not_username_or_invert = None
        self._password_requirements = None
        self._password_validity_period = None
        self._password_char_combination = None
        self.discriminator = None

        self.maximum_consecutive_identical_chars = maximum_consecutive_identical_chars
        self.maximum_password_length = maximum_password_length
        self.minimum_password_age = minimum_password_age
        self.minimum_password_length = minimum_password_length
        self.number_of_recent_passwords_disallowed = number_of_recent_passwords_disallowed
        self.password_not_username_or_invert = password_not_username_or_invert
        self.password_requirements = password_requirements
        self.password_validity_period = password_validity_period
        self.password_char_combination = password_char_combination

    @property
    def maximum_consecutive_identical_chars(self):
        """Gets the maximum_consecutive_identical_chars of this PasswordPolicyResult.

        同一字符连续出现的最大次数。

        :return: The maximum_consecutive_identical_chars of this PasswordPolicyResult.
        :rtype: int
        """
        return self._maximum_consecutive_identical_chars

    @maximum_consecutive_identical_chars.setter
    def maximum_consecutive_identical_chars(self, maximum_consecutive_identical_chars):
        """Sets the maximum_consecutive_identical_chars of this PasswordPolicyResult.

        同一字符连续出现的最大次数。

        :param maximum_consecutive_identical_chars: The maximum_consecutive_identical_chars of this PasswordPolicyResult.
        :type maximum_consecutive_identical_chars: int
        """
        self._maximum_consecutive_identical_chars = maximum_consecutive_identical_chars

    @property
    def maximum_password_length(self):
        """Gets the maximum_password_length of this PasswordPolicyResult.

        密码最大字符数。

        :return: The maximum_password_length of this PasswordPolicyResult.
        :rtype: int
        """
        return self._maximum_password_length

    @maximum_password_length.setter
    def maximum_password_length(self, maximum_password_length):
        """Sets the maximum_password_length of this PasswordPolicyResult.

        密码最大字符数。

        :param maximum_password_length: The maximum_password_length of this PasswordPolicyResult.
        :type maximum_password_length: int
        """
        self._maximum_password_length = maximum_password_length

    @property
    def minimum_password_age(self):
        """Gets the minimum_password_age of this PasswordPolicyResult.

        密码最短使用时间（分钟）。

        :return: The minimum_password_age of this PasswordPolicyResult.
        :rtype: int
        """
        return self._minimum_password_age

    @minimum_password_age.setter
    def minimum_password_age(self, minimum_password_age):
        """Sets the minimum_password_age of this PasswordPolicyResult.

        密码最短使用时间（分钟）。

        :param minimum_password_age: The minimum_password_age of this PasswordPolicyResult.
        :type minimum_password_age: int
        """
        self._minimum_password_age = minimum_password_age

    @property
    def minimum_password_length(self):
        """Gets the minimum_password_length of this PasswordPolicyResult.

        密码最小字符数。

        :return: The minimum_password_length of this PasswordPolicyResult.
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        """Sets the minimum_password_length of this PasswordPolicyResult.

        密码最小字符数。

        :param minimum_password_length: The minimum_password_length of this PasswordPolicyResult.
        :type minimum_password_length: int
        """
        self._minimum_password_length = minimum_password_length

    @property
    def number_of_recent_passwords_disallowed(self):
        """Gets the number_of_recent_passwords_disallowed of this PasswordPolicyResult.

        密码不能与历史密码重复次数。

        :return: The number_of_recent_passwords_disallowed of this PasswordPolicyResult.
        :rtype: int
        """
        return self._number_of_recent_passwords_disallowed

    @number_of_recent_passwords_disallowed.setter
    def number_of_recent_passwords_disallowed(self, number_of_recent_passwords_disallowed):
        """Sets the number_of_recent_passwords_disallowed of this PasswordPolicyResult.

        密码不能与历史密码重复次数。

        :param number_of_recent_passwords_disallowed: The number_of_recent_passwords_disallowed of this PasswordPolicyResult.
        :type number_of_recent_passwords_disallowed: int
        """
        self._number_of_recent_passwords_disallowed = number_of_recent_passwords_disallowed

    @property
    def password_not_username_or_invert(self):
        """Gets the password_not_username_or_invert of this PasswordPolicyResult.

        密码是否可以是用户名或用户名的反序。

        :return: The password_not_username_or_invert of this PasswordPolicyResult.
        :rtype: bool
        """
        return self._password_not_username_or_invert

    @password_not_username_or_invert.setter
    def password_not_username_or_invert(self, password_not_username_or_invert):
        """Sets the password_not_username_or_invert of this PasswordPolicyResult.

        密码是否可以是用户名或用户名的反序。

        :param password_not_username_or_invert: The password_not_username_or_invert of this PasswordPolicyResult.
        :type password_not_username_or_invert: bool
        """
        self._password_not_username_or_invert = password_not_username_or_invert

    @property
    def password_requirements(self):
        """Gets the password_requirements of this PasswordPolicyResult.

        设置密码必须包含的字符要求。

        :return: The password_requirements of this PasswordPolicyResult.
        :rtype: str
        """
        return self._password_requirements

    @password_requirements.setter
    def password_requirements(self, password_requirements):
        """Sets the password_requirements of this PasswordPolicyResult.

        设置密码必须包含的字符要求。

        :param password_requirements: The password_requirements of this PasswordPolicyResult.
        :type password_requirements: str
        """
        self._password_requirements = password_requirements

    @property
    def password_validity_period(self):
        """Gets the password_validity_period of this PasswordPolicyResult.

        密码有效期（天）。

        :return: The password_validity_period of this PasswordPolicyResult.
        :rtype: int
        """
        return self._password_validity_period

    @password_validity_period.setter
    def password_validity_period(self, password_validity_period):
        """Sets the password_validity_period of this PasswordPolicyResult.

        密码有效期（天）。

        :param password_validity_period: The password_validity_period of this PasswordPolicyResult.
        :type password_validity_period: int
        """
        self._password_validity_period = password_validity_period

    @property
    def password_char_combination(self):
        """Gets the password_char_combination of this PasswordPolicyResult.

        至少包含字符种类的个数，取值区间[2,4]。

        :return: The password_char_combination of this PasswordPolicyResult.
        :rtype: int
        """
        return self._password_char_combination

    @password_char_combination.setter
    def password_char_combination(self, password_char_combination):
        """Sets the password_char_combination of this PasswordPolicyResult.

        至少包含字符种类的个数，取值区间[2,4]。

        :param password_char_combination: The password_char_combination of this PasswordPolicyResult.
        :type password_char_combination: int
        """
        self._password_char_combination = password_char_combination

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
        if not isinstance(other, PasswordPolicyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
