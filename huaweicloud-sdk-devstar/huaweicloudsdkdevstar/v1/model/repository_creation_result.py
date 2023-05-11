# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepositoryCreationResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository': 'RepositoryBasicInfo',
        'task_id': 'str',
        'status': 'str',
        'failure_reason': 'str'
    }

    attribute_map = {
        'repository': 'repository',
        'task_id': 'task_id',
        'status': 'status',
        'failure_reason': 'failure_reason'
    }

    def __init__(self, repository=None, task_id=None, status=None, failure_reason=None):
        """RepositoryCreationResult

        The model defined in huaweicloud sdk

        :param repository: 
        :type repository: :class:`huaweicloudsdkdevstar.v1.RepositoryBasicInfo`
        :param task_id: 任务id
        :type task_id: str
        :param status: 任务状态, success:成功,failed:失败,creating:创建中
        :type status: str
        :param failure_reason: 失败原因
        :type failure_reason: str
        """
        
        

        self._repository = None
        self._task_id = None
        self._status = None
        self._failure_reason = None
        self.discriminator = None

        if repository is not None:
            self.repository = repository
        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def repository(self):
        """Gets the repository of this RepositoryCreationResult.

        :return: The repository of this RepositoryCreationResult.
        :rtype: :class:`huaweicloudsdkdevstar.v1.RepositoryBasicInfo`
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this RepositoryCreationResult.

        :param repository: The repository of this RepositoryCreationResult.
        :type repository: :class:`huaweicloudsdkdevstar.v1.RepositoryBasicInfo`
        """
        self._repository = repository

    @property
    def task_id(self):
        """Gets the task_id of this RepositoryCreationResult.

        任务id

        :return: The task_id of this RepositoryCreationResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this RepositoryCreationResult.

        任务id

        :param task_id: The task_id of this RepositoryCreationResult.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        """Gets the status of this RepositoryCreationResult.

        任务状态, success:成功,failed:失败,creating:创建中

        :return: The status of this RepositoryCreationResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RepositoryCreationResult.

        任务状态, success:成功,failed:失败,creating:创建中

        :param status: The status of this RepositoryCreationResult.
        :type status: str
        """
        self._status = status

    @property
    def failure_reason(self):
        """Gets the failure_reason of this RepositoryCreationResult.

        失败原因

        :return: The failure_reason of this RepositoryCreationResult.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this RepositoryCreationResult.

        失败原因

        :param failure_reason: The failure_reason of this RepositoryCreationResult.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

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
        if not isinstance(other, RepositoryCreationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
