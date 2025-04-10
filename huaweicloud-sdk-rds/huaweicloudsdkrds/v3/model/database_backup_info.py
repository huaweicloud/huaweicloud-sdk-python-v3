# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseBackupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'backup_file_name': 'str',
        'backup_file_size': 'int'
    }

    attribute_map = {
        'database_name': 'database_name',
        'backup_file_name': 'backup_file_name',
        'backup_file_size': 'backup_file_size'
    }

    def __init__(self, database_name=None, backup_file_name=None, backup_file_size=None):
        r"""DatabaseBackupInfo

        The model defined in huaweicloud sdk

        :param database_name: 库名
        :type database_name: str
        :param backup_file_name: 备份文件名
        :type backup_file_name: str
        :param backup_file_size: 备份文件大小
        :type backup_file_size: int
        """
        
        

        self._database_name = None
        self._backup_file_name = None
        self._backup_file_size = None
        self.discriminator = None

        self.database_name = database_name
        self.backup_file_name = backup_file_name
        self.backup_file_size = backup_file_size

    @property
    def database_name(self):
        r"""Gets the database_name of this DatabaseBackupInfo.

        库名

        :return: The database_name of this DatabaseBackupInfo.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this DatabaseBackupInfo.

        库名

        :param database_name: The database_name of this DatabaseBackupInfo.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def backup_file_name(self):
        r"""Gets the backup_file_name of this DatabaseBackupInfo.

        备份文件名

        :return: The backup_file_name of this DatabaseBackupInfo.
        :rtype: str
        """
        return self._backup_file_name

    @backup_file_name.setter
    def backup_file_name(self, backup_file_name):
        r"""Sets the backup_file_name of this DatabaseBackupInfo.

        备份文件名

        :param backup_file_name: The backup_file_name of this DatabaseBackupInfo.
        :type backup_file_name: str
        """
        self._backup_file_name = backup_file_name

    @property
    def backup_file_size(self):
        r"""Gets the backup_file_size of this DatabaseBackupInfo.

        备份文件大小

        :return: The backup_file_size of this DatabaseBackupInfo.
        :rtype: int
        """
        return self._backup_file_size

    @backup_file_size.setter
    def backup_file_size(self, backup_file_size):
        r"""Sets the backup_file_size of this DatabaseBackupInfo.

        备份文件大小

        :param backup_file_size: The backup_file_size of this DatabaseBackupInfo.
        :type backup_file_size: int
        """
        self._backup_file_size = backup_file_size

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
        if not isinstance(other, DatabaseBackupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
