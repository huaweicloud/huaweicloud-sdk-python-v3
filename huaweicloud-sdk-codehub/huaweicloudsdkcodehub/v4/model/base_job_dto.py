# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseJobDto:

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
        'sha': 'str',
        'ref': 'str',
        'status': 'str',
        'name': 'str',
        'target_url': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'started_at': 'str',
        'finished_at': 'str',
        'third_build_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'sha': 'sha',
        'ref': 'ref',
        'status': 'status',
        'name': 'name',
        'target_url': 'target_url',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'started_at': 'started_at',
        'finished_at': 'finished_at',
        'third_build_id': 'third_build_id'
    }

    def __init__(self, id=None, sha=None, ref=None, status=None, name=None, target_url=None, created_at=None, updated_at=None, started_at=None, finished_at=None, third_build_id=None):
        r"""BaseJobDto

        The model defined in huaweicloud sdk

        :param id: 任务ID
        :type id: int
        :param sha: 提交ID
        :type sha: str
        :param ref: 分支
        :type ref: str
        :param status: 阶段状态, pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时
        :type status: str
        :param name: 任务名称
        :type name: str
        :param target_url: 任务链接
        :type target_url: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param started_at: 开始时间
        :type started_at: str
        :param finished_at: 结束时间
        :type finished_at: str
        :param third_build_id: 任务在构建系统中的ID
        :type third_build_id: str
        """
        
        

        self._id = None
        self._sha = None
        self._ref = None
        self._status = None
        self._name = None
        self._target_url = None
        self._created_at = None
        self._updated_at = None
        self._started_at = None
        self._finished_at = None
        self._third_build_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if sha is not None:
            self.sha = sha
        if ref is not None:
            self.ref = ref
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if target_url is not None:
            self.target_url = target_url
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if third_build_id is not None:
            self.third_build_id = third_build_id

    @property
    def id(self):
        r"""Gets the id of this BaseJobDto.

        任务ID

        :return: The id of this BaseJobDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BaseJobDto.

        任务ID

        :param id: The id of this BaseJobDto.
        :type id: int
        """
        self._id = id

    @property
    def sha(self):
        r"""Gets the sha of this BaseJobDto.

        提交ID

        :return: The sha of this BaseJobDto.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this BaseJobDto.

        提交ID

        :param sha: The sha of this BaseJobDto.
        :type sha: str
        """
        self._sha = sha

    @property
    def ref(self):
        r"""Gets the ref of this BaseJobDto.

        分支

        :return: The ref of this BaseJobDto.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this BaseJobDto.

        分支

        :param ref: The ref of this BaseJobDto.
        :type ref: str
        """
        self._ref = ref

    @property
    def status(self):
        r"""Gets the status of this BaseJobDto.

        阶段状态, pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :return: The status of this BaseJobDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BaseJobDto.

        阶段状态, pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :param status: The status of this BaseJobDto.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this BaseJobDto.

        任务名称

        :return: The name of this BaseJobDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BaseJobDto.

        任务名称

        :param name: The name of this BaseJobDto.
        :type name: str
        """
        self._name = name

    @property
    def target_url(self):
        r"""Gets the target_url of this BaseJobDto.

        任务链接

        :return: The target_url of this BaseJobDto.
        :rtype: str
        """
        return self._target_url

    @target_url.setter
    def target_url(self, target_url):
        r"""Sets the target_url of this BaseJobDto.

        任务链接

        :param target_url: The target_url of this BaseJobDto.
        :type target_url: str
        """
        self._target_url = target_url

    @property
    def created_at(self):
        r"""Gets the created_at of this BaseJobDto.

        创建时间

        :return: The created_at of this BaseJobDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this BaseJobDto.

        创建时间

        :param created_at: The created_at of this BaseJobDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this BaseJobDto.

        更新时间

        :return: The updated_at of this BaseJobDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this BaseJobDto.

        更新时间

        :param updated_at: The updated_at of this BaseJobDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def started_at(self):
        r"""Gets the started_at of this BaseJobDto.

        开始时间

        :return: The started_at of this BaseJobDto.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this BaseJobDto.

        开始时间

        :param started_at: The started_at of this BaseJobDto.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        r"""Gets the finished_at of this BaseJobDto.

        结束时间

        :return: The finished_at of this BaseJobDto.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        r"""Sets the finished_at of this BaseJobDto.

        结束时间

        :param finished_at: The finished_at of this BaseJobDto.
        :type finished_at: str
        """
        self._finished_at = finished_at

    @property
    def third_build_id(self):
        r"""Gets the third_build_id of this BaseJobDto.

        任务在构建系统中的ID

        :return: The third_build_id of this BaseJobDto.
        :rtype: str
        """
        return self._third_build_id

    @third_build_id.setter
    def third_build_id(self, third_build_id):
        r"""Sets the third_build_id of this BaseJobDto.

        任务在构建系统中的ID

        :param third_build_id: The third_build_id of this BaseJobDto.
        :type third_build_id: str
        """
        self._third_build_id = third_build_id

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
        if not isinstance(other, BaseJobDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
