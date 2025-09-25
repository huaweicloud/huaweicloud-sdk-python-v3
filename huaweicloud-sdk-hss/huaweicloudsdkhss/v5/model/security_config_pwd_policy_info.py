# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityConfigPwdPolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_length': 'bool',
        'uppercase_letter': 'bool',
        'lowercase_letter': 'bool',
        'number': 'bool',
        'special_character': 'bool',
        'suggestion': 'str'
    }

    attribute_map = {
        'min_length': 'min_length',
        'uppercase_letter': 'uppercase_letter',
        'lowercase_letter': 'lowercase_letter',
        'number': 'number',
        'special_character': 'special_character',
        'suggestion': 'suggestion'
    }

    def __init__(self, min_length=None, uppercase_letter=None, lowercase_letter=None, number=None, special_character=None, suggestion=None):
        r"""SecurityConfigPwdPolicyInfo

        The model defined in huaweicloud sdk

        :param min_length: **参数解释**： 口令最小长度策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 
        :type min_length: bool
        :param uppercase_letter: **参数解释**： 大写字母策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 
        :type uppercase_letter: bool
        :param lowercase_letter: **参数解释**： 小写字母策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 
        :type lowercase_letter: bool
        :param number: **参数解释**： 数字策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求不涉及 
        :type number: bool
        :param special_character: **参数解释**： 特殊字符策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 
        :type special_character: bool
        :param suggestion: **参数解释**： 修改建议 **取值范围**： 不涉及 
        :type suggestion: str
        """
        
        

        self._min_length = None
        self._uppercase_letter = None
        self._lowercase_letter = None
        self._number = None
        self._special_character = None
        self._suggestion = None
        self.discriminator = None

        if min_length is not None:
            self.min_length = min_length
        if uppercase_letter is not None:
            self.uppercase_letter = uppercase_letter
        if lowercase_letter is not None:
            self.lowercase_letter = lowercase_letter
        if number is not None:
            self.number = number
        if special_character is not None:
            self.special_character = special_character
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def min_length(self):
        r"""Gets the min_length of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 口令最小长度策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 

        :return: The min_length of this SecurityConfigPwdPolicyInfo.
        :rtype: bool
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        r"""Sets the min_length of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 口令最小长度策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 

        :param min_length: The min_length of this SecurityConfigPwdPolicyInfo.
        :type min_length: bool
        """
        self._min_length = min_length

    @property
    def uppercase_letter(self):
        r"""Gets the uppercase_letter of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 大写字母策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 

        :return: The uppercase_letter of this SecurityConfigPwdPolicyInfo.
        :rtype: bool
        """
        return self._uppercase_letter

    @uppercase_letter.setter
    def uppercase_letter(self, uppercase_letter):
        r"""Sets the uppercase_letter of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 大写字母策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 

        :param uppercase_letter: The uppercase_letter of this SecurityConfigPwdPolicyInfo.
        :type uppercase_letter: bool
        """
        self._uppercase_letter = uppercase_letter

    @property
    def lowercase_letter(self):
        r"""Gets the lowercase_letter of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 小写字母策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 

        :return: The lowercase_letter of this SecurityConfigPwdPolicyInfo.
        :rtype: bool
        """
        return self._lowercase_letter

    @lowercase_letter.setter
    def lowercase_letter(self, lowercase_letter):
        r"""Sets the lowercase_letter of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 小写字母策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 

        :param lowercase_letter: The lowercase_letter of this SecurityConfigPwdPolicyInfo.
        :type lowercase_letter: bool
        """
        self._lowercase_letter = lowercase_letter

    @property
    def number(self):
        r"""Gets the number of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 数字策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求不涉及 

        :return: The number of this SecurityConfigPwdPolicyInfo.
        :rtype: bool
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 数字策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求不涉及 

        :param number: The number of this SecurityConfigPwdPolicyInfo.
        :type number: bool
        """
        self._number = number

    @property
    def special_character(self):
        r"""Gets the special_character of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 特殊字符策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 

        :return: The special_character of this SecurityConfigPwdPolicyInfo.
        :rtype: bool
        """
        return self._special_character

    @special_character.setter
    def special_character(self, special_character):
        r"""Sets the special_character of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 特殊字符策略是否满足要求 **取值范围**： - true：满足要求 - false：不满足要求 

        :param special_character: The special_character of this SecurityConfigPwdPolicyInfo.
        :type special_character: bool
        """
        self._special_character = special_character

    @property
    def suggestion(self):
        r"""Gets the suggestion of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 修改建议 **取值范围**： 不涉及 

        :return: The suggestion of this SecurityConfigPwdPolicyInfo.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this SecurityConfigPwdPolicyInfo.

        **参数解释**： 修改建议 **取值范围**： 不涉及 

        :param suggestion: The suggestion of this SecurityConfigPwdPolicyInfo.
        :type suggestion: str
        """
        self._suggestion = suggestion

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
        if not isinstance(other, SecurityConfigPwdPolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
