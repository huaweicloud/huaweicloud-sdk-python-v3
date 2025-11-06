# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Job:

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
        'resource_id': 'str',
        'job_type': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'finished_at': 'datetime',
        'error_message': 'str',
        'sub_jobs': 'list[SubJob]'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'job_type': 'job_type',
        'status': 'status',
        'created_at': 'created_at',
        'finished_at': 'finished_at',
        'error_message': 'error_message',
        'sub_jobs': 'sub_jobs'
    }

    def __init__(self, id=None, resource_id=None, job_type=None, status=None, created_at=None, finished_at=None, error_message=None, sub_jobs=None):
        r"""Job

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: str
        :param resource_id: 资源Id
        :type resource_id: str
        :param job_type: 任务类型
        :type job_type: str
        :param status: 任务状态
        :type status: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param finished_at: 完成时间
        :type finished_at: datetime
        :param error_message: 错误信息
        :type error_message: str
        :param sub_jobs: 子任务列表
        :type sub_jobs: list[:class:`huaweicloudsdkvpn.v5.SubJob`]
        """
        
        

        self._id = None
        self._resource_id = None
        self._job_type = None
        self._status = None
        self._created_at = None
        self._finished_at = None
        self._error_message = None
        self._sub_jobs = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if resource_id is not None:
            self.resource_id = resource_id
        if job_type is not None:
            self.job_type = job_type
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if finished_at is not None:
            self.finished_at = finished_at
        if error_message is not None:
            self.error_message = error_message
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs

    @property
    def id(self):
        r"""Gets the id of this Job.

        任务ID

        :return: The id of this Job.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Job.

        任务ID

        :param id: The id of this Job.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        r"""Gets the resource_id of this Job.

        资源Id

        :return: The resource_id of this Job.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this Job.

        资源Id

        :param resource_id: The resource_id of this Job.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def job_type(self):
        r"""Gets the job_type of this Job.

        任务类型

        :return: The job_type of this Job.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this Job.

        任务类型

        :param job_type: The job_type of this Job.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def status(self):
        r"""Gets the status of this Job.

        任务状态

        :return: The status of this Job.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Job.

        任务状态

        :param status: The status of this Job.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this Job.

        创建时间

        :return: The created_at of this Job.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Job.

        创建时间

        :param created_at: The created_at of this Job.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def finished_at(self):
        r"""Gets the finished_at of this Job.

        完成时间

        :return: The finished_at of this Job.
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        r"""Sets the finished_at of this Job.

        完成时间

        :param finished_at: The finished_at of this Job.
        :type finished_at: datetime
        """
        self._finished_at = finished_at

    @property
    def error_message(self):
        r"""Gets the error_message of this Job.

        错误信息

        :return: The error_message of this Job.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this Job.

        错误信息

        :param error_message: The error_message of this Job.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def sub_jobs(self):
        r"""Gets the sub_jobs of this Job.

        子任务列表

        :return: The sub_jobs of this Job.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.SubJob`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        r"""Sets the sub_jobs of this Job.

        子任务列表

        :param sub_jobs: The sub_jobs of this Job.
        :type sub_jobs: list[:class:`huaweicloudsdkvpn.v5.SubJob`]
        """
        self._sub_jobs = sub_jobs

    def to_dict(self):
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
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
