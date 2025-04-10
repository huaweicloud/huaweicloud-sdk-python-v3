# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagFieldNew:

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
        'content': 'str',
        'type': 'str',
        'is_analysis': 'bool',
        'index': 'int'
    }

    attribute_map = {
        'field_name': 'field_name',
        'content': 'content',
        'type': 'type',
        'is_analysis': 'is_analysis',
        'index': 'index'
    }

    def __init__(self, field_name=None, content=None, type=None, is_analysis=None, index=None):
        r"""TagFieldNew

        The model defined in huaweicloud sdk

        :param field_name: 字段名称
        :type field_name: str
        :param content: 字段示例内容
        :type content: str
        :param type: 字段数据类型。 可选范围：string、long、float
        :type type: str
        :param is_analysis: 是否开启快速分析
        :type is_analysis: bool
        :param index: 序号，从0开始
        :type index: int
        """
        
        

        self._field_name = None
        self._content = None
        self._type = None
        self._is_analysis = None
        self._index = None
        self.discriminator = None

        self.field_name = field_name
        if content is not None:
            self.content = content
        self.type = type
        if is_analysis is not None:
            self.is_analysis = is_analysis
        if index is not None:
            self.index = index

    @property
    def field_name(self):
        r"""Gets the field_name of this TagFieldNew.

        字段名称

        :return: The field_name of this TagFieldNew.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this TagFieldNew.

        字段名称

        :param field_name: The field_name of this TagFieldNew.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def content(self):
        r"""Gets the content of this TagFieldNew.

        字段示例内容

        :return: The content of this TagFieldNew.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this TagFieldNew.

        字段示例内容

        :param content: The content of this TagFieldNew.
        :type content: str
        """
        self._content = content

    @property
    def type(self):
        r"""Gets the type of this TagFieldNew.

        字段数据类型。 可选范围：string、long、float

        :return: The type of this TagFieldNew.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TagFieldNew.

        字段数据类型。 可选范围：string、long、float

        :param type: The type of this TagFieldNew.
        :type type: str
        """
        self._type = type

    @property
    def is_analysis(self):
        r"""Gets the is_analysis of this TagFieldNew.

        是否开启快速分析

        :return: The is_analysis of this TagFieldNew.
        :rtype: bool
        """
        return self._is_analysis

    @is_analysis.setter
    def is_analysis(self, is_analysis):
        r"""Sets the is_analysis of this TagFieldNew.

        是否开启快速分析

        :param is_analysis: The is_analysis of this TagFieldNew.
        :type is_analysis: bool
        """
        self._is_analysis = is_analysis

    @property
    def index(self):
        r"""Gets the index of this TagFieldNew.

        序号，从0开始

        :return: The index of this TagFieldNew.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this TagFieldNew.

        序号，从0开始

        :param index: The index of this TagFieldNew.
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
        if not isinstance(other, TagFieldNew):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
