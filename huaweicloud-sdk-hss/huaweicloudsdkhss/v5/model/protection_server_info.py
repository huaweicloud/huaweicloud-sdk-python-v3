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
        'host_id': 'str',
        'agent_id': 'str',
        'host_name': 'str',
        'host_ip': 'str',
        'private_ip': 'str',
        'os_type': 'str',
        'os_name': 'str',
        'host_status': 'str',
        'ransom_protection_status': 'str',
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
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'private_ip': 'private_ip',
        'os_type': 'os_type',
        'os_name': 'os_name',
        'host_status': 'host_status',
        'ransom_protection_status': 'ransom_protection_status',
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

    def __init__(self, host_id=None, agent_id=None, host_name=None, host_ip=None, private_ip=None, os_type=None, os_name=None, host_status=None, ransom_protection_status=None, agent_version=None, protect_status=None, group_id=None, group_name=None, protect_policy_id=None, protect_policy_name=None, backup_error=None, backup_protection_status=None, count_protect_event=None, count_backuped=None, agent_status=None, version=None, host_source=None, vault_id=None, vault_name=None, vault_size=None, vault_used=None, vault_allocated=None, vault_charging_mode=None, vault_status=None, backup_policy_id=None, backup_policy_name=None, backup_policy_enabled=None, resources_num=None):
        """ProtectionServerInfo

        The model defined in huaweicloud sdk

        :param host_id: 服务器ID
        :type host_id: str
        :param agent_id: Agent ID
        :type agent_id: str
        :param host_name: 服务器名称
        :type host_name: str
        :param host_ip: 弹性公网IP地址
        :type host_ip: str
        :param private_ip: 私有IP地址
        :type private_ip: str
        :param os_type: 操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。
        :type os_type: str
        :param os_name: 系统名称
        :type os_name: str
        :param host_status: 服务器状态，包含如下2种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。
        :type host_status: str
        :param ransom_protection_status: 勒索防护状态，包含如下4种。   - closed ：关闭。   - opened ：开启。   - opening ：开启中。   - closing ：关闭中。
        :type ransom_protection_status: str
        :param agent_version: agent版本
        :type agent_version: str
        :param protect_status: 防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。
        :type protect_status: str
        :param group_id: 服务器组ID
        :type group_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param protect_policy_id: 防护策略ID
        :type protect_policy_id: str
        :param protect_policy_name: 防护策略名称
        :type protect_policy_name: str
        :param backup_error: 
        :type backup_error: :class:`huaweicloudsdkhss.v5.ProtectionServerInfoBackupError`
        :param backup_protection_status: 是否开启备份，包含如下3种。   - failed_to_turn_on_backup: 无法开启备份   - closed ：关闭。   - opened ：开启。
        :type backup_protection_status: str
        :param count_protect_event: 防护事件数
        :type count_protect_event: int
        :param count_backuped: 已有备份数
        :type count_backuped: int
        :param agent_status: Agent状态
        :type agent_status: str
        :param version: 主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。
        :type version: str
        :param host_source: 服务器类型，包含如下3种输入。   - ecs ：ecs。   - outside ：线下主机。   - workspace ：云桌面。
        :type host_source: str
        :param vault_id: 存储库ID
        :type vault_id: str
        :param vault_name: 存储库名称
        :type vault_name: str
        :param vault_size: 总容量，单位GB
        :type vault_size: int
        :param vault_used: 已使用容量，单位MB
        :type vault_used: int
        :param vault_allocated: 已分配容量，单位GB，指绑定的服务器大小
        :type vault_allocated: int
        :param vault_charging_mode: 存储库创建模式，按需：post_paid，包周期：pre_paid
        :type vault_charging_mode: str
        :param vault_status: 存储库状态。   - available ：可用。   - lock ：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。
        :type vault_status: str
        :param backup_policy_id: 备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用
        :type backup_policy_id: str
        :param backup_policy_name: 备份策略名称
        :type backup_policy_name: str
        :param backup_policy_enabled: 策略是否启用
        :type backup_policy_enabled: bool
        :param resources_num: 已绑定服务器（个）
        :type resources_num: int
        """
        
        

        self._host_id = None
        self._agent_id = None
        self._host_name = None
        self._host_ip = None
        self._private_ip = None
        self._os_type = None
        self._os_name = None
        self._host_status = None
        self._ransom_protection_status = None
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
    def host_id(self):
        """Gets the host_id of this ProtectionServerInfo.

        服务器ID

        :return: The host_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ProtectionServerInfo.

        服务器ID

        :param host_id: The host_id of this ProtectionServerInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def agent_id(self):
        """Gets the agent_id of this ProtectionServerInfo.

        Agent ID

        :return: The agent_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this ProtectionServerInfo.

        Agent ID

        :param agent_id: The agent_id of this ProtectionServerInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def host_name(self):
        """Gets the host_name of this ProtectionServerInfo.

        服务器名称

        :return: The host_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this ProtectionServerInfo.

        服务器名称

        :param host_name: The host_name of this ProtectionServerInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_ip(self):
        """Gets the host_ip of this ProtectionServerInfo.

        弹性公网IP地址

        :return: The host_ip of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_ip

    @host_ip.setter
    def host_ip(self, host_ip):
        """Sets the host_ip of this ProtectionServerInfo.

        弹性公网IP地址

        :param host_ip: The host_ip of this ProtectionServerInfo.
        :type host_ip: str
        """
        self._host_ip = host_ip

    @property
    def private_ip(self):
        """Gets the private_ip of this ProtectionServerInfo.

        私有IP地址

        :return: The private_ip of this ProtectionServerInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ProtectionServerInfo.

        私有IP地址

        :param private_ip: The private_ip of this ProtectionServerInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def os_type(self):
        """Gets the os_type of this ProtectionServerInfo.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :return: The os_type of this ProtectionServerInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ProtectionServerInfo.

        操作系统类型，包含如下2种。   - Linux ：Linux。   - Windows ：Windows。

        :param os_type: The os_type of this ProtectionServerInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_name(self):
        """Gets the os_name of this ProtectionServerInfo.

        系统名称

        :return: The os_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this ProtectionServerInfo.

        系统名称

        :param os_name: The os_name of this ProtectionServerInfo.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def host_status(self):
        """Gets the host_status of this ProtectionServerInfo.

        服务器状态，包含如下2种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。

        :return: The host_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ProtectionServerInfo.

        服务器状态，包含如下2种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。

        :param host_status: The host_status of this ProtectionServerInfo.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def ransom_protection_status(self):
        """Gets the ransom_protection_status of this ProtectionServerInfo.

        勒索防护状态，包含如下4种。   - closed ：关闭。   - opened ：开启。   - opening ：开启中。   - closing ：关闭中。

        :return: The ransom_protection_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._ransom_protection_status

    @ransom_protection_status.setter
    def ransom_protection_status(self, ransom_protection_status):
        """Sets the ransom_protection_status of this ProtectionServerInfo.

        勒索防护状态，包含如下4种。   - closed ：关闭。   - opened ：开启。   - opening ：开启中。   - closing ：关闭中。

        :param ransom_protection_status: The ransom_protection_status of this ProtectionServerInfo.
        :type ransom_protection_status: str
        """
        self._ransom_protection_status = ransom_protection_status

    @property
    def agent_version(self):
        """Gets the agent_version of this ProtectionServerInfo.

        agent版本

        :return: The agent_version of this ProtectionServerInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        """Sets the agent_version of this ProtectionServerInfo.

        agent版本

        :param agent_version: The agent_version of this ProtectionServerInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def protect_status(self):
        """Gets the protect_status of this ProtectionServerInfo.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。

        :return: The protect_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ProtectionServerInfo.

        防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。

        :param protect_status: The protect_status of this ProtectionServerInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def group_id(self):
        """Gets the group_id of this ProtectionServerInfo.

        服务器组ID

        :return: The group_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ProtectionServerInfo.

        服务器组ID

        :param group_id: The group_id of this ProtectionServerInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        """Gets the group_name of this ProtectionServerInfo.

        服务器组名称

        :return: The group_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ProtectionServerInfo.

        服务器组名称

        :param group_name: The group_name of this ProtectionServerInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def protect_policy_id(self):
        """Gets the protect_policy_id of this ProtectionServerInfo.

        防护策略ID

        :return: The protect_policy_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._protect_policy_id

    @protect_policy_id.setter
    def protect_policy_id(self, protect_policy_id):
        """Sets the protect_policy_id of this ProtectionServerInfo.

        防护策略ID

        :param protect_policy_id: The protect_policy_id of this ProtectionServerInfo.
        :type protect_policy_id: str
        """
        self._protect_policy_id = protect_policy_id

    @property
    def protect_policy_name(self):
        """Gets the protect_policy_name of this ProtectionServerInfo.

        防护策略名称

        :return: The protect_policy_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._protect_policy_name

    @protect_policy_name.setter
    def protect_policy_name(self, protect_policy_name):
        """Sets the protect_policy_name of this ProtectionServerInfo.

        防护策略名称

        :param protect_policy_name: The protect_policy_name of this ProtectionServerInfo.
        :type protect_policy_name: str
        """
        self._protect_policy_name = protect_policy_name

    @property
    def backup_error(self):
        """Gets the backup_error of this ProtectionServerInfo.

        :return: The backup_error of this ProtectionServerInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ProtectionServerInfoBackupError`
        """
        return self._backup_error

    @backup_error.setter
    def backup_error(self, backup_error):
        """Sets the backup_error of this ProtectionServerInfo.

        :param backup_error: The backup_error of this ProtectionServerInfo.
        :type backup_error: :class:`huaweicloudsdkhss.v5.ProtectionServerInfoBackupError`
        """
        self._backup_error = backup_error

    @property
    def backup_protection_status(self):
        """Gets the backup_protection_status of this ProtectionServerInfo.

        是否开启备份，包含如下3种。   - failed_to_turn_on_backup: 无法开启备份   - closed ：关闭。   - opened ：开启。

        :return: The backup_protection_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._backup_protection_status

    @backup_protection_status.setter
    def backup_protection_status(self, backup_protection_status):
        """Sets the backup_protection_status of this ProtectionServerInfo.

        是否开启备份，包含如下3种。   - failed_to_turn_on_backup: 无法开启备份   - closed ：关闭。   - opened ：开启。

        :param backup_protection_status: The backup_protection_status of this ProtectionServerInfo.
        :type backup_protection_status: str
        """
        self._backup_protection_status = backup_protection_status

    @property
    def count_protect_event(self):
        """Gets the count_protect_event of this ProtectionServerInfo.

        防护事件数

        :return: The count_protect_event of this ProtectionServerInfo.
        :rtype: int
        """
        return self._count_protect_event

    @count_protect_event.setter
    def count_protect_event(self, count_protect_event):
        """Sets the count_protect_event of this ProtectionServerInfo.

        防护事件数

        :param count_protect_event: The count_protect_event of this ProtectionServerInfo.
        :type count_protect_event: int
        """
        self._count_protect_event = count_protect_event

    @property
    def count_backuped(self):
        """Gets the count_backuped of this ProtectionServerInfo.

        已有备份数

        :return: The count_backuped of this ProtectionServerInfo.
        :rtype: int
        """
        return self._count_backuped

    @count_backuped.setter
    def count_backuped(self, count_backuped):
        """Sets the count_backuped of this ProtectionServerInfo.

        已有备份数

        :param count_backuped: The count_backuped of this ProtectionServerInfo.
        :type count_backuped: int
        """
        self._count_backuped = count_backuped

    @property
    def agent_status(self):
        """Gets the agent_status of this ProtectionServerInfo.

        Agent状态

        :return: The agent_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        """Sets the agent_status of this ProtectionServerInfo.

        Agent状态

        :param agent_status: The agent_status of this ProtectionServerInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def version(self):
        """Gets the version of this ProtectionServerInfo.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :return: The version of this ProtectionServerInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProtectionServerInfo.

        主机开通的版本，包含如下7种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.advanced ：专业版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise ：容器版。

        :param version: The version of this ProtectionServerInfo.
        :type version: str
        """
        self._version = version

    @property
    def host_source(self):
        """Gets the host_source of this ProtectionServerInfo.

        服务器类型，包含如下3种输入。   - ecs ：ecs。   - outside ：线下主机。   - workspace ：云桌面。

        :return: The host_source of this ProtectionServerInfo.
        :rtype: str
        """
        return self._host_source

    @host_source.setter
    def host_source(self, host_source):
        """Sets the host_source of this ProtectionServerInfo.

        服务器类型，包含如下3种输入。   - ecs ：ecs。   - outside ：线下主机。   - workspace ：云桌面。

        :param host_source: The host_source of this ProtectionServerInfo.
        :type host_source: str
        """
        self._host_source = host_source

    @property
    def vault_id(self):
        """Gets the vault_id of this ProtectionServerInfo.

        存储库ID

        :return: The vault_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this ProtectionServerInfo.

        存储库ID

        :param vault_id: The vault_id of this ProtectionServerInfo.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def vault_name(self):
        """Gets the vault_name of this ProtectionServerInfo.

        存储库名称

        :return: The vault_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._vault_name

    @vault_name.setter
    def vault_name(self, vault_name):
        """Sets the vault_name of this ProtectionServerInfo.

        存储库名称

        :param vault_name: The vault_name of this ProtectionServerInfo.
        :type vault_name: str
        """
        self._vault_name = vault_name

    @property
    def vault_size(self):
        """Gets the vault_size of this ProtectionServerInfo.

        总容量，单位GB

        :return: The vault_size of this ProtectionServerInfo.
        :rtype: int
        """
        return self._vault_size

    @vault_size.setter
    def vault_size(self, vault_size):
        """Sets the vault_size of this ProtectionServerInfo.

        总容量，单位GB

        :param vault_size: The vault_size of this ProtectionServerInfo.
        :type vault_size: int
        """
        self._vault_size = vault_size

    @property
    def vault_used(self):
        """Gets the vault_used of this ProtectionServerInfo.

        已使用容量，单位MB

        :return: The vault_used of this ProtectionServerInfo.
        :rtype: int
        """
        return self._vault_used

    @vault_used.setter
    def vault_used(self, vault_used):
        """Sets the vault_used of this ProtectionServerInfo.

        已使用容量，单位MB

        :param vault_used: The vault_used of this ProtectionServerInfo.
        :type vault_used: int
        """
        self._vault_used = vault_used

    @property
    def vault_allocated(self):
        """Gets the vault_allocated of this ProtectionServerInfo.

        已分配容量，单位GB，指绑定的服务器大小

        :return: The vault_allocated of this ProtectionServerInfo.
        :rtype: int
        """
        return self._vault_allocated

    @vault_allocated.setter
    def vault_allocated(self, vault_allocated):
        """Sets the vault_allocated of this ProtectionServerInfo.

        已分配容量，单位GB，指绑定的服务器大小

        :param vault_allocated: The vault_allocated of this ProtectionServerInfo.
        :type vault_allocated: int
        """
        self._vault_allocated = vault_allocated

    @property
    def vault_charging_mode(self):
        """Gets the vault_charging_mode of this ProtectionServerInfo.

        存储库创建模式，按需：post_paid，包周期：pre_paid

        :return: The vault_charging_mode of this ProtectionServerInfo.
        :rtype: str
        """
        return self._vault_charging_mode

    @vault_charging_mode.setter
    def vault_charging_mode(self, vault_charging_mode):
        """Sets the vault_charging_mode of this ProtectionServerInfo.

        存储库创建模式，按需：post_paid，包周期：pre_paid

        :param vault_charging_mode: The vault_charging_mode of this ProtectionServerInfo.
        :type vault_charging_mode: str
        """
        self._vault_charging_mode = vault_charging_mode

    @property
    def vault_status(self):
        """Gets the vault_status of this ProtectionServerInfo.

        存储库状态。   - available ：可用。   - lock ：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。

        :return: The vault_status of this ProtectionServerInfo.
        :rtype: str
        """
        return self._vault_status

    @vault_status.setter
    def vault_status(self, vault_status):
        """Sets the vault_status of this ProtectionServerInfo.

        存储库状态。   - available ：可用。   - lock ：被锁定。   - frozen：冻结。   - deleting：删除中。   - error：错误。

        :param vault_status: The vault_status of this ProtectionServerInfo.
        :type vault_status: str
        """
        self._vault_status = vault_status

    @property
    def backup_policy_id(self):
        """Gets the backup_policy_id of this ProtectionServerInfo.

        备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用

        :return: The backup_policy_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        """Sets the backup_policy_id of this ProtectionServerInfo.

        备份策略ID，若为空，则为未绑定状态，若不为空，通过backup_policy_enabled字段判断策略是否启用

        :param backup_policy_id: The backup_policy_id of this ProtectionServerInfo.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def backup_policy_name(self):
        """Gets the backup_policy_name of this ProtectionServerInfo.

        备份策略名称

        :return: The backup_policy_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._backup_policy_name

    @backup_policy_name.setter
    def backup_policy_name(self, backup_policy_name):
        """Sets the backup_policy_name of this ProtectionServerInfo.

        备份策略名称

        :param backup_policy_name: The backup_policy_name of this ProtectionServerInfo.
        :type backup_policy_name: str
        """
        self._backup_policy_name = backup_policy_name

    @property
    def backup_policy_enabled(self):
        """Gets the backup_policy_enabled of this ProtectionServerInfo.

        策略是否启用

        :return: The backup_policy_enabled of this ProtectionServerInfo.
        :rtype: bool
        """
        return self._backup_policy_enabled

    @backup_policy_enabled.setter
    def backup_policy_enabled(self, backup_policy_enabled):
        """Sets the backup_policy_enabled of this ProtectionServerInfo.

        策略是否启用

        :param backup_policy_enabled: The backup_policy_enabled of this ProtectionServerInfo.
        :type backup_policy_enabled: bool
        """
        self._backup_policy_enabled = backup_policy_enabled

    @property
    def resources_num(self):
        """Gets the resources_num of this ProtectionServerInfo.

        已绑定服务器（个）

        :return: The resources_num of this ProtectionServerInfo.
        :rtype: int
        """
        return self._resources_num

    @resources_num.setter
    def resources_num(self, resources_num):
        """Sets the resources_num of this ProtectionServerInfo.

        已绑定服务器（个）

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
