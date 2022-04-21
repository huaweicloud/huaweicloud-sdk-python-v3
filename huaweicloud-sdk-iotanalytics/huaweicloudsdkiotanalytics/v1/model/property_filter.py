# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropertyFilter:

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
        'operator': 'str',
        'value': 'object'
    }

    attribute_map = {
        'property_name': 'property_name',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, property_name=None, operator=None, value=None):
        """PropertyFilter

        The model defined in huaweicloud sdk

        :param property_name: 过滤属性名称，正则：\&quot;^[a-zA-Z0-9_]{1,64}$\&quot;
        :type property_name: str
        :param operator: 过滤操作方式,当前仅支持“&#x3D;”
        :type operator: str
        :param value: 过滤属性值
        :type value: object
        """
        
        

        self._property_name = None
        self._operator = None
        self._value = None
        self.discriminator = None

        self.property_name = property_name
        self.operator = operator
        self.value = value

    @property
    def property_name(self):
        """Gets the property_name of this PropertyFilter.

        过滤属性名称，正则：\"^[a-zA-Z0-9_]{1,64}$\"

        :return: The property_name of this PropertyFilter.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this PropertyFilter.

        过滤属性名称，正则：\"^[a-zA-Z0-9_]{1,64}$\"

        :param property_name: The property_name of this PropertyFilter.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def operator(self):
        """Gets the operator of this PropertyFilter.

        过滤操作方式,当前仅支持“=”

        :return: The operator of this PropertyFilter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this PropertyFilter.

        过滤操作方式,当前仅支持“=”

        :param operator: The operator of this PropertyFilter.
        :type operator: str
        """
        self._operator = operator

    @property
    def value(self):
        """Gets the value of this PropertyFilter.

        过滤属性值

        :return: The value of this PropertyFilter.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PropertyFilter.

        过滤属性值

        :param value: The value of this PropertyFilter.
        :type value: object
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
        if not isinstance(other, PropertyFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
