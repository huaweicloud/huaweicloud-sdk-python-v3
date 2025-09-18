# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelineSimpleInfoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_name': 'str',
        'project_ids': 'str',
        'creator_ids': 'str',
        'executor_ids': 'str',
        'status': 'str',
        'outcome': 'str',
        'sort_key': 'str',
        'sort_dir': 'str',
        'git_url': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'pipeline_name': 'pipeline_name',
        'project_ids': 'project_ids',
        'creator_ids': 'creator_ids',
        'executor_ids': 'executor_ids',
        'status': 'status',
        'outcome': 'outcome',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'git_url': 'git_url',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, pipeline_name=None, project_ids=None, creator_ids=None, executor_ids=None, status=None, outcome=None, sort_key=None, sort_dir=None, git_url=None, offset=None, limit=None):
        r"""ListPipelineSimpleInfoRequestBody

        The model defined in huaweicloud sdk

        :param pipeline_name: **参数解释**： 流水线名字。查询时进行模糊匹配。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type pipeline_name: str
        :param project_ids: **参数解释**： 项目id，有多个值时用逗号分隔，id个数取值[0,10]，非必选。如果该参数有值，则获取对应项目下的流水线列表；如果没有值，则获取用户有权限的所有项目的流水线列表 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type project_ids: str
        :param creator_ids: **参数解释**： 创建人id，有多个值时用逗号分隔，id个数取值[0,10]，非必选 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type creator_ids: str
        :param executor_ids: **参数解释**： 执行人id。有多个值时用逗号分隔，id个数取值[0,10]，非必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type executor_ids: str
        :param status: **参数解释**： 流水线运行状态。 **约束限制**： 不涉及。 **取值范围**： - waiting：等待中。 - running：运行中。 - verifying：待审核。 - suspending：挂起。 - completed：执行完成。 **默认取值**： 不涉及。 
        :type status: str
        :param outcome: **参数解释**： 流水线执行结果。 **约束限制**： 不涉及。 **取值范围**： - success：成功。 - error：失败。 - aborted：终止。 **默认取值**： 不涉及。 
        :type outcome: str
        :param sort_key: **参数解释**： 用于排序的字段，非必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type sort_key: str
        :param sort_dir: **参数解释**： 排序方式。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 
        :type sort_dir: str
        :param git_url: **参数解释**： 代码仓地址。仅支持codehub仓库，如：git@codehub.XXX.git **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type git_url: str
        :param offset: **参数解释**： 偏移量。表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： offset大于等于0。 **默认取值**： 不涉及。 
        :type offset: int
        :param limit: **参数解释**： 每次查询的条目数量。 **约束限制**： 不涉及。 **取值范围**： 取值[10-50]。 **默认取值**： 10。 
        :type limit: int
        """
        
        

        self._pipeline_name = None
        self._project_ids = None
        self._creator_ids = None
        self._executor_ids = None
        self._status = None
        self._outcome = None
        self._sort_key = None
        self._sort_dir = None
        self._git_url = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if pipeline_name is not None:
            self.pipeline_name = pipeline_name
        if project_ids is not None:
            self.project_ids = project_ids
        if creator_ids is not None:
            self.creator_ids = creator_ids
        if executor_ids is not None:
            self.executor_ids = executor_ids
        if status is not None:
            self.status = status
        if outcome is not None:
            self.outcome = outcome
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if git_url is not None:
            self.git_url = git_url
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def pipeline_name(self):
        r"""Gets the pipeline_name of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 流水线名字。查询时进行模糊匹配。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The pipeline_name of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        r"""Sets the pipeline_name of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 流水线名字。查询时进行模糊匹配。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param pipeline_name: The pipeline_name of this ListPipelineSimpleInfoRequestBody.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

    @property
    def project_ids(self):
        r"""Gets the project_ids of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 项目id，有多个值时用逗号分隔，id个数取值[0,10]，非必选。如果该参数有值，则获取对应项目下的流水线列表；如果没有值，则获取用户有权限的所有项目的流水线列表 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The project_ids of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        r"""Sets the project_ids of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 项目id，有多个值时用逗号分隔，id个数取值[0,10]，非必选。如果该参数有值，则获取对应项目下的流水线列表；如果没有值，则获取用户有权限的所有项目的流水线列表 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param project_ids: The project_ids of this ListPipelineSimpleInfoRequestBody.
        :type project_ids: str
        """
        self._project_ids = project_ids

    @property
    def creator_ids(self):
        r"""Gets the creator_ids of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 创建人id，有多个值时用逗号分隔，id个数取值[0,10]，非必选 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The creator_ids of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._creator_ids

    @creator_ids.setter
    def creator_ids(self, creator_ids):
        r"""Sets the creator_ids of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 创建人id，有多个值时用逗号分隔，id个数取值[0,10]，非必选 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param creator_ids: The creator_ids of this ListPipelineSimpleInfoRequestBody.
        :type creator_ids: str
        """
        self._creator_ids = creator_ids

    @property
    def executor_ids(self):
        r"""Gets the executor_ids of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 执行人id。有多个值时用逗号分隔，id个数取值[0,10]，非必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The executor_ids of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._executor_ids

    @executor_ids.setter
    def executor_ids(self, executor_ids):
        r"""Sets the executor_ids of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 执行人id。有多个值时用逗号分隔，id个数取值[0,10]，非必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param executor_ids: The executor_ids of this ListPipelineSimpleInfoRequestBody.
        :type executor_ids: str
        """
        self._executor_ids = executor_ids

    @property
    def status(self):
        r"""Gets the status of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 流水线运行状态。 **约束限制**： 不涉及。 **取值范围**： - waiting：等待中。 - running：运行中。 - verifying：待审核。 - suspending：挂起。 - completed：执行完成。 **默认取值**： 不涉及。 

        :return: The status of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 流水线运行状态。 **约束限制**： 不涉及。 **取值范围**： - waiting：等待中。 - running：运行中。 - verifying：待审核。 - suspending：挂起。 - completed：执行完成。 **默认取值**： 不涉及。 

        :param status: The status of this ListPipelineSimpleInfoRequestBody.
        :type status: str
        """
        self._status = status

    @property
    def outcome(self):
        r"""Gets the outcome of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 流水线执行结果。 **约束限制**： 不涉及。 **取值范围**： - success：成功。 - error：失败。 - aborted：终止。 **默认取值**： 不涉及。 

        :return: The outcome of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        r"""Sets the outcome of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 流水线执行结果。 **约束限制**： 不涉及。 **取值范围**： - success：成功。 - error：失败。 - aborted：终止。 **默认取值**： 不涉及。 

        :param outcome: The outcome of this ListPipelineSimpleInfoRequestBody.
        :type outcome: str
        """
        self._outcome = outcome

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 用于排序的字段，非必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The sort_key of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 用于排序的字段，非必选。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param sort_key: The sort_key of this ListPipelineSimpleInfoRequestBody.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 排序方式。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 

        :return: The sort_dir of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 排序方式。 **约束限制**： 不涉及。 **取值范围**： - asc：按排序字段升序。 - desc：按排序字段降序。 **默认取值**： 不涉及。 

        :param sort_dir: The sort_dir of this ListPipelineSimpleInfoRequestBody.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def git_url(self):
        r"""Gets the git_url of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 代码仓地址。仅支持codehub仓库，如：git@codehub.XXX.git **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The git_url of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        r"""Sets the git_url of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 代码仓地址。仅支持codehub仓库，如：git@codehub.XXX.git **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param git_url: The git_url of this ListPipelineSimpleInfoRequestBody.
        :type git_url: str
        """
        self._git_url = git_url

    @property
    def offset(self):
        r"""Gets the offset of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 偏移量。表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： offset大于等于0。 **默认取值**： 不涉及。 

        :return: The offset of this ListPipelineSimpleInfoRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 偏移量。表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： offset大于等于0。 **默认取值**： 不涉及。 

        :param offset: The offset of this ListPipelineSimpleInfoRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 每次查询的条目数量。 **约束限制**： 不涉及。 **取值范围**： 取值[10-50]。 **默认取值**： 10。 

        :return: The limit of this ListPipelineSimpleInfoRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPipelineSimpleInfoRequestBody.

        **参数解释**： 每次查询的条目数量。 **约束限制**： 不涉及。 **取值范围**： 取值[10-50]。 **默认取值**： 10。 

        :param limit: The limit of this ListPipelineSimpleInfoRequestBody.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListPipelineSimpleInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
