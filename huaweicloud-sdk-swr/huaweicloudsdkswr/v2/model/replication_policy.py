# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplicationPolicy:

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
        'src_registry': 'ReplicationRegistry',
        'dest_registry': 'ReplicationRegistry',
        'dest_namespace': 'str',
        'filters': 'list[Filter]',
        'repo_scope_mode': 'str',
        'trigger': 'TriggerConfig',
        'override': 'bool',
        'enabled': 'bool',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'src_registry': 'src_registry',
        'dest_registry': 'dest_registry',
        'dest_namespace': 'dest_namespace',
        'filters': 'filters',
        'repo_scope_mode': 'repo_scope_mode',
        'trigger': 'trigger',
        'override': 'override',
        'enabled': 'enabled',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, name=None, description=None, src_registry=None, dest_registry=None, dest_namespace=None, filters=None, repo_scope_mode=None, trigger=None, override=None, enabled=None, created_at=None, updated_at=None):
        r"""ReplicationPolicy

        The model defined in huaweicloud sdk

        :param id: 策略ID
        :type id: int
        :param name: 策略名称
        :type name: str
        :param description: 策略描述描述
        :type description: str
        :param src_registry: 
        :type src_registry: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        :param dest_registry: 
        :type dest_registry: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        :param dest_namespace: 目标命名空间名，默认为空值
        :type dest_namespace: str
        :param filters: 源资源过滤器
        :type filters: list[:class:`huaweicloudsdkswr.v2.Filter`]
        :param repo_scope_mode: repo的范围模式
        :type repo_scope_mode: str
        :param trigger: 
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        :param override: 是否覆盖
        :type override: bool
        :param enabled: 是否使用
        :type enabled: bool
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._src_registry = None
        self._dest_registry = None
        self._dest_namespace = None
        self._filters = None
        self._repo_scope_mode = None
        self._trigger = None
        self._override = None
        self._enabled = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if src_registry is not None:
            self.src_registry = src_registry
        if dest_registry is not None:
            self.dest_registry = dest_registry
        if dest_namespace is not None:
            self.dest_namespace = dest_namespace
        if filters is not None:
            self.filters = filters
        if repo_scope_mode is not None:
            self.repo_scope_mode = repo_scope_mode
        if trigger is not None:
            self.trigger = trigger
        if override is not None:
            self.override = override
        if enabled is not None:
            self.enabled = enabled
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ReplicationPolicy.

        策略ID

        :return: The id of this ReplicationPolicy.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ReplicationPolicy.

        策略ID

        :param id: The id of this ReplicationPolicy.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ReplicationPolicy.

        策略名称

        :return: The name of this ReplicationPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ReplicationPolicy.

        策略名称

        :param name: The name of this ReplicationPolicy.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ReplicationPolicy.

        策略描述描述

        :return: The description of this ReplicationPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ReplicationPolicy.

        策略描述描述

        :param description: The description of this ReplicationPolicy.
        :type description: str
        """
        self._description = description

    @property
    def src_registry(self):
        r"""Gets the src_registry of this ReplicationPolicy.

        :return: The src_registry of this ReplicationPolicy.
        :rtype: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        """
        return self._src_registry

    @src_registry.setter
    def src_registry(self, src_registry):
        r"""Sets the src_registry of this ReplicationPolicy.

        :param src_registry: The src_registry of this ReplicationPolicy.
        :type src_registry: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        """
        self._src_registry = src_registry

    @property
    def dest_registry(self):
        r"""Gets the dest_registry of this ReplicationPolicy.

        :return: The dest_registry of this ReplicationPolicy.
        :rtype: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        """
        return self._dest_registry

    @dest_registry.setter
    def dest_registry(self, dest_registry):
        r"""Sets the dest_registry of this ReplicationPolicy.

        :param dest_registry: The dest_registry of this ReplicationPolicy.
        :type dest_registry: :class:`huaweicloudsdkswr.v2.ReplicationRegistry`
        """
        self._dest_registry = dest_registry

    @property
    def dest_namespace(self):
        r"""Gets the dest_namespace of this ReplicationPolicy.

        目标命名空间名，默认为空值

        :return: The dest_namespace of this ReplicationPolicy.
        :rtype: str
        """
        return self._dest_namespace

    @dest_namespace.setter
    def dest_namespace(self, dest_namespace):
        r"""Sets the dest_namespace of this ReplicationPolicy.

        目标命名空间名，默认为空值

        :param dest_namespace: The dest_namespace of this ReplicationPolicy.
        :type dest_namespace: str
        """
        self._dest_namespace = dest_namespace

    @property
    def filters(self):
        r"""Gets the filters of this ReplicationPolicy.

        源资源过滤器

        :return: The filters of this ReplicationPolicy.
        :rtype: list[:class:`huaweicloudsdkswr.v2.Filter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ReplicationPolicy.

        源资源过滤器

        :param filters: The filters of this ReplicationPolicy.
        :type filters: list[:class:`huaweicloudsdkswr.v2.Filter`]
        """
        self._filters = filters

    @property
    def repo_scope_mode(self):
        r"""Gets the repo_scope_mode of this ReplicationPolicy.

        repo的范围模式

        :return: The repo_scope_mode of this ReplicationPolicy.
        :rtype: str
        """
        return self._repo_scope_mode

    @repo_scope_mode.setter
    def repo_scope_mode(self, repo_scope_mode):
        r"""Sets the repo_scope_mode of this ReplicationPolicy.

        repo的范围模式

        :param repo_scope_mode: The repo_scope_mode of this ReplicationPolicy.
        :type repo_scope_mode: str
        """
        self._repo_scope_mode = repo_scope_mode

    @property
    def trigger(self):
        r"""Gets the trigger of this ReplicationPolicy.

        :return: The trigger of this ReplicationPolicy.
        :rtype: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        r"""Sets the trigger of this ReplicationPolicy.

        :param trigger: The trigger of this ReplicationPolicy.
        :type trigger: :class:`huaweicloudsdkswr.v2.TriggerConfig`
        """
        self._trigger = trigger

    @property
    def override(self):
        r"""Gets the override of this ReplicationPolicy.

        是否覆盖

        :return: The override of this ReplicationPolicy.
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        r"""Sets the override of this ReplicationPolicy.

        是否覆盖

        :param override: The override of this ReplicationPolicy.
        :type override: bool
        """
        self._override = override

    @property
    def enabled(self):
        r"""Gets the enabled of this ReplicationPolicy.

        是否使用

        :return: The enabled of this ReplicationPolicy.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this ReplicationPolicy.

        是否使用

        :param enabled: The enabled of this ReplicationPolicy.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def created_at(self):
        r"""Gets the created_at of this ReplicationPolicy.

        创建时间

        :return: The created_at of this ReplicationPolicy.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ReplicationPolicy.

        创建时间

        :param created_at: The created_at of this ReplicationPolicy.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ReplicationPolicy.

        更新时间

        :return: The updated_at of this ReplicationPolicy.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ReplicationPolicy.

        更新时间

        :param updated_at: The updated_at of this ReplicationPolicy.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ReplicationPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
