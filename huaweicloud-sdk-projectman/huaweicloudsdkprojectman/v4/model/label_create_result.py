# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelCreateResult:

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
        'category_types': 'list[str]',
        'color': 'str',
        'title': 'str'
    }

    attribute_map = {
        'id': 'id',
        'category_types': 'category_types',
        'color': 'color',
        'title': 'title'
    }

    def __init__(self, id=None, category_types=None, color=None, title=None):
        r"""LabelCreateResult

        The model defined in huaweicloud sdk

        :param id: 标签ID，可通过查询标签列表接口获取，响应消息体中的id字段的值就是标签ID。 18~19个字符的数字字符串。
        :type id: str
        :param category_types: 标签所属工作项类型编码。
        :type category_types: list[str]
        :param color: 标签颜色RGB。 0~16个字符。
        :type color: str
        :param title: 标签标题。 2~256个字符。
        :type title: str
        """
        
        

        self._id = None
        self._category_types = None
        self._color = None
        self._title = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category_types is not None:
            self.category_types = category_types
        if color is not None:
            self.color = color
        if title is not None:
            self.title = title

    @property
    def id(self):
        r"""Gets the id of this LabelCreateResult.

        标签ID，可通过查询标签列表接口获取，响应消息体中的id字段的值就是标签ID。 18~19个字符的数字字符串。

        :return: The id of this LabelCreateResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LabelCreateResult.

        标签ID，可通过查询标签列表接口获取，响应消息体中的id字段的值就是标签ID。 18~19个字符的数字字符串。

        :param id: The id of this LabelCreateResult.
        :type id: str
        """
        self._id = id

    @property
    def category_types(self):
        r"""Gets the category_types of this LabelCreateResult.

        标签所属工作项类型编码。

        :return: The category_types of this LabelCreateResult.
        :rtype: list[str]
        """
        return self._category_types

    @category_types.setter
    def category_types(self, category_types):
        r"""Sets the category_types of this LabelCreateResult.

        标签所属工作项类型编码。

        :param category_types: The category_types of this LabelCreateResult.
        :type category_types: list[str]
        """
        self._category_types = category_types

    @property
    def color(self):
        r"""Gets the color of this LabelCreateResult.

        标签颜色RGB。 0~16个字符。

        :return: The color of this LabelCreateResult.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this LabelCreateResult.

        标签颜色RGB。 0~16个字符。

        :param color: The color of this LabelCreateResult.
        :type color: str
        """
        self._color = color

    @property
    def title(self):
        r"""Gets the title of this LabelCreateResult.

        标签标题。 2~256个字符。

        :return: The title of this LabelCreateResult.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this LabelCreateResult.

        标签标题。 2~256个字符。

        :param title: The title of this LabelCreateResult.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, LabelCreateResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
