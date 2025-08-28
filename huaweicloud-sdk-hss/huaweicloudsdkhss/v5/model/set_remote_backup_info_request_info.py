# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetRemoteBackupInfoRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'remote_backup': 'bool',
        'backup_addr': 'str',
        'backup_host_id': 'str'
    }

    attribute_map = {
        'remote_backup': 'remote_backup',
        'backup_addr': 'backup_addr',
        'backup_host_id': 'backup_host_id'
    }

    def __init__(self, remote_backup=None, backup_addr=None, backup_host_id=None):
        r"""SetRemoteBackupInfoRequestInfo

        The model defined in huaweicloud sdk

        :param remote_backup: **参数解释**: 是否开启远端备份 **约束限制**: 不涉及 **取值范围**: - true ：开启远端备份，需要填写 backup_addr 和 backup_host_id。 - false ：关闭远端备份，无需填写 backup_addr 和 backup_host_id。  **默认取值**: false 
        :type remote_backup: bool
        :param backup_addr: **参数解释**: 远端备份地址，需包含IP和端口，格式为IP:端口 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type backup_addr: str
        :param backup_host_id: **参数解释**: 远端备份服务器的服务器ID，填写的远端备份服务器ID必须是已运行中的备份服务器ID **约束限制**: 需要使用 ListBackupHostsInfo 接口查询已运行中的远端备份服务器，在 ListBackupHostsInfo 接口的响应体中，backup_host_status 等于 1 的 backup_host_id 是已运行的远端备份服务器ID **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type backup_host_id: str
        """
        
        

        self._remote_backup = None
        self._backup_addr = None
        self._backup_host_id = None
        self.discriminator = None

        self.remote_backup = remote_backup
        if backup_addr is not None:
            self.backup_addr = backup_addr
        if backup_host_id is not None:
            self.backup_host_id = backup_host_id

    @property
    def remote_backup(self):
        r"""Gets the remote_backup of this SetRemoteBackupInfoRequestInfo.

        **参数解释**: 是否开启远端备份 **约束限制**: 不涉及 **取值范围**: - true ：开启远端备份，需要填写 backup_addr 和 backup_host_id。 - false ：关闭远端备份，无需填写 backup_addr 和 backup_host_id。  **默认取值**: false 

        :return: The remote_backup of this SetRemoteBackupInfoRequestInfo.
        :rtype: bool
        """
        return self._remote_backup

    @remote_backup.setter
    def remote_backup(self, remote_backup):
        r"""Sets the remote_backup of this SetRemoteBackupInfoRequestInfo.

        **参数解释**: 是否开启远端备份 **约束限制**: 不涉及 **取值范围**: - true ：开启远端备份，需要填写 backup_addr 和 backup_host_id。 - false ：关闭远端备份，无需填写 backup_addr 和 backup_host_id。  **默认取值**: false 

        :param remote_backup: The remote_backup of this SetRemoteBackupInfoRequestInfo.
        :type remote_backup: bool
        """
        self._remote_backup = remote_backup

    @property
    def backup_addr(self):
        r"""Gets the backup_addr of this SetRemoteBackupInfoRequestInfo.

        **参数解释**: 远端备份地址，需包含IP和端口，格式为IP:端口 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The backup_addr of this SetRemoteBackupInfoRequestInfo.
        :rtype: str
        """
        return self._backup_addr

    @backup_addr.setter
    def backup_addr(self, backup_addr):
        r"""Sets the backup_addr of this SetRemoteBackupInfoRequestInfo.

        **参数解释**: 远端备份地址，需包含IP和端口，格式为IP:端口 **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param backup_addr: The backup_addr of this SetRemoteBackupInfoRequestInfo.
        :type backup_addr: str
        """
        self._backup_addr = backup_addr

    @property
    def backup_host_id(self):
        r"""Gets the backup_host_id of this SetRemoteBackupInfoRequestInfo.

        **参数解释**: 远端备份服务器的服务器ID，填写的远端备份服务器ID必须是已运行中的备份服务器ID **约束限制**: 需要使用 ListBackupHostsInfo 接口查询已运行中的远端备份服务器，在 ListBackupHostsInfo 接口的响应体中，backup_host_status 等于 1 的 backup_host_id 是已运行的远端备份服务器ID **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The backup_host_id of this SetRemoteBackupInfoRequestInfo.
        :rtype: str
        """
        return self._backup_host_id

    @backup_host_id.setter
    def backup_host_id(self, backup_host_id):
        r"""Sets the backup_host_id of this SetRemoteBackupInfoRequestInfo.

        **参数解释**: 远端备份服务器的服务器ID，填写的远端备份服务器ID必须是已运行中的备份服务器ID **约束限制**: 需要使用 ListBackupHostsInfo 接口查询已运行中的远端备份服务器，在 ListBackupHostsInfo 接口的响应体中，backup_host_status 等于 1 的 backup_host_id 是已运行的远端备份服务器ID **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param backup_host_id: The backup_host_id of this SetRemoteBackupInfoRequestInfo.
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
        if not isinstance(other, SetRemoteBackupInfoRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
