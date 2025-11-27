# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'type': 'str',
        'resource_id_list': 'list[str]',
        'name': 'str',
        'region_id': 'str',
        'az_id': 'str',
        'ip_type': 'str',
        'ip': 'str',
        'status': 'str',
        'agent_state': 'str',
        'image_name': 'str',
        'os_type': 'str',
        'tag': 'str',
        'tag_key': 'str',
        'group_id': 'str',
        'component_id': 'str',
        'application_id': 'str',
        'cce_cluster_id': 'str',
        'ep_id': 'str',
        'is_delegated': 'str',
        'is_collected': 'bool',
        'flavor_name': 'str',
        'charging_mode': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'type': 'type',
        'resource_id_list': 'resource_id_list',
        'name': 'name',
        'region_id': 'region_id',
        'az_id': 'az_id',
        'ip_type': 'ip_type',
        'ip': 'ip',
        'status': 'status',
        'agent_state': 'agent_state',
        'image_name': 'image_name',
        'os_type': 'os_type',
        'tag': 'tag',
        'tag_key': 'tag_key',
        'group_id': 'group_id',
        'component_id': 'component_id',
        'application_id': 'application_id',
        'cce_cluster_id': 'cce_cluster_id',
        'ep_id': 'ep_id',
        'is_delegated': 'is_delegated',
        'is_collected': 'is_collected',
        'flavor_name': 'flavor_name',
        'charging_mode': 'charging_mode'
    }

    def __init__(self, provider=None, type=None, resource_id_list=None, name=None, region_id=None, az_id=None, ip_type=None, ip=None, status=None, agent_state=None, image_name=None, os_type=None, tag=None, tag_key=None, group_id=None, component_id=None, application_id=None, cce_cluster_id=None, ep_id=None, is_delegated=None, is_collected=None, flavor_name=None, charging_mode=None):
        r"""CountResourcesRequest

        The model defined in huaweicloud sdk

        :param provider: **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 可选ecs,cce，rds等服务资源。 **默认取值：** 不涉及。
        :type provider: str
        :param type: **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器 。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。
        :type type: str
        :param resource_id_list: **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 自定义,资源id组成的集合。 **默认取值：** 不涉及。
        :type resource_id_list: list[str]
        :param name: **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器 BMS。 **默认取值：** 不涉及。
        :type name: str
        :param region_id: **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。
        :type region_id: str
        :param az_id: **参数解释：** 可用区id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type az_id: str
        :param ip_type: **参数解释：** ip类型。 **约束限制：** 不涉及。 **取值范围：** fixed：内网IP，floating：弹性公网IP。 **默认取值：** 不涉及。
        :type ip_type: str
        :param ip: **参数解释：** 云资源IP。 **约束限制：** 不涉及。 **取值范围：** IPv4地址过滤结果，匹配规则为模糊匹配。 **默认取值：** 不涉及。
        :type ip: str
        :param status: **参数解释：** 云资源状态。 **约束限制：** 不涉及。 **取值范围：** 请选择[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws)[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws_hk)中存在的云服务器状态。 **默认取值：** 不涉及。
        :type status: str
        :param agent_state: **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - 运行中。 - 异常。 - 安装中。 - 安装失败。 - 已卸载。 - 未安装。 **默认取值：** 不涉及。
        :type agent_state: str
        :param image_name: **参数解释：** 镜像名称，模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type image_name: str
        :param os_type: **参数解释：** 系统类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type os_type: str
        :param tag: **参数解释：** 云资源的标签。 **约束限制：** 标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。 **取值范围：** 标签命名时，需满足如下要求：标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）以及中文字符。 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）、小数点（.）以及中文字符。 **默认取值：** 不涉及。
        :type tag: str
        :param tag_key: **参数解释：** 云资源的标签key。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tag_key: str
        :param group_id: **参数解释：** 云资源下的分组ID。 **约束限制：** 不涉及。 **取值范围：** 设置null值时获取未绑定分组的资源。 **默认取值：** 不涉及。
        :type group_id: str
        :param component_id: **参数解释：** 云资源下组件ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type component_id: str
        :param application_id: **参数解释：** 云资源下应用ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type application_id: str
        :param cce_cluster_id: **参数解释：** cce集群ID。 **约束限制：** 不涉及。 **取值范围：** 资源属于的cce的ID。 **默认取值：** 不涉及。
        :type cce_cluster_id: str
        :param ep_id: **参数解释：** 企业项目id。 **约束限制：** 不涉及。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。 **默认取值：** 不涉及。
        :type ep_id: str
        :param is_delegated: **参数解释：** 是否已托管。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type is_delegated: str
        :param is_collected: **参数解释：** 是否已收藏。 **约束限制：** 不涉及。 **取值范围：** - true：已收藏的企业项目。 - false：未收藏的企业项目。 **默认取值：** 不涉及。
        :type is_collected: bool
        :param flavor_name: **参数解释：** 云资源规格名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type flavor_name: str
        :param charging_mode: **参数解释：** 云服务器的计费类型。 **约束限制：** 不涉及。 **取值范围：** 计费模式： - 0：按需计费。 - 1：包年包月。 - 2：竞价计费。 **默认取值：** 不涉及。
        :type charging_mode: str
        """
        
        

        self._provider = None
        self._type = None
        self._resource_id_list = None
        self._name = None
        self._region_id = None
        self._az_id = None
        self._ip_type = None
        self._ip = None
        self._status = None
        self._agent_state = None
        self._image_name = None
        self._os_type = None
        self._tag = None
        self._tag_key = None
        self._group_id = None
        self._component_id = None
        self._application_id = None
        self._cce_cluster_id = None
        self._ep_id = None
        self._is_delegated = None
        self._is_collected = None
        self._flavor_name = None
        self._charging_mode = None
        self.discriminator = None

        self.provider = provider
        self.type = type
        if resource_id_list is not None:
            self.resource_id_list = resource_id_list
        if name is not None:
            self.name = name
        if region_id is not None:
            self.region_id = region_id
        if az_id is not None:
            self.az_id = az_id
        if ip_type is not None:
            self.ip_type = ip_type
        if ip is not None:
            self.ip = ip
        if status is not None:
            self.status = status
        if agent_state is not None:
            self.agent_state = agent_state
        if image_name is not None:
            self.image_name = image_name
        if os_type is not None:
            self.os_type = os_type
        if tag is not None:
            self.tag = tag
        if tag_key is not None:
            self.tag_key = tag_key
        if group_id is not None:
            self.group_id = group_id
        if component_id is not None:
            self.component_id = component_id
        if application_id is not None:
            self.application_id = application_id
        if cce_cluster_id is not None:
            self.cce_cluster_id = cce_cluster_id
        if ep_id is not None:
            self.ep_id = ep_id
        if is_delegated is not None:
            self.is_delegated = is_delegated
        if is_collected is not None:
            self.is_collected = is_collected
        if flavor_name is not None:
            self.flavor_name = flavor_name
        if charging_mode is not None:
            self.charging_mode = charging_mode

    @property
    def provider(self):
        r"""Gets the provider of this CountResourcesRequest.

        **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 可选ecs,cce，rds等服务资源。 **默认取值：** 不涉及。

        :return: The provider of this CountResourcesRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this CountResourcesRequest.

        **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 可选ecs,cce，rds等服务资源。 **默认取值：** 不涉及。

        :param provider: The provider of this CountResourcesRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this CountResourcesRequest.

        **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器 。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。

        :return: The type of this CountResourcesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CountResourcesRequest.

        **参数解释：** 资源类型名称。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器 。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。

        :param type: The type of this CountResourcesRequest.
        :type type: str
        """
        self._type = type

    @property
    def resource_id_list(self):
        r"""Gets the resource_id_list of this CountResourcesRequest.

        **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 自定义,资源id组成的集合。 **默认取值：** 不涉及。

        :return: The resource_id_list of this CountResourcesRequest.
        :rtype: list[str]
        """
        return self._resource_id_list

    @resource_id_list.setter
    def resource_id_list(self, resource_id_list):
        r"""Sets the resource_id_list of this CountResourcesRequest.

        **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 自定义,资源id组成的集合。 **默认取值：** 不涉及。

        :param resource_id_list: The resource_id_list of this CountResourcesRequest.
        :type resource_id_list: list[str]
        """
        self._resource_id_list = resource_id_list

    @property
    def name(self):
        r"""Gets the name of this CountResourcesRequest.

        **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器 BMS。 **默认取值：** 不涉及。

        :return: The name of this CountResourcesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CountResourcesRequest.

        **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器 BMS。 **默认取值：** 不涉及。

        :param name: The name of this CountResourcesRequest.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this CountResourcesRequest.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。

        :return: The region_id of this CountResourcesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CountResourcesRequest.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。

        :param region_id: The region_id of this CountResourcesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def az_id(self):
        r"""Gets the az_id of this CountResourcesRequest.

        **参数解释：** 可用区id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The az_id of this CountResourcesRequest.
        :rtype: str
        """
        return self._az_id

    @az_id.setter
    def az_id(self, az_id):
        r"""Sets the az_id of this CountResourcesRequest.

        **参数解释：** 可用区id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param az_id: The az_id of this CountResourcesRequest.
        :type az_id: str
        """
        self._az_id = az_id

    @property
    def ip_type(self):
        r"""Gets the ip_type of this CountResourcesRequest.

        **参数解释：** ip类型。 **约束限制：** 不涉及。 **取值范围：** fixed：内网IP，floating：弹性公网IP。 **默认取值：** 不涉及。

        :return: The ip_type of this CountResourcesRequest.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this CountResourcesRequest.

        **参数解释：** ip类型。 **约束限制：** 不涉及。 **取值范围：** fixed：内网IP，floating：弹性公网IP。 **默认取值：** 不涉及。

        :param ip_type: The ip_type of this CountResourcesRequest.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def ip(self):
        r"""Gets the ip of this CountResourcesRequest.

        **参数解释：** 云资源IP。 **约束限制：** 不涉及。 **取值范围：** IPv4地址过滤结果，匹配规则为模糊匹配。 **默认取值：** 不涉及。

        :return: The ip of this CountResourcesRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this CountResourcesRequest.

        **参数解释：** 云资源IP。 **约束限制：** 不涉及。 **取值范围：** IPv4地址过滤结果，匹配规则为模糊匹配。 **默认取值：** 不涉及。

        :param ip: The ip of this CountResourcesRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def status(self):
        r"""Gets the status of this CountResourcesRequest.

        **参数解释：** 云资源状态。 **约束限制：** 不涉及。 **取值范围：** 请选择[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws)[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws_hk)中存在的云服务器状态。 **默认取值：** 不涉及。

        :return: The status of this CountResourcesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountResourcesRequest.

        **参数解释：** 云资源状态。 **约束限制：** 不涉及。 **取值范围：** 请选择[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws)[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws_hk)中存在的云服务器状态。 **默认取值：** 不涉及。

        :param status: The status of this CountResourcesRequest.
        :type status: str
        """
        self._status = status

    @property
    def agent_state(self):
        r"""Gets the agent_state of this CountResourcesRequest.

        **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - 运行中。 - 异常。 - 安装中。 - 安装失败。 - 已卸载。 - 未安装。 **默认取值：** 不涉及。

        :return: The agent_state of this CountResourcesRequest.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this CountResourcesRequest.

        **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - 运行中。 - 异常。 - 安装中。 - 安装失败。 - 已卸载。 - 未安装。 **默认取值：** 不涉及。

        :param agent_state: The agent_state of this CountResourcesRequest.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def image_name(self):
        r"""Gets the image_name of this CountResourcesRequest.

        **参数解释：** 镜像名称，模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The image_name of this CountResourcesRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CountResourcesRequest.

        **参数解释：** 镜像名称，模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param image_name: The image_name of this CountResourcesRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def os_type(self):
        r"""Gets the os_type of this CountResourcesRequest.

        **参数解释：** 系统类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The os_type of this CountResourcesRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this CountResourcesRequest.

        **参数解释：** 系统类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param os_type: The os_type of this CountResourcesRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def tag(self):
        r"""Gets the tag of this CountResourcesRequest.

        **参数解释：** 云资源的标签。 **约束限制：** 标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。 **取值范围：** 标签命名时，需满足如下要求：标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）以及中文字符。 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）、小数点（.）以及中文字符。 **默认取值：** 不涉及。

        :return: The tag of this CountResourcesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this CountResourcesRequest.

        **参数解释：** 云资源的标签。 **约束限制：** 标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。 **取值范围：** 标签命名时，需满足如下要求：标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）以及中文字符。 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）、小数点（.）以及中文字符。 **默认取值：** 不涉及。

        :param tag: The tag of this CountResourcesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def tag_key(self):
        r"""Gets the tag_key of this CountResourcesRequest.

        **参数解释：** 云资源的标签key。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tag_key of this CountResourcesRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        r"""Sets the tag_key of this CountResourcesRequest.

        **参数解释：** 云资源的标签key。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tag_key: The tag_key of this CountResourcesRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

    @property
    def group_id(self):
        r"""Gets the group_id of this CountResourcesRequest.

        **参数解释：** 云资源下的分组ID。 **约束限制：** 不涉及。 **取值范围：** 设置null值时获取未绑定分组的资源。 **默认取值：** 不涉及。

        :return: The group_id of this CountResourcesRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this CountResourcesRequest.

        **参数解释：** 云资源下的分组ID。 **约束限制：** 不涉及。 **取值范围：** 设置null值时获取未绑定分组的资源。 **默认取值：** 不涉及。

        :param group_id: The group_id of this CountResourcesRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def component_id(self):
        r"""Gets the component_id of this CountResourcesRequest.

        **参数解释：** 云资源下组件ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The component_id of this CountResourcesRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this CountResourcesRequest.

        **参数解释：** 云资源下组件ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param component_id: The component_id of this CountResourcesRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def application_id(self):
        r"""Gets the application_id of this CountResourcesRequest.

        **参数解释：** 云资源下应用ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The application_id of this CountResourcesRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this CountResourcesRequest.

        **参数解释：** 云资源下应用ID。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param application_id: The application_id of this CountResourcesRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def cce_cluster_id(self):
        r"""Gets the cce_cluster_id of this CountResourcesRequest.

        **参数解释：** cce集群ID。 **约束限制：** 不涉及。 **取值范围：** 资源属于的cce的ID。 **默认取值：** 不涉及。

        :return: The cce_cluster_id of this CountResourcesRequest.
        :rtype: str
        """
        return self._cce_cluster_id

    @cce_cluster_id.setter
    def cce_cluster_id(self, cce_cluster_id):
        r"""Sets the cce_cluster_id of this CountResourcesRequest.

        **参数解释：** cce集群ID。 **约束限制：** 不涉及。 **取值范围：** 资源属于的cce的ID。 **默认取值：** 不涉及。

        :param cce_cluster_id: The cce_cluster_id of this CountResourcesRequest.
        :type cce_cluster_id: str
        """
        self._cce_cluster_id = cce_cluster_id

    @property
    def ep_id(self):
        r"""Gets the ep_id of this CountResourcesRequest.

        **参数解释：** 企业项目id。 **约束限制：** 不涉及。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。 **默认取值：** 不涉及。

        :return: The ep_id of this CountResourcesRequest.
        :rtype: str
        """
        return self._ep_id

    @ep_id.setter
    def ep_id(self, ep_id):
        r"""Sets the ep_id of this CountResourcesRequest.

        **参数解释：** 企业项目id。 **约束限制：** 不涉及。 **取值范围：** 请选择[[企业管理](https://support.huaweicloud.com/usermanual-em/em_eps_qs_0400.html)](tag:hws)[[企业管理](https://support.huaweicloud.com/intl/zh-cn/usermanual-em/em_eps_qs_0400.html)](tag:hws_hk)中存在的项目ID。 **默认取值：** 不涉及。

        :param ep_id: The ep_id of this CountResourcesRequest.
        :type ep_id: str
        """
        self._ep_id = ep_id

    @property
    def is_delegated(self):
        r"""Gets the is_delegated of this CountResourcesRequest.

        **参数解释：** 是否已托管。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The is_delegated of this CountResourcesRequest.
        :rtype: str
        """
        return self._is_delegated

    @is_delegated.setter
    def is_delegated(self, is_delegated):
        r"""Sets the is_delegated of this CountResourcesRequest.

        **参数解释：** 是否已托管。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param is_delegated: The is_delegated of this CountResourcesRequest.
        :type is_delegated: str
        """
        self._is_delegated = is_delegated

    @property
    def is_collected(self):
        r"""Gets the is_collected of this CountResourcesRequest.

        **参数解释：** 是否已收藏。 **约束限制：** 不涉及。 **取值范围：** - true：已收藏的企业项目。 - false：未收藏的企业项目。 **默认取值：** 不涉及。

        :return: The is_collected of this CountResourcesRequest.
        :rtype: bool
        """
        return self._is_collected

    @is_collected.setter
    def is_collected(self, is_collected):
        r"""Sets the is_collected of this CountResourcesRequest.

        **参数解释：** 是否已收藏。 **约束限制：** 不涉及。 **取值范围：** - true：已收藏的企业项目。 - false：未收藏的企业项目。 **默认取值：** 不涉及。

        :param is_collected: The is_collected of this CountResourcesRequest.
        :type is_collected: bool
        """
        self._is_collected = is_collected

    @property
    def flavor_name(self):
        r"""Gets the flavor_name of this CountResourcesRequest.

        **参数解释：** 云资源规格名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The flavor_name of this CountResourcesRequest.
        :rtype: str
        """
        return self._flavor_name

    @flavor_name.setter
    def flavor_name(self, flavor_name):
        r"""Sets the flavor_name of this CountResourcesRequest.

        **参数解释：** 云资源规格名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param flavor_name: The flavor_name of this CountResourcesRequest.
        :type flavor_name: str
        """
        self._flavor_name = flavor_name

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this CountResourcesRequest.

        **参数解释：** 云服务器的计费类型。 **约束限制：** 不涉及。 **取值范围：** 计费模式： - 0：按需计费。 - 1：包年包月。 - 2：竞价计费。 **默认取值：** 不涉及。

        :return: The charging_mode of this CountResourcesRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this CountResourcesRequest.

        **参数解释：** 云服务器的计费类型。 **约束限制：** 不涉及。 **取值范围：** 计费模式： - 0：按需计费。 - 1：包年包月。 - 2：竞价计费。 **默认取值：** 不涉及。

        :param charging_mode: The charging_mode of this CountResourcesRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

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
        if not isinstance(other, CountResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
