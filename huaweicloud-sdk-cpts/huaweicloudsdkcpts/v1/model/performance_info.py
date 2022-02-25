# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PerformanceInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'average_resp_time': 'float',
        'avg_network_traffic': 'float',
        'avg_rec_bytes': 'float',
        'avg_sent_bytes': 'float',
        'avg_tran_resp_time': 'float',
        'case_uri': 'str',
        'create_time': 'str',
        'current_thread_num': 'float',
        'detail_id': 'str',
        'end_time': 'str',
        'error_count': 'float',
        'error_events_count': 'float',
        'failed_assert': 'float',
        'failed_others': 'float',
        'failed_parsed': 'float',
        'failed_refused': 'float',
        'failed_timeout': 'float',
        'id': 'str',
        'is_aw': 'bool',
        'max': 'float',
        'max_network_traffic': 'float',
        'max_rec_bytes': 'float',
        'max_resp_time': 'float',
        'max_sent_bytes': 'float',
        'max_tran_resp_time': 'float',
        'min': 'float',
        'min_network_traffic': 'float',
        'name': 'str',
        'requests': 'float',
        'result': 'float',
        'start_time': 'str',
        'status': 'float',
        'success_count': 'float',
        'success_rate': 'float',
        'sum1xx': 'float',
        'sum2xx': 'float',
        'sum3xx': 'float',
        'sum4xx': 'float',
        'sum5xx': 'float',
        'task_id': 'str',
        'task_project_id': 'str',
        'task_status': 'float',
        'test_case_uri': 'str',
        'tp50': 'float',
        'tp75': 'float',
        'tp90': 'float',
        'tp95': 'float',
        'tp99': 'float',
        'tp999': 'float',
        'tp9999': 'float',
        'tps': 'float',
        'tran_tps': 'float',
        'transaction_id': 'str',
        'transaction_success': 'float',
        'transactional_success_rate': 'float',
        'transactional_tps': 'float',
        'transactional_tps_success': 'float',
        'transactions': 'float',
        'update_time': 'str',
        'vum': 'float'
    }

    attribute_map = {
        'average_resp_time': 'averageRespTime',
        'avg_network_traffic': 'avgNetworkTraffic',
        'avg_rec_bytes': 'avgRecBytes',
        'avg_sent_bytes': 'avgSentBytes',
        'avg_tran_resp_time': 'avgTranRespTime',
        'case_uri': 'caseUri',
        'create_time': 'createTime',
        'current_thread_num': 'currentThreadNum',
        'detail_id': 'detailId',
        'end_time': 'endTime',
        'error_count': 'errorCount',
        'error_events_count': 'errorEventsCount',
        'failed_assert': 'failedAssert',
        'failed_others': 'failedOthers',
        'failed_parsed': 'failedParsed',
        'failed_refused': 'failedRefused',
        'failed_timeout': 'failedTimeout',
        'id': 'id',
        'is_aw': 'isAW',
        'max': 'max',
        'max_network_traffic': 'maxNetworkTraffic',
        'max_rec_bytes': 'maxRecBytes',
        'max_resp_time': 'maxRespTime',
        'max_sent_bytes': 'maxSentBytes',
        'max_tran_resp_time': 'maxTranRespTime',
        'min': 'min',
        'min_network_traffic': 'minNetworkTraffic',
        'name': 'name',
        'requests': 'requests',
        'result': 'result',
        'start_time': 'startTime',
        'status': 'status',
        'success_count': 'successCount',
        'success_rate': 'successRate',
        'sum1xx': 'sum1xx',
        'sum2xx': 'sum2xx',
        'sum3xx': 'sum3xx',
        'sum4xx': 'sum4xx',
        'sum5xx': 'sum5xx',
        'task_id': 'taskId',
        'task_project_id': 'taskProjectId',
        'task_status': 'taskStatus',
        'test_case_uri': 'testCaseUri',
        'tp50': 'tp50',
        'tp75': 'tp75',
        'tp90': 'tp90',
        'tp95': 'tp95',
        'tp99': 'tp99',
        'tp999': 'tp999',
        'tp9999': 'tp9999',
        'tps': 'tps',
        'tran_tps': 'tranTPS',
        'transaction_id': 'transactionId',
        'transaction_success': 'transactionSuccess',
        'transactional_success_rate': 'transactionalSuccessRate',
        'transactional_tps': 'transactionalTps',
        'transactional_tps_success': 'transactionalTpsSuccess',
        'transactions': 'transactions',
        'update_time': 'updateTime',
        'vum': 'vum'
    }

    def __init__(self, average_resp_time=None, avg_network_traffic=None, avg_rec_bytes=None, avg_sent_bytes=None, avg_tran_resp_time=None, case_uri=None, create_time=None, current_thread_num=None, detail_id=None, end_time=None, error_count=None, error_events_count=None, failed_assert=None, failed_others=None, failed_parsed=None, failed_refused=None, failed_timeout=None, id=None, is_aw=None, max=None, max_network_traffic=None, max_rec_bytes=None, max_resp_time=None, max_sent_bytes=None, max_tran_resp_time=None, min=None, min_network_traffic=None, name=None, requests=None, result=None, start_time=None, status=None, success_count=None, success_rate=None, sum1xx=None, sum2xx=None, sum3xx=None, sum4xx=None, sum5xx=None, task_id=None, task_project_id=None, task_status=None, test_case_uri=None, tp50=None, tp75=None, tp90=None, tp95=None, tp99=None, tp999=None, tp9999=None, tps=None, tran_tps=None, transaction_id=None, transaction_success=None, transactional_success_rate=None, transactional_tps=None, transactional_tps_success=None, transactions=None, update_time=None, vum=None):
        """PerformanceInfo - a model defined in huaweicloud sdk"""
        
        

        self._average_resp_time = None
        self._avg_network_traffic = None
        self._avg_rec_bytes = None
        self._avg_sent_bytes = None
        self._avg_tran_resp_time = None
        self._case_uri = None
        self._create_time = None
        self._current_thread_num = None
        self._detail_id = None
        self._end_time = None
        self._error_count = None
        self._error_events_count = None
        self._failed_assert = None
        self._failed_others = None
        self._failed_parsed = None
        self._failed_refused = None
        self._failed_timeout = None
        self._id = None
        self._is_aw = None
        self._max = None
        self._max_network_traffic = None
        self._max_rec_bytes = None
        self._max_resp_time = None
        self._max_sent_bytes = None
        self._max_tran_resp_time = None
        self._min = None
        self._min_network_traffic = None
        self._name = None
        self._requests = None
        self._result = None
        self._start_time = None
        self._status = None
        self._success_count = None
        self._success_rate = None
        self._sum1xx = None
        self._sum2xx = None
        self._sum3xx = None
        self._sum4xx = None
        self._sum5xx = None
        self._task_id = None
        self._task_project_id = None
        self._task_status = None
        self._test_case_uri = None
        self._tp50 = None
        self._tp75 = None
        self._tp90 = None
        self._tp95 = None
        self._tp99 = None
        self._tp999 = None
        self._tp9999 = None
        self._tps = None
        self._tran_tps = None
        self._transaction_id = None
        self._transaction_success = None
        self._transactional_success_rate = None
        self._transactional_tps = None
        self._transactional_tps_success = None
        self._transactions = None
        self._update_time = None
        self._vum = None
        self.discriminator = None

        if average_resp_time is not None:
            self.average_resp_time = average_resp_time
        if avg_network_traffic is not None:
            self.avg_network_traffic = avg_network_traffic
        if avg_rec_bytes is not None:
            self.avg_rec_bytes = avg_rec_bytes
        if avg_sent_bytes is not None:
            self.avg_sent_bytes = avg_sent_bytes
        if avg_tran_resp_time is not None:
            self.avg_tran_resp_time = avg_tran_resp_time
        if case_uri is not None:
            self.case_uri = case_uri
        if create_time is not None:
            self.create_time = create_time
        if current_thread_num is not None:
            self.current_thread_num = current_thread_num
        if detail_id is not None:
            self.detail_id = detail_id
        if end_time is not None:
            self.end_time = end_time
        if error_count is not None:
            self.error_count = error_count
        if error_events_count is not None:
            self.error_events_count = error_events_count
        if failed_assert is not None:
            self.failed_assert = failed_assert
        if failed_others is not None:
            self.failed_others = failed_others
        if failed_parsed is not None:
            self.failed_parsed = failed_parsed
        if failed_refused is not None:
            self.failed_refused = failed_refused
        if failed_timeout is not None:
            self.failed_timeout = failed_timeout
        if id is not None:
            self.id = id
        if is_aw is not None:
            self.is_aw = is_aw
        if max is not None:
            self.max = max
        if max_network_traffic is not None:
            self.max_network_traffic = max_network_traffic
        if max_rec_bytes is not None:
            self.max_rec_bytes = max_rec_bytes
        if max_resp_time is not None:
            self.max_resp_time = max_resp_time
        if max_sent_bytes is not None:
            self.max_sent_bytes = max_sent_bytes
        if max_tran_resp_time is not None:
            self.max_tran_resp_time = max_tran_resp_time
        if min is not None:
            self.min = min
        if min_network_traffic is not None:
            self.min_network_traffic = min_network_traffic
        if name is not None:
            self.name = name
        if requests is not None:
            self.requests = requests
        if result is not None:
            self.result = result
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if success_count is not None:
            self.success_count = success_count
        if success_rate is not None:
            self.success_rate = success_rate
        if sum1xx is not None:
            self.sum1xx = sum1xx
        if sum2xx is not None:
            self.sum2xx = sum2xx
        if sum3xx is not None:
            self.sum3xx = sum3xx
        if sum4xx is not None:
            self.sum4xx = sum4xx
        if sum5xx is not None:
            self.sum5xx = sum5xx
        if task_id is not None:
            self.task_id = task_id
        if task_project_id is not None:
            self.task_project_id = task_project_id
        if task_status is not None:
            self.task_status = task_status
        if test_case_uri is not None:
            self.test_case_uri = test_case_uri
        if tp50 is not None:
            self.tp50 = tp50
        if tp75 is not None:
            self.tp75 = tp75
        if tp90 is not None:
            self.tp90 = tp90
        if tp95 is not None:
            self.tp95 = tp95
        if tp99 is not None:
            self.tp99 = tp99
        if tp999 is not None:
            self.tp999 = tp999
        if tp9999 is not None:
            self.tp9999 = tp9999
        if tps is not None:
            self.tps = tps
        if tran_tps is not None:
            self.tran_tps = tran_tps
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_success is not None:
            self.transaction_success = transaction_success
        if transactional_success_rate is not None:
            self.transactional_success_rate = transactional_success_rate
        if transactional_tps is not None:
            self.transactional_tps = transactional_tps
        if transactional_tps_success is not None:
            self.transactional_tps_success = transactional_tps_success
        if transactions is not None:
            self.transactions = transactions
        if update_time is not None:
            self.update_time = update_time
        if vum is not None:
            self.vum = vum

    @property
    def average_resp_time(self):
        """Gets the average_resp_time of this PerformanceInfo.

        平均响应时间

        :return: The average_resp_time of this PerformanceInfo.
        :rtype: float
        """
        return self._average_resp_time

    @average_resp_time.setter
    def average_resp_time(self, average_resp_time):
        """Sets the average_resp_time of this PerformanceInfo.

        平均响应时间

        :param average_resp_time: The average_resp_time of this PerformanceInfo.
        :type: float
        """
        self._average_resp_time = average_resp_time

    @property
    def avg_network_traffic(self):
        """Gets the avg_network_traffic of this PerformanceInfo.

        平均带宽

        :return: The avg_network_traffic of this PerformanceInfo.
        :rtype: float
        """
        return self._avg_network_traffic

    @avg_network_traffic.setter
    def avg_network_traffic(self, avg_network_traffic):
        """Sets the avg_network_traffic of this PerformanceInfo.

        平均带宽

        :param avg_network_traffic: The avg_network_traffic of this PerformanceInfo.
        :type: float
        """
        self._avg_network_traffic = avg_network_traffic

    @property
    def avg_rec_bytes(self):
        """Gets the avg_rec_bytes of this PerformanceInfo.

        平均下行带宽

        :return: The avg_rec_bytes of this PerformanceInfo.
        :rtype: float
        """
        return self._avg_rec_bytes

    @avg_rec_bytes.setter
    def avg_rec_bytes(self, avg_rec_bytes):
        """Sets the avg_rec_bytes of this PerformanceInfo.

        平均下行带宽

        :param avg_rec_bytes: The avg_rec_bytes of this PerformanceInfo.
        :type: float
        """
        self._avg_rec_bytes = avg_rec_bytes

    @property
    def avg_sent_bytes(self):
        """Gets the avg_sent_bytes of this PerformanceInfo.

        平均上行带宽

        :return: The avg_sent_bytes of this PerformanceInfo.
        :rtype: float
        """
        return self._avg_sent_bytes

    @avg_sent_bytes.setter
    def avg_sent_bytes(self, avg_sent_bytes):
        """Sets the avg_sent_bytes of this PerformanceInfo.

        平均上行带宽

        :param avg_sent_bytes: The avg_sent_bytes of this PerformanceInfo.
        :type: float
        """
        self._avg_sent_bytes = avg_sent_bytes

    @property
    def avg_tran_resp_time(self):
        """Gets the avg_tran_resp_time of this PerformanceInfo.

        事务平均响应时间

        :return: The avg_tran_resp_time of this PerformanceInfo.
        :rtype: float
        """
        return self._avg_tran_resp_time

    @avg_tran_resp_time.setter
    def avg_tran_resp_time(self, avg_tran_resp_time):
        """Sets the avg_tran_resp_time of this PerformanceInfo.

        事务平均响应时间

        :param avg_tran_resp_time: The avg_tran_resp_time of this PerformanceInfo.
        :type: float
        """
        self._avg_tran_resp_time = avg_tran_resp_time

    @property
    def case_uri(self):
        """Gets the case_uri of this PerformanceInfo.

        用例Uri

        :return: The case_uri of this PerformanceInfo.
        :rtype: str
        """
        return self._case_uri

    @case_uri.setter
    def case_uri(self, case_uri):
        """Sets the case_uri of this PerformanceInfo.

        用例Uri

        :param case_uri: The case_uri of this PerformanceInfo.
        :type: str
        """
        self._case_uri = case_uri

    @property
    def create_time(self):
        """Gets the create_time of this PerformanceInfo.

        创建时间

        :return: The create_time of this PerformanceInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PerformanceInfo.

        创建时间

        :param create_time: The create_time of this PerformanceInfo.
        :type: str
        """
        self._create_time = create_time

    @property
    def current_thread_num(self):
        """Gets the current_thread_num of this PerformanceInfo.

        最大并发数

        :return: The current_thread_num of this PerformanceInfo.
        :rtype: float
        """
        return self._current_thread_num

    @current_thread_num.setter
    def current_thread_num(self, current_thread_num):
        """Sets the current_thread_num of this PerformanceInfo.

        最大并发数

        :param current_thread_num: The current_thread_num of this PerformanceInfo.
        :type: float
        """
        self._current_thread_num = current_thread_num

    @property
    def detail_id(self):
        """Gets the detail_id of this PerformanceInfo.

        详情id

        :return: The detail_id of this PerformanceInfo.
        :rtype: str
        """
        return self._detail_id

    @detail_id.setter
    def detail_id(self, detail_id):
        """Sets the detail_id of this PerformanceInfo.

        详情id

        :param detail_id: The detail_id of this PerformanceInfo.
        :type: str
        """
        self._detail_id = detail_id

    @property
    def end_time(self):
        """Gets the end_time of this PerformanceInfo.

        结束时间

        :return: The end_time of this PerformanceInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this PerformanceInfo.

        结束时间

        :param end_time: The end_time of this PerformanceInfo.
        :type: str
        """
        self._end_time = end_time

    @property
    def error_count(self):
        """Gets the error_count of this PerformanceInfo.

        失败请求数

        :return: The error_count of this PerformanceInfo.
        :rtype: float
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this PerformanceInfo.

        失败请求数

        :param error_count: The error_count of this PerformanceInfo.
        :type: float
        """
        self._error_count = error_count

    @property
    def error_events_count(self):
        """Gets the error_events_count of this PerformanceInfo.

        ERROR级别的事件个数

        :return: The error_events_count of this PerformanceInfo.
        :rtype: float
        """
        return self._error_events_count

    @error_events_count.setter
    def error_events_count(self, error_events_count):
        """Sets the error_events_count of this PerformanceInfo.

        ERROR级别的事件个数

        :param error_events_count: The error_events_count of this PerformanceInfo.
        :type: float
        """
        self._error_events_count = error_events_count

    @property
    def failed_assert(self):
        """Gets the failed_assert of this PerformanceInfo.

        断言失败

        :return: The failed_assert of this PerformanceInfo.
        :rtype: float
        """
        return self._failed_assert

    @failed_assert.setter
    def failed_assert(self, failed_assert):
        """Sets the failed_assert of this PerformanceInfo.

        断言失败

        :param failed_assert: The failed_assert of this PerformanceInfo.
        :type: float
        """
        self._failed_assert = failed_assert

    @property
    def failed_others(self):
        """Gets the failed_others of this PerformanceInfo.

        其他失败

        :return: The failed_others of this PerformanceInfo.
        :rtype: float
        """
        return self._failed_others

    @failed_others.setter
    def failed_others(self, failed_others):
        """Sets the failed_others of this PerformanceInfo.

        其他失败

        :param failed_others: The failed_others of this PerformanceInfo.
        :type: float
        """
        self._failed_others = failed_others

    @property
    def failed_parsed(self):
        """Gets the failed_parsed of this PerformanceInfo.

        解析失败

        :return: The failed_parsed of this PerformanceInfo.
        :rtype: float
        """
        return self._failed_parsed

    @failed_parsed.setter
    def failed_parsed(self, failed_parsed):
        """Sets the failed_parsed of this PerformanceInfo.

        解析失败

        :param failed_parsed: The failed_parsed of this PerformanceInfo.
        :type: float
        """
        self._failed_parsed = failed_parsed

    @property
    def failed_refused(self):
        """Gets the failed_refused of this PerformanceInfo.

        连接被拒

        :return: The failed_refused of this PerformanceInfo.
        :rtype: float
        """
        return self._failed_refused

    @failed_refused.setter
    def failed_refused(self, failed_refused):
        """Sets the failed_refused of this PerformanceInfo.

        连接被拒

        :param failed_refused: The failed_refused of this PerformanceInfo.
        :type: float
        """
        self._failed_refused = failed_refused

    @property
    def failed_timeout(self):
        """Gets the failed_timeout of this PerformanceInfo.

        超时失败

        :return: The failed_timeout of this PerformanceInfo.
        :rtype: float
        """
        return self._failed_timeout

    @failed_timeout.setter
    def failed_timeout(self, failed_timeout):
        """Sets the failed_timeout of this PerformanceInfo.

        超时失败

        :param failed_timeout: The failed_timeout of this PerformanceInfo.
        :type: float
        """
        self._failed_timeout = failed_timeout

    @property
    def id(self):
        """Gets the id of this PerformanceInfo.

        id

        :return: The id of this PerformanceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PerformanceInfo.

        id

        :param id: The id of this PerformanceInfo.
        :type: str
        """
        self._id = id

    @property
    def is_aw(self):
        """Gets the is_aw of this PerformanceInfo.

        是否aw

        :return: The is_aw of this PerformanceInfo.
        :rtype: bool
        """
        return self._is_aw

    @is_aw.setter
    def is_aw(self, is_aw):
        """Sets the is_aw of this PerformanceInfo.

        是否aw

        :param is_aw: The is_aw of this PerformanceInfo.
        :type: bool
        """
        self._is_aw = is_aw

    @property
    def max(self):
        """Gets the max of this PerformanceInfo.

        最大响应时间

        :return: The max of this PerformanceInfo.
        :rtype: float
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this PerformanceInfo.

        最大响应时间

        :param max: The max of this PerformanceInfo.
        :type: float
        """
        self._max = max

    @property
    def max_network_traffic(self):
        """Gets the max_network_traffic of this PerformanceInfo.

        最大带宽

        :return: The max_network_traffic of this PerformanceInfo.
        :rtype: float
        """
        return self._max_network_traffic

    @max_network_traffic.setter
    def max_network_traffic(self, max_network_traffic):
        """Sets the max_network_traffic of this PerformanceInfo.

        最大带宽

        :param max_network_traffic: The max_network_traffic of this PerformanceInfo.
        :type: float
        """
        self._max_network_traffic = max_network_traffic

    @property
    def max_rec_bytes(self):
        """Gets the max_rec_bytes of this PerformanceInfo.

        最大接收字节数

        :return: The max_rec_bytes of this PerformanceInfo.
        :rtype: float
        """
        return self._max_rec_bytes

    @max_rec_bytes.setter
    def max_rec_bytes(self, max_rec_bytes):
        """Sets the max_rec_bytes of this PerformanceInfo.

        最大接收字节数

        :param max_rec_bytes: The max_rec_bytes of this PerformanceInfo.
        :type: float
        """
        self._max_rec_bytes = max_rec_bytes

    @property
    def max_resp_time(self):
        """Gets the max_resp_time of this PerformanceInfo.

        探底结果：响应时间

        :return: The max_resp_time of this PerformanceInfo.
        :rtype: float
        """
        return self._max_resp_time

    @max_resp_time.setter
    def max_resp_time(self, max_resp_time):
        """Sets the max_resp_time of this PerformanceInfo.

        探底结果：响应时间

        :param max_resp_time: The max_resp_time of this PerformanceInfo.
        :type: float
        """
        self._max_resp_time = max_resp_time

    @property
    def max_sent_bytes(self):
        """Gets the max_sent_bytes of this PerformanceInfo.

        最大发送带宽

        :return: The max_sent_bytes of this PerformanceInfo.
        :rtype: float
        """
        return self._max_sent_bytes

    @max_sent_bytes.setter
    def max_sent_bytes(self, max_sent_bytes):
        """Sets the max_sent_bytes of this PerformanceInfo.

        最大发送带宽

        :param max_sent_bytes: The max_sent_bytes of this PerformanceInfo.
        :type: float
        """
        self._max_sent_bytes = max_sent_bytes

    @property
    def max_tran_resp_time(self):
        """Gets the max_tran_resp_time of this PerformanceInfo.

        事务最大响应时间

        :return: The max_tran_resp_time of this PerformanceInfo.
        :rtype: float
        """
        return self._max_tran_resp_time

    @max_tran_resp_time.setter
    def max_tran_resp_time(self, max_tran_resp_time):
        """Sets the max_tran_resp_time of this PerformanceInfo.

        事务最大响应时间

        :param max_tran_resp_time: The max_tran_resp_time of this PerformanceInfo.
        :type: float
        """
        self._max_tran_resp_time = max_tran_resp_time

    @property
    def min(self):
        """Gets the min of this PerformanceInfo.

        最小响应时间

        :return: The min of this PerformanceInfo.
        :rtype: float
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this PerformanceInfo.

        最小响应时间

        :param min: The min of this PerformanceInfo.
        :type: float
        """
        self._min = min

    @property
    def min_network_traffic(self):
        """Gets the min_network_traffic of this PerformanceInfo.

        最小带宽

        :return: The min_network_traffic of this PerformanceInfo.
        :rtype: float
        """
        return self._min_network_traffic

    @min_network_traffic.setter
    def min_network_traffic(self, min_network_traffic):
        """Sets the min_network_traffic of this PerformanceInfo.

        最小带宽

        :param min_network_traffic: The min_network_traffic of this PerformanceInfo.
        :type: float
        """
        self._min_network_traffic = min_network_traffic

    @property
    def name(self):
        """Gets the name of this PerformanceInfo.

        名称

        :return: The name of this PerformanceInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PerformanceInfo.

        名称

        :param name: The name of this PerformanceInfo.
        :type: str
        """
        self._name = name

    @property
    def requests(self):
        """Gets the requests of this PerformanceInfo.

        请求数

        :return: The requests of this PerformanceInfo.
        :rtype: float
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this PerformanceInfo.

        请求数

        :param requests: The requests of this PerformanceInfo.
        :type: float
        """
        self._requests = requests

    @property
    def result(self):
        """Gets the result of this PerformanceInfo.

        用例/aw的执行结果

        :return: The result of this PerformanceInfo.
        :rtype: float
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this PerformanceInfo.

        用例/aw的执行结果

        :param result: The result of this PerformanceInfo.
        :type: float
        """
        self._result = result

    @property
    def start_time(self):
        """Gets the start_time of this PerformanceInfo.

        开始时间

        :return: The start_time of this PerformanceInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this PerformanceInfo.

        开始时间

        :param start_time: The start_time of this PerformanceInfo.
        :type: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this PerformanceInfo.

        用例状态

        :return: The status of this PerformanceInfo.
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PerformanceInfo.

        用例状态

        :param status: The status of this PerformanceInfo.
        :type: float
        """
        self._status = status

    @property
    def success_count(self):
        """Gets the success_count of this PerformanceInfo.

        成功数

        :return: The success_count of this PerformanceInfo.
        :rtype: float
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this PerformanceInfo.

        成功数

        :param success_count: The success_count of this PerformanceInfo.
        :type: float
        """
        self._success_count = success_count

    @property
    def success_rate(self):
        """Gets the success_rate of this PerformanceInfo.

        成功率

        :return: The success_rate of this PerformanceInfo.
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this PerformanceInfo.

        成功率

        :param success_rate: The success_rate of this PerformanceInfo.
        :type: float
        """
        self._success_rate = success_rate

    @property
    def sum1xx(self):
        """Gets the sum1xx of this PerformanceInfo.

        1xx响应码计数

        :return: The sum1xx of this PerformanceInfo.
        :rtype: float
        """
        return self._sum1xx

    @sum1xx.setter
    def sum1xx(self, sum1xx):
        """Sets the sum1xx of this PerformanceInfo.

        1xx响应码计数

        :param sum1xx: The sum1xx of this PerformanceInfo.
        :type: float
        """
        self._sum1xx = sum1xx

    @property
    def sum2xx(self):
        """Gets the sum2xx of this PerformanceInfo.

        2xx响应码计数

        :return: The sum2xx of this PerformanceInfo.
        :rtype: float
        """
        return self._sum2xx

    @sum2xx.setter
    def sum2xx(self, sum2xx):
        """Sets the sum2xx of this PerformanceInfo.

        2xx响应码计数

        :param sum2xx: The sum2xx of this PerformanceInfo.
        :type: float
        """
        self._sum2xx = sum2xx

    @property
    def sum3xx(self):
        """Gets the sum3xx of this PerformanceInfo.

        3xx响应码计数

        :return: The sum3xx of this PerformanceInfo.
        :rtype: float
        """
        return self._sum3xx

    @sum3xx.setter
    def sum3xx(self, sum3xx):
        """Sets the sum3xx of this PerformanceInfo.

        3xx响应码计数

        :param sum3xx: The sum3xx of this PerformanceInfo.
        :type: float
        """
        self._sum3xx = sum3xx

    @property
    def sum4xx(self):
        """Gets the sum4xx of this PerformanceInfo.

        4xx响应码计数

        :return: The sum4xx of this PerformanceInfo.
        :rtype: float
        """
        return self._sum4xx

    @sum4xx.setter
    def sum4xx(self, sum4xx):
        """Sets the sum4xx of this PerformanceInfo.

        4xx响应码计数

        :param sum4xx: The sum4xx of this PerformanceInfo.
        :type: float
        """
        self._sum4xx = sum4xx

    @property
    def sum5xx(self):
        """Gets the sum5xx of this PerformanceInfo.

        5xx响应码计数

        :return: The sum5xx of this PerformanceInfo.
        :rtype: float
        """
        return self._sum5xx

    @sum5xx.setter
    def sum5xx(self, sum5xx):
        """Sets the sum5xx of this PerformanceInfo.

        5xx响应码计数

        :param sum5xx: The sum5xx of this PerformanceInfo.
        :type: float
        """
        self._sum5xx = sum5xx

    @property
    def task_id(self):
        """Gets the task_id of this PerformanceInfo.

        任务id_轮次

        :return: The task_id of this PerformanceInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this PerformanceInfo.

        任务id_轮次

        :param task_id: The task_id of this PerformanceInfo.
        :type: str
        """
        self._task_id = task_id

    @property
    def task_project_id(self):
        """Gets the task_project_id of this PerformanceInfo.

        任务id

        :return: The task_project_id of this PerformanceInfo.
        :rtype: str
        """
        return self._task_project_id

    @task_project_id.setter
    def task_project_id(self, task_project_id):
        """Sets the task_project_id of this PerformanceInfo.

        任务id

        :param task_project_id: The task_project_id of this PerformanceInfo.
        :type: str
        """
        self._task_project_id = task_project_id

    @property
    def task_status(self):
        """Gets the task_status of this PerformanceInfo.

        任务状态

        :return: The task_status of this PerformanceInfo.
        :rtype: float
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this PerformanceInfo.

        任务状态

        :param task_status: The task_status of this PerformanceInfo.
        :type: float
        """
        self._task_status = task_status

    @property
    def test_case_uri(self):
        """Gets the test_case_uri of this PerformanceInfo.

        用例uri

        :return: The test_case_uri of this PerformanceInfo.
        :rtype: str
        """
        return self._test_case_uri

    @test_case_uri.setter
    def test_case_uri(self, test_case_uri):
        """Sets the test_case_uri of this PerformanceInfo.

        用例uri

        :param test_case_uri: The test_case_uri of this PerformanceInfo.
        :type: str
        """
        self._test_case_uri = test_case_uri

    @property
    def tp50(self):
        """Gets the tp50 of this PerformanceInfo.

        tp50

        :return: The tp50 of this PerformanceInfo.
        :rtype: float
        """
        return self._tp50

    @tp50.setter
    def tp50(self, tp50):
        """Sets the tp50 of this PerformanceInfo.

        tp50

        :param tp50: The tp50 of this PerformanceInfo.
        :type: float
        """
        self._tp50 = tp50

    @property
    def tp75(self):
        """Gets the tp75 of this PerformanceInfo.

        tp75

        :return: The tp75 of this PerformanceInfo.
        :rtype: float
        """
        return self._tp75

    @tp75.setter
    def tp75(self, tp75):
        """Sets the tp75 of this PerformanceInfo.

        tp75

        :param tp75: The tp75 of this PerformanceInfo.
        :type: float
        """
        self._tp75 = tp75

    @property
    def tp90(self):
        """Gets the tp90 of this PerformanceInfo.

        tp90

        :return: The tp90 of this PerformanceInfo.
        :rtype: float
        """
        return self._tp90

    @tp90.setter
    def tp90(self, tp90):
        """Sets the tp90 of this PerformanceInfo.

        tp90

        :param tp90: The tp90 of this PerformanceInfo.
        :type: float
        """
        self._tp90 = tp90

    @property
    def tp95(self):
        """Gets the tp95 of this PerformanceInfo.

        tp95

        :return: The tp95 of this PerformanceInfo.
        :rtype: float
        """
        return self._tp95

    @tp95.setter
    def tp95(self, tp95):
        """Sets the tp95 of this PerformanceInfo.

        tp95

        :param tp95: The tp95 of this PerformanceInfo.
        :type: float
        """
        self._tp95 = tp95

    @property
    def tp99(self):
        """Gets the tp99 of this PerformanceInfo.

        tp99

        :return: The tp99 of this PerformanceInfo.
        :rtype: float
        """
        return self._tp99

    @tp99.setter
    def tp99(self, tp99):
        """Sets the tp99 of this PerformanceInfo.

        tp99

        :param tp99: The tp99 of this PerformanceInfo.
        :type: float
        """
        self._tp99 = tp99

    @property
    def tp999(self):
        """Gets the tp999 of this PerformanceInfo.

        tp999

        :return: The tp999 of this PerformanceInfo.
        :rtype: float
        """
        return self._tp999

    @tp999.setter
    def tp999(self, tp999):
        """Sets the tp999 of this PerformanceInfo.

        tp999

        :param tp999: The tp999 of this PerformanceInfo.
        :type: float
        """
        self._tp999 = tp999

    @property
    def tp9999(self):
        """Gets the tp9999 of this PerformanceInfo.

        tp9999

        :return: The tp9999 of this PerformanceInfo.
        :rtype: float
        """
        return self._tp9999

    @tp9999.setter
    def tp9999(self, tp9999):
        """Sets the tp9999 of this PerformanceInfo.

        tp9999

        :param tp9999: The tp9999 of this PerformanceInfo.
        :type: float
        """
        self._tp9999 = tp9999

    @property
    def tps(self):
        """Gets the tps of this PerformanceInfo.

        tps

        :return: The tps of this PerformanceInfo.
        :rtype: float
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this PerformanceInfo.

        tps

        :param tps: The tps of this PerformanceInfo.
        :type: float
        """
        self._tps = tps

    @property
    def tran_tps(self):
        """Gets the tran_tps of this PerformanceInfo.

        事务TPS

        :return: The tran_tps of this PerformanceInfo.
        :rtype: float
        """
        return self._tran_tps

    @tran_tps.setter
    def tran_tps(self, tran_tps):
        """Sets the tran_tps of this PerformanceInfo.

        事务TPS

        :param tran_tps: The tran_tps of this PerformanceInfo.
        :type: float
        """
        self._tran_tps = tran_tps

    @property
    def transaction_id(self):
        """Gets the transaction_id of this PerformanceInfo.

        事务id

        :return: The transaction_id of this PerformanceInfo.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this PerformanceInfo.

        事务id

        :param transaction_id: The transaction_id of this PerformanceInfo.
        :type: str
        """
        self._transaction_id = transaction_id

    @property
    def transaction_success(self):
        """Gets the transaction_success of this PerformanceInfo.

        成功事务数

        :return: The transaction_success of this PerformanceInfo.
        :rtype: float
        """
        return self._transaction_success

    @transaction_success.setter
    def transaction_success(self, transaction_success):
        """Sets the transaction_success of this PerformanceInfo.

        成功事务数

        :param transaction_success: The transaction_success of this PerformanceInfo.
        :type: float
        """
        self._transaction_success = transaction_success

    @property
    def transactional_success_rate(self):
        """Gets the transactional_success_rate of this PerformanceInfo.

        事务成功率

        :return: The transactional_success_rate of this PerformanceInfo.
        :rtype: float
        """
        return self._transactional_success_rate

    @transactional_success_rate.setter
    def transactional_success_rate(self, transactional_success_rate):
        """Sets the transactional_success_rate of this PerformanceInfo.

        事务成功率

        :param transactional_success_rate: The transactional_success_rate of this PerformanceInfo.
        :type: float
        """
        self._transactional_success_rate = transactional_success_rate

    @property
    def transactional_tps(self):
        """Gets the transactional_tps of this PerformanceInfo.

        自定义事务tps

        :return: The transactional_tps of this PerformanceInfo.
        :rtype: float
        """
        return self._transactional_tps

    @transactional_tps.setter
    def transactional_tps(self, transactional_tps):
        """Sets the transactional_tps of this PerformanceInfo.

        自定义事务tps

        :param transactional_tps: The transactional_tps of this PerformanceInfo.
        :type: float
        """
        self._transactional_tps = transactional_tps

    @property
    def transactional_tps_success(self):
        """Gets the transactional_tps_success of this PerformanceInfo.

        自定义事务成功率

        :return: The transactional_tps_success of this PerformanceInfo.
        :rtype: float
        """
        return self._transactional_tps_success

    @transactional_tps_success.setter
    def transactional_tps_success(self, transactional_tps_success):
        """Sets the transactional_tps_success of this PerformanceInfo.

        自定义事务成功率

        :param transactional_tps_success: The transactional_tps_success of this PerformanceInfo.
        :type: float
        """
        self._transactional_tps_success = transactional_tps_success

    @property
    def transactions(self):
        """Gets the transactions of this PerformanceInfo.

        事务数

        :return: The transactions of this PerformanceInfo.
        :rtype: float
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this PerformanceInfo.

        事务数

        :param transactions: The transactions of this PerformanceInfo.
        :type: float
        """
        self._transactions = transactions

    @property
    def update_time(self):
        """Gets the update_time of this PerformanceInfo.

        更新时间

        :return: The update_time of this PerformanceInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this PerformanceInfo.

        更新时间

        :param update_time: The update_time of this PerformanceInfo.
        :type: str
        """
        self._update_time = update_time

    @property
    def vum(self):
        """Gets the vum of this PerformanceInfo.

        分钟数*并发数

        :return: The vum of this PerformanceInfo.
        :rtype: float
        """
        return self._vum

    @vum.setter
    def vum(self, vum):
        """Sets the vum of this PerformanceInfo.

        分钟数*并发数

        :param vum: The vum of this PerformanceInfo.
        :type: float
        """
        self._vum = vum

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
        if not isinstance(other, PerformanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
