# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Detail:

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
        'value': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'unit': 'unit'
    }

    def __init__(self, type=None, value=None, unit=None):
        r"""Detail

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 属性类型。 **取值范围**： - vCPU：CPU核心数。 - SATA：普通IO。 - SAS：高IO。 - SSD：超高IO。 - ESSD：极速型SSD。 - GPSSD：通用型SSD。 - LOCAL_DISK：本地盘。 - mem：内存大小。
        :type type: str
        :param value: **参数解释**： 属性值。 **取值范围**： 不涉及。
        :type value: str
        :param unit: **参数解释**： 属性单位。 **取值范围**： 当type为SATA、SAS、SSD、ESSD时，表示磁盘单位GB
        :type unit: str
        """
        
        

        self._type = None
        self._value = None
        self._unit = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.value = value
        if unit is not None:
            self.unit = unit

    @property
    def type(self):
        r"""Gets the type of this Detail.

        **参数解释**： 属性类型。 **取值范围**： - vCPU：CPU核心数。 - SATA：普通IO。 - SAS：高IO。 - SSD：超高IO。 - ESSD：极速型SSD。 - GPSSD：通用型SSD。 - LOCAL_DISK：本地盘。 - mem：内存大小。

        :return: The type of this Detail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Detail.

        **参数解释**： 属性类型。 **取值范围**： - vCPU：CPU核心数。 - SATA：普通IO。 - SAS：高IO。 - SSD：超高IO。 - ESSD：极速型SSD。 - GPSSD：通用型SSD。 - LOCAL_DISK：本地盘。 - mem：内存大小。

        :param type: The type of this Detail.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this Detail.

        **参数解释**： 属性值。 **取值范围**： 不涉及。

        :return: The value of this Detail.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this Detail.

        **参数解释**： 属性值。 **取值范围**： 不涉及。

        :param value: The value of this Detail.
        :type value: str
        """
        self._value = value

    @property
    def unit(self):
        r"""Gets the unit of this Detail.

        **参数解释**： 属性单位。 **取值范围**： 当type为SATA、SAS、SSD、ESSD时，表示磁盘单位GB

        :return: The unit of this Detail.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this Detail.

        **参数解释**： 属性单位。 **取值范围**： 当type为SATA、SAS、SSD、ESSD时，表示磁盘单位GB

        :param unit: The unit of this Detail.
        :type unit: str
        """
        self._unit = unit

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
        if not isinstance(other, Detail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
