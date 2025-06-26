# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImmutableRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'namespace_id': 'int',
        'namespace_name': 'str',
        'priority': 'int',
        'disabled': 'bool',
        'action': 'str',
        'template': 'str',
        'tag_selectors': 'list[RuleSelector]',
        'scope_selectors': 'dict(str, list[RuleSelector])'
    }

    attribute_map = {
        'id': 'id',
        'namespace_id': 'namespace_id',
        'namespace_name': 'namespace_name',
        'priority': 'priority',
        'disabled': 'disabled',
        'action': 'action',
        'template': 'template',
        'tag_selectors': 'tag_selectors',
        'scope_selectors': 'scope_selectors'
    }

    def __init__(self, id=None, namespace_id=None, namespace_name=None, priority=None, disabled=None, action=None, template=None, tag_selectors=None, scope_selectors=None):
        r"""ImmutableRule

        The model defined in huaweicloud sdk

        :param id: 不可变规则ID
        :type id: int
        :param namespace_id: 
        :type namespace_id: int
        :param namespace_name: 
        :type namespace_name: str
        :param priority: 
        :type priority: int
        :param disabled: 不可变规则是否生效
        :type disabled: bool
        :param action: 预留字段，仅支持填immutable
        :type action: str
        :param template: 预留字段，仅支持填immutable_template
        :type template: str
        :param tag_selectors: 制品版本选择器，目前只支持长度为1
        :type tag_selectors: list[:class:`huaweicloudsdkswr.v2.RuleSelector`]
        :param scope_selectors: 制品仓库选择器，目前只支持repository且长度为1
        :type scope_selectors: dict(str, list[RuleSelector])
        """
        
        

        self._id = None
        self._namespace_id = None
        self._namespace_name = None
        self._priority = None
        self._disabled = None
        self._action = None
        self._template = None
        self._tag_selectors = None
        self._scope_selectors = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if priority is not None:
            self.priority = priority
        if disabled is not None:
            self.disabled = disabled
        if action is not None:
            self.action = action
        if template is not None:
            self.template = template
        if tag_selectors is not None:
            self.tag_selectors = tag_selectors
        if scope_selectors is not None:
            self.scope_selectors = scope_selectors

    @property
    def id(self):
        r"""Gets the id of this ImmutableRule.

        不可变规则ID

        :return: The id of this ImmutableRule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ImmutableRule.

        不可变规则ID

        :param id: The id of this ImmutableRule.
        :type id: int
        """
        self._id = id

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this ImmutableRule.

        :return: The namespace_id of this ImmutableRule.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this ImmutableRule.

        :param namespace_id: The namespace_id of this ImmutableRule.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ImmutableRule.

        :return: The namespace_name of this ImmutableRule.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ImmutableRule.

        :param namespace_name: The namespace_name of this ImmutableRule.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def priority(self):
        r"""Gets the priority of this ImmutableRule.

        :return: The priority of this ImmutableRule.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ImmutableRule.

        :param priority: The priority of this ImmutableRule.
        :type priority: int
        """
        self._priority = priority

    @property
    def disabled(self):
        r"""Gets the disabled of this ImmutableRule.

        不可变规则是否生效

        :return: The disabled of this ImmutableRule.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this ImmutableRule.

        不可变规则是否生效

        :param disabled: The disabled of this ImmutableRule.
        :type disabled: bool
        """
        self._disabled = disabled

    @property
    def action(self):
        r"""Gets the action of this ImmutableRule.

        预留字段，仅支持填immutable

        :return: The action of this ImmutableRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ImmutableRule.

        预留字段，仅支持填immutable

        :param action: The action of this ImmutableRule.
        :type action: str
        """
        self._action = action

    @property
    def template(self):
        r"""Gets the template of this ImmutableRule.

        预留字段，仅支持填immutable_template

        :return: The template of this ImmutableRule.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this ImmutableRule.

        预留字段，仅支持填immutable_template

        :param template: The template of this ImmutableRule.
        :type template: str
        """
        self._template = template

    @property
    def tag_selectors(self):
        r"""Gets the tag_selectors of this ImmutableRule.

        制品版本选择器，目前只支持长度为1

        :return: The tag_selectors of this ImmutableRule.
        :rtype: list[:class:`huaweicloudsdkswr.v2.RuleSelector`]
        """
        return self._tag_selectors

    @tag_selectors.setter
    def tag_selectors(self, tag_selectors):
        r"""Sets the tag_selectors of this ImmutableRule.

        制品版本选择器，目前只支持长度为1

        :param tag_selectors: The tag_selectors of this ImmutableRule.
        :type tag_selectors: list[:class:`huaweicloudsdkswr.v2.RuleSelector`]
        """
        self._tag_selectors = tag_selectors

    @property
    def scope_selectors(self):
        r"""Gets the scope_selectors of this ImmutableRule.

        制品仓库选择器，目前只支持repository且长度为1

        :return: The scope_selectors of this ImmutableRule.
        :rtype: dict(str, list[RuleSelector])
        """
        return self._scope_selectors

    @scope_selectors.setter
    def scope_selectors(self, scope_selectors):
        r"""Sets the scope_selectors of this ImmutableRule.

        制品仓库选择器，目前只支持repository且长度为1

        :param scope_selectors: The scope_selectors of this ImmutableRule.
        :type scope_selectors: dict(str, list[RuleSelector])
        """
        self._scope_selectors = scope_selectors

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
        if not isinstance(other, ImmutableRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
