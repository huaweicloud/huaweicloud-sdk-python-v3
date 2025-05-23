# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StoredQueryRequestBody:

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
        'description': 'str',
        'expression': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'expression': 'expression'
    }

    def __init__(self, name=None, type=None, description=None, expression=None):
        r"""StoredQueryRequestBody

        The model defined in huaweicloud sdk

        :param name: ResourceQL 名字
        :type name: str
        :param type: 自定义查询类型，枚举值为“account”和“aggregator”。若取值为“account”，表示单帐号的自定义查询语句；若取值为“aggregator”，表示聚合器的自定义查询语句。默认值为“account”。
        :type type: str
        :param description: ResourceQL 描述
        :type description: str
        :param expression: ResourceQL 表达式
        :type expression: str
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._expression = None
        self.discriminator = None

        self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        self.expression = expression

    @property
    def name(self):
        r"""Gets the name of this StoredQueryRequestBody.

        ResourceQL 名字

        :return: The name of this StoredQueryRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this StoredQueryRequestBody.

        ResourceQL 名字

        :param name: The name of this StoredQueryRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this StoredQueryRequestBody.

        自定义查询类型，枚举值为“account”和“aggregator”。若取值为“account”，表示单帐号的自定义查询语句；若取值为“aggregator”，表示聚合器的自定义查询语句。默认值为“account”。

        :return: The type of this StoredQueryRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this StoredQueryRequestBody.

        自定义查询类型，枚举值为“account”和“aggregator”。若取值为“account”，表示单帐号的自定义查询语句；若取值为“aggregator”，表示聚合器的自定义查询语句。默认值为“account”。

        :param type: The type of this StoredQueryRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this StoredQueryRequestBody.

        ResourceQL 描述

        :return: The description of this StoredQueryRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this StoredQueryRequestBody.

        ResourceQL 描述

        :param description: The description of this StoredQueryRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def expression(self):
        r"""Gets the expression of this StoredQueryRequestBody.

        ResourceQL 表达式

        :return: The expression of this StoredQueryRequestBody.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this StoredQueryRequestBody.

        ResourceQL 表达式

        :param expression: The expression of this StoredQueryRequestBody.
        :type expression: str
        """
        self._expression = expression

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
        if not isinstance(other, StoredQueryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
