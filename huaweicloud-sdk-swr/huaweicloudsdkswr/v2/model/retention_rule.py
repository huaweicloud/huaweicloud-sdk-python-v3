# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RetentionRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'priority': 'int',
        'disabled': 'bool',
        'action': 'str',
        'template': 'str',
        'params': 'dict(str, object)',
        'tag_selectors': 'list[RetentionSelector]',
        'scope_selectors': 'dict(str, list[RetentionSelector])',
        'repo_scope_mode': 'str'
    }

    attribute_map = {
        'priority': 'priority',
        'disabled': 'disabled',
        'action': 'action',
        'template': 'template',
        'params': 'params',
        'tag_selectors': 'tag_selectors',
        'scope_selectors': 'scope_selectors',
        'repo_scope_mode': 'repo_scope_mode'
    }

    def __init__(self, priority=None, disabled=None, action=None, template=None, params=None, tag_selectors=None, scope_selectors=None, repo_scope_mode=None):
        r"""RetentionRule

        The model defined in huaweicloud sdk

        :param priority: 优先级，预留字段，默认为0
        :type priority: int
        :param disabled: 是否关闭此条规则
        :type disabled: bool
        :param action: 预留字段，目前只支持retain
        :type action: str
        :param template: 规则模板类型，值为：latestPulledN，latestPushedK，nDaysSinceLastPush，nDaysSinceLastPull
        :type template: str
        :param params: 保留方式的参数，配套template使用，可参考请求示例
        :type params: dict(str, object)
        :param tag_selectors: 制品版本选择器，目前只支持长度为1
        :type tag_selectors: list[:class:`huaweicloudsdkswr.v2.RetentionSelector`]
        :param scope_selectors: 制品仓库选择器，目前只支持repository且长度为1
        :type scope_selectors: dict(str, list[RetentionSelector])
        :param repo_scope_mode: repo选择模式，前端使用，可选regular、selection
        :type repo_scope_mode: str
        """
        
        

        self._priority = None
        self._disabled = None
        self._action = None
        self._template = None
        self._params = None
        self._tag_selectors = None
        self._scope_selectors = None
        self._repo_scope_mode = None
        self.discriminator = None

        self.priority = priority
        if disabled is not None:
            self.disabled = disabled
        self.action = action
        self.template = template
        self.params = params
        self.tag_selectors = tag_selectors
        self.scope_selectors = scope_selectors
        self.repo_scope_mode = repo_scope_mode

    @property
    def priority(self):
        r"""Gets the priority of this RetentionRule.

        优先级，预留字段，默认为0

        :return: The priority of this RetentionRule.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this RetentionRule.

        优先级，预留字段，默认为0

        :param priority: The priority of this RetentionRule.
        :type priority: int
        """
        self._priority = priority

    @property
    def disabled(self):
        r"""Gets the disabled of this RetentionRule.

        是否关闭此条规则

        :return: The disabled of this RetentionRule.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this RetentionRule.

        是否关闭此条规则

        :param disabled: The disabled of this RetentionRule.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def action(self):
        r"""Gets the action of this RetentionRule.

        预留字段，目前只支持retain

        :return: The action of this RetentionRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this RetentionRule.

        预留字段，目前只支持retain

        :param action: The action of this RetentionRule.
        :type action: str
        """
        self._action = action

    @property
    def template(self):
        r"""Gets the template of this RetentionRule.

        规则模板类型，值为：latestPulledN，latestPushedK，nDaysSinceLastPush，nDaysSinceLastPull

        :return: The template of this RetentionRule.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this RetentionRule.

        规则模板类型，值为：latestPulledN，latestPushedK，nDaysSinceLastPush，nDaysSinceLastPull

        :param template: The template of this RetentionRule.
        :type template: str
        """
        self._template = template

    @property
    def params(self):
        r"""Gets the params of this RetentionRule.

        保留方式的参数，配套template使用，可参考请求示例

        :return: The params of this RetentionRule.
        :rtype: dict(str, object)
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this RetentionRule.

        保留方式的参数，配套template使用，可参考请求示例

        :param params: The params of this RetentionRule.
        :type params: dict(str, object)
        """
        self._params = params

    @property
    def tag_selectors(self):
        r"""Gets the tag_selectors of this RetentionRule.

        制品版本选择器，目前只支持长度为1

        :return: The tag_selectors of this RetentionRule.
        :rtype: list[:class:`huaweicloudsdkswr.v2.RetentionSelector`]
        """
        return self._tag_selectors

    @tag_selectors.setter
    def tag_selectors(self, tag_selectors):
        r"""Sets the tag_selectors of this RetentionRule.

        制品版本选择器，目前只支持长度为1

        :param tag_selectors: The tag_selectors of this RetentionRule.
        :type tag_selectors: list[:class:`huaweicloudsdkswr.v2.RetentionSelector`]
        """
        self._tag_selectors = tag_selectors

    @property
    def scope_selectors(self):
        r"""Gets the scope_selectors of this RetentionRule.

        制品仓库选择器，目前只支持repository且长度为1

        :return: The scope_selectors of this RetentionRule.
        :rtype: dict(str, list[RetentionSelector])
        """
        return self._scope_selectors

    @scope_selectors.setter
    def scope_selectors(self, scope_selectors):
        r"""Sets the scope_selectors of this RetentionRule.

        制品仓库选择器，目前只支持repository且长度为1

        :param scope_selectors: The scope_selectors of this RetentionRule.
        :type scope_selectors: dict(str, list[RetentionSelector])
        """
        self._scope_selectors = scope_selectors

    @property
    def repo_scope_mode(self):
        r"""Gets the repo_scope_mode of this RetentionRule.

        repo选择模式，前端使用，可选regular、selection

        :return: The repo_scope_mode of this RetentionRule.
        :rtype: str
        """
        return self._repo_scope_mode

    @repo_scope_mode.setter
    def repo_scope_mode(self, repo_scope_mode):
        r"""Sets the repo_scope_mode of this RetentionRule.

        repo选择模式，前端使用，可选regular、selection

        :param repo_scope_mode: The repo_scope_mode of this RetentionRule.
        :type repo_scope_mode: str
        """
        self._repo_scope_mode = repo_scope_mode

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
        if not isinstance(other, RetentionRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
