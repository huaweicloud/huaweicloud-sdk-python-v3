# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectFilter:

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
        'operator': 'str',
        'field': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'operator': 'operator',
        'field': 'field',
        'values': 'values'
    }

    def __init__(self, name=None, operator=None, field=None, values=None):
        r"""ObjectFilter

        The model defined in huaweicloud sdk

        :param name: 条件名称
        :type name: str
        :param operator: 操作符 in/like/startwith/endwith/&#x3D;/!&#x3D;/&gt;/&lt;等
        :type operator: str
        :param field: 字段名称
        :type field: str
        :param values: 搜索值
        :type values: list[str]
        """
        
        

        self._name = None
        self._operator = None
        self._field = None
        self._values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if operator is not None:
            self.operator = operator
        if field is not None:
            self.field = field
        if values is not None:
            self.values = values

    @property
    def name(self):
        r"""Gets the name of this ObjectFilter.

        条件名称

        :return: The name of this ObjectFilter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ObjectFilter.

        条件名称

        :param name: The name of this ObjectFilter.
        :type name: str
        """
        self._name = name

    @property
    def operator(self):
        r"""Gets the operator of this ObjectFilter.

        操作符 in/like/startwith/endwith/=/!=/>/<等

        :return: The operator of this ObjectFilter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ObjectFilter.

        操作符 in/like/startwith/endwith/=/!=/>/<等

        :param operator: The operator of this ObjectFilter.
        :type operator: str
        """
        self._operator = operator

    @property
    def field(self):
        r"""Gets the field of this ObjectFilter.

        字段名称

        :return: The field of this ObjectFilter.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this ObjectFilter.

        字段名称

        :param field: The field of this ObjectFilter.
        :type field: str
        """
        self._field = field

    @property
    def values(self):
        r"""Gets the values of this ObjectFilter.

        搜索值

        :return: The values of this ObjectFilter.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ObjectFilter.

        搜索值

        :param values: The values of this ObjectFilter.
        :type values: list[str]
        """
        self._values = values

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
        if not isinstance(other, ObjectFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
