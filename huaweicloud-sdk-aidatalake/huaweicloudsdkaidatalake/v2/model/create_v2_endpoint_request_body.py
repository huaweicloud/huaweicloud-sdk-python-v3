# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateV2EndpointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compute_id': 'str',
        'name': 'str',
        'display_name': 'str',
        'description': 'str',
        'engine': 'V2EndpointCreateEngineConfig',
        'capacity': 'list[V2EndpointCapacityItem]',
        'prometheus_config': 'PrometheusConfig',
        'lts_config': 'LtsConfig',
        'credential': 'CredentialConfig',
        'resource_type': 'ResourceType',
        'tags': 'list[V2ResourceTag]'
    }

    attribute_map = {
        'compute_id': 'compute_id',
        'name': 'name',
        'display_name': 'display_name',
        'description': 'description',
        'engine': 'engine',
        'capacity': 'capacity',
        'prometheus_config': 'prometheus_config',
        'lts_config': 'lts_config',
        'credential': 'credential',
        'resource_type': 'resource_type',
        'tags': 'tags'
    }

    def __init__(self, compute_id=None, name=None, display_name=None, description=None, engine=None, capacity=None, prometheus_config=None, lts_config=None, credential=None, resource_type=None, tags=None):
        r"""CreateV2EndpointRequestBody

        The model defined in huaweicloud sdk

        :param compute_id: **参数解释**：计算资源ID。可通过[查询计算资源列表](ListV2Computes.xml)获取计算资源ID。 **约束限制**：预留模式和混合模式端点必填。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 
        :type compute_id: str
        :param name: **参数解释**：端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 
        :type name: str
        :param display_name: **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 
        :type display_name: str
        :param description: **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 
        :type description: str
        :param engine: 
        :type engine: :class:`huaweicloudsdkaidatalake.v2.V2EndpointCreateEngineConfig`
        :param capacity: **参数解释**：计算资源容量配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        :param prometheus_config: 
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        :param lts_config: 
        :type lts_config: :class:`huaweicloudsdkaidatalake.v2.LtsConfig`
        :param credential: 
        :type credential: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        :param resource_type: 
        :type resource_type: :class:`huaweicloudsdkaidatalake.v2.ResourceType`
        :param tags: **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        
        

        self._compute_id = None
        self._name = None
        self._display_name = None
        self._description = None
        self._engine = None
        self._capacity = None
        self._prometheus_config = None
        self._lts_config = None
        self._credential = None
        self._resource_type = None
        self._tags = None
        self.discriminator = None

        if compute_id is not None:
            self.compute_id = compute_id
        self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        self.engine = engine
        self.capacity = capacity
        if prometheus_config is not None:
            self.prometheus_config = prometheus_config
        if lts_config is not None:
            self.lts_config = lts_config
        if credential is not None:
            self.credential = credential
        self.resource_type = resource_type
        if tags is not None:
            self.tags = tags

    @property
    def compute_id(self):
        r"""Gets the compute_id of this CreateV2EndpointRequestBody.

        **参数解释**：计算资源ID。可通过[查询计算资源列表](ListV2Computes.xml)获取计算资源ID。 **约束限制**：预留模式和混合模式端点必填。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The compute_id of this CreateV2EndpointRequestBody.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        r"""Sets the compute_id of this CreateV2EndpointRequestBody.

        **参数解释**：计算资源ID。可通过[查询计算资源列表](ListV2Computes.xml)获取计算资源ID。 **约束限制**：预留模式和混合模式端点必填。 **取值范围**：长度为1~36个英文字母、数字和中划线的组合。 **默认取值**：不涉及。 

        :param compute_id: The compute_id of this CreateV2EndpointRequestBody.
        :type compute_id: str
        """
        self._compute_id = compute_id

    @property
    def name(self):
        r"""Gets the name of this CreateV2EndpointRequestBody.

        **参数解释**：端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 

        :return: The name of this CreateV2EndpointRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateV2EndpointRequestBody.

        **参数解释**：端点名称。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 

        :param name: The name of this CreateV2EndpointRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateV2EndpointRequestBody.

        **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 

        :return: The display_name of this CreateV2EndpointRequestBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateV2EndpointRequestBody.

        **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 

        :param display_name: The display_name of this CreateV2EndpointRequestBody.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this CreateV2EndpointRequestBody.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :return: The description of this CreateV2EndpointRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateV2EndpointRequestBody.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :param description: The description of this CreateV2EndpointRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def engine(self):
        r"""Gets the engine of this CreateV2EndpointRequestBody.

        :return: The engine of this CreateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2EndpointCreateEngineConfig`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this CreateV2EndpointRequestBody.

        :param engine: The engine of this CreateV2EndpointRequestBody.
        :type engine: :class:`huaweicloudsdkaidatalake.v2.V2EndpointCreateEngineConfig`
        """
        self._engine = engine

    @property
    def capacity(self):
        r"""Gets the capacity of this CreateV2EndpointRequestBody.

        **参数解释**：计算资源容量配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The capacity of this CreateV2EndpointRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this CreateV2EndpointRequestBody.

        **参数解释**：计算资源容量配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param capacity: The capacity of this CreateV2EndpointRequestBody.
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        """
        self._capacity = capacity

    @property
    def prometheus_config(self):
        r"""Gets the prometheus_config of this CreateV2EndpointRequestBody.

        :return: The prometheus_config of this CreateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        return self._prometheus_config

    @prometheus_config.setter
    def prometheus_config(self, prometheus_config):
        r"""Sets the prometheus_config of this CreateV2EndpointRequestBody.

        :param prometheus_config: The prometheus_config of this CreateV2EndpointRequestBody.
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        self._prometheus_config = prometheus_config

    @property
    def lts_config(self):
        r"""Gets the lts_config of this CreateV2EndpointRequestBody.

        :return: The lts_config of this CreateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.LtsConfig`
        """
        return self._lts_config

    @lts_config.setter
    def lts_config(self, lts_config):
        r"""Sets the lts_config of this CreateV2EndpointRequestBody.

        :param lts_config: The lts_config of this CreateV2EndpointRequestBody.
        :type lts_config: :class:`huaweicloudsdkaidatalake.v2.LtsConfig`
        """
        self._lts_config = lts_config

    @property
    def credential(self):
        r"""Gets the credential of this CreateV2EndpointRequestBody.

        :return: The credential of this CreateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        r"""Sets the credential of this CreateV2EndpointRequestBody.

        :param credential: The credential of this CreateV2EndpointRequestBody.
        :type credential: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        """
        self._credential = credential

    @property
    def resource_type(self):
        r"""Gets the resource_type of this CreateV2EndpointRequestBody.

        :return: The resource_type of this CreateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ResourceType`
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this CreateV2EndpointRequestBody.

        :param resource_type: The resource_type of this CreateV2EndpointRequestBody.
        :type resource_type: :class:`huaweicloudsdkaidatalake.v2.ResourceType`
        """
        self._resource_type = resource_type

    @property
    def tags(self):
        r"""Gets the tags of this CreateV2EndpointRequestBody.

        **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 

        :return: The tags of this CreateV2EndpointRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateV2EndpointRequestBody.

        **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 

        :param tags: The tags of this CreateV2EndpointRequestBody.
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateV2EndpointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
