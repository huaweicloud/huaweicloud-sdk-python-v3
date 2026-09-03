# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSparkJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'name': 'str',
        'create_time_after': 'int',
        'create_time_before': 'int',
        'endpoint_name': 'str',
        'states': 'list[str]',
        'job_type': 'str',
        'job_id': 'str',
        'create_user_id': 'str',
        'create_user_name': 'str',
        'labels': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'name': 'name',
        'create_time_after': 'create_time_after',
        'create_time_before': 'create_time_before',
        'endpoint_name': 'endpoint_name',
        'states': 'states',
        'job_type': 'job_type',
        'job_id': 'job_id',
        'create_user_id': 'create_user_id',
        'create_user_name': 'create_user_name',
        'labels': 'labels'
    }

    def __init__(self, workspace_id=None, marker=None, limit=None, page_reverse=None, name=None, create_time_after=None, create_time_before=None, endpoint_name=None, states=None, job_type=None, job_id=None, create_user_id=None, create_user_name=None, labels=None):
        r"""ListSparkJobsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type workspace_id: str
        :param marker: **参数解释**：作业ID游标位置，用于分页查询。 **约束限制**：首次查询可不传或传空字符串，后续查询传入上次返回的next_marker值。 **取值范围**：采用UUID格式，长度为36个字符，只能由英文大写字母、英文小写字母、数字及下划线和横线组成。 **默认取值**：不涉及。
        :type marker: str
        :param limit: **参数解释**：查询记录数，用于分页查询。 **约束限制**：不涉及。 **取值范围**：1~100之间的整数。 **默认取值**：10。
        :type limit: int
        :param page_reverse: **参数解释**：是否反向分页查询。默认为false，表示正向分页查询。 当设置为true时，表示查询上一页数据，需要配合marker参数使用。
        :type page_reverse: bool
        :param name: **参数解释**：作业名称，用于模糊查询作业。 **约束限制**：不涉及。 **取值范围**：长度为0~128个字符。 **默认取值**：不涉及。
        :type name: str
        :param create_time_after: **参数解释**：用于查询创建时间在该时间点之后的作业。 **约束限制**：不涉及。 **取值范围**：unix时间戳，单位为毫秒，最小值为1764061598000。 **默认取值**：不涉及。
        :type create_time_after: int
        :param create_time_before: **参数解释**：用于查询创建时间在该时间点之前的作业。 **约束限制**：不涉及。 **取值范围**：unix时间戳，单位为毫秒，最小值为1764061598000。 **默认取值**：不涉及。
        :type create_time_before: int
        :param endpoint_name: **参数解释**：端点名称，用于指定Spark作业执行环境。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param states: **参数解释**：Spark作业状态列表，用于过滤查询指定状态的作业。 **约束限制**：最多支持查询10种状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - SUCCEED：运行成功。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。
        :type states: list[str]
        :param job_type: **参数解释**：作业类型，用于过滤查询指定类型的作业。 **约束限制**：不涉及。 **取值范围**： - spark_jar_job：Spark jar作业。 - spark_python_job：Python Spark作业。 - spark_sql_scripting_job：SQL脚本作业（预留类型）。 **默认取值**：不涉及。
        :type job_type: str
        :param job_id: **参数解释**：Spark作业ID，用于精确查询指定作业。 **约束限制**：不涉及。 **取值范围**：只能由英文大写字母、英文小写字母、数字及下划线和横线组成，且长度为1~64个字符。 **默认取值**：不涉及。
        :type job_id: str
        :param create_user_id: **参数解释**：Spark作业创建者ID，用于过滤查询指定用户创建的作业。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。
        :type create_user_id: str
        :param create_user_name: **参数解释**：Spark作业创建者名称,用于精确过滤查询指定用户创建的作业。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 
        :type create_user_name: str
        :param labels: **参数解释**：作业标签，用于按标签过滤查询作业。支持多标签过滤，格式为“key&#x3D;value”，多个标签用逗号分隔。 **约束限制**：URL中“&#x3D;”需要转义为“%3D”。例如：labels&#x3D;k1%3Dv1，k2%3Dv2。 **取值范围**：长度为1~1024个字符。 **默认取值**：不涉及。
        :type labels: str
        """
        
        

        self._workspace_id = None
        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._name = None
        self._create_time_after = None
        self._create_time_before = None
        self._endpoint_name = None
        self._states = None
        self._job_type = None
        self._job_id = None
        self._create_user_id = None
        self._create_user_name = None
        self._labels = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if name is not None:
            self.name = name
        if create_time_after is not None:
            self.create_time_after = create_time_after
        if create_time_before is not None:
            self.create_time_before = create_time_before
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if states is not None:
            self.states = states
        if job_type is not None:
            self.job_type = job_type
        if job_id is not None:
            self.job_id = job_id
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if create_user_name is not None:
            self.create_user_name = create_user_name
        if labels is not None:
            self.labels = labels

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListSparkJobsRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The workspace_id of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListSparkJobsRequest.

        **参数解释**：工作空间的ID。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListSparkJobsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def marker(self):
        r"""Gets the marker of this ListSparkJobsRequest.

        **参数解释**：作业ID游标位置，用于分页查询。 **约束限制**：首次查询可不传或传空字符串，后续查询传入上次返回的next_marker值。 **取值范围**：采用UUID格式，长度为36个字符，只能由英文大写字母、英文小写字母、数字及下划线和横线组成。 **默认取值**：不涉及。

        :return: The marker of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSparkJobsRequest.

        **参数解释**：作业ID游标位置，用于分页查询。 **约束限制**：首次查询可不传或传空字符串，后续查询传入上次返回的next_marker值。 **取值范围**：采用UUID格式，长度为36个字符，只能由英文大写字母、英文小写字母、数字及下划线和横线组成。 **默认取值**：不涉及。

        :param marker: The marker of this ListSparkJobsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListSparkJobsRequest.

        **参数解释**：查询记录数，用于分页查询。 **约束限制**：不涉及。 **取值范围**：1~100之间的整数。 **默认取值**：10。

        :return: The limit of this ListSparkJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSparkJobsRequest.

        **参数解释**：查询记录数，用于分页查询。 **约束限制**：不涉及。 **取值范围**：1~100之间的整数。 **默认取值**：10。

        :param limit: The limit of this ListSparkJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListSparkJobsRequest.

        **参数解释**：是否反向分页查询。默认为false，表示正向分页查询。 当设置为true时，表示查询上一页数据，需要配合marker参数使用。

        :return: The page_reverse of this ListSparkJobsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListSparkJobsRequest.

        **参数解释**：是否反向分页查询。默认为false，表示正向分页查询。 当设置为true时，表示查询上一页数据，需要配合marker参数使用。

        :param page_reverse: The page_reverse of this ListSparkJobsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def name(self):
        r"""Gets the name of this ListSparkJobsRequest.

        **参数解释**：作业名称，用于模糊查询作业。 **约束限制**：不涉及。 **取值范围**：长度为0~128个字符。 **默认取值**：不涉及。

        :return: The name of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSparkJobsRequest.

        **参数解释**：作业名称，用于模糊查询作业。 **约束限制**：不涉及。 **取值范围**：长度为0~128个字符。 **默认取值**：不涉及。

        :param name: The name of this ListSparkJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_time_after(self):
        r"""Gets the create_time_after of this ListSparkJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之后的作业。 **约束限制**：不涉及。 **取值范围**：unix时间戳，单位为毫秒，最小值为1764061598000。 **默认取值**：不涉及。

        :return: The create_time_after of this ListSparkJobsRequest.
        :rtype: int
        """
        return self._create_time_after

    @create_time_after.setter
    def create_time_after(self, create_time_after):
        r"""Sets the create_time_after of this ListSparkJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之后的作业。 **约束限制**：不涉及。 **取值范围**：unix时间戳，单位为毫秒，最小值为1764061598000。 **默认取值**：不涉及。

        :param create_time_after: The create_time_after of this ListSparkJobsRequest.
        :type create_time_after: int
        """
        self._create_time_after = create_time_after

    @property
    def create_time_before(self):
        r"""Gets the create_time_before of this ListSparkJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之前的作业。 **约束限制**：不涉及。 **取值范围**：unix时间戳，单位为毫秒，最小值为1764061598000。 **默认取值**：不涉及。

        :return: The create_time_before of this ListSparkJobsRequest.
        :rtype: int
        """
        return self._create_time_before

    @create_time_before.setter
    def create_time_before(self, create_time_before):
        r"""Sets the create_time_before of this ListSparkJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之前的作业。 **约束限制**：不涉及。 **取值范围**：unix时间戳，单位为毫秒，最小值为1764061598000。 **默认取值**：不涉及。

        :param create_time_before: The create_time_before of this ListSparkJobsRequest.
        :type create_time_before: int
        """
        self._create_time_before = create_time_before

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ListSparkJobsRequest.

        **参数解释**：端点名称，用于指定Spark作业执行环境。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。

        :return: The endpoint_name of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ListSparkJobsRequest.

        **参数解释**：端点名称，用于指定Spark作业执行环境。 **约束限制**：不涉及。 **取值范围**：只能由英文小写字母、数字及中划线组成，以英文小写字母开头，以英文小写字母或数字结尾，且长度为1~63个字符。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this ListSparkJobsRequest.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def states(self):
        r"""Gets the states of this ListSparkJobsRequest.

        **参数解释**：Spark作业状态列表，用于过滤查询指定状态的作业。 **约束限制**：最多支持查询10种状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - SUCCEED：运行成功。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。

        :return: The states of this ListSparkJobsRequest.
        :rtype: list[str]
        """
        return self._states

    @states.setter
    def states(self, states):
        r"""Sets the states of this ListSparkJobsRequest.

        **参数解释**：Spark作业状态列表，用于过滤查询指定状态的作业。 **约束限制**：最多支持查询10种状态。 **取值范围**： - PENDING：启动中。 - QUEUED：排队中。 - RUNNING：运行中。 - CANCELING：取消中。 - CANCELED：已取消。 - FAILED：运行失败。 - SUCCEED：运行成功。 - QUEUED_TIMEOUT：排队超时。 - RUNNING_TIMEOUT：运行超时。

        :param states: The states of this ListSparkJobsRequest.
        :type states: list[str]
        """
        self._states = states

    @property
    def job_type(self):
        r"""Gets the job_type of this ListSparkJobsRequest.

        **参数解释**：作业类型，用于过滤查询指定类型的作业。 **约束限制**：不涉及。 **取值范围**： - spark_jar_job：Spark jar作业。 - spark_python_job：Python Spark作业。 - spark_sql_scripting_job：SQL脚本作业（预留类型）。 **默认取值**：不涉及。

        :return: The job_type of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListSparkJobsRequest.

        **参数解释**：作业类型，用于过滤查询指定类型的作业。 **约束限制**：不涉及。 **取值范围**： - spark_jar_job：Spark jar作业。 - spark_python_job：Python Spark作业。 - spark_sql_scripting_job：SQL脚本作业（预留类型）。 **默认取值**：不涉及。

        :param job_type: The job_type of this ListSparkJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_id(self):
        r"""Gets the job_id of this ListSparkJobsRequest.

        **参数解释**：Spark作业ID，用于精确查询指定作业。 **约束限制**：不涉及。 **取值范围**：只能由英文大写字母、英文小写字母、数字及下划线和横线组成，且长度为1~64个字符。 **默认取值**：不涉及。

        :return: The job_id of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListSparkJobsRequest.

        **参数解释**：Spark作业ID，用于精确查询指定作业。 **约束限制**：不涉及。 **取值范围**：只能由英文大写字母、英文小写字母、数字及下划线和横线组成，且长度为1~64个字符。 **默认取值**：不涉及。

        :param job_id: The job_id of this ListSparkJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this ListSparkJobsRequest.

        **参数解释**：Spark作业创建者ID，用于过滤查询指定用户创建的作业。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。

        :return: The create_user_id of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this ListSparkJobsRequest.

        **参数解释**：Spark作业创建者ID，用于过滤查询指定用户创建的作业。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 **默认取值**：不涉及。

        :param create_user_id: The create_user_id of this ListSparkJobsRequest.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def create_user_name(self):
        r"""Gets the create_user_name of this ListSparkJobsRequest.

        **参数解释**：Spark作业创建者名称,用于精确过滤查询指定用户创建的作业。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 

        :return: The create_user_name of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._create_user_name

    @create_user_name.setter
    def create_user_name(self, create_user_name):
        r"""Sets the create_user_name of this ListSparkJobsRequest.

        **参数解释**：Spark作业创建者名称,用于精确过滤查询指定用户创建的作业。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符。 

        :param create_user_name: The create_user_name of this ListSparkJobsRequest.
        :type create_user_name: str
        """
        self._create_user_name = create_user_name

    @property
    def labels(self):
        r"""Gets the labels of this ListSparkJobsRequest.

        **参数解释**：作业标签，用于按标签过滤查询作业。支持多标签过滤，格式为“key=value”，多个标签用逗号分隔。 **约束限制**：URL中“=”需要转义为“%3D”。例如：labels=k1%3Dv1，k2%3Dv2。 **取值范围**：长度为1~1024个字符。 **默认取值**：不涉及。

        :return: The labels of this ListSparkJobsRequest.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListSparkJobsRequest.

        **参数解释**：作业标签，用于按标签过滤查询作业。支持多标签过滤，格式为“key=value”，多个标签用逗号分隔。 **约束限制**：URL中“=”需要转义为“%3D”。例如：labels=k1%3Dv1，k2%3Dv2。 **取值范围**：长度为1~1024个字符。 **默认取值**：不涉及。

        :param labels: The labels of this ListSparkJobsRequest.
        :type labels: str
        """
        self._labels = labels

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
        if not isinstance(other, ListSparkJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
