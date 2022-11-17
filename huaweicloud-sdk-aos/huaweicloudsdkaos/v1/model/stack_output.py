# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StackOutput:

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
        'type': 'str',
        'value': 'str',
        'sensitive': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'value': 'value',
        'sensitive': 'sensitive'
    }

    def __init__(self, name=None, description=None, type=None, value=None, sensitive=None):
        """StackOutput

        The model defined in huaweicloud sdk

        :param name: 堆栈输出的name，由用户自己在模板中定义
        :type name: str
        :param description: 描述
        :type description: str
        :param type: 输出的类型
        :type type: str
        :param value: 输出的值(json字符串)
        :type value: str
        :param sensitive: 是否为敏感信息
        :type sensitive: bool
        """
        
        

        self._name = None
        self._description = None
        self._type = None
        self._value = None
        self._sensitive = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if sensitive is not None:
            self.sensitive = sensitive

    @property
    def name(self):
        """Gets the name of this StackOutput.

        堆栈输出的name，由用户自己在模板中定义

        :return: The name of this StackOutput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StackOutput.

        堆栈输出的name，由用户自己在模板中定义

        :param name: The name of this StackOutput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this StackOutput.

        描述

        :return: The description of this StackOutput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StackOutput.

        描述

        :param description: The description of this StackOutput.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this StackOutput.

        输出的类型

        :return: The type of this StackOutput.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StackOutput.

        输出的类型

        :param type: The type of this StackOutput.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this StackOutput.

        输出的值(json字符串)

        :return: The value of this StackOutput.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this StackOutput.

        输出的值(json字符串)

        :param value: The value of this StackOutput.
        :type value: str
        """
        self._value = value

    @property
    def sensitive(self):
        """Gets the sensitive of this StackOutput.

        是否为敏感信息

        :return: The sensitive of this StackOutput.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """Sets the sensitive of this StackOutput.

        是否为敏感信息

        :param sensitive: The sensitive of this StackOutput.
        :type sensitive: bool
        """
        self._sensitive = sensitive

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
        if not isinstance(other, StackOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
