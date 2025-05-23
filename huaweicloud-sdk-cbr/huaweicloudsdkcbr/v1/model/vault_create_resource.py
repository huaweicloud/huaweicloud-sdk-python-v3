# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VaultCreateResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'billing': 'Billing',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'project_id': 'str',
        'provider_id': 'str',
        'resources': 'list[ResourceResp]',
        'tags': 'list[Tag]',
        'enterprise_project_id': 'str',
        'auto_bind': 'bool',
        'bind_rules': 'VaultBindRules',
        'user_id': 'str',
        'created_at': 'str',
        'auto_expand': 'bool',
        'smn_notify': 'bool',
        'threshold': 'int',
        'err_text': 'str',
        'ret_code': 'str',
        'orders': 'list[CbcOrderResult]',
        'backup_name_prefix': 'str',
        'demand_billing': 'bool',
        'cbc_delete_count': 'int',
        'frozen': 'bool',
        'sys_lock_source_service': 'str',
        'locked': 'bool'
    }

    attribute_map = {
        'billing': 'billing',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'provider_id': 'provider_id',
        'resources': 'resources',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id',
        'auto_bind': 'auto_bind',
        'bind_rules': 'bind_rules',
        'user_id': 'user_id',
        'created_at': 'created_at',
        'auto_expand': 'auto_expand',
        'smn_notify': 'smn_notify',
        'threshold': 'threshold',
        'err_text': 'errText',
        'ret_code': 'retCode',
        'orders': 'orders',
        'backup_name_prefix': 'backup_name_prefix',
        'demand_billing': 'demand_billing',
        'cbc_delete_count': 'cbc_delete_count',
        'frozen': 'frozen',
        'sys_lock_source_service': 'sys_lock_source_service',
        'locked': 'locked'
    }

    def __init__(self, billing=None, description=None, id=None, name=None, project_id=None, provider_id=None, resources=None, tags=None, enterprise_project_id=None, auto_bind=None, bind_rules=None, user_id=None, created_at=None, auto_expand=None, smn_notify=None, threshold=None, err_text=None, ret_code=None, orders=None, backup_name_prefix=None, demand_billing=None, cbc_delete_count=None, frozen=None, sys_lock_source_service=None, locked=None):
        r"""VaultCreateResource

        The model defined in huaweicloud sdk

        :param billing: 
        :type billing: :class:`huaweicloudsdkcbr.v1.Billing`
        :param description: 存储库自定义描述信息。
        :type description: str
        :param id: 存储库ID
        :type id: str
        :param name: 存储库名称
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param provider_id: 存储库资源类型id
        :type provider_id: str
        :param resources: 存储库资源
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceResp`]
        :param tags: 存储库标签
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        :param enterprise_project_id: 企业项目id，默认为‘0’。
        :type enterprise_project_id: str
        :param auto_bind: 是否自动绑定，默认为false，不支持。
        :type auto_bind: bool
        :param bind_rules: 
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        :param user_id: 用户id
        :type user_id: str
        :param created_at: 创建时间,例如:\&quot;2020-02-05T10:38:34.209782\&quot;
        :type created_at: str
        :param auto_expand: [是否开启存储库自动扩容能力（只支持按需存储库）。](tag:hws,hws_hk) [是否开启存储库自动扩容能力。](tag:dt,ocb,tlf,sbc,fcs_vm,ctc,g42,tm,cmcc,tm,hcso_dt)
        :type auto_expand: bool
        :param smn_notify: 存储库smn消息通知开关
        :type smn_notify: bool
        :param threshold: 存储库容量阈值，已用容量占总容量达到此百分比即发送相关通知
        :type threshold: int
        :param err_text: 包周期创建错误信息
        :type err_text: str
        :param ret_code: 包周期订购结果
        :type ret_code: str
        :param orders: 包周期创建订单信息
        :type orders: list[:class:`huaweicloudsdkcbr.v1.CbcOrderResult`]
        :param backup_name_prefix: 备份名称前缀
        :type backup_name_prefix: str
        :param demand_billing: 是否允许使用超出存储库容量
        :type demand_billing: bool
        :param cbc_delete_count: 存储库删除次数
        :type cbc_delete_count: int
        :param frozen: 存储库是否冻结
        :type frozen: bool
        :param sys_lock_source_service: 用于标识SMB服务
        :type sys_lock_source_service: str
        :param locked: 用于标识该存储库是否已锁定
        :type locked: bool
        """
        
        

        self._billing = None
        self._description = None
        self._id = None
        self._name = None
        self._project_id = None
        self._provider_id = None
        self._resources = None
        self._tags = None
        self._enterprise_project_id = None
        self._auto_bind = None
        self._bind_rules = None
        self._user_id = None
        self._created_at = None
        self._auto_expand = None
        self._smn_notify = None
        self._threshold = None
        self._err_text = None
        self._ret_code = None
        self._orders = None
        self._backup_name_prefix = None
        self._demand_billing = None
        self._cbc_delete_count = None
        self._frozen = None
        self._sys_lock_source_service = None
        self._locked = None
        self.discriminator = None

        self.billing = billing
        if description is not None:
            self.description = description
        self.id = id
        self.name = name
        self.project_id = project_id
        self.provider_id = provider_id
        self.resources = resources
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if auto_bind is not None:
            self.auto_bind = auto_bind
        if bind_rules is not None:
            self.bind_rules = bind_rules
        if user_id is not None:
            self.user_id = user_id
        if created_at is not None:
            self.created_at = created_at
        if auto_expand is not None:
            self.auto_expand = auto_expand
        if smn_notify is not None:
            self.smn_notify = smn_notify
        if threshold is not None:
            self.threshold = threshold
        if err_text is not None:
            self.err_text = err_text
        if ret_code is not None:
            self.ret_code = ret_code
        if orders is not None:
            self.orders = orders
        if backup_name_prefix is not None:
            self.backup_name_prefix = backup_name_prefix
        if demand_billing is not None:
            self.demand_billing = demand_billing
        if cbc_delete_count is not None:
            self.cbc_delete_count = cbc_delete_count
        if frozen is not None:
            self.frozen = frozen
        if sys_lock_source_service is not None:
            self.sys_lock_source_service = sys_lock_source_service
        if locked is not None:
            self.locked = locked

    @property
    def billing(self):
        r"""Gets the billing of this VaultCreateResource.

        :return: The billing of this VaultCreateResource.
        :rtype: :class:`huaweicloudsdkcbr.v1.Billing`
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        r"""Sets the billing of this VaultCreateResource.

        :param billing: The billing of this VaultCreateResource.
        :type billing: :class:`huaweicloudsdkcbr.v1.Billing`
        """
        self._billing = billing

    @property
    def description(self):
        r"""Gets the description of this VaultCreateResource.

        存储库自定义描述信息。

        :return: The description of this VaultCreateResource.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VaultCreateResource.

        存储库自定义描述信息。

        :param description: The description of this VaultCreateResource.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this VaultCreateResource.

        存储库ID

        :return: The id of this VaultCreateResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VaultCreateResource.

        存储库ID

        :param id: The id of this VaultCreateResource.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this VaultCreateResource.

        存储库名称

        :return: The name of this VaultCreateResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VaultCreateResource.

        存储库名称

        :param name: The name of this VaultCreateResource.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this VaultCreateResource.

        项目ID

        :return: The project_id of this VaultCreateResource.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this VaultCreateResource.

        项目ID

        :param project_id: The project_id of this VaultCreateResource.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def provider_id(self):
        r"""Gets the provider_id of this VaultCreateResource.

        存储库资源类型id

        :return: The provider_id of this VaultCreateResource.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this VaultCreateResource.

        存储库资源类型id

        :param provider_id: The provider_id of this VaultCreateResource.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def resources(self):
        r"""Gets the resources of this VaultCreateResource.

        存储库资源

        :return: The resources of this VaultCreateResource.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.ResourceResp`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this VaultCreateResource.

        存储库资源

        :param resources: The resources of this VaultCreateResource.
        :type resources: list[:class:`huaweicloudsdkcbr.v1.ResourceResp`]
        """
        self._resources = resources

    @property
    def tags(self):
        r"""Gets the tags of this VaultCreateResource.

        存储库标签

        :return: The tags of this VaultCreateResource.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this VaultCreateResource.

        存储库标签

        :param tags: The tags of this VaultCreateResource.
        :type tags: list[:class:`huaweicloudsdkcbr.v1.Tag`]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this VaultCreateResource.

        企业项目id，默认为‘0’。

        :return: The enterprise_project_id of this VaultCreateResource.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this VaultCreateResource.

        企业项目id，默认为‘0’。

        :param enterprise_project_id: The enterprise_project_id of this VaultCreateResource.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def auto_bind(self):
        r"""Gets the auto_bind of this VaultCreateResource.

        是否自动绑定，默认为false，不支持。

        :return: The auto_bind of this VaultCreateResource.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        r"""Sets the auto_bind of this VaultCreateResource.

        是否自动绑定，默认为false，不支持。

        :param auto_bind: The auto_bind of this VaultCreateResource.
        :type auto_bind: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        r"""Gets the bind_rules of this VaultCreateResource.

        :return: The bind_rules of this VaultCreateResource.
        :rtype: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        r"""Sets the bind_rules of this VaultCreateResource.

        :param bind_rules: The bind_rules of this VaultCreateResource.
        :type bind_rules: :class:`huaweicloudsdkcbr.v1.VaultBindRules`
        """
        self._bind_rules = bind_rules

    @property
    def user_id(self):
        r"""Gets the user_id of this VaultCreateResource.

        用户id

        :return: The user_id of this VaultCreateResource.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this VaultCreateResource.

        用户id

        :param user_id: The user_id of this VaultCreateResource.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def created_at(self):
        r"""Gets the created_at of this VaultCreateResource.

        创建时间,例如:\"2020-02-05T10:38:34.209782\"

        :return: The created_at of this VaultCreateResource.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this VaultCreateResource.

        创建时间,例如:\"2020-02-05T10:38:34.209782\"

        :param created_at: The created_at of this VaultCreateResource.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def auto_expand(self):
        r"""Gets the auto_expand of this VaultCreateResource.

        [是否开启存储库自动扩容能力（只支持按需存储库）。](tag:hws,hws_hk) [是否开启存储库自动扩容能力。](tag:dt,ocb,tlf,sbc,fcs_vm,ctc,g42,tm,cmcc,tm,hcso_dt)

        :return: The auto_expand of this VaultCreateResource.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        r"""Sets the auto_expand of this VaultCreateResource.

        [是否开启存储库自动扩容能力（只支持按需存储库）。](tag:hws,hws_hk) [是否开启存储库自动扩容能力。](tag:dt,ocb,tlf,sbc,fcs_vm,ctc,g42,tm,cmcc,tm,hcso_dt)

        :param auto_expand: The auto_expand of this VaultCreateResource.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def smn_notify(self):
        r"""Gets the smn_notify of this VaultCreateResource.

        存储库smn消息通知开关

        :return: The smn_notify of this VaultCreateResource.
        :rtype: bool
        """
        return self._smn_notify

    @smn_notify.setter
    def smn_notify(self, smn_notify):
        r"""Sets the smn_notify of this VaultCreateResource.

        存储库smn消息通知开关

        :param smn_notify: The smn_notify of this VaultCreateResource.
        :type smn_notify: bool
        """
        self._smn_notify = smn_notify

    @property
    def threshold(self):
        r"""Gets the threshold of this VaultCreateResource.

        存储库容量阈值，已用容量占总容量达到此百分比即发送相关通知

        :return: The threshold of this VaultCreateResource.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this VaultCreateResource.

        存储库容量阈值，已用容量占总容量达到此百分比即发送相关通知

        :param threshold: The threshold of this VaultCreateResource.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def err_text(self):
        r"""Gets the err_text of this VaultCreateResource.

        包周期创建错误信息

        :return: The err_text of this VaultCreateResource.
        :rtype: str
        """
        return self._err_text

    @err_text.setter
    def err_text(self, err_text):
        r"""Sets the err_text of this VaultCreateResource.

        包周期创建错误信息

        :param err_text: The err_text of this VaultCreateResource.
        :type err_text: str
        """
        self._err_text = err_text

    @property
    def ret_code(self):
        r"""Gets the ret_code of this VaultCreateResource.

        包周期订购结果

        :return: The ret_code of this VaultCreateResource.
        :rtype: str
        """
        return self._ret_code

    @ret_code.setter
    def ret_code(self, ret_code):
        r"""Sets the ret_code of this VaultCreateResource.

        包周期订购结果

        :param ret_code: The ret_code of this VaultCreateResource.
        :type ret_code: str
        """
        self._ret_code = ret_code

    @property
    def orders(self):
        r"""Gets the orders of this VaultCreateResource.

        包周期创建订单信息

        :return: The orders of this VaultCreateResource.
        :rtype: list[:class:`huaweicloudsdkcbr.v1.CbcOrderResult`]
        """
        return self._orders

    @orders.setter
    def orders(self, orders):
        r"""Sets the orders of this VaultCreateResource.

        包周期创建订单信息

        :param orders: The orders of this VaultCreateResource.
        :type orders: list[:class:`huaweicloudsdkcbr.v1.CbcOrderResult`]
        """
        self._orders = orders

    @property
    def backup_name_prefix(self):
        r"""Gets the backup_name_prefix of this VaultCreateResource.

        备份名称前缀

        :return: The backup_name_prefix of this VaultCreateResource.
        :rtype: str
        """
        return self._backup_name_prefix

    @backup_name_prefix.setter
    def backup_name_prefix(self, backup_name_prefix):
        r"""Sets the backup_name_prefix of this VaultCreateResource.

        备份名称前缀

        :param backup_name_prefix: The backup_name_prefix of this VaultCreateResource.
        :type backup_name_prefix: str
        """
        self._backup_name_prefix = backup_name_prefix

    @property
    def demand_billing(self):
        r"""Gets the demand_billing of this VaultCreateResource.

        是否允许使用超出存储库容量

        :return: The demand_billing of this VaultCreateResource.
        :rtype: bool
        """
        return self._demand_billing

    @demand_billing.setter
    def demand_billing(self, demand_billing):
        r"""Sets the demand_billing of this VaultCreateResource.

        是否允许使用超出存储库容量

        :param demand_billing: The demand_billing of this VaultCreateResource.
        :type demand_billing: bool
        """
        self._demand_billing = demand_billing

    @property
    def cbc_delete_count(self):
        r"""Gets the cbc_delete_count of this VaultCreateResource.

        存储库删除次数

        :return: The cbc_delete_count of this VaultCreateResource.
        :rtype: int
        """
        return self._cbc_delete_count

    @cbc_delete_count.setter
    def cbc_delete_count(self, cbc_delete_count):
        r"""Sets the cbc_delete_count of this VaultCreateResource.

        存储库删除次数

        :param cbc_delete_count: The cbc_delete_count of this VaultCreateResource.
        :type cbc_delete_count: int
        """
        self._cbc_delete_count = cbc_delete_count

    @property
    def frozen(self):
        r"""Gets the frozen of this VaultCreateResource.

        存储库是否冻结

        :return: The frozen of this VaultCreateResource.
        :rtype: bool
        """
        return self._frozen

    @frozen.setter
    def frozen(self, frozen):
        r"""Sets the frozen of this VaultCreateResource.

        存储库是否冻结

        :param frozen: The frozen of this VaultCreateResource.
        :type frozen: bool
        """
        self._frozen = frozen

    @property
    def sys_lock_source_service(self):
        r"""Gets the sys_lock_source_service of this VaultCreateResource.

        用于标识SMB服务

        :return: The sys_lock_source_service of this VaultCreateResource.
        :rtype: str
        """
        return self._sys_lock_source_service

    @sys_lock_source_service.setter
    def sys_lock_source_service(self, sys_lock_source_service):
        r"""Sets the sys_lock_source_service of this VaultCreateResource.

        用于标识SMB服务

        :param sys_lock_source_service: The sys_lock_source_service of this VaultCreateResource.
        :type sys_lock_source_service: str
        """
        self._sys_lock_source_service = sys_lock_source_service

    @property
    def locked(self):
        r"""Gets the locked of this VaultCreateResource.

        用于标识该存储库是否已锁定

        :return: The locked of this VaultCreateResource.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this VaultCreateResource.

        用于标识该存储库是否已锁定

        :param locked: The locked of this VaultCreateResource.
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
        if not isinstance(other, VaultCreateResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
