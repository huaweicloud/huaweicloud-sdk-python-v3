# coding: utf-8

import pprint
import re

import six





class RestoreToExistingInstanceRequestBodySource:


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
        'restore_time': 'int',
        'database_name': 'dict(str, str)'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'backup_id': 'backup_id',
        'restore_time': 'restore_time',
        'database_name': 'database_name'
    }

    def __init__(self, instance_id=None, type=None, backup_id=None, restore_time=None, database_name=None):
        """RestoreToExistingInstanceRequestBodySource - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._type = None
        self._backup_id = None
        self._restore_time = None
        self._database_name = None
        self.discriminator = None

        self.instance_id = instance_id
        if type is not None:
            self.type = type
        if backup_id is not None:
            self.backup_id = backup_id
        if restore_time is not None:
            self.restore_time = restore_time
        if database_name is not None:
            self.database_name = database_name

    @property
    def instance_id(self):
        """Gets the instance_id of this RestoreToExistingInstanceRequestBodySource.

        实例ID。

        :return: The instance_id of this RestoreToExistingInstanceRequestBodySource.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RestoreToExistingInstanceRequestBodySource.

        实例ID。

        :param instance_id: The instance_id of this RestoreToExistingInstanceRequestBodySource.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this RestoreToExistingInstanceRequestBodySource.

        表示恢复方式，枚举值：  - “backup”，表示使用备份文件恢复，按照此方式恢复时，“type”字段为非必选，“backup_id”必选。 - “timestamp”，表示按时间点恢复，按照此方式恢复时，“type”字段必选，“restore_time”必选。

        :return: The type of this RestoreToExistingInstanceRequestBodySource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestoreToExistingInstanceRequestBodySource.

        表示恢复方式，枚举值：  - “backup”，表示使用备份文件恢复，按照此方式恢复时，“type”字段为非必选，“backup_id”必选。 - “timestamp”，表示按时间点恢复，按照此方式恢复时，“type”字段必选，“restore_time”必选。

        :param type: The type of this RestoreToExistingInstanceRequestBodySource.
        :type: str
        """
        self._type = type

    @property
    def backup_id(self):
        """Gets the backup_id of this RestoreToExistingInstanceRequestBodySource.

        用于恢复的备份ID。当使用备份文件恢复时需要指定该参数。

        :return: The backup_id of this RestoreToExistingInstanceRequestBodySource.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RestoreToExistingInstanceRequestBodySource.

        用于恢复的备份ID。当使用备份文件恢复时需要指定该参数。

        :param backup_id: The backup_id of this RestoreToExistingInstanceRequestBodySource.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def restore_time(self):
        """Gets the restore_time of this RestoreToExistingInstanceRequestBodySource.

        恢复数据的时间点，格式为UNIX时间戳，单位是毫秒，时区为UTC。

        :return: The restore_time of this RestoreToExistingInstanceRequestBodySource.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RestoreToExistingInstanceRequestBodySource.

        恢复数据的时间点，格式为UNIX时间戳，单位是毫秒，时区为UTC。

        :param restore_time: The restore_time of this RestoreToExistingInstanceRequestBodySource.
        :type: int
        """
        self._restore_time = restore_time

    @property
    def database_name(self):
        """Gets the database_name of this RestoreToExistingInstanceRequestBodySource.

        仅适用于SQL Server引擎，当有此参数时表示支持局部恢复和重命名恢复，恢复数据以局部恢复为主。不填写该字段时，默认恢复全部数据库。 - 新数据库名称不可与源实例或目标实例数据库名称重名，新数据库名称为空，默认按照原数据库名进行恢复。 - 新数据库名不能包含rdsadmin、master、msdb、tempdb、model或resource字段（不区分大小写）。 - 数据库名称长度在1~64个字符之间，包含字母、数字、下划线或中划线，不能包含其他特殊字符。

        :return: The database_name of this RestoreToExistingInstanceRequestBodySource.
        :rtype: dict(str, str)
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this RestoreToExistingInstanceRequestBodySource.

        仅适用于SQL Server引擎，当有此参数时表示支持局部恢复和重命名恢复，恢复数据以局部恢复为主。不填写该字段时，默认恢复全部数据库。 - 新数据库名称不可与源实例或目标实例数据库名称重名，新数据库名称为空，默认按照原数据库名进行恢复。 - 新数据库名不能包含rdsadmin、master、msdb、tempdb、model或resource字段（不区分大小写）。 - 数据库名称长度在1~64个字符之间，包含字母、数字、下划线或中划线，不能包含其他特殊字符。

        :param database_name: The database_name of this RestoreToExistingInstanceRequestBodySource.
        :type: dict(str, str)
        """
        self._database_name = database_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RestoreToExistingInstanceRequestBodySource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
