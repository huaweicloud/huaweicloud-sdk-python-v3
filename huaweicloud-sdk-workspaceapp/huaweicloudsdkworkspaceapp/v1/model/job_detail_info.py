# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobDetailInfo:

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
        'job_type': 'JobType',
        'job_resource_info': 'JobResourceInfo',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'status': 'JobDetailStatus',
        'error_code': 'str',
        'error_message': 'str',
        'project_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_type': 'job_type',
        'job_resource_info': 'job_resource_info',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'status': 'status',
        'error_code': 'error_code',
        'error_message': 'error_message',
        'project_id': 'project_id',
        'job_id': 'job_id'
    }

    def __init__(self, id=None, job_type=None, job_resource_info=None, begin_time=None, end_time=None, status=None, error_code=None, error_message=None, project_id=None, job_id=None):
        """JobDetailInfo

        The model defined in huaweicloud sdk

        :param id: 子任务ID。
        :type id: str
        :param job_type: 
        :type job_type: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        :param job_resource_info: 
        :type job_resource_info: :class:`huaweicloudsdkworkspaceapp.v1.JobResourceInfo`
        :param begin_time: 任务创建时间。
        :type begin_time: datetime
        :param end_time: 任务结束时间。
        :type end_time: datetime
        :param status: 
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.JobDetailStatus`
        :param error_code: 任务执行失败时的错误码。
        :type error_code: str
        :param error_message: 任务失败原因。
        :type error_message: str
        :param project_id: 项目ID。
        :type project_id: str
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        

        self._id = None
        self._job_type = None
        self._job_resource_info = None
        self._begin_time = None
        self._end_time = None
        self._status = None
        self._error_code = None
        self._error_message = None
        self._project_id = None
        self._job_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_type is not None:
            self.job_type = job_type
        if job_resource_info is not None:
            self.job_resource_info = job_resource_info
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if project_id is not None:
            self.project_id = project_id
        if job_id is not None:
            self.job_id = job_id

    @property
    def id(self):
        """Gets the id of this JobDetailInfo.

        子任务ID。

        :return: The id of this JobDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobDetailInfo.

        子任务ID。

        :param id: The id of this JobDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def job_type(self):
        """Gets the job_type of this JobDetailInfo.

        :return: The job_type of this JobDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobDetailInfo.

        :param job_type: The job_type of this JobDetailInfo.
        :type job_type: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        """
        self._job_type = job_type

    @property
    def job_resource_info(self):
        """Gets the job_resource_info of this JobDetailInfo.

        :return: The job_resource_info of this JobDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobResourceInfo`
        """
        return self._job_resource_info

    @job_resource_info.setter
    def job_resource_info(self, job_resource_info):
        """Sets the job_resource_info of this JobDetailInfo.

        :param job_resource_info: The job_resource_info of this JobDetailInfo.
        :type job_resource_info: :class:`huaweicloudsdkworkspaceapp.v1.JobResourceInfo`
        """
        self._job_resource_info = job_resource_info

    @property
    def begin_time(self):
        """Gets the begin_time of this JobDetailInfo.

        任务创建时间。

        :return: The begin_time of this JobDetailInfo.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this JobDetailInfo.

        任务创建时间。

        :param begin_time: The begin_time of this JobDetailInfo.
        :type begin_time: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this JobDetailInfo.

        任务结束时间。

        :return: The end_time of this JobDetailInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this JobDetailInfo.

        任务结束时间。

        :param end_time: The end_time of this JobDetailInfo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def status(self):
        """Gets the status of this JobDetailInfo.

        :return: The status of this JobDetailInfo.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobDetailStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobDetailInfo.

        :param status: The status of this JobDetailInfo.
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.JobDetailStatus`
        """
        self._status = status

    @property
    def error_code(self):
        """Gets the error_code of this JobDetailInfo.

        任务执行失败时的错误码。

        :return: The error_code of this JobDetailInfo.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this JobDetailInfo.

        任务执行失败时的错误码。

        :param error_code: The error_code of this JobDetailInfo.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this JobDetailInfo.

        任务失败原因。

        :return: The error_message of this JobDetailInfo.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this JobDetailInfo.

        任务失败原因。

        :param error_message: The error_message of this JobDetailInfo.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def project_id(self):
        """Gets the project_id of this JobDetailInfo.

        项目ID。

        :return: The project_id of this JobDetailInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this JobDetailInfo.

        项目ID。

        :param project_id: The project_id of this JobDetailInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def job_id(self):
        """Gets the job_id of this JobDetailInfo.

        任务ID。

        :return: The job_id of this JobDetailInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobDetailInfo.

        任务ID。

        :param job_id: The job_id of this JobDetailInfo.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, JobDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
