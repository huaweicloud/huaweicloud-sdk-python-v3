# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'agent_id': 'str',
        'name': 'str',
        'agent_type': 'str',
        'create_time': 'int',
        'total_token': 'float',
        'avg_request_count': 'float',
        'avg_duration_time': 'float',
        'avg_fail_count': 'float',
        'apm_app_id': 'str',
        'aom_prom_id': 'str',
        'apm_app_token': 'str',
        'aom_access_code': 'str',
        'lts_group_id': 'str',
        'lts_stream_id': 'str',
        'lts_label_name': 'str',
        'apm_exporter_endpoint': 'str',
        'aom_exporter_endpoint': 'str',
        'deleted': 'int'
    }

    attribute_map = {
        'source': 'source',
        'agent_id': 'agent_id',
        'name': 'name',
        'agent_type': 'agent_type',
        'create_time': 'create_time',
        'total_token': 'total_token',
        'avg_request_count': 'avg_request_count',
        'avg_duration_time': 'avg_duration_time',
        'avg_fail_count': 'avg_fail_count',
        'apm_app_id': 'apm_app_id',
        'aom_prom_id': 'aom_prom_id',
        'apm_app_token': 'apm_app_token',
        'aom_access_code': 'aom_access_code',
        'lts_group_id': 'lts_group_id',
        'lts_stream_id': 'lts_stream_id',
        'lts_label_name': 'lts_label_name',
        'apm_exporter_endpoint': 'apm_exporter_endpoint',
        'aom_exporter_endpoint': 'aom_exporter_endpoint',
        'deleted': 'deleted'
    }

    def __init__(self, source=None, agent_id=None, name=None, agent_type=None, create_time=None, total_token=None, avg_request_count=None, avg_duration_time=None, avg_fail_count=None, apm_app_id=None, aom_prom_id=None, apm_app_token=None, aom_access_code=None, lts_group_id=None, lts_stream_id=None, lts_label_name=None, apm_exporter_endpoint=None, aom_exporter_endpoint=None, deleted=None):
        r"""AgentInfo

        The model defined in huaweicloud sdk

        :param source: **参数解释**： 智能体来源。  **取值范围**：   - studio   - agentrun   - api 
        :type source: str
        :param agent_id: **参数解释**： 智能体ID。  **取值范围**： 不涉及。 
        :type agent_id: str
        :param name: **参数解释**： 智能体名称。  **取值范围**： 不涉及。 
        :type name: str
        :param agent_type: **参数解释**： 智能体类型。   **取值范围**：  - agent：单智能体。  - multiagents：多智能体。  - workflow：工作流。 
        :type agent_type: str
        :param create_time: **参数解释**： 创建时间。  **取值范围**： 不涉及。 
        :type create_time: int
        :param total_token: **参数解释**： 按照给定时间计算出tokens消耗。  **取值范围**： 不涉及。 
        :type total_token: float
        :param avg_request_count: **参数解释**： 平均请求次数 单位为分钟。  **取值范围**： 不涉及。 
        :type avg_request_count: float
        :param avg_duration_time: **参数解释**： 平均延迟时间 延迟时间总和除以次数。  **取值范围**： 不涉及。 
        :type avg_duration_time: float
        :param avg_fail_count: **参数解释**： 平均请求失败次数 单位为分钟。  **取值范围**： 不涉及。 
        :type avg_fail_count: float
        :param apm_app_id: **参数解释**： apm的app_id，非必填。  **取值范围**： 不涉及。 
        :type apm_app_id: str
        :param aom_prom_id: **参数解释**： aom的app_id，非必填。  **取值范围**： 不涉及。 
        :type aom_prom_id: str
        :param apm_app_token: **参数解释**： apm token，加密存储，非必填。  **取值范围**： 不涉及。 
        :type apm_app_token: str
        :param aom_access_code: **参数解释**： aom access_code，加密存储，非必填。  **取值范围**： 不涉及。 
        :type aom_access_code: str
        :param lts_group_id: **参数解释**： lts_group_id，非必填。  **取值范围**： 不涉及。 
        :type lts_group_id: str
        :param lts_stream_id: **参数解释**： lts_stream_id，非必填。  **取值范围**： 不涉及。 
        :type lts_stream_id: str
        :param lts_label_name: **参数解释**： 用于过滤lts日志标签。  **取值范围**： 不涉及。 
        :type lts_label_name: str
        :param apm_exporter_endpoint: **参数解释**： apm上报地址。  **取值范围**： 不涉及。 
        :type apm_exporter_endpoint: str
        :param aom_exporter_endpoint: **参数解释**： aom上报地址。  **取值范围**： 不涉及。 
        :type aom_exporter_endpoint: str
        :param deleted: **参数解释**： 是否被刪除。  **取值范围**： 不涉及。 
        :type deleted: int
        """
        
        

        self._source = None
        self._agent_id = None
        self._name = None
        self._agent_type = None
        self._create_time = None
        self._total_token = None
        self._avg_request_count = None
        self._avg_duration_time = None
        self._avg_fail_count = None
        self._apm_app_id = None
        self._aom_prom_id = None
        self._apm_app_token = None
        self._aom_access_code = None
        self._lts_group_id = None
        self._lts_stream_id = None
        self._lts_label_name = None
        self._apm_exporter_endpoint = None
        self._aom_exporter_endpoint = None
        self._deleted = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if agent_id is not None:
            self.agent_id = agent_id
        if name is not None:
            self.name = name
        if agent_type is not None:
            self.agent_type = agent_type
        if create_time is not None:
            self.create_time = create_time
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
        if apm_app_token is not None:
            self.apm_app_token = apm_app_token
        if aom_access_code is not None:
            self.aom_access_code = aom_access_code
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
        if deleted is not None:
            self.deleted = deleted

    @property
    def source(self):
        r"""Gets the source of this AgentInfo.

        **参数解释**： 智能体来源。  **取值范围**：   - studio   - agentrun   - api 

        :return: The source of this AgentInfo.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this AgentInfo.

        **参数解释**： 智能体来源。  **取值范围**：   - studio   - agentrun   - api 

        :param source: The source of this AgentInfo.
        :type source: str
        """
        self._source = source

    @property
    def agent_id(self):
        r"""Gets the agent_id of this AgentInfo.

        **参数解释**： 智能体ID。  **取值范围**： 不涉及。 

        :return: The agent_id of this AgentInfo.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        r"""Sets the agent_id of this AgentInfo.

        **参数解释**： 智能体ID。  **取值范围**： 不涉及。 

        :param agent_id: The agent_id of this AgentInfo.
        :type agent_id: str
        """
        self._agent_id = agent_id

    @property
    def name(self):
        r"""Gets the name of this AgentInfo.

        **参数解释**： 智能体名称。  **取值范围**： 不涉及。 

        :return: The name of this AgentInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AgentInfo.

        **参数解释**： 智能体名称。  **取值范围**： 不涉及。 

        :param name: The name of this AgentInfo.
        :type name: str
        """
        self._name = name

    @property
    def agent_type(self):
        r"""Gets the agent_type of this AgentInfo.

        **参数解释**： 智能体类型。   **取值范围**：  - agent：单智能体。  - multiagents：多智能体。  - workflow：工作流。 

        :return: The agent_type of this AgentInfo.
        :rtype: str
        """
        return self._agent_type

    @agent_type.setter
    def agent_type(self, agent_type):
        r"""Sets the agent_type of this AgentInfo.

        **参数解释**： 智能体类型。   **取值范围**：  - agent：单智能体。  - multiagents：多智能体。  - workflow：工作流。 

        :param agent_type: The agent_type of this AgentInfo.
        :type agent_type: str
        """
        self._agent_type = agent_type

    @property
    def create_time(self):
        r"""Gets the create_time of this AgentInfo.

        **参数解释**： 创建时间。  **取值范围**： 不涉及。 

        :return: The create_time of this AgentInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AgentInfo.

        **参数解释**： 创建时间。  **取值范围**： 不涉及。 

        :param create_time: The create_time of this AgentInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def total_token(self):
        r"""Gets the total_token of this AgentInfo.

        **参数解释**： 按照给定时间计算出tokens消耗。  **取值范围**： 不涉及。 

        :return: The total_token of this AgentInfo.
        :rtype: float
        """
        return self._total_token

    @total_token.setter
    def total_token(self, total_token):
        r"""Sets the total_token of this AgentInfo.

        **参数解释**： 按照给定时间计算出tokens消耗。  **取值范围**： 不涉及。 

        :param total_token: The total_token of this AgentInfo.
        :type total_token: float
        """
        self._total_token = total_token

    @property
    def avg_request_count(self):
        r"""Gets the avg_request_count of this AgentInfo.

        **参数解释**： 平均请求次数 单位为分钟。  **取值范围**： 不涉及。 

        :return: The avg_request_count of this AgentInfo.
        :rtype: float
        """
        return self._avg_request_count

    @avg_request_count.setter
    def avg_request_count(self, avg_request_count):
        r"""Sets the avg_request_count of this AgentInfo.

        **参数解释**： 平均请求次数 单位为分钟。  **取值范围**： 不涉及。 

        :param avg_request_count: The avg_request_count of this AgentInfo.
        :type avg_request_count: float
        """
        self._avg_request_count = avg_request_count

    @property
    def avg_duration_time(self):
        r"""Gets the avg_duration_time of this AgentInfo.

        **参数解释**： 平均延迟时间 延迟时间总和除以次数。  **取值范围**： 不涉及。 

        :return: The avg_duration_time of this AgentInfo.
        :rtype: float
        """
        return self._avg_duration_time

    @avg_duration_time.setter
    def avg_duration_time(self, avg_duration_time):
        r"""Sets the avg_duration_time of this AgentInfo.

        **参数解释**： 平均延迟时间 延迟时间总和除以次数。  **取值范围**： 不涉及。 

        :param avg_duration_time: The avg_duration_time of this AgentInfo.
        :type avg_duration_time: float
        """
        self._avg_duration_time = avg_duration_time

    @property
    def avg_fail_count(self):
        r"""Gets the avg_fail_count of this AgentInfo.

        **参数解释**： 平均请求失败次数 单位为分钟。  **取值范围**： 不涉及。 

        :return: The avg_fail_count of this AgentInfo.
        :rtype: float
        """
        return self._avg_fail_count

    @avg_fail_count.setter
    def avg_fail_count(self, avg_fail_count):
        r"""Sets the avg_fail_count of this AgentInfo.

        **参数解释**： 平均请求失败次数 单位为分钟。  **取值范围**： 不涉及。 

        :param avg_fail_count: The avg_fail_count of this AgentInfo.
        :type avg_fail_count: float
        """
        self._avg_fail_count = avg_fail_count

    @property
    def apm_app_id(self):
        r"""Gets the apm_app_id of this AgentInfo.

        **参数解释**： apm的app_id，非必填。  **取值范围**： 不涉及。 

        :return: The apm_app_id of this AgentInfo.
        :rtype: str
        """
        return self._apm_app_id

    @apm_app_id.setter
    def apm_app_id(self, apm_app_id):
        r"""Sets the apm_app_id of this AgentInfo.

        **参数解释**： apm的app_id，非必填。  **取值范围**： 不涉及。 

        :param apm_app_id: The apm_app_id of this AgentInfo.
        :type apm_app_id: str
        """
        self._apm_app_id = apm_app_id

    @property
    def aom_prom_id(self):
        r"""Gets the aom_prom_id of this AgentInfo.

        **参数解释**： aom的app_id，非必填。  **取值范围**： 不涉及。 

        :return: The aom_prom_id of this AgentInfo.
        :rtype: str
        """
        return self._aom_prom_id

    @aom_prom_id.setter
    def aom_prom_id(self, aom_prom_id):
        r"""Sets the aom_prom_id of this AgentInfo.

        **参数解释**： aom的app_id，非必填。  **取值范围**： 不涉及。 

        :param aom_prom_id: The aom_prom_id of this AgentInfo.
        :type aom_prom_id: str
        """
        self._aom_prom_id = aom_prom_id

    @property
    def apm_app_token(self):
        r"""Gets the apm_app_token of this AgentInfo.

        **参数解释**： apm token，加密存储，非必填。  **取值范围**： 不涉及。 

        :return: The apm_app_token of this AgentInfo.
        :rtype: str
        """
        return self._apm_app_token

    @apm_app_token.setter
    def apm_app_token(self, apm_app_token):
        r"""Sets the apm_app_token of this AgentInfo.

        **参数解释**： apm token，加密存储，非必填。  **取值范围**： 不涉及。 

        :param apm_app_token: The apm_app_token of this AgentInfo.
        :type apm_app_token: str
        """
        self._apm_app_token = apm_app_token

    @property
    def aom_access_code(self):
        r"""Gets the aom_access_code of this AgentInfo.

        **参数解释**： aom access_code，加密存储，非必填。  **取值范围**： 不涉及。 

        :return: The aom_access_code of this AgentInfo.
        :rtype: str
        """
        return self._aom_access_code

    @aom_access_code.setter
    def aom_access_code(self, aom_access_code):
        r"""Sets the aom_access_code of this AgentInfo.

        **参数解释**： aom access_code，加密存储，非必填。  **取值范围**： 不涉及。 

        :param aom_access_code: The aom_access_code of this AgentInfo.
        :type aom_access_code: str
        """
        self._aom_access_code = aom_access_code

    @property
    def lts_group_id(self):
        r"""Gets the lts_group_id of this AgentInfo.

        **参数解释**： lts_group_id，非必填。  **取值范围**： 不涉及。 

        :return: The lts_group_id of this AgentInfo.
        :rtype: str
        """
        return self._lts_group_id

    @lts_group_id.setter
    def lts_group_id(self, lts_group_id):
        r"""Sets the lts_group_id of this AgentInfo.

        **参数解释**： lts_group_id，非必填。  **取值范围**： 不涉及。 

        :param lts_group_id: The lts_group_id of this AgentInfo.
        :type lts_group_id: str
        """
        self._lts_group_id = lts_group_id

    @property
    def lts_stream_id(self):
        r"""Gets the lts_stream_id of this AgentInfo.

        **参数解释**： lts_stream_id，非必填。  **取值范围**： 不涉及。 

        :return: The lts_stream_id of this AgentInfo.
        :rtype: str
        """
        return self._lts_stream_id

    @lts_stream_id.setter
    def lts_stream_id(self, lts_stream_id):
        r"""Sets the lts_stream_id of this AgentInfo.

        **参数解释**： lts_stream_id，非必填。  **取值范围**： 不涉及。 

        :param lts_stream_id: The lts_stream_id of this AgentInfo.
        :type lts_stream_id: str
        """
        self._lts_stream_id = lts_stream_id

    @property
    def lts_label_name(self):
        r"""Gets the lts_label_name of this AgentInfo.

        **参数解释**： 用于过滤lts日志标签。  **取值范围**： 不涉及。 

        :return: The lts_label_name of this AgentInfo.
        :rtype: str
        """
        return self._lts_label_name

    @lts_label_name.setter
    def lts_label_name(self, lts_label_name):
        r"""Sets the lts_label_name of this AgentInfo.

        **参数解释**： 用于过滤lts日志标签。  **取值范围**： 不涉及。 

        :param lts_label_name: The lts_label_name of this AgentInfo.
        :type lts_label_name: str
        """
        self._lts_label_name = lts_label_name

    @property
    def apm_exporter_endpoint(self):
        r"""Gets the apm_exporter_endpoint of this AgentInfo.

        **参数解释**： apm上报地址。  **取值范围**： 不涉及。 

        :return: The apm_exporter_endpoint of this AgentInfo.
        :rtype: str
        """
        return self._apm_exporter_endpoint

    @apm_exporter_endpoint.setter
    def apm_exporter_endpoint(self, apm_exporter_endpoint):
        r"""Sets the apm_exporter_endpoint of this AgentInfo.

        **参数解释**： apm上报地址。  **取值范围**： 不涉及。 

        :param apm_exporter_endpoint: The apm_exporter_endpoint of this AgentInfo.
        :type apm_exporter_endpoint: str
        """
        self._apm_exporter_endpoint = apm_exporter_endpoint

    @property
    def aom_exporter_endpoint(self):
        r"""Gets the aom_exporter_endpoint of this AgentInfo.

        **参数解释**： aom上报地址。  **取值范围**： 不涉及。 

        :return: The aom_exporter_endpoint of this AgentInfo.
        :rtype: str
        """
        return self._aom_exporter_endpoint

    @aom_exporter_endpoint.setter
    def aom_exporter_endpoint(self, aom_exporter_endpoint):
        r"""Sets the aom_exporter_endpoint of this AgentInfo.

        **参数解释**： aom上报地址。  **取值范围**： 不涉及。 

        :param aom_exporter_endpoint: The aom_exporter_endpoint of this AgentInfo.
        :type aom_exporter_endpoint: str
        """
        self._aom_exporter_endpoint = aom_exporter_endpoint

    @property
    def deleted(self):
        r"""Gets the deleted of this AgentInfo.

        **参数解释**： 是否被刪除。  **取值范围**： 不涉及。 

        :return: The deleted of this AgentInfo.
        :rtype: int
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this AgentInfo.

        **参数解释**： 是否被刪除。  **取值范围**： 不涉及。 

        :param deleted: The deleted of this AgentInfo.
        :type deleted: int
        """
        self._deleted = deleted

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
        if not isinstance(other, AgentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
