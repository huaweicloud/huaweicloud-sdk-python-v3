# coding: utf-8

import re
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
        'host_status': 'str',
        'ransom_protection_status': 'str',
        'protect_status': 'str',
        'group_id': 'str',
        'group_name': 'str',
        'protect_policy_id': 'str',
        'protect_policy_name': 'str',
        'backup_error': 'ProtectionServerInfoBackupError',
        'backup_protection_status': 'str',
        'count_protect_event': 'int',
        'count_backuped': 'int'
    }

    attribute_map = {
        'host_id': 'host_id',
        'agent_id': 'agent_id',
        'host_name': 'host_name',
        'host_ip': 'host_ip',
        'private_ip': 'private_ip',
        'os_type': 'os_type',
        'host_status': 'host_status',
        'ransom_protection_status': 'ransom_protection_status',
        'protect_status': 'protect_status',
        'group_id': 'group_id',
        'group_name': 'group_name',
        'protect_policy_id': 'protect_policy_id',
        'protect_policy_name': 'protect_policy_name',
        'backup_error': 'backup_error',
        'backup_protection_status': 'backup_protection_status',
        'count_protect_event': 'count_protect_event',
        'count_backuped': 'count_backuped'
    }

    def __init__(self, host_id=None, agent_id=None, host_name=None, host_ip=None, private_ip=None, os_type=None, host_status=None, ransom_protection_status=None, protect_status=None, group_id=None, group_name=None, protect_policy_id=None, protect_policy_name=None, backup_error=None, backup_protection_status=None, count_protect_event=None, count_backuped=None):
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
        :param host_status: 服务器状态，包含如下2种。   - ACTIVE ：运行中。   - SHUTOFF ：关机。
        :type host_status: str
        :param ransom_protection_status: 勒索防护状态，包含如下4种。   - closed ：关闭。   - opened ：开启。   - opening ：开启中。   - closing ：关闭中。
        :type ransom_protection_status: str
        :param protect_status: 防护状态，包含如下2种。 - closed ：未防护。 - opened ：防护中。
        :type protect_status: str
        :param group_id: 服务器组ID
        :type group_id: str
        :param group_name: 服务器组名称
        :type group_name: str
        :param protect_policy_id: 策略ID
        :type protect_policy_id: str
        :param protect_policy_name: 策略名称
        :type protect_policy_name: str
        :param backup_error: 
        :type backup_error: :class:`huaweicloudsdkhss.v5.ProtectionServerInfoBackupError`
        :param backup_protection_status: 是否开启备份，包含如下3种。   - failed_to_turn_on_backup: 无法开启备份   - closed ：关闭。   - opened ：开启。
        :type backup_protection_status: str
        :param count_protect_event: 防护事件数
        :type count_protect_event: int
        :param count_backuped: 已有备份数
        :type count_backuped: int
        """
        
        

        self._host_id = None
        self._agent_id = None
        self._host_name = None
        self._host_ip = None
        self._private_ip = None
        self._os_type = None
        self._host_status = None
        self._ransom_protection_status = None
        self._protect_status = None
        self._group_id = None
        self._group_name = None
        self._protect_policy_id = None
        self._protect_policy_name = None
        self._backup_error = None
        self._backup_protection_status = None
        self._count_protect_event = None
        self._count_backuped = None
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
        if host_status is not None:
            self.host_status = host_status
        if ransom_protection_status is not None:
            self.ransom_protection_status = ransom_protection_status
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

        策略ID

        :return: The protect_policy_id of this ProtectionServerInfo.
        :rtype: str
        """
        return self._protect_policy_id

    @protect_policy_id.setter
    def protect_policy_id(self, protect_policy_id):
        """Sets the protect_policy_id of this ProtectionServerInfo.

        策略ID

        :param protect_policy_id: The protect_policy_id of this ProtectionServerInfo.
        :type protect_policy_id: str
        """
        self._protect_policy_id = protect_policy_id

    @property
    def protect_policy_name(self):
        """Gets the protect_policy_name of this ProtectionServerInfo.

        策略名称

        :return: The protect_policy_name of this ProtectionServerInfo.
        :rtype: str
        """
        return self._protect_policy_name

    @protect_policy_name.setter
    def protect_policy_name(self, protect_policy_name):
        """Sets the protect_policy_name of this ProtectionServerInfo.

        策略名称

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
