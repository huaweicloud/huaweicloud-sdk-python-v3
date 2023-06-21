# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AimPersonalTemplateParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'int',
        'name': 'str',
        'example': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'example': 'example'
    }

    def __init__(self, type=None, name=None, example=None):
        """AimPersonalTemplateParam

        The model defined in huaweicloud sdk

        :param type: 动态参数类型。1：表示文本类型。 
        :type type: int
        :param name: 动态参数名称。示例：${param1}。
        :type name: str
        :param example: 参数示例，动态参数对应的示例，不能大于100个字符。
        :type example: str
        """
        
        

        self._type = None
        self._name = None
        self._example = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.example = example

    @property
    def type(self):
        """Gets the type of this AimPersonalTemplateParam.

        动态参数类型。1：表示文本类型。 

        :return: The type of this AimPersonalTemplateParam.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AimPersonalTemplateParam.

        动态参数类型。1：表示文本类型。 

        :param type: The type of this AimPersonalTemplateParam.
        :type type: int
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this AimPersonalTemplateParam.

        动态参数名称。示例：${param1}。

        :return: The name of this AimPersonalTemplateParam.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AimPersonalTemplateParam.

        动态参数名称。示例：${param1}。

        :param name: The name of this AimPersonalTemplateParam.
        :type name: str
        """
        self._name = name

    @property
    def example(self):
        """Gets the example of this AimPersonalTemplateParam.

        参数示例，动态参数对应的示例，不能大于100个字符。

        :return: The example of this AimPersonalTemplateParam.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this AimPersonalTemplateParam.

        参数示例，动态参数对应的示例，不能大于100个字符。

        :param example: The example of this AimPersonalTemplateParam.
        :type example: str
        """
        self._example = example

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
        if not isinstance(other, AimPersonalTemplateParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
