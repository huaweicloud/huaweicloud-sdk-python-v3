# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eihealth_project_id': 'str',
        'job_id': 'str',
        'task_name': 'str',
        'task_index': 'str'
    }

    attribute_map = {
        'eihealth_project_id': 'eihealth_project_id',
        'job_id': 'job_id',
        'task_name': 'task_name',
        'task_index': 'task_index'
    }

    def __init__(self, eihealth_project_id=None, job_id=None, task_name=None, task_index=None):
        """ShowTaskInstancesRequest

        The model defined in huaweicloud sdk

        :param eihealth_project_id: 医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param job_id: 作业id
        :type job_id: str
        :param task_name: 子任务名称
        :type task_name: str
        :param task_index: 子任务的并发序号
        :type task_index: str
        """
        
        

        self._eihealth_project_id = None
        self._job_id = None
        self._task_name = None
        self._task_index = None
        self.discriminator = None

        self.eihealth_project_id = eihealth_project_id
        self.job_id = job_id
        self.task_name = task_name
        if task_index is not None:
            self.task_index = task_index

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ShowTaskInstancesRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ShowTaskInstancesRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ShowTaskInstancesRequest.

        医疗智能体平台项目ID，您可以在EIHealth平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ShowTaskInstancesRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def job_id(self):
        """Gets the job_id of this ShowTaskInstancesRequest.

        作业id

        :return: The job_id of this ShowTaskInstancesRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowTaskInstancesRequest.

        作业id

        :param job_id: The job_id of this ShowTaskInstancesRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def task_name(self):
        """Gets the task_name of this ShowTaskInstancesRequest.

        子任务名称

        :return: The task_name of this ShowTaskInstancesRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ShowTaskInstancesRequest.

        子任务名称

        :param task_name: The task_name of this ShowTaskInstancesRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def task_index(self):
        """Gets the task_index of this ShowTaskInstancesRequest.

        子任务的并发序号

        :return: The task_index of this ShowTaskInstancesRequest.
        :rtype: str
        """
        return self._task_index

    @task_index.setter
    def task_index(self, task_index):
        """Sets the task_index of this ShowTaskInstancesRequest.

        子任务的并发序号

        :param task_index: The task_index of this ShowTaskInstancesRequest.
        :type task_index: str
        """
        self._task_index = task_index

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
        if not isinstance(other, ShowTaskInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
