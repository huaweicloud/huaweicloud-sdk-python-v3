# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BodyPutLabelDto:

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
        'new_name': 'str',
        'color': 'str',
        'description': 'str',
        'priority': 'int',
        'expires_at': 'date'
    }

    attribute_map = {
        'name': 'name',
        'new_name': 'new_name',
        'color': 'color',
        'description': 'description',
        'priority': 'priority',
        'expires_at': 'expires_at'
    }

    def __init__(self, name=None, new_name=None, color=None, description=None, priority=None, expires_at=None):
        r"""BodyPutLabelDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param new_name: **参数解释：** 新标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type new_name: str
        :param color: **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **约束限制：** 不涉及。 **取值范围：** 正则&#x60;^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$&#x60; **默认取值：** 不涉及。
        :type color: str
        :param description: **参数解释：** 描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type description: str
        :param priority: **参数解释：** 优先级。 **约束限制：** 不涉及。 **取值范围：** 0-30 **默认取值：** 不涉及。
        :type priority: int
        :param expires_at: **参数解释：** 失效时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type expires_at: date
        """
        
        

        self._name = None
        self._new_name = None
        self._color = None
        self._description = None
        self._priority = None
        self._expires_at = None
        self.discriminator = None

        self.name = name
        if new_name is not None:
            self.new_name = new_name
        if color is not None:
            self.color = color
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if expires_at is not None:
            self.expires_at = expires_at

    @property
    def name(self):
        r"""Gets the name of this BodyPutLabelDto.

        **参数解释：** 标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this BodyPutLabelDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BodyPutLabelDto.

        **参数解释：** 标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this BodyPutLabelDto.
        :type name: str
        """
        self._name = name

    @property
    def new_name(self):
        r"""Gets the new_name of this BodyPutLabelDto.

        **参数解释：** 新标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The new_name of this BodyPutLabelDto.
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        r"""Sets the new_name of this BodyPutLabelDto.

        **参数解释：** 新标签名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param new_name: The new_name of this BodyPutLabelDto.
        :type new_name: str
        """
        self._new_name = new_name

    @property
    def color(self):
        r"""Gets the color of this BodyPutLabelDto.

        **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **约束限制：** 不涉及。 **取值范围：** 正则`^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$` **默认取值：** 不涉及。

        :return: The color of this BodyPutLabelDto.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this BodyPutLabelDto.

        **参数解释：** 标签颜色，以6位十六进制表示法给出，带有前导“#”符号（例如，#FFAABB）。 **约束限制：** 不涉及。 **取值范围：** 正则`^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$` **默认取值：** 不涉及。

        :param color: The color of this BodyPutLabelDto.
        :type color: str
        """
        self._color = color

    @property
    def description(self):
        r"""Gets the description of this BodyPutLabelDto.

        **参数解释：** 描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The description of this BodyPutLabelDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BodyPutLabelDto.

        **参数解释：** 描述。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param description: The description of this BodyPutLabelDto.
        :type description: str
        """
        self._description = description

    @property
    def priority(self):
        r"""Gets the priority of this BodyPutLabelDto.

        **参数解释：** 优先级。 **约束限制：** 不涉及。 **取值范围：** 0-30 **默认取值：** 不涉及。

        :return: The priority of this BodyPutLabelDto.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this BodyPutLabelDto.

        **参数解释：** 优先级。 **约束限制：** 不涉及。 **取值范围：** 0-30 **默认取值：** 不涉及。

        :param priority: The priority of this BodyPutLabelDto.
        :type priority: int
        """
        self._priority = priority

    @property
    def expires_at(self):
        r"""Gets the expires_at of this BodyPutLabelDto.

        **参数解释：** 失效时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The expires_at of this BodyPutLabelDto.
        :rtype: date
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this BodyPutLabelDto.

        **参数解释：** 失效时间。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param expires_at: The expires_at of this BodyPutLabelDto.
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
        if not isinstance(other, BodyPutLabelDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
