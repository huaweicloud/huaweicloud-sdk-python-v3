# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackendConstant:

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
        'position': 'str',
        'description': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'position': 'position',
        'description': 'description',
        'value': 'value'
    }

    def __init__(self, name=None, type=None, position=None, description=None, value=None):
        r"""BackendConstant

        The model defined in huaweicloud sdk

        :param name: 常量参数名
        :type name: str
        :param type: 常量参数类型
        :type type: str
        :param position: 常量参数位置
        :type position: str
        :param description: 常量参数描述
        :type description: str
        :param value: 常量参数值
        :type value: str
        """
        
        

        self._name = None
        self._type = None
        self._position = None
        self._description = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if position is not None:
            self.position = position
        if description is not None:
            self.description = description
        if value is not None:
            self.value = value

    @property
    def name(self):
        r"""Gets the name of this BackendConstant.

        常量参数名

        :return: The name of this BackendConstant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BackendConstant.

        常量参数名

        :param name: The name of this BackendConstant.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this BackendConstant.

        常量参数类型

        :return: The type of this BackendConstant.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BackendConstant.

        常量参数类型

        :param type: The type of this BackendConstant.
        :type type: str
        """
        self._type = type

    @property
    def position(self):
        r"""Gets the position of this BackendConstant.

        常量参数位置

        :return: The position of this BackendConstant.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this BackendConstant.

        常量参数位置

        :param position: The position of this BackendConstant.
        :type position: str
        """
        self._position = position

    @property
    def description(self):
        r"""Gets the description of this BackendConstant.

        常量参数描述

        :return: The description of this BackendConstant.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BackendConstant.

        常量参数描述

        :param description: The description of this BackendConstant.
        :type description: str
        """
        self._description = description

    @property
    def value(self):
        r"""Gets the value of this BackendConstant.

        常量参数值

        :return: The value of this BackendConstant.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this BackendConstant.

        常量参数值

        :param value: The value of this BackendConstant.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, BackendConstant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
