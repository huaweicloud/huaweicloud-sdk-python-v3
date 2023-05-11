# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructFieldInfoReturn:

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
        'type': 'str',
        'content': 'str',
        'is_analysis': 'bool',
        'index': 'int'
    }

    attribute_map = {
        'field_name': 'fieldName',
        'type': 'type',
        'content': 'content',
        'is_analysis': 'isAnalysis',
        'index': 'index'
    }

    def __init__(self, field_name=None, type=None, content=None, is_analysis=None, index=None):
        """StructFieldInfoReturn

        The model defined in huaweicloud sdk

        :param field_name: 字段名称
        :type field_name: str
        :param type: 字段数据类型
        :type type: str
        :param content: 字段内容
        :type content: str
        :param is_analysis: 结构化方式
        :type is_analysis: bool
        :param index: 序号
        :type index: int
        """
        
        

        self._field_name = None
        self._type = None
        self._content = None
        self._is_analysis = None
        self._index = None
        self.discriminator = None

        if field_name is not None:
            self.field_name = field_name
        if type is not None:
            self.type = type
        if content is not None:
            self.content = content
        if is_analysis is not None:
            self.is_analysis = is_analysis
        if index is not None:
            self.index = index

    @property
    def field_name(self):
        """Gets the field_name of this StructFieldInfoReturn.

        字段名称

        :return: The field_name of this StructFieldInfoReturn.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this StructFieldInfoReturn.

        字段名称

        :param field_name: The field_name of this StructFieldInfoReturn.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def type(self):
        """Gets the type of this StructFieldInfoReturn.

        字段数据类型

        :return: The type of this StructFieldInfoReturn.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StructFieldInfoReturn.

        字段数据类型

        :param type: The type of this StructFieldInfoReturn.
        :type type: str
        """
        self._type = type

    @property
    def content(self):
        """Gets the content of this StructFieldInfoReturn.

        字段内容

        :return: The content of this StructFieldInfoReturn.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this StructFieldInfoReturn.

        字段内容

        :param content: The content of this StructFieldInfoReturn.
        :type content: str
        """
        self._content = content

    @property
    def is_analysis(self):
        """Gets the is_analysis of this StructFieldInfoReturn.

        结构化方式

        :return: The is_analysis of this StructFieldInfoReturn.
        :rtype: bool
        """
        return self._is_analysis

    @is_analysis.setter
    def is_analysis(self, is_analysis):
        """Sets the is_analysis of this StructFieldInfoReturn.

        结构化方式

        :param is_analysis: The is_analysis of this StructFieldInfoReturn.
        :type is_analysis: bool
        """
        self._is_analysis = is_analysis

    @property
    def index(self):
        """Gets the index of this StructFieldInfoReturn.

        序号

        :return: The index of this StructFieldInfoReturn.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this StructFieldInfoReturn.

        序号

        :param index: The index of this StructFieldInfoReturn.
        :type index: int
        """
        self._index = index

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
        if not isinstance(other, StructFieldInfoReturn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
