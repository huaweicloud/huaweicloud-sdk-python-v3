# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgentInstancesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ai_agent_type': 'list[str]',
        'region_id': 'list[str]',
        'agent_status': 'list[str]',
        'desktop_status': 'list[str]',
        'desktop_connection': 'list[str]',
        'model_group_id': 'str',
        'channel_config_status': 'list[str]',
        'instance_name': 'str',
        'instance_id': 'str',
        'desktop_id': 'str',
        'create_time_start': 'datetime',
        'create_time_end': 'datetime',
        'tags': 'str',
        'risk_type': 'list[str]',
        'model_config_status': 'list[str]',
        'agent_version': 'str',
        'sort_field': 'str',
        'sort_order': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'ai_agent_type': 'ai_agent_type',
        'region_id': 'region_id',
        'agent_status': 'agent_status',
        'desktop_status': 'desktop_status',
        'desktop_connection': 'desktop_connection',
        'model_group_id': 'model_group_id',
        'channel_config_status': 'channel_config_status',
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'desktop_id': 'desktop_id',
        'create_time_start': 'create_time_start',
        'create_time_end': 'create_time_end',
        'tags': 'tags',
        'risk_type': 'risk_type',
        'model_config_status': 'model_config_status',
        'agent_version': 'agent_version',
        'sort_field': 'sort_field',
        'sort_order': 'sort_order',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, ai_agent_type=None, region_id=None, agent_status=None, desktop_status=None, desktop_connection=None, model_group_id=None, channel_config_status=None, instance_name=None, instance_id=None, desktop_id=None, create_time_start=None, create_time_end=None, tags=None, risk_type=None, model_config_status=None, agent_version=None, sort_field=None, sort_order=None, offset=None, limit=None):
        r"""ListAgentInstancesRequest

        The model defined in huaweicloud sdk

        :param ai_agent_type: Agent 类型，支持多选（OR 逻辑）：OpenClaw / OfficeClaw / HermesAgent
        :type ai_agent_type: list[str]
        :param region_id: 区域 ID，支持多选（OR 逻辑）
        :type region_id: list[str]
        :param agent_status: Agent 运行状态，支持多选（OR 逻辑）： - UNREACHABLE：连续3次心跳丢失（90秒无上报），触发告警 - ERROR：Agent进程健康检查连续失败3次或进程异常退出，尝试自动重启 - OFFLINE：桌面关机或重建中，停止心跳检测 - RUNNING：心跳正常且Agent进程健康检查通过
        :type agent_status: list[str]
        :param desktop_status: 桌面运行状态，支持多选（OR 逻辑）： - ACTIVE：运行中 - SHUTOFF：已关机 - HIBERNATED：已休眠 - ERROR：故障
        :type desktop_status: list[str]
        :param desktop_connection: 桌面连接状态，支持多选（OR 逻辑）： - UNREGISTER：桌面未注册（关机后也会出现） - REGISTERED：桌面已注册，等待用户连接 - CONNECTED：用户已连接，正在使用桌面 - DISCONNECTED：桌面与客户端断开会话
        :type desktop_connection: list[str]
        :param model_group_id: 已授权的模型分组 ID（单选）
        :type model_group_id: str
        :param channel_config_status: 通道配置状态，支持多选（OR 逻辑）： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败
        :type channel_config_status: list[str]
        :param instance_name: 实例名称（模糊搜索）
        :type instance_name: str
        :param instance_id: 实例 ID（精确搜索）
        :type instance_id: str
        :param desktop_id: 云桌面 ID（精确搜索）
        :type desktop_id: str
        :param create_time_start: 创建时间范围-开始
        :type create_time_start: datetime
        :param create_time_end: 创建时间范围-结束
        :type create_time_end: datetime
        :param tags: 标签过滤，格式：key1&#x3D;val1,key2&#x3D;val2，多个键值对用逗号分隔
        :type tags: str
        :param risk_type: 风险类型过滤，支持多选（OR 逻辑）： - MODEL_CONFIG_INCONSISTENT：模型配置不一致 - IM_CHANNEL_CONFIG_INCONSISTENT：IM通道配置不一致
        :type risk_type: list[str]
        :param model_config_status: 模型配置状态，支持多选（OR 逻辑）： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败
        :type model_config_status: list[str]
        :param agent_version: Agent 版本号（精确搜索）
        :type agent_version: str
        :param sort_field: 排序字段：create_time（默认）/ instance_name / agent_status / heartbeat_time
        :type sort_field: str
        :param sort_order: 排序方向：DESC（默认）/ ASC
        :type sort_order: str
        :param offset: 偏移量，从0开始
        :type offset: int
        :param limit: 每页条数
        :type limit: int
        """
        
        

        self._ai_agent_type = None
        self._region_id = None
        self._agent_status = None
        self._desktop_status = None
        self._desktop_connection = None
        self._model_group_id = None
        self._channel_config_status = None
        self._instance_name = None
        self._instance_id = None
        self._desktop_id = None
        self._create_time_start = None
        self._create_time_end = None
        self._tags = None
        self._risk_type = None
        self._model_config_status = None
        self._agent_version = None
        self._sort_field = None
        self._sort_order = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if ai_agent_type is not None:
            self.ai_agent_type = ai_agent_type
        if region_id is not None:
            self.region_id = region_id
        if agent_status is not None:
            self.agent_status = agent_status
        if desktop_status is not None:
            self.desktop_status = desktop_status
        if desktop_connection is not None:
            self.desktop_connection = desktop_connection
        if model_group_id is not None:
            self.model_group_id = model_group_id
        if channel_config_status is not None:
            self.channel_config_status = channel_config_status
        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if create_time_start is not None:
            self.create_time_start = create_time_start
        if create_time_end is not None:
            self.create_time_end = create_time_end
        if tags is not None:
            self.tags = tags
        if risk_type is not None:
            self.risk_type = risk_type
        if model_config_status is not None:
            self.model_config_status = model_config_status
        if agent_version is not None:
            self.agent_version = agent_version
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_order is not None:
            self.sort_order = sort_order
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def ai_agent_type(self):
        r"""Gets the ai_agent_type of this ListAgentInstancesRequest.

        Agent 类型，支持多选（OR 逻辑）：OpenClaw / OfficeClaw / HermesAgent

        :return: The ai_agent_type of this ListAgentInstancesRequest.
        :rtype: list[str]
        """
        return self._ai_agent_type

    @ai_agent_type.setter
    def ai_agent_type(self, ai_agent_type):
        r"""Sets the ai_agent_type of this ListAgentInstancesRequest.

        Agent 类型，支持多选（OR 逻辑）：OpenClaw / OfficeClaw / HermesAgent

        :param ai_agent_type: The ai_agent_type of this ListAgentInstancesRequest.
        :type ai_agent_type: list[str]
        """
        self._ai_agent_type = ai_agent_type

    @property
    def region_id(self):
        r"""Gets the region_id of this ListAgentInstancesRequest.

        区域 ID，支持多选（OR 逻辑）

        :return: The region_id of this ListAgentInstancesRequest.
        :rtype: list[str]
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListAgentInstancesRequest.

        区域 ID，支持多选（OR 逻辑）

        :param region_id: The region_id of this ListAgentInstancesRequest.
        :type region_id: list[str]
        """
        self._region_id = region_id

    @property
    def agent_status(self):
        r"""Gets the agent_status of this ListAgentInstancesRequest.

        Agent 运行状态，支持多选（OR 逻辑）： - UNREACHABLE：连续3次心跳丢失（90秒无上报），触发告警 - ERROR：Agent进程健康检查连续失败3次或进程异常退出，尝试自动重启 - OFFLINE：桌面关机或重建中，停止心跳检测 - RUNNING：心跳正常且Agent进程健康检查通过

        :return: The agent_status of this ListAgentInstancesRequest.
        :rtype: list[str]
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this ListAgentInstancesRequest.

        Agent 运行状态，支持多选（OR 逻辑）： - UNREACHABLE：连续3次心跳丢失（90秒无上报），触发告警 - ERROR：Agent进程健康检查连续失败3次或进程异常退出，尝试自动重启 - OFFLINE：桌面关机或重建中，停止心跳检测 - RUNNING：心跳正常且Agent进程健康检查通过

        :param agent_status: The agent_status of this ListAgentInstancesRequest.
        :type agent_status: list[str]
        """
        self._agent_status = agent_status

    @property
    def desktop_status(self):
        r"""Gets the desktop_status of this ListAgentInstancesRequest.

        桌面运行状态，支持多选（OR 逻辑）： - ACTIVE：运行中 - SHUTOFF：已关机 - HIBERNATED：已休眠 - ERROR：故障

        :return: The desktop_status of this ListAgentInstancesRequest.
        :rtype: list[str]
        """
        return self._desktop_status

    @desktop_status.setter
    def desktop_status(self, desktop_status):
        r"""Sets the desktop_status of this ListAgentInstancesRequest.

        桌面运行状态，支持多选（OR 逻辑）： - ACTIVE：运行中 - SHUTOFF：已关机 - HIBERNATED：已休眠 - ERROR：故障

        :param desktop_status: The desktop_status of this ListAgentInstancesRequest.
        :type desktop_status: list[str]
        """
        self._desktop_status = desktop_status

    @property
    def desktop_connection(self):
        r"""Gets the desktop_connection of this ListAgentInstancesRequest.

        桌面连接状态，支持多选（OR 逻辑）： - UNREGISTER：桌面未注册（关机后也会出现） - REGISTERED：桌面已注册，等待用户连接 - CONNECTED：用户已连接，正在使用桌面 - DISCONNECTED：桌面与客户端断开会话

        :return: The desktop_connection of this ListAgentInstancesRequest.
        :rtype: list[str]
        """
        return self._desktop_connection

    @desktop_connection.setter
    def desktop_connection(self, desktop_connection):
        r"""Sets the desktop_connection of this ListAgentInstancesRequest.

        桌面连接状态，支持多选（OR 逻辑）： - UNREGISTER：桌面未注册（关机后也会出现） - REGISTERED：桌面已注册，等待用户连接 - CONNECTED：用户已连接，正在使用桌面 - DISCONNECTED：桌面与客户端断开会话

        :param desktop_connection: The desktop_connection of this ListAgentInstancesRequest.
        :type desktop_connection: list[str]
        """
        self._desktop_connection = desktop_connection

    @property
    def model_group_id(self):
        r"""Gets the model_group_id of this ListAgentInstancesRequest.

        已授权的模型分组 ID（单选）

        :return: The model_group_id of this ListAgentInstancesRequest.
        :rtype: str
        """
        return self._model_group_id

    @model_group_id.setter
    def model_group_id(self, model_group_id):
        r"""Sets the model_group_id of this ListAgentInstancesRequest.

        已授权的模型分组 ID（单选）

        :param model_group_id: The model_group_id of this ListAgentInstancesRequest.
        :type model_group_id: str
        """
        self._model_group_id = model_group_id

    @property
    def channel_config_status(self):
        r"""Gets the channel_config_status of this ListAgentInstancesRequest.

        通道配置状态，支持多选（OR 逻辑）： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败

        :return: The channel_config_status of this ListAgentInstancesRequest.
        :rtype: list[str]
        """
        return self._channel_config_status

    @channel_config_status.setter
    def channel_config_status(self, channel_config_status):
        r"""Sets the channel_config_status of this ListAgentInstancesRequest.

        通道配置状态，支持多选（OR 逻辑）： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败

        :param channel_config_status: The channel_config_status of this ListAgentInstancesRequest.
        :type channel_config_status: list[str]
        """
        self._channel_config_status = channel_config_status

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ListAgentInstancesRequest.

        实例名称（模糊搜索）

        :return: The instance_name of this ListAgentInstancesRequest.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ListAgentInstancesRequest.

        实例名称（模糊搜索）

        :param instance_name: The instance_name of this ListAgentInstancesRequest.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListAgentInstancesRequest.

        实例 ID（精确搜索）

        :return: The instance_id of this ListAgentInstancesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListAgentInstancesRequest.

        实例 ID（精确搜索）

        :param instance_id: The instance_id of this ListAgentInstancesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ListAgentInstancesRequest.

        云桌面 ID（精确搜索）

        :return: The desktop_id of this ListAgentInstancesRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ListAgentInstancesRequest.

        云桌面 ID（精确搜索）

        :param desktop_id: The desktop_id of this ListAgentInstancesRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def create_time_start(self):
        r"""Gets the create_time_start of this ListAgentInstancesRequest.

        创建时间范围-开始

        :return: The create_time_start of this ListAgentInstancesRequest.
        :rtype: datetime
        """
        return self._create_time_start

    @create_time_start.setter
    def create_time_start(self, create_time_start):
        r"""Sets the create_time_start of this ListAgentInstancesRequest.

        创建时间范围-开始

        :param create_time_start: The create_time_start of this ListAgentInstancesRequest.
        :type create_time_start: datetime
        """
        self._create_time_start = create_time_start

    @property
    def create_time_end(self):
        r"""Gets the create_time_end of this ListAgentInstancesRequest.

        创建时间范围-结束

        :return: The create_time_end of this ListAgentInstancesRequest.
        :rtype: datetime
        """
        return self._create_time_end

    @create_time_end.setter
    def create_time_end(self, create_time_end):
        r"""Sets the create_time_end of this ListAgentInstancesRequest.

        创建时间范围-结束

        :param create_time_end: The create_time_end of this ListAgentInstancesRequest.
        :type create_time_end: datetime
        """
        self._create_time_end = create_time_end

    @property
    def tags(self):
        r"""Gets the tags of this ListAgentInstancesRequest.

        标签过滤，格式：key1=val1,key2=val2，多个键值对用逗号分隔

        :return: The tags of this ListAgentInstancesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListAgentInstancesRequest.

        标签过滤，格式：key1=val1,key2=val2，多个键值对用逗号分隔

        :param tags: The tags of this ListAgentInstancesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def risk_type(self):
        r"""Gets the risk_type of this ListAgentInstancesRequest.

        风险类型过滤，支持多选（OR 逻辑）： - MODEL_CONFIG_INCONSISTENT：模型配置不一致 - IM_CHANNEL_CONFIG_INCONSISTENT：IM通道配置不一致

        :return: The risk_type of this ListAgentInstancesRequest.
        :rtype: list[str]
        """
        return self._risk_type

    @risk_type.setter
    def risk_type(self, risk_type):
        r"""Sets the risk_type of this ListAgentInstancesRequest.

        风险类型过滤，支持多选（OR 逻辑）： - MODEL_CONFIG_INCONSISTENT：模型配置不一致 - IM_CHANNEL_CONFIG_INCONSISTENT：IM通道配置不一致

        :param risk_type: The risk_type of this ListAgentInstancesRequest.
        :type risk_type: list[str]
        """
        self._risk_type = risk_type

    @property
    def model_config_status(self):
        r"""Gets the model_config_status of this ListAgentInstancesRequest.

        模型配置状态，支持多选（OR 逻辑）： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败

        :return: The model_config_status of this ListAgentInstancesRequest.
        :rtype: list[str]
        """
        return self._model_config_status

    @model_config_status.setter
    def model_config_status(self, model_config_status):
        r"""Sets the model_config_status of this ListAgentInstancesRequest.

        模型配置状态，支持多选（OR 逻辑）： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败

        :param model_config_status: The model_config_status of this ListAgentInstancesRequest.
        :type model_config_status: list[str]
        """
        self._model_config_status = model_config_status

    @property
    def agent_version(self):
        r"""Gets the agent_version of this ListAgentInstancesRequest.

        Agent 版本号（精确搜索）

        :return: The agent_version of this ListAgentInstancesRequest.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this ListAgentInstancesRequest.

        Agent 版本号（精确搜索）

        :param agent_version: The agent_version of this ListAgentInstancesRequest.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListAgentInstancesRequest.

        排序字段：create_time（默认）/ instance_name / agent_status / heartbeat_time

        :return: The sort_field of this ListAgentInstancesRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListAgentInstancesRequest.

        排序字段：create_time（默认）/ instance_name / agent_status / heartbeat_time

        :param sort_field: The sort_field of this ListAgentInstancesRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_order(self):
        r"""Gets the sort_order of this ListAgentInstancesRequest.

        排序方向：DESC（默认）/ ASC

        :return: The sort_order of this ListAgentInstancesRequest.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        r"""Sets the sort_order of this ListAgentInstancesRequest.

        排序方向：DESC（默认）/ ASC

        :param sort_order: The sort_order of this ListAgentInstancesRequest.
        :type sort_order: str
        """
        self._sort_order = sort_order

    @property
    def offset(self):
        r"""Gets the offset of this ListAgentInstancesRequest.

        偏移量，从0开始

        :return: The offset of this ListAgentInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAgentInstancesRequest.

        偏移量，从0开始

        :param offset: The offset of this ListAgentInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListAgentInstancesRequest.

        每页条数

        :return: The limit of this ListAgentInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAgentInstancesRequest.

        每页条数

        :param limit: The limit of this ListAgentInstancesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListAgentInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
