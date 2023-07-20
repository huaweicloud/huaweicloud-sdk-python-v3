# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloneJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'name': 'str',
        'task_version': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'name': 'name',
        'task_version': 'task_version'
    }

    def __init__(self, job_id=None, name=None, task_version=None):
        """CloneJobReq

        The model defined in huaweicloud sdk

        :param job_id: 被克隆任务ID。
        :type job_id: str
        :param name: 克隆任务名称。名称在4位到50位之间，必须以字母开头，可以包含字母、数字、中划线或下划线，不能包含其他特殊字符，任务名称不能重复。
        :type name: str
        :param task_version: 任务版本号，新UX任务为2.0。默认为空，即克隆老任务。
        :type task_version: str
        """
        
        

        self._job_id = None
        self._name = None
        self._task_version = None
        self.discriminator = None

        self.job_id = job_id
        self.name = name
        if task_version is not None:
            self.task_version = task_version

    @property
    def job_id(self):
        """Gets the job_id of this CloneJobReq.

        被克隆任务ID。

        :return: The job_id of this CloneJobReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CloneJobReq.

        被克隆任务ID。

        :param job_id: The job_id of this CloneJobReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def name(self):
        """Gets the name of this CloneJobReq.

        克隆任务名称。名称在4位到50位之间，必须以字母开头，可以包含字母、数字、中划线或下划线，不能包含其他特殊字符，任务名称不能重复。

        :return: The name of this CloneJobReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloneJobReq.

        克隆任务名称。名称在4位到50位之间，必须以字母开头，可以包含字母、数字、中划线或下划线，不能包含其他特殊字符，任务名称不能重复。

        :param name: The name of this CloneJobReq.
        :type name: str
        """
        self._name = name

    @property
    def task_version(self):
        """Gets the task_version of this CloneJobReq.

        任务版本号，新UX任务为2.0。默认为空，即克隆老任务。

        :return: The task_version of this CloneJobReq.
        :rtype: str
        """
        return self._task_version

    @task_version.setter
    def task_version(self, task_version):
        """Sets the task_version of this CloneJobReq.

        任务版本号，新UX任务为2.0。默认为空，即克隆老任务。

        :param task_version: The task_version of this CloneJobReq.
        :type task_version: str
        """
        self._task_version = task_version

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
        if not isinstance(other, CloneJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
