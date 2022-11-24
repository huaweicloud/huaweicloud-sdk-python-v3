# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'source_instance_id': 'str',
        'restore_time': 'int'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'source_instance_id': 'source_instance_id',
        'restore_time': 'restore_time'
    }

    def __init__(self, backup_id=None, source_instance_id=None, restore_time=None):
        """RestoreInfo

        The model defined in huaweicloud sdk

        :param backup_id: 备份文件ID。  用于根据指定备份恢复数据到一个新创建的实例的场景，此场景下该字段取值不能为空。
        :type backup_id: str
        :param source_instance_id: 数据恢复参考的指定实例的ID。  用于恢复指定实例的指定时间点的数据到一个新创建的实例的场景，此场景下该字段取值不能为空。
        :type source_instance_id: str
        :param restore_time: 数据恢复的指定的时间点。  用于恢复指定实例的指定时间点的数据到一个新创建的实例的场景，此场景下该字段取值不能为空。取值为UTC 13位毫秒数，可通过[查询实例可恢复的时间段]接口进行查询。
        :type restore_time: int
        """
        
        

        self._backup_id = None
        self._source_instance_id = None
        self._restore_time = None
        self.discriminator = None

        if backup_id is not None:
            self.backup_id = backup_id
        if source_instance_id is not None:
            self.source_instance_id = source_instance_id
        if restore_time is not None:
            self.restore_time = restore_time

    @property
    def backup_id(self):
        """Gets the backup_id of this RestoreInfo.

        备份文件ID。  用于根据指定备份恢复数据到一个新创建的实例的场景，此场景下该字段取值不能为空。

        :return: The backup_id of this RestoreInfo.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this RestoreInfo.

        备份文件ID。  用于根据指定备份恢复数据到一个新创建的实例的场景，此场景下该字段取值不能为空。

        :param backup_id: The backup_id of this RestoreInfo.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def source_instance_id(self):
        """Gets the source_instance_id of this RestoreInfo.

        数据恢复参考的指定实例的ID。  用于恢复指定实例的指定时间点的数据到一个新创建的实例的场景，此场景下该字段取值不能为空。

        :return: The source_instance_id of this RestoreInfo.
        :rtype: str
        """
        return self._source_instance_id

    @source_instance_id.setter
    def source_instance_id(self, source_instance_id):
        """Sets the source_instance_id of this RestoreInfo.

        数据恢复参考的指定实例的ID。  用于恢复指定实例的指定时间点的数据到一个新创建的实例的场景，此场景下该字段取值不能为空。

        :param source_instance_id: The source_instance_id of this RestoreInfo.
        :type source_instance_id: str
        """
        self._source_instance_id = source_instance_id

    @property
    def restore_time(self):
        """Gets the restore_time of this RestoreInfo.

        数据恢复的指定的时间点。  用于恢复指定实例的指定时间点的数据到一个新创建的实例的场景，此场景下该字段取值不能为空。取值为UTC 13位毫秒数，可通过[查询实例可恢复的时间段]接口进行查询。

        :return: The restore_time of this RestoreInfo.
        :rtype: int
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        """Sets the restore_time of this RestoreInfo.

        数据恢复的指定的时间点。  用于恢复指定实例的指定时间点的数据到一个新创建的实例的场景，此场景下该字段取值不能为空。取值为UTC 13位毫秒数，可通过[查询实例可恢复的时间段]接口进行查询。

        :param restore_time: The restore_time of this RestoreInfo.
        :type restore_time: int
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
        if not isinstance(other, RestoreInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
