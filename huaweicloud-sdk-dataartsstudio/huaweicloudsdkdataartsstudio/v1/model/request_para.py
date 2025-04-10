# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestPara:

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
        'position': 'str',
        'type': 'str',
        'description': 'str',
        'necessary': 'bool',
        'example_value': 'str',
        'default_value': 'str',
        'support_null': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'position': 'position',
        'type': 'type',
        'description': 'description',
        'necessary': 'necessary',
        'example_value': 'example_value',
        'default_value': 'default_value',
        'support_null': 'support_null'
    }

    def __init__(self, name=None, position=None, type=None, description=None, necessary=None, example_value=None, default_value=None, support_null=None):
        r"""RequestPara

        The model defined in huaweicloud sdk

        :param name: 参数名
        :type name: str
        :param position: 参数的位置
        :type position: str
        :param type: 参数的类型
        :type type: str
        :param description: 参数的描述
        :type description: str
        :param necessary: 参数是否必填
        :type necessary: bool
        :param example_value: 实例值
        :type example_value: str
        :param default_value: 默认值
        :type default_value: str
        :param support_null: 支持NULL值。
        :type support_null: bool
        """
        
        

        self._name = None
        self._position = None
        self._type = None
        self._description = None
        self._necessary = None
        self._example_value = None
        self._default_value = None
        self._support_null = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if necessary is not None:
            self.necessary = necessary
        if example_value is not None:
            self.example_value = example_value
        if default_value is not None:
            self.default_value = default_value
        if support_null is not None:
            self.support_null = support_null

    @property
    def name(self):
        r"""Gets the name of this RequestPara.

        参数名

        :return: The name of this RequestPara.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RequestPara.

        参数名

        :param name: The name of this RequestPara.
        :type name: str
        """
        self._name = name

    @property
    def position(self):
        r"""Gets the position of this RequestPara.

        参数的位置

        :return: The position of this RequestPara.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this RequestPara.

        参数的位置

        :param position: The position of this RequestPara.
        :type position: str
        """
        self._position = position

    @property
    def type(self):
        r"""Gets the type of this RequestPara.

        参数的类型

        :return: The type of this RequestPara.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this RequestPara.

        参数的类型

        :param type: The type of this RequestPara.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this RequestPara.

        参数的描述

        :return: The description of this RequestPara.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RequestPara.

        参数的描述

        :param description: The description of this RequestPara.
        :type description: str
        """
        self._description = description

    @property
    def necessary(self):
        r"""Gets the necessary of this RequestPara.

        参数是否必填

        :return: The necessary of this RequestPara.
        :rtype: bool
        """
        return self._necessary

    @necessary.setter
    def necessary(self, necessary):
        r"""Sets the necessary of this RequestPara.

        参数是否必填

        :param necessary: The necessary of this RequestPara.
        :type necessary: bool
        """
        self._necessary = necessary

    @property
    def example_value(self):
        r"""Gets the example_value of this RequestPara.

        实例值

        :return: The example_value of this RequestPara.
        :rtype: str
        """
        return self._example_value

    @example_value.setter
    def example_value(self, example_value):
        r"""Sets the example_value of this RequestPara.

        实例值

        :param example_value: The example_value of this RequestPara.
        :type example_value: str
        """
        self._example_value = example_value

    @property
    def default_value(self):
        r"""Gets the default_value of this RequestPara.

        默认值

        :return: The default_value of this RequestPara.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this RequestPara.

        默认值

        :param default_value: The default_value of this RequestPara.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def support_null(self):
        r"""Gets the support_null of this RequestPara.

        支持NULL值。

        :return: The support_null of this RequestPara.
        :rtype: bool
        """
        return self._support_null

    @support_null.setter
    def support_null(self, support_null):
        r"""Sets the support_null of this RequestPara.

        支持NULL值。

        :param support_null: The support_null of this RequestPara.
        :type support_null: bool
        """
        self._support_null = support_null

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
        if not isinstance(other, RequestPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
