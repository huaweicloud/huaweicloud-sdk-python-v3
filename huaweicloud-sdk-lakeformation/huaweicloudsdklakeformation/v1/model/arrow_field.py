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
        'type': 'ArrowType',
        'nullable': 'bool',
        'metadata': 'dict(str, str)',
        'children': 'list[ArrowField]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'nullable': 'nullable',
        'metadata': 'metadata',
        'children': 'children'
    }

    def __init__(self, name=None, type=None, nullable=None, metadata=None, children=None):
        r"""ArrowField

        The model defined in huaweicloud sdk

        :param name: 字段名称。
        :type name: str
        :param type: 
        :type type: :class:`huaweicloudsdklakeformation.v1.ArrowType`
        :param nullable: 字段是否允许为null。
        :type nullable: bool
        :param metadata: 字段的元数据信息。
        :type metadata: dict(str, str)
        :param children: 
        :type children: list[:class:`huaweicloudsdklakeformation.v1.ArrowField`]
        """
        
        

        self._name = None
        self._type = None
        self._nullable = None
        self._metadata = None
        self._children = None
        self.discriminator = None

        self.name = name
        self.type = type
        if nullable is not None:
            self.nullable = nullable
        if metadata is not None:
            self.metadata = metadata
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
    def type(self):
        r"""Gets the type of this ArrowField.

        :return: The type of this ArrowField.
        :rtype: :class:`huaweicloudsdklakeformation.v1.ArrowType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ArrowField.

        :param type: The type of this ArrowField.
        :type type: :class:`huaweicloudsdklakeformation.v1.ArrowType`
        """
        self._type = type

    @property
    def nullable(self):
        r"""Gets the nullable of this ArrowField.

        字段是否允许为null。

        :return: The nullable of this ArrowField.
        :rtype: bool
        """
        return self._nullable

    @nullable.setter
    def nullable(self, nullable):
        r"""Sets the nullable of this ArrowField.

        字段是否允许为null。

        :param nullable: The nullable of this ArrowField.
        :type nullable: bool
        """
        self._nullable = nullable

    @property
    def metadata(self):
        r"""Gets the metadata of this ArrowField.

        字段的元数据信息。

        :return: The metadata of this ArrowField.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ArrowField.

        字段的元数据信息。

        :param metadata: The metadata of this ArrowField.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def children(self):
        r"""Gets the children of this ArrowField.

        :return: The children of this ArrowField.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.ArrowField`]
        """
        return self._children

    @children.setter
    def children(self, children):
        r"""Sets the children of this ArrowField.

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
