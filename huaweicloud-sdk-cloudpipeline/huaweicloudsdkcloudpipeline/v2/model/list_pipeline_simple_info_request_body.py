# coding: utf-8

import re
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
        """ListPipelineSimpleInfoRequestBody - a model defined in huaweicloud sdk"""
        
        

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
        """Gets the pipeline_name of this ListPipelineSimpleInfoRequestBody.

        流水线名字。参数存在，则进行模糊匹配

        :return: The pipeline_name of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        """Sets the pipeline_name of this ListPipelineSimpleInfoRequestBody.

        流水线名字。参数存在，则进行模糊匹配

        :param pipeline_name: The pipeline_name of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._pipeline_name = pipeline_name

    @property
    def project_ids(self):
        """Gets the project_ids of this ListPipelineSimpleInfoRequestBody.

        devCloud项目ids。该参数存在，则获取对应项目下的流水线列表，逗号分隔，id个数取值[0,10]；如果不存在，则获取调用方所属租户的流水线列表

        :return: The project_ids of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._project_ids

    @project_ids.setter
    def project_ids(self, project_ids):
        """Sets the project_ids of this ListPipelineSimpleInfoRequestBody.

        devCloud项目ids。该参数存在，则获取对应项目下的流水线列表，逗号分隔，id个数取值[0,10]；如果不存在，则获取调用方所属租户的流水线列表

        :param project_ids: The project_ids of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._project_ids = project_ids

    @property
    def creator_ids(self):
        """Gets the creator_ids of this ListPipelineSimpleInfoRequestBody.

        创建人id。该参数存在，逗号分隔，id个数取值[0,10]

        :return: The creator_ids of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._creator_ids

    @creator_ids.setter
    def creator_ids(self, creator_ids):
        """Sets the creator_ids of this ListPipelineSimpleInfoRequestBody.

        创建人id。该参数存在，逗号分隔，id个数取值[0,10]

        :param creator_ids: The creator_ids of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._creator_ids = creator_ids

    @property
    def executor_ids(self):
        """Gets the executor_ids of this ListPipelineSimpleInfoRequestBody.

        执行人id。该参数存在，逗号分隔，id个数取值[0,10]；

        :return: The executor_ids of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._executor_ids

    @executor_ids.setter
    def executor_ids(self, executor_ids):
        """Sets the executor_ids of this ListPipelineSimpleInfoRequestBody.

        执行人id。该参数存在，逗号分隔，id个数取值[0,10]；

        :param executor_ids: The executor_ids of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._executor_ids = executor_ids

    @property
    def status(self):
        """Gets the status of this ListPipelineSimpleInfoRequestBody.

        流水线运行状态。取值范围：waiting,running,verifying,handling,suspending,completed

        :return: The status of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPipelineSimpleInfoRequestBody.

        流水线运行状态。取值范围：waiting,running,verifying,handling,suspending,completed

        :param status: The status of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._status = status

    @property
    def outcome(self):
        """Gets the outcome of this ListPipelineSimpleInfoRequestBody.

        流水线结果，标记流水线。error、success、aborted

        :return: The outcome of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this ListPipelineSimpleInfoRequestBody.

        流水线结果，标记流水线。error、success、aborted

        :param outcome: The outcome of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._outcome = outcome

    @property
    def sort_key(self):
        """Gets the sort_key of this ListPipelineSimpleInfoRequestBody.

        用于排序的字段。取值为：pipeline_name,create_time,start_time

        :return: The sort_key of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this ListPipelineSimpleInfoRequestBody.

        用于排序的字段。取值为：pipeline_name,create_time,start_time

        :param sort_key: The sort_key of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this ListPipelineSimpleInfoRequestBody.

        排序类型。asc按排序字段升序，desc按排序字段降序

        :return: The sort_dir of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this ListPipelineSimpleInfoRequestBody.

        排序类型。asc按排序字段升序，desc按排序字段降序

        :param sort_dir: The sort_dir of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._sort_dir = sort_dir

    @property
    def git_url(self):
        """Gets the git_url of this ListPipelineSimpleInfoRequestBody.

        codehub搜索链接：git@codehub.XXX.git；gitee搜索链接：git@gitee.com.XXX.git；github搜索链接：git@github.com.XXX.git等

        :return: The git_url of this ListPipelineSimpleInfoRequestBody.
        :rtype: str
        """
        return self._git_url

    @git_url.setter
    def git_url(self, git_url):
        """Sets the git_url of this ListPipelineSimpleInfoRequestBody.

        codehub搜索链接：git@codehub.XXX.git；gitee搜索链接：git@gitee.com.XXX.git；github搜索链接：git@github.com.XXX.git等

        :param git_url: The git_url of this ListPipelineSimpleInfoRequestBody.
        :type: str
        """
        self._git_url = git_url

    @property
    def offset(self):
        """Gets the offset of this ListPipelineSimpleInfoRequestBody.

        偏移量。表示从此偏移量开始查询，offset大于等于0，默认取值为0

        :return: The offset of this ListPipelineSimpleInfoRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPipelineSimpleInfoRequestBody.

        偏移量。表示从此偏移量开始查询，offset大于等于0，默认取值为0

        :param offset: The offset of this ListPipelineSimpleInfoRequestBody.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPipelineSimpleInfoRequestBody.

        每次查询的条目数量。取值[10-50]，默认取值为10

        :return: The limit of this ListPipelineSimpleInfoRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPipelineSimpleInfoRequestBody.

        每次查询的条目数量。取值[10-50]，默认取值为10

        :param limit: The limit of this ListPipelineSimpleInfoRequestBody.
        :type: int
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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListPipelineSimpleInfoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other