# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigsMap:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'name': 'str'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name'
    }

    def __init__(self, key=None, name=None):
        """ConfigsMap

        The model defined in huaweicloud sdk

        :param key: 配置项的名称，以英文字母或中划线开头，由英文字母、数字、点号、中划线和下划线组成，长度1到63个字符。
        :type key: str
        :param name: 配置项的属性名，以英文小写字母开头，由中文字符，英文字母，数字，下划线和中划线组成，不能以中划线结尾，长度4-64位。
        :type name: str
        """
        
        

        self._key = None
        self._name = None
        self.discriminator = None

        self.key = key
        self.name = name

    @property
    def key(self):
        """Gets the key of this ConfigsMap.

        配置项的名称，以英文字母或中划线开头，由英文字母、数字、点号、中划线和下划线组成，长度1到63个字符。

        :return: The key of this ConfigsMap.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ConfigsMap.

        配置项的名称，以英文字母或中划线开头，由英文字母、数字、点号、中划线和下划线组成，长度1到63个字符。

        :param key: The key of this ConfigsMap.
        :type key: str
        """
        self._key = key

    @property
    def name(self):
        """Gets the name of this ConfigsMap.

        配置项的属性名，以英文小写字母开头，由中文字符，英文字母，数字，下划线和中划线组成，不能以中划线结尾，长度4-64位。

        :return: The name of this ConfigsMap.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConfigsMap.

        配置项的属性名，以英文小写字母开头，由中文字符，英文字母，数字，下划线和中划线组成，不能以中划线结尾，长度4-64位。

        :param name: The name of this ConfigsMap.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ConfigsMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
