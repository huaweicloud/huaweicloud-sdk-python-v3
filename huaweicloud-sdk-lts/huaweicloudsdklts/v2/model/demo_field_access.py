# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DemoFieldAccess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_name': 'str',
        'field_value': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'field_value': 'field_value'
    }

    def __init__(self, field_name=None, field_value=None):
        r"""DemoFieldAccess

        The model defined in huaweicloud sdk

        :param field_name: 字段名称需和keys中字段保持一致
        :type field_name: str
        :param field_value: 字段值
        :type field_value: str
        """
        
        

        self._field_name = None
        self._field_value = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if field_value is not None:
            self.field_value = field_value

    @property
    def field_name(self):
        r"""Gets the field_name of this DemoFieldAccess.

        字段名称需和keys中字段保持一致

        :return: The field_name of this DemoFieldAccess.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this DemoFieldAccess.

        字段名称需和keys中字段保持一致

        :param field_name: The field_name of this DemoFieldAccess.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def field_value(self):
        r"""Gets the field_value of this DemoFieldAccess.

        字段值

        :return: The field_value of this DemoFieldAccess.
        :rtype: str
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        r"""Sets the field_value of this DemoFieldAccess.

        字段值

        :param field_value: The field_value of this DemoFieldAccess.
        :type field_value: str
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
        if not isinstance(other, DemoFieldAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
