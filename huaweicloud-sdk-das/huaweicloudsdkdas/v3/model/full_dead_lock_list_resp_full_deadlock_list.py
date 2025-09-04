# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullDeadLockListRespFullDeadlockList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'happen_time': 'int',
        'mysql_deadlock': 'FullDeadLockListRespMysqlDeadlock'
    }

    attribute_map = {
        'happen_time': 'happen_time',
        'mysql_deadlock': 'mysql_deadlock'
    }

    def __init__(self, happen_time=None, mysql_deadlock=None):
        r"""FullDeadLockListRespFullDeadlockList

        The model defined in huaweicloud sdk

        :param happen_time: 死锁事件发生的 Unix 时间戳（毫秒级）
        :type happen_time: int
        :param mysql_deadlock: 
        :type mysql_deadlock: :class:`huaweicloudsdkdas.v3.FullDeadLockListRespMysqlDeadlock`
        """
        
        

        self._happen_time = None
        self._mysql_deadlock = None
        self.discriminator = None

        if happen_time is not None:
            self.happen_time = happen_time
        if mysql_deadlock is not None:
            self.mysql_deadlock = mysql_deadlock

    @property
    def happen_time(self):
        r"""Gets the happen_time of this FullDeadLockListRespFullDeadlockList.

        死锁事件发生的 Unix 时间戳（毫秒级）

        :return: The happen_time of this FullDeadLockListRespFullDeadlockList.
        :rtype: int
        """
        return self._happen_time

    @happen_time.setter
    def happen_time(self, happen_time):
        r"""Sets the happen_time of this FullDeadLockListRespFullDeadlockList.

        死锁事件发生的 Unix 时间戳（毫秒级）

        :param happen_time: The happen_time of this FullDeadLockListRespFullDeadlockList.
        :type happen_time: int
        """
        self._happen_time = happen_time

    @property
    def mysql_deadlock(self):
        r"""Gets the mysql_deadlock of this FullDeadLockListRespFullDeadlockList.

        :return: The mysql_deadlock of this FullDeadLockListRespFullDeadlockList.
        :rtype: :class:`huaweicloudsdkdas.v3.FullDeadLockListRespMysqlDeadlock`
        """
        return self._mysql_deadlock

    @mysql_deadlock.setter
    def mysql_deadlock(self, mysql_deadlock):
        r"""Sets the mysql_deadlock of this FullDeadLockListRespFullDeadlockList.

        :param mysql_deadlock: The mysql_deadlock of this FullDeadLockListRespFullDeadlockList.
        :type mysql_deadlock: :class:`huaweicloudsdkdas.v3.FullDeadLockListRespMysqlDeadlock`
        """
        self._mysql_deadlock = mysql_deadlock

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
        if not isinstance(other, FullDeadLockListRespFullDeadlockList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
