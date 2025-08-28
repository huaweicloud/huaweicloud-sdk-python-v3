# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MainJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'job_id': 'str',
        'job_type': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'project_id': 'str',
        'resource_id': 'str',
        'sub_jobs': 'list[SubJob]'
    }

    attribute_map = {
        'status': 'status',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'project_id': 'project_id',
        'resource_id': 'resource_id',
        'sub_jobs': 'sub_jobs'
    }

    def __init__(self, status=None, begin_time=None, end_time=None, job_id=None, job_type=None, error_code=None, error_msg=None, project_id=None, resource_id=None, sub_jobs=None):
        r"""MainJob

        The model defined in huaweicloud sdk

        :param status: 任务状态
        :type status: str
        :param begin_time: 任务开始时间
        :type begin_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param job_id: 任务ID
        :type job_id: str
        :param job_type: 任务类型
        :type job_type: str
        :param error_code: 任务的错误码
        :type error_code: str
        :param error_msg: 任务的错误信息
        :type error_msg: str
        :param project_id: 项目ID
        :type project_id: str
        :param resource_id: **参数解释**：资源ID。
        :type resource_id: str
        :param sub_jobs: **参数解释**：子任务列表。
        :type sub_jobs: list[:class:`huaweicloudsdkelb.v3.SubJob`]
        """
        
        

        self._status = None
        self._begin_time = None
        self._end_time = None
        self._job_id = None
        self._job_type = None
        self._error_code = None
        self._error_msg = None
        self._project_id = None
        self._resource_id = None
        self._sub_jobs = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if project_id is not None:
            self.project_id = project_id
        if resource_id is not None:
            self.resource_id = resource_id
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs

    @property
    def status(self):
        r"""Gets the status of this MainJob.

        任务状态

        :return: The status of this MainJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MainJob.

        任务状态

        :param status: The status of this MainJob.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this MainJob.

        任务开始时间

        :return: The begin_time of this MainJob.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this MainJob.

        任务开始时间

        :param begin_time: The begin_time of this MainJob.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this MainJob.

        任务结束时间

        :return: The end_time of this MainJob.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this MainJob.

        任务结束时间

        :param end_time: The end_time of this MainJob.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def job_id(self):
        r"""Gets the job_id of this MainJob.

        任务ID

        :return: The job_id of this MainJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this MainJob.

        任务ID

        :param job_id: The job_id of this MainJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        r"""Gets the job_type of this MainJob.

        任务类型

        :return: The job_type of this MainJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this MainJob.

        任务类型

        :param job_type: The job_type of this MainJob.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def error_code(self):
        r"""Gets the error_code of this MainJob.

        任务的错误码

        :return: The error_code of this MainJob.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this MainJob.

        任务的错误码

        :param error_code: The error_code of this MainJob.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this MainJob.

        任务的错误信息

        :return: The error_msg of this MainJob.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this MainJob.

        任务的错误信息

        :param error_msg: The error_msg of this MainJob.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def project_id(self):
        r"""Gets the project_id of this MainJob.

        项目ID

        :return: The project_id of this MainJob.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this MainJob.

        项目ID

        :param project_id: The project_id of this MainJob.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this MainJob.

        **参数解释**：资源ID。

        :return: The resource_id of this MainJob.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this MainJob.

        **参数解释**：资源ID。

        :param resource_id: The resource_id of this MainJob.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def sub_jobs(self):
        r"""Gets the sub_jobs of this MainJob.

        **参数解释**：子任务列表。

        :return: The sub_jobs of this MainJob.
        :rtype: list[:class:`huaweicloudsdkelb.v3.SubJob`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        r"""Sets the sub_jobs of this MainJob.

        **参数解释**：子任务列表。

        :param sub_jobs: The sub_jobs of this MainJob.
        :type sub_jobs: list[:class:`huaweicloudsdkelb.v3.SubJob`]
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
        if not isinstance(other, MainJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
