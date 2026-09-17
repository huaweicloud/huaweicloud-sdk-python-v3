# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLatestSpaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_time': 'int',
        'buy_storage_bytes': 'int',
        'used_storage_bytes': 'int',
        'last_storage_bytes': 'int',
        'buy_storage_percent': 'float',
        'data_usage_bytes': 'int',
        'data_usage_percent': 'float',
        'binlog_usage_bytes': 'int',
        'binlog_usage_percent': 'float',
        'relay_log_usage_bytes': 'int',
        'relay_log_usage_percent': 'float',
        'audit_log_usage_bytes': 'int',
        'audit_log_usage_percent': 'float',
        'slow_log_usage_bytes': 'int',
        'slow_log_usage_percent': 'float',
        'temp_usage_bytes': 'int',
        'temp_usage_percent': 'float',
        'undo_log_usage_bytes': 'int',
        'undo_log_usage_percent': 'float',
        'other_usage_bytes': 'int',
        'other_usage_percent': 'float',
        'too_many_files': 'bool',
        'page_usage_bytes': 'float',
        'total_space': 'int',
        'total_usage': 'int',
        'avail_size': 'int',
        'data': 'float',
        'log': 'float',
        'runtime': 'float',
        'slow_log': 'float',
        'audit_log': 'float',
        'tempdb': 'float',
        'msdb': 'float',
        'used_size_bytes': 'int',
        'total_size_bytes': 'int',
        'avg_daily_growth_bytes': 'float',
        'estimated_available_days': 'int',
        'data_size_bytes': 'int',
        'oplog_size_bytes': 'int',
        'other_size_bytes': 'int',
        'wal_size': 'float',
        'data_size': 'float',
        'pgaudit_log_size': 'float',
        'pgsql_tmp_size': 'float'
    }

    attribute_map = {
        'update_time': 'update_time',
        'buy_storage_bytes': 'buy_storage_bytes',
        'used_storage_bytes': 'used_storage_bytes',
        'last_storage_bytes': 'last_storage_bytes',
        'buy_storage_percent': 'buy_storage_percent',
        'data_usage_bytes': 'data_usage_bytes',
        'data_usage_percent': 'data_usage_percent',
        'binlog_usage_bytes': 'binlog_usage_bytes',
        'binlog_usage_percent': 'binlog_usage_percent',
        'relay_log_usage_bytes': 'relay_log_usage_bytes',
        'relay_log_usage_percent': 'relay_log_usage_percent',
        'audit_log_usage_bytes': 'audit_log_usage_bytes',
        'audit_log_usage_percent': 'audit_log_usage_percent',
        'slow_log_usage_bytes': 'slow_log_usage_bytes',
        'slow_log_usage_percent': 'slow_log_usage_percent',
        'temp_usage_bytes': 'temp_usage_bytes',
        'temp_usage_percent': 'temp_usage_percent',
        'undo_log_usage_bytes': 'undo_log_usage_bytes',
        'undo_log_usage_percent': 'undo_log_usage_percent',
        'other_usage_bytes': 'other_usage_bytes',
        'other_usage_percent': 'other_usage_percent',
        'too_many_files': 'too_many_files',
        'page_usage_bytes': 'page_usage_bytes',
        'total_space': 'total_space',
        'total_usage': 'total_usage',
        'avail_size': 'avail_size',
        'data': 'data',
        'log': 'log',
        'runtime': 'runtime',
        'slow_log': 'slow_log',
        'audit_log': 'audit_log',
        'tempdb': 'tempdb',
        'msdb': 'msdb',
        'used_size_bytes': 'used_size_bytes',
        'total_size_bytes': 'total_size_bytes',
        'avg_daily_growth_bytes': 'avg_daily_growth_bytes',
        'estimated_available_days': 'estimated_available_days',
        'data_size_bytes': 'data_size_bytes',
        'oplog_size_bytes': 'oplog_size_bytes',
        'other_size_bytes': 'other_size_bytes',
        'wal_size': 'wal_size',
        'data_size': 'data_size',
        'pgaudit_log_size': 'pgaudit_log_size',
        'pgsql_tmp_size': 'pgsql_tmp_size'
    }

    def __init__(self, update_time=None, buy_storage_bytes=None, used_storage_bytes=None, last_storage_bytes=None, buy_storage_percent=None, data_usage_bytes=None, data_usage_percent=None, binlog_usage_bytes=None, binlog_usage_percent=None, relay_log_usage_bytes=None, relay_log_usage_percent=None, audit_log_usage_bytes=None, audit_log_usage_percent=None, slow_log_usage_bytes=None, slow_log_usage_percent=None, temp_usage_bytes=None, temp_usage_percent=None, undo_log_usage_bytes=None, undo_log_usage_percent=None, other_usage_bytes=None, other_usage_percent=None, too_many_files=None, page_usage_bytes=None, total_space=None, total_usage=None, avail_size=None, data=None, log=None, runtime=None, slow_log=None, audit_log=None, tempdb=None, msdb=None, used_size_bytes=None, total_size_bytes=None, avg_daily_growth_bytes=None, estimated_available_days=None, data_size_bytes=None, oplog_size_bytes=None, other_size_bytes=None, wal_size=None, data_size=None, pgaudit_log_size=None, pgsql_tmp_size=None):
        r"""ShowLatestSpaceResponse

        The model defined in huaweicloud sdk

        :param update_time: 更新时间
        :type update_time: int
        :param buy_storage_bytes: MySQL购买空间
        :type buy_storage_bytes: int
        :param used_storage_bytes: MySQL已使用空间
        :type used_storage_bytes: int
        :param last_storage_bytes: MySQL剩余空间
        :type last_storage_bytes: int
        :param buy_storage_percent: MySQL使用空间占比
        :type buy_storage_percent: float
        :param data_usage_bytes: 数据空间
        :type data_usage_bytes: int
        :param data_usage_percent: 数据空间占比
        :type data_usage_percent: float
        :param binlog_usage_bytes: binlog空间
        :type binlog_usage_bytes: int
        :param binlog_usage_percent: binlog空间占比
        :type binlog_usage_percent: float
        :param relay_log_usage_bytes: relayLog空间
        :type relay_log_usage_bytes: int
        :param relay_log_usage_percent: relayLog空间占比
        :type relay_log_usage_percent: float
        :param audit_log_usage_bytes: auditLog空间
        :type audit_log_usage_bytes: int
        :param audit_log_usage_percent: auditLog空间占比
        :type audit_log_usage_percent: float
        :param slow_log_usage_bytes: slowLog空间
        :type slow_log_usage_bytes: int
        :param slow_log_usage_percent: slowLog空间占比
        :type slow_log_usage_percent: float
        :param temp_usage_bytes: 临时空间
        :type temp_usage_bytes: int
        :param temp_usage_percent: 临时空间占比
        :type temp_usage_percent: float
        :param undo_log_usage_bytes: undoLog空间
        :type undo_log_usage_bytes: int
        :param undo_log_usage_percent: undoLog空间占比
        :type undo_log_usage_percent: float
        :param other_usage_bytes: 其他空间
        :type other_usage_bytes: int
        :param other_usage_percent: 其他空间占比
        :type other_usage_percent: float
        :param too_many_files: 是否文件过多
        :type too_many_files: bool
        :param page_usage_bytes: TaurusDB数据空间
        :type page_usage_bytes: float
        :param total_space: SQLServer总空间
        :type total_space: int
        :param total_usage: SQLServer已使用空间
        :type total_usage: int
        :param avail_size: SQLServer可用空间
        :type avail_size: int
        :param data: SQLServer数据空间
        :type data: float
        :param log: SQLServer log空间
        :type log: float
        :param runtime: SQLServer runtime
        :type runtime: float
        :param slow_log: SQLServer slow_log空间
        :type slow_log: float
        :param audit_log: SQLServer audit_log空间
        :type audit_log: float
        :param tempdb: SQLServer tempdb空间
        :type tempdb: float
        :param msdb: SQLServer msdb空间
        :type msdb: float
        :param used_size_bytes: DDS磁盘使用量
        :type used_size_bytes: int
        :param total_size_bytes: DDS磁盘总量
        :type total_size_bytes: int
        :param avg_daily_growth_bytes: DDS近一周日均增长
        :type avg_daily_growth_bytes: float
        :param estimated_available_days: DDS预计可用天数
        :type estimated_available_days: int
        :param data_size_bytes: DDS数据空间
        :type data_size_bytes: int
        :param oplog_size_bytes: DDS oplog空间
        :type oplog_size_bytes: int
        :param other_size_bytes: DDS其他空间
        :type other_size_bytes: int
        :param wal_size: PostgreSQL wallog空间
        :type wal_size: float
        :param data_size: PostgreSQL数据空间
        :type data_size: float
        :param pgaudit_log_size: PostgreSQL auditlog空间
        :type pgaudit_log_size: float
        :param pgsql_tmp_size: PostgreSQL临时空间
        :type pgsql_tmp_size: float
        """
        
        super().__init__()

        self._update_time = None
        self._buy_storage_bytes = None
        self._used_storage_bytes = None
        self._last_storage_bytes = None
        self._buy_storage_percent = None
        self._data_usage_bytes = None
        self._data_usage_percent = None
        self._binlog_usage_bytes = None
        self._binlog_usage_percent = None
        self._relay_log_usage_bytes = None
        self._relay_log_usage_percent = None
        self._audit_log_usage_bytes = None
        self._audit_log_usage_percent = None
        self._slow_log_usage_bytes = None
        self._slow_log_usage_percent = None
        self._temp_usage_bytes = None
        self._temp_usage_percent = None
        self._undo_log_usage_bytes = None
        self._undo_log_usage_percent = None
        self._other_usage_bytes = None
        self._other_usage_percent = None
        self._too_many_files = None
        self._page_usage_bytes = None
        self._total_space = None
        self._total_usage = None
        self._avail_size = None
        self._data = None
        self._log = None
        self._runtime = None
        self._slow_log = None
        self._audit_log = None
        self._tempdb = None
        self._msdb = None
        self._used_size_bytes = None
        self._total_size_bytes = None
        self._avg_daily_growth_bytes = None
        self._estimated_available_days = None
        self._data_size_bytes = None
        self._oplog_size_bytes = None
        self._other_size_bytes = None
        self._wal_size = None
        self._data_size = None
        self._pgaudit_log_size = None
        self._pgsql_tmp_size = None
        self.discriminator = None

        if update_time is not None:
            self.update_time = update_time
        if buy_storage_bytes is not None:
            self.buy_storage_bytes = buy_storage_bytes
        if used_storage_bytes is not None:
            self.used_storage_bytes = used_storage_bytes
        if last_storage_bytes is not None:
            self.last_storage_bytes = last_storage_bytes
        if buy_storage_percent is not None:
            self.buy_storage_percent = buy_storage_percent
        if data_usage_bytes is not None:
            self.data_usage_bytes = data_usage_bytes
        if data_usage_percent is not None:
            self.data_usage_percent = data_usage_percent
        if binlog_usage_bytes is not None:
            self.binlog_usage_bytes = binlog_usage_bytes
        if binlog_usage_percent is not None:
            self.binlog_usage_percent = binlog_usage_percent
        if relay_log_usage_bytes is not None:
            self.relay_log_usage_bytes = relay_log_usage_bytes
        if relay_log_usage_percent is not None:
            self.relay_log_usage_percent = relay_log_usage_percent
        if audit_log_usage_bytes is not None:
            self.audit_log_usage_bytes = audit_log_usage_bytes
        if audit_log_usage_percent is not None:
            self.audit_log_usage_percent = audit_log_usage_percent
        if slow_log_usage_bytes is not None:
            self.slow_log_usage_bytes = slow_log_usage_bytes
        if slow_log_usage_percent is not None:
            self.slow_log_usage_percent = slow_log_usage_percent
        if temp_usage_bytes is not None:
            self.temp_usage_bytes = temp_usage_bytes
        if temp_usage_percent is not None:
            self.temp_usage_percent = temp_usage_percent
        if undo_log_usage_bytes is not None:
            self.undo_log_usage_bytes = undo_log_usage_bytes
        if undo_log_usage_percent is not None:
            self.undo_log_usage_percent = undo_log_usage_percent
        if other_usage_bytes is not None:
            self.other_usage_bytes = other_usage_bytes
        if other_usage_percent is not None:
            self.other_usage_percent = other_usage_percent
        if too_many_files is not None:
            self.too_many_files = too_many_files
        if page_usage_bytes is not None:
            self.page_usage_bytes = page_usage_bytes
        if total_space is not None:
            self.total_space = total_space
        if total_usage is not None:
            self.total_usage = total_usage
        if avail_size is not None:
            self.avail_size = avail_size
        if data is not None:
            self.data = data
        if log is not None:
            self.log = log
        if runtime is not None:
            self.runtime = runtime
        if slow_log is not None:
            self.slow_log = slow_log
        if audit_log is not None:
            self.audit_log = audit_log
        if tempdb is not None:
            self.tempdb = tempdb
        if msdb is not None:
            self.msdb = msdb
        if used_size_bytes is not None:
            self.used_size_bytes = used_size_bytes
        if total_size_bytes is not None:
            self.total_size_bytes = total_size_bytes
        if avg_daily_growth_bytes is not None:
            self.avg_daily_growth_bytes = avg_daily_growth_bytes
        if estimated_available_days is not None:
            self.estimated_available_days = estimated_available_days
        if data_size_bytes is not None:
            self.data_size_bytes = data_size_bytes
        if oplog_size_bytes is not None:
            self.oplog_size_bytes = oplog_size_bytes
        if other_size_bytes is not None:
            self.other_size_bytes = other_size_bytes
        if wal_size is not None:
            self.wal_size = wal_size
        if data_size is not None:
            self.data_size = data_size
        if pgaudit_log_size is not None:
            self.pgaudit_log_size = pgaudit_log_size
        if pgsql_tmp_size is not None:
            self.pgsql_tmp_size = pgsql_tmp_size

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowLatestSpaceResponse.

        更新时间

        :return: The update_time of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowLatestSpaceResponse.

        更新时间

        :param update_time: The update_time of this ShowLatestSpaceResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def buy_storage_bytes(self):
        r"""Gets the buy_storage_bytes of this ShowLatestSpaceResponse.

        MySQL购买空间

        :return: The buy_storage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._buy_storage_bytes

    @buy_storage_bytes.setter
    def buy_storage_bytes(self, buy_storage_bytes):
        r"""Sets the buy_storage_bytes of this ShowLatestSpaceResponse.

        MySQL购买空间

        :param buy_storage_bytes: The buy_storage_bytes of this ShowLatestSpaceResponse.
        :type buy_storage_bytes: int
        """
        self._buy_storage_bytes = buy_storage_bytes

    @property
    def used_storage_bytes(self):
        r"""Gets the used_storage_bytes of this ShowLatestSpaceResponse.

        MySQL已使用空间

        :return: The used_storage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._used_storage_bytes

    @used_storage_bytes.setter
    def used_storage_bytes(self, used_storage_bytes):
        r"""Sets the used_storage_bytes of this ShowLatestSpaceResponse.

        MySQL已使用空间

        :param used_storage_bytes: The used_storage_bytes of this ShowLatestSpaceResponse.
        :type used_storage_bytes: int
        """
        self._used_storage_bytes = used_storage_bytes

    @property
    def last_storage_bytes(self):
        r"""Gets the last_storage_bytes of this ShowLatestSpaceResponse.

        MySQL剩余空间

        :return: The last_storage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._last_storage_bytes

    @last_storage_bytes.setter
    def last_storage_bytes(self, last_storage_bytes):
        r"""Sets the last_storage_bytes of this ShowLatestSpaceResponse.

        MySQL剩余空间

        :param last_storage_bytes: The last_storage_bytes of this ShowLatestSpaceResponse.
        :type last_storage_bytes: int
        """
        self._last_storage_bytes = last_storage_bytes

    @property
    def buy_storage_percent(self):
        r"""Gets the buy_storage_percent of this ShowLatestSpaceResponse.

        MySQL使用空间占比

        :return: The buy_storage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._buy_storage_percent

    @buy_storage_percent.setter
    def buy_storage_percent(self, buy_storage_percent):
        r"""Sets the buy_storage_percent of this ShowLatestSpaceResponse.

        MySQL使用空间占比

        :param buy_storage_percent: The buy_storage_percent of this ShowLatestSpaceResponse.
        :type buy_storage_percent: float
        """
        self._buy_storage_percent = buy_storage_percent

    @property
    def data_usage_bytes(self):
        r"""Gets the data_usage_bytes of this ShowLatestSpaceResponse.

        数据空间

        :return: The data_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._data_usage_bytes

    @data_usage_bytes.setter
    def data_usage_bytes(self, data_usage_bytes):
        r"""Sets the data_usage_bytes of this ShowLatestSpaceResponse.

        数据空间

        :param data_usage_bytes: The data_usage_bytes of this ShowLatestSpaceResponse.
        :type data_usage_bytes: int
        """
        self._data_usage_bytes = data_usage_bytes

    @property
    def data_usage_percent(self):
        r"""Gets the data_usage_percent of this ShowLatestSpaceResponse.

        数据空间占比

        :return: The data_usage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._data_usage_percent

    @data_usage_percent.setter
    def data_usage_percent(self, data_usage_percent):
        r"""Sets the data_usage_percent of this ShowLatestSpaceResponse.

        数据空间占比

        :param data_usage_percent: The data_usage_percent of this ShowLatestSpaceResponse.
        :type data_usage_percent: float
        """
        self._data_usage_percent = data_usage_percent

    @property
    def binlog_usage_bytes(self):
        r"""Gets the binlog_usage_bytes of this ShowLatestSpaceResponse.

        binlog空间

        :return: The binlog_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._binlog_usage_bytes

    @binlog_usage_bytes.setter
    def binlog_usage_bytes(self, binlog_usage_bytes):
        r"""Sets the binlog_usage_bytes of this ShowLatestSpaceResponse.

        binlog空间

        :param binlog_usage_bytes: The binlog_usage_bytes of this ShowLatestSpaceResponse.
        :type binlog_usage_bytes: int
        """
        self._binlog_usage_bytes = binlog_usage_bytes

    @property
    def binlog_usage_percent(self):
        r"""Gets the binlog_usage_percent of this ShowLatestSpaceResponse.

        binlog空间占比

        :return: The binlog_usage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._binlog_usage_percent

    @binlog_usage_percent.setter
    def binlog_usage_percent(self, binlog_usage_percent):
        r"""Sets the binlog_usage_percent of this ShowLatestSpaceResponse.

        binlog空间占比

        :param binlog_usage_percent: The binlog_usage_percent of this ShowLatestSpaceResponse.
        :type binlog_usage_percent: float
        """
        self._binlog_usage_percent = binlog_usage_percent

    @property
    def relay_log_usage_bytes(self):
        r"""Gets the relay_log_usage_bytes of this ShowLatestSpaceResponse.

        relayLog空间

        :return: The relay_log_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._relay_log_usage_bytes

    @relay_log_usage_bytes.setter
    def relay_log_usage_bytes(self, relay_log_usage_bytes):
        r"""Sets the relay_log_usage_bytes of this ShowLatestSpaceResponse.

        relayLog空间

        :param relay_log_usage_bytes: The relay_log_usage_bytes of this ShowLatestSpaceResponse.
        :type relay_log_usage_bytes: int
        """
        self._relay_log_usage_bytes = relay_log_usage_bytes

    @property
    def relay_log_usage_percent(self):
        r"""Gets the relay_log_usage_percent of this ShowLatestSpaceResponse.

        relayLog空间占比

        :return: The relay_log_usage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._relay_log_usage_percent

    @relay_log_usage_percent.setter
    def relay_log_usage_percent(self, relay_log_usage_percent):
        r"""Sets the relay_log_usage_percent of this ShowLatestSpaceResponse.

        relayLog空间占比

        :param relay_log_usage_percent: The relay_log_usage_percent of this ShowLatestSpaceResponse.
        :type relay_log_usage_percent: float
        """
        self._relay_log_usage_percent = relay_log_usage_percent

    @property
    def audit_log_usage_bytes(self):
        r"""Gets the audit_log_usage_bytes of this ShowLatestSpaceResponse.

        auditLog空间

        :return: The audit_log_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._audit_log_usage_bytes

    @audit_log_usage_bytes.setter
    def audit_log_usage_bytes(self, audit_log_usage_bytes):
        r"""Sets the audit_log_usage_bytes of this ShowLatestSpaceResponse.

        auditLog空间

        :param audit_log_usage_bytes: The audit_log_usage_bytes of this ShowLatestSpaceResponse.
        :type audit_log_usage_bytes: int
        """
        self._audit_log_usage_bytes = audit_log_usage_bytes

    @property
    def audit_log_usage_percent(self):
        r"""Gets the audit_log_usage_percent of this ShowLatestSpaceResponse.

        auditLog空间占比

        :return: The audit_log_usage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._audit_log_usage_percent

    @audit_log_usage_percent.setter
    def audit_log_usage_percent(self, audit_log_usage_percent):
        r"""Sets the audit_log_usage_percent of this ShowLatestSpaceResponse.

        auditLog空间占比

        :param audit_log_usage_percent: The audit_log_usage_percent of this ShowLatestSpaceResponse.
        :type audit_log_usage_percent: float
        """
        self._audit_log_usage_percent = audit_log_usage_percent

    @property
    def slow_log_usage_bytes(self):
        r"""Gets the slow_log_usage_bytes of this ShowLatestSpaceResponse.

        slowLog空间

        :return: The slow_log_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._slow_log_usage_bytes

    @slow_log_usage_bytes.setter
    def slow_log_usage_bytes(self, slow_log_usage_bytes):
        r"""Sets the slow_log_usage_bytes of this ShowLatestSpaceResponse.

        slowLog空间

        :param slow_log_usage_bytes: The slow_log_usage_bytes of this ShowLatestSpaceResponse.
        :type slow_log_usage_bytes: int
        """
        self._slow_log_usage_bytes = slow_log_usage_bytes

    @property
    def slow_log_usage_percent(self):
        r"""Gets the slow_log_usage_percent of this ShowLatestSpaceResponse.

        slowLog空间占比

        :return: The slow_log_usage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._slow_log_usage_percent

    @slow_log_usage_percent.setter
    def slow_log_usage_percent(self, slow_log_usage_percent):
        r"""Sets the slow_log_usage_percent of this ShowLatestSpaceResponse.

        slowLog空间占比

        :param slow_log_usage_percent: The slow_log_usage_percent of this ShowLatestSpaceResponse.
        :type slow_log_usage_percent: float
        """
        self._slow_log_usage_percent = slow_log_usage_percent

    @property
    def temp_usage_bytes(self):
        r"""Gets the temp_usage_bytes of this ShowLatestSpaceResponse.

        临时空间

        :return: The temp_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._temp_usage_bytes

    @temp_usage_bytes.setter
    def temp_usage_bytes(self, temp_usage_bytes):
        r"""Sets the temp_usage_bytes of this ShowLatestSpaceResponse.

        临时空间

        :param temp_usage_bytes: The temp_usage_bytes of this ShowLatestSpaceResponse.
        :type temp_usage_bytes: int
        """
        self._temp_usage_bytes = temp_usage_bytes

    @property
    def temp_usage_percent(self):
        r"""Gets the temp_usage_percent of this ShowLatestSpaceResponse.

        临时空间占比

        :return: The temp_usage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._temp_usage_percent

    @temp_usage_percent.setter
    def temp_usage_percent(self, temp_usage_percent):
        r"""Sets the temp_usage_percent of this ShowLatestSpaceResponse.

        临时空间占比

        :param temp_usage_percent: The temp_usage_percent of this ShowLatestSpaceResponse.
        :type temp_usage_percent: float
        """
        self._temp_usage_percent = temp_usage_percent

    @property
    def undo_log_usage_bytes(self):
        r"""Gets the undo_log_usage_bytes of this ShowLatestSpaceResponse.

        undoLog空间

        :return: The undo_log_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._undo_log_usage_bytes

    @undo_log_usage_bytes.setter
    def undo_log_usage_bytes(self, undo_log_usage_bytes):
        r"""Sets the undo_log_usage_bytes of this ShowLatestSpaceResponse.

        undoLog空间

        :param undo_log_usage_bytes: The undo_log_usage_bytes of this ShowLatestSpaceResponse.
        :type undo_log_usage_bytes: int
        """
        self._undo_log_usage_bytes = undo_log_usage_bytes

    @property
    def undo_log_usage_percent(self):
        r"""Gets the undo_log_usage_percent of this ShowLatestSpaceResponse.

        undoLog空间占比

        :return: The undo_log_usage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._undo_log_usage_percent

    @undo_log_usage_percent.setter
    def undo_log_usage_percent(self, undo_log_usage_percent):
        r"""Sets the undo_log_usage_percent of this ShowLatestSpaceResponse.

        undoLog空间占比

        :param undo_log_usage_percent: The undo_log_usage_percent of this ShowLatestSpaceResponse.
        :type undo_log_usage_percent: float
        """
        self._undo_log_usage_percent = undo_log_usage_percent

    @property
    def other_usage_bytes(self):
        r"""Gets the other_usage_bytes of this ShowLatestSpaceResponse.

        其他空间

        :return: The other_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._other_usage_bytes

    @other_usage_bytes.setter
    def other_usage_bytes(self, other_usage_bytes):
        r"""Sets the other_usage_bytes of this ShowLatestSpaceResponse.

        其他空间

        :param other_usage_bytes: The other_usage_bytes of this ShowLatestSpaceResponse.
        :type other_usage_bytes: int
        """
        self._other_usage_bytes = other_usage_bytes

    @property
    def other_usage_percent(self):
        r"""Gets the other_usage_percent of this ShowLatestSpaceResponse.

        其他空间占比

        :return: The other_usage_percent of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._other_usage_percent

    @other_usage_percent.setter
    def other_usage_percent(self, other_usage_percent):
        r"""Sets the other_usage_percent of this ShowLatestSpaceResponse.

        其他空间占比

        :param other_usage_percent: The other_usage_percent of this ShowLatestSpaceResponse.
        :type other_usage_percent: float
        """
        self._other_usage_percent = other_usage_percent

    @property
    def too_many_files(self):
        r"""Gets the too_many_files of this ShowLatestSpaceResponse.

        是否文件过多

        :return: The too_many_files of this ShowLatestSpaceResponse.
        :rtype: bool
        """
        return self._too_many_files

    @too_many_files.setter
    def too_many_files(self, too_many_files):
        r"""Sets the too_many_files of this ShowLatestSpaceResponse.

        是否文件过多

        :param too_many_files: The too_many_files of this ShowLatestSpaceResponse.
        :type too_many_files: bool
        """
        self._too_many_files = too_many_files

    @property
    def page_usage_bytes(self):
        r"""Gets the page_usage_bytes of this ShowLatestSpaceResponse.

        TaurusDB数据空间

        :return: The page_usage_bytes of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._page_usage_bytes

    @page_usage_bytes.setter
    def page_usage_bytes(self, page_usage_bytes):
        r"""Sets the page_usage_bytes of this ShowLatestSpaceResponse.

        TaurusDB数据空间

        :param page_usage_bytes: The page_usage_bytes of this ShowLatestSpaceResponse.
        :type page_usage_bytes: float
        """
        self._page_usage_bytes = page_usage_bytes

    @property
    def total_space(self):
        r"""Gets the total_space of this ShowLatestSpaceResponse.

        SQLServer总空间

        :return: The total_space of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._total_space

    @total_space.setter
    def total_space(self, total_space):
        r"""Sets the total_space of this ShowLatestSpaceResponse.

        SQLServer总空间

        :param total_space: The total_space of this ShowLatestSpaceResponse.
        :type total_space: int
        """
        self._total_space = total_space

    @property
    def total_usage(self):
        r"""Gets the total_usage of this ShowLatestSpaceResponse.

        SQLServer已使用空间

        :return: The total_usage of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        r"""Sets the total_usage of this ShowLatestSpaceResponse.

        SQLServer已使用空间

        :param total_usage: The total_usage of this ShowLatestSpaceResponse.
        :type total_usage: int
        """
        self._total_usage = total_usage

    @property
    def avail_size(self):
        r"""Gets the avail_size of this ShowLatestSpaceResponse.

        SQLServer可用空间

        :return: The avail_size of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._avail_size

    @avail_size.setter
    def avail_size(self, avail_size):
        r"""Sets the avail_size of this ShowLatestSpaceResponse.

        SQLServer可用空间

        :param avail_size: The avail_size of this ShowLatestSpaceResponse.
        :type avail_size: int
        """
        self._avail_size = avail_size

    @property
    def data(self):
        r"""Gets the data of this ShowLatestSpaceResponse.

        SQLServer数据空间

        :return: The data of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ShowLatestSpaceResponse.

        SQLServer数据空间

        :param data: The data of this ShowLatestSpaceResponse.
        :type data: float
        """
        self._data = data

    @property
    def log(self):
        r"""Gets the log of this ShowLatestSpaceResponse.

        SQLServer log空间

        :return: The log of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._log

    @log.setter
    def log(self, log):
        r"""Sets the log of this ShowLatestSpaceResponse.

        SQLServer log空间

        :param log: The log of this ShowLatestSpaceResponse.
        :type log: float
        """
        self._log = log

    @property
    def runtime(self):
        r"""Gets the runtime of this ShowLatestSpaceResponse.

        SQLServer runtime

        :return: The runtime of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ShowLatestSpaceResponse.

        SQLServer runtime

        :param runtime: The runtime of this ShowLatestSpaceResponse.
        :type runtime: float
        """
        self._runtime = runtime

    @property
    def slow_log(self):
        r"""Gets the slow_log of this ShowLatestSpaceResponse.

        SQLServer slow_log空间

        :return: The slow_log of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._slow_log

    @slow_log.setter
    def slow_log(self, slow_log):
        r"""Sets the slow_log of this ShowLatestSpaceResponse.

        SQLServer slow_log空间

        :param slow_log: The slow_log of this ShowLatestSpaceResponse.
        :type slow_log: float
        """
        self._slow_log = slow_log

    @property
    def audit_log(self):
        r"""Gets the audit_log of this ShowLatestSpaceResponse.

        SQLServer audit_log空间

        :return: The audit_log of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._audit_log

    @audit_log.setter
    def audit_log(self, audit_log):
        r"""Sets the audit_log of this ShowLatestSpaceResponse.

        SQLServer audit_log空间

        :param audit_log: The audit_log of this ShowLatestSpaceResponse.
        :type audit_log: float
        """
        self._audit_log = audit_log

    @property
    def tempdb(self):
        r"""Gets the tempdb of this ShowLatestSpaceResponse.

        SQLServer tempdb空间

        :return: The tempdb of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._tempdb

    @tempdb.setter
    def tempdb(self, tempdb):
        r"""Sets the tempdb of this ShowLatestSpaceResponse.

        SQLServer tempdb空间

        :param tempdb: The tempdb of this ShowLatestSpaceResponse.
        :type tempdb: float
        """
        self._tempdb = tempdb

    @property
    def msdb(self):
        r"""Gets the msdb of this ShowLatestSpaceResponse.

        SQLServer msdb空间

        :return: The msdb of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._msdb

    @msdb.setter
    def msdb(self, msdb):
        r"""Sets the msdb of this ShowLatestSpaceResponse.

        SQLServer msdb空间

        :param msdb: The msdb of this ShowLatestSpaceResponse.
        :type msdb: float
        """
        self._msdb = msdb

    @property
    def used_size_bytes(self):
        r"""Gets the used_size_bytes of this ShowLatestSpaceResponse.

        DDS磁盘使用量

        :return: The used_size_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._used_size_bytes

    @used_size_bytes.setter
    def used_size_bytes(self, used_size_bytes):
        r"""Sets the used_size_bytes of this ShowLatestSpaceResponse.

        DDS磁盘使用量

        :param used_size_bytes: The used_size_bytes of this ShowLatestSpaceResponse.
        :type used_size_bytes: int
        """
        self._used_size_bytes = used_size_bytes

    @property
    def total_size_bytes(self):
        r"""Gets the total_size_bytes of this ShowLatestSpaceResponse.

        DDS磁盘总量

        :return: The total_size_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._total_size_bytes

    @total_size_bytes.setter
    def total_size_bytes(self, total_size_bytes):
        r"""Sets the total_size_bytes of this ShowLatestSpaceResponse.

        DDS磁盘总量

        :param total_size_bytes: The total_size_bytes of this ShowLatestSpaceResponse.
        :type total_size_bytes: int
        """
        self._total_size_bytes = total_size_bytes

    @property
    def avg_daily_growth_bytes(self):
        r"""Gets the avg_daily_growth_bytes of this ShowLatestSpaceResponse.

        DDS近一周日均增长

        :return: The avg_daily_growth_bytes of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._avg_daily_growth_bytes

    @avg_daily_growth_bytes.setter
    def avg_daily_growth_bytes(self, avg_daily_growth_bytes):
        r"""Sets the avg_daily_growth_bytes of this ShowLatestSpaceResponse.

        DDS近一周日均增长

        :param avg_daily_growth_bytes: The avg_daily_growth_bytes of this ShowLatestSpaceResponse.
        :type avg_daily_growth_bytes: float
        """
        self._avg_daily_growth_bytes = avg_daily_growth_bytes

    @property
    def estimated_available_days(self):
        r"""Gets the estimated_available_days of this ShowLatestSpaceResponse.

        DDS预计可用天数

        :return: The estimated_available_days of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._estimated_available_days

    @estimated_available_days.setter
    def estimated_available_days(self, estimated_available_days):
        r"""Sets the estimated_available_days of this ShowLatestSpaceResponse.

        DDS预计可用天数

        :param estimated_available_days: The estimated_available_days of this ShowLatestSpaceResponse.
        :type estimated_available_days: int
        """
        self._estimated_available_days = estimated_available_days

    @property
    def data_size_bytes(self):
        r"""Gets the data_size_bytes of this ShowLatestSpaceResponse.

        DDS数据空间

        :return: The data_size_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._data_size_bytes

    @data_size_bytes.setter
    def data_size_bytes(self, data_size_bytes):
        r"""Sets the data_size_bytes of this ShowLatestSpaceResponse.

        DDS数据空间

        :param data_size_bytes: The data_size_bytes of this ShowLatestSpaceResponse.
        :type data_size_bytes: int
        """
        self._data_size_bytes = data_size_bytes

    @property
    def oplog_size_bytes(self):
        r"""Gets the oplog_size_bytes of this ShowLatestSpaceResponse.

        DDS oplog空间

        :return: The oplog_size_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._oplog_size_bytes

    @oplog_size_bytes.setter
    def oplog_size_bytes(self, oplog_size_bytes):
        r"""Sets the oplog_size_bytes of this ShowLatestSpaceResponse.

        DDS oplog空间

        :param oplog_size_bytes: The oplog_size_bytes of this ShowLatestSpaceResponse.
        :type oplog_size_bytes: int
        """
        self._oplog_size_bytes = oplog_size_bytes

    @property
    def other_size_bytes(self):
        r"""Gets the other_size_bytes of this ShowLatestSpaceResponse.

        DDS其他空间

        :return: The other_size_bytes of this ShowLatestSpaceResponse.
        :rtype: int
        """
        return self._other_size_bytes

    @other_size_bytes.setter
    def other_size_bytes(self, other_size_bytes):
        r"""Sets the other_size_bytes of this ShowLatestSpaceResponse.

        DDS其他空间

        :param other_size_bytes: The other_size_bytes of this ShowLatestSpaceResponse.
        :type other_size_bytes: int
        """
        self._other_size_bytes = other_size_bytes

    @property
    def wal_size(self):
        r"""Gets the wal_size of this ShowLatestSpaceResponse.

        PostgreSQL wallog空间

        :return: The wal_size of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._wal_size

    @wal_size.setter
    def wal_size(self, wal_size):
        r"""Sets the wal_size of this ShowLatestSpaceResponse.

        PostgreSQL wallog空间

        :param wal_size: The wal_size of this ShowLatestSpaceResponse.
        :type wal_size: float
        """
        self._wal_size = wal_size

    @property
    def data_size(self):
        r"""Gets the data_size of this ShowLatestSpaceResponse.

        PostgreSQL数据空间

        :return: The data_size of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        r"""Sets the data_size of this ShowLatestSpaceResponse.

        PostgreSQL数据空间

        :param data_size: The data_size of this ShowLatestSpaceResponse.
        :type data_size: float
        """
        self._data_size = data_size

    @property
    def pgaudit_log_size(self):
        r"""Gets the pgaudit_log_size of this ShowLatestSpaceResponse.

        PostgreSQL auditlog空间

        :return: The pgaudit_log_size of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._pgaudit_log_size

    @pgaudit_log_size.setter
    def pgaudit_log_size(self, pgaudit_log_size):
        r"""Sets the pgaudit_log_size of this ShowLatestSpaceResponse.

        PostgreSQL auditlog空间

        :param pgaudit_log_size: The pgaudit_log_size of this ShowLatestSpaceResponse.
        :type pgaudit_log_size: float
        """
        self._pgaudit_log_size = pgaudit_log_size

    @property
    def pgsql_tmp_size(self):
        r"""Gets the pgsql_tmp_size of this ShowLatestSpaceResponse.

        PostgreSQL临时空间

        :return: The pgsql_tmp_size of this ShowLatestSpaceResponse.
        :rtype: float
        """
        return self._pgsql_tmp_size

    @pgsql_tmp_size.setter
    def pgsql_tmp_size(self, pgsql_tmp_size):
        r"""Sets the pgsql_tmp_size of this ShowLatestSpaceResponse.

        PostgreSQL临时空间

        :param pgsql_tmp_size: The pgsql_tmp_size of this ShowLatestSpaceResponse.
        :type pgsql_tmp_size: float
        """
        self._pgsql_tmp_size = pgsql_tmp_size

    def to_dict(self):
        import warnings
        warnings.warn("ShowLatestSpaceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLatestSpaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
