# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateV2ComputeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'capacity': 'list[CapacityItem]',
        'tags': 'list[V2ResourceTag]',
        'prometheus_config': 'PrometheusConfig'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'capacity': 'capacity',
        'tags': 'tags',
        'prometheus_config': 'prometheus_config'
    }

    def __init__(self, name=None, description=None, capacity=None, tags=None, prometheus_config=None):
        r"""UpdateV2ComputeRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**：计算资源名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 
        :type name: str
        :param description: **参数解释**：资源描述信息。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 **默认取值**：不涉及。
        :type description: str
        :param capacity: **参数解释**：计算资源容量配置，由CapacityItem对象组成的数组，每个对象定义了资源类型、资源数量和资源规格等信息。 **约束限制**：不涉及。 
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.CapacityItem`]
        :param tags: **参数解释**：标签列表，由V2ResourceTag对象组成的数组，每个对象定义了标签键和标签值。 **约束限制**：最多20个标签。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        :param prometheus_config: 
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        
        

        self._name = None
        self._description = None
        self._capacity = None
        self._tags = None
        self._prometheus_config = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if capacity is not None:
            self.capacity = capacity
        if tags is not None:
            self.tags = tags
        if prometheus_config is not None:
            self.prometheus_config = prometheus_config

    @property
    def name(self):
        r"""Gets the name of this UpdateV2ComputeRequestBody.

        **参数解释**：计算资源名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 

        :return: The name of this UpdateV2ComputeRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateV2ComputeRequestBody.

        **参数解释**：计算资源名称。 **约束限制**：不涉及。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。 

        :param name: The name of this UpdateV2ComputeRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateV2ComputeRequestBody.

        **参数解释**：资源描述信息。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 **默认取值**：不涉及。

        :return: The description of this UpdateV2ComputeRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateV2ComputeRequestBody.

        **参数解释**：资源描述信息。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 **默认取值**：不涉及。

        :param description: The description of this UpdateV2ComputeRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def capacity(self):
        r"""Gets the capacity of this UpdateV2ComputeRequestBody.

        **参数解释**：计算资源容量配置，由CapacityItem对象组成的数组，每个对象定义了资源类型、资源数量和资源规格等信息。 **约束限制**：不涉及。 

        :return: The capacity of this UpdateV2ComputeRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.CapacityItem`]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this UpdateV2ComputeRequestBody.

        **参数解释**：计算资源容量配置，由CapacityItem对象组成的数组，每个对象定义了资源类型、资源数量和资源规格等信息。 **约束限制**：不涉及。 

        :param capacity: The capacity of this UpdateV2ComputeRequestBody.
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.CapacityItem`]
        """
        self._capacity = capacity

    @property
    def tags(self):
        r"""Gets the tags of this UpdateV2ComputeRequestBody.

        **参数解释**：标签列表，由V2ResourceTag对象组成的数组，每个对象定义了标签键和标签值。 **约束限制**：最多20个标签。 

        :return: The tags of this UpdateV2ComputeRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateV2ComputeRequestBody.

        **参数解释**：标签列表，由V2ResourceTag对象组成的数组，每个对象定义了标签键和标签值。 **约束限制**：最多20个标签。 

        :param tags: The tags of this UpdateV2ComputeRequestBody.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        self._tags = tags

    @property
    def prometheus_config(self):
        r"""Gets the prometheus_config of this UpdateV2ComputeRequestBody.

        :return: The prometheus_config of this UpdateV2ComputeRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        return self._prometheus_config

    @prometheus_config.setter
    def prometheus_config(self, prometheus_config):
        r"""Sets the prometheus_config of this UpdateV2ComputeRequestBody.

        :param prometheus_config: The prometheus_config of this UpdateV2ComputeRequestBody.
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        self._prometheus_config = prometheus_config

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
        if not isinstance(other, UpdateV2ComputeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
