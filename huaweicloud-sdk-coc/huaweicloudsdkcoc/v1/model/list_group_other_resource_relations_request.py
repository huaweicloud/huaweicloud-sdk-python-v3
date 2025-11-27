# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupOtherResourceRelationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'component_id': 'str',
        'group_id': 'str',
        'vendor': 'str',
        'type': 'str',
        'limit': 'int',
        'offset': 'str',
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
        'charging_mode': 'str',
        'flavor_name': 'str',
        'ip_list': 'list[str]',
        'is_collected': 'bool'
    }

    attribute_map = {
        'application_id': 'application_id',
        'component_id': 'component_id',
        'group_id': 'group_id',
        'vendor': 'vendor',
        'type': 'type',
        'limit': 'limit',
        'offset': 'offset',
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
        'charging_mode': 'charging_mode',
        'flavor_name': 'flavor_name',
        'ip_list': 'ip_list',
        'is_collected': 'is_collected'
    }

    def __init__(self, application_id=None, component_id=None, group_id=None, vendor=None, type=None, limit=None, offset=None, resource_id_list=None, name=None, region_id=None, az_id=None, ip_type=None, ip=None, status=None, agent_state=None, image_name=None, os_type=None, tag=None, charging_mode=None, flavor_name=None, ip_list=None, is_collected=None):
        r"""ListGroupOtherResourceRelationsRequest

        The model defined in huaweicloud sdk

        :param application_id: **参数解释：** 分组关联的应用id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 分组关联的应用id。 **默认取值：** 不涉及。
        :type application_id: str
        :param component_id: **参数解释：** 组件id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 分组关联的组件id。 **默认取值：** 不涉及。
        :type component_id: str
        :param group_id: **参数解释：** 分组id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type group_id: str
        :param vendor: **参数解释：** 厂商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。 **默认取值：** 不涉及。
        :type vendor: str
        :param type: **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** 自定义，云资源类型。 **默认取值：** 不涉及。
        :type type: str
        :param limit: **参数解释：** 用于分页查询，查询数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。
        :type limit: int
        :param offset: **参数解释：** 分页查询偏移量，表示从此偏移量开始查询。 **约束限制：** 不涉及。 **取值范围：** 0-2147483647。 **默认取值：** 0。
        :type offset: str
        :param resource_id_list: **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 资源id列表，最大值100。 **默认取值：** 不涉及。
        :type resource_id_list: list[str]
        :param name: **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。
        :type name: str
        :param region_id: **参数解释：** 区域id列表。 **约束限制：** 不涉及。 **取值范围：** 区域id列表，最大值100。 **默认取值：** 不涉及。
        :type region_id: str
        :param az_id: **参数解释：** 可用区id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type az_id: str
        :param ip_type: **参数解释：** ip类型。 **约束限制：** 不涉及。 **取值范围：** fixed：内网IP。 floating：弹性公网IP。 **默认取值：** 不涉及。
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
        :param charging_mode: **参数解释：** 云服务器的计费类型。 **约束限制：** 不涉及。 **取值范围：** 计费模式： - 0：按需计费。 - 1：包年包月。 - 2：竞价计费。 **默认取值：** 不涉及。
        :type charging_mode: str
        :param flavor_name: **参数解释：** 规格名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type flavor_name: str
        :param ip_list: **参数解释：** ip列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type ip_list: list[str]
        :param is_collected: **参数解释：** 是否已收藏。 **约束限制：** 不涉及。 **取值范围：** - true：查询已收藏分组管理的资源关联。 - false：查询未收藏分组管理的资源关联。 **默认取值：** 不涉及。
        :type is_collected: bool
        """
        
        

        self._application_id = None
        self._component_id = None
        self._group_id = None
        self._vendor = None
        self._type = None
        self._limit = None
        self._offset = None
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
        self._charging_mode = None
        self._flavor_name = None
        self._ip_list = None
        self._is_collected = None
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if component_id is not None:
            self.component_id = component_id
        if group_id is not None:
            self.group_id = group_id
        self.vendor = vendor
        self.type = type
        self.limit = limit
        if offset is not None:
            self.offset = offset
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
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if flavor_name is not None:
            self.flavor_name = flavor_name
        if ip_list is not None:
            self.ip_list = ip_list
        if is_collected is not None:
            self.is_collected = is_collected

    @property
    def application_id(self):
        r"""Gets the application_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 分组关联的应用id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 分组关联的应用id。 **默认取值：** 不涉及。

        :return: The application_id of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 分组关联的应用id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 分组关联的应用id。 **默认取值：** 不涉及。

        :param application_id: The application_id of this ListGroupOtherResourceRelationsRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def component_id(self):
        r"""Gets the component_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 组件id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 分组关联的组件id。 **默认取值：** 不涉及。

        :return: The component_id of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 组件id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 分组关联的组件id。 **默认取值：** 不涉及。

        :param component_id: The component_id of this ListGroupOtherResourceRelationsRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 分组id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The group_id of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 分组id。 **约束限制：** 应用id和分组id，组件id不能共存,且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param group_id: The group_id of this ListGroupOtherResourceRelationsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def vendor(self):
        r"""Gets the vendor of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 厂商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。 **默认取值：** 不涉及。

        :return: The vendor of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 厂商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。 **默认取值：** 不涉及。

        :param vendor: The vendor of this ListGroupOtherResourceRelationsRequest.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def type(self):
        r"""Gets the type of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** 自定义，云资源类型。 **默认取值：** 不涉及。

        :return: The type of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 资源类型。 **约束限制：** 不涉及。 **取值范围：** 自定义，云资源类型。 **默认取值：** 不涉及。

        :param type: The type of this ListGroupOtherResourceRelationsRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 用于分页查询，查询数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。

        :return: The limit of this ListGroupOtherResourceRelationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 用于分页查询，查询数量。 **约束限制：** 不涉及。 **取值范围：** 自定义，在1-500范围。 **默认取值：** 不涉及。

        :param limit: The limit of this ListGroupOtherResourceRelationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 分页查询偏移量，表示从此偏移量开始查询。 **约束限制：** 不涉及。 **取值范围：** 0-2147483647。 **默认取值：** 0。

        :return: The offset of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 分页查询偏移量，表示从此偏移量开始查询。 **约束限制：** 不涉及。 **取值范围：** 0-2147483647。 **默认取值：** 0。

        :param offset: The offset of this ListGroupOtherResourceRelationsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def resource_id_list(self):
        r"""Gets the resource_id_list of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 资源id列表，最大值100。 **默认取值：** 不涉及。

        :return: The resource_id_list of this ListGroupOtherResourceRelationsRequest.
        :rtype: list[str]
        """
        return self._resource_id_list

    @resource_id_list.setter
    def resource_id_list(self, resource_id_list):
        r"""Sets the resource_id_list of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 资源id列表，最大值100。 **默认取值：** 不涉及。

        :param resource_id_list: The resource_id_list of this ListGroupOtherResourceRelationsRequest.
        :type resource_id_list: list[str]
        """
        self._resource_id_list = resource_id_list

    @property
    def name(self):
        r"""Gets the name of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。

        :return: The name of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。

        :param name: The name of this ListGroupOtherResourceRelationsRequest.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 区域id列表。 **约束限制：** 不涉及。 **取值范围：** 区域id列表，最大值100。 **默认取值：** 不涉及。

        :return: The region_id of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 区域id列表。 **约束限制：** 不涉及。 **取值范围：** 区域id列表，最大值100。 **默认取值：** 不涉及。

        :param region_id: The region_id of this ListGroupOtherResourceRelationsRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def az_id(self):
        r"""Gets the az_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 可用区id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The az_id of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._az_id

    @az_id.setter
    def az_id(self, az_id):
        r"""Sets the az_id of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 可用区id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param az_id: The az_id of this ListGroupOtherResourceRelationsRequest.
        :type az_id: str
        """
        self._az_id = az_id

    @property
    def ip_type(self):
        r"""Gets the ip_type of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** ip类型。 **约束限制：** 不涉及。 **取值范围：** fixed：内网IP。 floating：弹性公网IP。 **默认取值：** 不涉及。

        :return: The ip_type of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** ip类型。 **约束限制：** 不涉及。 **取值范围：** fixed：内网IP。 floating：弹性公网IP。 **默认取值：** 不涉及。

        :param ip_type: The ip_type of this ListGroupOtherResourceRelationsRequest.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def ip(self):
        r"""Gets the ip of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云资源IP。 **约束限制：** 不涉及。 **取值范围：** IPv4地址过滤结果，匹配规则为模糊匹配。 **默认取值：** 不涉及。

        :return: The ip of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云资源IP。 **约束限制：** 不涉及。 **取值范围：** IPv4地址过滤结果，匹配规则为模糊匹配。 **默认取值：** 不涉及。

        :param ip: The ip of this ListGroupOtherResourceRelationsRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def status(self):
        r"""Gets the status of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云资源状态。 **约束限制：** 不涉及。 **取值范围：** 请选择[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws)[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws_hk)中存在的云服务器状态。 **默认取值：** 不涉及。

        :return: The status of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云资源状态。 **约束限制：** 不涉及。 **取值范围：** 请选择[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws)[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws_hk)中存在的云服务器状态。 **默认取值：** 不涉及。

        :param status: The status of this ListGroupOtherResourceRelationsRequest.
        :type status: str
        """
        self._status = status

    @property
    def agent_state(self):
        r"""Gets the agent_state of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - 运行中。 - 异常。 - 安装中。 - 安装失败。 - 已卸载。 - 未安装。 **默认取值：** 不涉及。

        :return: The agent_state of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - 运行中。 - 异常。 - 安装中。 - 安装失败。 - 已卸载。 - 未安装。 **默认取值：** 不涉及。

        :param agent_state: The agent_state of this ListGroupOtherResourceRelationsRequest.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def image_name(self):
        r"""Gets the image_name of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 镜像名称，模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The image_name of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 镜像名称，模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param image_name: The image_name of this ListGroupOtherResourceRelationsRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 系统类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The os_type of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 系统类型。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param os_type: The os_type of this ListGroupOtherResourceRelationsRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def tag(self):
        r"""Gets the tag of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云资源的标签。 **约束限制：** 标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。 **取值范围：** 标签命名时，需满足如下要求：标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）以及中文字符。 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）、小数点（.）以及中文字符。 **默认取值：** 不涉及。

        :return: The tag of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云资源的标签。 **约束限制：** 标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。 **取值范围：** 标签命名时，需满足如下要求：标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）以及中文字符。 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）、小数点（.）以及中文字符。 **默认取值：** 不涉及。

        :param tag: The tag of this ListGroupOtherResourceRelationsRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云服务器的计费类型。 **约束限制：** 不涉及。 **取值范围：** 计费模式： - 0：按需计费。 - 1：包年包月。 - 2：竞价计费。 **默认取值：** 不涉及。

        :return: The charging_mode of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 云服务器的计费类型。 **约束限制：** 不涉及。 **取值范围：** 计费模式： - 0：按需计费。 - 1：包年包月。 - 2：竞价计费。 **默认取值：** 不涉及。

        :param charging_mode: The charging_mode of this ListGroupOtherResourceRelationsRequest.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def flavor_name(self):
        r"""Gets the flavor_name of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 规格名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The flavor_name of this ListGroupOtherResourceRelationsRequest.
        :rtype: str
        """
        return self._flavor_name

    @flavor_name.setter
    def flavor_name(self, flavor_name):
        r"""Sets the flavor_name of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 规格名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param flavor_name: The flavor_name of this ListGroupOtherResourceRelationsRequest.
        :type flavor_name: str
        """
        self._flavor_name = flavor_name

    @property
    def ip_list(self):
        r"""Gets the ip_list of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** ip列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The ip_list of this ListGroupOtherResourceRelationsRequest.
        :rtype: list[str]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** ip列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param ip_list: The ip_list of this ListGroupOtherResourceRelationsRequest.
        :type ip_list: list[str]
        """
        self._ip_list = ip_list

    @property
    def is_collected(self):
        r"""Gets the is_collected of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 是否已收藏。 **约束限制：** 不涉及。 **取值范围：** - true：查询已收藏分组管理的资源关联。 - false：查询未收藏分组管理的资源关联。 **默认取值：** 不涉及。

        :return: The is_collected of this ListGroupOtherResourceRelationsRequest.
        :rtype: bool
        """
        return self._is_collected

    @is_collected.setter
    def is_collected(self, is_collected):
        r"""Sets the is_collected of this ListGroupOtherResourceRelationsRequest.

        **参数解释：** 是否已收藏。 **约束限制：** 不涉及。 **取值范围：** - true：查询已收藏分组管理的资源关联。 - false：查询未收藏分组管理的资源关联。 **默认取值：** 不涉及。

        :param is_collected: The is_collected of this ListGroupOtherResourceRelationsRequest.
        :type is_collected: bool
        """
        self._is_collected = is_collected

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
        if not isinstance(other, ListGroupOtherResourceRelationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
