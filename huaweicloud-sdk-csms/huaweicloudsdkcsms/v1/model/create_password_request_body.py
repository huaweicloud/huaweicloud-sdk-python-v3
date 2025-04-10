# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePasswordRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password_policy_name': 'str',
        'length': 'int',
        'exclude_characters': 'str',
        'exclude_lowercase': 'bool',
        'exclude_uppercase': 'bool',
        'exclude_numbers': 'bool',
        'exclude_punctuation': 'bool',
        'include_space': 'bool',
        'require_each_included_type': 'bool'
    }

    attribute_map = {
        'password_policy_name': 'password_policy_name',
        'length': 'length',
        'exclude_characters': 'exclude_characters',
        'exclude_lowercase': 'exclude_lowercase',
        'exclude_uppercase': 'exclude_uppercase',
        'exclude_numbers': 'exclude_numbers',
        'exclude_punctuation': 'exclude_punctuation',
        'include_space': 'include_space',
        'require_each_included_type': 'require_each_included_type'
    }

    def __init__(self, password_policy_name=None, length=None, exclude_characters=None, exclude_lowercase=None, exclude_uppercase=None, exclude_numbers=None, exclude_punctuation=None, include_space=None, require_each_included_type=None):
        r"""CreatePasswordRequestBody

        The model defined in huaweicloud sdk

        :param password_policy_name: 策略名称
        :type password_policy_name: str
        :param length: 长度，默认32
        :type length: int
        :param exclude_characters: 需要排除的字符
        :type exclude_characters: str
        :param exclude_lowercase: 排除小写字母，默认false
        :type exclude_lowercase: bool
        :param exclude_uppercase: 排除大写字母，默认false
        :type exclude_uppercase: bool
        :param exclude_numbers: 排除数字，默认false
        :type exclude_numbers: bool
        :param exclude_punctuation: 排除符号，默认false
        :type exclude_punctuation: bool
        :param include_space: 包含空格，默认false
        :type include_space: bool
        :param require_each_included_type: 需要每个包含的类型，默认false
        :type require_each_included_type: bool
        """
        
        

        self._password_policy_name = None
        self._length = None
        self._exclude_characters = None
        self._exclude_lowercase = None
        self._exclude_uppercase = None
        self._exclude_numbers = None
        self._exclude_punctuation = None
        self._include_space = None
        self._require_each_included_type = None
        self.discriminator = None

        if password_policy_name is not None:
            self.password_policy_name = password_policy_name
        if length is not None:
            self.length = length
        if exclude_characters is not None:
            self.exclude_characters = exclude_characters
        if exclude_lowercase is not None:
            self.exclude_lowercase = exclude_lowercase
        if exclude_uppercase is not None:
            self.exclude_uppercase = exclude_uppercase
        if exclude_numbers is not None:
            self.exclude_numbers = exclude_numbers
        if exclude_punctuation is not None:
            self.exclude_punctuation = exclude_punctuation
        if include_space is not None:
            self.include_space = include_space
        if require_each_included_type is not None:
            self.require_each_included_type = require_each_included_type

    @property
    def password_policy_name(self):
        r"""Gets the password_policy_name of this CreatePasswordRequestBody.

        策略名称

        :return: The password_policy_name of this CreatePasswordRequestBody.
        :rtype: str
        """
        return self._password_policy_name

    @password_policy_name.setter
    def password_policy_name(self, password_policy_name):
        r"""Sets the password_policy_name of this CreatePasswordRequestBody.

        策略名称

        :param password_policy_name: The password_policy_name of this CreatePasswordRequestBody.
        :type password_policy_name: str
        """
        self._password_policy_name = password_policy_name

    @property
    def length(self):
        r"""Gets the length of this CreatePasswordRequestBody.

        长度，默认32

        :return: The length of this CreatePasswordRequestBody.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        r"""Sets the length of this CreatePasswordRequestBody.

        长度，默认32

        :param length: The length of this CreatePasswordRequestBody.
        :type length: int
        """
        self._length = length

    @property
    def exclude_characters(self):
        r"""Gets the exclude_characters of this CreatePasswordRequestBody.

        需要排除的字符

        :return: The exclude_characters of this CreatePasswordRequestBody.
        :rtype: str
        """
        return self._exclude_characters

    @exclude_characters.setter
    def exclude_characters(self, exclude_characters):
        r"""Sets the exclude_characters of this CreatePasswordRequestBody.

        需要排除的字符

        :param exclude_characters: The exclude_characters of this CreatePasswordRequestBody.
        :type exclude_characters: str
        """
        self._exclude_characters = exclude_characters

    @property
    def exclude_lowercase(self):
        r"""Gets the exclude_lowercase of this CreatePasswordRequestBody.

        排除小写字母，默认false

        :return: The exclude_lowercase of this CreatePasswordRequestBody.
        :rtype: bool
        """
        return self._exclude_lowercase

    @exclude_lowercase.setter
    def exclude_lowercase(self, exclude_lowercase):
        r"""Sets the exclude_lowercase of this CreatePasswordRequestBody.

        排除小写字母，默认false

        :param exclude_lowercase: The exclude_lowercase of this CreatePasswordRequestBody.
        :type exclude_lowercase: bool
        """
        self._exclude_lowercase = exclude_lowercase

    @property
    def exclude_uppercase(self):
        r"""Gets the exclude_uppercase of this CreatePasswordRequestBody.

        排除大写字母，默认false

        :return: The exclude_uppercase of this CreatePasswordRequestBody.
        :rtype: bool
        """
        return self._exclude_uppercase

    @exclude_uppercase.setter
    def exclude_uppercase(self, exclude_uppercase):
        r"""Sets the exclude_uppercase of this CreatePasswordRequestBody.

        排除大写字母，默认false

        :param exclude_uppercase: The exclude_uppercase of this CreatePasswordRequestBody.
        :type exclude_uppercase: bool
        """
        self._exclude_uppercase = exclude_uppercase

    @property
    def exclude_numbers(self):
        r"""Gets the exclude_numbers of this CreatePasswordRequestBody.

        排除数字，默认false

        :return: The exclude_numbers of this CreatePasswordRequestBody.
        :rtype: bool
        """
        return self._exclude_numbers

    @exclude_numbers.setter
    def exclude_numbers(self, exclude_numbers):
        r"""Sets the exclude_numbers of this CreatePasswordRequestBody.

        排除数字，默认false

        :param exclude_numbers: The exclude_numbers of this CreatePasswordRequestBody.
        :type exclude_numbers: bool
        """
        self._exclude_numbers = exclude_numbers

    @property
    def exclude_punctuation(self):
        r"""Gets the exclude_punctuation of this CreatePasswordRequestBody.

        排除符号，默认false

        :return: The exclude_punctuation of this CreatePasswordRequestBody.
        :rtype: bool
        """
        return self._exclude_punctuation

    @exclude_punctuation.setter
    def exclude_punctuation(self, exclude_punctuation):
        r"""Sets the exclude_punctuation of this CreatePasswordRequestBody.

        排除符号，默认false

        :param exclude_punctuation: The exclude_punctuation of this CreatePasswordRequestBody.
        :type exclude_punctuation: bool
        """
        self._exclude_punctuation = exclude_punctuation

    @property
    def include_space(self):
        r"""Gets the include_space of this CreatePasswordRequestBody.

        包含空格，默认false

        :return: The include_space of this CreatePasswordRequestBody.
        :rtype: bool
        """
        return self._include_space

    @include_space.setter
    def include_space(self, include_space):
        r"""Sets the include_space of this CreatePasswordRequestBody.

        包含空格，默认false

        :param include_space: The include_space of this CreatePasswordRequestBody.
        :type include_space: bool
        """
        self._include_space = include_space

    @property
    def require_each_included_type(self):
        r"""Gets the require_each_included_type of this CreatePasswordRequestBody.

        需要每个包含的类型，默认false

        :return: The require_each_included_type of this CreatePasswordRequestBody.
        :rtype: bool
        """
        return self._require_each_included_type

    @require_each_included_type.setter
    def require_each_included_type(self, require_each_included_type):
        r"""Sets the require_each_included_type of this CreatePasswordRequestBody.

        需要每个包含的类型，默认false

        :param require_each_included_type: The require_each_included_type of this CreatePasswordRequestBody.
        :type require_each_included_type: bool
        """
        self._require_each_included_type = require_each_included_type

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
        if not isinstance(other, CreatePasswordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
