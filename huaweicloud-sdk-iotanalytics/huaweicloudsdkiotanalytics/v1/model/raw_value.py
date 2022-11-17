# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RawValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'property_name': 'str',
        'values': 'list[object]'
    }

    attribute_map = {
        'property_name': 'property_name',
        'values': 'values'
    }

    def __init__(self, property_name=None, values=None):
        """RawValue

        The model defined in huaweicloud sdk

        :param property_name: 属性名称
        :type property_name: str
        :param values: 资产属性的历史值序列，示例：[1,2]
        :type values: list[object]
        """
        
        

        self._property_name = None
        self._values = None
        self.discriminator = None

        if property_name is not None:
            self.property_name = property_name
        if values is not None:
            self.values = values

    @property
    def property_name(self):
        """Gets the property_name of this RawValue.

        属性名称

        :return: The property_name of this RawValue.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this RawValue.

        属性名称

        :param property_name: The property_name of this RawValue.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def values(self):
        """Gets the values of this RawValue.

        资产属性的历史值序列，示例：[1,2]

        :return: The values of this RawValue.
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this RawValue.

        资产属性的历史值序列，示例：[1,2]

        :param values: The values of this RawValue.
        :type values: list[object]
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
        if not isinstance(other, RawValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
