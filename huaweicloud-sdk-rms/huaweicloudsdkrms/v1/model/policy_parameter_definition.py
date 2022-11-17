# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyParameterDefinition:

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
        'allowed_values': 'list[object]',
        'default_value': 'str',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'allowed_values': 'allowed_values',
        'default_value': 'default_value',
        'type': 'type'
    }

    def __init__(self, name=None, description=None, allowed_values=None, default_value=None, type=None):
        """PolicyParameterDefinition

        The model defined in huaweicloud sdk

        :param name: 策略参数名字
        :type name: str
        :param description: 策略参数描述
        :type description: str
        :param allowed_values: 策略参数允许值列表
        :type allowed_values: list[object]
        :param default_value: 策略参数默认值
        :type default_value: str
        :param type: 策略参数类型
        :type type: str
        """
        
        

        self._name = None
        self._description = None
        self._allowed_values = None
        self._default_value = None
        self._type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if allowed_values is not None:
            self.allowed_values = allowed_values
        if default_value is not None:
            self.default_value = default_value
        if type is not None:
            self.type = type

    @property
    def name(self):
        """Gets the name of this PolicyParameterDefinition.

        策略参数名字

        :return: The name of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PolicyParameterDefinition.

        策略参数名字

        :param name: The name of this PolicyParameterDefinition.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PolicyParameterDefinition.

        策略参数描述

        :return: The description of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyParameterDefinition.

        策略参数描述

        :param description: The description of this PolicyParameterDefinition.
        :type description: str
        """
        self._description = description

    @property
    def allowed_values(self):
        """Gets the allowed_values of this PolicyParameterDefinition.

        策略参数允许值列表

        :return: The allowed_values of this PolicyParameterDefinition.
        :rtype: list[object]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """Sets the allowed_values of this PolicyParameterDefinition.

        策略参数允许值列表

        :param allowed_values: The allowed_values of this PolicyParameterDefinition.
        :type allowed_values: list[object]
        """
        self._allowed_values = allowed_values

    @property
    def default_value(self):
        """Gets the default_value of this PolicyParameterDefinition.

        策略参数默认值

        :return: The default_value of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this PolicyParameterDefinition.

        策略参数默认值

        :param default_value: The default_value of this PolicyParameterDefinition.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def type(self):
        """Gets the type of this PolicyParameterDefinition.

        策略参数类型

        :return: The type of this PolicyParameterDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyParameterDefinition.

        策略参数类型

        :param type: The type of this PolicyParameterDefinition.
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
        if not isinstance(other, PolicyParameterDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
