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
        'display_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name'
    }

    def __init__(self, id=None, display_name=None):
        r"""OpsLabelValueItem

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 标签值的唯一标识符（ID）。 **约束限制：** 字符串长度0-100。 **取值范围：** 字符长度0-100。 **默认值：** 不涉及
        :type id: str
        :param display_name: **参数解释：** 标签面向用户展示的名称。 **约束限制：** 字符串长度1-100。 **取值范围：** 字符长度1-100。 **默认值：** 不涉及
        :type display_name: str
        """
        
        

        self._id = None
        self._display_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.display_name = display_name

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
    def display_name(self):
        r"""Gets the display_name of this OpsLabelValueItem.

        **参数解释：** 标签面向用户展示的名称。 **约束限制：** 字符串长度1-100。 **取值范围：** 字符长度1-100。 **默认值：** 不涉及

        :return: The display_name of this OpsLabelValueItem.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this OpsLabelValueItem.

        **参数解释：** 标签面向用户展示的名称。 **约束限制：** 字符串长度1-100。 **取值范围：** 字符长度1-100。 **默认值：** 不涉及

        :param display_name: The display_name of this OpsLabelValueItem.
        :type display_name: str
        """
        self._display_name = display_name

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
