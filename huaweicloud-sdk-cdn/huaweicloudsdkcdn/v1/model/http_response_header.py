# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpResponseHeader:

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
        'value': 'str',
        'action': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'action': 'action'
    }

    def __init__(self, name=None, value=None, action=None):
        """HttpResponseHeader

        The model defined in huaweicloud sdk

        :param name: 设置HTTP响应头参数。取值：\&quot;Content-Disposition\&quot;, \&quot;Content-Language\&quot;, \&quot;Access-Control-Allow-Origin\&quot;,\&quot;Access-Control-Allow-Methods\&quot;, \&quot;Access-Control-Max-Age\&quot;, \&quot;Access-Control-Expose-Headers\&quot;或自定义头部。格式要求：长度1~100，以字母开头，可以使用字母、数字和短横杠。
        :type name: str
        :param value: 设置HTTP响应头参数的值。自定义HTTP响应头参数长度范围1~256，支持字母、数字和特定字符（.-_*#!%&amp;+|^~&#39;\&quot;/:;,&#x3D;@?）。
        :type value: str
        :param action: 设置http响应头操作类型，取值“set/delete”。set代表设置，delete代表删除。
        :type action: str
        """
        
        

        self._name = None
        self._value = None
        self._action = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value
        self.action = action

    @property
    def name(self):
        """Gets the name of this HttpResponseHeader.

        设置HTTP响应头参数。取值：\"Content-Disposition\", \"Content-Language\", \"Access-Control-Allow-Origin\",\"Access-Control-Allow-Methods\", \"Access-Control-Max-Age\", \"Access-Control-Expose-Headers\"或自定义头部。格式要求：长度1~100，以字母开头，可以使用字母、数字和短横杠。

        :return: The name of this HttpResponseHeader.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HttpResponseHeader.

        设置HTTP响应头参数。取值：\"Content-Disposition\", \"Content-Language\", \"Access-Control-Allow-Origin\",\"Access-Control-Allow-Methods\", \"Access-Control-Max-Age\", \"Access-Control-Expose-Headers\"或自定义头部。格式要求：长度1~100，以字母开头，可以使用字母、数字和短横杠。

        :param name: The name of this HttpResponseHeader.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this HttpResponseHeader.

        设置HTTP响应头参数的值。自定义HTTP响应头参数长度范围1~256，支持字母、数字和特定字符（.-_*#!%&+|^~'\"/:;,=@?）。

        :return: The value of this HttpResponseHeader.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this HttpResponseHeader.

        设置HTTP响应头参数的值。自定义HTTP响应头参数长度范围1~256，支持字母、数字和特定字符（.-_*#!%&+|^~'\"/:;,=@?）。

        :param value: The value of this HttpResponseHeader.
        :type value: str
        """
        self._value = value

    @property
    def action(self):
        """Gets the action of this HttpResponseHeader.

        设置http响应头操作类型，取值“set/delete”。set代表设置，delete代表删除。

        :return: The action of this HttpResponseHeader.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this HttpResponseHeader.

        设置http响应头操作类型，取值“set/delete”。set代表设置，delete代表删除。

        :param action: The action of this HttpResponseHeader.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, HttpResponseHeader):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
