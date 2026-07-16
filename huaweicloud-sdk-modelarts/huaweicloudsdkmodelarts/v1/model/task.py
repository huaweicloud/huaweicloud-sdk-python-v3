# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Task:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'algorithm': 'TaskAlgorithm',
        'task_resource': 'TaskTaskResource',
        'log_export_path': 'TaskLogExportPath'
    }

    attribute_map = {
        'role': 'role',
        'algorithm': 'algorithm',
        'task_resource': 'task_resource',
        'log_export_path': 'log_export_path'
    }

    def __init__(self, role=None, algorithm=None, task_resource=None, log_export_path=None):
        r"""Task

        The model defined in huaweicloud sdk

        :param role: **参数解释**：任务角色，该功能暂未支持。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type role: str
        :param algorithm: 
        :type algorithm: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithm`
        :param task_resource: 
        :type task_resource: :class:`huaweicloudsdkmodelarts.v1.TaskTaskResource`
        :param log_export_path: 
        :type log_export_path: :class:`huaweicloudsdkmodelarts.v1.TaskLogExportPath`
        """
        
        

        self._role = None
        self._algorithm = None
        self._task_resource = None
        self._log_export_path = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if algorithm is not None:
            self.algorithm = algorithm
        if task_resource is not None:
            self.task_resource = task_resource
        if log_export_path is not None:
            self.log_export_path = log_export_path

    @property
    def role(self):
        r"""Gets the role of this Task.

        **参数解释**：任务角色，该功能暂未支持。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The role of this Task.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this Task.

        **参数解释**：任务角色，该功能暂未支持。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param role: The role of this Task.
        :type role: str
        """
        self._role = role

    @property
    def algorithm(self):
        r"""Gets the algorithm of this Task.

        :return: The algorithm of this Task.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithm`
        """
        return self._algorithm

    @algorithm.setter
    def algorithm(self, algorithm):
        r"""Sets the algorithm of this Task.

        :param algorithm: The algorithm of this Task.
        :type algorithm: :class:`huaweicloudsdkmodelarts.v1.TaskAlgorithm`
        """
        self._algorithm = algorithm

    @property
    def task_resource(self):
        r"""Gets the task_resource of this Task.

        :return: The task_resource of this Task.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TaskTaskResource`
        """
        return self._task_resource

    @task_resource.setter
    def task_resource(self, task_resource):
        r"""Sets the task_resource of this Task.

        :param task_resource: The task_resource of this Task.
        :type task_resource: :class:`huaweicloudsdkmodelarts.v1.TaskTaskResource`
        """
        self._task_resource = task_resource

    @property
    def log_export_path(self):
        r"""Gets the log_export_path of this Task.

        :return: The log_export_path of this Task.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.TaskLogExportPath`
        """
        return self._log_export_path

    @log_export_path.setter
    def log_export_path(self, log_export_path):
        r"""Sets the log_export_path of this Task.

        :param log_export_path: The log_export_path of this Task.
        :type log_export_path: :class:`huaweicloudsdkmodelarts.v1.TaskLogExportPath`
        """
        self._log_export_path = log_export_path

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
        if not isinstance(other, Task):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
