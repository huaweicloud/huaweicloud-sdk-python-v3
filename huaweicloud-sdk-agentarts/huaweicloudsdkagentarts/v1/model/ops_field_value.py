# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsFieldValue:

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
        'content_type': 'str',
        'value': 'object'
    }

    attribute_map = {
        'type': 'type',
        'content_type': 'content_type',
        'value': 'value'
    }

    def __init__(self, type=None, content_type=None, value=None):
        r"""OpsFieldValue

        The model defined in huaweicloud sdk

        :param type: **参数解释：** 字段的数据类型。 **取值范围：** 如 string, integer, float 等。
        :type type: str
        :param content_type: **参数解释：** 内容展示类型。 **取值范围：** 如 text, markdown, image 等。
        :type content_type: str
        :param value: **参数解释：** 字段承载的实际业务数据。 **取值范围：** 根据type字段确定具体数据类型和格式。
        :type value: object
        """
        
        

        self._type = None
        self._content_type = None
        self._value = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if content_type is not None:
            self.content_type = content_type
        if value is not None:
            self.value = value

    @property
    def type(self):
        r"""Gets the type of this OpsFieldValue.

        **参数解释：** 字段的数据类型。 **取值范围：** 如 string, integer, float 等。

        :return: The type of this OpsFieldValue.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OpsFieldValue.

        **参数解释：** 字段的数据类型。 **取值范围：** 如 string, integer, float 等。

        :param type: The type of this OpsFieldValue.
        :type type: str
        """
        self._type = type

    @property
    def content_type(self):
        r"""Gets the content_type of this OpsFieldValue.

        **参数解释：** 内容展示类型。 **取值范围：** 如 text, markdown, image 等。

        :return: The content_type of this OpsFieldValue.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this OpsFieldValue.

        **参数解释：** 内容展示类型。 **取值范围：** 如 text, markdown, image 等。

        :param content_type: The content_type of this OpsFieldValue.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def value(self):
        r"""Gets the value of this OpsFieldValue.

        **参数解释：** 字段承载的实际业务数据。 **取值范围：** 根据type字段确定具体数据类型和格式。

        :return: The value of this OpsFieldValue.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OpsFieldValue.

        **参数解释：** 字段承载的实际业务数据。 **取值范围：** 根据type字段确定具体数据类型和格式。

        :param value: The value of this OpsFieldValue.
        :type value: object
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
        if not isinstance(other, OpsFieldValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
