# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebhookPolicyDetail:

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
        'name': 'str',
        'description': 'str',
        'targets': 'list[Target]',
        'event_types': 'list[str]',
        'enabled': 'bool',
        'namespace_id': 'int',
        'namespace_name': 'str',
        'creator': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'scope_rules': 'list[ScopeRule]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'targets': 'targets',
        'event_types': 'event_types',
        'enabled': 'enabled',
        'namespace_id': 'namespace_id',
        'namespace_name': 'namespace_name',
        'creator': 'creator',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'scope_rules': 'scope_rules'
    }

    def __init__(self, id=None, name=None, description=None, targets=None, event_types=None, enabled=None, namespace_id=None, namespace_name=None, creator=None, created_at=None, updated_at=None, scope_rules=None):
        r"""WebhookPolicyDetail

        The model defined in huaweicloud sdk

        :param id: 触发器ID
        :type id: int
        :param name: 触发器策略名称
        :type name: str
        :param description: 触发器策略描述
        :type description: str
        :param targets: 触发目标
        :type targets: list[:class:`huaweicloudsdkswr.v2.Target`]
        :param event_types: 事件类型
        :type event_types: list[str]
        :param enabled: 是否使用，可选true或false
        :type enabled: bool
        :param namespace_id: 命名空间ID
        :type namespace_id: int
        :param namespace_name: 命名空间名
        :type namespace_name: str
        :param creator: 创建者
        :type creator: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param scope_rules: 触发作用范围规则
        :type scope_rules: list[:class:`huaweicloudsdkswr.v2.ScopeRule`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._targets = None
        self._event_types = None
        self._enabled = None
        self._namespace_id = None
        self._namespace_name = None
        self._creator = None
        self._created_at = None
        self._updated_at = None
        self._scope_rules = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if targets is not None:
            self.targets = targets
        if event_types is not None:
            self.event_types = event_types
        if enabled is not None:
            self.enabled = enabled
        if namespace_id is not None:
            self.namespace_id = namespace_id
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if creator is not None:
            self.creator = creator
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if scope_rules is not None:
            self.scope_rules = scope_rules

    @property
    def id(self):
        r"""Gets the id of this WebhookPolicyDetail.

        触发器ID

        :return: The id of this WebhookPolicyDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WebhookPolicyDetail.

        触发器ID

        :param id: The id of this WebhookPolicyDetail.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this WebhookPolicyDetail.

        触发器策略名称

        :return: The name of this WebhookPolicyDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WebhookPolicyDetail.

        触发器策略名称

        :param name: The name of this WebhookPolicyDetail.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this WebhookPolicyDetail.

        触发器策略描述

        :return: The description of this WebhookPolicyDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WebhookPolicyDetail.

        触发器策略描述

        :param description: The description of this WebhookPolicyDetail.
        :type description: str
        """
        self._description = description

    @property
    def targets(self):
        r"""Gets the targets of this WebhookPolicyDetail.

        触发目标

        :return: The targets of this WebhookPolicyDetail.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this WebhookPolicyDetail.

        触发目标

        :param targets: The targets of this WebhookPolicyDetail.
        :type targets: list[:class:`huaweicloudsdkswr.v2.Target`]
        """
        self._targets = targets

    @property
    def event_types(self):
        r"""Gets the event_types of this WebhookPolicyDetail.

        事件类型

        :return: The event_types of this WebhookPolicyDetail.
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        r"""Sets the event_types of this WebhookPolicyDetail.

        事件类型

        :param event_types: The event_types of this WebhookPolicyDetail.
        :type event_types: list[str]
        """
        self._event_types = event_types

    @property
    def enabled(self):
        r"""Gets the enabled of this WebhookPolicyDetail.

        是否使用，可选true或false

        :return: The enabled of this WebhookPolicyDetail.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this WebhookPolicyDetail.

        是否使用，可选true或false

        :param enabled: The enabled of this WebhookPolicyDetail.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def namespace_id(self):
        r"""Gets the namespace_id of this WebhookPolicyDetail.

        命名空间ID

        :return: The namespace_id of this WebhookPolicyDetail.
        :rtype: int
        """
        return self._namespace_id

    @namespace_id.setter
    def namespace_id(self, namespace_id):
        r"""Sets the namespace_id of this WebhookPolicyDetail.

        命名空间ID

        :param namespace_id: The namespace_id of this WebhookPolicyDetail.
        :type namespace_id: int
        """
        self._namespace_id = namespace_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this WebhookPolicyDetail.

        命名空间名

        :return: The namespace_name of this WebhookPolicyDetail.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this WebhookPolicyDetail.

        命名空间名

        :param namespace_name: The namespace_name of this WebhookPolicyDetail.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def creator(self):
        r"""Gets the creator of this WebhookPolicyDetail.

        创建者

        :return: The creator of this WebhookPolicyDetail.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this WebhookPolicyDetail.

        创建者

        :param creator: The creator of this WebhookPolicyDetail.
        :type creator: str
        """
        self._creator = creator

    @property
    def created_at(self):
        r"""Gets the created_at of this WebhookPolicyDetail.

        创建时间

        :return: The created_at of this WebhookPolicyDetail.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this WebhookPolicyDetail.

        创建时间

        :param created_at: The created_at of this WebhookPolicyDetail.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this WebhookPolicyDetail.

        更新时间

        :return: The updated_at of this WebhookPolicyDetail.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this WebhookPolicyDetail.

        更新时间

        :param updated_at: The updated_at of this WebhookPolicyDetail.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def scope_rules(self):
        r"""Gets the scope_rules of this WebhookPolicyDetail.

        触发作用范围规则

        :return: The scope_rules of this WebhookPolicyDetail.
        :rtype: list[:class:`huaweicloudsdkswr.v2.ScopeRule`]
        """
        return self._scope_rules

    @scope_rules.setter
    def scope_rules(self, scope_rules):
        r"""Sets the scope_rules of this WebhookPolicyDetail.

        触发作用范围规则

        :param scope_rules: The scope_rules of this WebhookPolicyDetail.
        :type scope_rules: list[:class:`huaweicloudsdkswr.v2.ScopeRule`]
        """
        self._scope_rules = scope_rules

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
        if not isinstance(other, WebhookPolicyDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
