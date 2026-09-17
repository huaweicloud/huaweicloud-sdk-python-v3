# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParameterValuesInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restart_required': 'bool',
        'readonly': 'bool',
        'name': 'str',
        'value': 'str',
        'type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'restart_required': 'restart_required',
        'readonly': 'readonly',
        'name': 'name',
        'value': 'value',
        'type': 'type',
        'description': 'description'
    }

    def __init__(self, restart_required=None, readonly=None, name=None, value=None, type=None, description=None):
        r"""ParameterValuesInfo

        The model defined in huaweicloud sdk

        :param restart_required: 是否需要重启
        :type restart_required: bool
        :param readonly: 是否只读
        :type readonly: bool
        :param name: 参数名
        :type name: str
        :param value: 参数值
        :type value: str
        :param type: 参数类型
        :type type: str
        :param description: 参数描述
        :type description: str
        """
        
        

        self._restart_required = None
        self._readonly = None
        self._name = None
        self._value = None
        self._type = None
        self._description = None
        self.discriminator = None

        if restart_required is not None:
            self.restart_required = restart_required
        if readonly is not None:
            self.readonly = readonly
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description

    @property
    def restart_required(self):
        r"""Gets the restart_required of this ParameterValuesInfo.

        是否需要重启

        :return: The restart_required of this ParameterValuesInfo.
        :rtype: bool
        """
        return self._restart_required

    @restart_required.setter
    def restart_required(self, restart_required):
        r"""Sets the restart_required of this ParameterValuesInfo.

        是否需要重启

        :param restart_required: The restart_required of this ParameterValuesInfo.
        :type restart_required: bool
        """
        self._restart_required = restart_required

    @property
    def readonly(self):
        r"""Gets the readonly of this ParameterValuesInfo.

        是否只读

        :return: The readonly of this ParameterValuesInfo.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        r"""Sets the readonly of this ParameterValuesInfo.

        是否只读

        :param readonly: The readonly of this ParameterValuesInfo.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def name(self):
        r"""Gets the name of this ParameterValuesInfo.

        参数名

        :return: The name of this ParameterValuesInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ParameterValuesInfo.

        参数名

        :param name: The name of this ParameterValuesInfo.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this ParameterValuesInfo.

        参数值

        :return: The value of this ParameterValuesInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ParameterValuesInfo.

        参数值

        :param value: The value of this ParameterValuesInfo.
        :type value: str
        """
        self._value = value

    @property
    def type(self):
        r"""Gets the type of this ParameterValuesInfo.

        参数类型

        :return: The type of this ParameterValuesInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ParameterValuesInfo.

        参数类型

        :param type: The type of this ParameterValuesInfo.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        r"""Gets the description of this ParameterValuesInfo.

        参数描述

        :return: The description of this ParameterValuesInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ParameterValuesInfo.

        参数描述

        :param description: The description of this ParameterValuesInfo.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ParameterValuesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
