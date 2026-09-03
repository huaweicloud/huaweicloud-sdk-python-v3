# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentInstanceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'desktop_id': 'str',
        'region_id': 'str',
        'ai_agent_type': 'str',
        'agent_status': 'str',
        'desktop_status': 'str',
        'desktop_connection': 'str',
        'model_config_status': 'str',
        'channel_config_status': 'str',
        'im_channel_configs': 'list[str]',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'product_id': 'str',
        'product_name': 'str',
        'image_id': 'str',
        'image_name': 'str',
        'desktop_pool_id': 'str',
        'user_name': 'str',
        'risks': 'list[AgentRisk]',
        'agent_version': 'str',
        'enterprise_project_id': 'str',
        'security_policy_control': 'int'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'desktop_id': 'desktop_id',
        'region_id': 'region_id',
        'ai_agent_type': 'ai_agent_type',
        'agent_status': 'agent_status',
        'desktop_status': 'desktop_status',
        'desktop_connection': 'desktop_connection',
        'model_config_status': 'model_config_status',
        'channel_config_status': 'channel_config_status',
        'im_channel_configs': 'im_channel_configs',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'product_id': 'product_id',
        'product_name': 'product_name',
        'image_id': 'image_id',
        'image_name': 'image_name',
        'desktop_pool_id': 'desktop_pool_id',
        'user_name': 'user_name',
        'risks': 'risks',
        'agent_version': 'agent_version',
        'enterprise_project_id': 'enterprise_project_id',
        'security_policy_control': 'security_policy_control'
    }

    def __init__(self, id=None, instance_id=None, instance_name=None, desktop_id=None, region_id=None, ai_agent_type=None, agent_status=None, desktop_status=None, desktop_connection=None, model_config_status=None, channel_config_status=None, im_channel_configs=None, create_time=None, update_time=None, product_id=None, product_name=None, image_id=None, image_name=None, desktop_pool_id=None, user_name=None, risks=None, agent_version=None, enterprise_project_id=None, security_policy_control=None):
        r"""AgentInstanceInfo

        The model defined in huaweicloud sdk

        :param id: 主键 ID
        :type id: str
        :param instance_id: Agent 实例 ID
        :type instance_id: str
        :param instance_name: 实例名称
        :type instance_name: str
        :param desktop_id: 关联云桌面 ID
        :type desktop_id: str
        :param region_id: 区域 ID
        :type region_id: str
        :param ai_agent_type: Agent 类型
        :type ai_agent_type: str
        :param agent_status: Agent 运行状态： - UNREACHABLE：连续3次心跳丢失（90秒无上报），触发告警 - ERROR：Agent进程健康检查连续失败3次或进程异常退出，尝试自动重启 - OFFLINE：桌面关机或重建中，停止心跳检测 - RUNNING：心跳正常且Agent进程健康检查通过
        :type agent_status: str
        :param desktop_status: 桌面运行状态： - ACTIVE：运行中 - SHUTOFF：已关机 - HIBERNATED：已休眠 - ERROR：故障
        :type desktop_status: str
        :param desktop_connection: 桌面连接状态： - UNREGISTER：桌面未注册（关机后也会出现） - REGISTERED：桌面已注册，等待用户连接 - CONNECTED：用户已连接，正在使用桌面 - DISCONNECTED：桌面与客户端断开会话
        :type desktop_connection: str
        :param model_config_status: 模型配置状态
        :type model_config_status: str
        :param channel_config_status: 通道配置状态： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败
        :type channel_config_status: str
        :param im_channel_configs: IM 通道配置 ID 列表
        :type im_channel_configs: list[str]
        :param create_time: 创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param product_id: 产品 ID
        :type product_id: str
        :param product_name: 产品名称
        :type product_name: str
        :param image_id: 镜像 ID
        :type image_id: str
        :param image_name: 镜像名称
        :type image_name: str
        :param desktop_pool_id: 桌面池 ID
        :type desktop_pool_id: str
        :param user_name: 用户名
        :type user_name: str
        :param risks: 风险列表
        :type risks: list[:class:`huaweicloudsdkworkspace.v2.AgentRisk`]
        :param agent_version: Agent 版本号
        :type agent_version: str
        :param enterprise_project_id: 企业项目 ID
        :type enterprise_project_id: str
        :param security_policy_control: 安全策略管控，1&#x3D;开启，0&#x3D;关闭
        :type security_policy_control: int
        """
        
        

        self._id = None
        self._instance_id = None
        self._instance_name = None
        self._desktop_id = None
        self._region_id = None
        self._ai_agent_type = None
        self._agent_status = None
        self._desktop_status = None
        self._desktop_connection = None
        self._model_config_status = None
        self._channel_config_status = None
        self._im_channel_configs = None
        self._create_time = None
        self._update_time = None
        self._product_id = None
        self._product_name = None
        self._image_id = None
        self._image_name = None
        self._desktop_pool_id = None
        self._user_name = None
        self._risks = None
        self._agent_version = None
        self._enterprise_project_id = None
        self._security_policy_control = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if desktop_id is not None:
            self.desktop_id = desktop_id
        if region_id is not None:
            self.region_id = region_id
        if ai_agent_type is not None:
            self.ai_agent_type = ai_agent_type
        if agent_status is not None:
            self.agent_status = agent_status
        if desktop_status is not None:
            self.desktop_status = desktop_status
        if desktop_connection is not None:
            self.desktop_connection = desktop_connection
        if model_config_status is not None:
            self.model_config_status = model_config_status
        if channel_config_status is not None:
            self.channel_config_status = channel_config_status
        if im_channel_configs is not None:
            self.im_channel_configs = im_channel_configs
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if product_id is not None:
            self.product_id = product_id
        if product_name is not None:
            self.product_name = product_name
        if image_id is not None:
            self.image_id = image_id
        if image_name is not None:
            self.image_name = image_name
        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if user_name is not None:
            self.user_name = user_name
        if risks is not None:
            self.risks = risks
        if agent_version is not None:
            self.agent_version = agent_version
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if security_policy_control is not None:
            self.security_policy_control = security_policy_control

    @property
    def id(self):
        r"""Gets the id of this AgentInstanceInfo.

        主键 ID

        :return: The id of this AgentInstanceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AgentInstanceInfo.

        主键 ID

        :param id: The id of this AgentInstanceInfo.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this AgentInstanceInfo.

        Agent 实例 ID

        :return: The instance_id of this AgentInstanceInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this AgentInstanceInfo.

        Agent 实例 ID

        :param instance_id: The instance_id of this AgentInstanceInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this AgentInstanceInfo.

        实例名称

        :return: The instance_name of this AgentInstanceInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this AgentInstanceInfo.

        实例名称

        :param instance_name: The instance_name of this AgentInstanceInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this AgentInstanceInfo.

        关联云桌面 ID

        :return: The desktop_id of this AgentInstanceInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this AgentInstanceInfo.

        关联云桌面 ID

        :param desktop_id: The desktop_id of this AgentInstanceInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def region_id(self):
        r"""Gets the region_id of this AgentInstanceInfo.

        区域 ID

        :return: The region_id of this AgentInstanceInfo.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this AgentInstanceInfo.

        区域 ID

        :param region_id: The region_id of this AgentInstanceInfo.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ai_agent_type(self):
        r"""Gets the ai_agent_type of this AgentInstanceInfo.

        Agent 类型

        :return: The ai_agent_type of this AgentInstanceInfo.
        :rtype: str
        """
        return self._ai_agent_type

    @ai_agent_type.setter
    def ai_agent_type(self, ai_agent_type):
        r"""Sets the ai_agent_type of this AgentInstanceInfo.

        Agent 类型

        :param ai_agent_type: The ai_agent_type of this AgentInstanceInfo.
        :type ai_agent_type: str
        """
        self._ai_agent_type = ai_agent_type

    @property
    def agent_status(self):
        r"""Gets the agent_status of this AgentInstanceInfo.

        Agent 运行状态： - UNREACHABLE：连续3次心跳丢失（90秒无上报），触发告警 - ERROR：Agent进程健康检查连续失败3次或进程异常退出，尝试自动重启 - OFFLINE：桌面关机或重建中，停止心跳检测 - RUNNING：心跳正常且Agent进程健康检查通过

        :return: The agent_status of this AgentInstanceInfo.
        :rtype: str
        """
        return self._agent_status

    @agent_status.setter
    def agent_status(self, agent_status):
        r"""Sets the agent_status of this AgentInstanceInfo.

        Agent 运行状态： - UNREACHABLE：连续3次心跳丢失（90秒无上报），触发告警 - ERROR：Agent进程健康检查连续失败3次或进程异常退出，尝试自动重启 - OFFLINE：桌面关机或重建中，停止心跳检测 - RUNNING：心跳正常且Agent进程健康检查通过

        :param agent_status: The agent_status of this AgentInstanceInfo.
        :type agent_status: str
        """
        self._agent_status = agent_status

    @property
    def desktop_status(self):
        r"""Gets the desktop_status of this AgentInstanceInfo.

        桌面运行状态： - ACTIVE：运行中 - SHUTOFF：已关机 - HIBERNATED：已休眠 - ERROR：故障

        :return: The desktop_status of this AgentInstanceInfo.
        :rtype: str
        """
        return self._desktop_status

    @desktop_status.setter
    def desktop_status(self, desktop_status):
        r"""Sets the desktop_status of this AgentInstanceInfo.

        桌面运行状态： - ACTIVE：运行中 - SHUTOFF：已关机 - HIBERNATED：已休眠 - ERROR：故障

        :param desktop_status: The desktop_status of this AgentInstanceInfo.
        :type desktop_status: str
        """
        self._desktop_status = desktop_status

    @property
    def desktop_connection(self):
        r"""Gets the desktop_connection of this AgentInstanceInfo.

        桌面连接状态： - UNREGISTER：桌面未注册（关机后也会出现） - REGISTERED：桌面已注册，等待用户连接 - CONNECTED：用户已连接，正在使用桌面 - DISCONNECTED：桌面与客户端断开会话

        :return: The desktop_connection of this AgentInstanceInfo.
        :rtype: str
        """
        return self._desktop_connection

    @desktop_connection.setter
    def desktop_connection(self, desktop_connection):
        r"""Sets the desktop_connection of this AgentInstanceInfo.

        桌面连接状态： - UNREGISTER：桌面未注册（关机后也会出现） - REGISTERED：桌面已注册，等待用户连接 - CONNECTED：用户已连接，正在使用桌面 - DISCONNECTED：桌面与客户端断开会话

        :param desktop_connection: The desktop_connection of this AgentInstanceInfo.
        :type desktop_connection: str
        """
        self._desktop_connection = desktop_connection

    @property
    def model_config_status(self):
        r"""Gets the model_config_status of this AgentInstanceInfo.

        模型配置状态

        :return: The model_config_status of this AgentInstanceInfo.
        :rtype: str
        """
        return self._model_config_status

    @model_config_status.setter
    def model_config_status(self, model_config_status):
        r"""Sets the model_config_status of this AgentInstanceInfo.

        模型配置状态

        :param model_config_status: The model_config_status of this AgentInstanceInfo.
        :type model_config_status: str
        """
        self._model_config_status = model_config_status

    @property
    def channel_config_status(self):
        r"""Gets the channel_config_status of this AgentInstanceInfo.

        通道配置状态： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败

        :return: The channel_config_status of this AgentInstanceInfo.
        :rtype: str
        """
        return self._channel_config_status

    @channel_config_status.setter
    def channel_config_status(self, channel_config_status):
        r"""Sets the channel_config_status of this AgentInstanceInfo.

        通道配置状态： - UNCONFIGURED：未配置 - APPLYING：配置中 - CONFIGURED：已配置 - FAILED：配置失败

        :param channel_config_status: The channel_config_status of this AgentInstanceInfo.
        :type channel_config_status: str
        """
        self._channel_config_status = channel_config_status

    @property
    def im_channel_configs(self):
        r"""Gets the im_channel_configs of this AgentInstanceInfo.

        IM 通道配置 ID 列表

        :return: The im_channel_configs of this AgentInstanceInfo.
        :rtype: list[str]
        """
        return self._im_channel_configs

    @im_channel_configs.setter
    def im_channel_configs(self, im_channel_configs):
        r"""Sets the im_channel_configs of this AgentInstanceInfo.

        IM 通道配置 ID 列表

        :param im_channel_configs: The im_channel_configs of this AgentInstanceInfo.
        :type im_channel_configs: list[str]
        """
        self._im_channel_configs = im_channel_configs

    @property
    def create_time(self):
        r"""Gets the create_time of this AgentInstanceInfo.

        创建时间

        :return: The create_time of this AgentInstanceInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AgentInstanceInfo.

        创建时间

        :param create_time: The create_time of this AgentInstanceInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AgentInstanceInfo.

        更新时间

        :return: The update_time of this AgentInstanceInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AgentInstanceInfo.

        更新时间

        :param update_time: The update_time of this AgentInstanceInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def product_id(self):
        r"""Gets the product_id of this AgentInstanceInfo.

        产品 ID

        :return: The product_id of this AgentInstanceInfo.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this AgentInstanceInfo.

        产品 ID

        :param product_id: The product_id of this AgentInstanceInfo.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def product_name(self):
        r"""Gets the product_name of this AgentInstanceInfo.

        产品名称

        :return: The product_name of this AgentInstanceInfo.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        r"""Sets the product_name of this AgentInstanceInfo.

        产品名称

        :param product_name: The product_name of this AgentInstanceInfo.
        :type product_name: str
        """
        self._product_name = product_name

    @property
    def image_id(self):
        r"""Gets the image_id of this AgentInstanceInfo.

        镜像 ID

        :return: The image_id of this AgentInstanceInfo.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this AgentInstanceInfo.

        镜像 ID

        :param image_id: The image_id of this AgentInstanceInfo.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def image_name(self):
        r"""Gets the image_name of this AgentInstanceInfo.

        镜像名称

        :return: The image_name of this AgentInstanceInfo.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this AgentInstanceInfo.

        镜像名称

        :param image_name: The image_name of this AgentInstanceInfo.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this AgentInstanceInfo.

        桌面池 ID

        :return: The desktop_pool_id of this AgentInstanceInfo.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this AgentInstanceInfo.

        桌面池 ID

        :param desktop_pool_id: The desktop_pool_id of this AgentInstanceInfo.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def user_name(self):
        r"""Gets the user_name of this AgentInstanceInfo.

        用户名

        :return: The user_name of this AgentInstanceInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this AgentInstanceInfo.

        用户名

        :param user_name: The user_name of this AgentInstanceInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def risks(self):
        r"""Gets the risks of this AgentInstanceInfo.

        风险列表

        :return: The risks of this AgentInstanceInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AgentRisk`]
        """
        return self._risks

    @risks.setter
    def risks(self, risks):
        r"""Sets the risks of this AgentInstanceInfo.

        风险列表

        :param risks: The risks of this AgentInstanceInfo.
        :type risks: list[:class:`huaweicloudsdkworkspace.v2.AgentRisk`]
        """
        self._risks = risks

    @property
    def agent_version(self):
        r"""Gets the agent_version of this AgentInstanceInfo.

        Agent 版本号

        :return: The agent_version of this AgentInstanceInfo.
        :rtype: str
        """
        return self._agent_version

    @agent_version.setter
    def agent_version(self, agent_version):
        r"""Sets the agent_version of this AgentInstanceInfo.

        Agent 版本号

        :param agent_version: The agent_version of this AgentInstanceInfo.
        :type agent_version: str
        """
        self._agent_version = agent_version

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this AgentInstanceInfo.

        企业项目 ID

        :return: The enterprise_project_id of this AgentInstanceInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this AgentInstanceInfo.

        企业项目 ID

        :param enterprise_project_id: The enterprise_project_id of this AgentInstanceInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def security_policy_control(self):
        r"""Gets the security_policy_control of this AgentInstanceInfo.

        安全策略管控，1=开启，0=关闭

        :return: The security_policy_control of this AgentInstanceInfo.
        :rtype: int
        """
        return self._security_policy_control

    @security_policy_control.setter
    def security_policy_control(self, security_policy_control):
        r"""Sets the security_policy_control of this AgentInstanceInfo.

        安全策略管控，1=开启，0=关闭

        :param security_policy_control: The security_policy_control of this AgentInstanceInfo.
        :type security_policy_control: int
        """
        self._security_policy_control = security_policy_control

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
        if not isinstance(other, AgentInstanceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
