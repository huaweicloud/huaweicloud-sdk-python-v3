# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaskRulesetItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'language': 'str',
        'rule_set_id': 'str',
        'if_use': 'str',
        'status': 'str'
    }

    attribute_map = {
        'language': 'language',
        'rule_set_id': 'rule_set_id',
        'if_use': 'if_use',
        'status': 'status'
    }

    def __init__(self, language=None, rule_set_id=None, if_use=None, status=None):
        """UpdateTaskRulesetItem

        The model defined in huaweicloud sdk

        :param language: 规则集语言
        :type language: str
        :param rule_set_id: 规则集ID,通过调用ListTaskRuleset接口，根据响应参数中的template_id获得
        :type rule_set_id: str
        :param if_use: 任务语言和规则集的关系是否启用，1是启用，0是未启用
        :type if_use: str
        :param status: 新/老数据表示，默认1
        :type status: str
        """
        
        

        self._language = None
        self._rule_set_id = None
        self._if_use = None
        self._status = None
        self.discriminator = None

        self.language = language
        self.rule_set_id = rule_set_id
        self.if_use = if_use
        self.status = status

    @property
    def language(self):
        """Gets the language of this UpdateTaskRulesetItem.

        规则集语言

        :return: The language of this UpdateTaskRulesetItem.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdateTaskRulesetItem.

        规则集语言

        :param language: The language of this UpdateTaskRulesetItem.
        :type language: str
        """
        self._language = language

    @property
    def rule_set_id(self):
        """Gets the rule_set_id of this UpdateTaskRulesetItem.

        规则集ID,通过调用ListTaskRuleset接口，根据响应参数中的template_id获得

        :return: The rule_set_id of this UpdateTaskRulesetItem.
        :rtype: str
        """
        return self._rule_set_id

    @rule_set_id.setter
    def rule_set_id(self, rule_set_id):
        """Sets the rule_set_id of this UpdateTaskRulesetItem.

        规则集ID,通过调用ListTaskRuleset接口，根据响应参数中的template_id获得

        :param rule_set_id: The rule_set_id of this UpdateTaskRulesetItem.
        :type rule_set_id: str
        """
        self._rule_set_id = rule_set_id

    @property
    def if_use(self):
        """Gets the if_use of this UpdateTaskRulesetItem.

        任务语言和规则集的关系是否启用，1是启用，0是未启用

        :return: The if_use of this UpdateTaskRulesetItem.
        :rtype: str
        """
        return self._if_use

    @if_use.setter
    def if_use(self, if_use):
        """Sets the if_use of this UpdateTaskRulesetItem.

        任务语言和规则集的关系是否启用，1是启用，0是未启用

        :param if_use: The if_use of this UpdateTaskRulesetItem.
        :type if_use: str
        """
        self._if_use = if_use

    @property
    def status(self):
        """Gets the status of this UpdateTaskRulesetItem.

        新/老数据表示，默认1

        :return: The status of this UpdateTaskRulesetItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateTaskRulesetItem.

        新/老数据表示，默认1

        :param status: The status of this UpdateTaskRulesetItem.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, UpdateTaskRulesetItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
