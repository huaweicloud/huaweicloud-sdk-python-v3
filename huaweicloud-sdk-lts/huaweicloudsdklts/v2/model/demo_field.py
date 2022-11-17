# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DemoField:

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
        'index': 'int',
        'relation': 'str',
        'user_defined_name': 'str'
    }

    attribute_map = {
        'field_name': 'field_name',
        'content': 'content',
        'type': 'type',
        'is_analysis': 'is_analysis',
        'index': 'index',
        'relation': 'relation',
        'user_defined_name': 'user_defined_name'
    }

    def __init__(self, field_name=None, content=None, type=None, is_analysis=None, index=None, relation=None, user_defined_name=None):
        """DemoField

        The model defined in huaweicloud sdk

        :param field_name: 字段名称
        :type field_name: str
        :param content: 字段示例内容
        :type content: str
        :param type: 字段数据类型。 可选范围：string、long、float
        :type type: str
        :param is_analysis: 是否开启快速分析
        :type is_analysis: bool
        :param index: 手动正则及分隔符方式中字段序号
        :type index: int
        :param relation: 描叙多层级json中字段间的层级关系
        :type relation: str
        :param user_defined_name: json及nginx方式中字段自定义别名
        :type user_defined_name: str
        """
        
        

        self._field_name = None
        self._content = None
        self._type = None
        self._is_analysis = None
        self._index = None
        self._relation = None
        self._user_defined_name = None
        self.discriminator = None

        self.field_name = field_name
        if content is not None:
            self.content = content
        self.type = type
        if is_analysis is not None:
            self.is_analysis = is_analysis
        if index is not None:
            self.index = index
        if relation is not None:
            self.relation = relation
        if user_defined_name is not None:
            self.user_defined_name = user_defined_name

    @property
    def field_name(self):
        """Gets the field_name of this DemoField.

        字段名称

        :return: The field_name of this DemoField.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this DemoField.

        字段名称

        :param field_name: The field_name of this DemoField.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def content(self):
        """Gets the content of this DemoField.

        字段示例内容

        :return: The content of this DemoField.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this DemoField.

        字段示例内容

        :param content: The content of this DemoField.
        :type content: str
        """
        self._content = content

    @property
    def type(self):
        """Gets the type of this DemoField.

        字段数据类型。 可选范围：string、long、float

        :return: The type of this DemoField.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DemoField.

        字段数据类型。 可选范围：string、long、float

        :param type: The type of this DemoField.
        :type type: str
        """
        self._type = type

    @property
    def is_analysis(self):
        """Gets the is_analysis of this DemoField.

        是否开启快速分析

        :return: The is_analysis of this DemoField.
        :rtype: bool
        """
        return self._is_analysis

    @is_analysis.setter
    def is_analysis(self, is_analysis):
        """Sets the is_analysis of this DemoField.

        是否开启快速分析

        :param is_analysis: The is_analysis of this DemoField.
        :type is_analysis: bool
        """
        self._is_analysis = is_analysis

    @property
    def index(self):
        """Gets the index of this DemoField.

        手动正则及分隔符方式中字段序号

        :return: The index of this DemoField.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DemoField.

        手动正则及分隔符方式中字段序号

        :param index: The index of this DemoField.
        :type index: int
        """
        self._index = index

    @property
    def relation(self):
        """Gets the relation of this DemoField.

        描叙多层级json中字段间的层级关系

        :return: The relation of this DemoField.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this DemoField.

        描叙多层级json中字段间的层级关系

        :param relation: The relation of this DemoField.
        :type relation: str
        """
        self._relation = relation

    @property
    def user_defined_name(self):
        """Gets the user_defined_name of this DemoField.

        json及nginx方式中字段自定义别名

        :return: The user_defined_name of this DemoField.
        :rtype: str
        """
        return self._user_defined_name

    @user_defined_name.setter
    def user_defined_name(self, user_defined_name):
        """Sets the user_defined_name of this DemoField.

        json及nginx方式中字段自定义别名

        :param user_defined_name: The user_defined_name of this DemoField.
        :type user_defined_name: str
        """
        self._user_defined_name = user_defined_name

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
        if not isinstance(other, DemoField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
