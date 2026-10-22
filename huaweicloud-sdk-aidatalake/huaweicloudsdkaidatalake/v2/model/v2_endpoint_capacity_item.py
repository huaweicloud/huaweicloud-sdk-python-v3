# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2EndpointCapacityItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'maximum_capacity': 'int',
        'minimum_capacity': 'int',
        'spec_code': 'str',
        'use_ondemand_resource': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'maximum_capacity': 'maximum_capacity',
        'minimum_capacity': 'minimum_capacity',
        'spec_code': 'spec_code',
        'use_ondemand_resource': 'use_ondemand_resource'
    }

    def __init__(self, type=None, maximum_capacity=None, minimum_capacity=None, spec_code=None, use_ondemand_resource=None):
        r"""V2EndpointCapacityItem

        The model defined in huaweicloud sdk

        :param type: **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 **默认取值**：不涉及。 
        :type type: str
        :param maximum_capacity: **参数解释**：资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：1~10000。 **默认取值**：不涉及。 
        :type maximum_capacity: int
        :param minimum_capacity: **参数解释**：最小资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~10000，小于等于maximum_capacity。 **默认取值**：不涉及。 
        :type minimum_capacity: int
        :param spec_code: **参数解释**：资源规格。获取方式：从规格列表查询获取。 **约束限制**：预留资源和混合模式端点此参数必填。端点创建后此参数不支持变更。 **取值范围**：支持英文字母、数字、小数点及连字符，长度为1~64个字符。 **默认取值**：不涉及。 
        :type spec_code: str
        :param use_ondemand_resource: **参数解释**：容量是否使用弹性资源。 **约束限制**：端点创建后此参数不支持变更。 **取值范围**：   - true：使用弹性资源。   - false：不使用弹性资源。 **默认取值**：false。 
        :type use_ondemand_resource: bool
        """
        
        

        self._type = None
        self._maximum_capacity = None
        self._minimum_capacity = None
        self._spec_code = None
        self._use_ondemand_resource = None
        self.discriminator = None

        self.type = type
        self.maximum_capacity = maximum_capacity
        self.minimum_capacity = minimum_capacity
        if spec_code is not None:
            self.spec_code = spec_code
        if use_ondemand_resource is not None:
            self.use_ondemand_resource = use_ondemand_resource

    @property
    def type(self):
        r"""Gets the type of this V2EndpointCapacityItem.

        **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 **默认取值**：不涉及。 

        :return: The type of this V2EndpointCapacityItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this V2EndpointCapacityItem.

        **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 **默认取值**：不涉及。 

        :param type: The type of this V2EndpointCapacityItem.
        :type type: str
        """
        self._type = type

    @property
    def maximum_capacity(self):
        r"""Gets the maximum_capacity of this V2EndpointCapacityItem.

        **参数解释**：资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：1~10000。 **默认取值**：不涉及。 

        :return: The maximum_capacity of this V2EndpointCapacityItem.
        :rtype: int
        """
        return self._maximum_capacity

    @maximum_capacity.setter
    def maximum_capacity(self, maximum_capacity):
        r"""Sets the maximum_capacity of this V2EndpointCapacityItem.

        **参数解释**：资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：1~10000。 **默认取值**：不涉及。 

        :param maximum_capacity: The maximum_capacity of this V2EndpointCapacityItem.
        :type maximum_capacity: int
        """
        self._maximum_capacity = maximum_capacity

    @property
    def minimum_capacity(self):
        r"""Gets the minimum_capacity of this V2EndpointCapacityItem.

        **参数解释**：最小资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~10000，小于等于maximum_capacity。 **默认取值**：不涉及。 

        :return: The minimum_capacity of this V2EndpointCapacityItem.
        :rtype: int
        """
        return self._minimum_capacity

    @minimum_capacity.setter
    def minimum_capacity(self, minimum_capacity):
        r"""Sets the minimum_capacity of this V2EndpointCapacityItem.

        **参数解释**：最小资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~10000，小于等于maximum_capacity。 **默认取值**：不涉及。 

        :param minimum_capacity: The minimum_capacity of this V2EndpointCapacityItem.
        :type minimum_capacity: int
        """
        self._minimum_capacity = minimum_capacity

    @property
    def spec_code(self):
        r"""Gets the spec_code of this V2EndpointCapacityItem.

        **参数解释**：资源规格。获取方式：从规格列表查询获取。 **约束限制**：预留资源和混合模式端点此参数必填。端点创建后此参数不支持变更。 **取值范围**：支持英文字母、数字、小数点及连字符，长度为1~64个字符。 **默认取值**：不涉及。 

        :return: The spec_code of this V2EndpointCapacityItem.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this V2EndpointCapacityItem.

        **参数解释**：资源规格。获取方式：从规格列表查询获取。 **约束限制**：预留资源和混合模式端点此参数必填。端点创建后此参数不支持变更。 **取值范围**：支持英文字母、数字、小数点及连字符，长度为1~64个字符。 **默认取值**：不涉及。 

        :param spec_code: The spec_code of this V2EndpointCapacityItem.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def use_ondemand_resource(self):
        r"""Gets the use_ondemand_resource of this V2EndpointCapacityItem.

        **参数解释**：容量是否使用弹性资源。 **约束限制**：端点创建后此参数不支持变更。 **取值范围**：   - true：使用弹性资源。   - false：不使用弹性资源。 **默认取值**：false。 

        :return: The use_ondemand_resource of this V2EndpointCapacityItem.
        :rtype: bool
        """
        return self._use_ondemand_resource

    @use_ondemand_resource.setter
    def use_ondemand_resource(self, use_ondemand_resource):
        r"""Sets the use_ondemand_resource of this V2EndpointCapacityItem.

        **参数解释**：容量是否使用弹性资源。 **约束限制**：端点创建后此参数不支持变更。 **取值范围**：   - true：使用弹性资源。   - false：不使用弹性资源。 **默认取值**：false。 

        :param use_ondemand_resource: The use_ondemand_resource of this V2EndpointCapacityItem.
        :type use_ondemand_resource: bool
        """
        self._use_ondemand_resource = use_ondemand_resource

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
        if not isinstance(other, V2EndpointCapacityItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
