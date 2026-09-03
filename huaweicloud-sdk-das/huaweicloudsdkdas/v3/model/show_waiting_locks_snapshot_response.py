# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWaitingLocksSnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'trx': 'list[InnodbTrxInfo]',
        'lock_waits_infos': 'list[object]',
        'wait_lock_count': 'int',
        'hold_lock_count': 'int',
        'time_greater_than_count': 'int',
        'lock_wait_threshold_second': 'int'
    }

    attribute_map = {
        'trx': 'trx',
        'lock_waits_infos': 'lock_waits_infos',
        'wait_lock_count': 'wait_lock_count',
        'hold_lock_count': 'hold_lock_count',
        'time_greater_than_count': 'time_greater_than_count',
        'lock_wait_threshold_second': 'lock_wait_threshold_second'
    }

    def __init__(self, trx=None, lock_waits_infos=None, wait_lock_count=None, hold_lock_count=None, time_greater_than_count=None, lock_wait_threshold_second=None):
        r"""ShowWaitingLocksSnapshotResponse

        The model defined in huaweicloud sdk

        :param trx: InnoDB锁对应的事务的信息
        :type trx: list[:class:`huaweicloudsdkdas.v3.InnodbTrxInfo`]
        :param lock_waits_infos: InnoDB锁等待信息
        :type lock_waits_infos: list[object]
        :param wait_lock_count: 等待锁的会话的数量
        :type wait_lock_count: int
        :param hold_lock_count: 持有锁的会话的数量
        :type hold_lock_count: int
        :param time_greater_than_count: 等锁时间大于阈值的会话的数量
        :type time_greater_than_count: int
        :param lock_wait_threshold_second: InnoDB锁等待时间阈值
        :type lock_wait_threshold_second: int
        """
        
        super().__init__()

        self._trx = None
        self._lock_waits_infos = None
        self._wait_lock_count = None
        self._hold_lock_count = None
        self._time_greater_than_count = None
        self._lock_wait_threshold_second = None
        self.discriminator = None

        if trx is not None:
            self.trx = trx
        if lock_waits_infos is not None:
            self.lock_waits_infos = lock_waits_infos
        if wait_lock_count is not None:
            self.wait_lock_count = wait_lock_count
        if hold_lock_count is not None:
            self.hold_lock_count = hold_lock_count
        if time_greater_than_count is not None:
            self.time_greater_than_count = time_greater_than_count
        if lock_wait_threshold_second is not None:
            self.lock_wait_threshold_second = lock_wait_threshold_second

    @property
    def trx(self):
        r"""Gets the trx of this ShowWaitingLocksSnapshotResponse.

        InnoDB锁对应的事务的信息

        :return: The trx of this ShowWaitingLocksSnapshotResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InnodbTrxInfo`]
        """
        return self._trx

    @trx.setter
    def trx(self, trx):
        r"""Sets the trx of this ShowWaitingLocksSnapshotResponse.

        InnoDB锁对应的事务的信息

        :param trx: The trx of this ShowWaitingLocksSnapshotResponse.
        :type trx: list[:class:`huaweicloudsdkdas.v3.InnodbTrxInfo`]
        """
        self._trx = trx

    @property
    def lock_waits_infos(self):
        r"""Gets the lock_waits_infos of this ShowWaitingLocksSnapshotResponse.

        InnoDB锁等待信息

        :return: The lock_waits_infos of this ShowWaitingLocksSnapshotResponse.
        :rtype: list[object]
        """
        return self._lock_waits_infos

    @lock_waits_infos.setter
    def lock_waits_infos(self, lock_waits_infos):
        r"""Sets the lock_waits_infos of this ShowWaitingLocksSnapshotResponse.

        InnoDB锁等待信息

        :param lock_waits_infos: The lock_waits_infos of this ShowWaitingLocksSnapshotResponse.
        :type lock_waits_infos: list[object]
        """
        self._lock_waits_infos = lock_waits_infos

    @property
    def wait_lock_count(self):
        r"""Gets the wait_lock_count of this ShowWaitingLocksSnapshotResponse.

        等待锁的会话的数量

        :return: The wait_lock_count of this ShowWaitingLocksSnapshotResponse.
        :rtype: int
        """
        return self._wait_lock_count

    @wait_lock_count.setter
    def wait_lock_count(self, wait_lock_count):
        r"""Sets the wait_lock_count of this ShowWaitingLocksSnapshotResponse.

        等待锁的会话的数量

        :param wait_lock_count: The wait_lock_count of this ShowWaitingLocksSnapshotResponse.
        :type wait_lock_count: int
        """
        self._wait_lock_count = wait_lock_count

    @property
    def hold_lock_count(self):
        r"""Gets the hold_lock_count of this ShowWaitingLocksSnapshotResponse.

        持有锁的会话的数量

        :return: The hold_lock_count of this ShowWaitingLocksSnapshotResponse.
        :rtype: int
        """
        return self._hold_lock_count

    @hold_lock_count.setter
    def hold_lock_count(self, hold_lock_count):
        r"""Sets the hold_lock_count of this ShowWaitingLocksSnapshotResponse.

        持有锁的会话的数量

        :param hold_lock_count: The hold_lock_count of this ShowWaitingLocksSnapshotResponse.
        :type hold_lock_count: int
        """
        self._hold_lock_count = hold_lock_count

    @property
    def time_greater_than_count(self):
        r"""Gets the time_greater_than_count of this ShowWaitingLocksSnapshotResponse.

        等锁时间大于阈值的会话的数量

        :return: The time_greater_than_count of this ShowWaitingLocksSnapshotResponse.
        :rtype: int
        """
        return self._time_greater_than_count

    @time_greater_than_count.setter
    def time_greater_than_count(self, time_greater_than_count):
        r"""Sets the time_greater_than_count of this ShowWaitingLocksSnapshotResponse.

        等锁时间大于阈值的会话的数量

        :param time_greater_than_count: The time_greater_than_count of this ShowWaitingLocksSnapshotResponse.
        :type time_greater_than_count: int
        """
        self._time_greater_than_count = time_greater_than_count

    @property
    def lock_wait_threshold_second(self):
        r"""Gets the lock_wait_threshold_second of this ShowWaitingLocksSnapshotResponse.

        InnoDB锁等待时间阈值

        :return: The lock_wait_threshold_second of this ShowWaitingLocksSnapshotResponse.
        :rtype: int
        """
        return self._lock_wait_threshold_second

    @lock_wait_threshold_second.setter
    def lock_wait_threshold_second(self, lock_wait_threshold_second):
        r"""Sets the lock_wait_threshold_second of this ShowWaitingLocksSnapshotResponse.

        InnoDB锁等待时间阈值

        :param lock_wait_threshold_second: The lock_wait_threshold_second of this ShowWaitingLocksSnapshotResponse.
        :type lock_wait_threshold_second: int
        """
        self._lock_wait_threshold_second = lock_wait_threshold_second

    def to_dict(self):
        import warnings
        warnings.warn("ShowWaitingLocksSnapshotResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowWaitingLocksSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
