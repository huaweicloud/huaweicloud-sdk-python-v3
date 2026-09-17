# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsThirdPartyAgentSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agent_id': 'str',
        'agent_name': 'str',
        'type': 'str',
        'agent_type': 'str',
        'debug_status': 'str',
        'deleted': 'int',
        'create_time': 'str',
        'source': 'str',
        'name': 'str',
        'description': 'str',
        'total_token': 'int',
        'avg_request_count': 'float',
        'avg_duration_time': 'float',
        'avg_fail_count': 'float',
        'apm_app_id': 'str',
        'aom_prom_id': 'str',
        'lts_group_id': 'str',
        'lts_stream_id': 'str',
        'lts_label_name': 'str',
        'apm_exporter_endpoint': 'str',
        'aom_exporter_endpoint': 'str',
        'lts_exporter_endpoint': 'str',
        'api_config': 'OpsThirdPartyAgentApiConfig',
        'response_config': 'OpsThirdPartyAgentResponseConfig',
        'timeout': 'int'
    }

    attribute_map = {
        'agent_id': 'agent_id',
        'agent_name': 'agent_name',
        'type': 'type',
        'agent_type': 'agent_type',
        'debug_status': 'debug_status',
        'deleted': 'deleted',
        'create_time': 'create_time',
        'source': 'source',
        'name': 'name',
        'description': 'description',
        'total_token': 'total_token',
        'avg_request_count': 'avg_request_count',
        'avg_duration_time': 'avg_duration_time',
        'avg_fail_count': 'avg_fail_count',
        'apm_app_id': 'apm_app_id',
        'aom_prom_id': 'aom_prom_id',
        'lts_group_id': 'lts_group_id',
        'lts_stream_id': 'lts_stream_id',
        'lts_label_name': 'lts_label_name',
        'apm_exporter_endpoint': 'apm_exporter_endpoint',
        'aom_exporter_endpoint': 'aom_exporter_endpoint',
        'lts_exporter_endpoint': 'lts_exporter_endpoint',
        'api_config': 'api_config',
        'response_config': 'response_config',
        'timeout': 'timeout'
    }

    def __init__(self, agent_id=None, agent_name=None, type=None, agent_type=None, debug_status=None, deleted=None, create_time=None, source=None, name=None, description=None, total_token=None, avg_request_count=None, avg_duration_time=None, avg_fail_count=None, apm_app_id=None, aom_prom_id=None, lts_group_id=None, lts_stream_id=None, lts_label_name=None, apm_exporter_endpoint=None, aom_exporter_endpoint=None, lts_exporter_endpoint=None, api_config=None, response_config=None, timeout=None):
        r"""OpsThirdPartyAgentSummary

        The model defined in huaweicloud sdk

        :param agent_id: **参数解释：** 三方智能体/智能体运行时ID。 **取值范围：** 不涉及。
        :type agent_id: str
        :param agent_name: **参数解释：** 三方智能体/智能体运行时名称。 **取值范围：** 不涉及。
        :type agent_name: str
        :param type: **参数解释：** 调试对象类型。 **取值范围：** - third_party_agent：三方托管智能体 - agent_runtime：智能体运行时
        :type type: str
        :param agent_type: **参数解释：** 智能体类型。 **取值范围：** - workflow：工作流 - agent：智能体 - multiagents：多智能体
        :type agent_type: str
        :param debug_status: **参数解释：** 调试状态。 **取值范围：** - NOT_DEBUGGED：未配置 - SUCCESS：调试成功 - FAILED：调试失败
        :type debug_status: str
        :param deleted: **参数解释：** 三方智能体是否已在可观测服务中被删除。 **取值范围：** - 0：未删除 - 1：已删除，不可用于创建新的评估任务
        :type deleted: int
        :param create_time: **参数解释：** 配置创建时间。时间格式为yyyy-MM-ddTHH:mm:ssZ，示例：2024-01-01T12:00:00Z。
        :type create_time: str
        :param source: **参数解释：** 智能体来源。
        :type source: str
        :param name: **参数解释：** 智能体名称（可观测服务返回）。
        :type name: str
        :param description: **参数解释：** 三方智能体配置描述。
        :type description: str
        :param total_token: **参数解释：** 累计Token消耗。
        :type total_token: int
        :param avg_request_count: **参数解释：** 平均请求次数。
        :type avg_request_count: float
        :param avg_duration_time: **参数解释：** 平均响应耗时。
        :type avg_duration_time: float
        :param avg_fail_count: **参数解释：** 平均失败次数。
        :type avg_fail_count: float
        :param apm_app_id: **参数解释：** APM 应用ID。
        :type apm_app_id: str
        :param aom_prom_id: **参数解释：** AOM Prometheus ID。
        :type aom_prom_id: str
        :param lts_group_id: **参数解释：** LTS 日志组ID。
        :type lts_group_id: str
        :param lts_stream_id: **参数解释：** LTS 日志流ID。
        :type lts_stream_id: str
        :param lts_label_name: **参数解释：** LTS 标签名称。
        :type lts_label_name: str
        :param apm_exporter_endpoint: **参数解释：** APM Exporter 端点。
        :type apm_exporter_endpoint: str
        :param aom_exporter_endpoint: **参数解释：** AOM Exporter 端点。
        :type aom_exporter_endpoint: str
        :param lts_exporter_endpoint: **参数解释：** LTS Exporter 端点。
        :type lts_exporter_endpoint: str
        :param api_config: 
        :type api_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentApiConfig`
        :param response_config: 
        :type response_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentResponseConfig`
        :param timeout: **参数解释：** 单次调用超时时间（秒）。
        :type timeout: int
        """
        
        

        self._agent_id = None
        self._agent_name = None
        self._type = None
        self._agent_type = None
        self._debug_status = None
        self._deleted = None
        self._create_time = None
        self._source = None
        self._name = None
        self._description = None
        self._total_token = None
        self._avg_request_count = None
        self._avg_duration_time = None
        self._avg_fail_count = None
        self._apm_app_id = None
        self._aom_prom_id = None
        self._lts_group_id = None
        self._lts_stream_id = None
        self._lts_label_name = None
        self._apm_exporter_endpoint = None
        self._aom_exporter_endpoint = None
        self._lts_exporter_endpoint = None
        self._api_config = None
        self._response_config = None
        self._timeout = None
        self.discriminator = None

        if agent_id is not None:
            self.agent_id = agent_id
        if agent_name is not None:
            self.agent_name = agent_name
        if type is not None:
            self.type = type
        if agent_type is not None:
            self.agent_type = agent_type
        if debug_status is not None:
            self.debug_status = debug_status
        if deleted is not None:
            self.deleted = deleted
        if create_time is not None:
            self.create_time = create_time
        if source is not None:
            self.source = source
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if total_token is not None:
            self.total_token = total_token
        if avg_request_count is not None:
            self.avg_request_count = avg_request_count
        if avg_duration_time is not None:
            self.avg_duration_time = avg_duration_time
        if avg_fail_count is not None:
            self.avg_fail_count = avg_fail_count
        if apm_app_id is not None:
            self.apm_app_id = apm_app_id
        if aom_prom_id is not None:
            self.aom_prom_id = aom_prom_id
        if lts_group_id is not None:
            self.lts_group_id = lts_group_id
        if lts_stream_id is not None:
            self.lts_stream_id = lts_stream_id
        if lts_label_name is not None:
            self.lts_label_name = lts_label_name
        if apm_exporter_endpoint is not None:
            self.apm_exporter_endpoint = apm_exporter_endpoint
        if aom_exporter_endpoint is not None:
            self.aom_exporter_endpoint = aom_exporter_endpoint
        if lts_exporter_endpoint is not None:
            self.lts_exporter_endpoint = lts_exporter_endpoint
        if api_config is not None:
            self.api_config = api_config
        if response_config is not None:
            self.response_config = response_config
        if timeout is not None:
            self.timeout = timeout

    @property
    def agent_id(self):
        r"""Gets the agent_id of this OpsThirdPartyAgentSummary.

        **参数解释：** 三方智能体/智能体运行时ID。 **取值范围：** 不涉及。

        :return: The agent_id of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this OpsThirdPartyAgentSummary.

        **参数解释：** 三方智能体/智能体运行时ID。 **取值范围：** 不涉及。

        :param agent_id: The agent_id of this OpsThirdPartyAgentSummary.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def agent_name(self):
        r"""Gets the agent_name of this OpsThirdPartyAgentSummary.

        **参数解释：** 三方智能体/智能体运行时名称。 **取值范围：** 不涉及。

        :return: The agent_name of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        r"""Sets the agent_name of this OpsThirdPartyAgentSummary.

        **参数解释：** 三方智能体/智能体运行时名称。 **取值范围：** 不涉及。

        :param agent_name: The agent_name of this OpsThirdPartyAgentSummary.
        :type agent_name: str
        """
        self._agent_name = agent_name

    @property
    def type(self):
        r"""Gets the type of this OpsThirdPartyAgentSummary.

        **参数解释：** 调试对象类型。 **取值范围：** - third_party_agent：三方托管智能体 - agent_runtime：智能体运行时

        :return: The type of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsThirdPartyAgentSummary.

        **参数解释：** 调试对象类型。 **取值范围：** - third_party_agent：三方托管智能体 - agent_runtime：智能体运行时

        :param type: The type of this OpsThirdPartyAgentSummary.
        :type type: str
        """
        self._type = type

    @property
    def agent_type(self):
        r"""Gets the agent_type of this OpsThirdPartyAgentSummary.

        **参数解释：** 智能体类型。 **取值范围：** - workflow：工作流 - agent：智能体 - multiagents：多智能体

        :return: The agent_type of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this OpsThirdPartyAgentSummary.

        **参数解释：** 智能体类型。 **取值范围：** - workflow：工作流 - agent：智能体 - multiagents：多智能体

        :param agent_type: The agent_type of this OpsThirdPartyAgentSummary.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def debug_status(self):
        r"""Gets the debug_status of this OpsThirdPartyAgentSummary.

        **参数解释：** 调试状态。 **取值范围：** - NOT_DEBUGGED：未配置 - SUCCESS：调试成功 - FAILED：调试失败

        :return: The debug_status of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._debug_status

    @debug_status.setter
    def debug_status(self, debug_status):
        r"""Sets the debug_status of this OpsThirdPartyAgentSummary.

        **参数解释：** 调试状态。 **取值范围：** - NOT_DEBUGGED：未配置 - SUCCESS：调试成功 - FAILED：调试失败

        :param debug_status: The debug_status of this OpsThirdPartyAgentSummary.
        :type debug_status: str
        """
        self._debug_status = debug_status

    @property
    def deleted(self):
        r"""Gets the deleted of this OpsThirdPartyAgentSummary.

        **参数解释：** 三方智能体是否已在可观测服务中被删除。 **取值范围：** - 0：未删除 - 1：已删除，不可用于创建新的评估任务

        :return: The deleted of this OpsThirdPartyAgentSummary.
        :rtype: int
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this OpsThirdPartyAgentSummary.

        **参数解释：** 三方智能体是否已在可观测服务中被删除。 **取值范围：** - 0：未删除 - 1：已删除，不可用于创建新的评估任务

        :param deleted: The deleted of this OpsThirdPartyAgentSummary.
        :type deleted: int
        """
        self._deleted = deleted

    @property
    def create_time(self):
        r"""Gets the create_time of this OpsThirdPartyAgentSummary.

        **参数解释：** 配置创建时间。时间格式为yyyy-MM-ddTHH:mm:ssZ，示例：2024-01-01T12:00:00Z。

        :return: The create_time of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this OpsThirdPartyAgentSummary.

        **参数解释：** 配置创建时间。时间格式为yyyy-MM-ddTHH:mm:ssZ，示例：2024-01-01T12:00:00Z。

        :param create_time: The create_time of this OpsThirdPartyAgentSummary.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def source(self):
        r"""Gets the source of this OpsThirdPartyAgentSummary.

        **参数解释：** 智能体来源。

        :return: The source of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this OpsThirdPartyAgentSummary.

        **参数解释：** 智能体来源。

        :param source: The source of this OpsThirdPartyAgentSummary.
        :type source: str
        """
        self._source = source

    @property
    def name(self):
        r"""Gets the name of this OpsThirdPartyAgentSummary.

        **参数解释：** 智能体名称（可观测服务返回）。

        :return: The name of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OpsThirdPartyAgentSummary.

        **参数解释：** 智能体名称（可观测服务返回）。

        :param name: The name of this OpsThirdPartyAgentSummary.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this OpsThirdPartyAgentSummary.

        **参数解释：** 三方智能体配置描述。

        :return: The description of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this OpsThirdPartyAgentSummary.

        **参数解释：** 三方智能体配置描述。

        :param description: The description of this OpsThirdPartyAgentSummary.
        :type description: str
        """
        self._description = description

    @property
    def total_token(self):
        r"""Gets the total_token of this OpsThirdPartyAgentSummary.

        **参数解释：** 累计Token消耗。

        :return: The total_token of this OpsThirdPartyAgentSummary.
        :rtype: int
        """
        return self._total_token

    @total_token.setter
    def total_token(self, total_token):
        r"""Sets the total_token of this OpsThirdPartyAgentSummary.

        **参数解释：** 累计Token消耗。

        :param total_token: The total_token of this OpsThirdPartyAgentSummary.
        :type total_token: int
        """
        self._total_token = total_token

    @property
    def avg_request_count(self):
        r"""Gets the avg_request_count of this OpsThirdPartyAgentSummary.

        **参数解释：** 平均请求次数。

        :return: The avg_request_count of this OpsThirdPartyAgentSummary.
        :rtype: float
        """
        return self._avg_request_count

    @avg_request_count.setter
    def avg_request_count(self, avg_request_count):
        r"""Sets the avg_request_count of this OpsThirdPartyAgentSummary.

        **参数解释：** 平均请求次数。

        :param avg_request_count: The avg_request_count of this OpsThirdPartyAgentSummary.
        :type avg_request_count: float
        """
        self._avg_request_count = avg_request_count

    @property
    def avg_duration_time(self):
        r"""Gets the avg_duration_time of this OpsThirdPartyAgentSummary.

        **参数解释：** 平均响应耗时。

        :return: The avg_duration_time of this OpsThirdPartyAgentSummary.
        :rtype: float
        """
        return self._avg_duration_time

    @avg_duration_time.setter
    def avg_duration_time(self, avg_duration_time):
        r"""Sets the avg_duration_time of this OpsThirdPartyAgentSummary.

        **参数解释：** 平均响应耗时。

        :param avg_duration_time: The avg_duration_time of this OpsThirdPartyAgentSummary.
        :type avg_duration_time: float
        """
        self._avg_duration_time = avg_duration_time

    @property
    def avg_fail_count(self):
        r"""Gets the avg_fail_count of this OpsThirdPartyAgentSummary.

        **参数解释：** 平均失败次数。

        :return: The avg_fail_count of this OpsThirdPartyAgentSummary.
        :rtype: float
        """
        return self._avg_fail_count

    @avg_fail_count.setter
    def avg_fail_count(self, avg_fail_count):
        r"""Sets the avg_fail_count of this OpsThirdPartyAgentSummary.

        **参数解释：** 平均失败次数。

        :param avg_fail_count: The avg_fail_count of this OpsThirdPartyAgentSummary.
        :type avg_fail_count: float
        """
        self._avg_fail_count = avg_fail_count

    @property
    def apm_app_id(self):
        r"""Gets the apm_app_id of this OpsThirdPartyAgentSummary.

        **参数解释：** APM 应用ID。

        :return: The apm_app_id of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._apm_app_id

    @apm_app_id.setter
    def apm_app_id(self, apm_app_id):
        r"""Sets the apm_app_id of this OpsThirdPartyAgentSummary.

        **参数解释：** APM 应用ID。

        :param apm_app_id: The apm_app_id of this OpsThirdPartyAgentSummary.
        :type apm_app_id: str
        """
        self._apm_app_id = apm_app_id

    @property
    def aom_prom_id(self):
        r"""Gets the aom_prom_id of this OpsThirdPartyAgentSummary.

        **参数解释：** AOM Prometheus ID。

        :return: The aom_prom_id of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._aom_prom_id

    @aom_prom_id.setter
    def aom_prom_id(self, aom_prom_id):
        r"""Sets the aom_prom_id of this OpsThirdPartyAgentSummary.

        **参数解释：** AOM Prometheus ID。

        :param aom_prom_id: The aom_prom_id of this OpsThirdPartyAgentSummary.
        :type aom_prom_id: str
        """
        self._aom_prom_id = aom_prom_id

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this OpsThirdPartyAgentSummary.

        **参数解释：** LTS 日志组ID。

        :return: The lts_group_id of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this OpsThirdPartyAgentSummary.

        **参数解释：** LTS 日志组ID。

        :param lts_group_id: The lts_group_id of this OpsThirdPartyAgentSummary.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_stream_id(self):
        r"""Gets the lts_stream_id of this OpsThirdPartyAgentSummary.

        **参数解释：** LTS 日志流ID。

        :return: The lts_stream_id of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._lts_stream_id

    @lts_stream_id.setter
    def lts_stream_id(self, lts_stream_id):
        r"""Sets the lts_stream_id of this OpsThirdPartyAgentSummary.

        **参数解释：** LTS 日志流ID。

        :param lts_stream_id: The lts_stream_id of this OpsThirdPartyAgentSummary.
        :type lts_stream_id: str
        """
        self._lts_stream_id = lts_stream_id

    @property
    def lts_label_name(self):
        r"""Gets the lts_label_name of this OpsThirdPartyAgentSummary.

        **参数解释：** LTS 标签名称。

        :return: The lts_label_name of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._lts_label_name

    @lts_label_name.setter
    def lts_label_name(self, lts_label_name):
        r"""Sets the lts_label_name of this OpsThirdPartyAgentSummary.

        **参数解释：** LTS 标签名称。

        :param lts_label_name: The lts_label_name of this OpsThirdPartyAgentSummary.
        :type lts_label_name: str
        """
        self._lts_label_name = lts_label_name

    @property
    def apm_exporter_endpoint(self):
        r"""Gets the apm_exporter_endpoint of this OpsThirdPartyAgentSummary.

        **参数解释：** APM Exporter 端点。

        :return: The apm_exporter_endpoint of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._apm_exporter_endpoint

    @apm_exporter_endpoint.setter
    def apm_exporter_endpoint(self, apm_exporter_endpoint):
        r"""Sets the apm_exporter_endpoint of this OpsThirdPartyAgentSummary.

        **参数解释：** APM Exporter 端点。

        :param apm_exporter_endpoint: The apm_exporter_endpoint of this OpsThirdPartyAgentSummary.
        :type apm_exporter_endpoint: str
        """
        self._apm_exporter_endpoint = apm_exporter_endpoint

    @property
    def aom_exporter_endpoint(self):
        r"""Gets the aom_exporter_endpoint of this OpsThirdPartyAgentSummary.

        **参数解释：** AOM Exporter 端点。

        :return: The aom_exporter_endpoint of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._aom_exporter_endpoint

    @aom_exporter_endpoint.setter
    def aom_exporter_endpoint(self, aom_exporter_endpoint):
        r"""Sets the aom_exporter_endpoint of this OpsThirdPartyAgentSummary.

        **参数解释：** AOM Exporter 端点。

        :param aom_exporter_endpoint: The aom_exporter_endpoint of this OpsThirdPartyAgentSummary.
        :type aom_exporter_endpoint: str
        """
        self._aom_exporter_endpoint = aom_exporter_endpoint

    @property
    def lts_exporter_endpoint(self):
        r"""Gets the lts_exporter_endpoint of this OpsThirdPartyAgentSummary.

        **参数解释：** LTS Exporter 端点。

        :return: The lts_exporter_endpoint of this OpsThirdPartyAgentSummary.
        :rtype: str
        """
        return self._lts_exporter_endpoint

    @lts_exporter_endpoint.setter
    def lts_exporter_endpoint(self, lts_exporter_endpoint):
        r"""Sets the lts_exporter_endpoint of this OpsThirdPartyAgentSummary.

        **参数解释：** LTS Exporter 端点。

        :param lts_exporter_endpoint: The lts_exporter_endpoint of this OpsThirdPartyAgentSummary.
        :type lts_exporter_endpoint: str
        """
        self._lts_exporter_endpoint = lts_exporter_endpoint

    @property
    def api_config(self):
        r"""Gets the api_config of this OpsThirdPartyAgentSummary.

        :return: The api_config of this OpsThirdPartyAgentSummary.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentApiConfig`
        """
        return self._api_config

    @api_config.setter
    def api_config(self, api_config):
        r"""Sets the api_config of this OpsThirdPartyAgentSummary.

        :param api_config: The api_config of this OpsThirdPartyAgentSummary.
        :type api_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentApiConfig`
        """
        self._api_config = api_config

    @property
    def response_config(self):
        r"""Gets the response_config of this OpsThirdPartyAgentSummary.

        :return: The response_config of this OpsThirdPartyAgentSummary.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentResponseConfig`
        """
        return self._response_config

    @response_config.setter
    def response_config(self, response_config):
        r"""Sets the response_config of this OpsThirdPartyAgentSummary.

        :param response_config: The response_config of this OpsThirdPartyAgentSummary.
        :type response_config: :class:`huaweicloudsdkagentarts.v1.OpsThirdPartyAgentResponseConfig`
        """
        self._response_config = response_config

    @property
    def timeout(self):
        r"""Gets the timeout of this OpsThirdPartyAgentSummary.

        **参数解释：** 单次调用超时时间（秒）。

        :return: The timeout of this OpsThirdPartyAgentSummary.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        r"""Sets the timeout of this OpsThirdPartyAgentSummary.

        **参数解释：** 单次调用超时时间（秒）。

        :param timeout: The timeout of this OpsThirdPartyAgentSummary.
        :type timeout: int
        """
        self._timeout = timeout

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
        if not isinstance(other, OpsThirdPartyAgentSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
