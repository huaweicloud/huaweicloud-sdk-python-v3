# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetTransactionListRespTransactionInfoList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_sec': 'int',
        'wait_locks': 'int',
        'hold_locks': 'int',
        'occurrence_time': 'int',
        'detail': 'str',
        'collect_time': 'int'
    }

    attribute_map = {
        'last_sec': 'last_sec',
        'wait_locks': 'wait_locks',
        'hold_locks': 'hold_locks',
        'occurrence_time': 'occurrence_time',
        'detail': 'detail',
        'collect_time': 'collect_time'
    }

    def __init__(self, last_sec=None, wait_locks=None, hold_locks=None, occurrence_time=None, detail=None, collect_time=None):
        r"""GetTransactionListRespTransactionInfoList

        The model defined in huaweicloud sdk

        :param last_sec: 事务持续时间
        :type last_sec: int
        :param wait_locks: 等待锁数量
        :type wait_locks: int
        :param hold_locks: 持有锁数量
        :type hold_locks: int
        :param occurrence_time: 发生时间
        :type occurrence_time: int
        :param detail: 事务内容
        :type detail: str
        :param collect_time: 收集时间
        :type collect_time: int
        """
        
        

        self._last_sec = None
        self._wait_locks = None
        self._hold_locks = None
        self._occurrence_time = None
        self._detail = None
        self._collect_time = None
        self.discriminator = None

        self.last_sec = last_sec
        self.wait_locks = wait_locks
        self.hold_locks = hold_locks
        self.occurrence_time = occurrence_time
        self.detail = detail
        self.collect_time = collect_time

    @property
    def last_sec(self):
        r"""Gets the last_sec of this GetTransactionListRespTransactionInfoList.

        事务持续时间

        :return: The last_sec of this GetTransactionListRespTransactionInfoList.
        :rtype: int
        """
        return self._last_sec

    @last_sec.setter
    def last_sec(self, last_sec):
        r"""Sets the last_sec of this GetTransactionListRespTransactionInfoList.

        事务持续时间

        :param last_sec: The last_sec of this GetTransactionListRespTransactionInfoList.
        :type last_sec: int
        """
        self._last_sec = last_sec

    @property
    def wait_locks(self):
        r"""Gets the wait_locks of this GetTransactionListRespTransactionInfoList.

        等待锁数量

        :return: The wait_locks of this GetTransactionListRespTransactionInfoList.
        :rtype: int
        """
        return self._wait_locks

    @wait_locks.setter
    def wait_locks(self, wait_locks):
        r"""Sets the wait_locks of this GetTransactionListRespTransactionInfoList.

        等待锁数量

        :param wait_locks: The wait_locks of this GetTransactionListRespTransactionInfoList.
        :type wait_locks: int
        """
        self._wait_locks = wait_locks

    @property
    def hold_locks(self):
        r"""Gets the hold_locks of this GetTransactionListRespTransactionInfoList.

        持有锁数量

        :return: The hold_locks of this GetTransactionListRespTransactionInfoList.
        :rtype: int
        """
        return self._hold_locks

    @hold_locks.setter
    def hold_locks(self, hold_locks):
        r"""Sets the hold_locks of this GetTransactionListRespTransactionInfoList.

        持有锁数量

        :param hold_locks: The hold_locks of this GetTransactionListRespTransactionInfoList.
        :type hold_locks: int
        """
        self._hold_locks = hold_locks

    @property
    def occurrence_time(self):
        r"""Gets the occurrence_time of this GetTransactionListRespTransactionInfoList.

        发生时间

        :return: The occurrence_time of this GetTransactionListRespTransactionInfoList.
        :rtype: int
        """
        return self._occurrence_time

    @occurrence_time.setter
    def occurrence_time(self, occurrence_time):
        r"""Sets the occurrence_time of this GetTransactionListRespTransactionInfoList.

        发生时间

        :param occurrence_time: The occurrence_time of this GetTransactionListRespTransactionInfoList.
        :type occurrence_time: int
        """
        self._occurrence_time = occurrence_time

    @property
    def detail(self):
        r"""Gets the detail of this GetTransactionListRespTransactionInfoList.

        事务内容

        :return: The detail of this GetTransactionListRespTransactionInfoList.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this GetTransactionListRespTransactionInfoList.

        事务内容

        :param detail: The detail of this GetTransactionListRespTransactionInfoList.
        :type detail: str
        """
        self._detail = detail

    @property
    def collect_time(self):
        r"""Gets the collect_time of this GetTransactionListRespTransactionInfoList.

        收集时间

        :return: The collect_time of this GetTransactionListRespTransactionInfoList.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this GetTransactionListRespTransactionInfoList.

        收集时间

        :param collect_time: The collect_time of this GetTransactionListRespTransactionInfoList.
        :type collect_time: int
        """
        self._collect_time = collect_time

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
        if not isinstance(other, GetTransactionListRespTransactionInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
