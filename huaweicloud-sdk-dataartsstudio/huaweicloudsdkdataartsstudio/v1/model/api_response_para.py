# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiResponsePara:

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
        'field': 'str',
        'type': 'str',
        'description': 'str',
        'example_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'field': 'field',
        'type': 'type',
        'description': 'description',
        'example_value': 'example_value'
    }

    def __init__(self, name=None, field=None, type=None, description=None, example_value=None):
        r"""ApiResponsePara

        The model defined in huaweicloud sdk

        :param name: 参数名
        :type name: str
        :param field: 绑定的表字段
        :type field: str
        :param type: 参数类型
        :type type: str
        :param description: 参数描述
        :type description: str
        :param example_value: 参数示例值
        :type example_value: str
        """
        
        

        self._name = None
        self._field = None
        self._type = None
        self._description = None
        self._example_value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if field is not None:
            self.field = field
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if example_value is not None:
            self.example_value = example_value

    @property
    def name(self):
        r"""Gets the name of this ApiResponsePara.

        参数名

        :return: The name of this ApiResponsePara.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApiResponsePara.

        参数名

        :param name: The name of this ApiResponsePara.
        :type name: str
        """
        self._name = name

    @property
    def field(self):
        r"""Gets the field of this ApiResponsePara.

        绑定的表字段

        :return: The field of this ApiResponsePara.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this ApiResponsePara.

        绑定的表字段

        :param field: The field of this ApiResponsePara.
        :type field: str
        """
        self._field = field

    @property
    def type(self):
        r"""Gets the type of this ApiResponsePara.

        参数类型

        :return: The type of this ApiResponsePara.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ApiResponsePara.

        参数类型

        :param type: The type of this ApiResponsePara.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this ApiResponsePara.

        参数描述

        :return: The description of this ApiResponsePara.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ApiResponsePara.

        参数描述

        :param description: The description of this ApiResponsePara.
        :type description: str
        """
        self._description = description

    @property
    def example_value(self):
        r"""Gets the example_value of this ApiResponsePara.

        参数示例值

        :return: The example_value of this ApiResponsePara.
        :rtype: str
        """
        return self._example_value

    @example_value.setter
    def example_value(self, example_value):
        r"""Sets the example_value of this ApiResponsePara.

        参数示例值

        :param example_value: The example_value of this ApiResponsePara.
        :type example_value: str
        """
        self._example_value = example_value

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
        if not isinstance(other, ApiResponsePara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
