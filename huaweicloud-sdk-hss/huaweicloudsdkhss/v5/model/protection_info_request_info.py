# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionInfoRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operating_system': 'str',
        'ransom_protection_status': 'str',
        'protection_policy_id': 'str',
        'create_protection_policy': 'ProtectionProxyInfoRequestInfo',
        'backup_protection_status': 'str',
        'backup_policy_id': 'str',
        'backup_cycle': 'UpdateBackupPolicyRequestInfo',
        'agent_id_list': 'list[str]',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'operating_system': 'operating_system',
        'ransom_protection_status': 'ransom_protection_status',
        'protection_policy_id': 'protection_policy_id',
        'create_protection_policy': 'create_protection_policy',
        'backup_protection_status': 'backup_protection_status',
        'backup_policy_id': 'backup_policy_id',
        'backup_cycle': 'backup_cycle',
        'agent_id_list': 'agent_id_list',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, operating_system=None, ransom_protection_status=None, protection_policy_id=None, create_protection_policy=None, backup_protection_status=None, backup_policy_id=None, backup_cycle=None, agent_id_list=None, host_id_list=None):
        """ProtectionInfoRequestInfo

        The model defined in huaweicloud sdk

        :param operating_system: 操作系统，包含如下：   - Windows : 无需处理   - Linux : 已忽略
        :type operating_system: str
        :param ransom_protection_status: 勒索防护是否开启，包含如下：   - closed ：关闭。   - opened ：开启。
        :type ransom_protection_status: str
        :param protection_policy_id: 防护策略ID
        :type protection_policy_id: str
        :param create_protection_policy: 
        :type create_protection_policy: :class:`huaweicloudsdkhss.v5.ProtectionProxyInfoRequestInfo`
        :param backup_protection_status: 是否服务器备份，包含如下：   - closed ：关闭。   - opened ：开启。
        :type backup_protection_status: str
        :param backup_policy_id: 备份策略ID
        :type backup_policy_id: str
        :param backup_cycle: 
        :type backup_cycle: :class:`huaweicloudsdkhss.v5.UpdateBackupPolicyRequestInfo`
        :param agent_id_list: 开启防护的Agent id列表
        :type agent_id_list: list[str]
        :param host_id_list: 开启防护的host id列表
        :type host_id_list: list[str]
        """
        
        

        self._operating_system = None
        self._ransom_protection_status = None
        self._protection_policy_id = None
        self._create_protection_policy = None
        self._backup_protection_status = None
        self._backup_policy_id = None
        self._backup_cycle = None
        self._agent_id_list = None
        self._host_id_list = None
        self.discriminator = None

        if operating_system is not None:
            self.operating_system = operating_system
        if ransom_protection_status is not None:
            self.ransom_protection_status = ransom_protection_status
        if protection_policy_id is not None:
            self.protection_policy_id = protection_policy_id
        if create_protection_policy is not None:
            self.create_protection_policy = create_protection_policy
        if backup_protection_status is not None:
            self.backup_protection_status = backup_protection_status
        if backup_policy_id is not None:
            self.backup_policy_id = backup_policy_id
        if backup_cycle is not None:
            self.backup_cycle = backup_cycle
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def operating_system(self):
        """Gets the operating_system of this ProtectionInfoRequestInfo.

        操作系统，包含如下：   - Windows : 无需处理   - Linux : 已忽略

        :return: The operating_system of this ProtectionInfoRequestInfo.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this ProtectionInfoRequestInfo.

        操作系统，包含如下：   - Windows : 无需处理   - Linux : 已忽略

        :param operating_system: The operating_system of this ProtectionInfoRequestInfo.
        :type operating_system: str
        """
        self._operating_system = operating_system

    @property
    def ransom_protection_status(self):
        """Gets the ransom_protection_status of this ProtectionInfoRequestInfo.

        勒索防护是否开启，包含如下：   - closed ：关闭。   - opened ：开启。

        :return: The ransom_protection_status of this ProtectionInfoRequestInfo.
        :rtype: str
        """
        return self._ransom_protection_status

    @ransom_protection_status.setter
    def ransom_protection_status(self, ransom_protection_status):
        """Sets the ransom_protection_status of this ProtectionInfoRequestInfo.

        勒索防护是否开启，包含如下：   - closed ：关闭。   - opened ：开启。

        :param ransom_protection_status: The ransom_protection_status of this ProtectionInfoRequestInfo.
        :type ransom_protection_status: str
        """
        self._ransom_protection_status = ransom_protection_status

    @property
    def protection_policy_id(self):
        """Gets the protection_policy_id of this ProtectionInfoRequestInfo.

        防护策略ID

        :return: The protection_policy_id of this ProtectionInfoRequestInfo.
        :rtype: str
        """
        return self._protection_policy_id

    @protection_policy_id.setter
    def protection_policy_id(self, protection_policy_id):
        """Sets the protection_policy_id of this ProtectionInfoRequestInfo.

        防护策略ID

        :param protection_policy_id: The protection_policy_id of this ProtectionInfoRequestInfo.
        :type protection_policy_id: str
        """
        self._protection_policy_id = protection_policy_id

    @property
    def create_protection_policy(self):
        """Gets the create_protection_policy of this ProtectionInfoRequestInfo.

        :return: The create_protection_policy of this ProtectionInfoRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ProtectionProxyInfoRequestInfo`
        """
        return self._create_protection_policy

    @create_protection_policy.setter
    def create_protection_policy(self, create_protection_policy):
        """Sets the create_protection_policy of this ProtectionInfoRequestInfo.

        :param create_protection_policy: The create_protection_policy of this ProtectionInfoRequestInfo.
        :type create_protection_policy: :class:`huaweicloudsdkhss.v5.ProtectionProxyInfoRequestInfo`
        """
        self._create_protection_policy = create_protection_policy

    @property
    def backup_protection_status(self):
        """Gets the backup_protection_status of this ProtectionInfoRequestInfo.

        是否服务器备份，包含如下：   - closed ：关闭。   - opened ：开启。

        :return: The backup_protection_status of this ProtectionInfoRequestInfo.
        :rtype: str
        """
        return self._backup_protection_status

    @backup_protection_status.setter
    def backup_protection_status(self, backup_protection_status):
        """Sets the backup_protection_status of this ProtectionInfoRequestInfo.

        是否服务器备份，包含如下：   - closed ：关闭。   - opened ：开启。

        :param backup_protection_status: The backup_protection_status of this ProtectionInfoRequestInfo.
        :type backup_protection_status: str
        """
        self._backup_protection_status = backup_protection_status

    @property
    def backup_policy_id(self):
        """Gets the backup_policy_id of this ProtectionInfoRequestInfo.

        备份策略ID

        :return: The backup_policy_id of this ProtectionInfoRequestInfo.
        :rtype: str
        """
        return self._backup_policy_id

    @backup_policy_id.setter
    def backup_policy_id(self, backup_policy_id):
        """Sets the backup_policy_id of this ProtectionInfoRequestInfo.

        备份策略ID

        :param backup_policy_id: The backup_policy_id of this ProtectionInfoRequestInfo.
        :type backup_policy_id: str
        """
        self._backup_policy_id = backup_policy_id

    @property
    def backup_cycle(self):
        """Gets the backup_cycle of this ProtectionInfoRequestInfo.

        :return: The backup_cycle of this ProtectionInfoRequestInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.UpdateBackupPolicyRequestInfo`
        """
        return self._backup_cycle

    @backup_cycle.setter
    def backup_cycle(self, backup_cycle):
        """Sets the backup_cycle of this ProtectionInfoRequestInfo.

        :param backup_cycle: The backup_cycle of this ProtectionInfoRequestInfo.
        :type backup_cycle: :class:`huaweicloudsdkhss.v5.UpdateBackupPolicyRequestInfo`
        """
        self._backup_cycle = backup_cycle

    @property
    def agent_id_list(self):
        """Gets the agent_id_list of this ProtectionInfoRequestInfo.

        开启防护的Agent id列表

        :return: The agent_id_list of this ProtectionInfoRequestInfo.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        """Sets the agent_id_list of this ProtectionInfoRequestInfo.

        开启防护的Agent id列表

        :param agent_id_list: The agent_id_list of this ProtectionInfoRequestInfo.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def host_id_list(self):
        """Gets the host_id_list of this ProtectionInfoRequestInfo.

        开启防护的host id列表

        :return: The host_id_list of this ProtectionInfoRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        """Sets the host_id_list of this ProtectionInfoRequestInfo.

        开启防护的host id列表

        :param host_id_list: The host_id_list of this ProtectionInfoRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, ProtectionInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
