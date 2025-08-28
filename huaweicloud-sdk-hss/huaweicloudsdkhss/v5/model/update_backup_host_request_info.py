# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBackupHostRequestInfo:

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
        'backup_host_ip': 'str',
        'backup_host_port': 'int',
        'backup_dir': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'backup_host_ip': 'backup_host_ip',
        'backup_host_port': 'backup_host_port',
        'backup_dir': 'backup_dir'
    }

    def __init__(self, host_id=None, backup_host_ip=None, backup_host_port=None, backup_dir=None):
        r"""UpdateBackupHostRequestInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 远端备份服务器的服务器ID，如果备份服务器之前不存在，则本次操作为新增，如果之前已存在，则本次操作为修改 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 
        :type host_id: str
        :param backup_host_ip: **参数解释**: 备份服务器IP **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 
        :type backup_host_ip: str
        :param backup_host_port: **参数解释**: 备份服务器端口 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值65535 **默认取值** : 不涉及 
        :type backup_host_port: int
        :param backup_dir: **参数解释**: 备份路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 
        :type backup_dir: str
        """
        
        

        self._host_id = None
        self._backup_host_ip = None
        self._backup_host_port = None
        self._backup_dir = None
        self.discriminator = None

        self.host_id = host_id
        self.backup_host_ip = backup_host_ip
        self.backup_host_port = backup_host_port
        self.backup_dir = backup_dir

    @property
    def host_id(self):
        r"""Gets the host_id of this UpdateBackupHostRequestInfo.

        **参数解释**: 远端备份服务器的服务器ID，如果备份服务器之前不存在，则本次操作为新增，如果之前已存在，则本次操作为修改 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 

        :return: The host_id of this UpdateBackupHostRequestInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this UpdateBackupHostRequestInfo.

        **参数解释**: 远端备份服务器的服务器ID，如果备份服务器之前不存在，则本次操作为新增，如果之前已存在，则本次操作为修改 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 

        :param host_id: The host_id of this UpdateBackupHostRequestInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def backup_host_ip(self):
        r"""Gets the backup_host_ip of this UpdateBackupHostRequestInfo.

        **参数解释**: 备份服务器IP **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 

        :return: The backup_host_ip of this UpdateBackupHostRequestInfo.
        :rtype: str
        """
        return self._backup_host_ip

    @backup_host_ip.setter
    def backup_host_ip(self, backup_host_ip):
        r"""Sets the backup_host_ip of this UpdateBackupHostRequestInfo.

        **参数解释**: 备份服务器IP **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 

        :param backup_host_ip: The backup_host_ip of this UpdateBackupHostRequestInfo.
        :type backup_host_ip: str
        """
        self._backup_host_ip = backup_host_ip

    @property
    def backup_host_port(self):
        r"""Gets the backup_host_port of this UpdateBackupHostRequestInfo.

        **参数解释**: 备份服务器端口 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值65535 **默认取值** : 不涉及 

        :return: The backup_host_port of this UpdateBackupHostRequestInfo.
        :rtype: int
        """
        return self._backup_host_port

    @backup_host_port.setter
    def backup_host_port(self, backup_host_port):
        r"""Sets the backup_host_port of this UpdateBackupHostRequestInfo.

        **参数解释**: 备份服务器端口 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值65535 **默认取值** : 不涉及 

        :param backup_host_port: The backup_host_port of this UpdateBackupHostRequestInfo.
        :type backup_host_port: int
        """
        self._backup_host_port = backup_host_port

    @property
    def backup_dir(self):
        r"""Gets the backup_dir of this UpdateBackupHostRequestInfo.

        **参数解释**: 备份路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 

        :return: The backup_dir of this UpdateBackupHostRequestInfo.
        :rtype: str
        """
        return self._backup_dir

    @backup_dir.setter
    def backup_dir(self, backup_dir):
        r"""Sets the backup_dir of this UpdateBackupHostRequestInfo.

        **参数解释**: 备份路径 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值** : 不涉及 

        :param backup_dir: The backup_dir of this UpdateBackupHostRequestInfo.
        :type backup_dir: str
        """
        self._backup_dir = backup_dir

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
        if not isinstance(other, UpdateBackupHostRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
