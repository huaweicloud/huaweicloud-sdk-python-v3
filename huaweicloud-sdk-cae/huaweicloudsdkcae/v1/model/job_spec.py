# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'progress': 'float',
        'status': 'str',
        'tasks': 'list[Task]'
    }

    attribute_map = {
        'progress': 'progress',
        'status': 'status',
        'tasks': 'tasks'
    }

    def __init__(self, progress=None, status=None, tasks=None):
        """JobSpec

        The model defined in huaweicloud sdk

        :param progress: 任务进度。
        :type progress: float
        :param status: 任务状态。
        :type status: str
        :param tasks: 子任务。
        :type tasks: list[:class:`huaweicloudsdkcae.v1.Task`]
        """
        
        

        self._progress = None
        self._status = None
        self._tasks = None
        self.discriminator = None

        if progress is not None:
            self.progress = progress
        if status is not None:
            self.status = status
        if tasks is not None:
            self.tasks = tasks

    @property
    def progress(self):
        """Gets the progress of this JobSpec.

        任务进度。

        :return: The progress of this JobSpec.
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this JobSpec.

        任务进度。

        :param progress: The progress of this JobSpec.
        :type progress: float
        """
        self._progress = progress

    @property
    def status(self):
        """Gets the status of this JobSpec.

        任务状态。

        :return: The status of this JobSpec.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this JobSpec.

        任务状态。

        :param status: The status of this JobSpec.
        :type status: str
        """
        self._status = status

    @property
    def tasks(self):
        """Gets the tasks of this JobSpec.

        子任务。

        :return: The tasks of this JobSpec.
        :rtype: list[:class:`huaweicloudsdkcae.v1.Task`]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this JobSpec.

        子任务。

        :param tasks: The tasks of this JobSpec.
        :type tasks: list[:class:`huaweicloudsdkcae.v1.Task`]
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
        if not isinstance(other, JobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
