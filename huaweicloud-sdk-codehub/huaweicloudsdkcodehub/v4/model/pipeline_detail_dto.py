# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineDetailDto:

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
        'finished_at': 'str',
        'repository_id': 'int',
        'is_invalid': 'bool',
        'type': 'str',
        'stages': 'list[PipelineStageDto]',
        'is_latest': 'bool',
        'trigger_user': 'str',
        'all_job_finished': 'bool'
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
        'finished_at': 'finished_at',
        'repository_id': 'repository_id',
        'is_invalid': 'is_invalid',
        'type': 'type',
        'stages': 'stages',
        'is_latest': 'is_latest',
        'trigger_user': 'trigger_user',
        'all_job_finished': 'all_job_finished'
    }

    def __init__(self, id=None, web_url=None, sha=None, ref=None, status=None, created_at=None, updated_at=None, started_at=None, finished_at=None, repository_id=None, is_invalid=None, type=None, stages=None, is_latest=None, trigger_user=None, all_job_finished=None):
        r"""PipelineDetailDto

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
        :param repository_id: 仓库ID
        :type repository_id: int
        :param is_invalid: 流水线是否失效
        :type is_invalid: bool
        :param type: 流水线类型，MERGE REQUEST代表为合并请求触发的流水线
        :type type: str
        :param stages: 
        :type stages: list[:class:`huaweicloudsdkcodehub.v4.PipelineStageDto`]
        :param is_latest: 是否是最近一条流水线
        :type is_latest: bool
        :param trigger_user: 触发的用户
        :type trigger_user: str
        :param all_job_finished: 是否所有job都运行完成
        :type all_job_finished: bool
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
        self._repository_id = None
        self._is_invalid = None
        self._type = None
        self._stages = None
        self._is_latest = None
        self._trigger_user = None
        self._all_job_finished = None
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
        if repository_id is not None:
            self.repository_id = repository_id
        if is_invalid is not None:
            self.is_invalid = is_invalid
        if type is not None:
            self.type = type
        if stages is not None:
            self.stages = stages
        if is_latest is not None:
            self.is_latest = is_latest
        if trigger_user is not None:
            self.trigger_user = trigger_user
        if all_job_finished is not None:
            self.all_job_finished = all_job_finished

    @property
    def id(self):
        r"""Gets the id of this PipelineDetailDto.

        流水线ID

        :return: The id of this PipelineDetailDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PipelineDetailDto.

        流水线ID

        :param id: The id of this PipelineDetailDto.
        :type id: int
        """
        self._id = id

    @property
    def web_url(self):
        r"""Gets the web_url of this PipelineDetailDto.

        流水线链接

        :return: The web_url of this PipelineDetailDto.
        :rtype: str
        """
        return self._web_url

    @web_url.setter
    def web_url(self, web_url):
        r"""Sets the web_url of this PipelineDetailDto.

        流水线链接

        :param web_url: The web_url of this PipelineDetailDto.
        :type web_url: str
        """
        self._web_url = web_url

    @property
    def sha(self):
        r"""Gets the sha of this PipelineDetailDto.

        commit id

        :return: The sha of this PipelineDetailDto.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this PipelineDetailDto.

        commit id

        :param sha: The sha of this PipelineDetailDto.
        :type sha: str
        """
        self._sha = sha

    @property
    def ref(self):
        r"""Gets the ref of this PipelineDetailDto.

        分支

        :return: The ref of this PipelineDetailDto.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        r"""Sets the ref of this PipelineDetailDto.

        分支

        :param ref: The ref of this PipelineDetailDto.
        :type ref: str
        """
        self._ref = ref

    @property
    def status(self):
        r"""Gets the status of this PipelineDetailDto.

        流水线状态，pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :return: The status of this PipelineDetailDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PipelineDetailDto.

        流水线状态，pending为排队，running为运行中，success为成功，failed为失败，canceled为取消，skipped为跳过，timedout为超时

        :param status: The status of this PipelineDetailDto.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this PipelineDetailDto.

        流水线创建时间

        :return: The created_at of this PipelineDetailDto.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this PipelineDetailDto.

        流水线创建时间

        :param created_at: The created_at of this PipelineDetailDto.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this PipelineDetailDto.

        流水线更新时间

        :return: The updated_at of this PipelineDetailDto.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this PipelineDetailDto.

        流水线更新时间

        :param updated_at: The updated_at of this PipelineDetailDto.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def started_at(self):
        r"""Gets the started_at of this PipelineDetailDto.

        流水线开始时间

        :return: The started_at of this PipelineDetailDto.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        r"""Sets the started_at of this PipelineDetailDto.

        流水线开始时间

        :param started_at: The started_at of this PipelineDetailDto.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        r"""Gets the finished_at of this PipelineDetailDto.

        流水线结束时间

        :return: The finished_at of this PipelineDetailDto.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        r"""Sets the finished_at of this PipelineDetailDto.

        流水线结束时间

        :param finished_at: The finished_at of this PipelineDetailDto.
        :type finished_at: str
        """
        self._finished_at = finished_at

    @property
    def repository_id(self):
        r"""Gets the repository_id of this PipelineDetailDto.

        仓库ID

        :return: The repository_id of this PipelineDetailDto.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this PipelineDetailDto.

        仓库ID

        :param repository_id: The repository_id of this PipelineDetailDto.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def is_invalid(self):
        r"""Gets the is_invalid of this PipelineDetailDto.

        流水线是否失效

        :return: The is_invalid of this PipelineDetailDto.
        :rtype: bool
        """
        return self._is_invalid

    @is_invalid.setter
    def is_invalid(self, is_invalid):
        r"""Sets the is_invalid of this PipelineDetailDto.

        流水线是否失效

        :param is_invalid: The is_invalid of this PipelineDetailDto.
        :type is_invalid: bool
        """
        self._is_invalid = is_invalid

    @property
    def type(self):
        r"""Gets the type of this PipelineDetailDto.

        流水线类型，MERGE REQUEST代表为合并请求触发的流水线

        :return: The type of this PipelineDetailDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PipelineDetailDto.

        流水线类型，MERGE REQUEST代表为合并请求触发的流水线

        :param type: The type of this PipelineDetailDto.
        :type type: str
        """
        self._type = type

    @property
    def stages(self):
        r"""Gets the stages of this PipelineDetailDto.

        :return: The stages of this PipelineDetailDto.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.PipelineStageDto`]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        r"""Sets the stages of this PipelineDetailDto.

        :param stages: The stages of this PipelineDetailDto.
        :type stages: list[:class:`huaweicloudsdkcodehub.v4.PipelineStageDto`]
        """
        self._stages = stages

    @property
    def is_latest(self):
        r"""Gets the is_latest of this PipelineDetailDto.

        是否是最近一条流水线

        :return: The is_latest of this PipelineDetailDto.
        :rtype: bool
        """
        return self._is_latest

    @is_latest.setter
    def is_latest(self, is_latest):
        r"""Sets the is_latest of this PipelineDetailDto.

        是否是最近一条流水线

        :param is_latest: The is_latest of this PipelineDetailDto.
        :type is_latest: bool
        """
        self._is_latest = is_latest

    @property
    def trigger_user(self):
        r"""Gets the trigger_user of this PipelineDetailDto.

        触发的用户

        :return: The trigger_user of this PipelineDetailDto.
        :rtype: str
        """
        return self._trigger_user

    @trigger_user.setter
    def trigger_user(self, trigger_user):
        r"""Sets the trigger_user of this PipelineDetailDto.

        触发的用户

        :param trigger_user: The trigger_user of this PipelineDetailDto.
        :type trigger_user: str
        """
        self._trigger_user = trigger_user

    @property
    def all_job_finished(self):
        r"""Gets the all_job_finished of this PipelineDetailDto.

        是否所有job都运行完成

        :return: The all_job_finished of this PipelineDetailDto.
        :rtype: bool
        """
        return self._all_job_finished

    @all_job_finished.setter
    def all_job_finished(self, all_job_finished):
        r"""Sets the all_job_finished of this PipelineDetailDto.

        是否所有job都运行完成

        :param all_job_finished: The all_job_finished of this PipelineDetailDto.
        :type all_job_finished: bool
        """
        self._all_job_finished = all_job_finished

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
        if not isinstance(other, PipelineDetailDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
