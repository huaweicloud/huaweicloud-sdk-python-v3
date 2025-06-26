# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SignatureExecutionSubTask:

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
        'job_id': 'str',
        'namespace': 'str',
        'repository': 'str',
        'tags': 'str',
        'digest': 'str',
        'status': 'str',
        'status_text': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'job_id': 'job_id',
        'namespace': 'namespace',
        'repository': 'repository',
        'tags': 'tags',
        'digest': 'digest',
        'status': 'status',
        'status_text': 'status_text',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, job_id=None, namespace=None, repository=None, tags=None, digest=None, status=None, status_text=None, created_at=None, updated_at=None):
        r"""SignatureExecutionSubTask

        The model defined in huaweicloud sdk

        :param id: 子任务ID
        :type id: int
        :param job_id: 子任务详情
        :type job_id: str
        :param namespace: 命名空间
        :type namespace: str
        :param repository: 镜像仓库
        :type repository: str
        :param tags: 镜像版本
        :type tags: str
        :param digest: 镜像层sha256
        :type digest: str
        :param status: 子任务状态
        :type status: str
        :param status_text: 状态详情信息
        :type status_text: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        """
        
        

        self._id = None
        self._job_id = None
        self._namespace = None
        self._repository = None
        self._tags = None
        self._digest = None
        self._status = None
        self._status_text = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if job_id is not None:
            self.job_id = job_id
        if namespace is not None:
            self.namespace = namespace
        if repository is not None:
            self.repository = repository
        if tags is not None:
            self.tags = tags
        if digest is not None:
            self.digest = digest
        if status is not None:
            self.status = status
        if status_text is not None:
            self.status_text = status_text
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this SignatureExecutionSubTask.

        子任务ID

        :return: The id of this SignatureExecutionSubTask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SignatureExecutionSubTask.

        子任务ID

        :param id: The id of this SignatureExecutionSubTask.
        :type id: int
        """
        self._id = id

    @property
    def job_id(self):
        r"""Gets the job_id of this SignatureExecutionSubTask.

        子任务详情

        :return: The job_id of this SignatureExecutionSubTask.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SignatureExecutionSubTask.

        子任务详情

        :param job_id: The job_id of this SignatureExecutionSubTask.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def namespace(self):
        r"""Gets the namespace of this SignatureExecutionSubTask.

        命名空间

        :return: The namespace of this SignatureExecutionSubTask.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this SignatureExecutionSubTask.

        命名空间

        :param namespace: The namespace of this SignatureExecutionSubTask.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this SignatureExecutionSubTask.

        镜像仓库

        :return: The repository of this SignatureExecutionSubTask.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this SignatureExecutionSubTask.

        镜像仓库

        :param repository: The repository of this SignatureExecutionSubTask.
        :type repository: str
        """
        self._repository = repository

    @property
    def tags(self):
        r"""Gets the tags of this SignatureExecutionSubTask.

        镜像版本

        :return: The tags of this SignatureExecutionSubTask.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this SignatureExecutionSubTask.

        镜像版本

        :param tags: The tags of this SignatureExecutionSubTask.
        :type tags: str
        """
        self._tags = tags

    @property
    def digest(self):
        r"""Gets the digest of this SignatureExecutionSubTask.

        镜像层sha256

        :return: The digest of this SignatureExecutionSubTask.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this SignatureExecutionSubTask.

        镜像层sha256

        :param digest: The digest of this SignatureExecutionSubTask.
        :type digest: str
        """
        self._digest = digest

    @property
    def status(self):
        r"""Gets the status of this SignatureExecutionSubTask.

        子任务状态

        :return: The status of this SignatureExecutionSubTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SignatureExecutionSubTask.

        子任务状态

        :param status: The status of this SignatureExecutionSubTask.
        :type status: str
        """
        self._status = status

    @property
    def status_text(self):
        r"""Gets the status_text of this SignatureExecutionSubTask.

        状态详情信息

        :return: The status_text of this SignatureExecutionSubTask.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        r"""Sets the status_text of this SignatureExecutionSubTask.

        状态详情信息

        :param status_text: The status_text of this SignatureExecutionSubTask.
        :type status_text: str
        """
        self._status_text = status_text

    @property
    def created_at(self):
        r"""Gets the created_at of this SignatureExecutionSubTask.

        创建时间

        :return: The created_at of this SignatureExecutionSubTask.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this SignatureExecutionSubTask.

        创建时间

        :param created_at: The created_at of this SignatureExecutionSubTask.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this SignatureExecutionSubTask.

        更新时间

        :return: The updated_at of this SignatureExecutionSubTask.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this SignatureExecutionSubTask.

        更新时间

        :param updated_at: The updated_at of this SignatureExecutionSubTask.
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
        if not isinstance(other, SignatureExecutionSubTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
