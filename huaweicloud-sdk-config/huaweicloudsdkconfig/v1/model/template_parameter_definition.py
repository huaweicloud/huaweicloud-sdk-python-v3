# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateParameterDefinition:

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
        'description': 'str',
        'default_value': 'object',
        'allowed_values': 'list[object]',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'default_value': 'default_value',
        'allowed_values': 'allowed_values',
        'type': 'type'
    }

    def __init__(self, name=None, description=None, default_value=None, allowed_values=None, type=None):
        """TemplateParameterDefinition

        The model defined in huaweicloud sdk

        :param name: 预定义合规包模板参数名字。
        :type name: str
        :param description: 预定义合规包模板参数描述。
        :type description: str
        :param default_value: 预定义合规包模板参数默认值。
        :type default_value: object
        :param allowed_values: 预定义合规包模板参数允许值列表
        :type allowed_values: list[object]
        :param type: 预定义合规包模板参数类型。
        :type type: str
        """
        
        

        self._name = None
        self._description = None
        self._default_value = None
        self._allowed_values = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if default_value is not None:
            self.default_value = default_value
        if allowed_values is not None:
            self.allowed_values = allowed_values
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this TemplateParameterDefinition.

        预定义合规包模板参数名字。

        :return: The name of this TemplateParameterDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateParameterDefinition.

        预定义合规包模板参数名字。

        :param name: The name of this TemplateParameterDefinition.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this TemplateParameterDefinition.

        预定义合规包模板参数描述。

        :return: The description of this TemplateParameterDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateParameterDefinition.

        预定义合规包模板参数描述。

        :param description: The description of this TemplateParameterDefinition.
        :type description: str
        """
        self._description = description

    @property
    def default_value(self):
        """Gets the default_value of this TemplateParameterDefinition.

        预定义合规包模板参数默认值。

        :return: The default_value of this TemplateParameterDefinition.
        :rtype: object
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this TemplateParameterDefinition.

        预定义合规包模板参数默认值。

        :param default_value: The default_value of this TemplateParameterDefinition.
        :type default_value: object
        """
        self._default_value = default_value

    @property
    def allowed_values(self):
        """Gets the allowed_values of this TemplateParameterDefinition.

        预定义合规包模板参数允许值列表

        :return: The allowed_values of this TemplateParameterDefinition.
        :rtype: list[object]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this TemplateParameterDefinition.

        预定义合规包模板参数允许值列表

        :param allowed_values: The allowed_values of this TemplateParameterDefinition.
        :type allowed_values: list[object]
        """
        self._allowed_values = allowed_values

    @property
    def type(self):
        """Gets the type of this TemplateParameterDefinition.

        预定义合规包模板参数类型。

        :return: The type of this TemplateParameterDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateParameterDefinition.

        预定义合规包模板参数类型。

        :param type: The type of this TemplateParameterDefinition.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, TemplateParameterDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
