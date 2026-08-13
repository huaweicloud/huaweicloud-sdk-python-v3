# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PaimonField:

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
        'type': 'PaimonType',
        'nullable': 'bool',
        'children': 'list[PaimonField]',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'nullable': 'nullable',
        'children': 'children',
        'description': 'description'
    }

    def __init__(self, name=None, type=None, nullable=None, children=None, description=None):
        r"""PaimonField

        The model defined in huaweicloud sdk

        :param name: 字段名称
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdklakeformation.v1.PaimonType`
        :param nullable: 字段是否允许为null
        :type nullable: bool
        :param children: 子字段
        :type children: list[:class:`huaweicloudsdklakeformation.v1.PaimonField`]
        :param description: 字段描述
        :type description: str
        """
        
        

        self._name = None
        self._type = None
        self._nullable = None
        self._children = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.type = type
        if nullable is not None:
            self.nullable = nullable
        if children is not None:
            self.children = children
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this PaimonField.

        字段名称

        :return: The name of this PaimonField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PaimonField.

        字段名称

        :param name: The name of this PaimonField.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this PaimonField.

        :return: The type of this PaimonField.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PaimonType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this PaimonField.

        :param type: The type of this PaimonField.
        :type type: :class:`huaweicloudsdklakeformation.v1.PaimonType`
        """
        self._type = type

    @property
    def nullable(self):
        r"""Gets the nullable of this PaimonField.

        字段是否允许为null

        :return: The nullable of this PaimonField.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this PaimonField.

        字段是否允许为null

        :param nullable: The nullable of this PaimonField.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def children(self):
        r"""Gets the children of this PaimonField.

        子字段

        :return: The children of this PaimonField.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PaimonField`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this PaimonField.

        子字段

        :param children: The children of this PaimonField.
        :type children: list[:class:`huaweicloudsdklakeformation.v1.PaimonField`]
        """
        self._children = children

    @property
    def description(self):
        r"""Gets the description of this PaimonField.

        字段描述

        :return: The description of this PaimonField.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PaimonField.

        字段描述

        :param description: The description of this PaimonField.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, PaimonField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
