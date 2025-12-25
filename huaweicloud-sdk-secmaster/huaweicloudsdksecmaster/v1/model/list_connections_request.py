# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'workspace_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'component_name': 'str',
        'creator_name': 'str',
        'modifier_name': 'str',
        'description': 'str',
        'create_start_time': 'str',
        'create_end_time': 'str',
        'update_start_time': 'str',
        'update_end_time': 'str',
        'is_defense_type': 'bool'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'component_name': 'component_name',
        'creator_name': 'creator_name',
        'modifier_name': 'modifier_name',
        'description': 'description',
        'create_start_time': 'create_start_time',
        'create_end_time': 'create_end_time',
        'update_start_time': 'update_start_time',
        'update_end_time': 'update_end_time',
        'is_defense_type': 'is_defense_type'
    }

    def __init__(self, project_id=None, workspace_id=None, offset=None, limit=None, name=None, component_name=None, creator_name=None, modifier_name=None, description=None, create_start_time=None, create_end_time=None, update_start_time=None, update_end_time=None, is_defense_type=None):
        r"""ListConnectionsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type project_id: str
        :param workspace_id: **参数解释**: 工作空间ID **取值范围**: 不涉及
        :type workspace_id: str
        :param offset: **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type offset: int
        :param limit: **参数解释：** 数据量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type limit: int
        :param name: 连接名称
        :type name: str
        :param component_name: 插件名称
        :type component_name: str
        :param creator_name: 创建人
        :type creator_name: str
        :param modifier_name: 修改人
        :type modifier_name: str
        :param description: 描述
        :type description: str
        :param create_start_time: 创建起始时间
        :type create_start_time: str
        :param create_end_time: 创建结束时间
        :type create_end_time: str
        :param update_start_time: 修改起始时间
        :type update_start_time: str
        :param update_end_time: 修改结束时间
        :type update_end_time: str
        :param is_defense_type: 是否用于应急策略的操作连接
        :type is_defense_type: bool
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._component_name = None
        self._creator_name = None
        self._modifier_name = None
        self._description = None
        self._create_start_time = None
        self._create_end_time = None
        self._update_start_time = None
        self._update_end_time = None
        self._is_defense_type = None
        self.discriminator = None

        self.project_id = project_id
        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if component_name is not None:
            self.component_name = component_name
        if creator_name is not None:
            self.creator_name = creator_name
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if description is not None:
            self.description = description
        if create_start_time is not None:
            self.create_start_time = create_start_time
        if create_end_time is not None:
            self.create_end_time = create_end_time
        if update_start_time is not None:
            self.update_start_time = update_start_time
        if update_end_time is not None:
            self.update_end_time = update_end_time
        if is_defense_type is not None:
            self.is_defense_type = is_defense_type

    @property
    def project_id(self):
        r"""Gets the project_id of this ListConnectionsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The project_id of this ListConnectionsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListConnectionsRequest.

        **参数解释：** 项目ID，用于明确项目归属，配置后可通过该ID查询项目下资产，可以通过调用API获取，也可以从控制台获取。[获取项目ID](secmaster_03_0014.xml) **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param project_id: The project_id of this ListConnectionsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListConnectionsRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :return: The workspace_id of this ListConnectionsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListConnectionsRequest.

        **参数解释**: 工作空间ID **取值范围**: 不涉及

        :param workspace_id: The workspace_id of this ListConnectionsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListConnectionsRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The offset of this ListConnectionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListConnectionsRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param offset: The offset of this ListConnectionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListConnectionsRequest.

        **参数解释：** 数据量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The limit of this ListConnectionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListConnectionsRequest.

        **参数解释：** 数据量 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param limit: The limit of this ListConnectionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListConnectionsRequest.

        连接名称

        :return: The name of this ListConnectionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListConnectionsRequest.

        连接名称

        :param name: The name of this ListConnectionsRequest.
        :type name: str
        """
        self._name = name

    @property
    def component_name(self):
        r"""Gets the component_name of this ListConnectionsRequest.

        插件名称

        :return: The component_name of this ListConnectionsRequest.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this ListConnectionsRequest.

        插件名称

        :param component_name: The component_name of this ListConnectionsRequest.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def creator_name(self):
        r"""Gets the creator_name of this ListConnectionsRequest.

        创建人

        :return: The creator_name of this ListConnectionsRequest.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this ListConnectionsRequest.

        创建人

        :param creator_name: The creator_name of this ListConnectionsRequest.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this ListConnectionsRequest.

        修改人

        :return: The modifier_name of this ListConnectionsRequest.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this ListConnectionsRequest.

        修改人

        :param modifier_name: The modifier_name of this ListConnectionsRequest.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def description(self):
        r"""Gets the description of this ListConnectionsRequest.

        描述

        :return: The description of this ListConnectionsRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListConnectionsRequest.

        描述

        :param description: The description of this ListConnectionsRequest.
        :type description: str
        """
        self._description = description

    @property
    def create_start_time(self):
        r"""Gets the create_start_time of this ListConnectionsRequest.

        创建起始时间

        :return: The create_start_time of this ListConnectionsRequest.
        :rtype: str
        """
        return self._create_start_time

    @create_start_time.setter
    def create_start_time(self, create_start_time):
        r"""Sets the create_start_time of this ListConnectionsRequest.

        创建起始时间

        :param create_start_time: The create_start_time of this ListConnectionsRequest.
        :type create_start_time: str
        """
        self._create_start_time = create_start_time

    @property
    def create_end_time(self):
        r"""Gets the create_end_time of this ListConnectionsRequest.

        创建结束时间

        :return: The create_end_time of this ListConnectionsRequest.
        :rtype: str
        """
        return self._create_end_time

    @create_end_time.setter
    def create_end_time(self, create_end_time):
        r"""Sets the create_end_time of this ListConnectionsRequest.

        创建结束时间

        :param create_end_time: The create_end_time of this ListConnectionsRequest.
        :type create_end_time: str
        """
        self._create_end_time = create_end_time

    @property
    def update_start_time(self):
        r"""Gets the update_start_time of this ListConnectionsRequest.

        修改起始时间

        :return: The update_start_time of this ListConnectionsRequest.
        :rtype: str
        """
        return self._update_start_time

    @update_start_time.setter
    def update_start_time(self, update_start_time):
        r"""Sets the update_start_time of this ListConnectionsRequest.

        修改起始时间

        :param update_start_time: The update_start_time of this ListConnectionsRequest.
        :type update_start_time: str
        """
        self._update_start_time = update_start_time

    @property
    def update_end_time(self):
        r"""Gets the update_end_time of this ListConnectionsRequest.

        修改结束时间

        :return: The update_end_time of this ListConnectionsRequest.
        :rtype: str
        """
        return self._update_end_time

    @update_end_time.setter
    def update_end_time(self, update_end_time):
        r"""Sets the update_end_time of this ListConnectionsRequest.

        修改结束时间

        :param update_end_time: The update_end_time of this ListConnectionsRequest.
        :type update_end_time: str
        """
        self._update_end_time = update_end_time

    @property
    def is_defense_type(self):
        r"""Gets the is_defense_type of this ListConnectionsRequest.

        是否用于应急策略的操作连接

        :return: The is_defense_type of this ListConnectionsRequest.
        :rtype: bool
        """
        return self._is_defense_type

    @is_defense_type.setter
    def is_defense_type(self, is_defense_type):
        r"""Sets the is_defense_type of this ListConnectionsRequest.

        是否用于应急策略的操作连接

        :param is_defense_type: The is_defense_type of this ListConnectionsRequest.
        :type is_defense_type: bool
        """
        self._is_defense_type = is_defense_type

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
        if not isinstance(other, ListConnectionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
