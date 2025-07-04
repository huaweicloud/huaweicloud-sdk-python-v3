# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSparkJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'end': 'int',
        '_from': 'int',
        'job_name': 'str',
        'job_id': 'str',
        'order': 'str',
        'queue_name': 'str',
        'size': 'int',
        'start': 'int',
        'state': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'end': 'end',
        '_from': 'from',
        'job_name': 'job_name',
        'job_id': 'job-id',
        'order': 'order',
        'queue_name': 'queue_name',
        'size': 'size',
        'start': 'start',
        'state': 'state'
    }

    def __init__(self, cluster_name=None, end=None, _from=None, job_name=None, job_id=None, order=None, queue_name=None, size=None, start=None, state=None):
        r"""ListSparkJobsRequest

        The model defined in huaweicloud sdk

        :param cluster_name: 参数解释:   DLI队列名称，不填写则获取当前Project下所有批处理作业(不推荐使用) 示例: cluster1 约束限制:  匹配正则表达式&#39;^(?!_)(?![0-9]+$)[A-Za-z0-9_]*$&#39;的字符串 取值范围: 无 默认取值: 无
        :type cluster_name: str
        :param end: 参数解释:   用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒 示例: 156789546456 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type end: int
        :param _from: 参数解释:   起始批处理作业的索引号，默认从0开始 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type _from: int
        :param job_name: 参数解释:   批处理作业的名称 示例: dli_test 约束限制:  无 取值范围: 无 默认取值: 无
        :type job_name: str
        :param job_id: 参数解释:   批处理作业的ID 示例: 03923a72-5ace-466a-a573-e8c7b08b8cf3 约束限制:  匹配正则表达式&#39;^[A-Fa-f0-9_-]*$&#39;的字符串 取值范围: 无 默认取值: 无
        :type job_id: str
        :param order: 参数解释:   指定作业排序方式 示例: DURATION_DESC 约束限制:  无 取值范围: DURATION_DESC（作业运行时长降序） DURATION_ASC（作业运行时长升序） CREATE_TIME_DESC（作业提交时间降序） CREATE_TIME_ASC（作业提交时间升序） 默认取值: 无
        :type order: str
        :param queue_name: 参数解释:   队列名称 示例: 03923a72-5ace-466a-a573-e8c7b08b8cf3 约束限制:  匹配正则表达式&#39;^[A-Fa-f0-9_-]*$&#39;的字符串 取值范围: 无 默认取值: 无
        :type queue_name: str
        :param size: 参数解释:   查询批处理作业的数量 示例: 1 约束限制:  无 取值范围: 无 默认取值: 100
        :type size: int
        :param start: 参数解释:   用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒 示例: 156456784655 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无
        :type start: int
        :param state: 参数解释:   批处理作业的状态 示例: success 约束限制:  无 取值范围: starting（批处理作业正在启动） running（批处理作业正在执行任务） dead（批处理作业已退出） success（批处理作业执行成功） recovering（批处理作业正在恢复） 默认取值: 无
        :type state: str
        """
        
        

        self._cluster_name = None
        self._end = None
        self.__from = None
        self._job_name = None
        self._job_id = None
        self._order = None
        self._queue_name = None
        self._size = None
        self._start = None
        self._state = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name
        if end is not None:
            self.end = end
        if _from is not None:
            self._from = _from
        if job_name is not None:
            self.job_name = job_name
        if job_id is not None:
            self.job_id = job_id
        if order is not None:
            self.order = order
        if queue_name is not None:
            self.queue_name = queue_name
        if size is not None:
            self.size = size
        if start is not None:
            self.start = start
        if state is not None:
            self.state = state

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListSparkJobsRequest.

        参数解释:   DLI队列名称，不填写则获取当前Project下所有批处理作业(不推荐使用) 示例: cluster1 约束限制:  匹配正则表达式'^(?!_)(?![0-9]+$)[A-Za-z0-9_]*$'的字符串 取值范围: 无 默认取值: 无

        :return: The cluster_name of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListSparkJobsRequest.

        参数解释:   DLI队列名称，不填写则获取当前Project下所有批处理作业(不推荐使用) 示例: cluster1 约束限制:  匹配正则表达式'^(?!_)(?![0-9]+$)[A-Za-z0-9_]*$'的字符串 取值范围: 无 默认取值: 无

        :param cluster_name: The cluster_name of this ListSparkJobsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def end(self):
        r"""Gets the end of this ListSparkJobsRequest.

        参数解释:   用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒 示例: 156789546456 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The end of this ListSparkJobsRequest.
        :rtype: int
        """
        return self._end

    @end.setter
    def end(self, end):
        r"""Sets the end of this ListSparkJobsRequest.

        参数解释:   用于查询开始时间在该时间点之前的作业。时间格式为unix时间戳，单位：毫秒 示例: 156789546456 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param end: The end of this ListSparkJobsRequest.
        :type end: int
        """
        self._end = end

    @property
    def _from(self):
        r"""Gets the _from of this ListSparkJobsRequest.

        参数解释:   起始批处理作业的索引号，默认从0开始 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The _from of this ListSparkJobsRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListSparkJobsRequest.

        参数解释:   起始批处理作业的索引号，默认从0开始 示例: 0 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param _from: The _from of this ListSparkJobsRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def job_name(self):
        r"""Gets the job_name of this ListSparkJobsRequest.

        参数解释:   批处理作业的名称 示例: dli_test 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The job_name of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListSparkJobsRequest.

        参数解释:   批处理作业的名称 示例: dli_test 约束限制:  无 取值范围: 无 默认取值: 无

        :param job_name: The job_name of this ListSparkJobsRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_id(self):
        r"""Gets the job_id of this ListSparkJobsRequest.

        参数解释:   批处理作业的ID 示例: 03923a72-5ace-466a-a573-e8c7b08b8cf3 约束限制:  匹配正则表达式'^[A-Fa-f0-9_-]*$'的字符串 取值范围: 无 默认取值: 无

        :return: The job_id of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListSparkJobsRequest.

        参数解释:   批处理作业的ID 示例: 03923a72-5ace-466a-a573-e8c7b08b8cf3 约束限制:  匹配正则表达式'^[A-Fa-f0-9_-]*$'的字符串 取值范围: 无 默认取值: 无

        :param job_id: The job_id of this ListSparkJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def order(self):
        r"""Gets the order of this ListSparkJobsRequest.

        参数解释:   指定作业排序方式 示例: DURATION_DESC 约束限制:  无 取值范围: DURATION_DESC（作业运行时长降序） DURATION_ASC（作业运行时长升序） CREATE_TIME_DESC（作业提交时间降序） CREATE_TIME_ASC（作业提交时间升序） 默认取值: 无

        :return: The order of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListSparkJobsRequest.

        参数解释:   指定作业排序方式 示例: DURATION_DESC 约束限制:  无 取值范围: DURATION_DESC（作业运行时长降序） DURATION_ASC（作业运行时长升序） CREATE_TIME_DESC（作业提交时间降序） CREATE_TIME_ASC（作业提交时间升序） 默认取值: 无

        :param order: The order of this ListSparkJobsRequest.
        :type order: str
        """
        self._order = order

    @property
    def queue_name(self):
        r"""Gets the queue_name of this ListSparkJobsRequest.

        参数解释:   队列名称 示例: 03923a72-5ace-466a-a573-e8c7b08b8cf3 约束限制:  匹配正则表达式'^[A-Fa-f0-9_-]*$'的字符串 取值范围: 无 默认取值: 无

        :return: The queue_name of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this ListSparkJobsRequest.

        参数解释:   队列名称 示例: 03923a72-5ace-466a-a573-e8c7b08b8cf3 约束限制:  匹配正则表达式'^[A-Fa-f0-9_-]*$'的字符串 取值范围: 无 默认取值: 无

        :param queue_name: The queue_name of this ListSparkJobsRequest.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def size(self):
        r"""Gets the size of this ListSparkJobsRequest.

        参数解释:   查询批处理作业的数量 示例: 1 约束限制:  无 取值范围: 无 默认取值: 100

        :return: The size of this ListSparkJobsRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListSparkJobsRequest.

        参数解释:   查询批处理作业的数量 示例: 1 约束限制:  无 取值范围: 无 默认取值: 100

        :param size: The size of this ListSparkJobsRequest.
        :type size: int
        """
        self._size = size

    @property
    def start(self):
        r"""Gets the start of this ListSparkJobsRequest.

        参数解释:   用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒 示例: 156456784655 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :return: The start of this ListSparkJobsRequest.
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this ListSparkJobsRequest.

        参数解释:   用于查询开始时间在该时间点之后的作业。时间格式为unix时间戳，单位：毫秒 示例: 156456784655 约束限制:  无 取值范围: 大于等于0的整数 默认取值: 无

        :param start: The start of this ListSparkJobsRequest.
        :type start: int
        """
        self._start = start

    @property
    def state(self):
        r"""Gets the state of this ListSparkJobsRequest.

        参数解释:   批处理作业的状态 示例: success 约束限制:  无 取值范围: starting（批处理作业正在启动） running（批处理作业正在执行任务） dead（批处理作业已退出） success（批处理作业执行成功） recovering（批处理作业正在恢复） 默认取值: 无

        :return: The state of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListSparkJobsRequest.

        参数解释:   批处理作业的状态 示例: success 约束限制:  无 取值范围: starting（批处理作业正在启动） running（批处理作业正在执行任务） dead（批处理作业已退出） success（批处理作业执行成功） recovering（批处理作业正在恢复） 默认取值: 无

        :param state: The state of this ListSparkJobsRequest.
        :type state: str
        """
        self._state = state

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
        if not isinstance(other, ListSparkJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
