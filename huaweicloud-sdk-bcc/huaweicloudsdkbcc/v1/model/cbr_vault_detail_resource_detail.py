# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CbrVaultDetailResourceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'cross_account': 'bool',
        'charging_mode': 'str',
        'object_type': 'str',
        'protect_type': 'str',
        'policy_ids': 'list[str]',
        'used': 'str',
        'bind_rules': 'str',
        'size': 'int',
        'vault_resources': 'list[str]',
        'cross_account_urn': 'str',
        'provider_id': 'str',
        'locked': 'bool',
        'auto_expand': 'bool',
        'is_multi_az': 'bool',
        'protect_status': 'list[str]',
        'status': 'str'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'cross_account': 'cross_account',
        'charging_mode': 'charging_mode',
        'object_type': 'object_type',
        'protect_type': 'protect_type',
        'policy_ids': 'policy_ids',
        'used': 'used',
        'bind_rules': 'bind_rules',
        'size': 'size',
        'vault_resources': 'vault_resources',
        'cross_account_urn': 'cross_account_urn',
        'provider_id': 'provider_id',
        'locked': 'locked',
        'auto_expand': 'auto_expand',
        'is_multi_az': 'is_multi_az',
        'protect_status': 'protect_status',
        'status': 'status'
    }

    def __init__(self, spec_code=None, cross_account=None, charging_mode=None, object_type=None, protect_type=None, policy_ids=None, used=None, bind_rules=None, size=None, vault_resources=None, cross_account_urn=None, provider_id=None, locked=None, auto_expand=None, is_multi_az=None, protect_status=None, status=None):
        r"""CbrVaultDetailResourceDetail

        The model defined in huaweicloud sdk

        :param spec_code: 规格编码。
        :type spec_code: str
        :param cross_account: 是否跨账号
        :type cross_account: bool
        :param charging_mode: 创建模式，按需：post_paid，包周期：pre_paid，默认为post_paid
        :type charging_mode: str
        :param object_type: 对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace），VMware（vmware），关系型数据库（rds），文件（file）
        :type object_type: str
        :param protect_type: 保护类型：备份（backup）、复制(replication)。
        :type protect_type: str
        :param policy_ids: 存储库关联的保护策略id
        :type policy_ids: list[str]
        :param used: 已使用容量，单位MB
        :type used: str
        :param bind_rules: 绑定规则
        :type bind_rules: str
        :param size: 容量，单位GB
        :type size: int
        :param vault_resources: 存储库资源列表
        :type vault_resources: list[str]
        :param cross_account_urn: 跨账号URN
        :type cross_account_urn: str
        :param provider_id: 存储库资源类型id
        :type provider_id: str
        :param locked: 是否已锁定
        :type locked: bool
        :param auto_expand: 是否开启存储库自动扩容能力（只支持按需存储库）。
        :type auto_expand: bool
        :param is_multi_az: 存储库是否多az
        :type is_multi_az: bool
        :param protect_status: 保护状态
        :type protect_status: list[str]
        :param status: status
        :type status: str
        """
        
        

        self._spec_code = None
        self._cross_account = None
        self._charging_mode = None
        self._object_type = None
        self._protect_type = None
        self._policy_ids = None
        self._used = None
        self._bind_rules = None
        self._size = None
        self._vault_resources = None
        self._cross_account_urn = None
        self._provider_id = None
        self._locked = None
        self._auto_expand = None
        self._is_multi_az = None
        self._protect_status = None
        self._status = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if cross_account is not None:
            self.cross_account = cross_account
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if object_type is not None:
            self.object_type = object_type
        if protect_type is not None:
            self.protect_type = protect_type
        if policy_ids is not None:
            self.policy_ids = policy_ids
        if used is not None:
            self.used = used
        if bind_rules is not None:
            self.bind_rules = bind_rules
        if size is not None:
            self.size = size
        if vault_resources is not None:
            self.vault_resources = vault_resources
        if cross_account_urn is not None:
            self.cross_account_urn = cross_account_urn
        if provider_id is not None:
            self.provider_id = provider_id
        if locked is not None:
            self.locked = locked
        if auto_expand is not None:
            self.auto_expand = auto_expand
        if is_multi_az is not None:
            self.is_multi_az = is_multi_az
        if protect_status is not None:
            self.protect_status = protect_status
        if status is not None:
            self.status = status

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CbrVaultDetailResourceDetail.

        规格编码。

        :return: The spec_code of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CbrVaultDetailResourceDetail.

        规格编码。

        :param spec_code: The spec_code of this CbrVaultDetailResourceDetail.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def cross_account(self):
        r"""Gets the cross_account of this CbrVaultDetailResourceDetail.

        是否跨账号

        :return: The cross_account of this CbrVaultDetailResourceDetail.
        :rtype: bool
        """
        return self._cross_account

    @cross_account.setter
    def cross_account(self, cross_account):
        r"""Sets the cross_account of this CbrVaultDetailResourceDetail.

        是否跨账号

        :param cross_account: The cross_account of this CbrVaultDetailResourceDetail.
        :type cross_account: bool
        """
        self._cross_account = cross_account

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CbrVaultDetailResourceDetail.

        创建模式，按需：post_paid，包周期：pre_paid，默认为post_paid

        :return: The charging_mode of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CbrVaultDetailResourceDetail.

        创建模式，按需：post_paid，包周期：pre_paid，默认为post_paid

        :param charging_mode: The charging_mode of this CbrVaultDetailResourceDetail.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def object_type(self):
        r"""Gets the object_type of this CbrVaultDetailResourceDetail.

        对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace），VMware（vmware），关系型数据库（rds），文件（file）

        :return: The object_type of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this CbrVaultDetailResourceDetail.

        对象类型：云服务器（server），云硬盘（disk），文件系统（turbo），云桌面（workspace），VMware（vmware），关系型数据库（rds），文件（file）

        :param object_type: The object_type of this CbrVaultDetailResourceDetail.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def protect_type(self):
        r"""Gets the protect_type of this CbrVaultDetailResourceDetail.

        保护类型：备份（backup）、复制(replication)。

        :return: The protect_type of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        r"""Sets the protect_type of this CbrVaultDetailResourceDetail.

        保护类型：备份（backup）、复制(replication)。

        :param protect_type: The protect_type of this CbrVaultDetailResourceDetail.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def policy_ids(self):
        r"""Gets the policy_ids of this CbrVaultDetailResourceDetail.

        存储库关联的保护策略id

        :return: The policy_ids of this CbrVaultDetailResourceDetail.
        :rtype: list[str]
        """
        return self._policy_ids

    @policy_ids.setter
    def policy_ids(self, policy_ids):
        r"""Sets the policy_ids of this CbrVaultDetailResourceDetail.

        存储库关联的保护策略id

        :param policy_ids: The policy_ids of this CbrVaultDetailResourceDetail.
        :type policy_ids: list[str]
        """
        self._policy_ids = policy_ids

    @property
    def used(self):
        r"""Gets the used of this CbrVaultDetailResourceDetail.

        已使用容量，单位MB

        :return: The used of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        r"""Sets the used of this CbrVaultDetailResourceDetail.

        已使用容量，单位MB

        :param used: The used of this CbrVaultDetailResourceDetail.
        :type used: str
        """
        self._used = used

    @property
    def bind_rules(self):
        r"""Gets the bind_rules of this CbrVaultDetailResourceDetail.

        绑定规则

        :return: The bind_rules of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        r"""Sets the bind_rules of this CbrVaultDetailResourceDetail.

        绑定规则

        :param bind_rules: The bind_rules of this CbrVaultDetailResourceDetail.
        :type bind_rules: str
        """
        self._bind_rules = bind_rules

    @property
    def size(self):
        r"""Gets the size of this CbrVaultDetailResourceDetail.

        容量，单位GB

        :return: The size of this CbrVaultDetailResourceDetail.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this CbrVaultDetailResourceDetail.

        容量，单位GB

        :param size: The size of this CbrVaultDetailResourceDetail.
        :type size: int
        """
        self._size = size

    @property
    def vault_resources(self):
        r"""Gets the vault_resources of this CbrVaultDetailResourceDetail.

        存储库资源列表

        :return: The vault_resources of this CbrVaultDetailResourceDetail.
        :rtype: list[str]
        """
        return self._vault_resources

    @vault_resources.setter
    def vault_resources(self, vault_resources):
        r"""Sets the vault_resources of this CbrVaultDetailResourceDetail.

        存储库资源列表

        :param vault_resources: The vault_resources of this CbrVaultDetailResourceDetail.
        :type vault_resources: list[str]
        """
        self._vault_resources = vault_resources

    @property
    def cross_account_urn(self):
        r"""Gets the cross_account_urn of this CbrVaultDetailResourceDetail.

        跨账号URN

        :return: The cross_account_urn of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._cross_account_urn

    @cross_account_urn.setter
    def cross_account_urn(self, cross_account_urn):
        r"""Sets the cross_account_urn of this CbrVaultDetailResourceDetail.

        跨账号URN

        :param cross_account_urn: The cross_account_urn of this CbrVaultDetailResourceDetail.
        :type cross_account_urn: str
        """
        self._cross_account_urn = cross_account_urn

    @property
    def provider_id(self):
        r"""Gets the provider_id of this CbrVaultDetailResourceDetail.

        存储库资源类型id

        :return: The provider_id of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this CbrVaultDetailResourceDetail.

        存储库资源类型id

        :param provider_id: The provider_id of this CbrVaultDetailResourceDetail.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def locked(self):
        r"""Gets the locked of this CbrVaultDetailResourceDetail.

        是否已锁定

        :return: The locked of this CbrVaultDetailResourceDetail.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this CbrVaultDetailResourceDetail.

        是否已锁定

        :param locked: The locked of this CbrVaultDetailResourceDetail.
        :type locked: bool
        """
        self._locked = locked

    @property
    def auto_expand(self):
        r"""Gets the auto_expand of this CbrVaultDetailResourceDetail.

        是否开启存储库自动扩容能力（只支持按需存储库）。

        :return: The auto_expand of this CbrVaultDetailResourceDetail.
        :rtype: bool
        """
        return self._auto_expand

    @auto_expand.setter
    def auto_expand(self, auto_expand):
        r"""Sets the auto_expand of this CbrVaultDetailResourceDetail.

        是否开启存储库自动扩容能力（只支持按需存储库）。

        :param auto_expand: The auto_expand of this CbrVaultDetailResourceDetail.
        :type auto_expand: bool
        """
        self._auto_expand = auto_expand

    @property
    def is_multi_az(self):
        r"""Gets the is_multi_az of this CbrVaultDetailResourceDetail.

        存储库是否多az

        :return: The is_multi_az of this CbrVaultDetailResourceDetail.
        :rtype: bool
        """
        return self._is_multi_az

    @is_multi_az.setter
    def is_multi_az(self, is_multi_az):
        r"""Sets the is_multi_az of this CbrVaultDetailResourceDetail.

        存储库是否多az

        :param is_multi_az: The is_multi_az of this CbrVaultDetailResourceDetail.
        :type is_multi_az: bool
        """
        self._is_multi_az = is_multi_az

    @property
    def protect_status(self):
        r"""Gets the protect_status of this CbrVaultDetailResourceDetail.

        保护状态

        :return: The protect_status of this CbrVaultDetailResourceDetail.
        :rtype: list[str]
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this CbrVaultDetailResourceDetail.

        保护状态

        :param protect_status: The protect_status of this CbrVaultDetailResourceDetail.
        :type protect_status: list[str]
        """
        self._protect_status = protect_status

    @property
    def status(self):
        r"""Gets the status of this CbrVaultDetailResourceDetail.

        status

        :return: The status of this CbrVaultDetailResourceDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CbrVaultDetailResourceDetail.

        status

        :param status: The status of this CbrVaultDetailResourceDetail.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, CbrVaultDetailResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
