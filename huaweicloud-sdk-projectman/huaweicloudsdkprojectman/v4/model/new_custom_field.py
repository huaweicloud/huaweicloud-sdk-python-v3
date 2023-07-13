# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NewCustomField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_field': 'str',
        'field_name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'custom_field': 'custom_field',
        'field_name': 'field_name',
        'value': 'value'
    }

    def __init__(self, custom_field=None, field_name=None, value=None):
        """NewCustomField

        The model defined in huaweicloud sdk

        :param custom_field: 自定义字段
        :type custom_field: str
        :param field_name: 自定义字段名称
        :type field_name: str
        :param value: 自定义属性对应的值，多个值以英文逗号区分开
        :type value: str
        """
        
        

        self._custom_field = None
        self._field_name = None
        self._value = None
        self.discriminator = None

        if custom_field is not None:
            self.custom_field = custom_field
        if field_name is not None:
            self.field_name = field_name
        if value is not None:
            self.value = value

    @property
    def custom_field(self):
        """Gets the custom_field of this NewCustomField.

        自定义字段

        :return: The custom_field of this NewCustomField.
        :rtype: str
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        """Sets the custom_field of this NewCustomField.

        自定义字段

        :param custom_field: The custom_field of this NewCustomField.
        :type custom_field: str
        """
        self._custom_field = custom_field

    @property
    def field_name(self):
        """Gets the field_name of this NewCustomField.

        自定义字段名称

        :return: The field_name of this NewCustomField.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this NewCustomField.

        自定义字段名称

        :param field_name: The field_name of this NewCustomField.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def value(self):
        """Gets the value of this NewCustomField.

        自定义属性对应的值，多个值以英文逗号区分开

        :return: The value of this NewCustomField.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NewCustomField.

        自定义属性对应的值，多个值以英文逗号区分开

        :param value: The value of this NewCustomField.
        :type value: str
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
        if not isinstance(other, NewCustomField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
