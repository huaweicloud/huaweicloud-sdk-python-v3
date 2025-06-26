# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWebhookPolicyRequestBody:

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
        'targets': 'list[Target]',
        'scope_rules': 'list[ScopeRule]',
        'event_types': 'list[str]',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'targets': 'targets',
        'scope_rules': 'scope_rules',
        'event_types': 'event_types',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, description=None, targets=None, scope_rules=None, event_types=None, enabled=None):
        r"""CreateWebhookPolicyRequestBody

        The model defined in huaweicloud sdk

        :param name: 触发器名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。
        :type name: str
        :param description: 触发器描述
        :type description: str
        :param targets: 触发器目标参数
        :type targets: list[:class:`huaweicloudsdkswr.v2.Target`]
        :param scope_rules: 作用范围规则
        :type scope_rules: list[:class:`huaweicloudsdkswr.v2.ScopeRule`]
        :param event_types: 触发器触发条件，当前支持PUSH_ARTIFACT
        :type event_types: list[str]
        :param enabled: 是否使用
        :type enabled: bool
        """
        
        

        self._name = None
        self._description = None
        self._targets = None
        self._scope_rules = None
        self._event_types = None
        self._enabled = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.targets = targets
        self.scope_rules = scope_rules
        self.event_types = event_types
        self.enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this CreateWebhookPolicyRequestBody.

        触发器名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。

        :return: The name of this CreateWebhookPolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateWebhookPolicyRequestBody.

        触发器名称，由字母、汉字、数字、下划线（_）、中划线 (-)组成，1-256个字符。

        :param name: The name of this CreateWebhookPolicyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateWebhookPolicyRequestBody.

        触发器描述

        :return: The description of this CreateWebhookPolicyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateWebhookPolicyRequestBody.

        触发器描述

        :param description: The description of this CreateWebhookPolicyRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def targets(self):
        r"""Gets the targets of this CreateWebhookPolicyRequestBody.

        触发器目标参数

        :return: The targets of this CreateWebhookPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this CreateWebhookPolicyRequestBody.

        触发器目标参数

        :param targets: The targets of this CreateWebhookPolicyRequestBody.
        :type targets: list[:class:`huaweicloudsdkswr.v2.Target`]
        """
        self._targets = targets

    @property
    def scope_rules(self):
        r"""Gets the scope_rules of this CreateWebhookPolicyRequestBody.

        作用范围规则

        :return: The scope_rules of this CreateWebhookPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdkswr.v2.ScopeRule`]
        """
        return self._scope_rules

    @scope_rules.setter
    def scope_rules(self, scope_rules):
        r"""Sets the scope_rules of this CreateWebhookPolicyRequestBody.

        作用范围规则

        :param scope_rules: The scope_rules of this CreateWebhookPolicyRequestBody.
        :type scope_rules: list[:class:`huaweicloudsdkswr.v2.ScopeRule`]
        """
        self._scope_rules = scope_rules

    @property
    def event_types(self):
        r"""Gets the event_types of this CreateWebhookPolicyRequestBody.

        触发器触发条件，当前支持PUSH_ARTIFACT

        :return: The event_types of this CreateWebhookPolicyRequestBody.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        r"""Sets the event_types of this CreateWebhookPolicyRequestBody.

        触发器触发条件，当前支持PUSH_ARTIFACT

        :param event_types: The event_types of this CreateWebhookPolicyRequestBody.
        :type event_types: list[str]
        """
        self._event_types = event_types

    @property
    def enabled(self):
        r"""Gets the enabled of this CreateWebhookPolicyRequestBody.

        是否使用

        :return: The enabled of this CreateWebhookPolicyRequestBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this CreateWebhookPolicyRequestBody.

        是否使用

        :param enabled: The enabled of this CreateWebhookPolicyRequestBody.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, CreateWebhookPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
