# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerDataVolume:

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
        'count': 'int'
    }

    attribute_map = {
        'size': 'size',
        'type': 'type',
        'count': 'count'
    }

    def __init__(self, size=None, type=None, count=None):
        r"""ServerDataVolume

        The model defined in huaweicloud sdk

        :param size: **参数解释**：数据盘大小。表示分配给数据盘的存储空间大小。 **约束限制**：不涉及。 **取值范围**：100 - 32768 GB **默认取值**：不涉及。
        :type size: int
        :param type: **参数解释**：系统盘类型。表示数据盘的存储类型。 **约束限制**：不涉及。 **取值范围**： - ESSD：极速型SSD云硬盘 - GPSSD：通用型SSD云硬盘 - SAS：高IO云硬盘 - SATA：普通IO云硬盘 - SSD：超高IO云硬盘 **默认取值**：不涉及。
        :type type: str
        :param count: **参数解释**：数据盘个数。表示为实例分配的数据盘数量。 **约束限制**：不涉及。 **取值范围**：1 - 8 **默认取值**：不涉及。
        :type count: int
        """
        
        

        self._size = None
        self._type = None
        self._count = None
        self.discriminator = None

        self.size = size
        self.type = type
        self.count = count

    @property
    def size(self):
        r"""Gets the size of this ServerDataVolume.

        **参数解释**：数据盘大小。表示分配给数据盘的存储空间大小。 **约束限制**：不涉及。 **取值范围**：100 - 32768 GB **默认取值**：不涉及。

        :return: The size of this ServerDataVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ServerDataVolume.

        **参数解释**：数据盘大小。表示分配给数据盘的存储空间大小。 **约束限制**：不涉及。 **取值范围**：100 - 32768 GB **默认取值**：不涉及。

        :param size: The size of this ServerDataVolume.
        :type size: int
        """
        self._size = size

    @property
    def type(self):
        r"""Gets the type of this ServerDataVolume.

        **参数解释**：系统盘类型。表示数据盘的存储类型。 **约束限制**：不涉及。 **取值范围**： - ESSD：极速型SSD云硬盘 - GPSSD：通用型SSD云硬盘 - SAS：高IO云硬盘 - SATA：普通IO云硬盘 - SSD：超高IO云硬盘 **默认取值**：不涉及。

        :return: The type of this ServerDataVolume.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ServerDataVolume.

        **参数解释**：系统盘类型。表示数据盘的存储类型。 **约束限制**：不涉及。 **取值范围**： - ESSD：极速型SSD云硬盘 - GPSSD：通用型SSD云硬盘 - SAS：高IO云硬盘 - SATA：普通IO云硬盘 - SSD：超高IO云硬盘 **默认取值**：不涉及。

        :param type: The type of this ServerDataVolume.
        :type type: str
        """
        self._type = type

    @property
    def count(self):
        r"""Gets the count of this ServerDataVolume.

        **参数解释**：数据盘个数。表示为实例分配的数据盘数量。 **约束限制**：不涉及。 **取值范围**：1 - 8 **默认取值**：不涉及。

        :return: The count of this ServerDataVolume.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ServerDataVolume.

        **参数解释**：数据盘个数。表示为实例分配的数据盘数量。 **约束限制**：不涉及。 **取值范围**：1 - 8 **默认取值**：不涉及。

        :param count: The count of this ServerDataVolume.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ServerDataVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
