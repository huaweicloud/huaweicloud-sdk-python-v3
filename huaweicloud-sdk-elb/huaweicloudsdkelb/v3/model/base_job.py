# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseJob:

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
        'resource_id': 'str'
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
        'resource_id': 'resource_id'
    }

    def __init__(self, status=None, begin_time=None, end_time=None, job_id=None, job_type=None, error_code=None, error_msg=None, project_id=None, resource_id=None):
        """BaseJob

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
        :param resource_id: 参数解释：资源ID。
        :type resource_id: str
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

    @property
    def status(self):
        """Gets the status of this BaseJob.

        任务状态

        :return: The status of this BaseJob.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BaseJob.

        任务状态

        :param status: The status of this BaseJob.
        :type status: str
        """
        self._status = status

    @property
    def begin_time(self):
        """Gets the begin_time of this BaseJob.

        任务开始时间

        :return: The begin_time of this BaseJob.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this BaseJob.

        任务开始时间

        :param begin_time: The begin_time of this BaseJob.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this BaseJob.

        任务结束时间

        :return: The end_time of this BaseJob.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this BaseJob.

        任务结束时间

        :param end_time: The end_time of this BaseJob.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def job_id(self):
        """Gets the job_id of this BaseJob.

        任务ID

        :return: The job_id of this BaseJob.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BaseJob.

        任务ID

        :param job_id: The job_id of this BaseJob.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this BaseJob.

        任务类型

        :return: The job_type of this BaseJob.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this BaseJob.

        任务类型

        :param job_type: The job_type of this BaseJob.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def error_code(self):
        """Gets the error_code of this BaseJob.

        任务的错误码

        :return: The error_code of this BaseJob.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this BaseJob.

        任务的错误码

        :param error_code: The error_code of this BaseJob.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        """Gets the error_msg of this BaseJob.

        任务的错误信息

        :return: The error_msg of this BaseJob.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        """Sets the error_msg of this BaseJob.

        任务的错误信息

        :param error_msg: The error_msg of this BaseJob.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def project_id(self):
        """Gets the project_id of this BaseJob.

        项目ID

        :return: The project_id of this BaseJob.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BaseJob.

        项目ID

        :param project_id: The project_id of this BaseJob.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_id(self):
        """Gets the resource_id of this BaseJob.

        参数解释：资源ID。

        :return: The resource_id of this BaseJob.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BaseJob.

        参数解释：资源ID。

        :param resource_id: The resource_id of this BaseJob.
        :type resource_id: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, BaseJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
