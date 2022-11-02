# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobExeListNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'job_name': 'str',
        'job_id': 'str',
        'user': 'str',
        'job_type': 'str',
        'job_state': 'str',
        'job_result': 'str',
        'queue': 'str',
        'limit': 'str',
        'offset': 'str',
        'sort_by': 'str',
        'submitted_time_begin': 'int',
        'submitted_time_end': 'int'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'job_name': 'job_name',
        'job_id': 'job_id',
        'user': 'user',
        'job_type': 'job_type',
        'job_state': 'job_state',
        'job_result': 'job_result',
        'queue': 'queue',
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'submitted_time_begin': 'submitted_time_begin',
        'submitted_time_end': 'submitted_time_end'
    }

    def __init__(self, cluster_id=None, job_name=None, job_id=None, user=None, job_type=None, job_state=None, job_result=None, queue=None, limit=None, offset=None, sort_by=None, submitted_time_begin=None, submitted_time_end=None):
        """ShowJobExeListNewRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。
        :type cluster_id: str
        :param job_name: 作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～128个字符。
        :type job_name: str
        :param job_id: 作业ID，只能由字母、数字、中划线(-)组成，并且长度为1~64字符。
        :type job_id: str
        :param user: 用户名称、只能由字母、数字、特殊字符(-_.)组成，且不能以数字开头，并且长度为1～32字符。
        :type user: str
        :param job_type: 作业类型。 - MapReduce - SparkPython - SparkSubmit：SparkPython类型的作业在查询时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink
        :type job_type: str
        :param job_state: 作业运行状态。 - FAILED：失败 - KILLED：已终止 - NEW：已创建 - NEW_SAVING：已创建保存中 - SUBMITTED：已提交 - ACCEPTED：已接受 - RUNNING：运行中 - FINISHED：已完成
        :type job_state: str
        :param job_result: 作业运行结果。 - FAILED：执行失败的作业。 - KILLED：执行中被手动终止的作业。 - UNDEFINED：正在执行的作业。 - SUCCEEDED：执行成功的作业。
        :type job_result: str
        :param queue: 作业的资源对列类型名称，作业的资源对列类型名称，只能由数字、字母和特殊字符(-_)组成, 并且长度为1～64字符。
        :type queue: str
        :param limit: 返回结果中每页显示条数。缺省值：10
        :type limit: str
        :param offset: 表示作业列表从该偏移量开始查询。缺省值：0
        :type offset: str
        :param sort_by: 返回结果的排序方式，默认值为desc。 - asc：按升序排列 - desc：按降序排列
        :type sort_by: str
        :param submitted_time_begin: 查询该时间之后提交的作业，UTC的毫秒时间戳。例如：1562032041362。
        :type submitted_time_begin: int
        :param submitted_time_end: 查询该时间之前提交的作业UTC的毫秒时间戳。例如：1562032041362。
        :type submitted_time_end: int
        """
        
        

        self._cluster_id = None
        self._job_name = None
        self._job_id = None
        self._user = None
        self._job_type = None
        self._job_state = None
        self._job_result = None
        self._queue = None
        self._limit = None
        self._offset = None
        self._sort_by = None
        self._submitted_time_begin = None
        self._submitted_time_end = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if job_name is not None:
            self.job_name = job_name
        if job_id is not None:
            self.job_id = job_id
        if user is not None:
            self.user = user
        if job_type is not None:
            self.job_type = job_type
        if job_state is not None:
            self.job_state = job_state
        if job_result is not None:
            self.job_result = job_result
        if queue is not None:
            self.queue = queue
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if submitted_time_begin is not None:
            self.submitted_time_begin = submitted_time_begin
        if submitted_time_end is not None:
            self.submitted_time_end = submitted_time_end

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowJobExeListNewRequest.

        集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :return: The cluster_id of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowJobExeListNewRequest.

        集群ID。获取方法，请参见[获取集群ID](https://support.huaweicloud.com/api-mrs/mrs_02_9001.html)。

        :param cluster_id: The cluster_id of this ShowJobExeListNewRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def job_name(self):
        """Gets the job_name of this ShowJobExeListNewRequest.

        作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～128个字符。

        :return: The job_name of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ShowJobExeListNewRequest.

        作业名称，只能由字母、数字、中划线和下划线组成，并且长度为1～128个字符。

        :param job_name: The job_name of this ShowJobExeListNewRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobExeListNewRequest.

        作业ID，只能由字母、数字、中划线(-)组成，并且长度为1~64字符。

        :return: The job_id of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobExeListNewRequest.

        作业ID，只能由字母、数字、中划线(-)组成，并且长度为1~64字符。

        :param job_id: The job_id of this ShowJobExeListNewRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def user(self):
        """Gets the user of this ShowJobExeListNewRequest.

        用户名称、只能由字母、数字、特殊字符(-_.)组成，且不能以数字开头，并且长度为1～32字符。

        :return: The user of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ShowJobExeListNewRequest.

        用户名称、只能由字母、数字、特殊字符(-_.)组成，且不能以数字开头，并且长度为1～32字符。

        :param user: The user of this ShowJobExeListNewRequest.
        :type user: str
        """
        self._user = user

    @property
    def job_type(self):
        """Gets the job_type of this ShowJobExeListNewRequest.

        作业类型。 - MapReduce - SparkPython - SparkSubmit：SparkPython类型的作业在查询时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink

        :return: The job_type of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowJobExeListNewRequest.

        作业类型。 - MapReduce - SparkPython - SparkSubmit：SparkPython类型的作业在查询时作业类型请选择SparkSubmit。 - HiveScript - HiveSql - DistCp，导入、导出数据。 - SparkScript - SparkSql - Flink

        :param job_type: The job_type of this ShowJobExeListNewRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_state(self):
        """Gets the job_state of this ShowJobExeListNewRequest.

        作业运行状态。 - FAILED：失败 - KILLED：已终止 - NEW：已创建 - NEW_SAVING：已创建保存中 - SUBMITTED：已提交 - ACCEPTED：已接受 - RUNNING：运行中 - FINISHED：已完成

        :return: The job_state of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this ShowJobExeListNewRequest.

        作业运行状态。 - FAILED：失败 - KILLED：已终止 - NEW：已创建 - NEW_SAVING：已创建保存中 - SUBMITTED：已提交 - ACCEPTED：已接受 - RUNNING：运行中 - FINISHED：已完成

        :param job_state: The job_state of this ShowJobExeListNewRequest.
        :type job_state: str
        """
        self._job_state = job_state

    @property
    def job_result(self):
        """Gets the job_result of this ShowJobExeListNewRequest.

        作业运行结果。 - FAILED：执行失败的作业。 - KILLED：执行中被手动终止的作业。 - UNDEFINED：正在执行的作业。 - SUCCEEDED：执行成功的作业。

        :return: The job_result of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._job_result

    @job_result.setter
    def job_result(self, job_result):
        """Sets the job_result of this ShowJobExeListNewRequest.

        作业运行结果。 - FAILED：执行失败的作业。 - KILLED：执行中被手动终止的作业。 - UNDEFINED：正在执行的作业。 - SUCCEEDED：执行成功的作业。

        :param job_result: The job_result of this ShowJobExeListNewRequest.
        :type job_result: str
        """
        self._job_result = job_result

    @property
    def queue(self):
        """Gets the queue of this ShowJobExeListNewRequest.

        作业的资源对列类型名称，作业的资源对列类型名称，只能由数字、字母和特殊字符(-_)组成, 并且长度为1～64字符。

        :return: The queue of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        """Sets the queue of this ShowJobExeListNewRequest.

        作业的资源对列类型名称，作业的资源对列类型名称，只能由数字、字母和特殊字符(-_)组成, 并且长度为1～64字符。

        :param queue: The queue of this ShowJobExeListNewRequest.
        :type queue: str
        """
        self._queue = queue

    @property
    def limit(self):
        """Gets the limit of this ShowJobExeListNewRequest.

        返回结果中每页显示条数。缺省值：10

        :return: The limit of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowJobExeListNewRequest.

        返回结果中每页显示条数。缺省值：10

        :param limit: The limit of this ShowJobExeListNewRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowJobExeListNewRequest.

        表示作业列表从该偏移量开始查询。缺省值：0

        :return: The offset of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowJobExeListNewRequest.

        表示作业列表从该偏移量开始查询。缺省值：0

        :param offset: The offset of this ShowJobExeListNewRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def sort_by(self):
        """Gets the sort_by of this ShowJobExeListNewRequest.

        返回结果的排序方式，默认值为desc。 - asc：按升序排列 - desc：按降序排列

        :return: The sort_by of this ShowJobExeListNewRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ShowJobExeListNewRequest.

        返回结果的排序方式，默认值为desc。 - asc：按升序排列 - desc：按降序排列

        :param sort_by: The sort_by of this ShowJobExeListNewRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def submitted_time_begin(self):
        """Gets the submitted_time_begin of this ShowJobExeListNewRequest.

        查询该时间之后提交的作业，UTC的毫秒时间戳。例如：1562032041362。

        :return: The submitted_time_begin of this ShowJobExeListNewRequest.
        :rtype: int
        """
        return self._submitted_time_begin

    @submitted_time_begin.setter
    def submitted_time_begin(self, submitted_time_begin):
        """Sets the submitted_time_begin of this ShowJobExeListNewRequest.

        查询该时间之后提交的作业，UTC的毫秒时间戳。例如：1562032041362。

        :param submitted_time_begin: The submitted_time_begin of this ShowJobExeListNewRequest.
        :type submitted_time_begin: int
        """
        self._submitted_time_begin = submitted_time_begin

    @property
    def submitted_time_end(self):
        """Gets the submitted_time_end of this ShowJobExeListNewRequest.

        查询该时间之前提交的作业UTC的毫秒时间戳。例如：1562032041362。

        :return: The submitted_time_end of this ShowJobExeListNewRequest.
        :rtype: int
        """
        return self._submitted_time_end

    @submitted_time_end.setter
    def submitted_time_end(self, submitted_time_end):
        """Sets the submitted_time_end of this ShowJobExeListNewRequest.

        查询该时间之前提交的作业UTC的毫秒时间戳。例如：1562032041362。

        :param submitted_time_end: The submitted_time_end of this ShowJobExeListNewRequest.
        :type submitted_time_end: int
        """
        self._submitted_time_end = submitted_time_end

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
        if not isinstance(other, ShowJobExeListNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
