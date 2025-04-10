# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParameterConfig:

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
        'default_value': 'str',
        'value_range': 'str',
        'is_need_restart': 'bool',
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'default_value': 'default_value',
        'value_range': 'value_range',
        'is_need_restart': 'is_need_restart',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, name=None, value=None, default_value=None, value_range=None, is_need_restart=None, description=None, created_at=None, updated_at=None):
        r"""ParameterConfig

        The model defined in huaweicloud sdk

        :param name: 参数名称
        :type name: str
        :param value: 参数值
        :type value: str
        :param default_value: 参数默认值
        :type default_value: str
        :param value_range: 参数值范围，如Integer取值0-1、Boolean取值true|false等。
        :type value_range: str
        :param is_need_restart: 是否需要重启。默认为true, “false”表示否。“true”表示是。
        :type is_need_restart: bool
        :param description: 参数描述。
        :type description: str
        :param created_at: 创建时间，例如：2023-01-20T07:18:26Z
        :type created_at: str
        :param updated_at: 更新时间，例如：2023-03-01T09:42:02Z
        :type updated_at: str
        """
        
        

        self._name = None
        self._value = None
        self._default_value = None
        self._value_range = None
        self._is_need_restart = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.default_value = default_value
        self.value_range = value_range
        self.is_need_restart = is_need_restart
        self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def name(self):
        r"""Gets the name of this ParameterConfig.

        参数名称

        :return: The name of this ParameterConfig.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ParameterConfig.

        参数名称

        :param name: The name of this ParameterConfig.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        r"""Gets the value of this ParameterConfig.

        参数值

        :return: The value of this ParameterConfig.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this ParameterConfig.

        参数值

        :param value: The value of this ParameterConfig.
        :type value: str
        """
        self._value = value

    @property
    def default_value(self):
        r"""Gets the default_value of this ParameterConfig.

        参数默认值

        :return: The default_value of this ParameterConfig.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this ParameterConfig.

        参数默认值

        :param default_value: The default_value of this ParameterConfig.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def value_range(self):
        r"""Gets the value_range of this ParameterConfig.

        参数值范围，如Integer取值0-1、Boolean取值true|false等。

        :return: The value_range of this ParameterConfig.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        r"""Sets the value_range of this ParameterConfig.

        参数值范围，如Integer取值0-1、Boolean取值true|false等。

        :param value_range: The value_range of this ParameterConfig.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def is_need_restart(self):
        r"""Gets the is_need_restart of this ParameterConfig.

        是否需要重启。默认为true, “false”表示否。“true”表示是。

        :return: The is_need_restart of this ParameterConfig.
        :rtype: bool
        """
        return self._is_need_restart

    @is_need_restart.setter
    def is_need_restart(self, is_need_restart):
        r"""Sets the is_need_restart of this ParameterConfig.

        是否需要重启。默认为true, “false”表示否。“true”表示是。

        :param is_need_restart: The is_need_restart of this ParameterConfig.
        :type is_need_restart: bool
        """
        self._is_need_restart = is_need_restart

    @property
    def description(self):
        r"""Gets the description of this ParameterConfig.

        参数描述。

        :return: The description of this ParameterConfig.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ParameterConfig.

        参数描述。

        :param description: The description of this ParameterConfig.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ParameterConfig.

        创建时间，例如：2023-01-20T07:18:26Z

        :return: The created_at of this ParameterConfig.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ParameterConfig.

        创建时间，例如：2023-01-20T07:18:26Z

        :param created_at: The created_at of this ParameterConfig.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ParameterConfig.

        更新时间，例如：2023-03-01T09:42:02Z

        :return: The updated_at of this ParameterConfig.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ParameterConfig.

        更新时间，例如：2023-03-01T09:42:02Z

        :param updated_at: The updated_at of this ParameterConfig.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ParameterConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
