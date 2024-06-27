# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dependent_info': 'list[ConditionInstance]',
        'enabled': 'bool',
        'is_config_dep': 'bool',
        'is_dependent': 'bool',
        'message': 'str',
        'result': 'str',
        'special_char': 'str',
        'special_char_valid': 'str',
        'x_example': 'str'
    }

    attribute_map = {
        'dependent_info': 'dependent_info',
        'enabled': 'enabled',
        'is_config_dep': 'is_configDep',
        'is_dependent': 'is_dependent',
        'message': 'message',
        'result': 'result',
        'special_char': 'special_char',
        'special_char_valid': 'special_char_valid',
        'x_example': 'x_example'
    }

    def __init__(self, dependent_info=None, enabled=None, is_config_dep=None, is_dependent=None, message=None, result=None, special_char=None, special_char_valid=None, x_example=None):
        """ValidateRule

        The model defined in huaweicloud sdk

        :param dependent_info: 依赖信息列表
        :type dependent_info: list[:class:`huaweicloudsdkcloudtest.v1.ConditionInstance`]
        :param enabled: 是否启用的标识符
        :type enabled: bool
        :param is_config_dep: 配置依赖的标识符
        :type is_config_dep: bool
        :param is_dependent: 是否依赖的标识符
        :type is_dependent: bool
        :param message: 消息
        :type message: str
        :param result: 结果
        :type result: str
        :param special_char: 特殊字符
        :type special_char: str
        :param special_char_valid: 特殊字符的有效性
        :type special_char_valid: str
        :param x_example: 示例
        :type x_example: str
        """
        
        

        self._dependent_info = None
        self._enabled = None
        self._is_config_dep = None
        self._is_dependent = None
        self._message = None
        self._result = None
        self._special_char = None
        self._special_char_valid = None
        self._x_example = None
        self.discriminator = None

        if dependent_info is not None:
            self.dependent_info = dependent_info
        if enabled is not None:
            self.enabled = enabled
        if is_config_dep is not None:
            self.is_config_dep = is_config_dep
        if is_dependent is not None:
            self.is_dependent = is_dependent
        if message is not None:
            self.message = message
        if result is not None:
            self.result = result
        if special_char is not None:
            self.special_char = special_char
        if special_char_valid is not None:
            self.special_char_valid = special_char_valid
        if x_example is not None:
            self.x_example = x_example

    @property
    def dependent_info(self):
        """Gets the dependent_info of this ValidateRule.

        依赖信息列表

        :return: The dependent_info of this ValidateRule.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ConditionInstance`]
        """
        return self._dependent_info

    @dependent_info.setter
    def dependent_info(self, dependent_info):
        """Sets the dependent_info of this ValidateRule.

        依赖信息列表

        :param dependent_info: The dependent_info of this ValidateRule.
        :type dependent_info: list[:class:`huaweicloudsdkcloudtest.v1.ConditionInstance`]
        """
        self._dependent_info = dependent_info

    @property
    def enabled(self):
        """Gets the enabled of this ValidateRule.

        是否启用的标识符

        :return: The enabled of this ValidateRule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ValidateRule.

        是否启用的标识符

        :param enabled: The enabled of this ValidateRule.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def is_config_dep(self):
        """Gets the is_config_dep of this ValidateRule.

        配置依赖的标识符

        :return: The is_config_dep of this ValidateRule.
        :rtype: bool
        """
        return self._is_config_dep

    @is_config_dep.setter
    def is_config_dep(self, is_config_dep):
        """Sets the is_config_dep of this ValidateRule.

        配置依赖的标识符

        :param is_config_dep: The is_config_dep of this ValidateRule.
        :type is_config_dep: bool
        """
        self._is_config_dep = is_config_dep

    @property
    def is_dependent(self):
        """Gets the is_dependent of this ValidateRule.

        是否依赖的标识符

        :return: The is_dependent of this ValidateRule.
        :rtype: bool
        """
        return self._is_dependent

    @is_dependent.setter
    def is_dependent(self, is_dependent):
        """Sets the is_dependent of this ValidateRule.

        是否依赖的标识符

        :param is_dependent: The is_dependent of this ValidateRule.
        :type is_dependent: bool
        """
        self._is_dependent = is_dependent

    @property
    def message(self):
        """Gets the message of this ValidateRule.

        消息

        :return: The message of this ValidateRule.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidateRule.

        消息

        :param message: The message of this ValidateRule.
        :type message: str
        """
        self._message = message

    @property
    def result(self):
        """Gets the result of this ValidateRule.

        结果

        :return: The result of this ValidateRule.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ValidateRule.

        结果

        :param result: The result of this ValidateRule.
        :type result: str
        """
        self._result = result

    @property
    def special_char(self):
        """Gets the special_char of this ValidateRule.

        特殊字符

        :return: The special_char of this ValidateRule.
        :rtype: str
        """
        return self._special_char

    @special_char.setter
    def special_char(self, special_char):
        """Sets the special_char of this ValidateRule.

        特殊字符

        :param special_char: The special_char of this ValidateRule.
        :type special_char: str
        """
        self._special_char = special_char

    @property
    def special_char_valid(self):
        """Gets the special_char_valid of this ValidateRule.

        特殊字符的有效性

        :return: The special_char_valid of this ValidateRule.
        :rtype: str
        """
        return self._special_char_valid

    @special_char_valid.setter
    def special_char_valid(self, special_char_valid):
        """Sets the special_char_valid of this ValidateRule.

        特殊字符的有效性

        :param special_char_valid: The special_char_valid of this ValidateRule.
        :type special_char_valid: str
        """
        self._special_char_valid = special_char_valid

    @property
    def x_example(self):
        """Gets the x_example of this ValidateRule.

        示例

        :return: The x_example of this ValidateRule.
        :rtype: str
        """
        return self._x_example

    @x_example.setter
    def x_example(self, x_example):
        """Sets the x_example of this ValidateRule.

        示例

        :param x_example: The x_example of this ValidateRule.
        :type x_example: str
        """
        self._x_example = x_example

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
        if not isinstance(other, ValidateRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
