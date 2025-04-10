# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StructFieldInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_analysis': 'bool',
        'content': 'str',
        'field_name': 'str',
        'type': 'str',
        'user_defined_name': 'str',
        'index': 'int'
    }

    attribute_map = {
        'is_analysis': 'isAnalysis',
        'content': 'content',
        'field_name': 'fieldName',
        'type': 'type',
        'user_defined_name': 'userDefinedName',
        'index': 'index'
    }

    def __init__(self, is_analysis=None, content=None, field_name=None, type=None, user_defined_name=None, index=None):
        r"""StructFieldInfo

        The model defined in huaweicloud sdk

        :param is_analysis: 结构化方式
        :type is_analysis: bool
        :param content: 字段内容
        :type content: str
        :param field_name: 字段名称
        :type field_name: str
        :param type: 字段数据类型,例：string，long，float
        :type type: str
        :param user_defined_name: 自定义别名(json方式中按需添加)
        :type user_defined_name: str
        :param index: 序号
        :type index: int
        """
        
        

        self._is_analysis = None
        self._content = None
        self._field_name = None
        self._type = None
        self._user_defined_name = None
        self._index = None
        self.discriminator = None

        if is_analysis is not None:
            self.is_analysis = is_analysis
        if content is not None:
            self.content = content
        if field_name is not None:
            self.field_name = field_name
        self.type = type
        if user_defined_name is not None:
            self.user_defined_name = user_defined_name
        if index is not None:
            self.index = index

    @property
    def is_analysis(self):
        r"""Gets the is_analysis of this StructFieldInfo.

        结构化方式

        :return: The is_analysis of this StructFieldInfo.
        :rtype: bool
        """
        return self._is_analysis

    @is_analysis.setter
    def is_analysis(self, is_analysis):
        r"""Sets the is_analysis of this StructFieldInfo.

        结构化方式

        :param is_analysis: The is_analysis of this StructFieldInfo.
        :type is_analysis: bool
        """
        self._is_analysis = is_analysis

    @property
    def content(self):
        r"""Gets the content of this StructFieldInfo.

        字段内容

        :return: The content of this StructFieldInfo.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this StructFieldInfo.

        字段内容

        :param content: The content of this StructFieldInfo.
        :type content: str
        """
        self._content = content

    @property
    def field_name(self):
        r"""Gets the field_name of this StructFieldInfo.

        字段名称

        :return: The field_name of this StructFieldInfo.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this StructFieldInfo.

        字段名称

        :param field_name: The field_name of this StructFieldInfo.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def type(self):
        r"""Gets the type of this StructFieldInfo.

        字段数据类型,例：string，long，float

        :return: The type of this StructFieldInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StructFieldInfo.

        字段数据类型,例：string，long，float

        :param type: The type of this StructFieldInfo.
        :type type: str
        """
        self._type = type

    @property
    def user_defined_name(self):
        r"""Gets the user_defined_name of this StructFieldInfo.

        自定义别名(json方式中按需添加)

        :return: The user_defined_name of this StructFieldInfo.
        :rtype: str
        """
        return self._user_defined_name

    @user_defined_name.setter
    def user_defined_name(self, user_defined_name):
        r"""Sets the user_defined_name of this StructFieldInfo.

        自定义别名(json方式中按需添加)

        :param user_defined_name: The user_defined_name of this StructFieldInfo.
        :type user_defined_name: str
        """
        self._user_defined_name = user_defined_name

    @property
    def index(self):
        r"""Gets the index of this StructFieldInfo.

        序号

        :return: The index of this StructFieldInfo.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this StructFieldInfo.

        序号

        :param index: The index of this StructFieldInfo.
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
        if not isinstance(other, StructFieldInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
