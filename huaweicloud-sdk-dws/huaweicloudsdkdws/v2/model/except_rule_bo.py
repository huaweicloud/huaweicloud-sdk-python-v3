# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExceptRuleBo:

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
        'action': 'str',
        'queues': 'list[str]',
        'except_rules': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'action': 'action',
        'queues': 'queues',
        'except_rules': 'except_rules'
    }

    def __init__(self, name=None, action=None, queues=None, except_rules=None):
        r"""ExceptRuleBo

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 规则名称。 **取值范围**： 不涉及。
        :type name: str
        :param action: **参数解释**： 触发异常规则操作。 **取值范围**： 不涉及。
        :type action: str
        :param queues: **参数解释**： 异常规则绑定的资源池名称列表。 **取值范围**： 不涉及。
        :type queues: list[str]
        :param except_rules: **参数解释**： 异常规则配置项。 **取值范围**： 不涉及。
        :type except_rules: dict(str, str)
        """
        
        

        self._name = None
        self._action = None
        self._queues = None
        self._except_rules = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if queues is not None:
            self.queues = queues
        if except_rules is not None:
            self.except_rules = except_rules

    @property
    def name(self):
        r"""Gets the name of this ExceptRuleBo.

        **参数解释**： 规则名称。 **取值范围**： 不涉及。

        :return: The name of this ExceptRuleBo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExceptRuleBo.

        **参数解释**： 规则名称。 **取值范围**： 不涉及。

        :param name: The name of this ExceptRuleBo.
        :type name: str
        """
        self._name = name

    @property
    def action(self):
        r"""Gets the action of this ExceptRuleBo.

        **参数解释**： 触发异常规则操作。 **取值范围**： 不涉及。

        :return: The action of this ExceptRuleBo.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ExceptRuleBo.

        **参数解释**： 触发异常规则操作。 **取值范围**： 不涉及。

        :param action: The action of this ExceptRuleBo.
        :type action: str
        """
        self._action = action

    @property
    def queues(self):
        r"""Gets the queues of this ExceptRuleBo.

        **参数解释**： 异常规则绑定的资源池名称列表。 **取值范围**： 不涉及。

        :return: The queues of this ExceptRuleBo.
        :rtype: list[str]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        r"""Sets the queues of this ExceptRuleBo.

        **参数解释**： 异常规则绑定的资源池名称列表。 **取值范围**： 不涉及。

        :param queues: The queues of this ExceptRuleBo.
        :type queues: list[str]
        """
        self._queues = queues

    @property
    def except_rules(self):
        r"""Gets the except_rules of this ExceptRuleBo.

        **参数解释**： 异常规则配置项。 **取值范围**： 不涉及。

        :return: The except_rules of this ExceptRuleBo.
        :rtype: dict(str, str)
        """
        return self._except_rules

    @except_rules.setter
    def except_rules(self, except_rules):
        r"""Sets the except_rules of this ExceptRuleBo.

        **参数解释**： 异常规则配置项。 **取值范围**： 不涉及。

        :param except_rules: The except_rules of this ExceptRuleBo.
        :type except_rules: dict(str, str)
        """
        self._except_rules = except_rules

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
        if not isinstance(other, ExceptRuleBo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
