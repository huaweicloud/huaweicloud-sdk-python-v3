# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ArrowField:

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
        'nullable': 'bool',
        'type': 'str',
        'children': 'list[ArrowField]'
    }

    attribute_map = {
        'name': 'name',
        'nullable': 'nullable',
        'type': 'type',
        'children': 'children'
    }

    def __init__(self, name=None, nullable=None, type=None, children=None):
        r"""ArrowField

        The model defined in huaweicloud sdk

        :param name: 字段名称。
        :type name: str
        :param nullable: 字段是否可为空。
        :type nullable: bool
        :param type: 字段类型。
        :type type: str
        :param children: 子字段列表（用于嵌套类型）。
        :type children: list[:class:`huaweicloudsdklakeformation.v1.ArrowField`]
        """
        
        

        self._name = None
        self._nullable = None
        self._type = None
        self._children = None
        self.discriminator = None

        self.name = name
        self.nullable = nullable
        self.type = type
        if children is not None:
            self.children = children

    @property
    def name(self):
        r"""Gets the name of this ArrowField.

        字段名称。

        :return: The name of this ArrowField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ArrowField.

        字段名称。

        :param name: The name of this ArrowField.
        :type name: str
        """
        self._name = name

    @property
    def nullable(self):
        r"""Gets the nullable of this ArrowField.

        字段是否可为空。

        :return: The nullable of this ArrowField.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this ArrowField.

        字段是否可为空。

        :param nullable: The nullable of this ArrowField.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def type(self):
        r"""Gets the type of this ArrowField.

        字段类型。

        :return: The type of this ArrowField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ArrowField.

        字段类型。

        :param type: The type of this ArrowField.
        :type type: str
        """
        self._type = type

    @property
    def children(self):
        r"""Gets the children of this ArrowField.

        子字段列表（用于嵌套类型）。

        :return: The children of this ArrowField.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ArrowField`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this ArrowField.

        子字段列表（用于嵌套类型）。

        :param children: The children of this ArrowField.
        :type children: list[:class:`huaweicloudsdklakeformation.v1.ArrowField`]
        """
        self._children = children

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
        if not isinstance(other, ArrowField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
