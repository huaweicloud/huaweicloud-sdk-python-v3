# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecoveryBackupSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'type': 'str',
        'backup_id': 'str',
        'restore_time': 'str',
        'table_list': 'list[RestoreTableListDetail]',
        'schema_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'backup_id': 'backup_id',
        'restore_time': 'restore_time',
        'table_list': 'table_list',
        'schema_type': 'schema_type'
    }

    def __init__(self, instance_id=None, type=None, backup_id=None, restore_time=None, table_list=None, schema_type=None):
        """RecoveryBackupSource

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param type: 恢复备份类型：backup，timestamp，different
        :type type: str
        :param backup_id: 用于恢复的备份ID。
        :type backup_id: str
        :param restore_time: UTC时间，时间戳
        :type restore_time: str
        :param table_list: 表基础信息。
        :type table_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.RestoreTableListDetail`]
        :param schema_type: 备份级别取值, 默认值：INSTANCE
        :type schema_type: str
        """
        
        

        self._instance_id = None
        self._type = None
        self._backup_id = None
        self._restore_time = None
        self._table_list = None
        self._schema_type = None
        self.discriminator = None

        self.instance_id = instance_id
        if type is not None:
            self.type = type
        self.backup_id = backup_id
        self.restore_time = restore_time
        if table_list is not None:
            self.table_list = table_list
        if schema_type is not None:
            self.schema_type = schema_type

    @property
    def instance_id(self):
        """Gets the instance_id of this RecoveryBackupSource.

        实例ID

        :return: The instance_id of this RecoveryBackupSource.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RecoveryBackupSource.

        实例ID

        :param instance_id: The instance_id of this RecoveryBackupSource.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this RecoveryBackupSource.

        恢复备份类型：backup，timestamp，different

        :return: The type of this RecoveryBackupSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RecoveryBackupSource.

        恢复备份类型：backup，timestamp，different

        :param type: The type of this RecoveryBackupSource.
        :type type: str
        """
        self._type = type

    @property
    def backup_id(self):
        """Gets the backup_id of this RecoveryBackupSource.

        用于恢复的备份ID。

        :return: The backup_id of this RecoveryBackupSource.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RecoveryBackupSource.

        用于恢复的备份ID。

        :param backup_id: The backup_id of this RecoveryBackupSource.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def restore_time(self):
        """Gets the restore_time of this RecoveryBackupSource.

        UTC时间，时间戳

        :return: The restore_time of this RecoveryBackupSource.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RecoveryBackupSource.

        UTC时间，时间戳

        :param restore_time: The restore_time of this RecoveryBackupSource.
        :type restore_time: str
        """
        self._restore_time = restore_time

    @property
    def table_list(self):
        """Gets the table_list of this RecoveryBackupSource.

        表基础信息。

        :return: The table_list of this RecoveryBackupSource.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.RestoreTableListDetail`]
        """
        return self._table_list

    @table_list.setter
    def table_list(self, table_list):
        """Sets the table_list of this RecoveryBackupSource.

        表基础信息。

        :param table_list: The table_list of this RecoveryBackupSource.
        :type table_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.RestoreTableListDetail`]
        """
        self._table_list = table_list

    @property
    def schema_type(self):
        """Gets the schema_type of this RecoveryBackupSource.

        备份级别取值, 默认值：INSTANCE

        :return: The schema_type of this RecoveryBackupSource.
        :rtype: str
        """
        return self._schema_type

    @schema_type.setter
    def schema_type(self, schema_type):
        """Sets the schema_type of this RecoveryBackupSource.

        备份级别取值, 默认值：INSTANCE

        :param schema_type: The schema_type of this RecoveryBackupSource.
        :type schema_type: str
        """
        self._schema_type = schema_type

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
        if not isinstance(other, RecoveryBackupSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
