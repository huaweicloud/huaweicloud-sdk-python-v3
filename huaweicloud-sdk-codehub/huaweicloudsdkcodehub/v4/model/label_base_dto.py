# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelBaseDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'color': 'str',
        'description': 'str',
        'text_color': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'color': 'color',
        'description': 'description',
        'text_color': 'text_color'
    }

    def __init__(self, id=None, name=None, color=None, description=None, text_color=None):
        r"""LabelBaseDto

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 标签ID。 **取值范围：** 1-2147483647
        :type id: int
        :param name: **参数解释：** 标签名。 **取值范围：** 不涉及。
        :type name: str
        :param color: **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **取值范围：** 正则&#x60;^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$&#x60;
        :type color: str
        :param description: **参数解释：** 描述。 **取值范围：** 不涉及。
        :type description: str
        :param text_color: **参数解释：** 字体颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **取值范围：** 正则&#x60;^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$&#x60;
        :type text_color: str
        """
        
        

        self._id = None
        self._name = None
        self._color = None
        self._description = None
        self._text_color = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if color is not None:
            self.color = color
        if description is not None:
            self.description = description
        if text_color is not None:
            self.text_color = text_color

    @property
    def id(self):
        r"""Gets the id of this LabelBaseDto.

        **参数解释：** 标签ID。 **取值范围：** 1-2147483647

        :return: The id of this LabelBaseDto.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LabelBaseDto.

        **参数解释：** 标签ID。 **取值范围：** 1-2147483647

        :param id: The id of this LabelBaseDto.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this LabelBaseDto.

        **参数解释：** 标签名。 **取值范围：** 不涉及。

        :return: The name of this LabelBaseDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this LabelBaseDto.

        **参数解释：** 标签名。 **取值范围：** 不涉及。

        :param name: The name of this LabelBaseDto.
        :type name: str
        """
        self._name = name

    @property
    def color(self):
        r"""Gets the color of this LabelBaseDto.

        **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **取值范围：** 正则`^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$`

        :return: The color of this LabelBaseDto.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this LabelBaseDto.

        **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **取值范围：** 正则`^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$`

        :param color: The color of this LabelBaseDto.
        :type color: str
        """
        self._color = color

    @property
    def description(self):
        r"""Gets the description of this LabelBaseDto.

        **参数解释：** 描述。 **取值范围：** 不涉及。

        :return: The description of this LabelBaseDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LabelBaseDto.

        **参数解释：** 描述。 **取值范围：** 不涉及。

        :param description: The description of this LabelBaseDto.
        :type description: str
        """
        self._description = description

    @property
    def text_color(self):
        r"""Gets the text_color of this LabelBaseDto.

        **参数解释：** 字体颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **取值范围：** 正则`^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$`

        :return: The text_color of this LabelBaseDto.
        :rtype: str
        """
        return self._text_color

    @text_color.setter
    def text_color(self, text_color):
        r"""Sets the text_color of this LabelBaseDto.

        **参数解释：** 字体颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **取值范围：** 正则`^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$`

        :param text_color: The text_color of this LabelBaseDto.
        :type text_color: str
        """
        self._text_color = text_color

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
        if not isinstance(other, LabelBaseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
