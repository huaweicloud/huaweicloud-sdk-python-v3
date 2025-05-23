# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTasklogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'task_id': 'str',
        'execute_id': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'task_id': 'task_id',
        'execute_id': 'execute_id'
    }

    def __init__(self, project_id=None, task_id=None, execute_id=None):
        r"""ShowTasklogRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param task_id: 任务ID
        :type task_id: str
        :param execute_id: 任务单次的执行ID
        :type execute_id: str
        """
        
        

        self._project_id = None
        self._task_id = None
        self._execute_id = None
        self.discriminator = None

        self.project_id = project_id
        self.task_id = task_id
        if execute_id is not None:
            self.execute_id = execute_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowTasklogRequest.

        项目ID

        :return: The project_id of this ShowTasklogRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowTasklogRequest.

        项目ID

        :param project_id: The project_id of this ShowTasklogRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowTasklogRequest.

        任务ID

        :return: The task_id of this ShowTasklogRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowTasklogRequest.

        任务ID

        :param task_id: The task_id of this ShowTasklogRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def execute_id(self):
        r"""Gets the execute_id of this ShowTasklogRequest.

        任务单次的执行ID

        :return: The execute_id of this ShowTasklogRequest.
        :rtype: str
        """
        return self._execute_id

    @execute_id.setter
    def execute_id(self, execute_id):
        r"""Sets the execute_id of this ShowTasklogRequest.

        任务单次的执行ID

        :param execute_id: The execute_id of this ShowTasklogRequest.
        :type execute_id: str
        """
        self._execute_id = execute_id

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
        if not isinstance(other, ShowTasklogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
