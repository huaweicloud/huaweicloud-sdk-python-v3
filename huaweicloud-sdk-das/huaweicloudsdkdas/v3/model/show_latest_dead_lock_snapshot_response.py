# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestDeadLockSnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mysql_dead_lock': 'QueryLatestDeadLockRespMysqlDeadLock',
        'find_lock': 'bool',
        'happen_time': 'int'
    }

    attribute_map = {
        'mysql_dead_lock': 'mysql_dead_lock',
        'find_lock': 'find_lock',
        'happen_time': 'happen_time'
    }

    def __init__(self, mysql_dead_lock=None, find_lock=None, happen_time=None):
        r"""ShowLatestDeadLockSnapshotResponse

        The model defined in huaweicloud sdk

        :param mysql_dead_lock: 
        :type mysql_dead_lock: :class:`huaweicloudsdkdas.v3.QueryLatestDeadLockRespMysqlDeadLock`
        :param find_lock: 表示系统是否成功检测到死锁事件
        :type find_lock: bool
        :param happen_time: 死锁事件发生的 Unix 时间戳
        :type happen_time: int
        """
        
        super(ShowLatestDeadLockSnapshotResponse, self).__init__()

        self._mysql_dead_lock = None
        self._find_lock = None
        self._happen_time = None
        self.discriminator = None

        if mysql_dead_lock is not None:
            self.mysql_dead_lock = mysql_dead_lock
        if find_lock is not None:
            self.find_lock = find_lock
        if happen_time is not None:
            self.happen_time = happen_time

    @property
    def mysql_dead_lock(self):
        r"""Gets the mysql_dead_lock of this ShowLatestDeadLockSnapshotResponse.

        :return: The mysql_dead_lock of this ShowLatestDeadLockSnapshotResponse.
        :rtype: :class:`huaweicloudsdkdas.v3.QueryLatestDeadLockRespMysqlDeadLock`
        """
        return self._mysql_dead_lock

    @mysql_dead_lock.setter
    def mysql_dead_lock(self, mysql_dead_lock):
        r"""Sets the mysql_dead_lock of this ShowLatestDeadLockSnapshotResponse.

        :param mysql_dead_lock: The mysql_dead_lock of this ShowLatestDeadLockSnapshotResponse.
        :type mysql_dead_lock: :class:`huaweicloudsdkdas.v3.QueryLatestDeadLockRespMysqlDeadLock`
        """
        self._mysql_dead_lock = mysql_dead_lock

    @property
    def find_lock(self):
        r"""Gets the find_lock of this ShowLatestDeadLockSnapshotResponse.

        表示系统是否成功检测到死锁事件

        :return: The find_lock of this ShowLatestDeadLockSnapshotResponse.
        :rtype: bool
        """
        return self._find_lock

    @find_lock.setter
    def find_lock(self, find_lock):
        r"""Sets the find_lock of this ShowLatestDeadLockSnapshotResponse.

        表示系统是否成功检测到死锁事件

        :param find_lock: The find_lock of this ShowLatestDeadLockSnapshotResponse.
        :type find_lock: bool
        """
        self._find_lock = find_lock

    @property
    def happen_time(self):
        r"""Gets the happen_time of this ShowLatestDeadLockSnapshotResponse.

        死锁事件发生的 Unix 时间戳

        :return: The happen_time of this ShowLatestDeadLockSnapshotResponse.
        :rtype: int
        """
        return self._happen_time

    @happen_time.setter
    def happen_time(self, happen_time):
        r"""Sets the happen_time of this ShowLatestDeadLockSnapshotResponse.

        死锁事件发生的 Unix 时间戳

        :param happen_time: The happen_time of this ShowLatestDeadLockSnapshotResponse.
        :type happen_time: int
        """
        self._happen_time = happen_time

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
        if not isinstance(other, ShowLatestDeadLockSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
