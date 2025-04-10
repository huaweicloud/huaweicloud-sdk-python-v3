# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultCreate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_policy_id': 'str',
        'billing': 'BillingCreate',
        'description': 'str',
        'name': 'str',
        'resources': 'list[ResourceCreate]',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'auto_bind': 'bool',
        'bind_rules': 'VaultBindRules',
        'auto_expand': 'bool',
        'threshold': 'int',
        'smn_notify': 'bool',
        'backup_name_prefix': 'str',
        'demand_billing': 'bool',
        'sys_lock_source_service': 'str',
        'locked': 'bool'
    }

    attribute_map = {
        'backup_policy_id': 'backup_policy_id',
        'billing': 'billing',
        'description': 'description',
        'name': 'name',
        'resources': 'resources',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'auto_bind': 'auto_bind',
        'bind_rules': 'bind_rules',
        'auto_expand': 'auto_expand',
        'threshold': 'threshold',
        'smn_notify': 'smn_notify',
        'backup_name_prefix': 'backup_name_prefix',
        'demand_billing': 'demand_billing',
        'sys_lock_source_service': 'sys_lock_source_service',
        'locked': 'locked'
    }

    def __init__(self, backup_policy_id=None, billing=None, description=None, name=None, resources=None, tags=None, enterprise_project_id=None, auto_bind=None, bind_rules=None, auto_expand=None, threshold=None, smn_notify=None, backup_name_prefix=None, demand_billing=None, sys_lock_source_service=None, locked=None):
        r"""VaultCreate

        The model defined in huaweicloud sdk

        :param backup_policy_id: 备份策略ID，不设置时为null，不自动备份。
        :type backup_policy_id: str
        :param billing: 
        :type billing: :class:`huaweicloudsdkcbr.v1.BillingCreate`
        :param description: 描述
        :type description: str
        :param name: 存储库名称
        :type name: str
        :param resources: 绑定的备份资源，未在创建时绑定资源填[]
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        :param tags: 标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        :param enterprise_project_id: 企业项目ID，默认为‘0’。
        :type enterprise_project_id: str
        :param auto_bind: 是否支持自动挂载。
        :type auto_bind: bool
        :param bind_rules: 
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        :param auto_expand: [是否开启存储库自动扩容能力（只支持按需存储库）。](tag:hws,hws_hk) [是否开启存储库自动扩容能力。](tag:dt,ocb,tlf,sbc,fcs_vm,ctc,g42,tm,cmcc,hcso_dt)
        :type auto_expand: bool
        :param threshold: 存储库容量阈值，已用容量占总容量达到此百分比，将根据 smn_notify 参数设置选择是否发送相关通知。 默认值为：80 最大值：100 最小值：1
        :type threshold: int
        :param smn_notify: 存储库smn消息通知开关。 默认值为 true。
        :type smn_notify: bool
        :param backup_name_prefix: 备份名称前缀，设置后该存储库自动备份产生的备份副本都将携带该备份名称前缀
        :type backup_name_prefix: str
        :param demand_billing: 存储库使用是否允许超出容量，只有创建包周期存储库时才允许该值为 true
        :type demand_billing: bool
        :param sys_lock_source_service: 用于标识SMB服务，您可以设置为SMB或者空
        :type sys_lock_source_service: str
        :param locked: 用于标识该存储库是否已锁定
        :type locked: bool
        """
        
        

        self._backup_policy_id = None
        self._billing = None
        self._description = None
        self._name = None
        self._resources = None
        self._tags = None
        self._enterprise_project_id = None
        self._auto_bind = None
        self._bind_rules = None
        self._auto_expand = None
        self._threshold = None
        self._smn_notify = None
        self._backup_name_prefix = None
        self._demand_billing = None
        self._sys_lock_source_service = None
        self._locked = None
        self.discriminator = None

        if backup_policy_id is not None:
            self.backup_policy_id = backup_policy_id
        self.billing = billing
        if description is not None:
            self.description = description
        self.name = name
        self.resources = resources
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if auto_bind is not None:
            self.auto_bind = auto_bind
        if bind_rules is not None:
            self.bind_rules = bind_rules
        if auto_expand is not None:
            self.auto_expand = auto_expand
        if threshold is not None:
            self.threshold = threshold
        if smn_notify is not None:
            self.smn_notify = smn_notify
        if backup_name_prefix is not None:
            self.backup_name_prefix = backup_name_prefix
        if demand_billing is not None:
            self.demand_billing = demand_billing
        if sys_lock_source_service is not None:
            self.sys_lock_source_service = sys_lock_source_service
        if locked is not None:
            self.locked = locked

    @property
    def backup_policy_id(self):
        r"""Gets the backup_policy_id of this VaultCreate.

        备份策略ID，不设置时为null，不自动备份。

        :return: The backup_policy_id of this VaultCreate.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        r"""Sets the backup_policy_id of this VaultCreate.

        备份策略ID，不设置时为null，不自动备份。

        :param backup_policy_id: The backup_policy_id of this VaultCreate.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def billing(self):
        r"""Gets the billing of this VaultCreate.

        :return: The billing of this VaultCreate.
        :rtype: :class:`huaweicloudsdkcbr.v1.BillingCreate`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this VaultCreate.

        :param billing: The billing of this VaultCreate.
        :type billing: :class:`huaweicloudsdkcbr.v1.BillingCreate`
        """
        self._billing = billing

    @property
    def description(self):
        r"""Gets the description of this VaultCreate.

        描述

        :return: The description of this VaultCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VaultCreate.

        描述

        :param description: The description of this VaultCreate.
        :type description: str
        """
        self._description = description

    @property
    def name(self):
        r"""Gets the name of this VaultCreate.

        存储库名称

        :return: The name of this VaultCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VaultCreate.

        存储库名称

        :param name: The name of this VaultCreate.
        :type name: str
        """
        self._name = name

    @property
    def resources(self):
        r"""Gets the resources of this VaultCreate.

        绑定的备份资源，未在创建时绑定资源填[]

        :return: The resources of this VaultCreate.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this VaultCreate.

        绑定的备份资源，未在创建时绑定资源填[]

        :param resources: The resources of this VaultCreate.
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        """
        self._resources = resources

    @property
    def tags(self):
        r"""Gets the tags of this VaultCreate.

        标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。

        :return: The tags of this VaultCreate.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this VaultCreate.

        标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。

        :param tags: The tags of this VaultCreate.
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this VaultCreate.

        企业项目ID，默认为‘0’。

        :return: The enterprise_project_id of this VaultCreate.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this VaultCreate.

        企业项目ID，默认为‘0’。

        :param enterprise_project_id: The enterprise_project_id of this VaultCreate.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_bind(self):
        r"""Gets the auto_bind of this VaultCreate.

        是否支持自动挂载。

        :return: The auto_bind of this VaultCreate.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        r"""Sets the auto_bind of this VaultCreate.

        是否支持自动挂载。

        :param auto_bind: The auto_bind of this VaultCreate.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        r"""Gets the bind_rules of this VaultCreate.

        :return: The bind_rules of this VaultCreate.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        r"""Sets the bind_rules of this VaultCreate.

        :param bind_rules: The bind_rules of this VaultCreate.
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def auto_expand(self):
        r"""Gets the auto_expand of this VaultCreate.

        [是否开启存储库自动扩容能力（只支持按需存储库）。](tag:hws,hws_hk) [是否开启存储库自动扩容能力。](tag:dt,ocb,tlf,sbc,fcs_vm,ctc,g42,tm,cmcc,hcso_dt)

        :return: The auto_expand of this VaultCreate.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        r"""Sets the auto_expand of this VaultCreate.

        [是否开启存储库自动扩容能力（只支持按需存储库）。](tag:hws,hws_hk) [是否开启存储库自动扩容能力。](tag:dt,ocb,tlf,sbc,fcs_vm,ctc,g42,tm,cmcc,hcso_dt)

        :param auto_expand: The auto_expand of this VaultCreate.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def threshold(self):
        r"""Gets the threshold of this VaultCreate.

        存储库容量阈值，已用容量占总容量达到此百分比，将根据 smn_notify 参数设置选择是否发送相关通知。 默认值为：80 最大值：100 最小值：1

        :return: The threshold of this VaultCreate.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this VaultCreate.

        存储库容量阈值，已用容量占总容量达到此百分比，将根据 smn_notify 参数设置选择是否发送相关通知。 默认值为：80 最大值：100 最小值：1

        :param threshold: The threshold of this VaultCreate.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def smn_notify(self):
        r"""Gets the smn_notify of this VaultCreate.

        存储库smn消息通知开关。 默认值为 true。

        :return: The smn_notify of this VaultCreate.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        r"""Sets the smn_notify of this VaultCreate.

        存储库smn消息通知开关。 默认值为 true。

        :param smn_notify: The smn_notify of this VaultCreate.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def backup_name_prefix(self):
        r"""Gets the backup_name_prefix of this VaultCreate.

        备份名称前缀，设置后该存储库自动备份产生的备份副本都将携带该备份名称前缀

        :return: The backup_name_prefix of this VaultCreate.
        :rtype: str
        """
        return self._backup_name_prefix

    @backup_name_prefix.setter
    def backup_name_prefix(self, backup_name_prefix):
        r"""Sets the backup_name_prefix of this VaultCreate.

        备份名称前缀，设置后该存储库自动备份产生的备份副本都将携带该备份名称前缀

        :param backup_name_prefix: The backup_name_prefix of this VaultCreate.
        :type backup_name_prefix: str
        """
        self._backup_name_prefix = backup_name_prefix

    @property
    def demand_billing(self):
        r"""Gets the demand_billing of this VaultCreate.

        存储库使用是否允许超出容量，只有创建包周期存储库时才允许该值为 true

        :return: The demand_billing of this VaultCreate.
        :rtype: bool
        """
        return self._demand_billing

    @demand_billing.setter
    def demand_billing(self, demand_billing):
        r"""Sets the demand_billing of this VaultCreate.

        存储库使用是否允许超出容量，只有创建包周期存储库时才允许该值为 true

        :param demand_billing: The demand_billing of this VaultCreate.
        :type demand_billing: bool
        """
        self._demand_billing = demand_billing

    @property
    def sys_lock_source_service(self):
        r"""Gets the sys_lock_source_service of this VaultCreate.

        用于标识SMB服务，您可以设置为SMB或者空

        :return: The sys_lock_source_service of this VaultCreate.
        :rtype: str
        """
        return self._sys_lock_source_service

    @sys_lock_source_service.setter
    def sys_lock_source_service(self, sys_lock_source_service):
        r"""Sets the sys_lock_source_service of this VaultCreate.

        用于标识SMB服务，您可以设置为SMB或者空

        :param sys_lock_source_service: The sys_lock_source_service of this VaultCreate.
        :type sys_lock_source_service: str
        """
        self._sys_lock_source_service = sys_lock_source_service

    @property
    def locked(self):
        r"""Gets the locked of this VaultCreate.

        用于标识该存储库是否已锁定

        :return: The locked of this VaultCreate.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this VaultCreate.

        用于标识该存储库是否已锁定

        :param locked: The locked of this VaultCreate.
        :type locked: bool
        """
        self._locked = locked

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
        if not isinstance(other, VaultCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
