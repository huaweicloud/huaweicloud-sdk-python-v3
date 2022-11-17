# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Columns:

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
        'type': 'str',
        'primary_key': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'primary_key': 'primary_key'
    }

    def __init__(self, name=None, type=None, primary_key=None):
        """Columns

        The model defined in huaweicloud sdk

        :param name: 数据的字段名称，最大支持长度256
        :type name: str
        :param type: 数据的字段类型
        :type type: str
        :param primary_key: 标记该字段是否为主键。true为主键，表示用来定位水印位置；false为非主键，将在该列嵌入/提取水印内容。字段类型列表中可同时包含多个为true或为false的字段
        :type primary_key: bool
        """
        
        

        self._name = None
        self._type = None
        self._primary_key = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.primary_key = primary_key

    @property
    def name(self):
        """Gets the name of this Columns.

        数据的字段名称，最大支持长度256

        :return: The name of this Columns.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Columns.

        数据的字段名称，最大支持长度256

        :param name: The name of this Columns.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this Columns.

        数据的字段类型

        :return: The type of this Columns.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Columns.

        数据的字段类型

        :param type: The type of this Columns.
        :type type: str
        """
        self._type = type

    @property
    def primary_key(self):
        """Gets the primary_key of this Columns.

        标记该字段是否为主键。true为主键，表示用来定位水印位置；false为非主键，将在该列嵌入/提取水印内容。字段类型列表中可同时包含多个为true或为false的字段

        :return: The primary_key of this Columns.
        :rtype: bool
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this Columns.

        标记该字段是否为主键。true为主键，表示用来定位水印位置；false为非主键，将在该列嵌入/提取水印内容。字段类型列表中可同时包含多个为true或为false的字段

        :param primary_key: The primary_key of this Columns.
        :type primary_key: bool
        """
        self._primary_key = primary_key

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
        if not isinstance(other, Columns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
