# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDeadLockAnalysisResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dead_lock_id': 'str',
        'job_id': 'str',
        'status': 'str',
        'sql_insight_job_id': 'int',
        'transaction_id': 'str',
        'total': 'int',
        'sql_list': 'list[ShowDeadLockAnalysisResultRespSqlList]',
        'transaction_ids': 'list[str]'
    }

    attribute_map = {
        'dead_lock_id': 'dead_lock_id',
        'job_id': 'job_id',
        'status': 'status',
        'sql_insight_job_id': 'sql_insight_job_id',
        'transaction_id': 'transaction_id',
        'total': 'total',
        'sql_list': 'sql_list',
        'transaction_ids': 'transaction_ids'
    }

    def __init__(self, dead_lock_id=None, job_id=None, status=None, sql_insight_job_id=None, transaction_id=None, total=None, sql_list=None, transaction_ids=None):
        r"""ShowDeadLockAnalysisResultResponse

        The model defined in huaweicloud sdk

        :param dead_lock_id: 死锁唯一标识
        :type dead_lock_id: str
        :param job_id: 分析任务ID
        :type job_id: str
        :param status: 分析任务状态
        :type status: str
        :param sql_insight_job_id: SQL洞察任务ID
        :type sql_insight_job_id: int
        :param transaction_id: 查询的事务ID
        :type transaction_id: str
        :param total: 该事务下SQL记录总数
        :type total: int
        :param sql_list: SQL详情列表
        :type sql_list: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockAnalysisResultRespSqlList`]
        :param transaction_ids: 从死锁事件解析的事务ID列表
        :type transaction_ids: list[str]
        """
        
        super().__init__()

        self._dead_lock_id = None
        self._job_id = None
        self._status = None
        self._sql_insight_job_id = None
        self._transaction_id = None
        self._total = None
        self._sql_list = None
        self._transaction_ids = None
        self.discriminator = None

        if dead_lock_id is not None:
            self.dead_lock_id = dead_lock_id
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if sql_insight_job_id is not None:
            self.sql_insight_job_id = sql_insight_job_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if total is not None:
            self.total = total
        if sql_list is not None:
            self.sql_list = sql_list
        if transaction_ids is not None:
            self.transaction_ids = transaction_ids

    @property
    def dead_lock_id(self):
        r"""Gets the dead_lock_id of this ShowDeadLockAnalysisResultResponse.

        死锁唯一标识

        :return: The dead_lock_id of this ShowDeadLockAnalysisResultResponse.
        :rtype: str
        """
        return self._dead_lock_id

    @dead_lock_id.setter
    def dead_lock_id(self, dead_lock_id):
        r"""Sets the dead_lock_id of this ShowDeadLockAnalysisResultResponse.

        死锁唯一标识

        :param dead_lock_id: The dead_lock_id of this ShowDeadLockAnalysisResultResponse.
        :type dead_lock_id: str
        """
        self._dead_lock_id = dead_lock_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowDeadLockAnalysisResultResponse.

        分析任务ID

        :return: The job_id of this ShowDeadLockAnalysisResultResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowDeadLockAnalysisResultResponse.

        分析任务ID

        :param job_id: The job_id of this ShowDeadLockAnalysisResultResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this ShowDeadLockAnalysisResultResponse.

        分析任务状态

        :return: The status of this ShowDeadLockAnalysisResultResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDeadLockAnalysisResultResponse.

        分析任务状态

        :param status: The status of this ShowDeadLockAnalysisResultResponse.
        :type status: str
        """
        self._status = status

    @property
    def sql_insight_job_id(self):
        r"""Gets the sql_insight_job_id of this ShowDeadLockAnalysisResultResponse.

        SQL洞察任务ID

        :return: The sql_insight_job_id of this ShowDeadLockAnalysisResultResponse.
        :rtype: int
        """
        return self._sql_insight_job_id

    @sql_insight_job_id.setter
    def sql_insight_job_id(self, sql_insight_job_id):
        r"""Sets the sql_insight_job_id of this ShowDeadLockAnalysisResultResponse.

        SQL洞察任务ID

        :param sql_insight_job_id: The sql_insight_job_id of this ShowDeadLockAnalysisResultResponse.
        :type sql_insight_job_id: int
        """
        self._sql_insight_job_id = sql_insight_job_id

    @property
    def transaction_id(self):
        r"""Gets the transaction_id of this ShowDeadLockAnalysisResultResponse.

        查询的事务ID

        :return: The transaction_id of this ShowDeadLockAnalysisResultResponse.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        r"""Sets the transaction_id of this ShowDeadLockAnalysisResultResponse.

        查询的事务ID

        :param transaction_id: The transaction_id of this ShowDeadLockAnalysisResultResponse.
        :type transaction_id: str
        """
        self._transaction_id = transaction_id

    @property
    def total(self):
        r"""Gets the total of this ShowDeadLockAnalysisResultResponse.

        该事务下SQL记录总数

        :return: The total of this ShowDeadLockAnalysisResultResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowDeadLockAnalysisResultResponse.

        该事务下SQL记录总数

        :param total: The total of this ShowDeadLockAnalysisResultResponse.
        :type total: int
        """
        self._total = total

    @property
    def sql_list(self):
        r"""Gets the sql_list of this ShowDeadLockAnalysisResultResponse.

        SQL详情列表

        :return: The sql_list of this ShowDeadLockAnalysisResultResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockAnalysisResultRespSqlList`]
        """
        return self._sql_list

    @sql_list.setter
    def sql_list(self, sql_list):
        r"""Sets the sql_list of this ShowDeadLockAnalysisResultResponse.

        SQL详情列表

        :param sql_list: The sql_list of this ShowDeadLockAnalysisResultResponse.
        :type sql_list: list[:class:`huaweicloudsdkdas.v3.ShowDeadLockAnalysisResultRespSqlList`]
        """
        self._sql_list = sql_list

    @property
    def transaction_ids(self):
        r"""Gets the transaction_ids of this ShowDeadLockAnalysisResultResponse.

        从死锁事件解析的事务ID列表

        :return: The transaction_ids of this ShowDeadLockAnalysisResultResponse.
        :rtype: list[str]
        """
        return self._transaction_ids

    @transaction_ids.setter
    def transaction_ids(self, transaction_ids):
        r"""Sets the transaction_ids of this ShowDeadLockAnalysisResultResponse.

        从死锁事件解析的事务ID列表

        :param transaction_ids: The transaction_ids of this ShowDeadLockAnalysisResultResponse.
        :type transaction_ids: list[str]
        """
        self._transaction_ids = transaction_ids

    def to_dict(self):
        import warnings
        warnings.warn("ShowDeadLockAnalysisResultResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowDeadLockAnalysisResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
