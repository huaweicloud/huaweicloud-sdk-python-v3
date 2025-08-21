# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineDto:

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
        'web_url': 'str',
        'sha': 'str',
        'ref': 'str',
        'status': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'started_at': 'str',
        'finished_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'web_url': 'web_url',
        'sha': 'sha',
        'ref': 'ref',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'started_at': 'started_at',
        'finished_at': 'finished_at'
    }

    def __init__(self, id=None, web_url=None, sha=None, ref=None, status=None, created_at=None, updated_at=None, started_at=None, finished_at=None):
        r"""PipelineDto

        The model defined in huaweicloud sdk

        :param id: 流水线ID
        :type id: int
        :param web_url: 流水线链接
        :type web_url: str
        :param sha: commit id
        :type sha: str
        :param ref: 分支
        :type ref: str
        :param status: 流水线状态，pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时
        :type status: str
        :param created_at: 流水线创建时间
        :type created_at: str
        :param updated_at: 流水线更新时间
        :type updated_at: str
        :param started_at: 流水线开始时间
        :type started_at: str
        :param finished_at: 流水线结束时间
        :type finished_at: str
        """
        
        

        self._id = None
        self._web_url = None
        self._sha = None
        self._ref = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._started_at = None
        self._finished_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if web_url is not None:
            self.web_url = web_url
        if sha is not None:
            self.sha = sha
        if ref is not None:
            self.ref = ref
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at

    @property
    def id(self):
        r"""Gets the id of this PipelineDto.

        流水线ID

        :return: The id of this PipelineDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PipelineDto.

        流水线ID

        :param id: The id of this PipelineDto.
        :type id: int
        """
        self._id = id

    @property
    def web_url(self):
        r"""Gets the web_url of this PipelineDto.

        流水线链接

        :return: The web_url of this PipelineDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this PipelineDto.

        流水线链接

        :param web_url: The web_url of this PipelineDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def sha(self):
        r"""Gets the sha of this PipelineDto.

        commit id

        :return: The sha of this PipelineDto.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this PipelineDto.

        commit id

        :param sha: The sha of this PipelineDto.
        :type sha: str
        """
        self._sha = sha

    @property
    def ref(self):
        r"""Gets the ref of this PipelineDto.

        分支

        :return: The ref of this PipelineDto.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this PipelineDto.

        分支

        :param ref: The ref of this PipelineDto.
        :type ref: str
        """
        self._ref = ref

    @property
    def status(self):
        r"""Gets the status of this PipelineDto.

        流水线状态，pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :return: The status of this PipelineDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PipelineDto.

        流水线状态，pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :param status: The status of this PipelineDto.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this PipelineDto.

        流水线创建时间

        :return: The created_at of this PipelineDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PipelineDto.

        流水线创建时间

        :param created_at: The created_at of this PipelineDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this PipelineDto.

        流水线更新时间

        :return: The updated_at of this PipelineDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this PipelineDto.

        流水线更新时间

        :param updated_at: The updated_at of this PipelineDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def started_at(self):
        r"""Gets the started_at of this PipelineDto.

        流水线开始时间

        :return: The started_at of this PipelineDto.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this PipelineDto.

        流水线开始时间

        :param started_at: The started_at of this PipelineDto.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        r"""Gets the finished_at of this PipelineDto.

        流水线结束时间

        :return: The finished_at of this PipelineDto.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        r"""Sets the finished_at of this PipelineDto.

        流水线结束时间

        :param finished_at: The finished_at of this PipelineDto.
        :type finished_at: str
        """
        self._finished_at = finished_at

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
        if not isinstance(other, PipelineDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
