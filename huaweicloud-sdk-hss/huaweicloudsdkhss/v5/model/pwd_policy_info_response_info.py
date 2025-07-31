# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PwdPolicyInfoResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'private_ip': 'str',
        'public_ip': 'str',
        'min_length': 'bool',
        'uppercase_letter': 'bool',
        'lowercase_letter': 'bool',
        'number': 'bool',
        'special_character': 'bool',
        'min_length_num': 'int',
        'min_uppercase_letter': 'int',
        'min_lowercase_letter': 'int',
        'min_number': 'int',
        'min_special_character': 'int',
        'update_time': 'int',
        'suggestion': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'private_ip': 'private_ip',
        'public_ip': 'public_ip',
        'min_length': 'min_length',
        'uppercase_letter': 'uppercase_letter',
        'lowercase_letter': 'lowercase_letter',
        'number': 'number',
        'special_character': 'special_character',
        'min_length_num': 'min_length_num',
        'min_uppercase_letter': 'min_uppercase_letter',
        'min_lowercase_letter': 'min_lowercase_letter',
        'min_number': 'min_number',
        'min_special_character': 'min_special_character',
        'update_time': 'update_time',
        'suggestion': 'suggestion'
    }

    def __init__(self, host_id=None, host_name=None, host_ip=None, private_ip=None, public_ip=None, min_length=None, uppercase_letter=None, lowercase_letter=None, number=None, special_character=None, min_length_num=None, min_uppercase_letter=None, min_lowercase_letter=None, min_number=None, min_special_character=None, update_time=None, suggestion=None):
        r"""PwdPolicyInfoResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 主机id **取值范围**: 不涉及 
        :type host_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 不涉及 
        :type host_name: str
        :param host_ip: **参数解释**: 服务器IP（私有IP），为兼容用户使用，不删除此字段 **取值范围**: 不涉及 
        :type host_ip: str
        :param private_ip: **参数解释**: 服务器私有IP **取值范围**: 不涉及 
        :type private_ip: str
        :param public_ip: **参数解释**: 服务器公网IP **取值范围**: 不涉及 
        :type public_ip: str
        :param min_length: **参数解释**: 口令最小长度的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 
        :type min_length: bool
        :param uppercase_letter: **参数解释**: 大写字母的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 
        :type uppercase_letter: bool
        :param lowercase_letter: **参数解释**: 小写字母的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 
        :type lowercase_letter: bool
        :param number: **参数解释**: 数字的设置是否符合要求，符合为true，不符合为false **取值范围**: - true：符合要求 - false：不符合要求 
        :type number: bool
        :param special_character: **参数解释**: 特殊字符的设置是否符合要求，符合为true，不符合为false **取值范围**: - true：符合要求 - false：不符合要求 
        :type special_character: bool
        :param min_length_num: **参数解释**: 复杂口令策略中定义的口令最小长度 **取值范围**: 8 - 26 
        :type min_length_num: int
        :param min_uppercase_letter: **参数解释**: 复杂口令策略中定义的最少包含的大写字母数 **取值范围**: 0 - 10 
        :type min_uppercase_letter: int
        :param min_lowercase_letter: **参数解释**: 复杂口令策略中定义的最少包含的小写字母数 **取值范围**: 0 - 10 
        :type min_lowercase_letter: int
        :param min_number: **参数解释**: 复杂口令策略中定义的最少包含的数字数 **取值范围**: 0 - 10 
        :type min_number: int
        :param min_special_character: **参数解释**: 复杂口令策略中定义的最少包含的特殊字母数 **取值范围**: 0 - 10 
        :type min_special_character: int
        :param update_time: **参数解释**: 最近扫描时间 **取值范围**: 不涉及 
        :type update_time: int
        :param suggestion: **参数解释**: 修改建议 **取值范围**: 不涉及 
        :type suggestion: str
        """
        
        

        self._host_id = None
        self._host_name = None
        self._host_ip = None
        self._private_ip = None
        self._public_ip = None
        self._min_length = None
        self._uppercase_letter = None
        self._lowercase_letter = None
        self._number = None
        self._special_character = None
        self._min_length_num = None
        self._min_uppercase_letter = None
        self._min_lowercase_letter = None
        self._min_number = None
        self._min_special_character = None
        self._update_time = None
        self._suggestion = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if public_ip is not None:
            self.public_ip = public_ip
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
        if min_length_num is not None:
            self.min_length_num = min_length_num
        if min_uppercase_letter is not None:
            self.min_uppercase_letter = min_uppercase_letter
        if min_lowercase_letter is not None:
            self.min_lowercase_letter = min_lowercase_letter
        if min_number is not None:
            self.min_number = min_number
        if min_special_character is not None:
            self.min_special_character = min_special_character
        if update_time is not None:
            self.update_time = update_time
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def host_id(self):
        r"""Gets the host_id of this PwdPolicyInfoResponseInfo.

        **参数解释**: 主机id **取值范围**: 不涉及 

        :return: The host_id of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this PwdPolicyInfoResponseInfo.

        **参数解释**: 主机id **取值范围**: 不涉及 

        :param host_id: The host_id of this PwdPolicyInfoResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this PwdPolicyInfoResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 不涉及 

        :return: The host_name of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this PwdPolicyInfoResponseInfo.

        **参数解释**: 服务器名称 **取值范围**: 不涉及 

        :param host_name: The host_name of this PwdPolicyInfoResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this PwdPolicyInfoResponseInfo.

        **参数解释**: 服务器IP（私有IP），为兼容用户使用，不删除此字段 **取值范围**: 不涉及 

        :return: The host_ip of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this PwdPolicyInfoResponseInfo.

        **参数解释**: 服务器IP（私有IP），为兼容用户使用，不删除此字段 **取值范围**: 不涉及 

        :param host_ip: The host_ip of this PwdPolicyInfoResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this PwdPolicyInfoResponseInfo.

        **参数解释**: 服务器私有IP **取值范围**: 不涉及 

        :return: The private_ip of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this PwdPolicyInfoResponseInfo.

        **参数解释**: 服务器私有IP **取值范围**: 不涉及 

        :param private_ip: The private_ip of this PwdPolicyInfoResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        r"""Gets the public_ip of this PwdPolicyInfoResponseInfo.

        **参数解释**: 服务器公网IP **取值范围**: 不涉及 

        :return: The public_ip of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this PwdPolicyInfoResponseInfo.

        **参数解释**: 服务器公网IP **取值范围**: 不涉及 

        :param public_ip: The public_ip of this PwdPolicyInfoResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def min_length(self):
        r"""Gets the min_length of this PwdPolicyInfoResponseInfo.

        **参数解释**: 口令最小长度的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 

        :return: The min_length of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        r"""Sets the min_length of this PwdPolicyInfoResponseInfo.

        **参数解释**: 口令最小长度的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 

        :param min_length: The min_length of this PwdPolicyInfoResponseInfo.
        :type min_length: bool
        """
        self._min_length = min_length

    @property
    def uppercase_letter(self):
        r"""Gets the uppercase_letter of this PwdPolicyInfoResponseInfo.

        **参数解释**: 大写字母的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 

        :return: The uppercase_letter of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._uppercase_letter

    @uppercase_letter.setter
    def uppercase_letter(self, uppercase_letter):
        r"""Sets the uppercase_letter of this PwdPolicyInfoResponseInfo.

        **参数解释**: 大写字母的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 

        :param uppercase_letter: The uppercase_letter of this PwdPolicyInfoResponseInfo.
        :type uppercase_letter: bool
        """
        self._uppercase_letter = uppercase_letter

    @property
    def lowercase_letter(self):
        r"""Gets the lowercase_letter of this PwdPolicyInfoResponseInfo.

        **参数解释**: 小写字母的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 

        :return: The lowercase_letter of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._lowercase_letter

    @lowercase_letter.setter
    def lowercase_letter(self, lowercase_letter):
        r"""Sets the lowercase_letter of this PwdPolicyInfoResponseInfo.

        **参数解释**: 小写字母的设置是否符合要求 **取值范围**: - true：符合要求 - false：不符合要求 

        :param lowercase_letter: The lowercase_letter of this PwdPolicyInfoResponseInfo.
        :type lowercase_letter: bool
        """
        self._lowercase_letter = lowercase_letter

    @property
    def number(self):
        r"""Gets the number of this PwdPolicyInfoResponseInfo.

        **参数解释**: 数字的设置是否符合要求，符合为true，不符合为false **取值范围**: - true：符合要求 - false：不符合要求 

        :return: The number of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this PwdPolicyInfoResponseInfo.

        **参数解释**: 数字的设置是否符合要求，符合为true，不符合为false **取值范围**: - true：符合要求 - false：不符合要求 

        :param number: The number of this PwdPolicyInfoResponseInfo.
        :type number: bool
        """
        self._number = number

    @property
    def special_character(self):
        r"""Gets the special_character of this PwdPolicyInfoResponseInfo.

        **参数解释**: 特殊字符的设置是否符合要求，符合为true，不符合为false **取值范围**: - true：符合要求 - false：不符合要求 

        :return: The special_character of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._special_character

    @special_character.setter
    def special_character(self, special_character):
        r"""Sets the special_character of this PwdPolicyInfoResponseInfo.

        **参数解释**: 特殊字符的设置是否符合要求，符合为true，不符合为false **取值范围**: - true：符合要求 - false：不符合要求 

        :param special_character: The special_character of this PwdPolicyInfoResponseInfo.
        :type special_character: bool
        """
        self._special_character = special_character

    @property
    def min_length_num(self):
        r"""Gets the min_length_num of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的口令最小长度 **取值范围**: 8 - 26 

        :return: The min_length_num of this PwdPolicyInfoResponseInfo.
        :rtype: int
        """
        return self._min_length_num

    @min_length_num.setter
    def min_length_num(self, min_length_num):
        r"""Sets the min_length_num of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的口令最小长度 **取值范围**: 8 - 26 

        :param min_length_num: The min_length_num of this PwdPolicyInfoResponseInfo.
        :type min_length_num: int
        """
        self._min_length_num = min_length_num

    @property
    def min_uppercase_letter(self):
        r"""Gets the min_uppercase_letter of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的最少包含的大写字母数 **取值范围**: 0 - 10 

        :return: The min_uppercase_letter of this PwdPolicyInfoResponseInfo.
        :rtype: int
        """
        return self._min_uppercase_letter

    @min_uppercase_letter.setter
    def min_uppercase_letter(self, min_uppercase_letter):
        r"""Sets the min_uppercase_letter of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的最少包含的大写字母数 **取值范围**: 0 - 10 

        :param min_uppercase_letter: The min_uppercase_letter of this PwdPolicyInfoResponseInfo.
        :type min_uppercase_letter: int
        """
        self._min_uppercase_letter = min_uppercase_letter

    @property
    def min_lowercase_letter(self):
        r"""Gets the min_lowercase_letter of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的最少包含的小写字母数 **取值范围**: 0 - 10 

        :return: The min_lowercase_letter of this PwdPolicyInfoResponseInfo.
        :rtype: int
        """
        return self._min_lowercase_letter

    @min_lowercase_letter.setter
    def min_lowercase_letter(self, min_lowercase_letter):
        r"""Sets the min_lowercase_letter of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的最少包含的小写字母数 **取值范围**: 0 - 10 

        :param min_lowercase_letter: The min_lowercase_letter of this PwdPolicyInfoResponseInfo.
        :type min_lowercase_letter: int
        """
        self._min_lowercase_letter = min_lowercase_letter

    @property
    def min_number(self):
        r"""Gets the min_number of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的最少包含的数字数 **取值范围**: 0 - 10 

        :return: The min_number of this PwdPolicyInfoResponseInfo.
        :rtype: int
        """
        return self._min_number

    @min_number.setter
    def min_number(self, min_number):
        r"""Sets the min_number of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的最少包含的数字数 **取值范围**: 0 - 10 

        :param min_number: The min_number of this PwdPolicyInfoResponseInfo.
        :type min_number: int
        """
        self._min_number = min_number

    @property
    def min_special_character(self):
        r"""Gets the min_special_character of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的最少包含的特殊字母数 **取值范围**: 0 - 10 

        :return: The min_special_character of this PwdPolicyInfoResponseInfo.
        :rtype: int
        """
        return self._min_special_character

    @min_special_character.setter
    def min_special_character(self, min_special_character):
        r"""Sets the min_special_character of this PwdPolicyInfoResponseInfo.

        **参数解释**: 复杂口令策略中定义的最少包含的特殊字母数 **取值范围**: 0 - 10 

        :param min_special_character: The min_special_character of this PwdPolicyInfoResponseInfo.
        :type min_special_character: int
        """
        self._min_special_character = min_special_character

    @property
    def update_time(self):
        r"""Gets the update_time of this PwdPolicyInfoResponseInfo.

        **参数解释**: 最近扫描时间 **取值范围**: 不涉及 

        :return: The update_time of this PwdPolicyInfoResponseInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PwdPolicyInfoResponseInfo.

        **参数解释**: 最近扫描时间 **取值范围**: 不涉及 

        :param update_time: The update_time of this PwdPolicyInfoResponseInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def suggestion(self):
        r"""Gets the suggestion of this PwdPolicyInfoResponseInfo.

        **参数解释**: 修改建议 **取值范围**: 不涉及 

        :return: The suggestion of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this PwdPolicyInfoResponseInfo.

        **参数解释**: 修改建议 **取值范围**: 不涉及 

        :param suggestion: The suggestion of this PwdPolicyInfoResponseInfo.
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
        if not isinstance(other, PwdPolicyInfoResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
