# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeVulStatusRequestInfoCustomBackupHosts:

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
        'vault_id': 'str',
        'backup_name': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'vault_id': 'vault_id',
        'backup_name': 'backup_name'
    }

    def __init__(self, host_id=None, vault_id=None, backup_name=None):
        """ChangeVulStatusRequestInfoCustomBackupHosts

        The model defined in huaweicloud sdk

        :param host_id: 主机id
        :type host_id: str
        :param vault_id: 存储库id
        :type vault_id: str
        :param backup_name: 备份名称
        :type backup_name: str
        """
        
        

        self._host_id = None
        self._vault_id = None
        self._backup_name = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if vault_id is not None:
            self.vault_id = vault_id
        if backup_name is not None:
            self.backup_name = backup_name

    @property
    def host_id(self):
        """Gets the host_id of this ChangeVulStatusRequestInfoCustomBackupHosts.

        主机id

        :return: The host_id of this ChangeVulStatusRequestInfoCustomBackupHosts.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ChangeVulStatusRequestInfoCustomBackupHosts.

        主机id

        :param host_id: The host_id of this ChangeVulStatusRequestInfoCustomBackupHosts.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def vault_id(self):
        """Gets the vault_id of this ChangeVulStatusRequestInfoCustomBackupHosts.

        存储库id

        :return: The vault_id of this ChangeVulStatusRequestInfoCustomBackupHosts.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this ChangeVulStatusRequestInfoCustomBackupHosts.

        存储库id

        :param vault_id: The vault_id of this ChangeVulStatusRequestInfoCustomBackupHosts.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def backup_name(self):
        """Gets the backup_name of this ChangeVulStatusRequestInfoCustomBackupHosts.

        备份名称

        :return: The backup_name of this ChangeVulStatusRequestInfoCustomBackupHosts.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        """Sets the backup_name of this ChangeVulStatusRequestInfoCustomBackupHosts.

        备份名称

        :param backup_name: The backup_name of this ChangeVulStatusRequestInfoCustomBackupHosts.
        :type backup_name: str
        """
        self._backup_name = backup_name

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
        if not isinstance(other, ChangeVulStatusRequestInfoCustomBackupHosts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
