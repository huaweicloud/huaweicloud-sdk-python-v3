# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FrameDecodeConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'frame_decode_type': 'str',
        'max_frame_length': 'int',
        'delimiter': 'str',
        'fixed_frame_length': 'int',
        'field_offset': 'int',
        'field_length': 'int',
        'initial_bytes': 'str',
        'adjustment_length': 'int',
        'initial_bytes_to_strip': 'int'
    }

    attribute_map = {
        'frame_decode_type': 'frame_decode_type',
        'max_frame_length': 'max_frame_length',
        'delimiter': 'delimiter',
        'fixed_frame_length': 'fixed_frame_length',
        'field_offset': 'field_offset',
        'field_length': 'field_length',
        'initial_bytes': 'initial_bytes',
        'adjustment_length': 'adjustment_length',
        'initial_bytes_to_strip': 'initial_bytes_to_strip'
    }

    def __init__(self, frame_decode_type=None, max_frame_length=None, delimiter=None, fixed_frame_length=None, field_offset=None, field_length=None, initial_bytes=None, adjustment_length=None, initial_bytes_to_strip=None):
        r"""FrameDecodeConfig

        The model defined in huaweicloud sdk

        :param frame_decode_type: **参数说明**：拆包组包规则。 **取值范围**： - DELIMITER：通过特定分隔符（如逗号、换行符等）来拆分或组合数据包。 - FIXED_LENGTH：按照固定的字节长度，对每一帧数据进行拆分或组合。 - FIELD_LENGTH：每一帧的长度可变，通过数据包中携带的长度字段信息进行拆分或组合。
        :type frame_decode_type: str
        :param max_frame_length: **参数说明**：单个帧的最大长度。拆包规则为DELIMITER|FIELD_LENGTH时，该参数必选。
        :type max_frame_length: int
        :param delimiter: **参数说明**：分隔符，hex string格式。拆包规则为DELIMITER，该参数必选。
        :type delimiter: str
        :param fixed_frame_length: **参数说明**：单个帧的固定长度。拆包规则为FIXED_LENGTH，该参数必选。
        :type fixed_frame_length: int
        :param field_offset: **参数说明**：指定长度字段在数据包中的起始位置（偏移量）。拆包规则为FIELD_LENGTH ，该参数必选。
        :type field_offset: int
        :param field_length: **参数说明**：指定长度字段占用的字节数。拆包规则为FIELD_LENGTH，该参数必选。
        :type field_length: int
        :param initial_bytes: **参数说明**：起始字符，hex string格式。拆包规则为FIXED_LENGTH，该参数可选。
        :type initial_bytes: str
        :param adjustment_length: **参数说明**：调整长度字段的值。拆包规则为FIELD_LENGTH，该参数可选。
        :type adjustment_length: int
        :param initial_bytes_to_strip: **参数说明**：指定解码后从数据包中去掉的字节数。通常用于去掉长度字段，只保留数据内容。拆包规则为FIELD_LENGTH，该参数可选。
        :type initial_bytes_to_strip: int
        """
        
        

        self._frame_decode_type = None
        self._max_frame_length = None
        self._delimiter = None
        self._fixed_frame_length = None
        self._field_offset = None
        self._field_length = None
        self._initial_bytes = None
        self._adjustment_length = None
        self._initial_bytes_to_strip = None
        self.discriminator = None

        if frame_decode_type is not None:
            self.frame_decode_type = frame_decode_type
        if max_frame_length is not None:
            self.max_frame_length = max_frame_length
        if delimiter is not None:
            self.delimiter = delimiter
        if fixed_frame_length is not None:
            self.fixed_frame_length = fixed_frame_length
        if field_offset is not None:
            self.field_offset = field_offset
        if field_length is not None:
            self.field_length = field_length
        if initial_bytes is not None:
            self.initial_bytes = initial_bytes
        if adjustment_length is not None:
            self.adjustment_length = adjustment_length
        if initial_bytes_to_strip is not None:
            self.initial_bytes_to_strip = initial_bytes_to_strip

    @property
    def frame_decode_type(self):
        r"""Gets the frame_decode_type of this FrameDecodeConfig.

        **参数说明**：拆包组包规则。 **取值范围**： - DELIMITER：通过特定分隔符（如逗号、换行符等）来拆分或组合数据包。 - FIXED_LENGTH：按照固定的字节长度，对每一帧数据进行拆分或组合。 - FIELD_LENGTH：每一帧的长度可变，通过数据包中携带的长度字段信息进行拆分或组合。

        :return: The frame_decode_type of this FrameDecodeConfig.
        :rtype: str
        """
        return self._frame_decode_type

    @frame_decode_type.setter
    def frame_decode_type(self, frame_decode_type):
        r"""Sets the frame_decode_type of this FrameDecodeConfig.

        **参数说明**：拆包组包规则。 **取值范围**： - DELIMITER：通过特定分隔符（如逗号、换行符等）来拆分或组合数据包。 - FIXED_LENGTH：按照固定的字节长度，对每一帧数据进行拆分或组合。 - FIELD_LENGTH：每一帧的长度可变，通过数据包中携带的长度字段信息进行拆分或组合。

        :param frame_decode_type: The frame_decode_type of this FrameDecodeConfig.
        :type frame_decode_type: str
        """
        self._frame_decode_type = frame_decode_type

    @property
    def max_frame_length(self):
        r"""Gets the max_frame_length of this FrameDecodeConfig.

        **参数说明**：单个帧的最大长度。拆包规则为DELIMITER|FIELD_LENGTH时，该参数必选。

        :return: The max_frame_length of this FrameDecodeConfig.
        :rtype: int
        """
        return self._max_frame_length

    @max_frame_length.setter
    def max_frame_length(self, max_frame_length):
        r"""Sets the max_frame_length of this FrameDecodeConfig.

        **参数说明**：单个帧的最大长度。拆包规则为DELIMITER|FIELD_LENGTH时，该参数必选。

        :param max_frame_length: The max_frame_length of this FrameDecodeConfig.
        :type max_frame_length: int
        """
        self._max_frame_length = max_frame_length

    @property
    def delimiter(self):
        r"""Gets the delimiter of this FrameDecodeConfig.

        **参数说明**：分隔符，hex string格式。拆包规则为DELIMITER，该参数必选。

        :return: The delimiter of this FrameDecodeConfig.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        r"""Sets the delimiter of this FrameDecodeConfig.

        **参数说明**：分隔符，hex string格式。拆包规则为DELIMITER，该参数必选。

        :param delimiter: The delimiter of this FrameDecodeConfig.
        :type delimiter: str
        """
        self._delimiter = delimiter

    @property
    def fixed_frame_length(self):
        r"""Gets the fixed_frame_length of this FrameDecodeConfig.

        **参数说明**：单个帧的固定长度。拆包规则为FIXED_LENGTH，该参数必选。

        :return: The fixed_frame_length of this FrameDecodeConfig.
        :rtype: int
        """
        return self._fixed_frame_length

    @fixed_frame_length.setter
    def fixed_frame_length(self, fixed_frame_length):
        r"""Sets the fixed_frame_length of this FrameDecodeConfig.

        **参数说明**：单个帧的固定长度。拆包规则为FIXED_LENGTH，该参数必选。

        :param fixed_frame_length: The fixed_frame_length of this FrameDecodeConfig.
        :type fixed_frame_length: int
        """
        self._fixed_frame_length = fixed_frame_length

    @property
    def field_offset(self):
        r"""Gets the field_offset of this FrameDecodeConfig.

        **参数说明**：指定长度字段在数据包中的起始位置（偏移量）。拆包规则为FIELD_LENGTH ，该参数必选。

        :return: The field_offset of this FrameDecodeConfig.
        :rtype: int
        """
        return self._field_offset

    @field_offset.setter
    def field_offset(self, field_offset):
        r"""Sets the field_offset of this FrameDecodeConfig.

        **参数说明**：指定长度字段在数据包中的起始位置（偏移量）。拆包规则为FIELD_LENGTH ，该参数必选。

        :param field_offset: The field_offset of this FrameDecodeConfig.
        :type field_offset: int
        """
        self._field_offset = field_offset

    @property
    def field_length(self):
        r"""Gets the field_length of this FrameDecodeConfig.

        **参数说明**：指定长度字段占用的字节数。拆包规则为FIELD_LENGTH，该参数必选。

        :return: The field_length of this FrameDecodeConfig.
        :rtype: int
        """
        return self._field_length

    @field_length.setter
    def field_length(self, field_length):
        r"""Sets the field_length of this FrameDecodeConfig.

        **参数说明**：指定长度字段占用的字节数。拆包规则为FIELD_LENGTH，该参数必选。

        :param field_length: The field_length of this FrameDecodeConfig.
        :type field_length: int
        """
        self._field_length = field_length

    @property
    def initial_bytes(self):
        r"""Gets the initial_bytes of this FrameDecodeConfig.

        **参数说明**：起始字符，hex string格式。拆包规则为FIXED_LENGTH，该参数可选。

        :return: The initial_bytes of this FrameDecodeConfig.
        :rtype: str
        """
        return self._initial_bytes

    @initial_bytes.setter
    def initial_bytes(self, initial_bytes):
        r"""Sets the initial_bytes of this FrameDecodeConfig.

        **参数说明**：起始字符，hex string格式。拆包规则为FIXED_LENGTH，该参数可选。

        :param initial_bytes: The initial_bytes of this FrameDecodeConfig.
        :type initial_bytes: str
        """
        self._initial_bytes = initial_bytes

    @property
    def adjustment_length(self):
        r"""Gets the adjustment_length of this FrameDecodeConfig.

        **参数说明**：调整长度字段的值。拆包规则为FIELD_LENGTH，该参数可选。

        :return: The adjustment_length of this FrameDecodeConfig.
        :rtype: int
        """
        return self._adjustment_length

    @adjustment_length.setter
    def adjustment_length(self, adjustment_length):
        r"""Sets the adjustment_length of this FrameDecodeConfig.

        **参数说明**：调整长度字段的值。拆包规则为FIELD_LENGTH，该参数可选。

        :param adjustment_length: The adjustment_length of this FrameDecodeConfig.
        :type adjustment_length: int
        """
        self._adjustment_length = adjustment_length

    @property
    def initial_bytes_to_strip(self):
        r"""Gets the initial_bytes_to_strip of this FrameDecodeConfig.

        **参数说明**：指定解码后从数据包中去掉的字节数。通常用于去掉长度字段，只保留数据内容。拆包规则为FIELD_LENGTH，该参数可选。

        :return: The initial_bytes_to_strip of this FrameDecodeConfig.
        :rtype: int
        """
        return self._initial_bytes_to_strip

    @initial_bytes_to_strip.setter
    def initial_bytes_to_strip(self, initial_bytes_to_strip):
        r"""Sets the initial_bytes_to_strip of this FrameDecodeConfig.

        **参数说明**：指定解码后从数据包中去掉的字节数。通常用于去掉长度字段，只保留数据内容。拆包规则为FIELD_LENGTH，该参数可选。

        :param initial_bytes_to_strip: The initial_bytes_to_strip of this FrameDecodeConfig.
        :type initial_bytes_to_strip: int
        """
        self._initial_bytes_to_strip = initial_bytes_to_strip

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
        if not isinstance(other, FrameDecodeConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
