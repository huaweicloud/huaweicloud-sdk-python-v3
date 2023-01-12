# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRespJobList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'status': 'str',
        'job_type': 'str',
        'job_name': 'str',
        'related_graph': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'job_detail': 'ShowJobRespJobDetail',
        'fail_reason': 'str',
        'job_progress': 'float'
    }

    attribute_map = {
        'job_id': 'job_id',
        'status': 'status',
        'job_type': 'job_type',
        'job_name': 'job_name',
        'related_graph': 'related_graph',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'job_detail': 'job_detail',
        'fail_reason': 'fail_reason',
        'job_progress': 'job_progress'
    }

    def __init__(self, job_id=None, status=None, job_type=None, job_name=None, related_graph=None, begin_time=None, end_time=None, job_detail=None, fail_reason=None, job_progress=None):
        """ListJobsRespJobList

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param status: 任务状态。  - pending:等待中 - running:运行中 - success:成功 - failed:失败
        :type status: str
        :param job_type: 任务类型。
        :type job_type: str
        :param job_name: 任务名称。
        :type job_name: str
        :param related_graph: 关联图名称。
        :type related_graph: str
        :param begin_time: 任务开始时间，格式为UTC,\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;。
        :type begin_time: str
        :param end_time: 任务结束时间，格式为UTC,\&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;。
        :type end_time: str
        :param job_detail: 
        :type job_detail: :class:`huaweicloudsdkges.v2.ShowJobRespJobDetail`
        :param fail_reason: 任务失败原因。
        :type fail_reason: str
        :param job_progress: 任务执行进度，预留字段，暂未使用。
        :type job_progress: float
        """
        
        

        self._job_id = None
        self._status = None
        self._job_type = None
        self._job_name = None
        self._related_graph = None
        self._begin_time = None
        self._end_time = None
        self._job_detail = None
        self._fail_reason = None
        self._job_progress = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if job_type is not None:
            self.job_type = job_type
        if job_name is not None:
            self.job_name = job_name
        if related_graph is not None:
            self.related_graph = related_graph
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if job_detail is not None:
            self.job_detail = job_detail
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if job_progress is not None:
            self.job_progress = job_progress

    @property
    def job_id(self):
        """Gets the job_id of this ListJobsRespJobList.

        任务ID。

        :return: The job_id of this ListJobsRespJobList.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListJobsRespJobList.

        任务ID。

        :param job_id: The job_id of this ListJobsRespJobList.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this ListJobsRespJobList.

        任务状态。  - pending:等待中 - running:运行中 - success:成功 - failed:失败

        :return: The status of this ListJobsRespJobList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListJobsRespJobList.

        任务状态。  - pending:等待中 - running:运行中 - success:成功 - failed:失败

        :param status: The status of this ListJobsRespJobList.
        :type status: str
        """
        self._status = status

    @property
    def job_type(self):
        """Gets the job_type of this ListJobsRespJobList.

        任务类型。

        :return: The job_type of this ListJobsRespJobList.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ListJobsRespJobList.

        任务类型。

        :param job_type: The job_type of this ListJobsRespJobList.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_name(self):
        """Gets the job_name of this ListJobsRespJobList.

        任务名称。

        :return: The job_name of this ListJobsRespJobList.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this ListJobsRespJobList.

        任务名称。

        :param job_name: The job_name of this ListJobsRespJobList.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def related_graph(self):
        """Gets the related_graph of this ListJobsRespJobList.

        关联图名称。

        :return: The related_graph of this ListJobsRespJobList.
        :rtype: str
        """
        return self._related_graph

    @related_graph.setter
    def related_graph(self, related_graph):
        """Sets the related_graph of this ListJobsRespJobList.

        关联图名称。

        :param related_graph: The related_graph of this ListJobsRespJobList.
        :type related_graph: str
        """
        self._related_graph = related_graph

    @property
    def begin_time(self):
        """Gets the begin_time of this ListJobsRespJobList.

        任务开始时间，格式为UTC,\"yyyy-MM-dd'T'HH:mm:ss\"。

        :return: The begin_time of this ListJobsRespJobList.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListJobsRespJobList.

        任务开始时间，格式为UTC,\"yyyy-MM-dd'T'HH:mm:ss\"。

        :param begin_time: The begin_time of this ListJobsRespJobList.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListJobsRespJobList.

        任务结束时间，格式为UTC,\"yyyy-MM-dd'T'HH:mm:ss\"。

        :return: The end_time of this ListJobsRespJobList.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListJobsRespJobList.

        任务结束时间，格式为UTC,\"yyyy-MM-dd'T'HH:mm:ss\"。

        :param end_time: The end_time of this ListJobsRespJobList.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def job_detail(self):
        """Gets the job_detail of this ListJobsRespJobList.

        :return: The job_detail of this ListJobsRespJobList.
        :rtype: :class:`huaweicloudsdkges.v2.ShowJobRespJobDetail`
        """
        return self._job_detail

    @job_detail.setter
    def job_detail(self, job_detail):
        """Sets the job_detail of this ListJobsRespJobList.

        :param job_detail: The job_detail of this ListJobsRespJobList.
        :type job_detail: :class:`huaweicloudsdkges.v2.ShowJobRespJobDetail`
        """
        self._job_detail = job_detail

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ListJobsRespJobList.

        任务失败原因。

        :return: The fail_reason of this ListJobsRespJobList.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ListJobsRespJobList.

        任务失败原因。

        :param fail_reason: The fail_reason of this ListJobsRespJobList.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def job_progress(self):
        """Gets the job_progress of this ListJobsRespJobList.

        任务执行进度，预留字段，暂未使用。

        :return: The job_progress of this ListJobsRespJobList.
        :rtype: float
        """
        return self._job_progress

    @job_progress.setter
    def job_progress(self, job_progress):
        """Sets the job_progress of this ListJobsRespJobList.

        任务执行进度，预留字段，暂未使用。

        :param job_progress: The job_progress of this ListJobsRespJobList.
        :type job_progress: float
        """
        self._job_progress = job_progress

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
        if not isinstance(other, ListJobsRespJobList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
