# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomFieldV2:

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
        'value': 'str',
        'new_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'new_name': 'new_name'
    }

    def __init__(self, name=None, value=None, new_name=None):
        r"""CustomFieldV2

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 自定义字段。 **取值范围：** 不涉及。
        :type name: str
        :param value: **参数解释：** 自定义字段对应的值。 **取值范围：** 不涉及。
        :type value: str
        :param new_name: **参数解释：** 自定义字段修改后的名称。 **取值范围：** 不涉及。
        :type new_name: str
        """
        
        

        self._name = None
        self._value = None
        self._new_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if new_name is not None:
            self.new_name = new_name

    @property
    def name(self):
        r"""Gets the name of this CustomFieldV2.

        **参数解释：** 自定义字段。 **取值范围：** 不涉及。

        :return: The name of this CustomFieldV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CustomFieldV2.

        **参数解释：** 自定义字段。 **取值范围：** 不涉及。

        :param name: The name of this CustomFieldV2.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this CustomFieldV2.

        **参数解释：** 自定义字段对应的值。 **取值范围：** 不涉及。

        :return: The value of this CustomFieldV2.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CustomFieldV2.

        **参数解释：** 自定义字段对应的值。 **取值范围：** 不涉及。

        :param value: The value of this CustomFieldV2.
        :type value: str
        """
        self._value = value

    @property
    def new_name(self):
        r"""Gets the new_name of this CustomFieldV2.

        **参数解释：** 自定义字段修改后的名称。 **取值范围：** 不涉及。

        :return: The new_name of this CustomFieldV2.
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        r"""Sets the new_name of this CustomFieldV2.

        **参数解释：** 自定义字段修改后的名称。 **取值范围：** 不涉及。

        :param new_name: The new_name of this CustomFieldV2.
        :type new_name: str
        """
        self._new_name = new_name

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
        if not isinstance(other, CustomFieldV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
