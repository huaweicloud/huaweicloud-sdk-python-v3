# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FullDeadLock:

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
        'dead_lock_id': 'str',
        'mysql_dead_lock': 'MySQLDeadLock'
    }

    attribute_map = {
        'happen_time': 'happen_time',
        'dead_lock_id': 'dead_lock_id',
        'mysql_dead_lock': 'mysql_dead_lock'
    }

    def __init__(self, happen_time=None, dead_lock_id=None, mysql_dead_lock=None):
        r"""FullDeadLock

        The model defined in huaweicloud sdk

        :param happen_time: 发生时间（ms）
        :type happen_time: int
        :param dead_lock_id: 死锁ID
        :type dead_lock_id: str
        :param mysql_dead_lock: 
        :type mysql_dead_lock: :class:`huaweicloudsdkdas.v3.MySQLDeadLock`
        """
        
        

        self._happen_time = None
        self._dead_lock_id = None
        self._mysql_dead_lock = None
        self.discriminator = None

        if happen_time is not None:
            self.happen_time = happen_time
        if dead_lock_id is not None:
            self.dead_lock_id = dead_lock_id
        if mysql_dead_lock is not None:
            self.mysql_dead_lock = mysql_dead_lock

    @property
    def happen_time(self):
        r"""Gets the happen_time of this FullDeadLock.

        发生时间（ms）

        :return: The happen_time of this FullDeadLock.
        :rtype: int
        """
        return self._happen_time

    @happen_time.setter
    def happen_time(self, happen_time):
        r"""Sets the happen_time of this FullDeadLock.

        发生时间（ms）

        :param happen_time: The happen_time of this FullDeadLock.
        :type happen_time: int
        """
        self._happen_time = happen_time

    @property
    def dead_lock_id(self):
        r"""Gets the dead_lock_id of this FullDeadLock.

        死锁ID

        :return: The dead_lock_id of this FullDeadLock.
        :rtype: str
        """
        return self._dead_lock_id

    @dead_lock_id.setter
    def dead_lock_id(self, dead_lock_id):
        r"""Sets the dead_lock_id of this FullDeadLock.

        死锁ID

        :param dead_lock_id: The dead_lock_id of this FullDeadLock.
        :type dead_lock_id: str
        """
        self._dead_lock_id = dead_lock_id

    @property
    def mysql_dead_lock(self):
        r"""Gets the mysql_dead_lock of this FullDeadLock.

        :return: The mysql_dead_lock of this FullDeadLock.
        :rtype: :class:`huaweicloudsdkdas.v3.MySQLDeadLock`
        """
        return self._mysql_dead_lock

    @mysql_dead_lock.setter
    def mysql_dead_lock(self, mysql_dead_lock):
        r"""Sets the mysql_dead_lock of this FullDeadLock.

        :param mysql_dead_lock: The mysql_dead_lock of this FullDeadLock.
        :type mysql_dead_lock: :class:`huaweicloudsdkdas.v3.MySQLDeadLock`
        """
        self._mysql_dead_lock = mysql_dead_lock

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FullDeadLock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
