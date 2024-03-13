# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobAndNodeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'job_name': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'job_name': 'job_name',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, task_id=None, job_name=None, workspace_id=None):
        """JobAndNodeInfo

        The model defined in huaweicloud sdk

        :param task_id: 作业算子id
        :type task_id: str
        :param job_name: 作业算子名称
        :type job_name: str
        :param workspace_id: 作业算子所在空间id
        :type workspace_id: str
        """
        
        

        self._task_id = None
        self._job_name = None
        self._workspace_id = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if job_name is not None:
            self.job_name = job_name
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def task_id(self):
        """Gets the task_id of this JobAndNodeInfo.

        作业算子id

        :return: The task_id of this JobAndNodeInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this JobAndNodeInfo.

        作业算子id

        :param task_id: The task_id of this JobAndNodeInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def job_name(self):
        """Gets the job_name of this JobAndNodeInfo.

        作业算子名称

        :return: The job_name of this JobAndNodeInfo.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this JobAndNodeInfo.

        作业算子名称

        :param job_name: The job_name of this JobAndNodeInfo.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this JobAndNodeInfo.

        作业算子所在空间id

        :return: The workspace_id of this JobAndNodeInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this JobAndNodeInfo.

        作业算子所在空间id

        :param workspace_id: The workspace_id of this JobAndNodeInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, JobAndNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
