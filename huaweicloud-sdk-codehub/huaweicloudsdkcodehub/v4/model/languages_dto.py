# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LanguagesDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'color': 'str',
        'label': 'str',
        'value': 'float'
    }

    attribute_map = {
        'color': 'color',
        'label': 'label',
        'value': 'value'
    }

    def __init__(self, color=None, label=None, value=None):
        r"""LanguagesDto

        The model defined in huaweicloud sdk

        :param color: **参数解释：** 颜色。
        :type color: str
        :param label: **参数解释：** 语言类型。
        :type label: str
        :param value: **参数解释：** 比重。
        :type value: float
        """
        
        

        self._color = None
        self._label = None
        self._value = None
        self.discriminator = None

        if color is not None:
            self.color = color
        if label is not None:
            self.label = label
        if value is not None:
            self.value = value

    @property
    def color(self):
        r"""Gets the color of this LanguagesDto.

        **参数解释：** 颜色。

        :return: The color of this LanguagesDto.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this LanguagesDto.

        **参数解释：** 颜色。

        :param color: The color of this LanguagesDto.
        :type color: str
        """
        self._color = color

    @property
    def label(self):
        r"""Gets the label of this LanguagesDto.

        **参数解释：** 语言类型。

        :return: The label of this LanguagesDto.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this LanguagesDto.

        **参数解释：** 语言类型。

        :param label: The label of this LanguagesDto.
        :type label: str
        """
        self._label = label

    @property
    def value(self):
        r"""Gets the value of this LanguagesDto.

        **参数解释：** 比重。

        :return: The value of this LanguagesDto.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this LanguagesDto.

        **参数解释：** 比重。

        :param value: The value of this LanguagesDto.
        :type value: float
        """
        self._value = value

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
        if not isinstance(other, LanguagesDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
