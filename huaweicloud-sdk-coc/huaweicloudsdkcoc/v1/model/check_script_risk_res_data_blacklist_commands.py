# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckScriptRiskResDataBlacklistCommands:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command_name': 'str',
        'command_rule': 'str',
        'example': 'str',
        'description_en': 'str',
        'description_zh': 'str'
    }

    attribute_map = {
        'command_name': 'command_name',
        'command_rule': 'command_rule',
        'example': 'example',
        'description_en': 'description_en',
        'description_zh': 'description_zh'
    }

    def __init__(self, command_name=None, command_rule=None, example=None, description_en=None, description_zh=None):
        r"""CheckScriptRiskResDataBlacklistCommands

        The model defined in huaweicloud sdk

        :param command_name: 命令。
        :type command_name: str
        :param command_rule: 匹配规则。
        :type command_rule: str
        :param example: 实例。
        :type example: str
        :param description_en: 黑名单命令中文描述。
        :type description_en: str
        :param description_zh: 黑名单命令英文描述。
        :type description_zh: str
        """
        
        

        self._command_name = None
        self._command_rule = None
        self._example = None
        self._description_en = None
        self._description_zh = None
        self.discriminator = None

        if command_name is not None:
            self.command_name = command_name
        if command_rule is not None:
            self.command_rule = command_rule
        if example is not None:
            self.example = example
        if description_en is not None:
            self.description_en = description_en
        if description_zh is not None:
            self.description_zh = description_zh

    @property
    def command_name(self):
        r"""Gets the command_name of this CheckScriptRiskResDataBlacklistCommands.

        命令。

        :return: The command_name of this CheckScriptRiskResDataBlacklistCommands.
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        r"""Sets the command_name of this CheckScriptRiskResDataBlacklistCommands.

        命令。

        :param command_name: The command_name of this CheckScriptRiskResDataBlacklistCommands.
        :type command_name: str
        """
        self._command_name = command_name

    @property
    def command_rule(self):
        r"""Gets the command_rule of this CheckScriptRiskResDataBlacklistCommands.

        匹配规则。

        :return: The command_rule of this CheckScriptRiskResDataBlacklistCommands.
        :rtype: str
        """
        return self._command_rule

    @command_rule.setter
    def command_rule(self, command_rule):
        r"""Sets the command_rule of this CheckScriptRiskResDataBlacklistCommands.

        匹配规则。

        :param command_rule: The command_rule of this CheckScriptRiskResDataBlacklistCommands.
        :type command_rule: str
        """
        self._command_rule = command_rule

    @property
    def example(self):
        r"""Gets the example of this CheckScriptRiskResDataBlacklistCommands.

        实例。

        :return: The example of this CheckScriptRiskResDataBlacklistCommands.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        r"""Sets the example of this CheckScriptRiskResDataBlacklistCommands.

        实例。

        :param example: The example of this CheckScriptRiskResDataBlacklistCommands.
        :type example: str
        """
        self._example = example

    @property
    def description_en(self):
        r"""Gets the description_en of this CheckScriptRiskResDataBlacklistCommands.

        黑名单命令中文描述。

        :return: The description_en of this CheckScriptRiskResDataBlacklistCommands.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this CheckScriptRiskResDataBlacklistCommands.

        黑名单命令中文描述。

        :param description_en: The description_en of this CheckScriptRiskResDataBlacklistCommands.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def description_zh(self):
        r"""Gets the description_zh of this CheckScriptRiskResDataBlacklistCommands.

        黑名单命令英文描述。

        :return: The description_zh of this CheckScriptRiskResDataBlacklistCommands.
        :rtype: str
        """
        return self._description_zh

    @description_zh.setter
    def description_zh(self, description_zh):
        r"""Sets the description_zh of this CheckScriptRiskResDataBlacklistCommands.

        黑名单命令英文描述。

        :param description_zh: The description_zh of this CheckScriptRiskResDataBlacklistCommands.
        :type description_zh: str
        """
        self._description_zh = description_zh

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
        if not isinstance(other, CheckScriptRiskResDataBlacklistCommands):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
