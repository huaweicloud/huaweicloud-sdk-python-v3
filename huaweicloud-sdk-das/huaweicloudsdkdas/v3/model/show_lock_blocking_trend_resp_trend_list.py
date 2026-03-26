# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLockBlockingTrendRespTrendList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collect_time': 'int',
        'total_lock_blocking_count': 'int',
        'async_io_completion_count': 'int',
        'async_network_io_count': 'int',
        'cxconsumer_count': 'int',
        'cxpacket_count': 'int',
        'dtc_count': 'int',
        'lck_m_bu_count': 'int',
        'lck_m_is_count': 'int',
        'lck_m_iu_count': 'int',
        'lck_m_ix_count': 'int',
        'other_count': 'int'
    }

    attribute_map = {
        'collect_time': 'collect_time',
        'total_lock_blocking_count': 'total_lock_blocking_count',
        'async_io_completion_count': 'async_io_completion_count',
        'async_network_io_count': 'async_network_io_count',
        'cxconsumer_count': 'cxconsumer_count',
        'cxpacket_count': 'cxpacket_count',
        'dtc_count': 'dtc_count',
        'lck_m_bu_count': 'lck_m_bu_count',
        'lck_m_is_count': 'lck_m_is_count',
        'lck_m_iu_count': 'lck_m_iu_count',
        'lck_m_ix_count': 'lck_m_ix_count',
        'other_count': 'other_count'
    }

    def __init__(self, collect_time=None, total_lock_blocking_count=None, async_io_completion_count=None, async_network_io_count=None, cxconsumer_count=None, cxpacket_count=None, dtc_count=None, lck_m_bu_count=None, lck_m_is_count=None, lck_m_iu_count=None, lck_m_ix_count=None, other_count=None):
        r"""ShowLockBlockingTrendRespTrendList

        The model defined in huaweicloud sdk

        :param collect_time: 采集时间
        :type collect_time: int
        :param total_lock_blocking_count: 锁阻塞总数
        :type total_lock_blocking_count: int
        :param async_io_completion_count: ASYNC_IO_COMPLETION数量
        :type async_io_completion_count: int
        :param async_network_io_count: ASYNC_NETWORK_IO数量
        :type async_network_io_count: int
        :param cxconsumer_count: CXCONSUMER数量
        :type cxconsumer_count: int
        :param cxpacket_count: CXPACKET数量
        :type cxpacket_count: int
        :param dtc_count: DTC数量
        :type dtc_count: int
        :param lck_m_bu_count: LCK_M_BU数量
        :type lck_m_bu_count: int
        :param lck_m_is_count: LCK_M_IS数量
        :type lck_m_is_count: int
        :param lck_m_iu_count: LCK_M_IU数量
        :type lck_m_iu_count: int
        :param lck_m_ix_count: LCK_M_IX数量
        :type lck_m_ix_count: int
        :param other_count: 其他锁阻塞数量
        :type other_count: int
        """
        
        

        self._collect_time = None
        self._total_lock_blocking_count = None
        self._async_io_completion_count = None
        self._async_network_io_count = None
        self._cxconsumer_count = None
        self._cxpacket_count = None
        self._dtc_count = None
        self._lck_m_bu_count = None
        self._lck_m_is_count = None
        self._lck_m_iu_count = None
        self._lck_m_ix_count = None
        self._other_count = None
        self.discriminator = None

        if collect_time is not None:
            self.collect_time = collect_time
        if total_lock_blocking_count is not None:
            self.total_lock_blocking_count = total_lock_blocking_count
        if async_io_completion_count is not None:
            self.async_io_completion_count = async_io_completion_count
        if async_network_io_count is not None:
            self.async_network_io_count = async_network_io_count
        if cxconsumer_count is not None:
            self.cxconsumer_count = cxconsumer_count
        if cxpacket_count is not None:
            self.cxpacket_count = cxpacket_count
        if dtc_count is not None:
            self.dtc_count = dtc_count
        if lck_m_bu_count is not None:
            self.lck_m_bu_count = lck_m_bu_count
        if lck_m_is_count is not None:
            self.lck_m_is_count = lck_m_is_count
        if lck_m_iu_count is not None:
            self.lck_m_iu_count = lck_m_iu_count
        if lck_m_ix_count is not None:
            self.lck_m_ix_count = lck_m_ix_count
        if other_count is not None:
            self.other_count = other_count

    @property
    def collect_time(self):
        r"""Gets the collect_time of this ShowLockBlockingTrendRespTrendList.

        采集时间

        :return: The collect_time of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this ShowLockBlockingTrendRespTrendList.

        采集时间

        :param collect_time: The collect_time of this ShowLockBlockingTrendRespTrendList.
        :type collect_time: int
        """
        self._collect_time = collect_time

    @property
    def total_lock_blocking_count(self):
        r"""Gets the total_lock_blocking_count of this ShowLockBlockingTrendRespTrendList.

        锁阻塞总数

        :return: The total_lock_blocking_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._total_lock_blocking_count

    @total_lock_blocking_count.setter
    def total_lock_blocking_count(self, total_lock_blocking_count):
        r"""Sets the total_lock_blocking_count of this ShowLockBlockingTrendRespTrendList.

        锁阻塞总数

        :param total_lock_blocking_count: The total_lock_blocking_count of this ShowLockBlockingTrendRespTrendList.
        :type total_lock_blocking_count: int
        """
        self._total_lock_blocking_count = total_lock_blocking_count

    @property
    def async_io_completion_count(self):
        r"""Gets the async_io_completion_count of this ShowLockBlockingTrendRespTrendList.

        ASYNC_IO_COMPLETION数量

        :return: The async_io_completion_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._async_io_completion_count

    @async_io_completion_count.setter
    def async_io_completion_count(self, async_io_completion_count):
        r"""Sets the async_io_completion_count of this ShowLockBlockingTrendRespTrendList.

        ASYNC_IO_COMPLETION数量

        :param async_io_completion_count: The async_io_completion_count of this ShowLockBlockingTrendRespTrendList.
        :type async_io_completion_count: int
        """
        self._async_io_completion_count = async_io_completion_count

    @property
    def async_network_io_count(self):
        r"""Gets the async_network_io_count of this ShowLockBlockingTrendRespTrendList.

        ASYNC_NETWORK_IO数量

        :return: The async_network_io_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._async_network_io_count

    @async_network_io_count.setter
    def async_network_io_count(self, async_network_io_count):
        r"""Sets the async_network_io_count of this ShowLockBlockingTrendRespTrendList.

        ASYNC_NETWORK_IO数量

        :param async_network_io_count: The async_network_io_count of this ShowLockBlockingTrendRespTrendList.
        :type async_network_io_count: int
        """
        self._async_network_io_count = async_network_io_count

    @property
    def cxconsumer_count(self):
        r"""Gets the cxconsumer_count of this ShowLockBlockingTrendRespTrendList.

        CXCONSUMER数量

        :return: The cxconsumer_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._cxconsumer_count

    @cxconsumer_count.setter
    def cxconsumer_count(self, cxconsumer_count):
        r"""Sets the cxconsumer_count of this ShowLockBlockingTrendRespTrendList.

        CXCONSUMER数量

        :param cxconsumer_count: The cxconsumer_count of this ShowLockBlockingTrendRespTrendList.
        :type cxconsumer_count: int
        """
        self._cxconsumer_count = cxconsumer_count

    @property
    def cxpacket_count(self):
        r"""Gets the cxpacket_count of this ShowLockBlockingTrendRespTrendList.

        CXPACKET数量

        :return: The cxpacket_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._cxpacket_count

    @cxpacket_count.setter
    def cxpacket_count(self, cxpacket_count):
        r"""Sets the cxpacket_count of this ShowLockBlockingTrendRespTrendList.

        CXPACKET数量

        :param cxpacket_count: The cxpacket_count of this ShowLockBlockingTrendRespTrendList.
        :type cxpacket_count: int
        """
        self._cxpacket_count = cxpacket_count

    @property
    def dtc_count(self):
        r"""Gets the dtc_count of this ShowLockBlockingTrendRespTrendList.

        DTC数量

        :return: The dtc_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._dtc_count

    @dtc_count.setter
    def dtc_count(self, dtc_count):
        r"""Sets the dtc_count of this ShowLockBlockingTrendRespTrendList.

        DTC数量

        :param dtc_count: The dtc_count of this ShowLockBlockingTrendRespTrendList.
        :type dtc_count: int
        """
        self._dtc_count = dtc_count

    @property
    def lck_m_bu_count(self):
        r"""Gets the lck_m_bu_count of this ShowLockBlockingTrendRespTrendList.

        LCK_M_BU数量

        :return: The lck_m_bu_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._lck_m_bu_count

    @lck_m_bu_count.setter
    def lck_m_bu_count(self, lck_m_bu_count):
        r"""Sets the lck_m_bu_count of this ShowLockBlockingTrendRespTrendList.

        LCK_M_BU数量

        :param lck_m_bu_count: The lck_m_bu_count of this ShowLockBlockingTrendRespTrendList.
        :type lck_m_bu_count: int
        """
        self._lck_m_bu_count = lck_m_bu_count

    @property
    def lck_m_is_count(self):
        r"""Gets the lck_m_is_count of this ShowLockBlockingTrendRespTrendList.

        LCK_M_IS数量

        :return: The lck_m_is_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._lck_m_is_count

    @lck_m_is_count.setter
    def lck_m_is_count(self, lck_m_is_count):
        r"""Sets the lck_m_is_count of this ShowLockBlockingTrendRespTrendList.

        LCK_M_IS数量

        :param lck_m_is_count: The lck_m_is_count of this ShowLockBlockingTrendRespTrendList.
        :type lck_m_is_count: int
        """
        self._lck_m_is_count = lck_m_is_count

    @property
    def lck_m_iu_count(self):
        r"""Gets the lck_m_iu_count of this ShowLockBlockingTrendRespTrendList.

        LCK_M_IU数量

        :return: The lck_m_iu_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._lck_m_iu_count

    @lck_m_iu_count.setter
    def lck_m_iu_count(self, lck_m_iu_count):
        r"""Sets the lck_m_iu_count of this ShowLockBlockingTrendRespTrendList.

        LCK_M_IU数量

        :param lck_m_iu_count: The lck_m_iu_count of this ShowLockBlockingTrendRespTrendList.
        :type lck_m_iu_count: int
        """
        self._lck_m_iu_count = lck_m_iu_count

    @property
    def lck_m_ix_count(self):
        r"""Gets the lck_m_ix_count of this ShowLockBlockingTrendRespTrendList.

        LCK_M_IX数量

        :return: The lck_m_ix_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._lck_m_ix_count

    @lck_m_ix_count.setter
    def lck_m_ix_count(self, lck_m_ix_count):
        r"""Sets the lck_m_ix_count of this ShowLockBlockingTrendRespTrendList.

        LCK_M_IX数量

        :param lck_m_ix_count: The lck_m_ix_count of this ShowLockBlockingTrendRespTrendList.
        :type lck_m_ix_count: int
        """
        self._lck_m_ix_count = lck_m_ix_count

    @property
    def other_count(self):
        r"""Gets the other_count of this ShowLockBlockingTrendRespTrendList.

        其他锁阻塞数量

        :return: The other_count of this ShowLockBlockingTrendRespTrendList.
        :rtype: int
        """
        return self._other_count

    @other_count.setter
    def other_count(self, other_count):
        r"""Sets the other_count of this ShowLockBlockingTrendRespTrendList.

        其他锁阻塞数量

        :param other_count: The other_count of this ShowLockBlockingTrendRespTrendList.
        :type other_count: int
        """
        self._other_count = other_count

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
        if not isinstance(other, ShowLockBlockingTrendRespTrendList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
