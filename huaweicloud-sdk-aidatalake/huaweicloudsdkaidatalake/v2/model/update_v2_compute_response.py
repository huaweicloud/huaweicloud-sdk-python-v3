# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateV2ComputeResponse(SdkResponse):

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
        'prometheus_config': 'PrometheusConfig'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'charge_mode': 'charge_mode',
        'capacity': 'capacity',
        'properties': 'properties',
        'tags': 'tags',
        'prometheus_config': 'prometheus_config'
    }

    def __init__(self, id=None, name=None, description=None, charge_mode=None, capacity=None, properties=None, tags=None, prometheus_config=None):
        r"""UpdateV2ComputeResponse

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
        """
        
        super().__init__()

        self._id = None
        self._name = None
        self._description = None
        self._charge_mode = None
        self._capacity = None
        self._properties = None
        self._tags = None
        self._prometheus_config = None
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

    @property
    def id(self):
        r"""Gets the id of this UpdateV2ComputeResponse.

        **参数解释**：计算资源ID。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 

        :return: The id of this UpdateV2ComputeResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateV2ComputeResponse.

        **参数解释**：计算资源ID。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 

        :param id: The id of this UpdateV2ComputeResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UpdateV2ComputeResponse.

        **参数解释**：计算资源名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 

        :return: The name of this UpdateV2ComputeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateV2ComputeResponse.

        **参数解释**：计算资源名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 

        :param name: The name of this UpdateV2ComputeResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateV2ComputeResponse.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :return: The description of this UpdateV2ComputeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateV2ComputeResponse.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :param description: The description of this UpdateV2ComputeResponse.
        :type description: str
        """
        self._description = description

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this UpdateV2ComputeResponse.

        :return: The charge_mode of this UpdateV2ComputeResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ChargeMode`
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this UpdateV2ComputeResponse.

        :param charge_mode: The charge_mode of this UpdateV2ComputeResponse.
        :type charge_mode: :class:`huaweicloudsdkaidatalake.v2.ChargeMode`
        """
        self._charge_mode = charge_mode

    @property
    def capacity(self):
        r"""Gets the capacity of this UpdateV2ComputeResponse.

        **参数解释**：计算资源容量配置，由ResourceCapacityItem对象组成的数组，每个对象定义了资源类型、资源数量、资源规格和资源ID等信息。 

        :return: The capacity of this UpdateV2ComputeResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ResourceCapacityItem`]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this UpdateV2ComputeResponse.

        **参数解释**：计算资源容量配置，由ResourceCapacityItem对象组成的数组，每个对象定义了资源类型、资源数量、资源规格和资源ID等信息。 

        :param capacity: The capacity of this UpdateV2ComputeResponse.
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.ResourceCapacityItem`]
        """
        self._capacity = capacity

    @property
    def properties(self):
        r"""Gets the properties of this UpdateV2ComputeResponse.

        **参数解释**：计算资源额外属性键值对映射。 

        :return: The properties of this UpdateV2ComputeResponse.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this UpdateV2ComputeResponse.

        **参数解释**：计算资源额外属性键值对映射。 

        :param properties: The properties of this UpdateV2ComputeResponse.
        :type properties: dict(str, str)
        """
        self._properties = properties

    @property
    def tags(self):
        r"""Gets the tags of this UpdateV2ComputeResponse.

        **参数解释**：标签列表，由Tag对象组成的数组，每个对象定义了标签键和标签值。 

        :return: The tags of this UpdateV2ComputeResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateV2ComputeResponse.

        **参数解释**：标签列表，由Tag对象组成的数组，每个对象定义了标签键和标签值。 

        :param tags: The tags of this UpdateV2ComputeResponse.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.Tag`]
        """
        self._tags = tags

    @property
    def prometheus_config(self):
        r"""Gets the prometheus_config of this UpdateV2ComputeResponse.

        :return: The prometheus_config of this UpdateV2ComputeResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        return self._prometheus_config

    @prometheus_config.setter
    def prometheus_config(self, prometheus_config):
        r"""Sets the prometheus_config of this UpdateV2ComputeResponse.

        :param prometheus_config: The prometheus_config of this UpdateV2ComputeResponse.
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        self._prometheus_config = prometheus_config

    def to_dict(self):
        import warnings
        warnings.warn("UpdateV2ComputeResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdateV2ComputeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
