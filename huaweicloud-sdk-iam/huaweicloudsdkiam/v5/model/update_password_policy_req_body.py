# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePasswordPolicyReqBody:

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
        'password_reuse_prevention': 'int',
        'password_not_username_or_invert': 'bool',
        'password_validity_period': 'int',
        'password_char_combination': 'int',
        'allow_user_to_change_password': 'bool'
    }

    attribute_map = {
        'maximum_consecutive_identical_chars': 'maximum_consecutive_identical_chars',
        'minimum_password_age': 'minimum_password_age',
        'minimum_password_length': 'minimum_password_length',
        'password_reuse_prevention': 'password_reuse_prevention',
        'password_not_username_or_invert': 'password_not_username_or_invert',
        'password_validity_period': 'password_validity_period',
        'password_char_combination': 'password_char_combination',
        'allow_user_to_change_password': 'allow_user_to_change_password'
    }

    def __init__(self, maximum_consecutive_identical_chars=None, minimum_password_age=None, minimum_password_length=None, password_reuse_prevention=None, password_not_username_or_invert=None, password_validity_period=None, password_char_combination=None, allow_user_to_change_password=None):
        r"""UpdatePasswordPolicyReqBody

        The model defined in huaweicloud sdk

        :param maximum_consecutive_identical_chars: 同一字符连续出现的最大次数，取值范围为[0,32]。
        :type maximum_consecutive_identical_chars: int
        :param minimum_password_age: 密码最短使用时间（分钟），取值范围为[0,1440]。
        :type minimum_password_age: int
        :param minimum_password_length: 密码最小字符数，取值范围为[8,32]。
        :type minimum_password_length: int
        :param password_reuse_prevention: 密码不能与历史密码重复次数，取值范围为[0,24]。
        :type password_reuse_prevention: int
        :param password_not_username_or_invert: 密码是否可以是用户名或用户名的反序。默认值为true，为true时表示密码不可以是用户名或用户名的反序。
        :type password_not_username_or_invert: bool
        :param password_validity_period: 密码有效期（天），取值范围为[0,180]。
        :type password_validity_period: int
        :param password_char_combination: 至少包含字符种类的个数，取值范围为[2,4]。
        :type password_char_combination: int
        :param allow_user_to_change_password: 是否允许IAM用户修改自己的密码，不适用于根用户。
        :type allow_user_to_change_password: bool
        """
        
        

        self._maximum_consecutive_identical_chars = None
        self._minimum_password_age = None
        self._minimum_password_length = None
        self._password_reuse_prevention = None
        self._password_not_username_or_invert = None
        self._password_validity_period = None
        self._password_char_combination = None
        self._allow_user_to_change_password = None
        self.discriminator = None

        if maximum_consecutive_identical_chars is not None:
            self.maximum_consecutive_identical_chars = maximum_consecutive_identical_chars
        if minimum_password_age is not None:
            self.minimum_password_age = minimum_password_age
        if minimum_password_length is not None:
            self.minimum_password_length = minimum_password_length
        if password_reuse_prevention is not None:
            self.password_reuse_prevention = password_reuse_prevention
        if password_not_username_or_invert is not None:
            self.password_not_username_or_invert = password_not_username_or_invert
        if password_validity_period is not None:
            self.password_validity_period = password_validity_period
        if password_char_combination is not None:
            self.password_char_combination = password_char_combination
        if allow_user_to_change_password is not None:
            self.allow_user_to_change_password = allow_user_to_change_password

    @property
    def maximum_consecutive_identical_chars(self):
        r"""Gets the maximum_consecutive_identical_chars of this UpdatePasswordPolicyReqBody.

        同一字符连续出现的最大次数，取值范围为[0,32]。

        :return: The maximum_consecutive_identical_chars of this UpdatePasswordPolicyReqBody.
        :rtype: int
        """
        return self._maximum_consecutive_identical_chars

    @maximum_consecutive_identical_chars.setter
    def maximum_consecutive_identical_chars(self, maximum_consecutive_identical_chars):
        r"""Sets the maximum_consecutive_identical_chars of this UpdatePasswordPolicyReqBody.

        同一字符连续出现的最大次数，取值范围为[0,32]。

        :param maximum_consecutive_identical_chars: The maximum_consecutive_identical_chars of this UpdatePasswordPolicyReqBody.
        :type maximum_consecutive_identical_chars: int
        """
        self._maximum_consecutive_identical_chars = maximum_consecutive_identical_chars

    @property
    def minimum_password_age(self):
        r"""Gets the minimum_password_age of this UpdatePasswordPolicyReqBody.

        密码最短使用时间（分钟），取值范围为[0,1440]。

        :return: The minimum_password_age of this UpdatePasswordPolicyReqBody.
        :rtype: int
        """
        return self._minimum_password_age

    @minimum_password_age.setter
    def minimum_password_age(self, minimum_password_age):
        r"""Sets the minimum_password_age of this UpdatePasswordPolicyReqBody.

        密码最短使用时间（分钟），取值范围为[0,1440]。

        :param minimum_password_age: The minimum_password_age of this UpdatePasswordPolicyReqBody.
        :type minimum_password_age: int
        """
        self._minimum_password_age = minimum_password_age

    @property
    def minimum_password_length(self):
        r"""Gets the minimum_password_length of this UpdatePasswordPolicyReqBody.

        密码最小字符数，取值范围为[8,32]。

        :return: The minimum_password_length of this UpdatePasswordPolicyReqBody.
        :rtype: int
        """
        return self._minimum_password_length

    @minimum_password_length.setter
    def minimum_password_length(self, minimum_password_length):
        r"""Sets the minimum_password_length of this UpdatePasswordPolicyReqBody.

        密码最小字符数，取值范围为[8,32]。

        :param minimum_password_length: The minimum_password_length of this UpdatePasswordPolicyReqBody.
        :type minimum_password_length: int
        """
        self._minimum_password_length = minimum_password_length

    @property
    def password_reuse_prevention(self):
        r"""Gets the password_reuse_prevention of this UpdatePasswordPolicyReqBody.

        密码不能与历史密码重复次数，取值范围为[0,24]。

        :return: The password_reuse_prevention of this UpdatePasswordPolicyReqBody.
        :rtype: int
        """
        return self._password_reuse_prevention

    @password_reuse_prevention.setter
    def password_reuse_prevention(self, password_reuse_prevention):
        r"""Sets the password_reuse_prevention of this UpdatePasswordPolicyReqBody.

        密码不能与历史密码重复次数，取值范围为[0,24]。

        :param password_reuse_prevention: The password_reuse_prevention of this UpdatePasswordPolicyReqBody.
        :type password_reuse_prevention: int
        """
        self._password_reuse_prevention = password_reuse_prevention

    @property
    def password_not_username_or_invert(self):
        r"""Gets the password_not_username_or_invert of this UpdatePasswordPolicyReqBody.

        密码是否可以是用户名或用户名的反序。默认值为true，为true时表示密码不可以是用户名或用户名的反序。

        :return: The password_not_username_or_invert of this UpdatePasswordPolicyReqBody.
        :rtype: bool
        """
        return self._password_not_username_or_invert

    @password_not_username_or_invert.setter
    def password_not_username_or_invert(self, password_not_username_or_invert):
        r"""Sets the password_not_username_or_invert of this UpdatePasswordPolicyReqBody.

        密码是否可以是用户名或用户名的反序。默认值为true，为true时表示密码不可以是用户名或用户名的反序。

        :param password_not_username_or_invert: The password_not_username_or_invert of this UpdatePasswordPolicyReqBody.
        :type password_not_username_or_invert: bool
        """
        self._password_not_username_or_invert = password_not_username_or_invert

    @property
    def password_validity_period(self):
        r"""Gets the password_validity_period of this UpdatePasswordPolicyReqBody.

        密码有效期（天），取值范围为[0,180]。

        :return: The password_validity_period of this UpdatePasswordPolicyReqBody.
        :rtype: int
        """
        return self._password_validity_period

    @password_validity_period.setter
    def password_validity_period(self, password_validity_period):
        r"""Sets the password_validity_period of this UpdatePasswordPolicyReqBody.

        密码有效期（天），取值范围为[0,180]。

        :param password_validity_period: The password_validity_period of this UpdatePasswordPolicyReqBody.
        :type password_validity_period: int
        """
        self._password_validity_period = password_validity_period

    @property
    def password_char_combination(self):
        r"""Gets the password_char_combination of this UpdatePasswordPolicyReqBody.

        至少包含字符种类的个数，取值范围为[2,4]。

        :return: The password_char_combination of this UpdatePasswordPolicyReqBody.
        :rtype: int
        """
        return self._password_char_combination

    @password_char_combination.setter
    def password_char_combination(self, password_char_combination):
        r"""Sets the password_char_combination of this UpdatePasswordPolicyReqBody.

        至少包含字符种类的个数，取值范围为[2,4]。

        :param password_char_combination: The password_char_combination of this UpdatePasswordPolicyReqBody.
        :type password_char_combination: int
        """
        self._password_char_combination = password_char_combination

    @property
    def allow_user_to_change_password(self):
        r"""Gets the allow_user_to_change_password of this UpdatePasswordPolicyReqBody.

        是否允许IAM用户修改自己的密码，不适用于根用户。

        :return: The allow_user_to_change_password of this UpdatePasswordPolicyReqBody.
        :rtype: bool
        """
        return self._allow_user_to_change_password

    @allow_user_to_change_password.setter
    def allow_user_to_change_password(self, allow_user_to_change_password):
        r"""Sets the allow_user_to_change_password of this UpdatePasswordPolicyReqBody.

        是否允许IAM用户修改自己的密码，不适用于根用户。

        :param allow_user_to_change_password: The allow_user_to_change_password of this UpdatePasswordPolicyReqBody.
        :type allow_user_to_change_password: bool
        """
        self._allow_user_to_change_password = allow_user_to_change_password

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
        if not isinstance(other, UpdatePasswordPolicyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
