# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NextflowParamsDto:

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
        'value': 'str',
        'type': 'str',
        'description': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'type': 'type',
        'description': 'description',
        'required': 'required'
    }

    def __init__(self, name=None, value=None, type=None, description=None, required=None):
        """NextflowParamsDto

        The model defined in huaweicloud sdk

        :param name: 参数名
        :type name: str
        :param value: 参数值
        :type value: str
        :param type: 参数类型,取值[Other|File|Directory]
        :type type: str
        :param description: 参数描述。取值范围：[0-255]
        :type description: str
        :param required: 参数是否必填
        :type required: bool
        """
        
        

        self._name = None
        self._value = None
        self._type = None
        self._description = None
        self._required = None
        self.discriminator = None

        self.name = name
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if required is not None:
            self.required = required

    @property
    def name(self):
        """Gets the name of this NextflowParamsDto.

        参数名

        :return: The name of this NextflowParamsDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NextflowParamsDto.

        参数名

        :param name: The name of this NextflowParamsDto.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this NextflowParamsDto.

        参数值

        :return: The value of this NextflowParamsDto.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NextflowParamsDto.

        参数值

        :param value: The value of this NextflowParamsDto.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        """Gets the type of this NextflowParamsDto.

        参数类型,取值[Other|File|Directory]

        :return: The type of this NextflowParamsDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NextflowParamsDto.

        参数类型,取值[Other|File|Directory]

        :param type: The type of this NextflowParamsDto.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this NextflowParamsDto.

        参数描述。取值范围：[0-255]

        :return: The description of this NextflowParamsDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NextflowParamsDto.

        参数描述。取值范围：[0-255]

        :param description: The description of this NextflowParamsDto.
        :type description: str
        """
        self._description = description

    @property
    def required(self):
        """Gets the required of this NextflowParamsDto.

        参数是否必填

        :return: The required of this NextflowParamsDto.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this NextflowParamsDto.

        参数是否必填

        :param required: The required of this NextflowParamsDto.
        :type required: bool
        """
        self._required = required

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
        if not isinstance(other, NextflowParamsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
