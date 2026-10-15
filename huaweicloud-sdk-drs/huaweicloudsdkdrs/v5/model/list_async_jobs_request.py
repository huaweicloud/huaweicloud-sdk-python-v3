# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAsyncJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'async_job_id': 'str',
        'status': 'str',
        'domain_name': 'str',
        'user_name': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'async_job_id': 'async_job_id',
        'status': 'status',
        'domain_name': 'domain_name',
        'user_name': 'user_name',
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, x_language=None, async_job_id=None, status=None, domain_name=None, user_name=None, offset=None, limit=None, sort_key=None, sort_dir=None):
        r"""ListAsyncJobsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us
        :type x_language: str
        :param async_job_id: **参数解释**：  批量异步创建的任务ID，用于按任务ID筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type async_job_id: str
        :param status: **参数解释**：  批量异步创建的任务状态，用于按任务状态筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  - ASYNC_JOB_VALIDATING：批量异步任务参数校验中 - ASYNC_JOB_VALIDATE_FAILED：批量异步任务参数校验失败 - AUTO_PARAM_VALIDATE_SUCCESS：批量异步任务参数校验成功 - COMMIT_SUCCESS：批量异步任务提交成功  **默认取值**：  不涉及
        :type status: str
        :param domain_name: **参数解释**：  批量异步创建任务的租户名，用于按租户名筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type domain_name: str
        :param user_name: **参数解释**：  批量异步创建任务的用户名，用于按用户名筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type user_name: str
        :param offset: **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0
        :type offset: int
        :param limit: **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及
        :type limit: int
        :param sort_key: **参数解释**：  返回结果按该关键字排序，指定批量异步任务列表的排序依据。  **约束限制**：  不涉及。  **取值范围**：  - create_time：按创建时间排序  **默认取值**：  create_time
        :type sort_key: str
        :param sort_dir: **参数解释**：  排序方向，指定返回结果按升序或降序排列。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序 - asc：升序  **默认取值**：  desc
        :type sort_dir: str
        """
        
        

        self._x_language = None
        self._async_job_id = None
        self._status = None
        self._domain_name = None
        self._user_name = None
        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if async_job_id is not None:
            self.async_job_id = async_job_id
        if status is not None:
            self.status = status
        if domain_name is not None:
            self.domain_name = domain_name
        if user_name is not None:
            self.user_name = user_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def x_language(self):
        r"""Gets the x_language of this ListAsyncJobsRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us

        :return: The x_language of this ListAsyncJobsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListAsyncJobsRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文 - zh-cn：中文  **默认取值**：  en-us

        :param x_language: The x_language of this ListAsyncJobsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def async_job_id(self):
        r"""Gets the async_job_id of this ListAsyncJobsRequest.

        **参数解释**：  批量异步创建的任务ID，用于按任务ID筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The async_job_id of this ListAsyncJobsRequest.
        :rtype: str
        """
        return self._async_job_id

    @async_job_id.setter
    def async_job_id(self, async_job_id):
        r"""Sets the async_job_id of this ListAsyncJobsRequest.

        **参数解释**：  批量异步创建的任务ID，用于按任务ID筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param async_job_id: The async_job_id of this ListAsyncJobsRequest.
        :type async_job_id: str
        """
        self._async_job_id = async_job_id

    @property
    def status(self):
        r"""Gets the status of this ListAsyncJobsRequest.

        **参数解释**：  批量异步创建的任务状态，用于按任务状态筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  - ASYNC_JOB_VALIDATING：批量异步任务参数校验中 - ASYNC_JOB_VALIDATE_FAILED：批量异步任务参数校验失败 - AUTO_PARAM_VALIDATE_SUCCESS：批量异步任务参数校验成功 - COMMIT_SUCCESS：批量异步任务提交成功  **默认取值**：  不涉及

        :return: The status of this ListAsyncJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAsyncJobsRequest.

        **参数解释**：  批量异步创建的任务状态，用于按任务状态筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  - ASYNC_JOB_VALIDATING：批量异步任务参数校验中 - ASYNC_JOB_VALIDATE_FAILED：批量异步任务参数校验失败 - AUTO_PARAM_VALIDATE_SUCCESS：批量异步任务参数校验成功 - COMMIT_SUCCESS：批量异步任务提交成功  **默认取值**：  不涉及

        :param status: The status of this ListAsyncJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListAsyncJobsRequest.

        **参数解释**：  批量异步创建任务的租户名，用于按租户名筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The domain_name of this ListAsyncJobsRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListAsyncJobsRequest.

        **参数解释**：  批量异步创建任务的租户名，用于按租户名筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param domain_name: The domain_name of this ListAsyncJobsRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def user_name(self):
        r"""Gets the user_name of this ListAsyncJobsRequest.

        **参数解释**：  批量异步创建任务的用户名，用于按用户名筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The user_name of this ListAsyncJobsRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ListAsyncJobsRequest.

        **参数解释**：  批量异步创建任务的用户名，用于按用户名筛选查询结果。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param user_name: The user_name of this ListAsyncJobsRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def offset(self):
        r"""Gets the offset of this ListAsyncJobsRequest.

        **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0

        :return: The offset of this ListAsyncJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAsyncJobsRequest.

        **参数解释**：  偏移量，表示查询该偏移量后面的记录，用于分页查询。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  0

        :param offset: The offset of this ListAsyncJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAsyncJobsRequest.

        **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :return: The limit of this ListAsyncJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAsyncJobsRequest.

        **参数解释**：  查询返回记录的数量限制，用于分页查询时控制每页返回的数据条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及

        :param limit: The limit of this ListAsyncJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListAsyncJobsRequest.

        **参数解释**：  返回结果按该关键字排序，指定批量异步任务列表的排序依据。  **约束限制**：  不涉及。  **取值范围**：  - create_time：按创建时间排序  **默认取值**：  create_time

        :return: The sort_key of this ListAsyncJobsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListAsyncJobsRequest.

        **参数解释**：  返回结果按该关键字排序，指定批量异步任务列表的排序依据。  **约束限制**：  不涉及。  **取值范围**：  - create_time：按创建时间排序  **默认取值**：  create_time

        :param sort_key: The sort_key of this ListAsyncJobsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListAsyncJobsRequest.

        **参数解释**：  排序方向，指定返回结果按升序或降序排列。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序 - asc：升序  **默认取值**：  desc

        :return: The sort_dir of this ListAsyncJobsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListAsyncJobsRequest.

        **参数解释**：  排序方向，指定返回结果按升序或降序排列。  **约束限制**：  不涉及。  **取值范围**：  - desc：降序 - asc：升序  **默认取值**：  desc

        :param sort_dir: The sort_dir of this ListAsyncJobsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAsyncJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
