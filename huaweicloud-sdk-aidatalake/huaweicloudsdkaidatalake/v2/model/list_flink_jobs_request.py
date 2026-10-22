# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkJobsRequest:

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
        'create_time_after': 'int',
        'create_time_before': 'int',
        'endpoint_id': 'str',
        'endpoint_name': 'str',
        'name': 'str',
        'job_id': 'str',
        'deployment_id': 'str',
        'state': 'list[FlinkJobState]',
        'job_type': 'str',
        'execution_mode': 'str',
        'create_user_id': 'str',
        'labels': 'list[str]'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'create_time_after': 'create_time_after',
        'create_time_before': 'create_time_before',
        'endpoint_id': 'endpoint_id',
        'endpoint_name': 'endpoint_name',
        'name': 'name',
        'job_id': 'job_id',
        'deployment_id': 'deployment_id',
        'state': 'state',
        'job_type': 'job_type',
        'execution_mode': 'execution_mode',
        'create_user_id': 'create_user_id',
        'labels': 'labels'
    }

    def __init__(self, workspace_id=None, marker=None, limit=None, page_reverse=None, create_time_after=None, create_time_before=None, endpoint_id=None, endpoint_name=None, name=None, job_id=None, deployment_id=None, state=None, job_type=None, execution_mode=None, create_user_id=None, labels=None):
        r"""ListFlinkJobsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type workspace_id: str
        :param marker: **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。
        :type marker: str
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。
        :type limit: int
        :param page_reverse: **参数解释**：分页查询方向，用于控制翻页方向。 **约束限制**：与marker参数配合使用。当page_reverse&#x3D;true时，必须传入marker参数，否则返回400错误。 **取值范围**：   - true：向前翻页（查询marker之前的数据）。   - false：向后翻页（查询marker之后的数据）。 **默认取值**：false。
        :type page_reverse: bool
        :param create_time_after: **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type create_time_after: int
        :param create_time_before: **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type create_time_before: int
        :param endpoint_id: **参数解释**：作业运行的端点ID，用于按端点筛选作业。 **约束限制**：不涉及。 **取值范围**：采用UUID格式，固定36个字符。 **默认取值**：不涉及。
        :type endpoint_id: str
        :param endpoint_name: **参数解释**：通过端点名称检索的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 
        :type endpoint_name: str
        :param name: **参数解释**：作业名称，用于按作业名称模糊筛选。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 **默认取值**：不涉及。
        :type name: str
        :param job_id: **参数解释**：Flink作业ID，用于按作业ID筛选，可通过[创建Flink作业](RunFlinkJob.xml)接口返回值获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。
        :type job_id: str
        :param deployment_id: **参数解释**：已部署作业ID，用于按部署ID筛选作业。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 **默认取值**：不涉及。
        :type deployment_id: str
        :param state: **参数解释**：Flink作业状态，用于按状态筛选作业列表。数组元素为FlinkJobState枚举，取值如下：   - CREATED：已创建。   - STARTING：启动中。   - RUNNING：运行中。   - CANCELLING：停止中。   - FAILED：已失败。   - CANCELLED：已停止。   - FINISHED：已完成。 **约束限制**：不涉及。
        :type state: list[:class:`huaweicloudsdkaidatalake.v2.FlinkJobState`]
        :param job_type: **参数解释**：作业类型，用于按作业类型筛选列表。 **约束限制**：不涉及。 **取值范围**：   - FLINK_SQL_JOB：SQL作业。   - FLINK_JAR_JOB：JAR作业。 **默认取值**：不涉及。
        :type job_type: str
        :param execution_mode: **参数解释**：执行模式，用于按执行模式筛选作业列表。 **约束限制**：不涉及。 **取值范围**：   - STREAMING：流模式。   - BATCH：批模式。 **默认取值**：不涉及。
        :type execution_mode: str
        :param create_user_id: **参数解释**：创建者用户ID（即IAM用户ID），用于按创建者筛选作业，获取方法请参见[获取账号ID](aidatalake_02_0030.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符，只能由英文字母和数字组成。 **默认取值**：不涉及。
        :type create_user_id: str
        :param labels: **参数解释**：标签过滤条件，用于按标签筛选作业。格式为key&#x3D;value，支持多个标签。 **约束限制**：最多10个标签。
        :type labels: list[str]
        """
        
        

        self._workspace_id = None
        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._create_time_after = None
        self._create_time_before = None
        self._endpoint_id = None
        self._endpoint_name = None
        self._name = None
        self._job_id = None
        self._deployment_id = None
        self._state = None
        self._job_type = None
        self._execution_mode = None
        self._create_user_id = None
        self._labels = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if create_time_after is not None:
            self.create_time_after = create_time_after
        if create_time_before is not None:
            self.create_time_before = create_time_before
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if endpoint_name is not None:
            self.endpoint_name = endpoint_name
        if name is not None:
            self.name = name
        if job_id is not None:
            self.job_id = job_id
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if state is not None:
            self.state = state
        if job_type is not None:
            self.job_type = job_type
        if execution_mode is not None:
            self.execution_mode = execution_mode
        if create_user_id is not None:
            self.create_user_id = create_user_id
        if labels is not None:
            self.labels = labels

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListFlinkJobsRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The workspace_id of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListFlinkJobsRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListFlinkJobsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def marker(self):
        r"""Gets the marker of this ListFlinkJobsRequest.

        **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :return: The marker of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFlinkJobsRequest.

        **参数解释**：上一页中最后一条记录id，查询第一页时传空值。 **约束限制**：不涉及。 **取值范围**：长度为1~36个字符，支持大小写英文字母、数字、连字符。 **默认取值**：不涉及。

        :param marker: The marker of this ListFlinkJobsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListFlinkJobsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :return: The limit of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlinkJobsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :param limit: The limit of this ListFlinkJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListFlinkJobsRequest.

        **参数解释**：分页查询方向，用于控制翻页方向。 **约束限制**：与marker参数配合使用。当page_reverse=true时，必须传入marker参数，否则返回400错误。 **取值范围**：   - true：向前翻页（查询marker之前的数据）。   - false：向后翻页（查询marker之后的数据）。 **默认取值**：false。

        :return: The page_reverse of this ListFlinkJobsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListFlinkJobsRequest.

        **参数解释**：分页查询方向，用于控制翻页方向。 **约束限制**：与marker参数配合使用。当page_reverse=true时，必须传入marker参数，否则返回400错误。 **取值范围**：   - true：向前翻页（查询marker之前的数据）。   - false：向后翻页（查询marker之后的数据）。 **默认取值**：false。

        :param page_reverse: The page_reverse of this ListFlinkJobsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def create_time_after(self):
        r"""Gets the create_time_after of this ListFlinkJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The create_time_after of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._create_time_after

    @create_time_after.setter
    def create_time_after(self, create_time_after):
        r"""Sets the create_time_after of this ListFlinkJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param create_time_after: The create_time_after of this ListFlinkJobsRequest.
        :type create_time_after: int
        """
        self._create_time_after = create_time_after

    @property
    def create_time_before(self):
        r"""Gets the create_time_before of this ListFlinkJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The create_time_before of this ListFlinkJobsRequest.
        :rtype: int
        """
        return self._create_time_before

    @create_time_before.setter
    def create_time_before(self, create_time_before):
        r"""Sets the create_time_before of this ListFlinkJobsRequest.

        **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param create_time_before: The create_time_before of this ListFlinkJobsRequest.
        :type create_time_before: int
        """
        self._create_time_before = create_time_before

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListFlinkJobsRequest.

        **参数解释**：作业运行的端点ID，用于按端点筛选作业。 **约束限制**：不涉及。 **取值范围**：采用UUID格式，固定36个字符。 **默认取值**：不涉及。

        :return: The endpoint_id of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListFlinkJobsRequest.

        **参数解释**：作业运行的端点ID，用于按端点筛选作业。 **约束限制**：不涉及。 **取值范围**：采用UUID格式，固定36个字符。 **默认取值**：不涉及。

        :param endpoint_id: The endpoint_id of this ListFlinkJobsRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this ListFlinkJobsRequest.

        **参数解释**：通过端点名称检索的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 

        :return: The endpoint_name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this ListFlinkJobsRequest.

        **参数解释**：通过端点名称检索的参数。 **约束限制**：不涉及。 **取值范围**：长度为1~64的中文、英文字母、数字、下划线、中划线、点号、空格的组合。 **默认取值**：不涉及。 

        :param endpoint_name: The endpoint_name of this ListFlinkJobsRequest.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def name(self):
        r"""Gets the name of this ListFlinkJobsRequest.

        **参数解释**：作业名称，用于按作业名称模糊筛选。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 **默认取值**：不涉及。

        :return: The name of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListFlinkJobsRequest.

        **参数解释**：作业名称，用于按作业名称模糊筛选。 **约束限制**：不涉及。 **取值范围**：长度为1~128个字符，以字母或数字开头和结尾，中间可包含字母、数字、下划线和中划线。 **默认取值**：不涉及。

        :param name: The name of this ListFlinkJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def job_id(self):
        r"""Gets the job_id of this ListFlinkJobsRequest.

        **参数解释**：Flink作业ID，用于按作业ID筛选，可通过[创建Flink作业](RunFlinkJob.xml)接口返回值获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :return: The job_id of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListFlinkJobsRequest.

        **参数解释**：Flink作业ID，用于按作业ID筛选，可通过[创建Flink作业](RunFlinkJob.xml)接口返回值获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :param job_id: The job_id of this ListFlinkJobsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def deployment_id(self):
        r"""Gets the deployment_id of this ListFlinkJobsRequest.

        **参数解释**：已部署作业ID，用于按部署ID筛选作业。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 **默认取值**：不涉及。

        :return: The deployment_id of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        r"""Sets the deployment_id of this ListFlinkJobsRequest.

        **参数解释**：已部署作业ID，用于按部署ID筛选作业。 **约束限制**：不涉及。 **取值范围**：长度为1~64个字符，只能由英文字母、数字、下划线和中划线组成。 **默认取值**：不涉及。

        :param deployment_id: The deployment_id of this ListFlinkJobsRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def state(self):
        r"""Gets the state of this ListFlinkJobsRequest.

        **参数解释**：Flink作业状态，用于按状态筛选作业列表。数组元素为FlinkJobState枚举，取值如下：   - CREATED：已创建。   - STARTING：启动中。   - RUNNING：运行中。   - CANCELLING：停止中。   - FAILED：已失败。   - CANCELLED：已停止。   - FINISHED：已完成。 **约束限制**：不涉及。

        :return: The state of this ListFlinkJobsRequest.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.FlinkJobState`]
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListFlinkJobsRequest.

        **参数解释**：Flink作业状态，用于按状态筛选作业列表。数组元素为FlinkJobState枚举，取值如下：   - CREATED：已创建。   - STARTING：启动中。   - RUNNING：运行中。   - CANCELLING：停止中。   - FAILED：已失败。   - CANCELLED：已停止。   - FINISHED：已完成。 **约束限制**：不涉及。

        :param state: The state of this ListFlinkJobsRequest.
        :type state: list[:class:`huaweicloudsdkaidatalake.v2.FlinkJobState`]
        """
        self._state = state

    @property
    def job_type(self):
        r"""Gets the job_type of this ListFlinkJobsRequest.

        **参数解释**：作业类型，用于按作业类型筛选列表。 **约束限制**：不涉及。 **取值范围**：   - FLINK_SQL_JOB：SQL作业。   - FLINK_JAR_JOB：JAR作业。 **默认取值**：不涉及。

        :return: The job_type of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this ListFlinkJobsRequest.

        **参数解释**：作业类型，用于按作业类型筛选列表。 **约束限制**：不涉及。 **取值范围**：   - FLINK_SQL_JOB：SQL作业。   - FLINK_JAR_JOB：JAR作业。 **默认取值**：不涉及。

        :param job_type: The job_type of this ListFlinkJobsRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def execution_mode(self):
        r"""Gets the execution_mode of this ListFlinkJobsRequest.

        **参数解释**：执行模式，用于按执行模式筛选作业列表。 **约束限制**：不涉及。 **取值范围**：   - STREAMING：流模式。   - BATCH：批模式。 **默认取值**：不涉及。

        :return: The execution_mode of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        r"""Sets the execution_mode of this ListFlinkJobsRequest.

        **参数解释**：执行模式，用于按执行模式筛选作业列表。 **约束限制**：不涉及。 **取值范围**：   - STREAMING：流模式。   - BATCH：批模式。 **默认取值**：不涉及。

        :param execution_mode: The execution_mode of this ListFlinkJobsRequest.
        :type execution_mode: str
        """
        self._execution_mode = execution_mode

    @property
    def create_user_id(self):
        r"""Gets the create_user_id of this ListFlinkJobsRequest.

        **参数解释**：创建者用户ID（即IAM用户ID），用于按创建者筛选作业，获取方法请参见[获取账号ID](aidatalake_02_0030.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符，只能由英文字母和数字组成。 **默认取值**：不涉及。

        :return: The create_user_id of this ListFlinkJobsRequest.
        :rtype: str
        """
        return self._create_user_id

    @create_user_id.setter
    def create_user_id(self, create_user_id):
        r"""Sets the create_user_id of this ListFlinkJobsRequest.

        **参数解释**：创建者用户ID（即IAM用户ID），用于按创建者筛选作业，获取方法请参见[获取账号ID](aidatalake_02_0030.xml)。 **约束限制**：不涉及。 **取值范围**：长度为1~256个字符，只能由英文字母和数字组成。 **默认取值**：不涉及。

        :param create_user_id: The create_user_id of this ListFlinkJobsRequest.
        :type create_user_id: str
        """
        self._create_user_id = create_user_id

    @property
    def labels(self):
        r"""Gets the labels of this ListFlinkJobsRequest.

        **参数解释**：标签过滤条件，用于按标签筛选作业。格式为key=value，支持多个标签。 **约束限制**：最多10个标签。

        :return: The labels of this ListFlinkJobsRequest.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this ListFlinkJobsRequest.

        **参数解释**：标签过滤条件，用于按标签筛选作业。格式为key=value，支持多个标签。 **约束限制**：最多10个标签。

        :param labels: The labels of this ListFlinkJobsRequest.
        :type labels: list[str]
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
        if not isinstance(other, ListFlinkJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
