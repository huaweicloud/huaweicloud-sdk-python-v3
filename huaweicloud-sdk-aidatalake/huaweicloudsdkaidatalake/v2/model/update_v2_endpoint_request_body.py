# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateV2EndpointRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'description': 'str',
        'capacity': 'list[V2EndpointCapacityItem]',
        'engine': 'V2EndpointUpdateEngineConfig',
        'prometheus_config': 'PrometheusConfig',
        'lts_config': 'LtsConfig',
        'credential': 'CredentialConfig',
        'tags': 'list[V2ResourceTag]'
    }

    attribute_map = {
        'display_name': 'display_name',
        'description': 'description',
        'capacity': 'capacity',
        'engine': 'engine',
        'prometheus_config': 'prometheus_config',
        'lts_config': 'lts_config',
        'credential': 'credential',
        'tags': 'tags'
    }

    def __init__(self, display_name=None, description=None, capacity=None, engine=None, prometheus_config=None, lts_config=None, credential=None, tags=None):
        r"""UpdateV2EndpointRequestBody

        The model defined in huaweicloud sdk

        :param display_name: **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 
        :type display_name: str
        :param description: **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 
        :type description: str
        :param capacity: **参数解释**：计算资源容量配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        :param engine: 
        :type engine: :class:`huaweicloudsdkaidatalake.v2.V2EndpointUpdateEngineConfig`
        :param prometheus_config: 
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        :param lts_config: 
        :type lts_config: :class:`huaweicloudsdkaidatalake.v2.LtsConfig`
        :param credential: 
        :type credential: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        :param tags: **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 
        :type tags: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        
        

        self._display_name = None
        self._description = None
        self._capacity = None
        self._engine = None
        self._prometheus_config = None
        self._lts_config = None
        self._credential = None
        self._tags = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if capacity is not None:
            self.capacity = capacity
        if engine is not None:
            self.engine = engine
        if prometheus_config is not None:
            self.prometheus_config = prometheus_config
        if lts_config is not None:
            self.lts_config = lts_config
        if credential is not None:
            self.credential = credential
        if tags is not None:
            self.tags = tags

    @property
    def display_name(self):
        r"""Gets the display_name of this UpdateV2EndpointRequestBody.

        **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 

        :return: The display_name of this UpdateV2EndpointRequestBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this UpdateV2EndpointRequestBody.

        **参数解释**：端点显示名称。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 

        :param display_name: The display_name of this UpdateV2EndpointRequestBody.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this UpdateV2EndpointRequestBody.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :return: The description of this UpdateV2EndpointRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateV2EndpointRequestBody.

        **参数解释**：资源描述信息。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~512个字符。 

        :param description: The description of this UpdateV2EndpointRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def capacity(self):
        r"""Gets the capacity of this UpdateV2EndpointRequestBody.

        **参数解释**：计算资源容量配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The capacity of this UpdateV2EndpointRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this UpdateV2EndpointRequestBody.

        **参数解释**：计算资源容量配置。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param capacity: The capacity of this UpdateV2EndpointRequestBody.
        :type capacity: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointCapacityItem`]
        """
        self._capacity = capacity

    @property
    def engine(self):
        r"""Gets the engine of this UpdateV2EndpointRequestBody.

        :return: The engine of this UpdateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.V2EndpointUpdateEngineConfig`
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        r"""Sets the engine of this UpdateV2EndpointRequestBody.

        :param engine: The engine of this UpdateV2EndpointRequestBody.
        :type engine: :class:`huaweicloudsdkaidatalake.v2.V2EndpointUpdateEngineConfig`
        """
        self._engine = engine

    @property
    def prometheus_config(self):
        r"""Gets the prometheus_config of this UpdateV2EndpointRequestBody.

        :return: The prometheus_config of this UpdateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        return self._prometheus_config

    @prometheus_config.setter
    def prometheus_config(self, prometheus_config):
        r"""Sets the prometheus_config of this UpdateV2EndpointRequestBody.

        :param prometheus_config: The prometheus_config of this UpdateV2EndpointRequestBody.
        :type prometheus_config: :class:`huaweicloudsdkaidatalake.v2.PrometheusConfig`
        """
        self._prometheus_config = prometheus_config

    @property
    def lts_config(self):
        r"""Gets the lts_config of this UpdateV2EndpointRequestBody.

        :return: The lts_config of this UpdateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.LtsConfig`
        """
        return self._lts_config

    @lts_config.setter
    def lts_config(self, lts_config):
        r"""Sets the lts_config of this UpdateV2EndpointRequestBody.

        :param lts_config: The lts_config of this UpdateV2EndpointRequestBody.
        :type lts_config: :class:`huaweicloudsdkaidatalake.v2.LtsConfig`
        """
        self._lts_config = lts_config

    @property
    def credential(self):
        r"""Gets the credential of this UpdateV2EndpointRequestBody.

        :return: The credential of this UpdateV2EndpointRequestBody.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        r"""Sets the credential of this UpdateV2EndpointRequestBody.

        :param credential: The credential of this UpdateV2EndpointRequestBody.
        :type credential: :class:`huaweicloudsdkaidatalake.v2.CredentialConfig`
        """
        self._credential = credential

    @property
    def tags(self):
        r"""Gets the tags of this UpdateV2EndpointRequestBody.

        **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 

        :return: The tags of this UpdateV2EndpointRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateV2EndpointRequestBody.

        **参数解释**：标签列表，每个元素为一个V2ResourceTag对象，包含key（标签键）和value（标签值）字段。 **约束限制**：最多20个标签。 

        :param tags: The tags of this UpdateV2EndpointRequestBody.
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
        if not isinstance(other, UpdateV2EndpointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
