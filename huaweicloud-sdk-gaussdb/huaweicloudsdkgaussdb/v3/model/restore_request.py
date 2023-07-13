# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_instance_id': 'str',
        'source_instance_id': 'str',
        'backup_id': 'str',
        'restore_time': 'int',
        'type': 'str'
    }

    attribute_map = {
        'target_instance_id': 'target_instance_id',
        'source_instance_id': 'source_instance_id',
        'backup_id': 'backup_id',
        'restore_time': 'restore_time',
        'type': 'type'
    }

    def __init__(self, target_instance_id=None, source_instance_id=None, backup_id=None, restore_time=None, type=None):
        """RestoreRequest

        The model defined in huaweicloud sdk

        :param target_instance_id: 目标实例ID。
        :type target_instance_id: str
        :param source_instance_id: 源实例ID。
        :type source_instance_id: str
        :param backup_id: 用于恢复的备份ID。当使用备份文件恢复时需要指定该参数。
        :type backup_id: str
        :param restore_time: 恢复数据的时间点，格式为UNIX时间戳，单位是毫秒，时区为UTC。
        :type restore_time: int
        :param type: 表示恢复方式，枚举值： - backup：表示使用备份文件恢复，按照此方式恢复时，当\&quot;type\&quot;字段为非必选时，\&quot;backup_id\&quot;必选。 - timestamp：表示按时间点恢复，按照此方式恢复时，当\&quot;type\&quot;字段必选时，\&quot;restore_time\&quot;必选。
        :type type: str
        """
        
        

        self._target_instance_id = None
        self._source_instance_id = None
        self._backup_id = None
        self._restore_time = None
        self._type = None
        self.discriminator = None

        self.target_instance_id = target_instance_id
        self.source_instance_id = source_instance_id
        if backup_id is not None:
            self.backup_id = backup_id
        if restore_time is not None:
            self.restore_time = restore_time
        self.type = type

    @property
    def target_instance_id(self):
        """Gets the target_instance_id of this RestoreRequest.

        目标实例ID。

        :return: The target_instance_id of this RestoreRequest.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        """Sets the target_instance_id of this RestoreRequest.

        目标实例ID。

        :param target_instance_id: The target_instance_id of this RestoreRequest.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this RestoreRequest.

        源实例ID。

        :return: The source_instance_id of this RestoreRequest.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this RestoreRequest.

        源实例ID。

        :param source_instance_id: The source_instance_id of this RestoreRequest.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def backup_id(self):
        """Gets the backup_id of this RestoreRequest.

        用于恢复的备份ID。当使用备份文件恢复时需要指定该参数。

        :return: The backup_id of this RestoreRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RestoreRequest.

        用于恢复的备份ID。当使用备份文件恢复时需要指定该参数。

        :param backup_id: The backup_id of this RestoreRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def restore_time(self):
        """Gets the restore_time of this RestoreRequest.

        恢复数据的时间点，格式为UNIX时间戳，单位是毫秒，时区为UTC。

        :return: The restore_time of this RestoreRequest.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RestoreRequest.

        恢复数据的时间点，格式为UNIX时间戳，单位是毫秒，时区为UTC。

        :param restore_time: The restore_time of this RestoreRequest.
        :type restore_time: int
        """
        self._restore_time = restore_time

    @property
    def type(self):
        """Gets the type of this RestoreRequest.

        表示恢复方式，枚举值： - backup：表示使用备份文件恢复，按照此方式恢复时，当\"type\"字段为非必选时，\"backup_id\"必选。 - timestamp：表示按时间点恢复，按照此方式恢复时，当\"type\"字段必选时，\"restore_time\"必选。

        :return: The type of this RestoreRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RestoreRequest.

        表示恢复方式，枚举值： - backup：表示使用备份文件恢复，按照此方式恢复时，当\"type\"字段为非必选时，\"backup_id\"必选。 - timestamp：表示按时间点恢复，按照此方式恢复时，当\"type\"字段必选时，\"restore_time\"必选。

        :param type: The type of this RestoreRequest.
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
        if not isinstance(other, RestoreRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
