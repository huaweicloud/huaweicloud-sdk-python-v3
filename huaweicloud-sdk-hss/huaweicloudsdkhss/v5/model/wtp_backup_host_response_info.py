# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WtpBackupHostResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_host_ip': 'str',
        'backup_host_port': 'int',
        'backup_dir': 'str',
        'backup_host_status': 'int',
        'backup_host_name': 'str',
        'backup_host_id': 'str'
    }

    attribute_map = {
        'backup_host_ip': 'backup_host_ip',
        'backup_host_port': 'backup_host_port',
        'backup_dir': 'backup_dir',
        'backup_host_status': 'backup_host_status',
        'backup_host_name': 'backup_host_name',
        'backup_host_id': 'backup_host_id'
    }

    def __init__(self, backup_host_ip=None, backup_host_port=None, backup_dir=None, backup_host_status=None, backup_host_name=None, backup_host_id=None):
        r"""WtpBackupHostResponseInfo

        The model defined in huaweicloud sdk

        :param backup_host_ip: **参数解释**: 备份服务器IP **取值范围**: 字符长度0-256位 
        :type backup_host_ip: str
        :param backup_host_port: **参数解释**: 备份服务器端口 **取值范围**: 最小值0，最大值65535 
        :type backup_host_port: int
        :param backup_dir: **参数解释**: 备份路径 **取值范围**: 字符长度0-256位 
        :type backup_dir: str
        :param backup_host_status: **参数解释**: 备份状态 **取值范围**: - -1 ：启动失败 - 0 ：未启动 - 1 ：运行中 - 2 ：启动中 
        :type backup_host_status: int
        :param backup_host_name: **参数解释**: 远端备份服务器的服务器名称 **取值范围**: 字符长度0-256位 
        :type backup_host_name: str
        :param backup_host_id: **参数解释**: 远端备份服务器的服务器ID **取值范围**: 字符长度0-256位 
        :type backup_host_id: str
        """
        
        

        self._backup_host_ip = None
        self._backup_host_port = None
        self._backup_dir = None
        self._backup_host_status = None
        self._backup_host_name = None
        self._backup_host_id = None
        self.discriminator = None

        if backup_host_ip is not None:
            self.backup_host_ip = backup_host_ip
        if backup_host_port is not None:
            self.backup_host_port = backup_host_port
        if backup_dir is not None:
            self.backup_dir = backup_dir
        if backup_host_status is not None:
            self.backup_host_status = backup_host_status
        if backup_host_name is not None:
            self.backup_host_name = backup_host_name
        if backup_host_id is not None:
            self.backup_host_id = backup_host_id

    @property
    def backup_host_ip(self):
        r"""Gets the backup_host_ip of this WtpBackupHostResponseInfo.

        **参数解释**: 备份服务器IP **取值范围**: 字符长度0-256位 

        :return: The backup_host_ip of this WtpBackupHostResponseInfo.
        :rtype: str
        """
        return self._backup_host_ip

    @backup_host_ip.setter
    def backup_host_ip(self, backup_host_ip):
        r"""Sets the backup_host_ip of this WtpBackupHostResponseInfo.

        **参数解释**: 备份服务器IP **取值范围**: 字符长度0-256位 

        :param backup_host_ip: The backup_host_ip of this WtpBackupHostResponseInfo.
        :type backup_host_ip: str
        """
        self._backup_host_ip = backup_host_ip

    @property
    def backup_host_port(self):
        r"""Gets the backup_host_port of this WtpBackupHostResponseInfo.

        **参数解释**: 备份服务器端口 **取值范围**: 最小值0，最大值65535 

        :return: The backup_host_port of this WtpBackupHostResponseInfo.
        :rtype: int
        """
        return self._backup_host_port

    @backup_host_port.setter
    def backup_host_port(self, backup_host_port):
        r"""Sets the backup_host_port of this WtpBackupHostResponseInfo.

        **参数解释**: 备份服务器端口 **取值范围**: 最小值0，最大值65535 

        :param backup_host_port: The backup_host_port of this WtpBackupHostResponseInfo.
        :type backup_host_port: int
        """
        self._backup_host_port = backup_host_port

    @property
    def backup_dir(self):
        r"""Gets the backup_dir of this WtpBackupHostResponseInfo.

        **参数解释**: 备份路径 **取值范围**: 字符长度0-256位 

        :return: The backup_dir of this WtpBackupHostResponseInfo.
        :rtype: str
        """
        return self._backup_dir

    @backup_dir.setter
    def backup_dir(self, backup_dir):
        r"""Sets the backup_dir of this WtpBackupHostResponseInfo.

        **参数解释**: 备份路径 **取值范围**: 字符长度0-256位 

        :param backup_dir: The backup_dir of this WtpBackupHostResponseInfo.
        :type backup_dir: str
        """
        self._backup_dir = backup_dir

    @property
    def backup_host_status(self):
        r"""Gets the backup_host_status of this WtpBackupHostResponseInfo.

        **参数解释**: 备份状态 **取值范围**: - -1 ：启动失败 - 0 ：未启动 - 1 ：运行中 - 2 ：启动中 

        :return: The backup_host_status of this WtpBackupHostResponseInfo.
        :rtype: int
        """
        return self._backup_host_status

    @backup_host_status.setter
    def backup_host_status(self, backup_host_status):
        r"""Sets the backup_host_status of this WtpBackupHostResponseInfo.

        **参数解释**: 备份状态 **取值范围**: - -1 ：启动失败 - 0 ：未启动 - 1 ：运行中 - 2 ：启动中 

        :param backup_host_status: The backup_host_status of this WtpBackupHostResponseInfo.
        :type backup_host_status: int
        """
        self._backup_host_status = backup_host_status

    @property
    def backup_host_name(self):
        r"""Gets the backup_host_name of this WtpBackupHostResponseInfo.

        **参数解释**: 远端备份服务器的服务器名称 **取值范围**: 字符长度0-256位 

        :return: The backup_host_name of this WtpBackupHostResponseInfo.
        :rtype: str
        """
        return self._backup_host_name

    @backup_host_name.setter
    def backup_host_name(self, backup_host_name):
        r"""Sets the backup_host_name of this WtpBackupHostResponseInfo.

        **参数解释**: 远端备份服务器的服务器名称 **取值范围**: 字符长度0-256位 

        :param backup_host_name: The backup_host_name of this WtpBackupHostResponseInfo.
        :type backup_host_name: str
        """
        self._backup_host_name = backup_host_name

    @property
    def backup_host_id(self):
        r"""Gets the backup_host_id of this WtpBackupHostResponseInfo.

        **参数解释**: 远端备份服务器的服务器ID **取值范围**: 字符长度0-256位 

        :return: The backup_host_id of this WtpBackupHostResponseInfo.
        :rtype: str
        """
        return self._backup_host_id

    @backup_host_id.setter
    def backup_host_id(self, backup_host_id):
        r"""Sets the backup_host_id of this WtpBackupHostResponseInfo.

        **参数解释**: 远端备份服务器的服务器ID **取值范围**: 字符长度0-256位 

        :param backup_host_id: The backup_host_id of this WtpBackupHostResponseInfo.
        :type backup_host_id: str
        """
        self._backup_host_id = backup_host_id

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
        if not isinstance(other, WtpBackupHostResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
