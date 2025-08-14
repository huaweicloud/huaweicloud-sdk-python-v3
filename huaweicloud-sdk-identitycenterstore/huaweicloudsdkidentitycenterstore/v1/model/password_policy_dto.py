# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PasswordPolicyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'minimum_password_length': 'int',
        'require_lowercase_characters': 'bool',
        'require_numbers': 'bool',
        'require_symbols': 'bool',
        'require_uppercase_characters': 'bool',
        'max_password_age': 'int',
        'password_reuse_prevention': 'int'
    }

    attribute_map = {
        'minimum_password_length': 'minimum_password_length',
        'require_lowercase_characters': 'require_lowercase_characters',
        'require_numbers': 'require_numbers',
        'require_symbols': 'require_symbols',
        'require_uppercase_characters': 'require_uppercase_characters',
        'max_password_age': 'max_password_age',
        'password_reuse_prevention': 'password_reuse_prevention'
    }

    def __init__(self, minimum_password_length=None, require_lowercase_characters=None, require_numbers=None, require_symbols=None, require_uppercase_characters=None, max_password_age=None, password_reuse_prevention=None):
        r"""PasswordPolicyDto

        The model defined in huaweicloud sdk

        :param minimum_password_length: 最小密码长度
        :type minimum_password_length: int
        :param require_lowercase_characters: 是否要求小写字母
        :type require_lowercase_characters: bool
        :param require_numbers: 是否要求数字
        :type require_numbers: bool
        :param require_symbols: 是否要求特殊字符
        :type require_symbols: bool
        :param require_uppercase_characters: 是否要求大写字母
        :type require_uppercase_characters: bool
        :param max_password_age: 密码有效期
        :type max_password_age: int
        :param password_reuse_prevention: 密码重复使用次数，默认只支持1
        :type password_reuse_prevention: int
        """
        
        

        self._minimum_password_length = None
        self._require_lowercase_characters = None
        self._require_numbers = None
        self._require_symbols = None
        self._require_uppercase_characters = None
        self._max_password_age = None
        self._password_reuse_prevention = None
        self.discriminator = None

        if minimum_password_length is not None:
            self.minimum_password_length = minimum_password_length
        if require_lowercase_characters is not None:
            self.require_lowercase_characters = require_lowercase_characters
        if require_numbers is not None:
            self.require_numbers = require_numbers
        if require_symbols is not None:
            self.require_symbols = require_symbols
        if require_uppercase_characters is not None:
            self.require_uppercase_characters = require_uppercase_characters
        if max_password_age is not None:
            self.max_password_age = max_password_age
        if password_reuse_prevention is not None:
            self.password_reuse_prevention = password_reuse_prevention

    @property
    def minimum_password_length(self):
        r"""Gets the minimum_password_length of this PasswordPolicyDto.

        最小密码长度

        :return: The minimum_password_length of this PasswordPolicyDto.
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        r"""Sets the minimum_password_length of this PasswordPolicyDto.

        最小密码长度

        :param minimum_password_length: The minimum_password_length of this PasswordPolicyDto.
        :type minimum_password_length: int
        """
        self._minimum_password_length = minimum_password_length

    @property
    def require_lowercase_characters(self):
        r"""Gets the require_lowercase_characters of this PasswordPolicyDto.

        是否要求小写字母

        :return: The require_lowercase_characters of this PasswordPolicyDto.
        :rtype: bool
        """
        return self._require_lowercase_characters

    @require_lowercase_characters.setter
    def require_lowercase_characters(self, require_lowercase_characters):
        r"""Sets the require_lowercase_characters of this PasswordPolicyDto.

        是否要求小写字母

        :param require_lowercase_characters: The require_lowercase_characters of this PasswordPolicyDto.
        :type require_lowercase_characters: bool
        """
        self._require_lowercase_characters = require_lowercase_characters

    @property
    def require_numbers(self):
        r"""Gets the require_numbers of this PasswordPolicyDto.

        是否要求数字

        :return: The require_numbers of this PasswordPolicyDto.
        :rtype: bool
        """
        return self._require_numbers

    @require_numbers.setter
    def require_numbers(self, require_numbers):
        r"""Sets the require_numbers of this PasswordPolicyDto.

        是否要求数字

        :param require_numbers: The require_numbers of this PasswordPolicyDto.
        :type require_numbers: bool
        """
        self._require_numbers = require_numbers

    @property
    def require_symbols(self):
        r"""Gets the require_symbols of this PasswordPolicyDto.

        是否要求特殊字符

        :return: The require_symbols of this PasswordPolicyDto.
        :rtype: bool
        """
        return self._require_symbols

    @require_symbols.setter
    def require_symbols(self, require_symbols):
        r"""Sets the require_symbols of this PasswordPolicyDto.

        是否要求特殊字符

        :param require_symbols: The require_symbols of this PasswordPolicyDto.
        :type require_symbols: bool
        """
        self._require_symbols = require_symbols

    @property
    def require_uppercase_characters(self):
        r"""Gets the require_uppercase_characters of this PasswordPolicyDto.

        是否要求大写字母

        :return: The require_uppercase_characters of this PasswordPolicyDto.
        :rtype: bool
        """
        return self._require_uppercase_characters

    @require_uppercase_characters.setter
    def require_uppercase_characters(self, require_uppercase_characters):
        r"""Sets the require_uppercase_characters of this PasswordPolicyDto.

        是否要求大写字母

        :param require_uppercase_characters: The require_uppercase_characters of this PasswordPolicyDto.
        :type require_uppercase_characters: bool
        """
        self._require_uppercase_characters = require_uppercase_characters

    @property
    def max_password_age(self):
        r"""Gets the max_password_age of this PasswordPolicyDto.

        密码有效期

        :return: The max_password_age of this PasswordPolicyDto.
        :rtype: int
        """
        return self._max_password_age

    @max_password_age.setter
    def max_password_age(self, max_password_age):
        r"""Sets the max_password_age of this PasswordPolicyDto.

        密码有效期

        :param max_password_age: The max_password_age of this PasswordPolicyDto.
        :type max_password_age: int
        """
        self._max_password_age = max_password_age

    @property
    def password_reuse_prevention(self):
        r"""Gets the password_reuse_prevention of this PasswordPolicyDto.

        密码重复使用次数，默认只支持1

        :return: The password_reuse_prevention of this PasswordPolicyDto.
        :rtype: int
        """
        return self._password_reuse_prevention

    @password_reuse_prevention.setter
    def password_reuse_prevention(self, password_reuse_prevention):
        r"""Sets the password_reuse_prevention of this PasswordPolicyDto.

        密码重复使用次数，默认只支持1

        :param password_reuse_prevention: The password_reuse_prevention of this PasswordPolicyDto.
        :type password_reuse_prevention: int
        """
        self._password_reuse_prevention = password_reuse_prevention

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
        if not isinstance(other, PasswordPolicyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
