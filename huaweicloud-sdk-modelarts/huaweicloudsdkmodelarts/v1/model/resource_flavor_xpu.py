# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceFlavorXpu:

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
        'size': 'str',
        'memory': 'str',
        'card': 'str',
        'chip': 'str'
    }

    attribute_map = {
        'type': 'type',
        'size': 'size',
        'memory': 'memory',
        'card': 'card',
        'chip': 'chip'
    }

    def __init__(self, type=None, size=None, memory=None, card=None, chip=None):
        r"""ResourceFlavorXpu

        The model defined in huaweicloud sdk

        :param type: **参数解释**：卡类型。 **取值范围**：不涉及。
        :type type: str
        :param size: **参数解释**：芯片数量。reseverd for backwards compatibility **取值范围**：不涉及。
        :type size: str
        :param memory: **参数解释**：单卡显存大小。 **取值范围**：不涉及。
        :type memory: str
        :param card: **参数解释**：卡数量。 **取值范围**：不涉及。
        :type card: str
        :param chip: **参数解释**：芯片数量。值同size字段一致。 **取值范围**：不涉及。
        :type chip: str
        """
        
        

        self._type = None
        self._size = None
        self._memory = None
        self._card = None
        self._chip = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if size is not None:
            self.size = size
        if memory is not None:
            self.memory = memory
        if card is not None:
            self.card = card
        if chip is not None:
            self.chip = chip

    @property
    def type(self):
        r"""Gets the type of this ResourceFlavorXpu.

        **参数解释**：卡类型。 **取值范围**：不涉及。

        :return: The type of this ResourceFlavorXpu.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceFlavorXpu.

        **参数解释**：卡类型。 **取值范围**：不涉及。

        :param type: The type of this ResourceFlavorXpu.
        :type type: str
        """
        self._type = type

    @property
    def size(self):
        r"""Gets the size of this ResourceFlavorXpu.

        **参数解释**：芯片数量。reseverd for backwards compatibility **取值范围**：不涉及。

        :return: The size of this ResourceFlavorXpu.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ResourceFlavorXpu.

        **参数解释**：芯片数量。reseverd for backwards compatibility **取值范围**：不涉及。

        :param size: The size of this ResourceFlavorXpu.
        :type size: str
        """
        self._size = size

    @property
    def memory(self):
        r"""Gets the memory of this ResourceFlavorXpu.

        **参数解释**：单卡显存大小。 **取值范围**：不涉及。

        :return: The memory of this ResourceFlavorXpu.
        :rtype: str
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ResourceFlavorXpu.

        **参数解释**：单卡显存大小。 **取值范围**：不涉及。

        :param memory: The memory of this ResourceFlavorXpu.
        :type memory: str
        """
        self._memory = memory

    @property
    def card(self):
        r"""Gets the card of this ResourceFlavorXpu.

        **参数解释**：卡数量。 **取值范围**：不涉及。

        :return: The card of this ResourceFlavorXpu.
        :rtype: str
        """
        return self._card

    @card.setter
    def card(self, card):
        r"""Sets the card of this ResourceFlavorXpu.

        **参数解释**：卡数量。 **取值范围**：不涉及。

        :param card: The card of this ResourceFlavorXpu.
        :type card: str
        """
        self._card = card

    @property
    def chip(self):
        r"""Gets the chip of this ResourceFlavorXpu.

        **参数解释**：芯片数量。值同size字段一致。 **取值范围**：不涉及。

        :return: The chip of this ResourceFlavorXpu.
        :rtype: str
        """
        return self._chip

    @chip.setter
    def chip(self, chip):
        r"""Sets the chip of this ResourceFlavorXpu.

        **参数解释**：芯片数量。值同size字段一致。 **取值范围**：不涉及。

        :param chip: The chip of this ResourceFlavorXpu.
        :type chip: str
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
        if not isinstance(other, ResourceFlavorXpu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
