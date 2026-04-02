# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GcTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'job_name': 'str',
        'job_kind': 'str',
        'job_parameters': 'JobParameters',
        'job_status': 'str',
        'creation_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_name': 'job_name',
        'job_kind': 'job_kind',
        'job_parameters': 'job_parameters',
        'job_status': 'job_status',
        'creation_time': 'creation_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, job_name=None, job_kind=None, job_parameters=None, job_status=None, creation_time=None, update_time=None):
        r"""GcTask

        The model defined in huaweicloud sdk

        :param id: gc任务的ID。
        :type id: int
        :param job_name: gc任务的名称。
        :type job_name: str
        :param job_kind: 任务类型，MANUAL：手动执行，SCHEDULE：定时执行。
        :type job_kind: str
        :param job_parameters: 
        :type job_parameters: :class:`huaweicloudsdkswr.v2.JobParameters`
        :param job_status: gc任务的状态，Success：已完成，Stopped：已停止，Running：清理中，Pending：排队中，Error：失败。
        :type job_status: str
        :param creation_time: gc任务的创建时间。
        :type creation_time: str
        :param update_time: gc任务的更新时间。
        :type update_time: str
        """
        
        

        self._id = None
        self._job_name = None
        self._job_kind = None
        self._job_parameters = None
        self._job_status = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_name is not None:
            self.job_name = job_name
        if job_kind is not None:
            self.job_kind = job_kind
        if job_parameters is not None:
            self.job_parameters = job_parameters
        if job_status is not None:
            self.job_status = job_status
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this GcTask.

        gc任务的ID。

        :return: The id of this GcTask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this GcTask.

        gc任务的ID。

        :param id: The id of this GcTask.
        :type id: int
        """
        self._id = id

    @property
    def job_name(self):
        r"""Gets the job_name of this GcTask.

        gc任务的名称。

        :return: The job_name of this GcTask.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this GcTask.

        gc任务的名称。

        :param job_name: The job_name of this GcTask.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_kind(self):
        r"""Gets the job_kind of this GcTask.

        任务类型，MANUAL：手动执行，SCHEDULE：定时执行。

        :return: The job_kind of this GcTask.
        :rtype: str
        """
        return self._job_kind

    @job_kind.setter
    def job_kind(self, job_kind):
        r"""Sets the job_kind of this GcTask.

        任务类型，MANUAL：手动执行，SCHEDULE：定时执行。

        :param job_kind: The job_kind of this GcTask.
        :type job_kind: str
        """
        self._job_kind = job_kind

    @property
    def job_parameters(self):
        r"""Gets the job_parameters of this GcTask.

        :return: The job_parameters of this GcTask.
        :rtype: :class:`huaweicloudsdkswr.v2.JobParameters`
        """
        return self._job_parameters

    @job_parameters.setter
    def job_parameters(self, job_parameters):
        r"""Sets the job_parameters of this GcTask.

        :param job_parameters: The job_parameters of this GcTask.
        :type job_parameters: :class:`huaweicloudsdkswr.v2.JobParameters`
        """
        self._job_parameters = job_parameters

    @property
    def job_status(self):
        r"""Gets the job_status of this GcTask.

        gc任务的状态，Success：已完成，Stopped：已停止，Running：清理中，Pending：排队中，Error：失败。

        :return: The job_status of this GcTask.
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        r"""Sets the job_status of this GcTask.

        gc任务的状态，Success：已完成，Stopped：已停止，Running：清理中，Pending：排队中，Error：失败。

        :param job_status: The job_status of this GcTask.
        :type job_status: str
        """
        self._job_status = job_status

    @property
    def creation_time(self):
        r"""Gets the creation_time of this GcTask.

        gc任务的创建时间。

        :return: The creation_time of this GcTask.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        r"""Sets the creation_time of this GcTask.

        gc任务的创建时间。

        :param creation_time: The creation_time of this GcTask.
        :type creation_time: str
        """
        self._creation_time = creation_time

    @property
    def update_time(self):
        r"""Gets the update_time of this GcTask.

        gc任务的更新时间。

        :return: The update_time of this GcTask.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this GcTask.

        gc任务的更新时间。

        :param update_time: The update_time of this GcTask.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, GcTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
