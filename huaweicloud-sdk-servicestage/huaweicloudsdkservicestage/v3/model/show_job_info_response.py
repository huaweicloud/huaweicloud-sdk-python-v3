# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_count': 'int',
        'job': 'JobInfo',
        'tasks': 'list[TaskInfo]'
    }

    attribute_map = {
        'task_count': 'task_count',
        'job': 'job',
        'tasks': 'tasks'
    }

    def __init__(self, task_count=None, job=None, tasks=None):
        r"""ShowJobInfoResponse

        The model defined in huaweicloud sdk

        :param task_count: 
        :type task_count: int
        :param job: 
        :type job: :class:`huaweicloudsdkservicestage.v3.JobInfo`
        :param tasks: 
        :type tasks: list[:class:`huaweicloudsdkservicestage.v3.TaskInfo`]
        """
        
        super(ShowJobInfoResponse, self).__init__()

        self._task_count = None
        self._job = None
        self._tasks = None
        self.discriminator = None

        if task_count is not None:
            self.task_count = task_count
        if job is not None:
            self.job = job
        if tasks is not None:
            self.tasks = tasks

    @property
    def task_count(self):
        r"""Gets the task_count of this ShowJobInfoResponse.

        :return: The task_count of this ShowJobInfoResponse.
        :rtype: int
        """
        return self._task_count

    @task_count.setter
    def task_count(self, task_count):
        r"""Sets the task_count of this ShowJobInfoResponse.

        :param task_count: The task_count of this ShowJobInfoResponse.
        :type task_count: int
        """
        self._task_count = task_count

    @property
    def job(self):
        r"""Gets the job of this ShowJobInfoResponse.

        :return: The job of this ShowJobInfoResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v3.JobInfo`
        """
        return self._job

    @job.setter
    def job(self, job):
        r"""Sets the job of this ShowJobInfoResponse.

        :param job: The job of this ShowJobInfoResponse.
        :type job: :class:`huaweicloudsdkservicestage.v3.JobInfo`
        """
        self._job = job

    @property
    def tasks(self):
        r"""Gets the tasks of this ShowJobInfoResponse.

        :return: The tasks of this ShowJobInfoResponse.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.TaskInfo`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        r"""Sets the tasks of this ShowJobInfoResponse.

        :param tasks: The tasks of this ShowJobInfoResponse.
        :type tasks: list[:class:`huaweicloudsdkservicestage.v3.TaskInfo`]
        """
        self._tasks = tasks

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
        if not isinstance(other, ShowJobInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
