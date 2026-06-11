# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArrowType:

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
        'bit_width': 'int',
        'is_signed': 'bool',
        'precision': 'int',
        'scale': 'int',
        'unit': 'str',
        'timezone': 'str',
        'list_size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'bit_width': 'bit_width',
        'is_signed': 'is_signed',
        'precision': 'precision',
        'scale': 'scale',
        'unit': 'unit',
        'timezone': 'timezone',
        'list_size': 'list_size'
    }

    def __init__(self, name=None, bit_width=None, is_signed=None, precision=None, scale=None, unit=None, timezone=None, list_size=None):
        r"""ArrowType

        The model defined in huaweicloud sdk

        :param name: Arrow类型名称，如Int, Float, Utf8, Bool, Date, Timestamp, List, Struct等。
        :type name: str
        :param bit_width: 类型的位宽，适用于Int、Float等数值类型。如Int32的bit_width为32。
        :type bit_width: int
        :param is_signed: 是否为有符号类型，适用于整数类型。
        :type is_signed: bool
        :param precision: Decimal类型的精度。
        :type precision: int
        :param scale: Decimal类型的标度。
        :type scale: int
        :param unit: 时间单位，适用于Date、Timestamp、Time类型。如SECOND、MILLISECOND、MICROSECOND、NANOSECOND。
        :type unit: str
        :param timezone: 时区信息，适用于Timestamp类型。
        :type timezone: str
        :param list_size: FixedSizeList类型的列表大小，表示固定大小列表中的元素数量。
        :type list_size: int
        """
        
        

        self._name = None
        self._bit_width = None
        self._is_signed = None
        self._precision = None
        self._scale = None
        self._unit = None
        self._timezone = None
        self._list_size = None
        self.discriminator = None

        self.name = name
        if bit_width is not None:
            self.bit_width = bit_width
        if is_signed is not None:
            self.is_signed = is_signed
        if precision is not None:
            self.precision = precision
        if scale is not None:
            self.scale = scale
        if unit is not None:
            self.unit = unit
        if timezone is not None:
            self.timezone = timezone
        if list_size is not None:
            self.list_size = list_size

    @property
    def name(self):
        r"""Gets the name of this ArrowType.

        Arrow类型名称，如Int, Float, Utf8, Bool, Date, Timestamp, List, Struct等。

        :return: The name of this ArrowType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ArrowType.

        Arrow类型名称，如Int, Float, Utf8, Bool, Date, Timestamp, List, Struct等。

        :param name: The name of this ArrowType.
        :type name: str
        """
        self._name = name

    @property
    def bit_width(self):
        r"""Gets the bit_width of this ArrowType.

        类型的位宽，适用于Int、Float等数值类型。如Int32的bit_width为32。

        :return: The bit_width of this ArrowType.
        :rtype: int
        """
        return self._bit_width

    @bit_width.setter
    def bit_width(self, bit_width):
        r"""Sets the bit_width of this ArrowType.

        类型的位宽，适用于Int、Float等数值类型。如Int32的bit_width为32。

        :param bit_width: The bit_width of this ArrowType.
        :type bit_width: int
        """
        self._bit_width = bit_width

    @property
    def is_signed(self):
        r"""Gets the is_signed of this ArrowType.

        是否为有符号类型，适用于整数类型。

        :return: The is_signed of this ArrowType.
        :rtype: bool
        """
        return self._is_signed

    @is_signed.setter
    def is_signed(self, is_signed):
        r"""Sets the is_signed of this ArrowType.

        是否为有符号类型，适用于整数类型。

        :param is_signed: The is_signed of this ArrowType.
        :type is_signed: bool
        """
        self._is_signed = is_signed

    @property
    def precision(self):
        r"""Gets the precision of this ArrowType.

        Decimal类型的精度。

        :return: The precision of this ArrowType.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        r"""Sets the precision of this ArrowType.

        Decimal类型的精度。

        :param precision: The precision of this ArrowType.
        :type precision: int
        """
        self._precision = precision

    @property
    def scale(self):
        r"""Gets the scale of this ArrowType.

        Decimal类型的标度。

        :return: The scale of this ArrowType.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        r"""Sets the scale of this ArrowType.

        Decimal类型的标度。

        :param scale: The scale of this ArrowType.
        :type scale: int
        """
        self._scale = scale

    @property
    def unit(self):
        r"""Gets the unit of this ArrowType.

        时间单位，适用于Date、Timestamp、Time类型。如SECOND、MILLISECOND、MICROSECOND、NANOSECOND。

        :return: The unit of this ArrowType.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this ArrowType.

        时间单位，适用于Date、Timestamp、Time类型。如SECOND、MILLISECOND、MICROSECOND、NANOSECOND。

        :param unit: The unit of this ArrowType.
        :type unit: str
        """
        self._unit = unit

    @property
    def timezone(self):
        r"""Gets the timezone of this ArrowType.

        时区信息，适用于Timestamp类型。

        :return: The timezone of this ArrowType.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this ArrowType.

        时区信息，适用于Timestamp类型。

        :param timezone: The timezone of this ArrowType.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def list_size(self):
        r"""Gets the list_size of this ArrowType.

        FixedSizeList类型的列表大小，表示固定大小列表中的元素数量。

        :return: The list_size of this ArrowType.
        :rtype: int
        """
        return self._list_size

    @list_size.setter
    def list_size(self, list_size):
        r"""Sets the list_size of this ArrowType.

        FixedSizeList类型的列表大小，表示固定大小列表中的元素数量。

        :param list_size: The list_size of this ArrowType.
        :type list_size: int
        """
        self._list_size = list_size

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
        if not isinstance(other, ArrowType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
