# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParaGroupParameterResult:

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
        'need_restart': 'bool',
        'readonly': 'bool',
        'value_range': 'str',
        'data_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'need_restart': 'need_restart',
        'readonly': 'readonly',
        'value_range': 'value_range',
        'data_type': 'data_type',
        'description': 'description'
    }

    def __init__(self, name=None, value=None, need_restart=None, readonly=None, value_range=None, data_type=None, description=None):
        """ParaGroupParameterResult

        The model defined in huaweicloud sdk

        :param name: 特定参数名称。
        :type name: str
        :param value: 特定参数值。
        :type value: str
        :param need_restart: 参数是否需要重启。 - 取值为\&quot;true\&quot;，需要重启。 - 取值为\&quot;false\&quot;，不需要重启。
        :type need_restart: bool
        :param readonly: 该参数是否只读(true：只读；false：可编辑)。
        :type readonly: bool
        :param value_range: 参数取值范围。
        :type value_range: str
        :param data_type: 参数类型，取值为“string”、“integer”、“boolean”、“list”、\&quot;all\&quot;或“float”之一。
        :type data_type: str
        :param description: 参数描述。
        :type description: str
        """
        
        

        self._name = None
        self._value = None
        self._need_restart = None
        self._readonly = None
        self._value_range = None
        self._data_type = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.need_restart = need_restart
        self.readonly = readonly
        self.value_range = value_range
        self.data_type = data_type
        self.description = description

    @property
    def name(self):
        """Gets the name of this ParaGroupParameterResult.

        特定参数名称。

        :return: The name of this ParaGroupParameterResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParaGroupParameterResult.

        特定参数名称。

        :param name: The name of this ParaGroupParameterResult.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this ParaGroupParameterResult.

        特定参数值。

        :return: The value of this ParaGroupParameterResult.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ParaGroupParameterResult.

        特定参数值。

        :param value: The value of this ParaGroupParameterResult.
        :type value: str
        """
        self._value = value

    @property
    def need_restart(self):
        """Gets the need_restart of this ParaGroupParameterResult.

        参数是否需要重启。 - 取值为\"true\"，需要重启。 - 取值为\"false\"，不需要重启。

        :return: The need_restart of this ParaGroupParameterResult.
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        """Sets the need_restart of this ParaGroupParameterResult.

        参数是否需要重启。 - 取值为\"true\"，需要重启。 - 取值为\"false\"，不需要重启。

        :param need_restart: The need_restart of this ParaGroupParameterResult.
        :type need_restart: bool
        """
        self._need_restart = need_restart

    @property
    def readonly(self):
        """Gets the readonly of this ParaGroupParameterResult.

        该参数是否只读(true：只读；false：可编辑)。

        :return: The readonly of this ParaGroupParameterResult.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this ParaGroupParameterResult.

        该参数是否只读(true：只读；false：可编辑)。

        :param readonly: The readonly of this ParaGroupParameterResult.
        :type readonly: bool
        """
        self._readonly = readonly

    @property
    def value_range(self):
        """Gets the value_range of this ParaGroupParameterResult.

        参数取值范围。

        :return: The value_range of this ParaGroupParameterResult.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this ParaGroupParameterResult.

        参数取值范围。

        :param value_range: The value_range of this ParaGroupParameterResult.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def data_type(self):
        """Gets the data_type of this ParaGroupParameterResult.

        参数类型，取值为“string”、“integer”、“boolean”、“list”、\"all\"或“float”之一。

        :return: The data_type of this ParaGroupParameterResult.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ParaGroupParameterResult.

        参数类型，取值为“string”、“integer”、“boolean”、“list”、\"all\"或“float”之一。

        :param data_type: The data_type of this ParaGroupParameterResult.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def description(self):
        """Gets the description of this ParaGroupParameterResult.

        参数描述。

        :return: The description of this ParaGroupParameterResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ParaGroupParameterResult.

        参数描述。

        :param description: The description of this ParaGroupParameterResult.
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
        if not isinstance(other, ParaGroupParameterResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
