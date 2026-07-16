# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFieldValueInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'type': 'str',
        'content_type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'key': 'key',
        'type': 'type',
        'content_type': 'content_type',
        'value': 'value'
    }

    def __init__(self, key=None, type=None, content_type=None, value=None):
        r"""OpsFieldValueInput

        The model defined in huaweicloud sdk

        :param key: **参数解释：** 字段的键名，需与评测集Schema中定义的字段名保持一致。 **约束限制：** 字符串长度为0到10000个字符。 **取值范围：** 符合Schema定义的Key字符串。 **默认取值：** 不涉及。 
        :type key: str
        :param type: **参数解释：** 字段的数据存储类型，决定系统底层解析逻辑。 **约束限制：** 长度0到10000字符。 **取值范围：** 常见值如 string, integer, float, boolean, object 等。 **默认取值：** 不涉及。 
        :type type: str
        :param content_type: **参数解释：** 字段的内容表现形式，用于前端渲染或后端逻辑识别。 **约束限制：** 长度0到10000字符。 **取值范围：** 常见值如 text, markdown, image_url, file_path 等。 **默认取值：** text。 
        :type content_type: str
        :param value: **参数解释：** 字段承载的实际业务数据值。 **约束限制：** 长度0到10000字符。 **取值范围：** 根据type定义，需符合对应的解析要求。 **默认取值：** 不涉及。 
        :type value: str
        """
        
        

        self._key = None
        self._type = None
        self._content_type = None
        self._value = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if type is not None:
            self.type = type
        if content_type is not None:
            self.content_type = content_type
        if value is not None:
            self.value = value

    @property
    def key(self):
        r"""Gets the key of this OpsFieldValueInput.

        **参数解释：** 字段的键名，需与评测集Schema中定义的字段名保持一致。 **约束限制：** 字符串长度为0到10000个字符。 **取值范围：** 符合Schema定义的Key字符串。 **默认取值：** 不涉及。 

        :return: The key of this OpsFieldValueInput.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this OpsFieldValueInput.

        **参数解释：** 字段的键名，需与评测集Schema中定义的字段名保持一致。 **约束限制：** 字符串长度为0到10000个字符。 **取值范围：** 符合Schema定义的Key字符串。 **默认取值：** 不涉及。 

        :param key: The key of this OpsFieldValueInput.
        :type key: str
        """
        self._key = key

    @property
    def type(self):
        r"""Gets the type of this OpsFieldValueInput.

        **参数解释：** 字段的数据存储类型，决定系统底层解析逻辑。 **约束限制：** 长度0到10000字符。 **取值范围：** 常见值如 string, integer, float, boolean, object 等。 **默认取值：** 不涉及。 

        :return: The type of this OpsFieldValueInput.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsFieldValueInput.

        **参数解释：** 字段的数据存储类型，决定系统底层解析逻辑。 **约束限制：** 长度0到10000字符。 **取值范围：** 常见值如 string, integer, float, boolean, object 等。 **默认取值：** 不涉及。 

        :param type: The type of this OpsFieldValueInput.
        :type type: str
        """
        self._type = type

    @property
    def content_type(self):
        r"""Gets the content_type of this OpsFieldValueInput.

        **参数解释：** 字段的内容表现形式，用于前端渲染或后端逻辑识别。 **约束限制：** 长度0到10000字符。 **取值范围：** 常见值如 text, markdown, image_url, file_path 等。 **默认取值：** text。 

        :return: The content_type of this OpsFieldValueInput.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this OpsFieldValueInput.

        **参数解释：** 字段的内容表现形式，用于前端渲染或后端逻辑识别。 **约束限制：** 长度0到10000字符。 **取值范围：** 常见值如 text, markdown, image_url, file_path 等。 **默认取值：** text。 

        :param content_type: The content_type of this OpsFieldValueInput.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def value(self):
        r"""Gets the value of this OpsFieldValueInput.

        **参数解释：** 字段承载的实际业务数据值。 **约束限制：** 长度0到10000字符。 **取值范围：** 根据type定义，需符合对应的解析要求。 **默认取值：** 不涉及。 

        :return: The value of this OpsFieldValueInput.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OpsFieldValueInput.

        **参数解释：** 字段承载的实际业务数据值。 **约束限制：** 长度0到10000字符。 **取值范围：** 根据type定义，需符合对应的解析要求。 **默认取值：** 不涉及。 

        :param value: The value of this OpsFieldValueInput.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, OpsFieldValueInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
