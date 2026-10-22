# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2ComputeInfo:

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
        'description': 'str',
        'charge_mode': 'ChargeMode',
        'capacity': 'list[ResourceCapacityItem]',
        'properties': 'dict(str, str)',
        'tags': 'list[Tag]',
        'prometheus_config': 'PrometheusConfig',
        'update_time': 'datetime',
        'create_time': 'datetime',
        'status': 'str',
        'creator': 'Creator',
        'error': 'Error'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'charge_mode': 'charge_mode',
        'capacity': 'capacity',
        'properties': 'properties',
        'tags': 'tags',
        'prometheus_config': 'prometheus_config',
        'update_time': 'update_time',
        'create_time': 'create_time',
        'status': 'status',
        'creator': 'creator',
        'error': 'error'
    }

    def __init__(self, id=None, name=None, description=None, charge_mode=None, capacity=None, properties=None, tags=None, prometheus_config=None, update_time=None, create_time=None, status=None, creator=None, error=None):
        r"""V2ComputeInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**：计算资源ID。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 
        :type id: str
        :param name: **参数解释**：计算资源名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 
        :type name: str
        :param description: **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 
        :type description: str
        :param charge_mode: 
        :type charge_mode: :class:`huaweicloudsdkaidatalake.v2.ChargeMode`
        :param capacity: **参数解释**：计算资源容量配置，由ResourceCapacityItem对象组成的数组，每个对象定义了资源类型、资源数量、资源规格和资源ID等信息。 
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.ResourceCapacityItem`]
        :param properties: **参数解释**：计算资源额外属性键值对映射。 
        :type properties: dict(str, str)
        :param tags: **参数解释**：标签列表，由Tag对象组成的数组，每个对象定义了标签键和标签值。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.Tag`]
        :param prometheus_config: 
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        :param update_time: **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type update_time: datetime
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param status: **参数解释**：资源状态。 **取值范围**：   - PREPARING：创建中。   - RELEASING：释放中。   - RUNNING：运行中。   - SCALEIN：缩容中。   - SCALEOUT：扩容中。   - FREEZING：冻结中。   - DELETED：已删除。   - DELETING：删除中。   - FAILED：失败。   - ORDER_PAYING：订单支付中。 
        :type status: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkaidatalake.v2.Creator`
        :param error: 
        :type error: Error
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._charge_mode = None
        self._capacity = None
        self._properties = None
        self._tags = None
        self._prometheus_config = None
        self._update_time = None
        self._create_time = None
        self._status = None
        self._creator = None
        self._error = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if capacity is not None:
            self.capacity = capacity
        if properties is not None:
            self.properties = properties
        if tags is not None:
            self.tags = tags
        if prometheus_config is not None:
            self.prometheus_config = prometheus_config
        if update_time is not None:
            self.update_time = update_time
        if create_time is not None:
            self.create_time = create_time
        if status is not None:
            self.status = status
        if creator is not None:
            self.creator = creator
        if error is not None:
            self.error = error

    @property
    def id(self):
        r"""Gets the id of this V2ComputeInfo.

        **参数解释**：计算资源ID。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 

        :return: The id of this V2ComputeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this V2ComputeInfo.

        **参数解释**：计算资源ID。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 

        :param id: The id of this V2ComputeInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this V2ComputeInfo.

        **参数解释**：计算资源名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 

        :return: The name of this V2ComputeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this V2ComputeInfo.

        **参数解释**：计算资源名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 

        :param name: The name of this V2ComputeInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this V2ComputeInfo.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :return: The description of this V2ComputeInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this V2ComputeInfo.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :param description: The description of this V2ComputeInfo.
        :type description: str
        """
        self._description = description

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this V2ComputeInfo.

        :return: The charge_mode of this V2ComputeInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ChargeMode`
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this V2ComputeInfo.

        :param charge_mode: The charge_mode of this V2ComputeInfo.
        :type charge_mode: :class:`huaweicloudsdkaidatalake.v2.ChargeMode`
        """
        self._charge_mode = charge_mode

    @property
    def capacity(self):
        r"""Gets the capacity of this V2ComputeInfo.

        **参数解释**：计算资源容量配置，由ResourceCapacityItem对象组成的数组，每个对象定义了资源类型、资源数量、资源规格和资源ID等信息。 

        :return: The capacity of this V2ComputeInfo.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ResourceCapacityItem`]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this V2ComputeInfo.

        **参数解释**：计算资源容量配置，由ResourceCapacityItem对象组成的数组，每个对象定义了资源类型、资源数量、资源规格和资源ID等信息。 

        :param capacity: The capacity of this V2ComputeInfo.
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.ResourceCapacityItem`]
        """
        self._capacity = capacity

    @property
    def properties(self):
        r"""Gets the properties of this V2ComputeInfo.

        **参数解释**：计算资源额外属性键值对映射。 

        :return: The properties of this V2ComputeInfo.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this V2ComputeInfo.

        **参数解释**：计算资源额外属性键值对映射。 

        :param properties: The properties of this V2ComputeInfo.
        :type properties: dict(str, str)
        """
        self._properties = properties

    @property
    def tags(self):
        r"""Gets the tags of this V2ComputeInfo.

        **参数解释**：标签列表，由Tag对象组成的数组，每个对象定义了标签键和标签值。 

        :return: The tags of this V2ComputeInfo.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this V2ComputeInfo.

        **参数解释**：标签列表，由Tag对象组成的数组，每个对象定义了标签键和标签值。 

        :param tags: The tags of this V2ComputeInfo.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.Tag`]
        """
        self._tags = tags

    @property
    def prometheus_config(self):
        r"""Gets the prometheus_config of this V2ComputeInfo.

        :return: The prometheus_config of this V2ComputeInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        return self._prometheus_config

    @prometheus_config.setter
    def prometheus_config(self, prometheus_config):
        r"""Sets the prometheus_config of this V2ComputeInfo.

        :param prometheus_config: The prometheus_config of this V2ComputeInfo.
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        self._prometheus_config = prometheus_config

    @property
    def update_time(self):
        r"""Gets the update_time of this V2ComputeInfo.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The update_time of this V2ComputeInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this V2ComputeInfo.

        **参数解释**：资源更新时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param update_time: The update_time of this V2ComputeInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def create_time(self):
        r"""Gets the create_time of this V2ComputeInfo.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this V2ComputeInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this V2ComputeInfo.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this V2ComputeInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def status(self):
        r"""Gets the status of this V2ComputeInfo.

        **参数解释**：资源状态。 **取值范围**：   - PREPARING：创建中。   - RELEASING：释放中。   - RUNNING：运行中。   - SCALEIN：缩容中。   - SCALEOUT：扩容中。   - FREEZING：冻结中。   - DELETED：已删除。   - DELETING：删除中。   - FAILED：失败。   - ORDER_PAYING：订单支付中。 

        :return: The status of this V2ComputeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this V2ComputeInfo.

        **参数解释**：资源状态。 **取值范围**：   - PREPARING：创建中。   - RELEASING：释放中。   - RUNNING：运行中。   - SCALEIN：缩容中。   - SCALEOUT：扩容中。   - FREEZING：冻结中。   - DELETED：已删除。   - DELETING：删除中。   - FAILED：失败。   - ORDER_PAYING：订单支付中。 

        :param status: The status of this V2ComputeInfo.
        :type status: str
        """
        self._status = status

    @property
    def creator(self):
        r"""Gets the creator of this V2ComputeInfo.

        :return: The creator of this V2ComputeInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.Creator`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this V2ComputeInfo.

        :param creator: The creator of this V2ComputeInfo.
        :type creator: :class:`huaweicloudsdkaidatalake.v2.Creator`
        """
        self._creator = creator

    @property
    def error(self):
        r"""Gets the error of this V2ComputeInfo.

        :return: The error of this V2ComputeInfo.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this V2ComputeInfo.

        :param error: The error of this V2ComputeInfo.
        :type error: Error
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
        if not isinstance(other, V2ComputeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
