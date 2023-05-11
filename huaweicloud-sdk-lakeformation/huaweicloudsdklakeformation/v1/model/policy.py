# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Policy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'allow_exceptions': 'list[PolicyItem]',
        'conditions': 'list[PolicyItemCondition]',
        'create_time': 'datetime',
        'created_by': 'str',
        'data_mask_policy_items': 'list[DataMaskPolicyItem]',
        'deny_exceptions': 'list[PolicyItem]',
        'deny_policy_items': 'list[PolicyItem]',
        'description': 'str',
        'guid': 'str',
        'id': 'int',
        'is_audit_enabled': 'bool',
        'is_default_policy': 'bool',
        'is_deny_all_else': 'bool',
        'is_enabled': 'bool',
        'name': 'str',
        'options': 'object',
        'policy_items': 'list[PolicyItem]',
        'policy_labels': 'list[str]',
        'policy_priority': 'int',
        'policy_type': 'int',
        'resource_signature': 'str',
        'resources': 'dict(str, PolicyResource)',
        'row_filter_policy_items': 'list[RowFilterPolicyItem]',
        'service': 'str',
        'service_type': 'str',
        'update_time': 'datetime',
        'updated_by': 'str',
        'validity_schedules': 'list[ValiditySchedule]',
        'version': 'int',
        'zone_name': 'str'
    }

    attribute_map = {
        'allow_exceptions': 'allow_exceptions',
        'conditions': 'conditions',
        'create_time': 'create_time',
        'created_by': 'created_by',
        'data_mask_policy_items': 'data_mask_policy_items',
        'deny_exceptions': 'deny_exceptions',
        'deny_policy_items': 'deny_policy_items',
        'description': 'description',
        'guid': 'guid',
        'id': 'id',
        'is_audit_enabled': 'is_audit_enabled',
        'is_default_policy': 'is_default_policy',
        'is_deny_all_else': 'is_deny_all_else',
        'is_enabled': 'is_enabled',
        'name': 'name',
        'options': 'options',
        'policy_items': 'policy_items',
        'policy_labels': 'policy_labels',
        'policy_priority': 'policy_priority',
        'policy_type': 'policy_type',
        'resource_signature': 'resource_signature',
        'resources': 'resources',
        'row_filter_policy_items': 'row_filter_policy_items',
        'service': 'service',
        'service_type': 'service_type',
        'update_time': 'update_time',
        'updated_by': 'updated_by',
        'validity_schedules': 'validity_schedules',
        'version': 'version',
        'zone_name': 'zone_name'
    }

    def __init__(self, allow_exceptions=None, conditions=None, create_time=None, created_by=None, data_mask_policy_items=None, deny_exceptions=None, deny_policy_items=None, description=None, guid=None, id=None, is_audit_enabled=None, is_default_policy=None, is_deny_all_else=None, is_enabled=None, name=None, options=None, policy_items=None, policy_labels=None, policy_priority=None, policy_type=None, resource_signature=None, resources=None, row_filter_policy_items=None, service=None, service_type=None, update_time=None, updated_by=None, validity_schedules=None, version=None, zone_name=None):
        """Policy

        The model defined in huaweicloud sdk

        :param allow_exceptions: 排除的允许策略
        :type allow_exceptions: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        :param conditions: 条件属性
        :type conditions: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemCondition`]
        :param create_time: 创建时间
        :type create_time: datetime
        :param created_by: 创建者
        :type created_by: str
        :param data_mask_policy_items: 类掩码策略条目
        :type data_mask_policy_items: list[:class:`huaweicloudsdklakeformation.v1.DataMaskPolicyItem`]
        :param deny_exceptions: 拒绝排除策略
        :type deny_exceptions: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        :param deny_policy_items: 拒绝策略
        :type deny_policy_items: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        :param description: 描述
        :type description: str
        :param guid: 唯一guid
        :type guid: str
        :param id: 主键
        :type id: int
        :param is_audit_enabled: 是否支持审计
        :type is_audit_enabled: bool
        :param is_default_policy: 是否默认策略
        :type is_default_policy: bool
        :param is_deny_all_else: 是否拒绝所有
        :type is_deny_all_else: bool
        :param is_enabled: 是否启动
        :type is_enabled: bool
        :param name: 名
        :type name: str
        :param options: 选项
        :type options: object
        :param policy_items: 策略信息数组
        :type policy_items: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        :param policy_labels: 策略便签
        :type policy_labels: list[str]
        :param policy_priority: 策略优先级
        :type policy_priority: int
        :param policy_type: 策略类型
        :type policy_type: int
        :param resource_signature: 资源签名
        :type resource_signature: str
        :param resources: 资源
        :type resources: dict(str, PolicyResource)
        :param row_filter_policy_items: 行过滤策略条目
        :type row_filter_policy_items: list[:class:`huaweicloudsdklakeformation.v1.RowFilterPolicyItem`]
        :param service: 服务
        :type service: str
        :param service_type: 服务类型
        :type service_type: str
        :param update_time: 更新时间
        :type update_time: datetime
        :param updated_by: 更新者
        :type updated_by: str
        :param validity_schedules: 验证周期
        :type validity_schedules: list[:class:`huaweicloudsdklakeformation.v1.ValiditySchedule`]
        :param version: 版本
        :type version: int
        :param zone_name: 域
        :type zone_name: str
        """
        
        

        self._allow_exceptions = None
        self._conditions = None
        self._create_time = None
        self._created_by = None
        self._data_mask_policy_items = None
        self._deny_exceptions = None
        self._deny_policy_items = None
        self._description = None
        self._guid = None
        self._id = None
        self._is_audit_enabled = None
        self._is_default_policy = None
        self._is_deny_all_else = None
        self._is_enabled = None
        self._name = None
        self._options = None
        self._policy_items = None
        self._policy_labels = None
        self._policy_priority = None
        self._policy_type = None
        self._resource_signature = None
        self._resources = None
        self._row_filter_policy_items = None
        self._service = None
        self._service_type = None
        self._update_time = None
        self._updated_by = None
        self._validity_schedules = None
        self._version = None
        self._zone_name = None
        self.discriminator = None

        if allow_exceptions is not None:
            self.allow_exceptions = allow_exceptions
        if conditions is not None:
            self.conditions = conditions
        if create_time is not None:
            self.create_time = create_time
        if created_by is not None:
            self.created_by = created_by
        if data_mask_policy_items is not None:
            self.data_mask_policy_items = data_mask_policy_items
        if deny_exceptions is not None:
            self.deny_exceptions = deny_exceptions
        if deny_policy_items is not None:
            self.deny_policy_items = deny_policy_items
        if description is not None:
            self.description = description
        if guid is not None:
            self.guid = guid
        if id is not None:
            self.id = id
        if is_audit_enabled is not None:
            self.is_audit_enabled = is_audit_enabled
        if is_default_policy is not None:
            self.is_default_policy = is_default_policy
        if is_deny_all_else is not None:
            self.is_deny_all_else = is_deny_all_else
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if policy_items is not None:
            self.policy_items = policy_items
        if policy_labels is not None:
            self.policy_labels = policy_labels
        if policy_priority is not None:
            self.policy_priority = policy_priority
        if policy_type is not None:
            self.policy_type = policy_type
        if resource_signature is not None:
            self.resource_signature = resource_signature
        if resources is not None:
            self.resources = resources
        if row_filter_policy_items is not None:
            self.row_filter_policy_items = row_filter_policy_items
        if service is not None:
            self.service = service
        if service_type is not None:
            self.service_type = service_type
        if update_time is not None:
            self.update_time = update_time
        if updated_by is not None:
            self.updated_by = updated_by
        if validity_schedules is not None:
            self.validity_schedules = validity_schedules
        if version is not None:
            self.version = version
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def allow_exceptions(self):
        """Gets the allow_exceptions of this Policy.

        排除的允许策略

        :return: The allow_exceptions of this Policy.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        """
        return self._allow_exceptions

    @allow_exceptions.setter
    def allow_exceptions(self, allow_exceptions):
        """Sets the allow_exceptions of this Policy.

        排除的允许策略

        :param allow_exceptions: The allow_exceptions of this Policy.
        :type allow_exceptions: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        """
        self._allow_exceptions = allow_exceptions

    @property
    def conditions(self):
        """Gets the conditions of this Policy.

        条件属性

        :return: The conditions of this Policy.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemCondition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this Policy.

        条件属性

        :param conditions: The conditions of this Policy.
        :type conditions: list[:class:`huaweicloudsdklakeformation.v1.PolicyItemCondition`]
        """
        self._conditions = conditions

    @property
    def create_time(self):
        """Gets the create_time of this Policy.

        创建时间

        :return: The create_time of this Policy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Policy.

        创建时间

        :param create_time: The create_time of this Policy.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def created_by(self):
        """Gets the created_by of this Policy.

        创建者

        :return: The created_by of this Policy.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Policy.

        创建者

        :param created_by: The created_by of this Policy.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def data_mask_policy_items(self):
        """Gets the data_mask_policy_items of this Policy.

        类掩码策略条目

        :return: The data_mask_policy_items of this Policy.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.DataMaskPolicyItem`]
        """
        return self._data_mask_policy_items

    @data_mask_policy_items.setter
    def data_mask_policy_items(self, data_mask_policy_items):
        """Sets the data_mask_policy_items of this Policy.

        类掩码策略条目

        :param data_mask_policy_items: The data_mask_policy_items of this Policy.
        :type data_mask_policy_items: list[:class:`huaweicloudsdklakeformation.v1.DataMaskPolicyItem`]
        """
        self._data_mask_policy_items = data_mask_policy_items

    @property
    def deny_exceptions(self):
        """Gets the deny_exceptions of this Policy.

        拒绝排除策略

        :return: The deny_exceptions of this Policy.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        """
        return self._deny_exceptions

    @deny_exceptions.setter
    def deny_exceptions(self, deny_exceptions):
        """Sets the deny_exceptions of this Policy.

        拒绝排除策略

        :param deny_exceptions: The deny_exceptions of this Policy.
        :type deny_exceptions: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        """
        self._deny_exceptions = deny_exceptions

    @property
    def deny_policy_items(self):
        """Gets the deny_policy_items of this Policy.

        拒绝策略

        :return: The deny_policy_items of this Policy.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        """
        return self._deny_policy_items

    @deny_policy_items.setter
    def deny_policy_items(self, deny_policy_items):
        """Sets the deny_policy_items of this Policy.

        拒绝策略

        :param deny_policy_items: The deny_policy_items of this Policy.
        :type deny_policy_items: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        """
        self._deny_policy_items = deny_policy_items

    @property
    def description(self):
        """Gets the description of this Policy.

        描述

        :return: The description of this Policy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Policy.

        描述

        :param description: The description of this Policy.
        :type description: str
        """
        self._description = description

    @property
    def guid(self):
        """Gets the guid of this Policy.

        唯一guid

        :return: The guid of this Policy.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this Policy.

        唯一guid

        :param guid: The guid of this Policy.
        :type guid: str
        """
        self._guid = guid

    @property
    def id(self):
        """Gets the id of this Policy.

        主键

        :return: The id of this Policy.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Policy.

        主键

        :param id: The id of this Policy.
        :type id: int
        """
        self._id = id

    @property
    def is_audit_enabled(self):
        """Gets the is_audit_enabled of this Policy.

        是否支持审计

        :return: The is_audit_enabled of this Policy.
        :rtype: bool
        """
        return self._is_audit_enabled

    @is_audit_enabled.setter
    def is_audit_enabled(self, is_audit_enabled):
        """Sets the is_audit_enabled of this Policy.

        是否支持审计

        :param is_audit_enabled: The is_audit_enabled of this Policy.
        :type is_audit_enabled: bool
        """
        self._is_audit_enabled = is_audit_enabled

    @property
    def is_default_policy(self):
        """Gets the is_default_policy of this Policy.

        是否默认策略

        :return: The is_default_policy of this Policy.
        :rtype: bool
        """
        return self._is_default_policy

    @is_default_policy.setter
    def is_default_policy(self, is_default_policy):
        """Sets the is_default_policy of this Policy.

        是否默认策略

        :param is_default_policy: The is_default_policy of this Policy.
        :type is_default_policy: bool
        """
        self._is_default_policy = is_default_policy

    @property
    def is_deny_all_else(self):
        """Gets the is_deny_all_else of this Policy.

        是否拒绝所有

        :return: The is_deny_all_else of this Policy.
        :rtype: bool
        """
        return self._is_deny_all_else

    @is_deny_all_else.setter
    def is_deny_all_else(self, is_deny_all_else):
        """Sets the is_deny_all_else of this Policy.

        是否拒绝所有

        :param is_deny_all_else: The is_deny_all_else of this Policy.
        :type is_deny_all_else: bool
        """
        self._is_deny_all_else = is_deny_all_else

    @property
    def is_enabled(self):
        """Gets the is_enabled of this Policy.

        是否启动

        :return: The is_enabled of this Policy.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this Policy.

        是否启动

        :param is_enabled: The is_enabled of this Policy.
        :type is_enabled: bool
        """
        self._is_enabled = is_enabled

    @property
    def name(self):
        """Gets the name of this Policy.

        名

        :return: The name of this Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Policy.

        名

        :param name: The name of this Policy.
        :type name: str
        """
        self._name = name

    @property
    def options(self):
        """Gets the options of this Policy.

        选项

        :return: The options of this Policy.
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Policy.

        选项

        :param options: The options of this Policy.
        :type options: object
        """
        self._options = options

    @property
    def policy_items(self):
        """Gets the policy_items of this Policy.

        策略信息数组

        :return: The policy_items of this Policy.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        """
        return self._policy_items

    @policy_items.setter
    def policy_items(self, policy_items):
        """Sets the policy_items of this Policy.

        策略信息数组

        :param policy_items: The policy_items of this Policy.
        :type policy_items: list[:class:`huaweicloudsdklakeformation.v1.PolicyItem`]
        """
        self._policy_items = policy_items

    @property
    def policy_labels(self):
        """Gets the policy_labels of this Policy.

        策略便签

        :return: The policy_labels of this Policy.
        :rtype: list[str]
        """
        return self._policy_labels

    @policy_labels.setter
    def policy_labels(self, policy_labels):
        """Sets the policy_labels of this Policy.

        策略便签

        :param policy_labels: The policy_labels of this Policy.
        :type policy_labels: list[str]
        """
        self._policy_labels = policy_labels

    @property
    def policy_priority(self):
        """Gets the policy_priority of this Policy.

        策略优先级

        :return: The policy_priority of this Policy.
        :rtype: int
        """
        return self._policy_priority

    @policy_priority.setter
    def policy_priority(self, policy_priority):
        """Sets the policy_priority of this Policy.

        策略优先级

        :param policy_priority: The policy_priority of this Policy.
        :type policy_priority: int
        """
        self._policy_priority = policy_priority

    @property
    def policy_type(self):
        """Gets the policy_type of this Policy.

        策略类型

        :return: The policy_type of this Policy.
        :rtype: int
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this Policy.

        策略类型

        :param policy_type: The policy_type of this Policy.
        :type policy_type: int
        """
        self._policy_type = policy_type

    @property
    def resource_signature(self):
        """Gets the resource_signature of this Policy.

        资源签名

        :return: The resource_signature of this Policy.
        :rtype: str
        """
        return self._resource_signature

    @resource_signature.setter
    def resource_signature(self, resource_signature):
        """Sets the resource_signature of this Policy.

        资源签名

        :param resource_signature: The resource_signature of this Policy.
        :type resource_signature: str
        """
        self._resource_signature = resource_signature

    @property
    def resources(self):
        """Gets the resources of this Policy.

        资源

        :return: The resources of this Policy.
        :rtype: dict(str, PolicyResource)
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Policy.

        资源

        :param resources: The resources of this Policy.
        :type resources: dict(str, PolicyResource)
        """
        self._resources = resources

    @property
    def row_filter_policy_items(self):
        """Gets the row_filter_policy_items of this Policy.

        行过滤策略条目

        :return: The row_filter_policy_items of this Policy.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.RowFilterPolicyItem`]
        """
        return self._row_filter_policy_items

    @row_filter_policy_items.setter
    def row_filter_policy_items(self, row_filter_policy_items):
        """Sets the row_filter_policy_items of this Policy.

        行过滤策略条目

        :param row_filter_policy_items: The row_filter_policy_items of this Policy.
        :type row_filter_policy_items: list[:class:`huaweicloudsdklakeformation.v1.RowFilterPolicyItem`]
        """
        self._row_filter_policy_items = row_filter_policy_items

    @property
    def service(self):
        """Gets the service of this Policy.

        服务

        :return: The service of this Policy.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this Policy.

        服务

        :param service: The service of this Policy.
        :type service: str
        """
        self._service = service

    @property
    def service_type(self):
        """Gets the service_type of this Policy.

        服务类型

        :return: The service_type of this Policy.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this Policy.

        服务类型

        :param service_type: The service_type of this Policy.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def update_time(self):
        """Gets the update_time of this Policy.

        更新时间

        :return: The update_time of this Policy.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Policy.

        更新时间

        :param update_time: The update_time of this Policy.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def updated_by(self):
        """Gets the updated_by of this Policy.

        更新者

        :return: The updated_by of this Policy.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Policy.

        更新者

        :param updated_by: The updated_by of this Policy.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def validity_schedules(self):
        """Gets the validity_schedules of this Policy.

        验证周期

        :return: The validity_schedules of this Policy.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ValiditySchedule`]
        """
        return self._validity_schedules

    @validity_schedules.setter
    def validity_schedules(self, validity_schedules):
        """Sets the validity_schedules of this Policy.

        验证周期

        :param validity_schedules: The validity_schedules of this Policy.
        :type validity_schedules: list[:class:`huaweicloudsdklakeformation.v1.ValiditySchedule`]
        """
        self._validity_schedules = validity_schedules

    @property
    def version(self):
        """Gets the version of this Policy.

        版本

        :return: The version of this Policy.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Policy.

        版本

        :param version: The version of this Policy.
        :type version: int
        """
        self._version = version

    @property
    def zone_name(self):
        """Gets the zone_name of this Policy.

        域

        :return: The zone_name of this Policy.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this Policy.

        域

        :param zone_name: The zone_name of this Policy.
        :type zone_name: str
        """
        self._zone_name = zone_name

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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
