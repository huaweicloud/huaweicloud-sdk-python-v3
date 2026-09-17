# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsLabelValueItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'tag_value_name': 'str',
        'status': 'str',
        'color': 'str',
        'order': 'int'
    }

    attribute_map = {
        'id': 'id',
        'tag_value_name': 'tag_value_name',
        'status': 'status',
        'color': 'color',
        'order': 'order'
    }

    def __init__(self, id=None, tag_value_name=None, status=None, color=None, order=None):
        r"""OpsLabelValueItem

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 标签值的唯一标识符（ID）。 **约束限制：** 字符串长度0-100。 **取值范围：** 字符长度0-100。 **默认值：** 不涉及
        :type id: str
        :param tag_value_name: **参数解释：** 标签面向用户展示的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tag_value_name: str
        :param status: **参数解释：** 标签项状态。 **约束限制：** 可选，必须为枚举值之一。 **取值范围：** - ACTIVE：启用 - INACTIVE：停用 **默认取值：** ACTIVE（不传默认为启用）。
        :type status: str
        :param color: **参数解释：** 标签项展示颜色。 **约束限制：** 不涉及。 **取值范围：** 0~1000。 **默认取值：** 不涉及。
        :type color: str
        :param order: **参数解释：** 标签项排序序号，数值越小展示越靠前（按升序排列）。 **约束限制：** 可选，非负整数。 **取值范围：** 0~10000。 **默认取值：** 0（不传时默认为0，按添加顺序展示）。
        :type order: int
        """
        
        

        self._id = None
        self._tag_value_name = None
        self._status = None
        self._color = None
        self._order = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.tag_value_name = tag_value_name
        if status is not None:
            self.status = status
        if color is not None:
            self.color = color
        if order is not None:
            self.order = order

    @property
    def id(self):
        r"""Gets the id of this OpsLabelValueItem.

        **参数解释：** 标签值的唯一标识符（ID）。 **约束限制：** 字符串长度0-100。 **取值范围：** 字符长度0-100。 **默认值：** 不涉及

        :return: The id of this OpsLabelValueItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsLabelValueItem.

        **参数解释：** 标签值的唯一标识符（ID）。 **约束限制：** 字符串长度0-100。 **取值范围：** 字符长度0-100。 **默认值：** 不涉及

        :param id: The id of this OpsLabelValueItem.
        :type id: str
        """
        self._id = id

    @property
    def tag_value_name(self):
        r"""Gets the tag_value_name of this OpsLabelValueItem.

        **参数解释：** 标签面向用户展示的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tag_value_name of this OpsLabelValueItem.
        :rtype: str
        """
        return self._tag_value_name

    @tag_value_name.setter
    def tag_value_name(self, tag_value_name):
        r"""Sets the tag_value_name of this OpsLabelValueItem.

        **参数解释：** 标签面向用户展示的名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tag_value_name: The tag_value_name of this OpsLabelValueItem.
        :type tag_value_name: str
        """
        self._tag_value_name = tag_value_name

    @property
    def status(self):
        r"""Gets the status of this OpsLabelValueItem.

        **参数解释：** 标签项状态。 **约束限制：** 可选，必须为枚举值之一。 **取值范围：** - ACTIVE：启用 - INACTIVE：停用 **默认取值：** ACTIVE（不传默认为启用）。

        :return: The status of this OpsLabelValueItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this OpsLabelValueItem.

        **参数解释：** 标签项状态。 **约束限制：** 可选，必须为枚举值之一。 **取值范围：** - ACTIVE：启用 - INACTIVE：停用 **默认取值：** ACTIVE（不传默认为启用）。

        :param status: The status of this OpsLabelValueItem.
        :type status: str
        """
        self._status = status

    @property
    def color(self):
        r"""Gets the color of this OpsLabelValueItem.

        **参数解释：** 标签项展示颜色。 **约束限制：** 不涉及。 **取值范围：** 0~1000。 **默认取值：** 不涉及。

        :return: The color of this OpsLabelValueItem.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this OpsLabelValueItem.

        **参数解释：** 标签项展示颜色。 **约束限制：** 不涉及。 **取值范围：** 0~1000。 **默认取值：** 不涉及。

        :param color: The color of this OpsLabelValueItem.
        :type color: str
        """
        self._color = color

    @property
    def order(self):
        r"""Gets the order of this OpsLabelValueItem.

        **参数解释：** 标签项排序序号，数值越小展示越靠前（按升序排列）。 **约束限制：** 可选，非负整数。 **取值范围：** 0~10000。 **默认取值：** 0（不传时默认为0，按添加顺序展示）。

        :return: The order of this OpsLabelValueItem.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this OpsLabelValueItem.

        **参数解释：** 标签项排序序号，数值越小展示越靠前（按升序排列）。 **约束限制：** 可选，非负整数。 **取值范围：** 0~10000。 **默认取值：** 0（不传时默认为0，按添加顺序展示）。

        :param order: The order of this OpsLabelValueItem.
        :type order: int
        """
        self._order = order

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
        if not isinstance(other, OpsLabelValueItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
