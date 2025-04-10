# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultOrder:

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
        'billing': 'BillingCreate',
        'resources': 'list[ResourceCreate]',
        'description': 'str',
        'backup_policy_id': 'str',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'auto_bind': 'bool',
        'bind_rules': 'VaultBindRules',
        'threshold': 'int',
        'smn_notify': 'bool',
        'parameters': 'VaultCreateParameters',
        'auto_expand': 'bool',
        'locked': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'billing': 'billing',
        'resources': 'resources',
        'description': 'description',
        'backup_policy_id': 'backup_policy_id',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'auto_bind': 'auto_bind',
        'bind_rules': 'bind_rules',
        'threshold': 'threshold',
        'smn_notify': 'smn_notify',
        'parameters': 'parameters',
        'auto_expand': 'auto_expand',
        'locked': 'locked'
    }

    def __init__(self, name=None, billing=None, resources=None, description=None, backup_policy_id=None, tags=None, enterprise_project_id=None, auto_bind=None, bind_rules=None, threshold=None, smn_notify=None, parameters=None, auto_expand=None, locked=None):
        r"""VaultOrder

        The model defined in huaweicloud sdk

        :param name: 存储库名称  最小长度：1  最大长度：64
        :type name: str
        :param billing: 
        :type billing: :class:`huaweicloudsdkcbr.v1.BillingCreate`
        :param resources: 绑定的备份资源，未在创建时绑定资源填[]
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        :param description: 描述  最小长度：0  最大长度：255
        :type description: str
        :param backup_policy_id: 备份策略ID，不设置时为null，不自动备份。
        :type backup_policy_id: str
        :param tags: 标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        :param enterprise_project_id: 企业项目ID，默认为‘0’。
        :type enterprise_project_id: str
        :param auto_bind: 是否支持自动挂载。
        :type auto_bind: bool
        :param bind_rules: 
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        :param threshold: 存储库阈值，百分比。  最小值：1  最大值：100
        :type threshold: int
        :param smn_notify: 当容量到达阈值，是否启用通知
        :type smn_notify: bool
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkcbr.v1.VaultCreateParameters`
        :param auto_expand: 是否开启存储库自动扩容能力（只支持按需存储库）。
        :type auto_expand: bool
        :param locked: 用于标识当前存储库是否已锁定
        :type locked: bool
        """
        
        

        self._name = None
        self._billing = None
        self._resources = None
        self._description = None
        self._backup_policy_id = None
        self._tags = None
        self._enterprise_project_id = None
        self._auto_bind = None
        self._bind_rules = None
        self._threshold = None
        self._smn_notify = None
        self._parameters = None
        self._auto_expand = None
        self._locked = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.billing = billing
        self.resources = resources
        if description is not None:
            self.description = description
        if backup_policy_id is not None:
            self.backup_policy_id = backup_policy_id
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if auto_bind is not None:
            self.auto_bind = auto_bind
        if bind_rules is not None:
            self.bind_rules = bind_rules
        if threshold is not None:
            self.threshold = threshold
        if smn_notify is not None:
            self.smn_notify = smn_notify
        if parameters is not None:
            self.parameters = parameters
        if auto_expand is not None:
            self.auto_expand = auto_expand
        if locked is not None:
            self.locked = locked

    @property
    def name(self):
        r"""Gets the name of this VaultOrder.

        存储库名称  最小长度：1  最大长度：64

        :return: The name of this VaultOrder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VaultOrder.

        存储库名称  最小长度：1  最大长度：64

        :param name: The name of this VaultOrder.
        :type name: str
        """
        self._name = name

    @property
    def billing(self):
        r"""Gets the billing of this VaultOrder.

        :return: The billing of this VaultOrder.
        :rtype: :class:`huaweicloudsdkcbr.v1.BillingCreate`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this VaultOrder.

        :param billing: The billing of this VaultOrder.
        :type billing: :class:`huaweicloudsdkcbr.v1.BillingCreate`
        """
        self._billing = billing

    @property
    def resources(self):
        r"""Gets the resources of this VaultOrder.

        绑定的备份资源，未在创建时绑定资源填[]

        :return: The resources of this VaultOrder.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this VaultOrder.

        绑定的备份资源，未在创建时绑定资源填[]

        :param resources: The resources of this VaultOrder.
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        """
        self._resources = resources

    @property
    def description(self):
        r"""Gets the description of this VaultOrder.

        描述  最小长度：0  最大长度：255

        :return: The description of this VaultOrder.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VaultOrder.

        描述  最小长度：0  最大长度：255

        :param description: The description of this VaultOrder.
        :type description: str
        """
        self._description = description

    @property
    def backup_policy_id(self):
        r"""Gets the backup_policy_id of this VaultOrder.

        备份策略ID，不设置时为null，不自动备份。

        :return: The backup_policy_id of this VaultOrder.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        r"""Sets the backup_policy_id of this VaultOrder.

        备份策略ID，不设置时为null，不自动备份。

        :param backup_policy_id: The backup_policy_id of this VaultOrder.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def tags(self):
        r"""Gets the tags of this VaultOrder.

        标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。

        :return: The tags of this VaultOrder.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this VaultOrder.

        标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。

        :param tags: The tags of this VaultOrder.
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this VaultOrder.

        企业项目ID，默认为‘0’。

        :return: The enterprise_project_id of this VaultOrder.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this VaultOrder.

        企业项目ID，默认为‘0’。

        :param enterprise_project_id: The enterprise_project_id of this VaultOrder.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_bind(self):
        r"""Gets the auto_bind of this VaultOrder.

        是否支持自动挂载。

        :return: The auto_bind of this VaultOrder.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        r"""Sets the auto_bind of this VaultOrder.

        是否支持自动挂载。

        :param auto_bind: The auto_bind of this VaultOrder.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        r"""Gets the bind_rules of this VaultOrder.

        :return: The bind_rules of this VaultOrder.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        r"""Sets the bind_rules of this VaultOrder.

        :param bind_rules: The bind_rules of this VaultOrder.
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def threshold(self):
        r"""Gets the threshold of this VaultOrder.

        存储库阈值，百分比。  最小值：1  最大值：100

        :return: The threshold of this VaultOrder.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this VaultOrder.

        存储库阈值，百分比。  最小值：1  最大值：100

        :param threshold: The threshold of this VaultOrder.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def smn_notify(self):
        r"""Gets the smn_notify of this VaultOrder.

        当容量到达阈值，是否启用通知

        :return: The smn_notify of this VaultOrder.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        r"""Sets the smn_notify of this VaultOrder.

        当容量到达阈值，是否启用通知

        :param smn_notify: The smn_notify of this VaultOrder.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def parameters(self):
        r"""Gets the parameters of this VaultOrder.

        :return: The parameters of this VaultOrder.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultCreateParameters`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this VaultOrder.

        :param parameters: The parameters of this VaultOrder.
        :type parameters: :class:`huaweicloudsdkcbr.v1.VaultCreateParameters`
        """
        self._parameters = parameters

    @property
    def auto_expand(self):
        r"""Gets the auto_expand of this VaultOrder.

        是否开启存储库自动扩容能力（只支持按需存储库）。

        :return: The auto_expand of this VaultOrder.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        r"""Sets the auto_expand of this VaultOrder.

        是否开启存储库自动扩容能力（只支持按需存储库）。

        :param auto_expand: The auto_expand of this VaultOrder.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def locked(self):
        r"""Gets the locked of this VaultOrder.

        用于标识当前存储库是否已锁定

        :return: The locked of this VaultOrder.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this VaultOrder.

        用于标识当前存储库是否已锁定

        :param locked: The locked of this VaultOrder.
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
        if not isinstance(other, VaultOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
