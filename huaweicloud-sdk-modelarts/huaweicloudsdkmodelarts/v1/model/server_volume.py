# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerVolume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'type': 'str',
        'evs_type': 'str',
        'evs_id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'type': 'type',
        'evs_type': 'evs_type',
        'evs_id': 'evs_id'
    }

    def __init__(self, size=None, type=None, evs_type=None, evs_id=None):
        r"""ServerVolume

        The model defined in huaweicloud sdk

        :param size: **参数解释**：EVS盘大小。表示分配给系统盘的存储空间大小。 **约束限制**：不涉及。 **取值范围**：100 - 1024 GB **默认取值**：不涉及。
        :type size: int
        :param type: **参数解释**：存储类型。表示系统盘或数据盘。 **约束限制**：不涉及。 **取值范围**： - ROOT：系统盘 - DATA：数据盘  **默认取值**：不涉及。
        :type type: str
        :param evs_type: **参数解释**：EVS盘类型。表示EVS盘的存储类型。 **约束限制**：不涉及。 **取值范围**： - ESSD：极速型SSD云硬盘 - GPSSD：通用型SSD云硬盘 - SAS：高IO云硬盘 - SATA：普通IO云硬盘 - SSD：超高IO云硬盘  **默认取值**：不涉及。
        :type evs_type: str
        :param evs_id: **参数解释**：EVS盘的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。
        :type evs_id: str
        """
        
        

        self._size = None
        self._type = None
        self._evs_type = None
        self._evs_id = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if type is not None:
            self.type = type
        if evs_type is not None:
            self.evs_type = evs_type
        if evs_id is not None:
            self.evs_id = evs_id

    @property
    def size(self):
        r"""Gets the size of this ServerVolume.

        **参数解释**：EVS盘大小。表示分配给系统盘的存储空间大小。 **约束限制**：不涉及。 **取值范围**：100 - 1024 GB **默认取值**：不涉及。

        :return: The size of this ServerVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ServerVolume.

        **参数解释**：EVS盘大小。表示分配给系统盘的存储空间大小。 **约束限制**：不涉及。 **取值范围**：100 - 1024 GB **默认取值**：不涉及。

        :param size: The size of this ServerVolume.
        :type size: int
        """
        self._size = size

    @property
    def type(self):
        r"""Gets the type of this ServerVolume.

        **参数解释**：存储类型。表示系统盘或数据盘。 **约束限制**：不涉及。 **取值范围**： - ROOT：系统盘 - DATA：数据盘  **默认取值**：不涉及。

        :return: The type of this ServerVolume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ServerVolume.

        **参数解释**：存储类型。表示系统盘或数据盘。 **约束限制**：不涉及。 **取值范围**： - ROOT：系统盘 - DATA：数据盘  **默认取值**：不涉及。

        :param type: The type of this ServerVolume.
        :type type: str
        """
        self._type = type

    @property
    def evs_type(self):
        r"""Gets the evs_type of this ServerVolume.

        **参数解释**：EVS盘类型。表示EVS盘的存储类型。 **约束限制**：不涉及。 **取值范围**： - ESSD：极速型SSD云硬盘 - GPSSD：通用型SSD云硬盘 - SAS：高IO云硬盘 - SATA：普通IO云硬盘 - SSD：超高IO云硬盘  **默认取值**：不涉及。

        :return: The evs_type of this ServerVolume.
        :rtype: str
        """
        return self._evs_type

    @evs_type.setter
    def evs_type(self, evs_type):
        r"""Sets the evs_type of this ServerVolume.

        **参数解释**：EVS盘类型。表示EVS盘的存储类型。 **约束限制**：不涉及。 **取值范围**： - ESSD：极速型SSD云硬盘 - GPSSD：通用型SSD云硬盘 - SAS：高IO云硬盘 - SATA：普通IO云硬盘 - SSD：超高IO云硬盘  **默认取值**：不涉及。

        :param evs_type: The evs_type of this ServerVolume.
        :type evs_type: str
        """
        self._evs_type = evs_type

    @property
    def evs_id(self):
        r"""Gets the evs_id of this ServerVolume.

        **参数解释**：EVS盘的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :return: The evs_id of this ServerVolume.
        :rtype: str
        """
        return self._evs_id

    @evs_id.setter
    def evs_id(self, evs_id):
        r"""Sets the evs_id of this ServerVolume.

        **参数解释**：EVS盘的ID。 **取值范围**：^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$。

        :param evs_id: The evs_id of this ServerVolume.
        :type evs_id: str
        """
        self._evs_id = evs_id

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
        if not isinstance(other, ServerVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
