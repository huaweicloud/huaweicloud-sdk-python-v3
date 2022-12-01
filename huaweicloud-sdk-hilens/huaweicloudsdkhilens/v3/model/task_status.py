# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cause': 'str',
        'pod_id': 'str',
        'pod_name': 'str',
        'task_status': 'str'
    }

    attribute_map = {
        'cause': 'cause',
        'pod_id': 'pod_id',
        'pod_name': 'pod_name',
        'task_status': 'task_status'
    }

    def __init__(self, cause=None, pod_id=None, pod_name=None, task_status=None):
        """TaskStatus

        The model defined in huaweicloud sdk

        :param cause: 作业运行失败原因
        :type cause: str
        :param pod_id: 实例id
        :type pod_id: str
        :param pod_name: 实例名称
        :type pod_name: str
        :param task_status: 作业在实例上的状态
        :type task_status: str
        """
        
        

        self._cause = None
        self._pod_id = None
        self._pod_name = None
        self._task_status = None
        self.discriminator = None

        if cause is not None:
            self.cause = cause
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_name is not None:
            self.pod_name = pod_name
        if task_status is not None:
            self.task_status = task_status

    @property
    def cause(self):
        """Gets the cause of this TaskStatus.

        作业运行失败原因

        :return: The cause of this TaskStatus.
        :rtype: str
        """
        return self._cause

    @cause.setter
    def cause(self, cause):
        """Sets the cause of this TaskStatus.

        作业运行失败原因

        :param cause: The cause of this TaskStatus.
        :type cause: str
        """
        self._cause = cause

    @property
    def pod_id(self):
        """Gets the pod_id of this TaskStatus.

        实例id

        :return: The pod_id of this TaskStatus.
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        """Sets the pod_id of this TaskStatus.

        实例id

        :param pod_id: The pod_id of this TaskStatus.
        :type pod_id: str
        """
        self._pod_id = pod_id

    @property
    def pod_name(self):
        """Gets the pod_name of this TaskStatus.

        实例名称

        :return: The pod_name of this TaskStatus.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this TaskStatus.

        实例名称

        :param pod_name: The pod_name of this TaskStatus.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def task_status(self):
        """Gets the task_status of this TaskStatus.

        作业在实例上的状态

        :return: The task_status of this TaskStatus.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this TaskStatus.

        作业在实例上的状态

        :param task_status: The task_status of this TaskStatus.
        :type task_status: str
        """
        self._task_status = task_status

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
        if not isinstance(other, TaskStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
