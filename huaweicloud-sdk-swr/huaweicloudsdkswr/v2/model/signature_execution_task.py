# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignatureExecutionTask:

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
        'execution_id': 'int',
        'job_id': 'str',
        'status': 'str',
        'status_text': 'str',
        'namespace': 'str',
        'repository': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'execution_id': 'execution_id',
        'job_id': 'job_id',
        'status': 'status',
        'status_text': 'status_text',
        'namespace': 'namespace',
        'repository': 'repository',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, execution_id=None, job_id=None, status=None, status_text=None, namespace=None, repository=None, created_at=None, updated_at=None):
        r"""SignatureExecutionTask

        The model defined in huaweicloud sdk

        :param id: 执行任务ID
        :type id: int
        :param execution_id: 执行ID
        :type execution_id: int
        :param job_id: jobId
        :type job_id: str
        :param status: 执行任务状态
        :type status: str
        :param status_text: 执行任务状态信息
        :type status_text: str
        :param namespace: 命名空间
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._execution_id = None
        self._job_id = None
        self._status = None
        self._status_text = None
        self._namespace = None
        self._repository = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if execution_id is not None:
            self.execution_id = execution_id
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if status_text is not None:
            self.status_text = status_text
        if namespace is not None:
            self.namespace = namespace
        if repository is not None:
            self.repository = repository
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this SignatureExecutionTask.

        执行任务ID

        :return: The id of this SignatureExecutionTask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SignatureExecutionTask.

        执行任务ID

        :param id: The id of this SignatureExecutionTask.
        :type id: int
        """
        self._id = id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this SignatureExecutionTask.

        执行ID

        :return: The execution_id of this SignatureExecutionTask.
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this SignatureExecutionTask.

        执行ID

        :param execution_id: The execution_id of this SignatureExecutionTask.
        :type execution_id: int
        """
        self._execution_id = execution_id

    @property
    def job_id(self):
        r"""Gets the job_id of this SignatureExecutionTask.

        jobId

        :return: The job_id of this SignatureExecutionTask.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SignatureExecutionTask.

        jobId

        :param job_id: The job_id of this SignatureExecutionTask.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def status(self):
        r"""Gets the status of this SignatureExecutionTask.

        执行任务状态

        :return: The status of this SignatureExecutionTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SignatureExecutionTask.

        执行任务状态

        :param status: The status of this SignatureExecutionTask.
        :type status: str
        """
        self._status = status

    @property
    def status_text(self):
        r"""Gets the status_text of this SignatureExecutionTask.

        执行任务状态信息

        :return: The status_text of this SignatureExecutionTask.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        r"""Sets the status_text of this SignatureExecutionTask.

        执行任务状态信息

        :param status_text: The status_text of this SignatureExecutionTask.
        :type status_text: str
        """
        self._status_text = status_text

    @property
    def namespace(self):
        r"""Gets the namespace of this SignatureExecutionTask.

        命名空间

        :return: The namespace of this SignatureExecutionTask.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this SignatureExecutionTask.

        命名空间

        :param namespace: The namespace of this SignatureExecutionTask.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this SignatureExecutionTask.

        镜像仓库名称

        :return: The repository of this SignatureExecutionTask.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this SignatureExecutionTask.

        镜像仓库名称

        :param repository: The repository of this SignatureExecutionTask.
        :type repository: str
        """
        self._repository = repository

    @property
    def created_at(self):
        r"""Gets the created_at of this SignatureExecutionTask.

        创建时间

        :return: The created_at of this SignatureExecutionTask.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SignatureExecutionTask.

        创建时间

        :param created_at: The created_at of this SignatureExecutionTask.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SignatureExecutionTask.

        更新时间

        :return: The updated_at of this SignatureExecutionTask.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SignatureExecutionTask.

        更新时间

        :param updated_at: The updated_at of this SignatureExecutionTask.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, SignatureExecutionTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
