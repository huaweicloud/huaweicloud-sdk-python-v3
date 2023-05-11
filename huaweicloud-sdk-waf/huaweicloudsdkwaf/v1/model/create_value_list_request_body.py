# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateValueListRequestBody:

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
        'values': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'values': 'values',
        'description': 'description'
    }

    def __init__(self, name=None, type=None, values=None, description=None):
        """CreateValueListRequestBody

        The model defined in huaweicloud sdk

        :param name: 引用表名称，只能由数字、字母、中划线、下划线和英文句点组成，长度不能超过64
        :type name: str
        :param type: 引用表类型，参见枚举列表
        :type type: str
        :param values: 引用表的值
        :type values: list[str]
        :param description: 引用表描述，最长128字符
        :type description: str
        """
        
        

        self._name = None
        self._type = None
        self._values = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.values = values
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this CreateValueListRequestBody.

        引用表名称，只能由数字、字母、中划线、下划线和英文句点组成，长度不能超过64

        :return: The name of this CreateValueListRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateValueListRequestBody.

        引用表名称，只能由数字、字母、中划线、下划线和英文句点组成，长度不能超过64

        :param name: The name of this CreateValueListRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateValueListRequestBody.

        引用表类型，参见枚举列表

        :return: The type of this CreateValueListRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateValueListRequestBody.

        引用表类型，参见枚举列表

        :param type: The type of this CreateValueListRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def values(self):
        """Gets the values of this CreateValueListRequestBody.

        引用表的值

        :return: The values of this CreateValueListRequestBody.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this CreateValueListRequestBody.

        引用表的值

        :param values: The values of this CreateValueListRequestBody.
        :type values: list[str]
        """
        self._values = values

    @property
    def description(self):
        """Gets the description of this CreateValueListRequestBody.

        引用表描述，最长128字符

        :return: The description of this CreateValueListRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateValueListRequestBody.

        引用表描述，最长128字符

        :param description: The description of this CreateValueListRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateValueListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
