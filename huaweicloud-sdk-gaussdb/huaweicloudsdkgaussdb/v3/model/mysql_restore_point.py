# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlRestorePoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_time': 'int',
        'source_instance_id': 'str',
        'backup_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'restore_time': 'restore_time',
        'source_instance_id': 'source_instance_id',
        'backup_id': 'backup_id',
        'type': 'type'
    }

    def __init__(self, restore_time=None, source_instance_id=None, backup_id=None, type=None):
        """MysqlRestorePoint

        The model defined in huaweicloud sdk

        :param restore_time: PITR。要恢复的时间点。
        :type restore_time: int
        :param source_instance_id: 源实例ID。
        :type source_instance_id: str
        :param backup_id: 备份文件ID。
        :type backup_id: str
        :param type: 备份类型。当参数为空时，backup_id不能为空，即默认按备份文件恢复。 当参数不为空时，取值范围： - backup：表示按备份文件恢复； - timestamp：表示按时间点恢复；
        :type type: str
        """
        
        

        self._restore_time = None
        self._source_instance_id = None
        self._backup_id = None
        self._type = None
        self.discriminator = None

        if restore_time is not None:
            self.restore_time = restore_time
        self.source_instance_id = source_instance_id
        if backup_id is not None:
            self.backup_id = backup_id
        if type is not None:
            self.type = type

    @property
    def restore_time(self):
        """Gets the restore_time of this MysqlRestorePoint.

        PITR。要恢复的时间点。

        :return: The restore_time of this MysqlRestorePoint.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this MysqlRestorePoint.

        PITR。要恢复的时间点。

        :param restore_time: The restore_time of this MysqlRestorePoint.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this MysqlRestorePoint.

        源实例ID。

        :return: The source_instance_id of this MysqlRestorePoint.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this MysqlRestorePoint.

        源实例ID。

        :param source_instance_id: The source_instance_id of this MysqlRestorePoint.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def backup_id(self):
        """Gets the backup_id of this MysqlRestorePoint.

        备份文件ID。

        :return: The backup_id of this MysqlRestorePoint.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this MysqlRestorePoint.

        备份文件ID。

        :param backup_id: The backup_id of this MysqlRestorePoint.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def type(self):
        """Gets the type of this MysqlRestorePoint.

        备份类型。当参数为空时，backup_id不能为空，即默认按备份文件恢复。 当参数不为空时，取值范围： - backup：表示按备份文件恢复； - timestamp：表示按时间点恢复；

        :return: The type of this MysqlRestorePoint.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MysqlRestorePoint.

        备份类型。当参数为空时，backup_id不能为空，即默认按备份文件恢复。 当参数不为空时，取值范围： - backup：表示按备份文件恢复； - timestamp：表示按时间点恢复；

        :param type: The type of this MysqlRestorePoint.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, MysqlRestorePoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
