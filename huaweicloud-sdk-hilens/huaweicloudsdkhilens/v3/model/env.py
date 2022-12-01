# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Env:

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
        'value_from': 'ValueFrom',
        'field_path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'value_from': 'value_from',
        'field_path': 'field_path'
    }

    def __init__(self, name=None, value=None, value_from=None, field_path=None):
        """Env

        The model defined in huaweicloud sdk

        :param name: 环境变量的key，由大小写字母或下划线开头，由数字、大小写字母、下划线组成，最大长度2048个字符，不允许重复
        :type name: str
        :param value: 环境变量的value，最大长度20480个字符。value、value_from和field_path必须三选一使用
        :type value: str
        :param value_from: 
        :type value_from: :class:`huaweicloudsdkhilens.v3.ValueFrom`
        :param field_path: 该参数目前只支持赋值\&quot;status.hostIP\&quot;，即引用边缘节点的IP地址作为环境变量。value、value_from和field_path必须三选一使用
        :type field_path: str
        """
        
        

        self._name = None
        self._value = None
        self._value_from = None
        self._field_path = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value
        if value_from is not None:
            self.value_from = value_from
        if field_path is not None:
            self.field_path = field_path

    @property
    def name(self):
        """Gets the name of this Env.

        环境变量的key，由大小写字母或下划线开头，由数字、大小写字母、下划线组成，最大长度2048个字符，不允许重复

        :return: The name of this Env.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Env.

        环境变量的key，由大小写字母或下划线开头，由数字、大小写字母、下划线组成，最大长度2048个字符，不允许重复

        :param name: The name of this Env.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this Env.

        环境变量的value，最大长度20480个字符。value、value_from和field_path必须三选一使用

        :return: The value of this Env.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Env.

        环境变量的value，最大长度20480个字符。value、value_from和field_path必须三选一使用

        :param value: The value of this Env.
        :type value: str
        """
        self._value = value

    @property
    def value_from(self):
        """Gets the value_from of this Env.

        :return: The value_from of this Env.
        :rtype: :class:`huaweicloudsdkhilens.v3.ValueFrom`
        """
        return self._value_from

    @value_from.setter
    def value_from(self, value_from):
        """Sets the value_from of this Env.

        :param value_from: The value_from of this Env.
        :type value_from: :class:`huaweicloudsdkhilens.v3.ValueFrom`
        """
        self._value_from = value_from

    @property
    def field_path(self):
        """Gets the field_path of this Env.

        该参数目前只支持赋值\"status.hostIP\"，即引用边缘节点的IP地址作为环境变量。value、value_from和field_path必须三选一使用

        :return: The field_path of this Env.
        :rtype: str
        """
        return self._field_path

    @field_path.setter
    def field_path(self, field_path):
        """Sets the field_path of this Env.

        该参数目前只支持赋值\"status.hostIP\"，即引用边缘节点的IP地址作为环境变量。value、value_from和field_path必须三选一使用

        :param field_path: The field_path of this Env.
        :type field_path: str
        """
        self._field_path = field_path

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
        if not isinstance(other, Env):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
