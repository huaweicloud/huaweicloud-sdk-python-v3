# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubtaskDetail:

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
        'status': 'str',
        'status_text': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'job_id': 'job_id',
        'namespace': 'namespace',
        'repository': 'repository',
        'tag': 'tag',
        'digest': 'digest',
        'status': 'status',
        'status_text': 'status_text',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, job_id=None, namespace=None, repository=None, tag=None, digest=None, status=None, status_text=None, start_time=None, end_time=None):
        r"""SubtaskDetail

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
        :param digest: 摘要
        :type digest: str
        :param status: 状态
        :type status: str
        :param status_text: 状态信息
        :type status_text: str
        :param start_time: 开始时间
        :type start_time: str
        :param end_time: 结束时间
        :type end_time: str
        """
        
        

        self._id = None
        self._job_id = None
        self._namespace = None
        self._repository = None
        self._tag = None
        self._digest = None
        self._status = None
        self._status_text = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.id = id
        self.job_id = job_id
        self.namespace = namespace
        self.repository = repository
        self.tag = tag
        self.digest = digest
        self.status = status
        self.status_text = status_text
        self.start_time = start_time
        self.end_time = end_time

    @property
    def id(self):
        r"""Gets the id of this SubtaskDetail.

        子任务ID

        :return: The id of this SubtaskDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SubtaskDetail.

        子任务ID

        :param id: The id of this SubtaskDetail.
        :type id: int
        """
        self._id = id

    @property
    def job_id(self):
        r"""Gets the job_id of this SubtaskDetail.

        内部任务ID

        :return: The job_id of this SubtaskDetail.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SubtaskDetail.

        内部任务ID

        :param job_id: The job_id of this SubtaskDetail.
        :type job_id: int
        """
        self._job_id = job_id

    @property
    def namespace(self):
        r"""Gets the namespace of this SubtaskDetail.

        命名空间名

        :return: The namespace of this SubtaskDetail.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this SubtaskDetail.

        命名空间名

        :param namespace: The namespace of this SubtaskDetail.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this SubtaskDetail.

        制品仓库

        :return: The repository of this SubtaskDetail.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this SubtaskDetail.

        制品仓库

        :param repository: The repository of this SubtaskDetail.
        :type repository: str
        """
        self._repository = repository

    @property
    def tag(self):
        r"""Gets the tag of this SubtaskDetail.

        制品版本

        :return: The tag of this SubtaskDetail.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this SubtaskDetail.

        制品版本

        :param tag: The tag of this SubtaskDetail.
        :type tag: str
        """
        self._tag = tag

    @property
    def digest(self):
        r"""Gets the digest of this SubtaskDetail.

        摘要

        :return: The digest of this SubtaskDetail.
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        r"""Sets the digest of this SubtaskDetail.

        摘要

        :param digest: The digest of this SubtaskDetail.
        :type digest: str
        """
        self._digest = digest

    @property
    def status(self):
        r"""Gets the status of this SubtaskDetail.

        状态

        :return: The status of this SubtaskDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubtaskDetail.

        状态

        :param status: The status of this SubtaskDetail.
        :type status: str
        """
        self._status = status

    @property
    def status_text(self):
        r"""Gets the status_text of this SubtaskDetail.

        状态信息

        :return: The status_text of this SubtaskDetail.
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        r"""Sets the status_text of this SubtaskDetail.

        状态信息

        :param status_text: The status_text of this SubtaskDetail.
        :type status_text: str
        """
        self._status_text = status_text

    @property
    def start_time(self):
        r"""Gets the start_time of this SubtaskDetail.

        开始时间

        :return: The start_time of this SubtaskDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this SubtaskDetail.

        开始时间

        :param start_time: The start_time of this SubtaskDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SubtaskDetail.

        结束时间

        :return: The end_time of this SubtaskDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SubtaskDetail.

        结束时间

        :param end_time: The end_time of this SubtaskDetail.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, SubtaskDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
