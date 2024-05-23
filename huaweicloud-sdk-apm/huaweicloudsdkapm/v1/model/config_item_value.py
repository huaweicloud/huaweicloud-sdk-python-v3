# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigItemValue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_name': 'str',
        'display_name': 'str',
        'config_data_type': 'str',
        'max_length': 'int',
        'min_value': 'float',
        'max_value': 'float',
        'option_values': 'list[OptionValue]',
        'default_value': 'str',
        'since_version': 'str',
        'dead_version': 'str',
        'value': 'str',
        'object_array_patterns': 'list[ObjectArrayPatterns]',
        'override_list': 'list[ConfigItemOverride]'
    }

    attribute_map = {
        'config_name': 'config_name',
        'display_name': 'display_name',
        'config_data_type': 'config_data_type',
        'max_length': 'max_length',
        'min_value': 'min_value',
        'max_value': 'max_value',
        'option_values': 'option_values',
        'default_value': 'default_value',
        'since_version': 'since_version',
        'dead_version': 'dead_version',
        'value': 'value',
        'object_array_patterns': 'object_array_patterns',
        'override_list': 'override_list'
    }

    def __init__(self, config_name=None, display_name=None, config_data_type=None, max_length=None, min_value=None, max_value=None, option_values=None, default_value=None, since_version=None, dead_version=None, value=None, object_array_patterns=None, override_list=None):
        """ConfigItemValue

        The model defined in huaweicloud sdk

        :param config_name: 配置项名字
        :type config_name: str
        :param display_name: 显示名称
        :type display_name: str
        :param config_data_type: 数据类型
        :type config_data_type: str
        :param max_length: 最大长度
        :type max_length: int
        :param min_value: 最小值
        :type min_value: float
        :param max_value: 最大值
        :type max_value: float
        :param option_values: 可选值
        :type option_values: list[:class:`huaweicloudsdkapm.v1.OptionValue`]
        :param default_value: 默认值
        :type default_value: str
        :param since_version: 开始版本
        :type since_version: str
        :param dead_version: 截至版本
        :type dead_version: str
        :param value: 值
        :type value: str
        :param object_array_patterns: 对象数组
        :type object_array_patterns: list[:class:`huaweicloudsdkapm.v1.ObjectArrayPatterns`]
        :param override_list: 实际生效值
        :type override_list: list[:class:`huaweicloudsdkapm.v1.ConfigItemOverride`]
        """
        
        

        self._config_name = None
        self._display_name = None
        self._config_data_type = None
        self._max_length = None
        self._min_value = None
        self._max_value = None
        self._option_values = None
        self._default_value = None
        self._since_version = None
        self._dead_version = None
        self._value = None
        self._object_array_patterns = None
        self._override_list = None
        self.discriminator = None

        if config_name is not None:
            self.config_name = config_name
        if display_name is not None:
            self.display_name = display_name
        if config_data_type is not None:
            self.config_data_type = config_data_type
        if max_length is not None:
            self.max_length = max_length
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if option_values is not None:
            self.option_values = option_values
        if default_value is not None:
            self.default_value = default_value
        if since_version is not None:
            self.since_version = since_version
        if dead_version is not None:
            self.dead_version = dead_version
        if value is not None:
            self.value = value
        if object_array_patterns is not None:
            self.object_array_patterns = object_array_patterns
        if override_list is not None:
            self.override_list = override_list

    @property
    def config_name(self):
        """Gets the config_name of this ConfigItemValue.

        配置项名字

        :return: The config_name of this ConfigItemValue.
        :rtype: str
        """
        return self._config_name

    @config_name.setter
    def config_name(self, config_name):
        """Sets the config_name of this ConfigItemValue.

        配置项名字

        :param config_name: The config_name of this ConfigItemValue.
        :type config_name: str
        """
        self._config_name = config_name

    @property
    def display_name(self):
        """Gets the display_name of this ConfigItemValue.

        显示名称

        :return: The display_name of this ConfigItemValue.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ConfigItemValue.

        显示名称

        :param display_name: The display_name of this ConfigItemValue.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def config_data_type(self):
        """Gets the config_data_type of this ConfigItemValue.

        数据类型

        :return: The config_data_type of this ConfigItemValue.
        :rtype: str
        """
        return self._config_data_type

    @config_data_type.setter
    def config_data_type(self, config_data_type):
        """Sets the config_data_type of this ConfigItemValue.

        数据类型

        :param config_data_type: The config_data_type of this ConfigItemValue.
        :type config_data_type: str
        """
        self._config_data_type = config_data_type

    @property
    def max_length(self):
        """Gets the max_length of this ConfigItemValue.

        最大长度

        :return: The max_length of this ConfigItemValue.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ConfigItemValue.

        最大长度

        :param max_length: The max_length of this ConfigItemValue.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def min_value(self):
        """Gets the min_value of this ConfigItemValue.

        最小值

        :return: The min_value of this ConfigItemValue.
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this ConfigItemValue.

        最小值

        :param min_value: The min_value of this ConfigItemValue.
        :type min_value: float
        """
        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this ConfigItemValue.

        最大值

        :return: The max_value of this ConfigItemValue.
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this ConfigItemValue.

        最大值

        :param max_value: The max_value of this ConfigItemValue.
        :type max_value: float
        """
        self._max_value = max_value

    @property
    def option_values(self):
        """Gets the option_values of this ConfigItemValue.

        可选值

        :return: The option_values of this ConfigItemValue.
        :rtype: list[:class:`huaweicloudsdkapm.v1.OptionValue`]
        """
        return self._option_values

    @option_values.setter
    def option_values(self, option_values):
        """Sets the option_values of this ConfigItemValue.

        可选值

        :param option_values: The option_values of this ConfigItemValue.
        :type option_values: list[:class:`huaweicloudsdkapm.v1.OptionValue`]
        """
        self._option_values = option_values

    @property
    def default_value(self):
        """Gets the default_value of this ConfigItemValue.

        默认值

        :return: The default_value of this ConfigItemValue.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ConfigItemValue.

        默认值

        :param default_value: The default_value of this ConfigItemValue.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def since_version(self):
        """Gets the since_version of this ConfigItemValue.

        开始版本

        :return: The since_version of this ConfigItemValue.
        :rtype: str
        """
        return self._since_version

    @since_version.setter
    def since_version(self, since_version):
        """Sets the since_version of this ConfigItemValue.

        开始版本

        :param since_version: The since_version of this ConfigItemValue.
        :type since_version: str
        """
        self._since_version = since_version

    @property
    def dead_version(self):
        """Gets the dead_version of this ConfigItemValue.

        截至版本

        :return: The dead_version of this ConfigItemValue.
        :rtype: str
        """
        return self._dead_version

    @dead_version.setter
    def dead_version(self, dead_version):
        """Sets the dead_version of this ConfigItemValue.

        截至版本

        :param dead_version: The dead_version of this ConfigItemValue.
        :type dead_version: str
        """
        self._dead_version = dead_version

    @property
    def value(self):
        """Gets the value of this ConfigItemValue.

        值

        :return: The value of this ConfigItemValue.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConfigItemValue.

        值

        :param value: The value of this ConfigItemValue.
        :type value: str
        """
        self._value = value

    @property
    def object_array_patterns(self):
        """Gets the object_array_patterns of this ConfigItemValue.

        对象数组

        :return: The object_array_patterns of this ConfigItemValue.
        :rtype: list[:class:`huaweicloudsdkapm.v1.ObjectArrayPatterns`]
        """
        return self._object_array_patterns

    @object_array_patterns.setter
    def object_array_patterns(self, object_array_patterns):
        """Sets the object_array_patterns of this ConfigItemValue.

        对象数组

        :param object_array_patterns: The object_array_patterns of this ConfigItemValue.
        :type object_array_patterns: list[:class:`huaweicloudsdkapm.v1.ObjectArrayPatterns`]
        """
        self._object_array_patterns = object_array_patterns

    @property
    def override_list(self):
        """Gets the override_list of this ConfigItemValue.

        实际生效值

        :return: The override_list of this ConfigItemValue.
        :rtype: list[:class:`huaweicloudsdkapm.v1.ConfigItemOverride`]
        """
        return self._override_list

    @override_list.setter
    def override_list(self, override_list):
        """Sets the override_list of this ConfigItemValue.

        实际生效值

        :param override_list: The override_list of this ConfigItemValue.
        :type override_list: list[:class:`huaweicloudsdkapm.v1.ConfigItemOverride`]
        """
        self._override_list = override_list

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
        if not isinstance(other, ConfigItemValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
