# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label_type': 'str',
        'color': 'str',
        'title': 'str',
        'category_types': 'list[str]'
    }

    attribute_map = {
        'label_type': 'label_type',
        'color': 'color',
        'title': 'title',
        'category_types': 'category_types'
    }

    def __init__(self, label_type=None, color=None, title=None, category_types=None):
        r"""LabelParam

        The model defined in huaweicloud sdk

        :param label_type: 标签所属工作项类型，对应工作项的type字段，枚举类型。不推荐使用此参数，建议使用category_types参数。
        :type label_type: str
        :param color: 标签颜色，作为更新参数时非必填。
        :type color: str
        :param title: 标签标题。 1~30个字符。
        :type title: str
        :param category_types: 标签所属工作项类型编码。
        :type category_types: list[str]
        """
        
        

        self._label_type = None
        self._color = None
        self._title = None
        self._category_types = None
        self.discriminator = None

        if label_type is not None:
            self.label_type = label_type
        self.color = color
        self.title = title
        self.category_types = category_types

    @property
    def label_type(self):
        r"""Gets the label_type of this LabelParam.

        标签所属工作项类型，对应工作项的type字段，枚举类型。不推荐使用此参数，建议使用category_types参数。

        :return: The label_type of this LabelParam.
        :rtype: str
        """
        return self._label_type

    @label_type.setter
    def label_type(self, label_type):
        r"""Sets the label_type of this LabelParam.

        标签所属工作项类型，对应工作项的type字段，枚举类型。不推荐使用此参数，建议使用category_types参数。

        :param label_type: The label_type of this LabelParam.
        :type label_type: str
        """
        self._label_type = label_type

    @property
    def color(self):
        r"""Gets the color of this LabelParam.

        标签颜色，作为更新参数时非必填。

        :return: The color of this LabelParam.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this LabelParam.

        标签颜色，作为更新参数时非必填。

        :param color: The color of this LabelParam.
        :type color: str
        """
        self._color = color

    @property
    def title(self):
        r"""Gets the title of this LabelParam.

        标签标题。 1~30个字符。

        :return: The title of this LabelParam.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this LabelParam.

        标签标题。 1~30个字符。

        :param title: The title of this LabelParam.
        :type title: str
        """
        self._title = title

    @property
    def category_types(self):
        r"""Gets the category_types of this LabelParam.

        标签所属工作项类型编码。

        :return: The category_types of this LabelParam.
        :rtype: list[str]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        r"""Sets the category_types of this LabelParam.

        标签所属工作项类型编码。

        :param category_types: The category_types of this LabelParam.
        :type category_types: list[str]
        """
        self._category_types = category_types

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
        if not isinstance(other, LabelParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
