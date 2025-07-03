# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectFilterV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operator': 'str',
        'field': 'str',
        'group': 'str',
        'name': 'str',
        'match_type': 'str',
        'priority_type': 'str',
        'values': 'list[object]'
    }

    attribute_map = {
        'operator': 'operator',
        'field': 'field',
        'group': 'group',
        'name': 'name',
        'match_type': 'match_type',
        'priority_type': 'priority_type',
        'values': 'values'
    }

    def __init__(self, operator=None, field=None, group=None, name=None, match_type=None, priority_type=None, values=None):
        r"""ObjectFilterV2

        The model defined in huaweicloud sdk

        :param operator: 操作符 in/like/startwith/endwith/&#x3D;/!&#x3D;/&gt;/&lt;等
        :type operator: str
        :param field: 字段名称
        :type field: str
        :param group: 分组
        :type group: str
        :param name: 条件名称
        :type name: str
        :param match_type: 匹配方式
        :type match_type: str
        :param priority_type: 优先级处理方式
        :type priority_type: str
        :param values: 搜索值
        :type values: list[object]
        """
        
        

        self._operator = None
        self._field = None
        self._group = None
        self._name = None
        self._match_type = None
        self._priority_type = None
        self._values = None
        self.discriminator = None

        self.operator = operator
        self.field = field
        if group is not None:
            self.group = group
        if name is not None:
            self.name = name
        if match_type is not None:
            self.match_type = match_type
        if priority_type is not None:
            self.priority_type = priority_type
        self.values = values

    @property
    def operator(self):
        r"""Gets the operator of this ObjectFilterV2.

        操作符 in/like/startwith/endwith/=/!=/>/<等

        :return: The operator of this ObjectFilterV2.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ObjectFilterV2.

        操作符 in/like/startwith/endwith/=/!=/>/<等

        :param operator: The operator of this ObjectFilterV2.
        :type operator: str
        """
        self._operator = operator

    @property
    def field(self):
        r"""Gets the field of this ObjectFilterV2.

        字段名称

        :return: The field of this ObjectFilterV2.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this ObjectFilterV2.

        字段名称

        :param field: The field of this ObjectFilterV2.
        :type field: str
        """
        self._field = field

    @property
    def group(self):
        r"""Gets the group of this ObjectFilterV2.

        分组

        :return: The group of this ObjectFilterV2.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this ObjectFilterV2.

        分组

        :param group: The group of this ObjectFilterV2.
        :type group: str
        """
        self._group = group

    @property
    def name(self):
        r"""Gets the name of this ObjectFilterV2.

        条件名称

        :return: The name of this ObjectFilterV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ObjectFilterV2.

        条件名称

        :param name: The name of this ObjectFilterV2.
        :type name: str
        """
        self._name = name

    @property
    def match_type(self):
        r"""Gets the match_type of this ObjectFilterV2.

        匹配方式

        :return: The match_type of this ObjectFilterV2.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        r"""Sets the match_type of this ObjectFilterV2.

        匹配方式

        :param match_type: The match_type of this ObjectFilterV2.
        :type match_type: str
        """
        self._match_type = match_type

    @property
    def priority_type(self):
        r"""Gets the priority_type of this ObjectFilterV2.

        优先级处理方式

        :return: The priority_type of this ObjectFilterV2.
        :rtype: str
        """
        return self._priority_type

    @priority_type.setter
    def priority_type(self, priority_type):
        r"""Sets the priority_type of this ObjectFilterV2.

        优先级处理方式

        :param priority_type: The priority_type of this ObjectFilterV2.
        :type priority_type: str
        """
        self._priority_type = priority_type

    @property
    def values(self):
        r"""Gets the values of this ObjectFilterV2.

        搜索值

        :return: The values of this ObjectFilterV2.
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ObjectFilterV2.

        搜索值

        :param values: The values of this ObjectFilterV2.
        :type values: list[object]
        """
        self._values = values

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
        if not isinstance(other, ObjectFilterV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
