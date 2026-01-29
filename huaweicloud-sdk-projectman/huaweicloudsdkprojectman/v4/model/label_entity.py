# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LabelEntity:

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
        'label_type': 'str',
        'color': 'str',
        'title': 'str'
    }

    attribute_map = {
        'id': 'id',
        'label_type': 'label_type',
        'color': 'color',
        'title': 'title'
    }

    def __init__(self, id=None, label_type=None, color=None, title=None):
        r"""LabelEntity

        The model defined in huaweicloud sdk

        :param id: 标签id
        :type id: str
        :param label_type: 标签所属工作项类型，对应工作项的type字段
        :type label_type: str
        :param color: 标签颜色RGB
        :type color: str
        :param title: 标签标题
        :type title: str
        """
        
        

        self._id = None
        self._label_type = None
        self._color = None
        self._title = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if label_type is not None:
            self.label_type = label_type
        if color is not None:
            self.color = color
        if title is not None:
            self.title = title

    @property
    def id(self):
        r"""Gets the id of this LabelEntity.

        标签id

        :return: The id of this LabelEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this LabelEntity.

        标签id

        :param id: The id of this LabelEntity.
        :type id: str
        """
        self._id = id

    @property
    def label_type(self):
        r"""Gets the label_type of this LabelEntity.

        标签所属工作项类型，对应工作项的type字段

        :return: The label_type of this LabelEntity.
        :rtype: str
        """
        return self._label_type

    @label_type.setter
    def label_type(self, label_type):
        r"""Sets the label_type of this LabelEntity.

        标签所属工作项类型，对应工作项的type字段

        :param label_type: The label_type of this LabelEntity.
        :type label_type: str
        """
        self._label_type = label_type

    @property
    def color(self):
        r"""Gets the color of this LabelEntity.

        标签颜色RGB

        :return: The color of this LabelEntity.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        r"""Sets the color of this LabelEntity.

        标签颜色RGB

        :param color: The color of this LabelEntity.
        :type color: str
        """
        self._color = color

    @property
    def title(self):
        r"""Gets the title of this LabelEntity.

        标签标题

        :return: The title of this LabelEntity.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this LabelEntity.

        标签标题

        :param title: The title of this LabelEntity.
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
        if not isinstance(other, LabelEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
