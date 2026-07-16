# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AscendInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'npu': 'int',
        'npu_memory': 'str',
        'type': 'str',
        'chip': 'int'
    }

    attribute_map = {
        'npu': 'npu',
        'npu_memory': 'npu_memory',
        'type': 'type',
        'chip': 'chip'
    }

    def __init__(self, npu=None, npu_memory=None, type=None, chip=None):
        r"""AscendInfo

        The model defined in huaweicloud sdk

        :param npu: **参数解释**：NPU数量。 **取值范围**：不涉及。
        :type npu: int
        :param npu_memory: **参数解释**：NPU内存。 **取值范围**：不涉及。
        :type npu_memory: str
        :param type: **参数解释**：NPU类型。 **取值范围**：不涉及。
        :type type: str
        :param chip: **参数解释**：NPU设备数。 **取值范围**：不涉及。
        :type chip: int
        """
        
        

        self._npu = None
        self._npu_memory = None
        self._type = None
        self._chip = None
        self.discriminator = None

        if npu is not None:
            self.npu = npu
        if npu_memory is not None:
            self.npu_memory = npu_memory
        if type is not None:
            self.type = type
        if chip is not None:
            self.chip = chip

    @property
    def npu(self):
        r"""Gets the npu of this AscendInfo.

        **参数解释**：NPU数量。 **取值范围**：不涉及。

        :return: The npu of this AscendInfo.
        :rtype: int
        """
        return self._npu

    @npu.setter
    def npu(self, npu):
        r"""Sets the npu of this AscendInfo.

        **参数解释**：NPU数量。 **取值范围**：不涉及。

        :param npu: The npu of this AscendInfo.
        :type npu: int
        """
        self._npu = npu

    @property
    def npu_memory(self):
        r"""Gets the npu_memory of this AscendInfo.

        **参数解释**：NPU内存。 **取值范围**：不涉及。

        :return: The npu_memory of this AscendInfo.
        :rtype: str
        """
        return self._npu_memory

    @npu_memory.setter
    def npu_memory(self, npu_memory):
        r"""Sets the npu_memory of this AscendInfo.

        **参数解释**：NPU内存。 **取值范围**：不涉及。

        :param npu_memory: The npu_memory of this AscendInfo.
        :type npu_memory: str
        """
        self._npu_memory = npu_memory

    @property
    def type(self):
        r"""Gets the type of this AscendInfo.

        **参数解释**：NPU类型。 **取值范围**：不涉及。

        :return: The type of this AscendInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AscendInfo.

        **参数解释**：NPU类型。 **取值范围**：不涉及。

        :param type: The type of this AscendInfo.
        :type type: str
        """
        self._type = type

    @property
    def chip(self):
        r"""Gets the chip of this AscendInfo.

        **参数解释**：NPU设备数。 **取值范围**：不涉及。

        :return: The chip of this AscendInfo.
        :rtype: int
        """
        return self._chip

    @chip.setter
    def chip(self, chip):
        r"""Sets the chip of this AscendInfo.

        **参数解释**：NPU设备数。 **取值范围**：不涉及。

        :param chip: The chip of this AscendInfo.
        :type chip: int
        """
        self._chip = chip

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
        if not isinstance(other, AscendInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
