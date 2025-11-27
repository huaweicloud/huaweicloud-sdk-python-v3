# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountGroupRmsResourceRelationsRequest:

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
        'group_id': 'str',
        'provider': 'str',
        'type': 'str',
        'vendor': 'str',
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
        'tag': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'group_id': 'group_id',
        'provider': 'provider',
        'type': 'type',
        'vendor': 'vendor',
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
        'tag': 'tag'
    }

    def __init__(self, application_id=None, group_id=None, provider=None, type=None, vendor=None, resource_id_list=None, name=None, region_id=None, az_id=None, ip_type=None, ip=None, status=None, agent_state=None, image_name=None, os_type=None, tag=None):
        r"""CountGroupRmsResourceRelationsRequest

        The model defined in huaweicloud sdk

        :param application_id: **参数解释：** 应用id。 **约束限制：** 应用id，和分组id不能共存，且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type application_id: str
        :param group_id: **参数解释：** 分组id。 **约束限制：** 分组id，和应用id不能共存，且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type group_id: str
        :param provider: **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type provider: str
        :param type: **参数解释：** 云服务资源类型。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。
        :type type: str
        :param vendor: **参数解释：** 厂商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。 **默认取值：** 不涉及
        :type vendor: str
        :param resource_id_list: **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 用户选择的资源id组成的集合。 **默认取值：** 不涉及。
        :type resource_id_list: list[str]
        :param name: **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。
        :type name: str
        :param region_id: **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。
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
        :param os_type: **参数解释：** 系统类型。 **约束限制：** 不涉及。 **取值范围：** - windows：windows操作系统类型。 - linux：linux操作系统类型。 **默认取值：** 不涉及。
        :type os_type: str
        :param tag: **参数解释：** 云资源的标签。 **约束限制：** 标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。 **取值范围：** 标签命名时，需满足如下要求：标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）以及中文字符。 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）、小数点（.）以及中文字符。 **默认取值：** 不涉及。
        :type tag: str
        """
        
        

        self._application_id = None
        self._group_id = None
        self._provider = None
        self._type = None
        self._vendor = None
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
        self.discriminator = None

        if application_id is not None:
            self.application_id = application_id
        if group_id is not None:
            self.group_id = group_id
        self.provider = provider
        self.type = type
        self.vendor = vendor
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

    @property
    def application_id(self):
        r"""Gets the application_id of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 应用id。 **约束限制：** 应用id，和分组id不能共存，且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The application_id of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 应用id。 **约束限制：** 应用id，和分组id不能共存，且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param application_id: The application_id of this CountGroupRmsResourceRelationsRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def group_id(self):
        r"""Gets the group_id of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 分组id。 **约束限制：** 分组id，和应用id不能共存，且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The group_id of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 分组id。 **约束限制：** 分组id，和应用id不能共存，且必填其中一个。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param group_id: The group_id of this CountGroupRmsResourceRelationsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def provider(self):
        r"""Gets the provider of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The provider of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        r"""Sets the provider of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云服务名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param provider: The provider of this CountGroupRmsResourceRelationsRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def type(self):
        r"""Gets the type of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云服务资源类型。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。

        :return: The type of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云服务资源类型。 **约束限制：** 不涉及。 **取值范围：** 资源类型较多，根据实际业务选择资源类型、常用资源类型如下： - cloudservers：弹性云服务器。 - servers：裸金属服务器。 - clusters：云容器引擎。 - instances：云数据库。 **默认取值：** 不涉及。

        :param type: The type of this CountGroupRmsResourceRelationsRequest.
        :type type: str
        """
        self._type = type

    @property
    def vendor(self):
        r"""Gets the vendor of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 厂商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。 **默认取值：** 不涉及

        :return: The vendor of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        r"""Sets the vendor of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 厂商信息。 **约束限制：** 不涉及。 **取值范围：** - RMS：华为云厂商。 - ALI：阿里云厂商。 - OTHER：其他厂商。 **默认取值：** 不涉及

        :param vendor: The vendor of this CountGroupRmsResourceRelationsRequest.
        :type vendor: str
        """
        self._vendor = vendor

    @property
    def resource_id_list(self):
        r"""Gets the resource_id_list of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 用户选择的资源id组成的集合。 **默认取值：** 不涉及。

        :return: The resource_id_list of this CountGroupRmsResourceRelationsRequest.
        :rtype: list[str]
        """
        return self._resource_id_list

    @resource_id_list.setter
    def resource_id_list(self, resource_id_list):
        r"""Sets the resource_id_list of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 资源id列表。 **约束限制：** 不涉及。 **取值范围：** 用户选择的资源id组成的集合。 **默认取值：** 不涉及。

        :param resource_id_list: The resource_id_list of this CountGroupRmsResourceRelationsRequest.
        :type resource_id_list: list[str]
        """
        self._resource_id_list = resource_id_list

    @property
    def name(self):
        r"""Gets the name of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。

        :return: The name of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云资源名称。 **约束限制：** 不涉及。 **取值范围：** 自定义，可参考：裸金属服务器BMS。 **默认取值：** 不涉及。

        :param name: The name of this CountGroupRmsResourceRelationsRequest.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。

        :return: The region_id of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 关联的区域region的id。 **默认取值：** 不涉及。

        :param region_id: The region_id of this CountGroupRmsResourceRelationsRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def az_id(self):
        r"""Gets the az_id of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 可用区id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The az_id of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._az_id

    @az_id.setter
    def az_id(self, az_id):
        r"""Sets the az_id of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 可用区id。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param az_id: The az_id of this CountGroupRmsResourceRelationsRequest.
        :type az_id: str
        """
        self._az_id = az_id

    @property
    def ip_type(self):
        r"""Gets the ip_type of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** ip类型。 **约束限制：** 不涉及。 **取值范围：** fixed：内网IP。 floating：弹性公网IP。 **默认取值：** 不涉及。

        :return: The ip_type of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        r"""Sets the ip_type of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** ip类型。 **约束限制：** 不涉及。 **取值范围：** fixed：内网IP。 floating：弹性公网IP。 **默认取值：** 不涉及。

        :param ip_type: The ip_type of this CountGroupRmsResourceRelationsRequest.
        :type ip_type: str
        """
        self._ip_type = ip_type

    @property
    def ip(self):
        r"""Gets the ip of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云资源IP。 **约束限制：** 不涉及。 **取值范围：** IPv4地址过滤结果，匹配规则为模糊匹配。 **默认取值：** 不涉及。

        :return: The ip of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云资源IP。 **约束限制：** 不涉及。 **取值范围：** IPv4地址过滤结果，匹配规则为模糊匹配。 **默认取值：** 不涉及。

        :param ip: The ip of this CountGroupRmsResourceRelationsRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def status(self):
        r"""Gets the status of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云资源状态。 **约束限制：** 不涉及。 **取值范围：** 请选择[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws)[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws_hk)中存在的云服务器状态。 **默认取值：** 不涉及。

        :return: The status of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云资源状态。 **约束限制：** 不涉及。 **取值范围：** 请选择[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws)[[弹性云服务器 ECS](https://support.huaweicloud.com/api-ecs/ecs_08_0002.html)](tag:hws_hk)中存在的云服务器状态。 **默认取值：** 不涉及。

        :param status: The status of this CountGroupRmsResourceRelationsRequest.
        :type status: str
        """
        self._status = status

    @property
    def agent_state(self):
        r"""Gets the agent_state of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - 运行中。 - 异常。 - 安装中。 - 安装失败。 - 已卸载。 - 未安装。 **默认取值：** 不涉及。

        :return: The agent_state of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._agent_state

    @agent_state.setter
    def agent_state(self, agent_state):
        r"""Sets the agent_state of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** agent状态。 **约束限制：** 不涉及。 **取值范围：** - 运行中。 - 异常。 - 安装中。 - 安装失败。 - 已卸载。 - 未安装。 **默认取值：** 不涉及。

        :param agent_state: The agent_state of this CountGroupRmsResourceRelationsRequest.
        :type agent_state: str
        """
        self._agent_state = agent_state

    @property
    def image_name(self):
        r"""Gets the image_name of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 镜像名称，模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The image_name of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 镜像名称，模糊匹配。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param image_name: The image_name of this CountGroupRmsResourceRelationsRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def os_type(self):
        r"""Gets the os_type of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 系统类型。 **约束限制：** 不涉及。 **取值范围：** - windows：windows操作系统类型。 - linux：linux操作系统类型。 **默认取值：** 不涉及。

        :return: The os_type of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 系统类型。 **约束限制：** 不涉及。 **取值范围：** - windows：windows操作系统类型。 - linux：linux操作系统类型。 **默认取值：** 不涉及。

        :param os_type: The os_type of this CountGroupRmsResourceRelationsRequest.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def tag(self):
        r"""Gets the tag of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云资源的标签。 **约束限制：** 标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。 **取值范围：** 标签命名时，需满足如下要求：标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）以及中文字符。 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）、小数点（.）以及中文字符。 **默认取值：** 不涉及。

        :return: The tag of this CountGroupRmsResourceRelationsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this CountGroupRmsResourceRelationsRequest.

        **参数解释：** 云资源的标签。 **约束限制：** 标签的格式为“key.value”。其中，key的长度不超过36个字符，value的长度不超过43个字符。 **取值范围：** 标签命名时，需满足如下要求：标签的key值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）以及中文字符。 标签的value值只能包含大写字母（A~Z）、小写字母（a~z）、数字（0-9）、下划线（）、中划线（-）、小数点（.）以及中文字符。 **默认取值：** 不涉及。

        :param tag: The tag of this CountGroupRmsResourceRelationsRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, CountGroupRmsResourceRelationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
