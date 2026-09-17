# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NewCustomFieldV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_field': 'str',
        'field_name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'custom_field': 'custom_field',
        'field_name': 'field_name',
        'value': 'value'
    }

    def __init__(self, custom_field=None, field_name=None, value=None):
        r"""NewCustomFieldV2

        The model defined in huaweicloud sdk

        :param custom_field: **参数解释：** 自定义字段。 **取值范围：** 不涉及。
        :type custom_field: str
        :param field_name: **参数解释：** 自定义字段名称。 **取值范围：** 不涉及。
        :type field_name: str
        :param value: **参数解释：** 自定义属性对应的值，多个值以英文逗号区分开。 **取值范围：** 不涉及。
        :type value: str
        """
        
        

        self._custom_field = None
        self._field_name = None
        self._value = None
        self.discriminator = None

        if custom_field is not None:
            self.custom_field = custom_field
        if field_name is not None:
            self.field_name = field_name
        if value is not None:
            self.value = value

    @property
    def custom_field(self):
        r"""Gets the custom_field of this NewCustomFieldV2.

        **参数解释：** 自定义字段。 **取值范围：** 不涉及。

        :return: The custom_field of this NewCustomFieldV2.
        :rtype: str
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        r"""Sets the custom_field of this NewCustomFieldV2.

        **参数解释：** 自定义字段。 **取值范围：** 不涉及。

        :param custom_field: The custom_field of this NewCustomFieldV2.
        :type custom_field: str
        """
        self._custom_field = custom_field

    @property
    def field_name(self):
        r"""Gets the field_name of this NewCustomFieldV2.

        **参数解释：** 自定义字段名称。 **取值范围：** 不涉及。

        :return: The field_name of this NewCustomFieldV2.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this NewCustomFieldV2.

        **参数解释：** 自定义字段名称。 **取值范围：** 不涉及。

        :param field_name: The field_name of this NewCustomFieldV2.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def value(self):
        r"""Gets the value of this NewCustomFieldV2.

        **参数解释：** 自定义属性对应的值，多个值以英文逗号区分开。 **取值范围：** 不涉及。

        :return: The value of this NewCustomFieldV2.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this NewCustomFieldV2.

        **参数解释：** 自定义属性对应的值，多个值以英文逗号区分开。 **取值范围：** 不涉及。

        :param value: The value of this NewCustomFieldV2.
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
        if not isinstance(other, NewCustomFieldV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
