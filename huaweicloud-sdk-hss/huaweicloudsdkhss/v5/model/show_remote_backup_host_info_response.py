# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRemoteBackupHostInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_addr': 'str',
        'backup_host_id': 'str',
        'backup_host_name': 'str',
        'remote_backup': 'bool'
    }

    attribute_map = {
        'backup_addr': 'backup_addr',
        'backup_host_id': 'backup_host_id',
        'backup_host_name': 'backup_host_name',
        'remote_backup': 'remote_backup'
    }

    def __init__(self, backup_addr=None, backup_host_id=None, backup_host_name=None, remote_backup=None):
        r"""ShowRemoteBackupHostInfoResponse

        The model defined in huaweicloud sdk

        :param backup_addr: 远端备份服务器的地址，包含IP和端口
        :type backup_addr: str
        :param backup_host_id: 远端备份服务器的服务器ID
        :type backup_host_id: str
        :param backup_host_name: 远端备份服务器的服务器名称
        :type backup_host_name: str
        :param remote_backup: **参数解释** 服务器是否开启远端备份 **取值范围**  - true : 已开启远端备份。 - false: 未开启远端备份。
        :type remote_backup: bool
        """
        
        super(ShowRemoteBackupHostInfoResponse, self).__init__()

        self._backup_addr = None
        self._backup_host_id = None
        self._backup_host_name = None
        self._remote_backup = None
        self.discriminator = None

        if backup_addr is not None:
            self.backup_addr = backup_addr
        if backup_host_id is not None:
            self.backup_host_id = backup_host_id
        if backup_host_name is not None:
            self.backup_host_name = backup_host_name
        if remote_backup is not None:
            self.remote_backup = remote_backup

    @property
    def backup_addr(self):
        r"""Gets the backup_addr of this ShowRemoteBackupHostInfoResponse.

        远端备份服务器的地址，包含IP和端口

        :return: The backup_addr of this ShowRemoteBackupHostInfoResponse.
        :rtype: str
        """
        return self._backup_addr

    @backup_addr.setter
    def backup_addr(self, backup_addr):
        r"""Sets the backup_addr of this ShowRemoteBackupHostInfoResponse.

        远端备份服务器的地址，包含IP和端口

        :param backup_addr: The backup_addr of this ShowRemoteBackupHostInfoResponse.
        :type backup_addr: str
        """
        self._backup_addr = backup_addr

    @property
    def backup_host_id(self):
        r"""Gets the backup_host_id of this ShowRemoteBackupHostInfoResponse.

        远端备份服务器的服务器ID

        :return: The backup_host_id of this ShowRemoteBackupHostInfoResponse.
        :rtype: str
        """
        return self._backup_host_id

    @backup_host_id.setter
    def backup_host_id(self, backup_host_id):
        r"""Sets the backup_host_id of this ShowRemoteBackupHostInfoResponse.

        远端备份服务器的服务器ID

        :param backup_host_id: The backup_host_id of this ShowRemoteBackupHostInfoResponse.
        :type backup_host_id: str
        """
        self._backup_host_id = backup_host_id

    @property
    def backup_host_name(self):
        r"""Gets the backup_host_name of this ShowRemoteBackupHostInfoResponse.

        远端备份服务器的服务器名称

        :return: The backup_host_name of this ShowRemoteBackupHostInfoResponse.
        :rtype: str
        """
        return self._backup_host_name

    @backup_host_name.setter
    def backup_host_name(self, backup_host_name):
        r"""Sets the backup_host_name of this ShowRemoteBackupHostInfoResponse.

        远端备份服务器的服务器名称

        :param backup_host_name: The backup_host_name of this ShowRemoteBackupHostInfoResponse.
        :type backup_host_name: str
        """
        self._backup_host_name = backup_host_name

    @property
    def remote_backup(self):
        r"""Gets the remote_backup of this ShowRemoteBackupHostInfoResponse.

        **参数解释** 服务器是否开启远端备份 **取值范围**  - true : 已开启远端备份。 - false: 未开启远端备份。

        :return: The remote_backup of this ShowRemoteBackupHostInfoResponse.
        :rtype: bool
        """
        return self._remote_backup

    @remote_backup.setter
    def remote_backup(self, remote_backup):
        r"""Sets the remote_backup of this ShowRemoteBackupHostInfoResponse.

        **参数解释** 服务器是否开启远端备份 **取值范围**  - true : 已开启远端备份。 - false: 未开启远端备份。

        :param remote_backup: The remote_backup of this ShowRemoteBackupHostInfoResponse.
        :type remote_backup: bool
        """
        self._remote_backup = remote_backup

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
        if not isinstance(other, ShowRemoteBackupHostInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
