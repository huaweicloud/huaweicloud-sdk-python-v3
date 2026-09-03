# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetaLockResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'infos': 'list[MetaLockInfo]',
        'count': 'int',
        'wait_lock_count': 'int',
        'hold_lock_count': 'int',
        'time_greater_than_count': 'int',
        'lock_wait_threshold_second': 'int'
    }

    attribute_map = {
        'infos': 'infos',
        'count': 'count',
        'wait_lock_count': 'wait_lock_count',
        'hold_lock_count': 'hold_lock_count',
        'time_greater_than_count': 'time_greater_than_count',
        'lock_wait_threshold_second': 'lock_wait_threshold_second'
    }

    def __init__(self, infos=None, count=None, wait_lock_count=None, hold_lock_count=None, time_greater_than_count=None, lock_wait_threshold_second=None):
        r"""ShowMetaLockResponse

        The model defined in huaweicloud sdk

        :param infos: MDL锁等待信息
        :type infos: list[:class:`huaweicloudsdkdas.v3.MetaLockInfo`]
        :param count: MDL锁总数量
        :type count: int
        :param wait_lock_count: 等待锁的会话的数量
        :type wait_lock_count: int
        :param hold_lock_count: 持有锁的会话的数量
        :type hold_lock_count: int
        :param time_greater_than_count: 等锁时间大于阈值的会话的数量
        :type time_greater_than_count: int
        :param lock_wait_threshold_second: MDL锁等待时间阈值
        :type lock_wait_threshold_second: int
        """
        
        super().__init__()

        self._infos = None
        self._count = None
        self._wait_lock_count = None
        self._hold_lock_count = None
        self._time_greater_than_count = None
        self._lock_wait_threshold_second = None
        self.discriminator = None

        if infos is not None:
            self.infos = infos
        if count is not None:
            self.count = count
        if wait_lock_count is not None:
            self.wait_lock_count = wait_lock_count
        if hold_lock_count is not None:
            self.hold_lock_count = hold_lock_count
        if time_greater_than_count is not None:
            self.time_greater_than_count = time_greater_than_count
        if lock_wait_threshold_second is not None:
            self.lock_wait_threshold_second = lock_wait_threshold_second

    @property
    def infos(self):
        r"""Gets the infos of this ShowMetaLockResponse.

        MDL锁等待信息

        :return: The infos of this ShowMetaLockResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.MetaLockInfo`]
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        r"""Sets the infos of this ShowMetaLockResponse.

        MDL锁等待信息

        :param infos: The infos of this ShowMetaLockResponse.
        :type infos: list[:class:`huaweicloudsdkdas.v3.MetaLockInfo`]
        """
        self._infos = infos

    @property
    def count(self):
        r"""Gets the count of this ShowMetaLockResponse.

        MDL锁总数量

        :return: The count of this ShowMetaLockResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowMetaLockResponse.

        MDL锁总数量

        :param count: The count of this ShowMetaLockResponse.
        :type count: int
        """
        self._count = count

    @property
    def wait_lock_count(self):
        r"""Gets the wait_lock_count of this ShowMetaLockResponse.

        等待锁的会话的数量

        :return: The wait_lock_count of this ShowMetaLockResponse.
        :rtype: int
        """
        return self._wait_lock_count

    @wait_lock_count.setter
    def wait_lock_count(self, wait_lock_count):
        r"""Sets the wait_lock_count of this ShowMetaLockResponse.

        等待锁的会话的数量

        :param wait_lock_count: The wait_lock_count of this ShowMetaLockResponse.
        :type wait_lock_count: int
        """
        self._wait_lock_count = wait_lock_count

    @property
    def hold_lock_count(self):
        r"""Gets the hold_lock_count of this ShowMetaLockResponse.

        持有锁的会话的数量

        :return: The hold_lock_count of this ShowMetaLockResponse.
        :rtype: int
        """
        return self._hold_lock_count

    @hold_lock_count.setter
    def hold_lock_count(self, hold_lock_count):
        r"""Sets the hold_lock_count of this ShowMetaLockResponse.

        持有锁的会话的数量

        :param hold_lock_count: The hold_lock_count of this ShowMetaLockResponse.
        :type hold_lock_count: int
        """
        self._hold_lock_count = hold_lock_count

    @property
    def time_greater_than_count(self):
        r"""Gets the time_greater_than_count of this ShowMetaLockResponse.

        等锁时间大于阈值的会话的数量

        :return: The time_greater_than_count of this ShowMetaLockResponse.
        :rtype: int
        """
        return self._time_greater_than_count

    @time_greater_than_count.setter
    def time_greater_than_count(self, time_greater_than_count):
        r"""Sets the time_greater_than_count of this ShowMetaLockResponse.

        等锁时间大于阈值的会话的数量

        :param time_greater_than_count: The time_greater_than_count of this ShowMetaLockResponse.
        :type time_greater_than_count: int
        """
        self._time_greater_than_count = time_greater_than_count

    @property
    def lock_wait_threshold_second(self):
        r"""Gets the lock_wait_threshold_second of this ShowMetaLockResponse.

        MDL锁等待时间阈值

        :return: The lock_wait_threshold_second of this ShowMetaLockResponse.
        :rtype: int
        """
        return self._lock_wait_threshold_second

    @lock_wait_threshold_second.setter
    def lock_wait_threshold_second(self, lock_wait_threshold_second):
        r"""Sets the lock_wait_threshold_second of this ShowMetaLockResponse.

        MDL锁等待时间阈值

        :param lock_wait_threshold_second: The lock_wait_threshold_second of this ShowMetaLockResponse.
        :type lock_wait_threshold_second: int
        """
        self._lock_wait_threshold_second = lock_wait_threshold_second

    def to_dict(self):
        import warnings
        warnings.warn("ShowMetaLockResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowMetaLockResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
