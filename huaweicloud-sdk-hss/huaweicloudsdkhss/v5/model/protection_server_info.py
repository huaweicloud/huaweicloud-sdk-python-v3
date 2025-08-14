# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionServerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'enterprise_project_id': 'str',
        'host_id': 'str',
        'agent_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'private_ip': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'host_status': 'str',
        'ransom_protection_status': 'str',
        'ransom_protection_fail_reason': 'str',
        'failed_decoy_dir': 'str',
        'agent_version': 'str',
        'protect_status': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'protect_policy_id': 'str',
        'protect_policy_name': 'str',
        'backup_error': 'ProtectionServerInfoBackupError',
        'backup_protection_status': 'str',
        'count_protect_event': 'int',
        'count_backuped': 'int',
        'agent_status': 'str',
        'version': 'str',
        'host_source': 'str',
        'vault_id': 'str',
        'vault_name': 'str',
        'vault_size': 'int',
        'vault_used': 'int',
        'vault_allocated': 'int',
        'vault_charging_mode': 'str',
        'vault_status': 'str',
        'backup_policy_id': 'str',
        'backup_policy_name': 'str',
        'backup_policy_enabled': 'bool',
        'resources_num': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'enterprise_project_id': 'enterprise_project_id',
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'private_ip': 'private_ip',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'host_status': 'host_status',
        'ransom_protection_status': 'ransom_protection_status',
        'ransom_protection_fail_reason': 'ransom_protection_fail_reason',
        'failed_decoy_dir': 'failed_decoy_dir',
        'agent_version': 'agent_version',
        'protect_status': 'protect_status',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'protect_policy_id': 'protect_policy_id',
        'protect_policy_name': 'protect_policy_name',
        'backup_error': 'backup_error',
        'backup_protection_status': 'backup_protection_status',
        'count_protect_event': 'count_protect_event',
        'count_backuped': 'count_backuped',
        'agent_status': 'agent_status',
        'version': 'version',
        'host_source': 'host_source',
        'vault_id': 'vault_id',
        'vault_name': 'vault_name',
        'vault_size': 'vault_size',
        'vault_used': 'vault_used',
        'vault_allocated': 'vault_allocated',
        'vault_charging_mode': 'vault_charging_mode',
        'vault_status': 'vault_status',
        'backup_policy_id': 'backup_policy_id',
        'backup_policy_name': 'backup_policy_name',
        'backup_policy_enabled': 'backup_policy_enabled',
        'resources_num': 'resources_num'
    }

    def __init__(self, project_id=None, enterprise_project_id=None, host_id=None, agent_id=None, host_name=None, host_ip=None, private_ip=None, os_type=None, os_name=None, host_status=None, ransom_protection_status=None, ransom_protection_fail_reason=None, failed_decoy_dir=None, agent_version=None, protect_status=None, group_id=None, group_name=None, protect_policy_id=None, protect_policy_name=None, backup_error=None, backup_protection_status=None, count_protect_event=None, count_backuped=None, agent_status=None, version=None, host_source=None, vault_id=None, vault_name=None, vault_size=None, vault_used=None, vault_allocated=None, vault_charging_mode=None, vault_status=None, backup_policy_id=None, backup_policy_name=None, backup_policy_enabled=None, resources_num=None):
        r"""ProtectionServerInfo

        The model defined in huaweicloud sdk

        :param project_id: **参数解释**: 项目ID **取值范围**: 字符长度0-128 
        :type project_id: str
        :param enterprise_project_id: **参数解释**: 企业项目ID **取值范围**: 字符长度0-128 
        :type enterprise_project_id: str
        :param host_id: **参数解释**: 服务器ID **取值范围**: 字符长度0-128 
        :type host_id: str
        :param agent_id: **参数解释**: Agent ID **取值范围**: 字符长度0-128 
        :type agent_id: str
        :param host_name: **参数解释**: 服务器名称 **取值范围**: 字符长度0-128 
        :type host_name: str
        :param host_ip: **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128 
        :type host_ip: str
        :param private_ip: **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128 
        :type private_ip: str
        :param os_type: **参数解释**: 操作系统类型 **取值范围**:   包含如下2种。     - Linux ：Linux。     - Windows ：Windows。
        :type os_type: str
        :param os_name: **参数解释**: 系统名称 **取值范围**: 字符长度0-128 
        :type os_name: str
        :param host_status: **参数解释**: 服务器状态 **取值范围**: 包含如下2种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。
        :type host_status: str
        :param ransom_protection_status: **参数解释**: 勒索防护状态 **取值范围**: 包含如下6种。   - closed ：未开启。   - opened ：防护中。   - opening ：开启中。   - closing ：关闭中。   - protect_failed：防护失败。   - protect_degraded：防护降级
        :type ransom_protection_status: str
        :param ransom_protection_fail_reason: **参数解释**: 勒索防护失败细分原因 **取值范围**: 包含如下4种。   - driver_load_failed ：驱动加载失败。   - protect_interrupted ：防护中断。   - decoy_deploy_totally_failed ：全部诱饵部署失败。   - decoy_deploy_partially_failed ：部分诱饵部署失败。
        :type ransom_protection_fail_reason: str
        :param failed_decoy_dir: **参数解释**: 诱饵防护失败的目录（仅部分诱饵部署失败状态有值） **取值范围**: 字符长度0-512 
        :type failed_decoy_dir: str
        :param agent_version: **参数解释**: agent版本 **取值范围**: 字符长度1-128 
        :type agent_version: str
        :param protect_status: **参数解释**: 防护状态 **取值范围**: 包含如下2种。 - closed ：未防护。 - opened ：防护中。
        :type protect_status: str
        :param group_id: **参数解释**: 服务器组ID **取值范围**: 字符长度1-128 
        :type group_id: str
        :param group_name: **参数解释**: 服务器组名称 **取值范围**: 字符长度1-128 
        :type group_name: str
        :param protect_policy_id: **参数解释**: 防护策略ID **取值范围**: 字符长度1-128 
        :type protect_policy_id: str
        :param protect_policy_name: **参数解释**: 防护策略名称 **取值范围**: 字符长度1-128 
        :type protect_policy_name: str
        :param backup_error: 
        :type backup_error: :class:`huaweicloudsdkhss.v5.ProtectionServerInfoBackupError`
        :param backup_protection_status: **参数解释**: 是否开启备份 **取值范围**: 包含如下3种。   - failed_to_turn_on_backup: 无法开启备份   - closed ：关闭。   - opened ：开启。
        :type backup_protection_status: str
        :param count_protect_event: **参数解释**: 防护事件数 **取值范围**: 取值0-2097152 
        :type count_protect_event: int
        :param count_backuped: **参数解释**: 已有备份数 **取值范围**: 取值0-2097152 
        :type count_backuped: int
        :param agent_status: **参数解释**: Agent状态 **取值范围**: 字符长度1-128 
        :type agent_status: str
        :param version: **参数解释**: 主机开通的版本    **取值范围**: 包含如下7种输入：   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。
        :type version: str
        :param host_source: **参数解释**: 服务器类型 **取值范围**: 包含如下3种输入：   - ecs ：弹性云服务器。   - outside ：线下主机。   - workspace ：云桌面。
        :type host_source: str
        :param vault_id: **参数解释**: 存储库ID **取值范围**: 字符长度0-128 
        :type vault_id: str
        :param vault_name: **参数解释**: 存储库名称 **取值范围**: 字符长度0-128 
        :type vault_name: str
        :param vault_size: **参数解释**: 总容量，单位GB **取值范围**: 取值0-2097152 
        :type vault_size: int
        :param vault_used: **参数解释**: 已使用容量，单位MB **取值范围**: 取值0-2097152 
        :type vault_used: int
        :param vault_allocated: **参数解释**: 已分配容量，单位GB，指绑定的服务器大小 **取值范围**: 取值0-2097152 
        :type vault_allocated: int
        :param vault_charging_mode: **参数解释**: 存储库创建模式 **取值范围**: 包含如下2种： - 按需：post_paid - 包周期：pre_paid 
        :type vault_charging_mode: str
        :param vault_status: **参数解释**: 存储库状态。 **取值范围**: 包含如下5种：   - available ：可用。   - lock ：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。
        :type vault_status: str
        :param backup_policy_id: **参数解释**: 备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用。 **取值范围**: 字符长度1-128 
        :type backup_policy_id: str
        :param backup_policy_name: **参数解释**: 备份策略名称 **取值范围**: 字符长度1-128 
        :type backup_policy_name: str
        :param backup_policy_enabled: **参数解释**: 策略是否启用 **取值范围**: 包含如下2种：   - true ：策略已启用。   - false ：策略未启用。 
        :type backup_policy_enabled: bool
        :param resources_num: **参数解释**: 已绑定服务器（个） **取值范围**: 取值0-2097152 
        :type resources_num: int
        """
        
        

        self._project_id = None
        self._enterprise_project_id = None
        self._host_id = None
        self._agent_id = None
        self._host_name = None
        self._host_ip = None
        self._private_ip = None
        self._os_type = None
        self._os_name = None
        self._host_status = None
        self._ransom_protection_status = None
        self._ransom_protection_fail_reason = None
        self._failed_decoy_dir = None
        self._agent_version = None
        self._protect_status = None
        self._group_id = None
        self._group_name = None
        self._protect_policy_id = None
        self._protect_policy_name = None
        self._backup_error = None
        self._backup_protection_status = None
        self._count_protect_event = None
        self._count_backuped = None
        self._agent_status = None
        self._version = None
        self._host_source = None
        self._vault_id = None
        self._vault_name = None
        self._vault_size = None
        self._vault_used = None
        self._vault_allocated = None
        self._vault_charging_mode = None
        self._vault_status = None
        self._backup_policy_id = None
        self._backup_policy_name = None
        self._backup_policy_enabled = None
        self._resources_num = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if host_id is not None:
            self.host_id = host_id
        if agent_id is not None:
            self.agent_id = agent_id
        if host_name is not None:
            self.host_name = host_name
        if host_ip is not None:
            self.host_ip = host_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if os_type is not None:
            self.os_type = os_type
        if os_name is not None:
            self.os_name = os_name
        if host_status is not None:
            self.host_status = host_status
        if ransom_protection_status is not None:
            self.ransom_protection_status = ransom_protection_status
        if ransom_protection_fail_reason is not None:
            self.ransom_protection_fail_reason = ransom_protection_fail_reason
        if failed_decoy_dir is not None:
            self.failed_decoy_dir = failed_decoy_dir
        if agent_version is not None:
            self.agent_version = agent_version
        if protect_status is not None:
            self.protect_status = protect_status
        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if protect_policy_id is not None:
            self.protect_policy_id = protect_policy_id
        if protect_policy_name is not None:
            self.protect_policy_name = protect_policy_name
        if backup_error is not None:
            self.backup_error = backup_error
        if backup_protection_status is not None:
            self.backup_protection_status = backup_protection_status
        if count_protect_event is not None:
            self.count_protect_event = count_protect_event
        if count_backuped is not None:
            self.count_backuped = count_backuped
        if agent_status is not None:
            self.agent_status = agent_status
        if version is not None:
            self.version = version
        if host_source is not None:
            self.host_source = host_source
        if vault_id is not None:
            self.vault_id = vault_id
        if vault_name is not None:
            self.vault_name = vault_name
        if vault_size is not None:
            self.vault_size = vault_size
        if vault_used is not None:
            self.vault_used = vault_used
        if vault_allocated is not None:
            self.vault_allocated = vault_allocated
        if vault_charging_mode is not None:
            self.vault_charging_mode = vault_charging_mode
        if vault_status is not None:
            self.vault_status = vault_status
        if backup_policy_id is not None:
            self.backup_policy_id = backup_policy_id
        if backup_policy_name is not None:
            self.backup_policy_name = backup_policy_name
        if backup_policy_enabled is not None:
            self.backup_policy_enabled = backup_policy_enabled
        if resources_num is not None:
            self.resources_num = resources_num

    @property
    def project_id(self):
        r"""Gets the project_id of this ProtectionServerInfo.

        **参数解释**: 项目ID **取值范围**: 字符长度0-128 

        :return: The project_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ProtectionServerInfo.

        **参数解释**: 项目ID **取值范围**: 字符长度0-128 

        :param project_id: The project_id of this ProtectionServerInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ProtectionServerInfo.

        **参数解释**: 企业项目ID **取值范围**: 字符长度0-128 

        :return: The enterprise_project_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ProtectionServerInfo.

        **参数解释**: 企业项目ID **取值范围**: 字符长度0-128 

        :param enterprise_project_id: The enterprise_project_id of this ProtectionServerInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ProtectionServerInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度0-128 

        :return: The host_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ProtectionServerInfo.

        **参数解释**: 服务器ID **取值范围**: 字符长度0-128 

        :param host_id: The host_id of this ProtectionServerInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        r"""Gets the agent_id of this ProtectionServerInfo.

        **参数解释**: Agent ID **取值范围**: 字符长度0-128 

        :return: The agent_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this ProtectionServerInfo.

        **参数解释**: Agent ID **取值范围**: 字符长度0-128 

        :param agent_id: The agent_id of this ProtectionServerInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ProtectionServerInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度0-128 

        :return: The host_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ProtectionServerInfo.

        **参数解释**: 服务器名称 **取值范围**: 字符长度0-128 

        :param host_name: The host_name of this ProtectionServerInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        r"""Gets the host_ip of this ProtectionServerInfo.

        **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128 

        :return: The host_ip of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        r"""Sets the host_ip of this ProtectionServerInfo.

        **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128 

        :param host_ip: The host_ip of this ProtectionServerInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ProtectionServerInfo.

        **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128 

        :return: The private_ip of this ProtectionServerInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ProtectionServerInfo.

        **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128 

        :param private_ip: The private_ip of this ProtectionServerInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def os_type(self):
        r"""Gets the os_type of this ProtectionServerInfo.

        **参数解释**: 操作系统类型 **取值范围**:   包含如下2种。     - Linux ：Linux。     - Windows ：Windows。

        :return: The os_type of this ProtectionServerInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ProtectionServerInfo.

        **参数解释**: 操作系统类型 **取值范围**:   包含如下2种。     - Linux ：Linux。     - Windows ：Windows。

        :param os_type: The os_type of this ProtectionServerInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        r"""Gets the os_name of this ProtectionServerInfo.

        **参数解释**: 系统名称 **取值范围**: 字符长度0-128 

        :return: The os_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this ProtectionServerInfo.

        **参数解释**: 系统名称 **取值范围**: 字符长度0-128 

        :param os_name: The os_name of this ProtectionServerInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def host_status(self):
        r"""Gets the host_status of this ProtectionServerInfo.

        **参数解释**: 服务器状态 **取值范围**: 包含如下2种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。

        :return: The host_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ProtectionServerInfo.

        **参数解释**: 服务器状态 **取值范围**: 包含如下2种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。

        :param host_status: The host_status of this ProtectionServerInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def ransom_protection_status(self):
        r"""Gets the ransom_protection_status of this ProtectionServerInfo.

        **参数解释**: 勒索防护状态 **取值范围**: 包含如下6种。   - closed ：未开启。   - opened ：防护中。   - opening ：开启中。   - closing ：关闭中。   - protect_failed：防护失败。   - protect_degraded：防护降级

        :return: The ransom_protection_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._ransom_protection_status

    @ransom_protection_status.setter
    def ransom_protection_status(self, ransom_protection_status):
        r"""Sets the ransom_protection_status of this ProtectionServerInfo.

        **参数解释**: 勒索防护状态 **取值范围**: 包含如下6种。   - closed ：未开启。   - opened ：防护中。   - opening ：开启中。   - closing ：关闭中。   - protect_failed：防护失败。   - protect_degraded：防护降级

        :param ransom_protection_status: The ransom_protection_status of this ProtectionServerInfo.
        :type ransom_protection_status: str
        """
        self._ransom_protection_status = ransom_protection_status

    @property
    def ransom_protection_fail_reason(self):
        r"""Gets the ransom_protection_fail_reason of this ProtectionServerInfo.

        **参数解释**: 勒索防护失败细分原因 **取值范围**: 包含如下4种。   - driver_load_failed ：驱动加载失败。   - protect_interrupted ：防护中断。   - decoy_deploy_totally_failed ：全部诱饵部署失败。   - decoy_deploy_partially_failed ：部分诱饵部署失败。

        :return: The ransom_protection_fail_reason of this ProtectionServerInfo.
        :rtype: str
        """
        return self._ransom_protection_fail_reason

    @ransom_protection_fail_reason.setter
    def ransom_protection_fail_reason(self, ransom_protection_fail_reason):
        r"""Sets the ransom_protection_fail_reason of this ProtectionServerInfo.

        **参数解释**: 勒索防护失败细分原因 **取值范围**: 包含如下4种。   - driver_load_failed ：驱动加载失败。   - protect_interrupted ：防护中断。   - decoy_deploy_totally_failed ：全部诱饵部署失败。   - decoy_deploy_partially_failed ：部分诱饵部署失败。

        :param ransom_protection_fail_reason: The ransom_protection_fail_reason of this ProtectionServerInfo.
        :type ransom_protection_fail_reason: str
        """
        self._ransom_protection_fail_reason = ransom_protection_fail_reason

    @property
    def failed_decoy_dir(self):
        r"""Gets the failed_decoy_dir of this ProtectionServerInfo.

        **参数解释**: 诱饵防护失败的目录（仅部分诱饵部署失败状态有值） **取值范围**: 字符长度0-512 

        :return: The failed_decoy_dir of this ProtectionServerInfo.
        :rtype: str
        """
        return self._failed_decoy_dir

    @failed_decoy_dir.setter
    def failed_decoy_dir(self, failed_decoy_dir):
        r"""Sets the failed_decoy_dir of this ProtectionServerInfo.

        **参数解释**: 诱饵防护失败的目录（仅部分诱饵部署失败状态有值） **取值范围**: 字符长度0-512 

        :param failed_decoy_dir: The failed_decoy_dir of this ProtectionServerInfo.
        :type failed_decoy_dir: str
        """
        self._failed_decoy_dir = failed_decoy_dir

    @property
    def agent_version(self):
        r"""Gets the agent_version of this ProtectionServerInfo.

        **参数解释**: agent版本 **取值范围**: 字符长度1-128 

        :return: The agent_version of this ProtectionServerInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this ProtectionServerInfo.

        **参数解释**: agent版本 **取值范围**: 字符长度1-128 

        :param agent_version: The agent_version of this ProtectionServerInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ProtectionServerInfo.

        **参数解释**: 防护状态 **取值范围**: 包含如下2种。 - closed ：未防护。 - opened ：防护中。

        :return: The protect_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ProtectionServerInfo.

        **参数解释**: 防护状态 **取值范围**: 包含如下2种。 - closed ：未防护。 - opened ：防护中。

        :param protect_status: The protect_status of this ProtectionServerInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def group_id(self):
        r"""Gets the group_id of this ProtectionServerInfo.

        **参数解释**: 服务器组ID **取值范围**: 字符长度1-128 

        :return: The group_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ProtectionServerInfo.

        **参数解释**: 服务器组ID **取值范围**: 字符长度1-128 

        :param group_id: The group_id of this ProtectionServerInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this ProtectionServerInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度1-128 

        :return: The group_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this ProtectionServerInfo.

        **参数解释**: 服务器组名称 **取值范围**: 字符长度1-128 

        :param group_name: The group_name of this ProtectionServerInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def protect_policy_id(self):
        r"""Gets the protect_policy_id of this ProtectionServerInfo.

        **参数解释**: 防护策略ID **取值范围**: 字符长度1-128 

        :return: The protect_policy_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._protect_policy_id

    @protect_policy_id.setter
    def protect_policy_id(self, protect_policy_id):
        r"""Sets the protect_policy_id of this ProtectionServerInfo.

        **参数解释**: 防护策略ID **取值范围**: 字符长度1-128 

        :param protect_policy_id: The protect_policy_id of this ProtectionServerInfo.
        :type protect_policy_id: str
        """
        self._protect_policy_id = protect_policy_id

    @property
    def protect_policy_name(self):
        r"""Gets the protect_policy_name of this ProtectionServerInfo.

        **参数解释**: 防护策略名称 **取值范围**: 字符长度1-128 

        :return: The protect_policy_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._protect_policy_name

    @protect_policy_name.setter
    def protect_policy_name(self, protect_policy_name):
        r"""Sets the protect_policy_name of this ProtectionServerInfo.

        **参数解释**: 防护策略名称 **取值范围**: 字符长度1-128 

        :param protect_policy_name: The protect_policy_name of this ProtectionServerInfo.
        :type protect_policy_name: str
        """
        self._protect_policy_name = protect_policy_name

    @property
    def backup_error(self):
        r"""Gets the backup_error of this ProtectionServerInfo.

        :return: The backup_error of this ProtectionServerInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ProtectionServerInfoBackupError`
        """
        return self._backup_error

    @backup_error.setter
    def backup_error(self, backup_error):
        r"""Sets the backup_error of this ProtectionServerInfo.

        :param backup_error: The backup_error of this ProtectionServerInfo.
        :type backup_error: :class:`huaweicloudsdkhss.v5.ProtectionServerInfoBackupError`
        """
        self._backup_error = backup_error

    @property
    def backup_protection_status(self):
        r"""Gets the backup_protection_status of this ProtectionServerInfo.

        **参数解释**: 是否开启备份 **取值范围**: 包含如下3种。   - failed_to_turn_on_backup: 无法开启备份   - closed ：关闭。   - opened ：开启。

        :return: The backup_protection_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._backup_protection_status

    @backup_protection_status.setter
    def backup_protection_status(self, backup_protection_status):
        r"""Sets the backup_protection_status of this ProtectionServerInfo.

        **参数解释**: 是否开启备份 **取值范围**: 包含如下3种。   - failed_to_turn_on_backup: 无法开启备份   - closed ：关闭。   - opened ：开启。

        :param backup_protection_status: The backup_protection_status of this ProtectionServerInfo.
        :type backup_protection_status: str
        """
        self._backup_protection_status = backup_protection_status

    @property
    def count_protect_event(self):
        r"""Gets the count_protect_event of this ProtectionServerInfo.

        **参数解释**: 防护事件数 **取值范围**: 取值0-2097152 

        :return: The count_protect_event of this ProtectionServerInfo.
        :rtype: int
        """
        return self._count_protect_event

    @count_protect_event.setter
    def count_protect_event(self, count_protect_event):
        r"""Sets the count_protect_event of this ProtectionServerInfo.

        **参数解释**: 防护事件数 **取值范围**: 取值0-2097152 

        :param count_protect_event: The count_protect_event of this ProtectionServerInfo.
        :type count_protect_event: int
        """
        self._count_protect_event = count_protect_event

    @property
    def count_backuped(self):
        r"""Gets the count_backuped of this ProtectionServerInfo.

        **参数解释**: 已有备份数 **取值范围**: 取值0-2097152 

        :return: The count_backuped of this ProtectionServerInfo.
        :rtype: int
        """
        return self._count_backuped

    @count_backuped.setter
    def count_backuped(self, count_backuped):
        r"""Sets the count_backuped of this ProtectionServerInfo.

        **参数解释**: 已有备份数 **取值范围**: 取值0-2097152 

        :param count_backuped: The count_backuped of this ProtectionServerInfo.
        :type count_backuped: int
        """
        self._count_backuped = count_backuped

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ProtectionServerInfo.

        **参数解释**: Agent状态 **取值范围**: 字符长度1-128 

        :return: The agent_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ProtectionServerInfo.

        **参数解释**: Agent状态 **取值范围**: 字符长度1-128 

        :param agent_status: The agent_status of this ProtectionServerInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def version(self):
        r"""Gets the version of this ProtectionServerInfo.

        **参数解释**: 主机开通的版本    **取值范围**: 包含如下7种输入：   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :return: The version of this ProtectionServerInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ProtectionServerInfo.

        **参数解释**: 主机开通的版本    **取值范围**: 包含如下7种输入：   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :param version: The version of this ProtectionServerInfo.
        :type version: str
        """
        self._version = version

    @property
    def host_source(self):
        r"""Gets the host_source of this ProtectionServerInfo.

        **参数解释**: 服务器类型 **取值范围**: 包含如下3种输入：   - ecs ：弹性云服务器。   - outside ：线下主机。   - workspace ：云桌面。

        :return: The host_source of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_source

    @host_source.setter
    def host_source(self, host_source):
        r"""Sets the host_source of this ProtectionServerInfo.

        **参数解释**: 服务器类型 **取值范围**: 包含如下3种输入：   - ecs ：弹性云服务器。   - outside ：线下主机。   - workspace ：云桌面。

        :param host_source: The host_source of this ProtectionServerInfo.
        :type host_source: str
        """
        self._host_source = host_source

    @property
    def vault_id(self):
        r"""Gets the vault_id of this ProtectionServerInfo.

        **参数解释**: 存储库ID **取值范围**: 字符长度0-128 

        :return: The vault_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this ProtectionServerInfo.

        **参数解释**: 存储库ID **取值范围**: 字符长度0-128 

        :param vault_id: The vault_id of this ProtectionServerInfo.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def vault_name(self):
        r"""Gets the vault_name of this ProtectionServerInfo.

        **参数解释**: 存储库名称 **取值范围**: 字符长度0-128 

        :return: The vault_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        r"""Sets the vault_name of this ProtectionServerInfo.

        **参数解释**: 存储库名称 **取值范围**: 字符长度0-128 

        :param vault_name: The vault_name of this ProtectionServerInfo.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def vault_size(self):
        r"""Gets the vault_size of this ProtectionServerInfo.

        **参数解释**: 总容量，单位GB **取值范围**: 取值0-2097152 

        :return: The vault_size of this ProtectionServerInfo.
        :rtype: int
        """
        return self._vault_size

    @vault_size.setter
    def vault_size(self, vault_size):
        r"""Sets the vault_size of this ProtectionServerInfo.

        **参数解释**: 总容量，单位GB **取值范围**: 取值0-2097152 

        :param vault_size: The vault_size of this ProtectionServerInfo.
        :type vault_size: int
        """
        self._vault_size = vault_size

    @property
    def vault_used(self):
        r"""Gets the vault_used of this ProtectionServerInfo.

        **参数解释**: 已使用容量，单位MB **取值范围**: 取值0-2097152 

        :return: The vault_used of this ProtectionServerInfo.
        :rtype: int
        """
        return self._vault_used

    @vault_used.setter
    def vault_used(self, vault_used):
        r"""Sets the vault_used of this ProtectionServerInfo.

        **参数解释**: 已使用容量，单位MB **取值范围**: 取值0-2097152 

        :param vault_used: The vault_used of this ProtectionServerInfo.
        :type vault_used: int
        """
        self._vault_used = vault_used

    @property
    def vault_allocated(self):
        r"""Gets the vault_allocated of this ProtectionServerInfo.

        **参数解释**: 已分配容量，单位GB，指绑定的服务器大小 **取值范围**: 取值0-2097152 

        :return: The vault_allocated of this ProtectionServerInfo.
        :rtype: int
        """
        return self._vault_allocated

    @vault_allocated.setter
    def vault_allocated(self, vault_allocated):
        r"""Sets the vault_allocated of this ProtectionServerInfo.

        **参数解释**: 已分配容量，单位GB，指绑定的服务器大小 **取值范围**: 取值0-2097152 

        :param vault_allocated: The vault_allocated of this ProtectionServerInfo.
        :type vault_allocated: int
        """
        self._vault_allocated = vault_allocated

    @property
    def vault_charging_mode(self):
        r"""Gets the vault_charging_mode of this ProtectionServerInfo.

        **参数解释**: 存储库创建模式 **取值范围**: 包含如下2种： - 按需：post_paid - 包周期：pre_paid 

        :return: The vault_charging_mode of this ProtectionServerInfo.
        :rtype: str
        """
        return self._vault_charging_mode

    @vault_charging_mode.setter
    def vault_charging_mode(self, vault_charging_mode):
        r"""Sets the vault_charging_mode of this ProtectionServerInfo.

        **参数解释**: 存储库创建模式 **取值范围**: 包含如下2种： - 按需：post_paid - 包周期：pre_paid 

        :param vault_charging_mode: The vault_charging_mode of this ProtectionServerInfo.
        :type vault_charging_mode: str
        """
        self._vault_charging_mode = vault_charging_mode

    @property
    def vault_status(self):
        r"""Gets the vault_status of this ProtectionServerInfo.

        **参数解释**: 存储库状态。 **取值范围**: 包含如下5种：   - available ：可用。   - lock ：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。

        :return: The vault_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._vault_status

    @vault_status.setter
    def vault_status(self, vault_status):
        r"""Sets the vault_status of this ProtectionServerInfo.

        **参数解释**: 存储库状态。 **取值范围**: 包含如下5种：   - available ：可用。   - lock ：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。

        :param vault_status: The vault_status of this ProtectionServerInfo.
        :type vault_status: str
        """
        self._vault_status = vault_status

    @property
    def backup_policy_id(self):
        r"""Gets the backup_policy_id of this ProtectionServerInfo.

        **参数解释**: 备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用。 **取值范围**: 字符长度1-128 

        :return: The backup_policy_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        r"""Sets the backup_policy_id of this ProtectionServerInfo.

        **参数解释**: 备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用。 **取值范围**: 字符长度1-128 

        :param backup_policy_id: The backup_policy_id of this ProtectionServerInfo.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def backup_policy_name(self):
        r"""Gets the backup_policy_name of this ProtectionServerInfo.

        **参数解释**: 备份策略名称 **取值范围**: 字符长度1-128 

        :return: The backup_policy_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._backup_policy_name

    @backup_policy_name.setter
    def backup_policy_name(self, backup_policy_name):
        r"""Sets the backup_policy_name of this ProtectionServerInfo.

        **参数解释**: 备份策略名称 **取值范围**: 字符长度1-128 

        :param backup_policy_name: The backup_policy_name of this ProtectionServerInfo.
        :type backup_policy_name: str
        """
        self._backup_policy_name = backup_policy_name

    @property
    def backup_policy_enabled(self):
        r"""Gets the backup_policy_enabled of this ProtectionServerInfo.

        **参数解释**: 策略是否启用 **取值范围**: 包含如下2种：   - true ：策略已启用。   - false ：策略未启用。 

        :return: The backup_policy_enabled of this ProtectionServerInfo.
        :rtype: bool
        """
        return self._backup_policy_enabled

    @backup_policy_enabled.setter
    def backup_policy_enabled(self, backup_policy_enabled):
        r"""Sets the backup_policy_enabled of this ProtectionServerInfo.

        **参数解释**: 策略是否启用 **取值范围**: 包含如下2种：   - true ：策略已启用。   - false ：策略未启用。 

        :param backup_policy_enabled: The backup_policy_enabled of this ProtectionServerInfo.
        :type backup_policy_enabled: bool
        """
        self._backup_policy_enabled = backup_policy_enabled

    @property
    def resources_num(self):
        r"""Gets the resources_num of this ProtectionServerInfo.

        **参数解释**: 已绑定服务器（个） **取值范围**: 取值0-2097152 

        :return: The resources_num of this ProtectionServerInfo.
        :rtype: int
        """
        return self._resources_num

    @resources_num.setter
    def resources_num(self, resources_num):
        r"""Sets the resources_num of this ProtectionServerInfo.

        **参数解释**: 已绑定服务器（个） **取值范围**: 取值0-2097152 

        :param resources_num: The resources_num of this ProtectionServerInfo.
        :type resources_num: int
        """
        self._resources_num = resources_num

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
        if not isinstance(other, ProtectionServerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
