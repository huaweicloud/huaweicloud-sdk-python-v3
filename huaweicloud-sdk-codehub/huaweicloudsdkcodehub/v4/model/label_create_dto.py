# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelCreateDto:

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
        'color': 'str',
        'description': 'str',
        'expires_at': 'date'
    }

    attribute_map = {
        'name': 'name',
        'color': 'color',
        'description': 'description',
        'expires_at': 'expires_at'
    }

    def __init__(self, name=None, color=None, description=None, expires_at=None):
        r"""LabelCreateDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param color: **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **约束限制：** 不涉及。 **取值范围：** 正则&#x60;^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$&#x60; **默认取值：** 不涉及。
        :type color: str
        :param description: **参数解释：** 描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type description: str
        :param expires_at: **参数解释：** 失效时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type expires_at: date
        """
        
        

        self._name = None
        self._color = None
        self._description = None
        self._expires_at = None
        self.discriminator = None

        self.name = name
        if color is not None:
            self.color = color
        if description is not None:
            self.description = description
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def name(self):
        r"""Gets the name of this LabelCreateDto.

        **参数解释：** 标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this LabelCreateDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LabelCreateDto.

        **参数解释：** 标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this LabelCreateDto.
        :type name: str
        """
        self._name = name

    @property
    def color(self):
        r"""Gets the color of this LabelCreateDto.

        **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **约束限制：** 不涉及。 **取值范围：** 正则`^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$` **默认取值：** 不涉及。

        :return: The color of this LabelCreateDto.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this LabelCreateDto.

        **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **约束限制：** 不涉及。 **取值范围：** 正则`^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$` **默认取值：** 不涉及。

        :param color: The color of this LabelCreateDto.
        :type color: str
        """
        self._color = color

    @property
    def description(self):
        r"""Gets the description of this LabelCreateDto.

        **参数解释：** 描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The description of this LabelCreateDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LabelCreateDto.

        **参数解释：** 描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param description: The description of this LabelCreateDto.
        :type description: str
        """
        self._description = description

    @property
    def expires_at(self):
        r"""Gets the expires_at of this LabelCreateDto.

        **参数解释：** 失效时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The expires_at of this LabelCreateDto.
        :rtype: date
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this LabelCreateDto.

        **参数解释：** 失效时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param expires_at: The expires_at of this LabelCreateDto.
        :type expires_at: date
        """
        self._expires_at = expires_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LabelCreateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
