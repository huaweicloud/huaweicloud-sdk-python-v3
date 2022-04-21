# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizedExtension:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'object_identifier': 'str',
        'value': 'str'
    }

    attribute_map = {
        'object_identifier': 'object_identifier',
        'value': 'value'
    }

    def __init__(self, object_identifier=None, value=None):
        """CustomizedExtension

        The model defined in huaweicloud sdk

        :param object_identifier: 对象标识符。 &gt; 本参数需要满足ASN1规范的点分十进制符号格式的字符串，如1.3.6.1.4.1.2011.4.99。
        :type object_identifier: str
        :param value: 自定义属性内容。
        :type value: str
        """
        
        

        self._object_identifier = None
        self._value = None
        self.discriminator = None

        if object_identifier is not None:
            self.object_identifier = object_identifier
        if value is not None:
            self.value = value

    @property
    def object_identifier(self):
        """Gets the object_identifier of this CustomizedExtension.

        对象标识符。 > 本参数需要满足ASN1规范的点分十进制符号格式的字符串，如1.3.6.1.4.1.2011.4.99。

        :return: The object_identifier of this CustomizedExtension.
        :rtype: str
        """
        return self._object_identifier

    @object_identifier.setter
    def object_identifier(self, object_identifier):
        """Sets the object_identifier of this CustomizedExtension.

        对象标识符。 > 本参数需要满足ASN1规范的点分十进制符号格式的字符串，如1.3.6.1.4.1.2011.4.99。

        :param object_identifier: The object_identifier of this CustomizedExtension.
        :type object_identifier: str
        """
        self._object_identifier = object_identifier

    @property
    def value(self):
        """Gets the value of this CustomizedExtension.

        自定义属性内容。

        :return: The value of this CustomizedExtension.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomizedExtension.

        自定义属性内容。

        :param value: The value of this CustomizedExtension.
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
        if not isinstance(other, CustomizedExtension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
