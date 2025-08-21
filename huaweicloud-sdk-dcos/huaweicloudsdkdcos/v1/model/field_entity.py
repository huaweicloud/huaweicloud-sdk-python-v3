# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FieldEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_code': 'str',
        'field_value': 'object'
    }

    attribute_map = {
        'field_code': 'field_code',
        'field_value': 'field_value'
    }

    def __init__(self, field_code=None, field_value=None):
        r"""FieldEntity

        The model defined in huaweicloud sdk

        :param field_code: 字段编码
        :type field_code: str
        :param field_value: 字段值
        :type field_value: object
        """
        
        

        self._field_code = None
        self._field_value = None
        self.discriminator = None

        self.field_code = field_code
        if field_value is not None:
            self.field_value = field_value

    @property
    def field_code(self):
        r"""Gets the field_code of this FieldEntity.

        字段编码

        :return: The field_code of this FieldEntity.
        :rtype: str
        """
        return self._field_code

    @field_code.setter
    def field_code(self, field_code):
        r"""Sets the field_code of this FieldEntity.

        字段编码

        :param field_code: The field_code of this FieldEntity.
        :type field_code: str
        """
        self._field_code = field_code

    @property
    def field_value(self):
        r"""Gets the field_value of this FieldEntity.

        字段值

        :return: The field_value of this FieldEntity.
        :rtype: object
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        r"""Sets the field_value of this FieldEntity.

        字段值

        :param field_value: The field_value of this FieldEntity.
        :type field_value: object
        """
        self._field_value = field_value

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
        if not isinstance(other, FieldEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
