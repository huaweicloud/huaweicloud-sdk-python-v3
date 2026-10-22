# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CapacityVersion:

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
        'capacity': 'int',
        'target_capacity': 'int',
        'spec_code': 'str'
    }

    attribute_map = {
        'type': 'type',
        'capacity': 'capacity',
        'target_capacity': 'target_capacity',
        'spec_code': 'spec_code'
    }

    def __init__(self, type=None, capacity=None, target_capacity=None, spec_code=None):
        r"""CapacityVersion

        The model defined in huaweicloud sdk

        :param type: **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 **默认取值**：不涉及。 
        :type type: str
        :param capacity: **参数解释**：资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~48000。 **默认取值**：不涉及。 
        :type capacity: int
        :param target_capacity: **参数解释**：目标资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~48000。 **默认取值**：不涉及。 
        :type target_capacity: int
        :param spec_code: **参数解释**：资源规格。 **约束限制**：不涉及。 **取值范围**：由英文字母、数字、小数点和中划线组成，长度为1~64个字符。 **默认取值**：不涉及。 
        :type spec_code: str
        """
        
        

        self._type = None
        self._capacity = None
        self._target_capacity = None
        self._spec_code = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if capacity is not None:
            self.capacity = capacity
        if target_capacity is not None:
            self.target_capacity = target_capacity
        if spec_code is not None:
            self.spec_code = spec_code

    @property
    def type(self):
        r"""Gets the type of this CapacityVersion.

        **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 **默认取值**：不涉及。 

        :return: The type of this CapacityVersion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CapacityVersion.

        **参数解释**：资源类型。 **约束限制**：不涉及。 **取值范围**：   - CPU：中央处理器。   - GPU：图形处理器。   - NPU：神经网络处理器。 **默认取值**：不涉及。 

        :param type: The type of this CapacityVersion.
        :type type: str
        """
        self._type = type

    @property
    def capacity(self):
        r"""Gets the capacity of this CapacityVersion.

        **参数解释**：资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~48000。 **默认取值**：不涉及。 

        :return: The capacity of this CapacityVersion.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        r"""Sets the capacity of this CapacityVersion.

        **参数解释**：资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~48000。 **默认取值**：不涉及。 

        :param capacity: The capacity of this CapacityVersion.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def target_capacity(self):
        r"""Gets the target_capacity of this CapacityVersion.

        **参数解释**：目标资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~48000。 **默认取值**：不涉及。 

        :return: The target_capacity of this CapacityVersion.
        :rtype: int
        """
        return self._target_capacity

    @target_capacity.setter
    def target_capacity(self, target_capacity):
        r"""Sets the target_capacity of this CapacityVersion.

        **参数解释**：目标资源数量。CPU资源单位为核，GPU/NPU资源单位为个。 **约束限制**：不涉及。 **取值范围**：0~48000。 **默认取值**：不涉及。 

        :param target_capacity: The target_capacity of this CapacityVersion.
        :type target_capacity: int
        """
        self._target_capacity = target_capacity

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CapacityVersion.

        **参数解释**：资源规格。 **约束限制**：不涉及。 **取值范围**：由英文字母、数字、小数点和中划线组成，长度为1~64个字符。 **默认取值**：不涉及。 

        :return: The spec_code of this CapacityVersion.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CapacityVersion.

        **参数解释**：资源规格。 **约束限制**：不涉及。 **取值范围**：由英文字母、数字、小数点和中划线组成，长度为1~64个字符。 **默认取值**：不涉及。 

        :param spec_code: The spec_code of this CapacityVersion.
        :type spec_code: str
        """
        self._spec_code = spec_code

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
        if not isinstance(other, CapacityVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
