# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyIndex:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'is_chinese_exist': 'bool',
        'properties': 'dict(str, KeyIndex)'
    }

    attribute_map = {
        'type': 'type',
        'is_chinese_exist': 'is_chinese_exist',
        'properties': 'properties'
    }

    def __init__(self, type=None, is_chinese_exist=None, properties=None):
        r"""KeyIndex

        The model defined in huaweicloud sdk

        :param type: 字段类型；text 全文索引字段、keyword 结构化字段、long Long、integer Integer、double Double、float Float、date 时间字段
        :type type: str
        :param is_chinese_exist: 是否包含中文
        :type is_chinese_exist: bool
        :param properties: 嵌套结构
        :type properties: dict(str, KeyIndex)
        """
        
        

        self._type = None
        self._is_chinese_exist = None
        self._properties = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if is_chinese_exist is not None:
            self.is_chinese_exist = is_chinese_exist
        if properties is not None:
            self.properties = properties

    @property
    def type(self):
        r"""Gets the type of this KeyIndex.

        字段类型；text 全文索引字段、keyword 结构化字段、long Long、integer Integer、double Double、float Float、date 时间字段

        :return: The type of this KeyIndex.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this KeyIndex.

        字段类型；text 全文索引字段、keyword 结构化字段、long Long、integer Integer、double Double、float Float、date 时间字段

        :param type: The type of this KeyIndex.
        :type type: str
        """
        self._type = type

    @property
    def is_chinese_exist(self):
        r"""Gets the is_chinese_exist of this KeyIndex.

        是否包含中文

        :return: The is_chinese_exist of this KeyIndex.
        :rtype: bool
        """
        return self._is_chinese_exist

    @is_chinese_exist.setter
    def is_chinese_exist(self, is_chinese_exist):
        r"""Sets the is_chinese_exist of this KeyIndex.

        是否包含中文

        :param is_chinese_exist: The is_chinese_exist of this KeyIndex.
        :type is_chinese_exist: bool
        """
        self._is_chinese_exist = is_chinese_exist

    @property
    def properties(self):
        r"""Gets the properties of this KeyIndex.

        嵌套结构

        :return: The properties of this KeyIndex.
        :rtype: dict(str, KeyIndex)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this KeyIndex.

        嵌套结构

        :param properties: The properties of this KeyIndex.
        :type properties: dict(str, KeyIndex)
        """
        self._properties = properties

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
        if not isinstance(other, KeyIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
