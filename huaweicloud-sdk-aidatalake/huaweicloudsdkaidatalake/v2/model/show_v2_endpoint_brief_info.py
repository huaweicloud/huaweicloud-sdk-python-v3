# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowV2EndpointBriefInfo:

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
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'status': 'str',
        'engine': 'dict(str, object)',
        'capacity': 'list[V2EndpointCapacityItem]',
        'resource_type': 'ResourceType',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'compute_id': 'str',
        'credential': 'CredentialConfig',
        'creator': 'Creator',
        'tags': 'list[ResourceTag]',
        'error': 'Error'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'display_name': 'display_name',
        'description': 'description',
        'status': 'status',
        'engine': 'engine',
        'capacity': 'capacity',
        'resource_type': 'resource_type',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'compute_id': 'compute_id',
        'credential': 'credential',
        'creator': 'creator',
        'tags': 'tags',
        'error': 'error'
    }

    def __init__(self, id=None, name=None, display_name=None, description=None, status=None, engine=None, capacity=None, resource_type=None, create_time=None, update_time=None, compute_id=None, credential=None, creator=None, tags=None, error=None):
        r"""ShowV2EndpointBriefInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。
        :type id: str
        :param name: **参数解释**：端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 
        :type name: str
        :param display_name: **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 
        :type display_name: str
        :param description: **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 
        :type description: str
        :param status: **参数解释**：Endpoint状态。 **取值范围**：   - CREATING：创建中。   - RUNNING：运行中。   - CREATE_FAILED：创建失败。   - DELETING：删除中。   - DELETED：已删除。   - UPDATING：更新中。   - UPDATE_FAILED：更新失败。   - DELETE_FAILED：删除失败。   - FROZEN：冻结。   - TRIAL_ENDED：试用结束。   - ON_DEMAND_FROZEN：按需冻结。 
        :type status: str
        :param engine: **参数解释**：引擎配置。 
        :type engine: dict(str, object)
        :param capacity: **参数解释**：计算资源容量配置。 
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkaidatalake.v2.ResourceType`
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param update_time: **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type update_time: datetime
        :param compute_id: **参数解释**：计算资源ID。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 
        :type compute_id: str
        :param credential: 
        :type credential: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        :param creator: 
        :type creator: :class:`huaweicloudsdkaidatalake.v2.Creator`
        :param tags: **参数解释**：资源标签列表，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        :param error: 
        :type error: :class:`huaweicloudsdkaidatalake.v2.Error`
        """
        
        

        self._id = None
        self._name = None
        self._display_name = None
        self._description = None
        self._status = None
        self._engine = None
        self._capacity = None
        self._resource_type = None
        self._create_time = None
        self._update_time = None
        self._compute_id = None
        self._credential = None
        self._creator = None
        self._tags = None
        self._error = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if engine is not None:
            self.engine = engine
        if capacity is not None:
            self.capacity = capacity
        if resource_type is not None:
            self.resource_type = resource_type
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if compute_id is not None:
            self.compute_id = compute_id
        if credential is not None:
            self.credential = credential
        if creator is not None:
            self.creator = creator
        if tags is not None:
            self.tags = tags
        if error is not None:
            self.error = error

    @property
    def id(self):
        r"""Gets the id of this ShowV2EndpointBriefInfo.

        **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :return: The id of this ShowV2EndpointBriefInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowV2EndpointBriefInfo.

        **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :param id: The id of this ShowV2EndpointBriefInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowV2EndpointBriefInfo.

        **参数解释**：端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 

        :return: The name of this ShowV2EndpointBriefInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowV2EndpointBriefInfo.

        **参数解释**：端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 

        :param name: The name of this ShowV2EndpointBriefInfo.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this ShowV2EndpointBriefInfo.

        **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 

        :return: The display_name of this ShowV2EndpointBriefInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this ShowV2EndpointBriefInfo.

        **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 

        :param display_name: The display_name of this ShowV2EndpointBriefInfo.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this ShowV2EndpointBriefInfo.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :return: The description of this ShowV2EndpointBriefInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowV2EndpointBriefInfo.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :param description: The description of this ShowV2EndpointBriefInfo.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this ShowV2EndpointBriefInfo.

        **参数解释**：Endpoint状态。 **取值范围**：   - CREATING：创建中。   - RUNNING：运行中。   - CREATE_FAILED：创建失败。   - DELETING：删除中。   - DELETED：已删除。   - UPDATING：更新中。   - UPDATE_FAILED：更新失败。   - DELETE_FAILED：删除失败。   - FROZEN：冻结。   - TRIAL_ENDED：试用结束。   - ON_DEMAND_FROZEN：按需冻结。 

        :return: The status of this ShowV2EndpointBriefInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowV2EndpointBriefInfo.

        **参数解释**：Endpoint状态。 **取值范围**：   - CREATING：创建中。   - RUNNING：运行中。   - CREATE_FAILED：创建失败。   - DELETING：删除中。   - DELETED：已删除。   - UPDATING：更新中。   - UPDATE_FAILED：更新失败。   - DELETE_FAILED：删除失败。   - FROZEN：冻结。   - TRIAL_ENDED：试用结束。   - ON_DEMAND_FROZEN：按需冻结。 

        :param status: The status of this ShowV2EndpointBriefInfo.
        :type status: str
        """
        self._status = status

    @property
    def engine(self):
        r"""Gets the engine of this ShowV2EndpointBriefInfo.

        **参数解释**：引擎配置。 

        :return: The engine of this ShowV2EndpointBriefInfo.
        :rtype: dict(str, object)
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this ShowV2EndpointBriefInfo.

        **参数解释**：引擎配置。 

        :param engine: The engine of this ShowV2EndpointBriefInfo.
        :type engine: dict(str, object)
        """
        self._engine = engine

    @property
    def capacity(self):
        r"""Gets the capacity of this ShowV2EndpointBriefInfo.

        **参数解释**：计算资源容量配置。 

        :return: The capacity of this ShowV2EndpointBriefInfo.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this ShowV2EndpointBriefInfo.

        **参数解释**：计算资源容量配置。 

        :param capacity: The capacity of this ShowV2EndpointBriefInfo.
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        """
        self._capacity = capacity

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowV2EndpointBriefInfo.

        :return: The resource_type of this ShowV2EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowV2EndpointBriefInfo.

        :param resource_type: The resource_type of this ShowV2EndpointBriefInfo.
        :type resource_type: :class:`huaweicloudsdkaidatalake.v2.ResourceType`
        """
        self._resource_type = resource_type

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowV2EndpointBriefInfo.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this ShowV2EndpointBriefInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowV2EndpointBriefInfo.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this ShowV2EndpointBriefInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowV2EndpointBriefInfo.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The update_time of this ShowV2EndpointBriefInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowV2EndpointBriefInfo.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param update_time: The update_time of this ShowV2EndpointBriefInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def compute_id(self):
        r"""Gets the compute_id of this ShowV2EndpointBriefInfo.

        **参数解释**：计算资源ID。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 

        :return: The compute_id of this ShowV2EndpointBriefInfo.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        r"""Sets the compute_id of this ShowV2EndpointBriefInfo.

        **参数解释**：计算资源ID。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 

        :param compute_id: The compute_id of this ShowV2EndpointBriefInfo.
        :type compute_id: str
        """
        self._compute_id = compute_id

    @property
    def credential(self):
        r"""Gets the credential of this ShowV2EndpointBriefInfo.

        :return: The credential of this ShowV2EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        r"""Sets the credential of this ShowV2EndpointBriefInfo.

        :param credential: The credential of this ShowV2EndpointBriefInfo.
        :type credential: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        """
        self._credential = credential

    @property
    def creator(self):
        r"""Gets the creator of this ShowV2EndpointBriefInfo.

        :return: The creator of this ShowV2EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.Creator`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowV2EndpointBriefInfo.

        :param creator: The creator of this ShowV2EndpointBriefInfo.
        :type creator: :class:`huaweicloudsdkaidatalake.v2.Creator`
        """
        self._creator = creator

    @property
    def tags(self):
        r"""Gets the tags of this ShowV2EndpointBriefInfo.

        **参数解释**：资源标签列表，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 

        :return: The tags of this ShowV2EndpointBriefInfo.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowV2EndpointBriefInfo.

        **参数解释**：资源标签列表，每个元素为一个ResourceTag对象，包含key（标签键）和value（标签值）字段。 

        :param tags: The tags of this ShowV2EndpointBriefInfo.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.ResourceTag`]
        """
        self._tags = tags

    @property
    def error(self):
        r"""Gets the error of this ShowV2EndpointBriefInfo.

        :return: The error of this ShowV2EndpointBriefInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.Error`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this ShowV2EndpointBriefInfo.

        :param error: The error of this ShowV2EndpointBriefInfo.
        :type error: :class:`huaweicloudsdkaidatalake.v2.Error`
        """
        self._error = error

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
        if not isinstance(other, ShowV2EndpointBriefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
