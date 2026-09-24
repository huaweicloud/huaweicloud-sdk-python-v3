# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrePaidVaultOrder:

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
        'billing': 'PrePaidBillingCreate',
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
        'locked': 'bool',
        'cross_account': 'bool',
        'data_encryption': 'DataEncryption'
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
        'locked': 'locked',
        'cross_account': 'cross_account',
        'data_encryption': 'data_encryption'
    }

    def __init__(self, name=None, billing=None, resources=None, description=None, backup_policy_id=None, tags=None, enterprise_project_id=None, auto_bind=None, bind_rules=None, threshold=None, smn_notify=None, parameters=None, auto_expand=None, locked=None, cross_account=None, data_encryption=None):
        r"""PrePaidVaultOrder

        The model defined in huaweicloud sdk

        :param name: 存储库名称，最大支持64字符，只能由中文、字母、数字、\&quot;_\&quot;、\&quot;-\&quot;组成。默认取值不涉及。
        :type name: str
        :param billing: 
        :type billing: :class:`huaweicloudsdkcbr.v1.PrePaidBillingCreate`
        :param resources: 绑定的备份资源，未在创建时绑定资源填[]
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        :param description: 存储库描述，取值范围：最小长度：0，最大长度：255。默认取值不涉及。
        :type description: str
        :param backup_policy_id: 备份策略ID，默认值为null，不自动备份。 [获取方法请参见\&quot;[获取备份策略ID](https://support.huaweicloud.com/api-cbr/ListPolicies.html)\&quot;。](tag:hws) [获取方法请参见\&quot;[获取备份策略ID](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ListPolicies.html)\&quot;。](tag:hws_hk)
        :type backup_policy_id: str
        :param tags: 标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        :param enterprise_project_id: 企业项目ID，默认为&#39;0&#39;。 [获取方法请参见\&quot;[获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)\&quot;。](tag:hws) [获取方法请参见\&quot;[获取企业项目ID](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0126101490.html)\&quot;。](tag:hws_hk)
        :type enterprise_project_id: str
        :param auto_bind: 功能说明：是否支持自动挂载。默认为false。 取值范围： - true：支持自动挂载 - false：不支持自动挂载
        :type auto_bind: bool
        :param bind_rules: 
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        :param threshold: 功能说明：存储库容量阈值，存储库已用容量和总容量的百分比超过该值，如果smn_notify为开，将发送相关通知。 取值范围：[1, 100]，默认值为80。
        :type threshold: int
        :param smn_notify: 功能说明：是否发送smn通知开关，默认为true 取值范围： - true：发送smn通知 - false：不发送smn通知
        :type smn_notify: bool
        :param parameters: 
        :type parameters: :class:`huaweicloudsdkcbr.v1.VaultCreateParameters`
        :param auto_expand: 功能说明：是否开启存储库自动扩容能力（只支持按需存储库），默认为false。 取值范围： - true：支持自动扩容； - false：不支持自动扩容。
        :type auto_expand: bool
        :param locked: 功能说明：用于标识当前存储库是否已锁定，锁定的存储库不支持解锁。默认值为false。 [关于备份锁定的详细信息，请参考\&quot;[开启备份锁定](https://support.huaweicloud.com/usermanual-cbr/cbr_01_0035.html)\&quot;。](tag:hws) [关于备份锁定的详细信息，请参考\&quot;[开启备份锁定](https://support.huaweicloud.com/intl/zh-cn/usermanual-cbr/cbr_01_0035.html)\&quot;。](tag:hws_hk) 取值范围： - true：锁定存储库 - false：不锁定存储库
        :type locked: bool
        :param cross_account: 功能说明：是否为跨账号复制存储库，默认值为false，只有创建跨账号复制存储库时才允许该值为true。 取值范围： - false: 非跨账号复制存储库 - true: 跨账号复制存储库
        :type cross_account: bool
        :param data_encryption: 
        :type data_encryption: :class:`huaweicloudsdkcbr.v1.DataEncryption`
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
        self._cross_account = None
        self._data_encryption = None
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
        if cross_account is not None:
            self.cross_account = cross_account
        if data_encryption is not None:
            self.data_encryption = data_encryption

    @property
    def name(self):
        r"""Gets the name of this PrePaidVaultOrder.

        存储库名称，最大支持64字符，只能由中文、字母、数字、\"_\"、\"-\"组成。默认取值不涉及。

        :return: The name of this PrePaidVaultOrder.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PrePaidVaultOrder.

        存储库名称，最大支持64字符，只能由中文、字母、数字、\"_\"、\"-\"组成。默认取值不涉及。

        :param name: The name of this PrePaidVaultOrder.
        :type name: str
        """
        self._name = name

    @property
    def billing(self):
        r"""Gets the billing of this PrePaidVaultOrder.

        :return: The billing of this PrePaidVaultOrder.
        :rtype: :class:`huaweicloudsdkcbr.v1.PrePaidBillingCreate`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this PrePaidVaultOrder.

        :param billing: The billing of this PrePaidVaultOrder.
        :type billing: :class:`huaweicloudsdkcbr.v1.PrePaidBillingCreate`
        """
        self._billing = billing

    @property
    def resources(self):
        r"""Gets the resources of this PrePaidVaultOrder.

        绑定的备份资源，未在创建时绑定资源填[]

        :return: The resources of this PrePaidVaultOrder.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this PrePaidVaultOrder.

        绑定的备份资源，未在创建时绑定资源填[]

        :param resources: The resources of this PrePaidVaultOrder.
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceCreate`]
        """
        self._resources = resources

    @property
    def description(self):
        r"""Gets the description of this PrePaidVaultOrder.

        存储库描述，取值范围：最小长度：0，最大长度：255。默认取值不涉及。

        :return: The description of this PrePaidVaultOrder.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PrePaidVaultOrder.

        存储库描述，取值范围：最小长度：0，最大长度：255。默认取值不涉及。

        :param description: The description of this PrePaidVaultOrder.
        :type description: str
        """
        self._description = description

    @property
    def backup_policy_id(self):
        r"""Gets the backup_policy_id of this PrePaidVaultOrder.

        备份策略ID，默认值为null，不自动备份。 [获取方法请参见\"[获取备份策略ID](https://support.huaweicloud.com/api-cbr/ListPolicies.html)\"。](tag:hws) [获取方法请参见\"[获取备份策略ID](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ListPolicies.html)\"。](tag:hws_hk)

        :return: The backup_policy_id of this PrePaidVaultOrder.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        r"""Sets the backup_policy_id of this PrePaidVaultOrder.

        备份策略ID，默认值为null，不自动备份。 [获取方法请参见\"[获取备份策略ID](https://support.huaweicloud.com/api-cbr/ListPolicies.html)\"。](tag:hws) [获取方法请参见\"[获取备份策略ID](https://support.huaweicloud.com/intl/zh-cn/api-cbr/ListPolicies.html)\"。](tag:hws_hk)

        :param backup_policy_id: The backup_policy_id of this PrePaidVaultOrder.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def tags(self):
        r"""Gets the tags of this PrePaidVaultOrder.

        标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。

        :return: The tags of this PrePaidVaultOrder.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this PrePaidVaultOrder.

        标签列表 tags不允许为空列表。 tags中最多包含10个key。 tags中key不允许重复。

        :param tags: The tags of this PrePaidVaultOrder.
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this PrePaidVaultOrder.

        企业项目ID，默认为'0'。 [获取方法请参见\"[获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)\"。](tag:hws) [获取方法请参见\"[获取企业项目ID](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0126101490.html)\"。](tag:hws_hk)

        :return: The enterprise_project_id of this PrePaidVaultOrder.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this PrePaidVaultOrder.

        企业项目ID，默认为'0'。 [获取方法请参见\"[获取企业项目ID](https://support.huaweicloud.com/usermanual-em/zh-cn_topic_0126101490.html)\"。](tag:hws) [获取方法请参见\"[获取企业项目ID](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/zh-cn_topic_0126101490.html)\"。](tag:hws_hk)

        :param enterprise_project_id: The enterprise_project_id of this PrePaidVaultOrder.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_bind(self):
        r"""Gets the auto_bind of this PrePaidVaultOrder.

        功能说明：是否支持自动挂载。默认为false。 取值范围： - true：支持自动挂载 - false：不支持自动挂载

        :return: The auto_bind of this PrePaidVaultOrder.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        r"""Sets the auto_bind of this PrePaidVaultOrder.

        功能说明：是否支持自动挂载。默认为false。 取值范围： - true：支持自动挂载 - false：不支持自动挂载

        :param auto_bind: The auto_bind of this PrePaidVaultOrder.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        r"""Gets the bind_rules of this PrePaidVaultOrder.

        :return: The bind_rules of this PrePaidVaultOrder.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        r"""Sets the bind_rules of this PrePaidVaultOrder.

        :param bind_rules: The bind_rules of this PrePaidVaultOrder.
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def threshold(self):
        r"""Gets the threshold of this PrePaidVaultOrder.

        功能说明：存储库容量阈值，存储库已用容量和总容量的百分比超过该值，如果smn_notify为开，将发送相关通知。 取值范围：[1, 100]，默认值为80。

        :return: The threshold of this PrePaidVaultOrder.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this PrePaidVaultOrder.

        功能说明：存储库容量阈值，存储库已用容量和总容量的百分比超过该值，如果smn_notify为开，将发送相关通知。 取值范围：[1, 100]，默认值为80。

        :param threshold: The threshold of this PrePaidVaultOrder.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def smn_notify(self):
        r"""Gets the smn_notify of this PrePaidVaultOrder.

        功能说明：是否发送smn通知开关，默认为true 取值范围： - true：发送smn通知 - false：不发送smn通知

        :return: The smn_notify of this PrePaidVaultOrder.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        r"""Sets the smn_notify of this PrePaidVaultOrder.

        功能说明：是否发送smn通知开关，默认为true 取值范围： - true：发送smn通知 - false：不发送smn通知

        :param smn_notify: The smn_notify of this PrePaidVaultOrder.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def parameters(self):
        r"""Gets the parameters of this PrePaidVaultOrder.

        :return: The parameters of this PrePaidVaultOrder.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultCreateParameters`
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this PrePaidVaultOrder.

        :param parameters: The parameters of this PrePaidVaultOrder.
        :type parameters: :class:`huaweicloudsdkcbr.v1.VaultCreateParameters`
        """
        self._parameters = parameters

    @property
    def auto_expand(self):
        r"""Gets the auto_expand of this PrePaidVaultOrder.

        功能说明：是否开启存储库自动扩容能力（只支持按需存储库），默认为false。 取值范围： - true：支持自动扩容； - false：不支持自动扩容。

        :return: The auto_expand of this PrePaidVaultOrder.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        r"""Sets the auto_expand of this PrePaidVaultOrder.

        功能说明：是否开启存储库自动扩容能力（只支持按需存储库），默认为false。 取值范围： - true：支持自动扩容； - false：不支持自动扩容。

        :param auto_expand: The auto_expand of this PrePaidVaultOrder.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def locked(self):
        r"""Gets the locked of this PrePaidVaultOrder.

        功能说明：用于标识当前存储库是否已锁定，锁定的存储库不支持解锁。默认值为false。 [关于备份锁定的详细信息，请参考\"[开启备份锁定](https://support.huaweicloud.com/usermanual-cbr/cbr_01_0035.html)\"。](tag:hws) [关于备份锁定的详细信息，请参考\"[开启备份锁定](https://support.huaweicloud.com/intl/zh-cn/usermanual-cbr/cbr_01_0035.html)\"。](tag:hws_hk) 取值范围： - true：锁定存储库 - false：不锁定存储库

        :return: The locked of this PrePaidVaultOrder.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this PrePaidVaultOrder.

        功能说明：用于标识当前存储库是否已锁定，锁定的存储库不支持解锁。默认值为false。 [关于备份锁定的详细信息，请参考\"[开启备份锁定](https://support.huaweicloud.com/usermanual-cbr/cbr_01_0035.html)\"。](tag:hws) [关于备份锁定的详细信息，请参考\"[开启备份锁定](https://support.huaweicloud.com/intl/zh-cn/usermanual-cbr/cbr_01_0035.html)\"。](tag:hws_hk) 取值范围： - true：锁定存储库 - false：不锁定存储库

        :param locked: The locked of this PrePaidVaultOrder.
        :type locked: bool
        """
        self._locked = locked

    @property
    def cross_account(self):
        r"""Gets the cross_account of this PrePaidVaultOrder.

        功能说明：是否为跨账号复制存储库，默认值为false，只有创建跨账号复制存储库时才允许该值为true。 取值范围： - false: 非跨账号复制存储库 - true: 跨账号复制存储库

        :return: The cross_account of this PrePaidVaultOrder.
        :rtype: bool
        """
        return self._cross_account

    @cross_account.setter
    def cross_account(self, cross_account):
        r"""Sets the cross_account of this PrePaidVaultOrder.

        功能说明：是否为跨账号复制存储库，默认值为false，只有创建跨账号复制存储库时才允许该值为true。 取值范围： - false: 非跨账号复制存储库 - true: 跨账号复制存储库

        :param cross_account: The cross_account of this PrePaidVaultOrder.
        :type cross_account: bool
        """
        self._cross_account = cross_account

    @property
    def data_encryption(self):
        r"""Gets the data_encryption of this PrePaidVaultOrder.

        :return: The data_encryption of this PrePaidVaultOrder.
        :rtype: :class:`huaweicloudsdkcbr.v1.DataEncryption`
        """
        return self._data_encryption

    @data_encryption.setter
    def data_encryption(self, data_encryption):
        r"""Sets the data_encryption of this PrePaidVaultOrder.

        :param data_encryption: The data_encryption of this PrePaidVaultOrder.
        :type data_encryption: :class:`huaweicloudsdkcbr.v1.DataEncryption`
        """
        self._data_encryption = data_encryption

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PrePaidVaultOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
