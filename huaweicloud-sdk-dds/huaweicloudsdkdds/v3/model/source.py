# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Source:

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
        'restore_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'backup_id': 'backup_id',
        'restore_time': 'restore_time'
    }

    def __init__(self, instance_id=None, type=None, backup_id=None, restore_time=None):
        """Source

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type instance_id: str
        :param type: 表示恢复方式，枚举值： - “backup”，表示使用备份文件恢复，按照此方式恢复时，“type”字段为非必选，“backup_id”必选。 - “timestamp”，表示按时间点恢复，按照此方式恢复时，“type”字段必选，“restore_time”必选。
        :type type: str
        :param backup_id: 用于恢复的备份ID。当使用备份文件恢复时需要指定该参数。
        :type backup_id: str
        :param restore_time: 恢复数据的时间点，格式为UNIX时间戳，单位是毫秒，时区为UTC。
        :type restore_time: str
        """
        
        

        self._instance_id = None
        self._type = None
        self._backup_id = None
        self._restore_time = None
        self.discriminator = None

        self.instance_id = instance_id
        if type is not None:
            self.type = type
        if backup_id is not None:
            self.backup_id = backup_id
        if restore_time is not None:
            self.restore_time = restore_time

    @property
    def instance_id(self):
        """Gets the instance_id of this Source.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this Source.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Source.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this Source.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        """Gets the type of this Source.

        表示恢复方式，枚举值： - “backup”，表示使用备份文件恢复，按照此方式恢复时，“type”字段为非必选，“backup_id”必选。 - “timestamp”，表示按时间点恢复，按照此方式恢复时，“type”字段必选，“restore_time”必选。

        :return: The type of this Source.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Source.

        表示恢复方式，枚举值： - “backup”，表示使用备份文件恢复，按照此方式恢复时，“type”字段为非必选，“backup_id”必选。 - “timestamp”，表示按时间点恢复，按照此方式恢复时，“type”字段必选，“restore_time”必选。

        :param type: The type of this Source.
        :type type: str
        """
        self._type = type

    @property
    def backup_id(self):
        """Gets the backup_id of this Source.

        用于恢复的备份ID。当使用备份文件恢复时需要指定该参数。

        :return: The backup_id of this Source.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this Source.

        用于恢复的备份ID。当使用备份文件恢复时需要指定该参数。

        :param backup_id: The backup_id of this Source.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def restore_time(self):
        """Gets the restore_time of this Source.

        恢复数据的时间点，格式为UNIX时间戳，单位是毫秒，时区为UTC。

        :return: The restore_time of this Source.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this Source.

        恢复数据的时间点，格式为UNIX时间戳，单位是毫秒，时区为UTC。

        :param restore_time: The restore_time of this Source.
        :type restore_time: str
        """
        self._restore_time = restore_time

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
        if not isinstance(other, Source):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
