# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetailDataInfo:


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
        'avg_rec_bytes': 'float',
        'avg_sent_bytes': 'int',
        'avg_tran_resp_time': 'str',
        'case_uri': 'str',
        'create_time': 'str',
        'current_thread_num': 'int',
        'detail_id': 'str',
        'end_time': 'str',
        'error_count': 'int',
        'error_events_count': 'int',
        'failed_assert': 'int',
        'failed_others': 'int',
        'failed_parsed': 'int',
        'failed_refused': 'int',
        'failed_timeout': 'int',
        'id': 'str',
        'is_aw': 'bool',
        'max': 'int',
        'max_rec_bytes': 'int',
        'max_resp_time': 'int',
        'max_sent_bytes': 'int',
        'max_tran_resp_time': 'int',
        'min': 'int',
        'name': 'str',
        'requests': 'int',
        'result': 'int',
        'start_time': 'str',
        'status': 'int',
        'success_count': 'int',
        'success_rate': 'int',
        'sum1xx': 'int',
        'sum2xx': 'int',
        'sum3xx': 'int',
        'sum4xx': 'int',
        'sum5xx': 'int',
        'task_id': 'str',
        'task_project_id': 'str',
        'task_status': 'int',
        'test_case_uri': 'str',
        'tp50': 'int',
        'tp75': 'int',
        'tp90': 'int',
        'tp95': 'int',
        'tp99': 'int',
        'tps': 'float',
        'tran_tps': 'str',
        'transaction_id': 'str',
        'transaction_success': 'str',
        'transactional_success_rate': 'int',
        'transactional_tps': 'int',
        'transactional_tps_success': 'int',
        'transactions': 'str',
        'update_time': 'str',
        'vum': 'int'
    }

    attribute_map = {
        'average_resp_time': 'averageRespTime',
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
        'max_rec_bytes': 'maxRecBytes',
        'max_resp_time': 'maxRespTime',
        'max_sent_bytes': 'maxSentBytes',
        'max_tran_resp_time': 'maxTranRespTime',
        'min': 'min',
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

    def __init__(self, average_resp_time=None, avg_rec_bytes=None, avg_sent_bytes=None, avg_tran_resp_time=None, case_uri=None, create_time=None, current_thread_num=None, detail_id=None, end_time=None, error_count=None, error_events_count=None, failed_assert=None, failed_others=None, failed_parsed=None, failed_refused=None, failed_timeout=None, id=None, is_aw=None, max=None, max_rec_bytes=None, max_resp_time=None, max_sent_bytes=None, max_tran_resp_time=None, min=None, name=None, requests=None, result=None, start_time=None, status=None, success_count=None, success_rate=None, sum1xx=None, sum2xx=None, sum3xx=None, sum4xx=None, sum5xx=None, task_id=None, task_project_id=None, task_status=None, test_case_uri=None, tp50=None, tp75=None, tp90=None, tp95=None, tp99=None, tps=None, tran_tps=None, transaction_id=None, transaction_success=None, transactional_success_rate=None, transactional_tps=None, transactional_tps_success=None, transactions=None, update_time=None, vum=None):
        """DetailDataInfo - a model defined in huaweicloud sdk"""
        
        

        self._average_resp_time = None
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
        self._max_rec_bytes = None
        self._max_resp_time = None
        self._max_sent_bytes = None
        self._max_tran_resp_time = None
        self._min = None
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
        """Gets the average_resp_time of this DetailDataInfo.

        averageRespTime

        :return: The average_resp_time of this DetailDataInfo.
        :rtype: float
        """
        return self._average_resp_time

    @average_resp_time.setter
    def average_resp_time(self, average_resp_time):
        """Sets the average_resp_time of this DetailDataInfo.

        averageRespTime

        :param average_resp_time: The average_resp_time of this DetailDataInfo.
        :type: float
        """
        self._average_resp_time = average_resp_time

    @property
    def avg_rec_bytes(self):
        """Gets the avg_rec_bytes of this DetailDataInfo.

        avgRecBytes

        :return: The avg_rec_bytes of this DetailDataInfo.
        :rtype: float
        """
        return self._avg_rec_bytes

    @avg_rec_bytes.setter
    def avg_rec_bytes(self, avg_rec_bytes):
        """Sets the avg_rec_bytes of this DetailDataInfo.

        avgRecBytes

        :param avg_rec_bytes: The avg_rec_bytes of this DetailDataInfo.
        :type: float
        """
        self._avg_rec_bytes = avg_rec_bytes

    @property
    def avg_sent_bytes(self):
        """Gets the avg_sent_bytes of this DetailDataInfo.

        avgSentBytes

        :return: The avg_sent_bytes of this DetailDataInfo.
        :rtype: int
        """
        return self._avg_sent_bytes

    @avg_sent_bytes.setter
    def avg_sent_bytes(self, avg_sent_bytes):
        """Sets the avg_sent_bytes of this DetailDataInfo.

        avgSentBytes

        :param avg_sent_bytes: The avg_sent_bytes of this DetailDataInfo.
        :type: int
        """
        self._avg_sent_bytes = avg_sent_bytes

    @property
    def avg_tran_resp_time(self):
        """Gets the avg_tran_resp_time of this DetailDataInfo.

        avgTranRespTime

        :return: The avg_tran_resp_time of this DetailDataInfo.
        :rtype: str
        """
        return self._avg_tran_resp_time

    @avg_tran_resp_time.setter
    def avg_tran_resp_time(self, avg_tran_resp_time):
        """Sets the avg_tran_resp_time of this DetailDataInfo.

        avgTranRespTime

        :param avg_tran_resp_time: The avg_tran_resp_time of this DetailDataInfo.
        :type: str
        """
        self._avg_tran_resp_time = avg_tran_resp_time

    @property
    def case_uri(self):
        """Gets the case_uri of this DetailDataInfo.

        caseUri

        :return: The case_uri of this DetailDataInfo.
        :rtype: str
        """
        return self._case_uri

    @case_uri.setter
    def case_uri(self, case_uri):
        """Sets the case_uri of this DetailDataInfo.

        caseUri

        :param case_uri: The case_uri of this DetailDataInfo.
        :type: str
        """
        self._case_uri = case_uri

    @property
    def create_time(self):
        """Gets the create_time of this DetailDataInfo.

        createTime

        :return: The create_time of this DetailDataInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DetailDataInfo.

        createTime

        :param create_time: The create_time of this DetailDataInfo.
        :type: str
        """
        self._create_time = create_time

    @property
    def current_thread_num(self):
        """Gets the current_thread_num of this DetailDataInfo.

        currentThreadNum

        :return: The current_thread_num of this DetailDataInfo.
        :rtype: int
        """
        return self._current_thread_num

    @current_thread_num.setter
    def current_thread_num(self, current_thread_num):
        """Sets the current_thread_num of this DetailDataInfo.

        currentThreadNum

        :param current_thread_num: The current_thread_num of this DetailDataInfo.
        :type: int
        """
        self._current_thread_num = current_thread_num

    @property
    def detail_id(self):
        """Gets the detail_id of this DetailDataInfo.

        detailId

        :return: The detail_id of this DetailDataInfo.
        :rtype: str
        """
        return self._detail_id

    @detail_id.setter
    def detail_id(self, detail_id):
        """Sets the detail_id of this DetailDataInfo.

        detailId

        :param detail_id: The detail_id of this DetailDataInfo.
        :type: str
        """
        self._detail_id = detail_id

    @property
    def end_time(self):
        """Gets the end_time of this DetailDataInfo.

        endTime

        :return: The end_time of this DetailDataInfo.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this DetailDataInfo.

        endTime

        :param end_time: The end_time of this DetailDataInfo.
        :type: str
        """
        self._end_time = end_time

    @property
    def error_count(self):
        """Gets the error_count of this DetailDataInfo.

        errorCount

        :return: The error_count of this DetailDataInfo.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this DetailDataInfo.

        errorCount

        :param error_count: The error_count of this DetailDataInfo.
        :type: int
        """
        self._error_count = error_count

    @property
    def error_events_count(self):
        """Gets the error_events_count of this DetailDataInfo.

        errorEventsCount

        :return: The error_events_count of this DetailDataInfo.
        :rtype: int
        """
        return self._error_events_count

    @error_events_count.setter
    def error_events_count(self, error_events_count):
        """Sets the error_events_count of this DetailDataInfo.

        errorEventsCount

        :param error_events_count: The error_events_count of this DetailDataInfo.
        :type: int
        """
        self._error_events_count = error_events_count

    @property
    def failed_assert(self):
        """Gets the failed_assert of this DetailDataInfo.

        failedAssert

        :return: The failed_assert of this DetailDataInfo.
        :rtype: int
        """
        return self._failed_assert

    @failed_assert.setter
    def failed_assert(self, failed_assert):
        """Sets the failed_assert of this DetailDataInfo.

        failedAssert

        :param failed_assert: The failed_assert of this DetailDataInfo.
        :type: int
        """
        self._failed_assert = failed_assert

    @property
    def failed_others(self):
        """Gets the failed_others of this DetailDataInfo.

        failedOthers

        :return: The failed_others of this DetailDataInfo.
        :rtype: int
        """
        return self._failed_others

    @failed_others.setter
    def failed_others(self, failed_others):
        """Sets the failed_others of this DetailDataInfo.

        failedOthers

        :param failed_others: The failed_others of this DetailDataInfo.
        :type: int
        """
        self._failed_others = failed_others

    @property
    def failed_parsed(self):
        """Gets the failed_parsed of this DetailDataInfo.

        failedParsed

        :return: The failed_parsed of this DetailDataInfo.
        :rtype: int
        """
        return self._failed_parsed

    @failed_parsed.setter
    def failed_parsed(self, failed_parsed):
        """Sets the failed_parsed of this DetailDataInfo.

        failedParsed

        :param failed_parsed: The failed_parsed of this DetailDataInfo.
        :type: int
        """
        self._failed_parsed = failed_parsed

    @property
    def failed_refused(self):
        """Gets the failed_refused of this DetailDataInfo.

        failedRefused

        :return: The failed_refused of this DetailDataInfo.
        :rtype: int
        """
        return self._failed_refused

    @failed_refused.setter
    def failed_refused(self, failed_refused):
        """Sets the failed_refused of this DetailDataInfo.

        failedRefused

        :param failed_refused: The failed_refused of this DetailDataInfo.
        :type: int
        """
        self._failed_refused = failed_refused

    @property
    def failed_timeout(self):
        """Gets the failed_timeout of this DetailDataInfo.

        failedTimeout

        :return: The failed_timeout of this DetailDataInfo.
        :rtype: int
        """
        return self._failed_timeout

    @failed_timeout.setter
    def failed_timeout(self, failed_timeout):
        """Sets the failed_timeout of this DetailDataInfo.

        failedTimeout

        :param failed_timeout: The failed_timeout of this DetailDataInfo.
        :type: int
        """
        self._failed_timeout = failed_timeout

    @property
    def id(self):
        """Gets the id of this DetailDataInfo.

        id

        :return: The id of this DetailDataInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DetailDataInfo.

        id

        :param id: The id of this DetailDataInfo.
        :type: str
        """
        self._id = id

    @property
    def is_aw(self):
        """Gets the is_aw of this DetailDataInfo.

        isAW

        :return: The is_aw of this DetailDataInfo.
        :rtype: bool
        """
        return self._is_aw

    @is_aw.setter
    def is_aw(self, is_aw):
        """Sets the is_aw of this DetailDataInfo.

        isAW

        :param is_aw: The is_aw of this DetailDataInfo.
        :type: bool
        """
        self._is_aw = is_aw

    @property
    def max(self):
        """Gets the max of this DetailDataInfo.

        max

        :return: The max of this DetailDataInfo.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this DetailDataInfo.

        max

        :param max: The max of this DetailDataInfo.
        :type: int
        """
        self._max = max

    @property
    def max_rec_bytes(self):
        """Gets the max_rec_bytes of this DetailDataInfo.

        maxRecBytes

        :return: The max_rec_bytes of this DetailDataInfo.
        :rtype: int
        """
        return self._max_rec_bytes

    @max_rec_bytes.setter
    def max_rec_bytes(self, max_rec_bytes):
        """Sets the max_rec_bytes of this DetailDataInfo.

        maxRecBytes

        :param max_rec_bytes: The max_rec_bytes of this DetailDataInfo.
        :type: int
        """
        self._max_rec_bytes = max_rec_bytes

    @property
    def max_resp_time(self):
        """Gets the max_resp_time of this DetailDataInfo.

        maxRespTime

        :return: The max_resp_time of this DetailDataInfo.
        :rtype: int
        """
        return self._max_resp_time

    @max_resp_time.setter
    def max_resp_time(self, max_resp_time):
        """Sets the max_resp_time of this DetailDataInfo.

        maxRespTime

        :param max_resp_time: The max_resp_time of this DetailDataInfo.
        :type: int
        """
        self._max_resp_time = max_resp_time

    @property
    def max_sent_bytes(self):
        """Gets the max_sent_bytes of this DetailDataInfo.

        maxSentBytes

        :return: The max_sent_bytes of this DetailDataInfo.
        :rtype: int
        """
        return self._max_sent_bytes

    @max_sent_bytes.setter
    def max_sent_bytes(self, max_sent_bytes):
        """Sets the max_sent_bytes of this DetailDataInfo.

        maxSentBytes

        :param max_sent_bytes: The max_sent_bytes of this DetailDataInfo.
        :type: int
        """
        self._max_sent_bytes = max_sent_bytes

    @property
    def max_tran_resp_time(self):
        """Gets the max_tran_resp_time of this DetailDataInfo.

        maxTranRespTime

        :return: The max_tran_resp_time of this DetailDataInfo.
        :rtype: int
        """
        return self._max_tran_resp_time

    @max_tran_resp_time.setter
    def max_tran_resp_time(self, max_tran_resp_time):
        """Sets the max_tran_resp_time of this DetailDataInfo.

        maxTranRespTime

        :param max_tran_resp_time: The max_tran_resp_time of this DetailDataInfo.
        :type: int
        """
        self._max_tran_resp_time = max_tran_resp_time

    @property
    def min(self):
        """Gets the min of this DetailDataInfo.

        min

        :return: The min of this DetailDataInfo.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this DetailDataInfo.

        min

        :param min: The min of this DetailDataInfo.
        :type: int
        """
        self._min = min

    @property
    def name(self):
        """Gets the name of this DetailDataInfo.

        name

        :return: The name of this DetailDataInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DetailDataInfo.

        name

        :param name: The name of this DetailDataInfo.
        :type: str
        """
        self._name = name

    @property
    def requests(self):
        """Gets the requests of this DetailDataInfo.

        requests

        :return: The requests of this DetailDataInfo.
        :rtype: int
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this DetailDataInfo.

        requests

        :param requests: The requests of this DetailDataInfo.
        :type: int
        """
        self._requests = requests

    @property
    def result(self):
        """Gets the result of this DetailDataInfo.

        result

        :return: The result of this DetailDataInfo.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DetailDataInfo.

        result

        :param result: The result of this DetailDataInfo.
        :type: int
        """
        self._result = result

    @property
    def start_time(self):
        """Gets the start_time of this DetailDataInfo.

        startTime

        :return: The start_time of this DetailDataInfo.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DetailDataInfo.

        startTime

        :param start_time: The start_time of this DetailDataInfo.
        :type: str
        """
        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this DetailDataInfo.

        status

        :return: The status of this DetailDataInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DetailDataInfo.

        status

        :param status: The status of this DetailDataInfo.
        :type: int
        """
        self._status = status

    @property
    def success_count(self):
        """Gets the success_count of this DetailDataInfo.

        successCount

        :return: The success_count of this DetailDataInfo.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this DetailDataInfo.

        successCount

        :param success_count: The success_count of this DetailDataInfo.
        :type: int
        """
        self._success_count = success_count

    @property
    def success_rate(self):
        """Gets the success_rate of this DetailDataInfo.

        successRate

        :return: The success_rate of this DetailDataInfo.
        :rtype: int
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        """Sets the success_rate of this DetailDataInfo.

        successRate

        :param success_rate: The success_rate of this DetailDataInfo.
        :type: int
        """
        self._success_rate = success_rate

    @property
    def sum1xx(self):
        """Gets the sum1xx of this DetailDataInfo.

        sum1xx

        :return: The sum1xx of this DetailDataInfo.
        :rtype: int
        """
        return self._sum1xx

    @sum1xx.setter
    def sum1xx(self, sum1xx):
        """Sets the sum1xx of this DetailDataInfo.

        sum1xx

        :param sum1xx: The sum1xx of this DetailDataInfo.
        :type: int
        """
        self._sum1xx = sum1xx

    @property
    def sum2xx(self):
        """Gets the sum2xx of this DetailDataInfo.

        sum2xx

        :return: The sum2xx of this DetailDataInfo.
        :rtype: int
        """
        return self._sum2xx

    @sum2xx.setter
    def sum2xx(self, sum2xx):
        """Sets the sum2xx of this DetailDataInfo.

        sum2xx

        :param sum2xx: The sum2xx of this DetailDataInfo.
        :type: int
        """
        self._sum2xx = sum2xx

    @property
    def sum3xx(self):
        """Gets the sum3xx of this DetailDataInfo.

        sum3xx

        :return: The sum3xx of this DetailDataInfo.
        :rtype: int
        """
        return self._sum3xx

    @sum3xx.setter
    def sum3xx(self, sum3xx):
        """Sets the sum3xx of this DetailDataInfo.

        sum3xx

        :param sum3xx: The sum3xx of this DetailDataInfo.
        :type: int
        """
        self._sum3xx = sum3xx

    @property
    def sum4xx(self):
        """Gets the sum4xx of this DetailDataInfo.

        sum4xx

        :return: The sum4xx of this DetailDataInfo.
        :rtype: int
        """
        return self._sum4xx

    @sum4xx.setter
    def sum4xx(self, sum4xx):
        """Sets the sum4xx of this DetailDataInfo.

        sum4xx

        :param sum4xx: The sum4xx of this DetailDataInfo.
        :type: int
        """
        self._sum4xx = sum4xx

    @property
    def sum5xx(self):
        """Gets the sum5xx of this DetailDataInfo.

        sum5xx

        :return: The sum5xx of this DetailDataInfo.
        :rtype: int
        """
        return self._sum5xx

    @sum5xx.setter
    def sum5xx(self, sum5xx):
        """Sets the sum5xx of this DetailDataInfo.

        sum5xx

        :param sum5xx: The sum5xx of this DetailDataInfo.
        :type: int
        """
        self._sum5xx = sum5xx

    @property
    def task_id(self):
        """Gets the task_id of this DetailDataInfo.

        taskId

        :return: The task_id of this DetailDataInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DetailDataInfo.

        taskId

        :param task_id: The task_id of this DetailDataInfo.
        :type: str
        """
        self._task_id = task_id

    @property
    def task_project_id(self):
        """Gets the task_project_id of this DetailDataInfo.

        taskProjectId

        :return: The task_project_id of this DetailDataInfo.
        :rtype: str
        """
        return self._task_project_id

    @task_project_id.setter
    def task_project_id(self, task_project_id):
        """Sets the task_project_id of this DetailDataInfo.

        taskProjectId

        :param task_project_id: The task_project_id of this DetailDataInfo.
        :type: str
        """
        self._task_project_id = task_project_id

    @property
    def task_status(self):
        """Gets the task_status of this DetailDataInfo.

        taskStatus

        :return: The task_status of this DetailDataInfo.
        :rtype: int
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this DetailDataInfo.

        taskStatus

        :param task_status: The task_status of this DetailDataInfo.
        :type: int
        """
        self._task_status = task_status

    @property
    def test_case_uri(self):
        """Gets the test_case_uri of this DetailDataInfo.

        testCaseUri

        :return: The test_case_uri of this DetailDataInfo.
        :rtype: str
        """
        return self._test_case_uri

    @test_case_uri.setter
    def test_case_uri(self, test_case_uri):
        """Sets the test_case_uri of this DetailDataInfo.

        testCaseUri

        :param test_case_uri: The test_case_uri of this DetailDataInfo.
        :type: str
        """
        self._test_case_uri = test_case_uri

    @property
    def tp50(self):
        """Gets the tp50 of this DetailDataInfo.

        tp50

        :return: The tp50 of this DetailDataInfo.
        :rtype: int
        """
        return self._tp50

    @tp50.setter
    def tp50(self, tp50):
        """Sets the tp50 of this DetailDataInfo.

        tp50

        :param tp50: The tp50 of this DetailDataInfo.
        :type: int
        """
        self._tp50 = tp50

    @property
    def tp75(self):
        """Gets the tp75 of this DetailDataInfo.

        tp75

        :return: The tp75 of this DetailDataInfo.
        :rtype: int
        """
        return self._tp75

    @tp75.setter
    def tp75(self, tp75):
        """Sets the tp75 of this DetailDataInfo.

        tp75

        :param tp75: The tp75 of this DetailDataInfo.
        :type: int
        """
        self._tp75 = tp75

    @property
    def tp90(self):
        """Gets the tp90 of this DetailDataInfo.

        tp90

        :return: The tp90 of this DetailDataInfo.
        :rtype: int
        """
        return self._tp90

    @tp90.setter
    def tp90(self, tp90):
        """Sets the tp90 of this DetailDataInfo.

        tp90

        :param tp90: The tp90 of this DetailDataInfo.
        :type: int
        """
        self._tp90 = tp90

    @property
    def tp95(self):
        """Gets the tp95 of this DetailDataInfo.

        tp95

        :return: The tp95 of this DetailDataInfo.
        :rtype: int
        """
        return self._tp95

    @tp95.setter
    def tp95(self, tp95):
        """Sets the tp95 of this DetailDataInfo.

        tp95

        :param tp95: The tp95 of this DetailDataInfo.
        :type: int
        """
        self._tp95 = tp95

    @property
    def tp99(self):
        """Gets the tp99 of this DetailDataInfo.

        tp99

        :return: The tp99 of this DetailDataInfo.
        :rtype: int
        """
        return self._tp99

    @tp99.setter
    def tp99(self, tp99):
        """Sets the tp99 of this DetailDataInfo.

        tp99

        :param tp99: The tp99 of this DetailDataInfo.
        :type: int
        """
        self._tp99 = tp99

    @property
    def tps(self):
        """Gets the tps of this DetailDataInfo.

        tps

        :return: The tps of this DetailDataInfo.
        :rtype: float
        """
        return self._tps

    @tps.setter
    def tps(self, tps):
        """Sets the tps of this DetailDataInfo.

        tps

        :param tps: The tps of this DetailDataInfo.
        :type: float
        """
        self._tps = tps

    @property
    def tran_tps(self):
        """Gets the tran_tps of this DetailDataInfo.

        tranTPS

        :return: The tran_tps of this DetailDataInfo.
        :rtype: str
        """
        return self._tran_tps

    @tran_tps.setter
    def tran_tps(self, tran_tps):
        """Sets the tran_tps of this DetailDataInfo.

        tranTPS

        :param tran_tps: The tran_tps of this DetailDataInfo.
        :type: str
        """
        self._tran_tps = tran_tps

    @property
    def transaction_id(self):
        """Gets the transaction_id of this DetailDataInfo.

        transactionId

        :return: The transaction_id of this DetailDataInfo.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this DetailDataInfo.

        transactionId

        :param transaction_id: The transaction_id of this DetailDataInfo.
        :type: str
        """
        self._transaction_id = transaction_id

    @property
    def transaction_success(self):
        """Gets the transaction_success of this DetailDataInfo.

        transactionSuccess

        :return: The transaction_success of this DetailDataInfo.
        :rtype: str
        """
        return self._transaction_success

    @transaction_success.setter
    def transaction_success(self, transaction_success):
        """Sets the transaction_success of this DetailDataInfo.

        transactionSuccess

        :param transaction_success: The transaction_success of this DetailDataInfo.
        :type: str
        """
        self._transaction_success = transaction_success

    @property
    def transactional_success_rate(self):
        """Gets the transactional_success_rate of this DetailDataInfo.

        transactionalSuccessRate

        :return: The transactional_success_rate of this DetailDataInfo.
        :rtype: int
        """
        return self._transactional_success_rate

    @transactional_success_rate.setter
    def transactional_success_rate(self, transactional_success_rate):
        """Sets the transactional_success_rate of this DetailDataInfo.

        transactionalSuccessRate

        :param transactional_success_rate: The transactional_success_rate of this DetailDataInfo.
        :type: int
        """
        self._transactional_success_rate = transactional_success_rate

    @property
    def transactional_tps(self):
        """Gets the transactional_tps of this DetailDataInfo.

        transactionalTps

        :return: The transactional_tps of this DetailDataInfo.
        :rtype: int
        """
        return self._transactional_tps

    @transactional_tps.setter
    def transactional_tps(self, transactional_tps):
        """Sets the transactional_tps of this DetailDataInfo.

        transactionalTps

        :param transactional_tps: The transactional_tps of this DetailDataInfo.
        :type: int
        """
        self._transactional_tps = transactional_tps

    @property
    def transactional_tps_success(self):
        """Gets the transactional_tps_success of this DetailDataInfo.

        transactionalTpsSuccess

        :return: The transactional_tps_success of this DetailDataInfo.
        :rtype: int
        """
        return self._transactional_tps_success

    @transactional_tps_success.setter
    def transactional_tps_success(self, transactional_tps_success):
        """Sets the transactional_tps_success of this DetailDataInfo.

        transactionalTpsSuccess

        :param transactional_tps_success: The transactional_tps_success of this DetailDataInfo.
        :type: int
        """
        self._transactional_tps_success = transactional_tps_success

    @property
    def transactions(self):
        """Gets the transactions of this DetailDataInfo.

        transactions

        :return: The transactions of this DetailDataInfo.
        :rtype: str
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this DetailDataInfo.

        transactions

        :param transactions: The transactions of this DetailDataInfo.
        :type: str
        """
        self._transactions = transactions

    @property
    def update_time(self):
        """Gets the update_time of this DetailDataInfo.

        updateTime

        :return: The update_time of this DetailDataInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DetailDataInfo.

        updateTime

        :param update_time: The update_time of this DetailDataInfo.
        :type: str
        """
        self._update_time = update_time

    @property
    def vum(self):
        """Gets the vum of this DetailDataInfo.

        vum

        :return: The vum of this DetailDataInfo.
        :rtype: int
        """
        return self._vum

    @vum.setter
    def vum(self, vum):
        """Sets the vum of this DetailDataInfo.

        vum

        :param vum: The vum of this DetailDataInfo.
        :type: int
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
        if not isinstance(other, DetailDataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
