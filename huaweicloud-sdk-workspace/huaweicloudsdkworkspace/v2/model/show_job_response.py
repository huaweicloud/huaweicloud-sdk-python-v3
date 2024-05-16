# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'job_type': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'status': 'str',
        'job_error_code': 'str',
        'fail_reason': 'str',
        'sub_jobs_total': 'int',
        'sub_jobs': 'list[JobDetailInfo]'
    }

    attribute_map = {
        'id': 'id',
        'job_type': 'job_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'job_error_code': 'job_error_code',
        'fail_reason': 'fail_reason',
        'sub_jobs_total': 'sub_jobs_total',
        'sub_jobs': 'sub_jobs'
    }

    def __init__(self, id=None, job_type=None, begin_time=None, end_time=None, status=None, job_error_code=None, fail_reason=None, sub_jobs_total=None, sub_jobs=None):
        """ShowJobResponse

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param job_type: 任务类型
        :type job_type: str
        :param begin_time: 任务开始时间
        :type begin_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param status: 任务状态
        :type status: str
        :param job_error_code: 任务错误码
        :type job_error_code: str
        :param fail_reason: 任务失败原因
        :type fail_reason: str
        :param sub_jobs_total: 子任务总数
        :type sub_jobs_total: int
        :param sub_jobs: 子任务列表
        :type sub_jobs: list[:class:`huaweicloudsdkworkspace.v2.JobDetailInfo`]
        """
        
        super(ShowJobResponse, self).__init__()

        self._id = None
        self._job_type = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._job_error_code = None
        self._fail_reason = None
        self._sub_jobs_total = None
        self._sub_jobs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_type is not None:
            self.job_type = job_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if job_error_code is not None:
            self.job_error_code = job_error_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if sub_jobs_total is not None:
            self.sub_jobs_total = sub_jobs_total
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs

    @property
    def id(self):
        """Gets the id of this ShowJobResponse.

        任务ID

        :return: The id of this ShowJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowJobResponse.

        任务ID

        :param id: The id of this ShowJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def job_type(self):
        """Gets the job_type of this ShowJobResponse.

        任务类型

        :return: The job_type of this ShowJobResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowJobResponse.

        任务类型

        :param job_type: The job_type of this ShowJobResponse.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowJobResponse.

        任务开始时间

        :return: The begin_time of this ShowJobResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowJobResponse.

        任务开始时间

        :param begin_time: The begin_time of this ShowJobResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobResponse.

        任务结束时间

        :return: The end_time of this ShowJobResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobResponse.

        任务结束时间

        :param end_time: The end_time of this ShowJobResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this ShowJobResponse.

        任务状态

        :return: The status of this ShowJobResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobResponse.

        任务状态

        :param status: The status of this ShowJobResponse.
        :type status: str
        """
        self._status = status

    @property
    def job_error_code(self):
        """Gets the job_error_code of this ShowJobResponse.

        任务错误码

        :return: The job_error_code of this ShowJobResponse.
        :rtype: str
        """
        return self._job_error_code

    @job_error_code.setter
    def job_error_code(self, job_error_code):
        """Sets the job_error_code of this ShowJobResponse.

        任务错误码

        :param job_error_code: The job_error_code of this ShowJobResponse.
        :type job_error_code: str
        """
        self._job_error_code = job_error_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowJobResponse.

        任务失败原因

        :return: The fail_reason of this ShowJobResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowJobResponse.

        任务失败原因

        :param fail_reason: The fail_reason of this ShowJobResponse.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

    @property
    def sub_jobs_total(self):
        """Gets the sub_jobs_total of this ShowJobResponse.

        子任务总数

        :return: The sub_jobs_total of this ShowJobResponse.
        :rtype: int
        """
        return self._sub_jobs_total

    @sub_jobs_total.setter
    def sub_jobs_total(self, sub_jobs_total):
        """Sets the sub_jobs_total of this ShowJobResponse.

        子任务总数

        :param sub_jobs_total: The sub_jobs_total of this ShowJobResponse.
        :type sub_jobs_total: int
        """
        self._sub_jobs_total = sub_jobs_total

    @property
    def sub_jobs(self):
        """Gets the sub_jobs of this ShowJobResponse.

        子任务列表

        :return: The sub_jobs of this ShowJobResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.JobDetailInfo`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        """Sets the sub_jobs of this ShowJobResponse.

        子任务列表

        :param sub_jobs: The sub_jobs of this ShowJobResponse.
        :type sub_jobs: list[:class:`huaweicloudsdkworkspace.v2.JobDetailInfo`]
        """
        self._sub_jobs = sub_jobs

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
        if not isinstance(other, ShowJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
