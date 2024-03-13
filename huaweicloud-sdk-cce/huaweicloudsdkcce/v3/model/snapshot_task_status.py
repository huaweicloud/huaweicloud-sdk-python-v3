# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SnapshotTaskStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latest_backup_time': 'str'
    }

    attribute_map = {
        'latest_backup_time': 'latestBackupTime'
    }

    def __init__(self, latest_backup_time=None):
        """SnapshotTaskStatus

        The model defined in huaweicloud sdk

        :param latest_backup_time: 最近一次备份的时间
        :type latest_backup_time: str
        """
        
        

        self._latest_backup_time = None
        self.discriminator = None

        if latest_backup_time is not None:
            self.latest_backup_time = latest_backup_time

    @property
    def latest_backup_time(self):
        """Gets the latest_backup_time of this SnapshotTaskStatus.

        最近一次备份的时间

        :return: The latest_backup_time of this SnapshotTaskStatus.
        :rtype: str
        """
        return self._latest_backup_time

    @latest_backup_time.setter
    def latest_backup_time(self, latest_backup_time):
        """Sets the latest_backup_time of this SnapshotTaskStatus.

        最近一次备份的时间

        :param latest_backup_time: The latest_backup_time of this SnapshotTaskStatus.
        :type latest_backup_time: str
        """
        self._latest_backup_time = latest_backup_time

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
        if not isinstance(other, SnapshotTaskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
