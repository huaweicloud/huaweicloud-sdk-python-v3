# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Subtask:

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
        'job_id': 'int',
        'namespace': 'str',
        'repository': 'str',
        'tag': 'str',
        'digest': 'str',
        'action': 'str',
        'status': 'str',
        'status_text': 'str',
        'op_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_id': 'job_id',
        'namespace': 'namespace',
        'repository': 'repository',
        'tag': 'tag',
        'digest': 'digest',
        'action': 'action',
        'status': 'status',
        'status_text': 'status_text',
        'op_time': 'op_time'
    }

    def __init__(self, id=None, job_id=None, namespace=None, repository=None, tag=None, digest=None, action=None, status=None, status_text=None, op_time=None):
        r"""Subtask

        The model defined in huaweicloud sdk

        :param id: 子任务ID
        :type id: int
        :param job_id: 内部任务ID
        :type job_id: int
        :param namespace: 命名空间名
        :type namespace: str
        :param repository: 制品仓库
        :type repository: str
        :param tag: 制品版本
        :type tag: str
        :param digest: sha256值
        :type digest: str
        :param action: 老化动作， DEL
        :type action: str
        :param status: 状态，Initialized、Pending、InProgress、Succeed、Failed、Stopped
        :type status: str
        :param status_text: 状态信息
        :type status_text: str
        :param op_time: 开始时间
        :type op_time: str
        """
        
        

        self._id = None
        self._job_id = None
        self._namespace = None
        self._repository = None
        self._tag = None
        self._digest = None
        self._action = None
        self._status = None
        self._status_text = None
        self._op_time = None
        self.discriminator = None

        self.id = id
        self.job_id = job_id
        self.namespace = namespace
        self.repository = repository
        self.tag = tag
        self.digest = digest
        self.action = action
        self.status = status
        self.status_text = status_text
        self.op_time = op_time

    @property
    def id(self):
        r"""Gets the id of this Subtask.

        子任务ID

        :return: The id of this Subtask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Subtask.

        子任务ID

        :param id: The id of this Subtask.
        :type id: int
        """
        self._id = id

    @property
    def job_id(self):
        r"""Gets the job_id of this Subtask.

        内部任务ID

        :return: The job_id of this Subtask.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this Subtask.

        内部任务ID

        :param job_id: The job_id of this Subtask.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def namespace(self):
        r"""Gets the namespace of this Subtask.

        命名空间名

        :return: The namespace of this Subtask.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this Subtask.

        命名空间名

        :param namespace: The namespace of this Subtask.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this Subtask.

        制品仓库

        :return: The repository of this Subtask.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this Subtask.

        制品仓库

        :param repository: The repository of this Subtask.
        :type repository: str
        """
        self._repository = repository

    @property
    def tag(self):
        r"""Gets the tag of this Subtask.

        制品版本

        :return: The tag of this Subtask.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this Subtask.

        制品版本

        :param tag: The tag of this Subtask.
        :type tag: str
        """
        self._tag = tag

    @property
    def digest(self):
        r"""Gets the digest of this Subtask.

        sha256值

        :return: The digest of this Subtask.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this Subtask.

        sha256值

        :param digest: The digest of this Subtask.
        :type digest: str
        """
        self._digest = digest

    @property
    def action(self):
        r"""Gets the action of this Subtask.

        老化动作， DEL

        :return: The action of this Subtask.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this Subtask.

        老化动作， DEL

        :param action: The action of this Subtask.
        :type action: str
        """
        self._action = action

    @property
    def status(self):
        r"""Gets the status of this Subtask.

        状态，Initialized、Pending、InProgress、Succeed、Failed、Stopped

        :return: The status of this Subtask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Subtask.

        状态，Initialized、Pending、InProgress、Succeed、Failed、Stopped

        :param status: The status of this Subtask.
        :type status: str
        """
        self._status = status

    @property
    def status_text(self):
        r"""Gets the status_text of this Subtask.

        状态信息

        :return: The status_text of this Subtask.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        r"""Sets the status_text of this Subtask.

        状态信息

        :param status_text: The status_text of this Subtask.
        :type status_text: str
        """
        self._status_text = status_text

    @property
    def op_time(self):
        r"""Gets the op_time of this Subtask.

        开始时间

        :return: The op_time of this Subtask.
        :rtype: str
        """
        return self._op_time

    @op_time.setter
    def op_time(self, op_time):
        r"""Sets the op_time of this Subtask.

        开始时间

        :param op_time: The op_time of this Subtask.
        :type op_time: str
        """
        self._op_time = op_time

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
        if not isinstance(other, Subtask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
