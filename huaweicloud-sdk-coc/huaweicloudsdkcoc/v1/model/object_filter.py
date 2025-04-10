# coding: utf-8

import six

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
        'operator': 'str',
        'field': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'operator': 'operator',
        'field': 'field',
        'values': 'values'
    }

    def __init__(self, operator=None, field=None, values=None):
        r"""ObjectFilter

        The model defined in huaweicloud sdk

        :param operator: 操作符 in/like/startwith/endwith/&#x3D;/!&#x3D;/&gt;/&lt;等
        :type operator: str
        :param field: 字段名称
        :type field: str
        :param values: 搜索值
        :type values: list[str]
        """
        
        

        self._operator = None
        self._field = None
        self._values = None
        self.discriminator = None

        self.operator = operator
        self.field = field
        self.values = values

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
        if not isinstance(other, ObjectFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
