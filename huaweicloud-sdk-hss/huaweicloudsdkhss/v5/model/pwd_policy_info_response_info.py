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
        'suggestion': 'suggestion'
    }

    def __init__(self, host_id=None, host_name=None, host_ip=None, private_ip=None, public_ip=None, min_length=None, uppercase_letter=None, lowercase_letter=None, number=None, special_character=None, suggestion=None):
        """PwdPolicyInfoResponseInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 服务器IP（私有IP），为兼容用户使用，不删除此字段
        :type host_ip: str
        :param private_ip: 服务器私有IP
        :type private_ip: str
        :param public_ip: 服务器公网IP
        :type public_ip: str
        :param min_length: 口令最小长度的设置是否符合要求，符合为true，不符合为false
        :type min_length: bool
        :param uppercase_letter: 大写字母的设置是否符合要求，符合为true，不符合为false
        :type uppercase_letter: bool
        :param lowercase_letter: 小写字母的设置是否符合要求，符合为true，不符合为false
        :type lowercase_letter: bool
        :param number: 数字的设置是否符合要求，符合为true，不符合为false
        :type number: bool
        :param special_character: 特殊字符的设置是否符合要求，符合为true，不符合为false
        :type special_character: bool
        :param suggestion: 修改建议
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
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def host_id(self):
        """Gets the host_id of this PwdPolicyInfoResponseInfo.

        主机id

        :return: The host_id of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this PwdPolicyInfoResponseInfo.

        主机id

        :param host_id: The host_id of this PwdPolicyInfoResponseInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        """Gets the host_name of this PwdPolicyInfoResponseInfo.

        服务器名称

        :return: The host_name of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this PwdPolicyInfoResponseInfo.

        服务器名称

        :param host_name: The host_name of this PwdPolicyInfoResponseInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this PwdPolicyInfoResponseInfo.

        服务器IP（私有IP），为兼容用户使用，不删除此字段

        :return: The host_ip of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this PwdPolicyInfoResponseInfo.

        服务器IP（私有IP），为兼容用户使用，不删除此字段

        :param host_ip: The host_ip of this PwdPolicyInfoResponseInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def private_ip(self):
        """Gets the private_ip of this PwdPolicyInfoResponseInfo.

        服务器私有IP

        :return: The private_ip of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this PwdPolicyInfoResponseInfo.

        服务器私有IP

        :param private_ip: The private_ip of this PwdPolicyInfoResponseInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def public_ip(self):
        """Gets the public_ip of this PwdPolicyInfoResponseInfo.

        服务器公网IP

        :return: The public_ip of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this PwdPolicyInfoResponseInfo.

        服务器公网IP

        :param public_ip: The public_ip of this PwdPolicyInfoResponseInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def min_length(self):
        """Gets the min_length of this PwdPolicyInfoResponseInfo.

        口令最小长度的设置是否符合要求，符合为true，不符合为false

        :return: The min_length of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this PwdPolicyInfoResponseInfo.

        口令最小长度的设置是否符合要求，符合为true，不符合为false

        :param min_length: The min_length of this PwdPolicyInfoResponseInfo.
        :type min_length: bool
        """
        self._min_length = min_length

    @property
    def uppercase_letter(self):
        """Gets the uppercase_letter of this PwdPolicyInfoResponseInfo.

        大写字母的设置是否符合要求，符合为true，不符合为false

        :return: The uppercase_letter of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._uppercase_letter

    @uppercase_letter.setter
    def uppercase_letter(self, uppercase_letter):
        """Sets the uppercase_letter of this PwdPolicyInfoResponseInfo.

        大写字母的设置是否符合要求，符合为true，不符合为false

        :param uppercase_letter: The uppercase_letter of this PwdPolicyInfoResponseInfo.
        :type uppercase_letter: bool
        """
        self._uppercase_letter = uppercase_letter

    @property
    def lowercase_letter(self):
        """Gets the lowercase_letter of this PwdPolicyInfoResponseInfo.

        小写字母的设置是否符合要求，符合为true，不符合为false

        :return: The lowercase_letter of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._lowercase_letter

    @lowercase_letter.setter
    def lowercase_letter(self, lowercase_letter):
        """Sets the lowercase_letter of this PwdPolicyInfoResponseInfo.

        小写字母的设置是否符合要求，符合为true，不符合为false

        :param lowercase_letter: The lowercase_letter of this PwdPolicyInfoResponseInfo.
        :type lowercase_letter: bool
        """
        self._lowercase_letter = lowercase_letter

    @property
    def number(self):
        """Gets the number of this PwdPolicyInfoResponseInfo.

        数字的设置是否符合要求，符合为true，不符合为false

        :return: The number of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PwdPolicyInfoResponseInfo.

        数字的设置是否符合要求，符合为true，不符合为false

        :param number: The number of this PwdPolicyInfoResponseInfo.
        :type number: bool
        """
        self._number = number

    @property
    def special_character(self):
        """Gets the special_character of this PwdPolicyInfoResponseInfo.

        特殊字符的设置是否符合要求，符合为true，不符合为false

        :return: The special_character of this PwdPolicyInfoResponseInfo.
        :rtype: bool
        """
        return self._special_character

    @special_character.setter
    def special_character(self, special_character):
        """Sets the special_character of this PwdPolicyInfoResponseInfo.

        特殊字符的设置是否符合要求，符合为true，不符合为false

        :param special_character: The special_character of this PwdPolicyInfoResponseInfo.
        :type special_character: bool
        """
        self._special_character = special_character

    @property
    def suggestion(self):
        """Gets the suggestion of this PwdPolicyInfoResponseInfo.

        修改建议

        :return: The suggestion of this PwdPolicyInfoResponseInfo.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this PwdPolicyInfoResponseInfo.

        修改建议

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
