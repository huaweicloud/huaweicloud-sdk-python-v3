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
        'restore_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'type': 'type',
        'backup_id': 'backup_id',
        'restore_time': 'restore_time'
    }

    def __init__(self, instance_id=None, type=None, backup_id=None, restore_time=None):
        r"""RecoveryBackupSource

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param type: 恢复备份类型：backup，timestamp，different
        :type type: str
        :param backup_id: 用于恢复的备份ID。
        :type backup_id: str
        :param restore_time: UTC时间，时间戳
        :type restore_time: str
        """
        
        

        self._instance_id = None
        self._type = None
        self._backup_id = None
        self._restore_time = None
        self.discriminator = None

        self.instance_id = instance_id
        self.type = type
        if backup_id is not None:
            self.backup_id = backup_id
        if restore_time is not None:
            self.restore_time = restore_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RecoveryBackupSource.

        实例ID

        :return: The instance_id of this RecoveryBackupSource.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RecoveryBackupSource.

        实例ID

        :param instance_id: The instance_id of this RecoveryBackupSource.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def type(self):
        r"""Gets the type of this RecoveryBackupSource.

        恢复备份类型：backup，timestamp，different

        :return: The type of this RecoveryBackupSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RecoveryBackupSource.

        恢复备份类型：backup，timestamp，different

        :param type: The type of this RecoveryBackupSource.
        :type type: str
        """
        self._type = type

    @property
    def backup_id(self):
        r"""Gets the backup_id of this RecoveryBackupSource.

        用于恢复的备份ID。

        :return: The backup_id of this RecoveryBackupSource.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RecoveryBackupSource.

        用于恢复的备份ID。

        :param backup_id: The backup_id of this RecoveryBackupSource.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def restore_time(self):
        r"""Gets the restore_time of this RecoveryBackupSource.

        UTC时间，时间戳

        :return: The restore_time of this RecoveryBackupSource.
        :rtype: str
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        r"""Sets the restore_time of this RecoveryBackupSource.

        UTC时间，时间戳

        :param restore_time: The restore_time of this RecoveryBackupSource.
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
        if not isinstance(other, RecoveryBackupSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
