# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppOutputParameterDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'required': 'bool',
        'type': 'str',
        'pattern': 'str',
        'values': 'list[str]',
        'enum': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'required': 'required',
        'type': 'type',
        'pattern': 'pattern',
        'values': 'values',
        'enum': 'enum'
    }

    def __init__(self, name=None, description=None, required=None, type=None, pattern=None, values=None, enum=None):
        """AppOutputParameterDto

        The model defined in huaweicloud sdk

        :param name: 参数名称，单个应用内唯一。取值范围：长度为[1,32]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。
        :type name: str
        :param description: 参数描述。取值范围：[0-255]
        :type description: str
        :param required: 参数是否必须
        :type required: bool
        :param type: 参数类型。取值：[STRING，FILE，DIRECTORY，ENUM]
        :type type: str
        :param pattern: 提示用户参数填写的格式，取值范围：[0-64]。对于STRING类型，匹配字符串内容，比如后缀约束.fastq；对于ENUM类型，可以提示一定要在param_enum列表范围内取值；对于FILE类型，约束文件后缀类型；对于DIRECTORY类型，提示目录下需要包含哪些文件；
        :type pattern: str
        :param values: 参数取值 如填写，只支持填一项，根据参数类型进行不同的校验
        :type values: list[str]
        :param enum: 枚举参数的取值列表，列表最大长度20，每一项字符串最长128。参数类型为ENUM时需要填此字段
        :type enum: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._required = None
        self._type = None
        self._pattern = None
        self._values = None
        self._enum = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.required = required
        self.type = type
        if pattern is not None:
            self.pattern = pattern
        if values is not None:
            self.values = values
        if enum is not None:
            self.enum = enum

    @property
    def name(self):
        """Gets the name of this AppOutputParameterDto.

        参数名称，单个应用内唯一。取值范围：长度为[1,32]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。

        :return: The name of this AppOutputParameterDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppOutputParameterDto.

        参数名称，单个应用内唯一。取值范围：长度为[1,32]，以小写字母开头，允许出现中划线(-)、小写字母和数字，且必须以小写字母或数字结尾。

        :param name: The name of this AppOutputParameterDto.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AppOutputParameterDto.

        参数描述。取值范围：[0-255]

        :return: The description of this AppOutputParameterDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppOutputParameterDto.

        参数描述。取值范围：[0-255]

        :param description: The description of this AppOutputParameterDto.
        :type description: str
        """
        self._description = description

    @property
    def required(self):
        """Gets the required of this AppOutputParameterDto.

        参数是否必须

        :return: The required of this AppOutputParameterDto.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this AppOutputParameterDto.

        参数是否必须

        :param required: The required of this AppOutputParameterDto.
        :type required: bool
        """
        self._required = required

    @property
    def type(self):
        """Gets the type of this AppOutputParameterDto.

        参数类型。取值：[STRING，FILE，DIRECTORY，ENUM]

        :return: The type of this AppOutputParameterDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AppOutputParameterDto.

        参数类型。取值：[STRING，FILE，DIRECTORY，ENUM]

        :param type: The type of this AppOutputParameterDto.
        :type type: str
        """
        self._type = type

    @property
    def pattern(self):
        """Gets the pattern of this AppOutputParameterDto.

        提示用户参数填写的格式，取值范围：[0-64]。对于STRING类型，匹配字符串内容，比如后缀约束.fastq；对于ENUM类型，可以提示一定要在param_enum列表范围内取值；对于FILE类型，约束文件后缀类型；对于DIRECTORY类型，提示目录下需要包含哪些文件；

        :return: The pattern of this AppOutputParameterDto.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this AppOutputParameterDto.

        提示用户参数填写的格式，取值范围：[0-64]。对于STRING类型，匹配字符串内容，比如后缀约束.fastq；对于ENUM类型，可以提示一定要在param_enum列表范围内取值；对于FILE类型，约束文件后缀类型；对于DIRECTORY类型，提示目录下需要包含哪些文件；

        :param pattern: The pattern of this AppOutputParameterDto.
        :type pattern: str
        """
        self._pattern = pattern

    @property
    def values(self):
        """Gets the values of this AppOutputParameterDto.

        参数取值 如填写，只支持填一项，根据参数类型进行不同的校验

        :return: The values of this AppOutputParameterDto.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this AppOutputParameterDto.

        参数取值 如填写，只支持填一项，根据参数类型进行不同的校验

        :param values: The values of this AppOutputParameterDto.
        :type values: list[str]
        """
        self._values = values

    @property
    def enum(self):
        """Gets the enum of this AppOutputParameterDto.

        枚举参数的取值列表，列表最大长度20，每一项字符串最长128。参数类型为ENUM时需要填此字段

        :return: The enum of this AppOutputParameterDto.
        :rtype: list[str]
        """
        return self._enum

    @enum.setter
    def enum(self, enum):
        """Sets the enum of this AppOutputParameterDto.

        枚举参数的取值列表，列表最大长度20，每一项字符串最长128。参数类型为ENUM时需要填此字段

        :param enum: The enum of this AppOutputParameterDto.
        :type enum: list[str]
        """
        self._enum = enum

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
        if not isinstance(other, AppOutputParameterDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
