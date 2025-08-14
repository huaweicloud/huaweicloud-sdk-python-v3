# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStartProtectionRequestInfo:

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
        'backup_protection_status': 'str',
        'vault_id': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'operating_system': 'operating_system',
        'ransom_protection_status': 'ransom_protection_status',
        'protection_policy_id': 'protection_policy_id',
        'backup_protection_status': 'backup_protection_status',
        'vault_id': 'vault_id',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, operating_system=None, ransom_protection_status=None, protection_policy_id=None, backup_protection_status=None, vault_id=None, host_id_list=None):
        r"""BatchStartProtectionRequestInfo

        The model defined in huaweicloud sdk

        :param operating_system: 操作系统，包含如下：   - Windows : Windows系统   - Linux : Linux系统
        :type operating_system: str
        :param ransom_protection_status: 勒索防护是否开启，包含如下：   - closed ：关闭。   - opened ：开启。   若选择开启，protection_policy_id必填一项
        :type ransom_protection_status: str
        :param protection_policy_id: 防护策略ID，若ransom_protection_status为opened，则该字段必选
        :type protection_policy_id: str
        :param backup_protection_status: 是否服务器备份，包含如下：   - closed ：关闭。   - opened ：开启。   若选择开启服务器备份，则vault_id必填
        :type backup_protection_status: str
        :param vault_id: 需要绑定的存储库ID，若backup_protection_status为opened，则该字段必填
        :type vault_id: str
        :param host_id_list: 开启防护的host id列表
        :type host_id_list: list[str]
        """
        
        

        self._operating_system = None
        self._ransom_protection_status = None
        self._protection_policy_id = None
        self._backup_protection_status = None
        self._vault_id = None
        self._host_id_list = None
        self.discriminator = None

        self.operating_system = operating_system
        self.ransom_protection_status = ransom_protection_status
        if protection_policy_id is not None:
            self.protection_policy_id = protection_policy_id
        self.backup_protection_status = backup_protection_status
        if vault_id is not None:
            self.vault_id = vault_id
        self.host_id_list = host_id_list

    @property
    def operating_system(self):
        r"""Gets the operating_system of this BatchStartProtectionRequestInfo.

        操作系统，包含如下：   - Windows : Windows系统   - Linux : Linux系统

        :return: The operating_system of this BatchStartProtectionRequestInfo.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        r"""Sets the operating_system of this BatchStartProtectionRequestInfo.

        操作系统，包含如下：   - Windows : Windows系统   - Linux : Linux系统

        :param operating_system: The operating_system of this BatchStartProtectionRequestInfo.
        :type operating_system: str
        """
        self._operating_system = operating_system

    @property
    def ransom_protection_status(self):
        r"""Gets the ransom_protection_status of this BatchStartProtectionRequestInfo.

        勒索防护是否开启，包含如下：   - closed ：关闭。   - opened ：开启。   若选择开启，protection_policy_id必填一项

        :return: The ransom_protection_status of this BatchStartProtectionRequestInfo.
        :rtype: str
        """
        return self._ransom_protection_status

    @ransom_protection_status.setter
    def ransom_protection_status(self, ransom_protection_status):
        r"""Sets the ransom_protection_status of this BatchStartProtectionRequestInfo.

        勒索防护是否开启，包含如下：   - closed ：关闭。   - opened ：开启。   若选择开启，protection_policy_id必填一项

        :param ransom_protection_status: The ransom_protection_status of this BatchStartProtectionRequestInfo.
        :type ransom_protection_status: str
        """
        self._ransom_protection_status = ransom_protection_status

    @property
    def protection_policy_id(self):
        r"""Gets the protection_policy_id of this BatchStartProtectionRequestInfo.

        防护策略ID，若ransom_protection_status为opened，则该字段必选

        :return: The protection_policy_id of this BatchStartProtectionRequestInfo.
        :rtype: str
        """
        return self._protection_policy_id

    @protection_policy_id.setter
    def protection_policy_id(self, protection_policy_id):
        r"""Sets the protection_policy_id of this BatchStartProtectionRequestInfo.

        防护策略ID，若ransom_protection_status为opened，则该字段必选

        :param protection_policy_id: The protection_policy_id of this BatchStartProtectionRequestInfo.
        :type protection_policy_id: str
        """
        self._protection_policy_id = protection_policy_id

    @property
    def backup_protection_status(self):
        r"""Gets the backup_protection_status of this BatchStartProtectionRequestInfo.

        是否服务器备份，包含如下：   - closed ：关闭。   - opened ：开启。   若选择开启服务器备份，则vault_id必填

        :return: The backup_protection_status of this BatchStartProtectionRequestInfo.
        :rtype: str
        """
        return self._backup_protection_status

    @backup_protection_status.setter
    def backup_protection_status(self, backup_protection_status):
        r"""Sets the backup_protection_status of this BatchStartProtectionRequestInfo.

        是否服务器备份，包含如下：   - closed ：关闭。   - opened ：开启。   若选择开启服务器备份，则vault_id必填

        :param backup_protection_status: The backup_protection_status of this BatchStartProtectionRequestInfo.
        :type backup_protection_status: str
        """
        self._backup_protection_status = backup_protection_status

    @property
    def vault_id(self):
        r"""Gets the vault_id of this BatchStartProtectionRequestInfo.

        需要绑定的存储库ID，若backup_protection_status为opened，则该字段必填

        :return: The vault_id of this BatchStartProtectionRequestInfo.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this BatchStartProtectionRequestInfo.

        需要绑定的存储库ID，若backup_protection_status为opened，则该字段必填

        :param vault_id: The vault_id of this BatchStartProtectionRequestInfo.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this BatchStartProtectionRequestInfo.

        开启防护的host id列表

        :return: The host_id_list of this BatchStartProtectionRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this BatchStartProtectionRequestInfo.

        开启防护的host id列表

        :param host_id_list: The host_id_list of this BatchStartProtectionRequestInfo.
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
        if not isinstance(other, BatchStartProtectionRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
