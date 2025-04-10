# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_name': 'str',
        'data_type': 'str',
        'default_value': 'str',
        'value_range': 'str',
        'description': 'str',
        'is_modifiable': 'str'
    }

    attribute_map = {
        'param_name': 'param_name',
        'data_type': 'data_type',
        'default_value': 'default_value',
        'value_range': 'value_range',
        'description': 'description',
        'is_modifiable': 'is_modifiable'
    }

    def __init__(self, param_name=None, data_type=None, default_value=None, value_range=None, description=None, is_modifiable=None):
        r"""DbParameter

        The model defined in huaweicloud sdk

        :param param_name: 参数名称。
        :type param_name: str
        :param data_type: 参数类型。
        :type data_type: str
        :param default_value: 参数默认值。
        :type default_value: str
        :param value_range: 参数取值范围。
        :type value_range: str
        :param description: 参数描述。
        :type description: str
        :param is_modifiable: **参数解释**：  新增子任务的场景，用于区分库参数是否支持修改。  **取值范围**：  不涉及。
        :type is_modifiable: str
        """
        
        

        self._param_name = None
        self._data_type = None
        self._default_value = None
        self._value_range = None
        self._description = None
        self._is_modifiable = None
        self.discriminator = None

        if param_name is not None:
            self.param_name = param_name
        if data_type is not None:
            self.data_type = data_type
        if default_value is not None:
            self.default_value = default_value
        if value_range is not None:
            self.value_range = value_range
        if description is not None:
            self.description = description
        if is_modifiable is not None:
            self.is_modifiable = is_modifiable

    @property
    def param_name(self):
        r"""Gets the param_name of this DbParameter.

        参数名称。

        :return: The param_name of this DbParameter.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        r"""Sets the param_name of this DbParameter.

        参数名称。

        :param param_name: The param_name of this DbParameter.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def data_type(self):
        r"""Gets the data_type of this DbParameter.

        参数类型。

        :return: The data_type of this DbParameter.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this DbParameter.

        参数类型。

        :param data_type: The data_type of this DbParameter.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def default_value(self):
        r"""Gets the default_value of this DbParameter.

        参数默认值。

        :return: The default_value of this DbParameter.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this DbParameter.

        参数默认值。

        :param default_value: The default_value of this DbParameter.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def value_range(self):
        r"""Gets the value_range of this DbParameter.

        参数取值范围。

        :return: The value_range of this DbParameter.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        r"""Sets the value_range of this DbParameter.

        参数取值范围。

        :param value_range: The value_range of this DbParameter.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def description(self):
        r"""Gets the description of this DbParameter.

        参数描述。

        :return: The description of this DbParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DbParameter.

        参数描述。

        :param description: The description of this DbParameter.
        :type description: str
        """
        self._description = description

    @property
    def is_modifiable(self):
        r"""Gets the is_modifiable of this DbParameter.

        **参数解释**：  新增子任务的场景，用于区分库参数是否支持修改。  **取值范围**：  不涉及。

        :return: The is_modifiable of this DbParameter.
        :rtype: str
        """
        return self._is_modifiable

    @is_modifiable.setter
    def is_modifiable(self, is_modifiable):
        r"""Sets the is_modifiable of this DbParameter.

        **参数解释**：  新增子任务的场景，用于区分库参数是否支持修改。  **取值范围**：  不涉及。

        :param is_modifiable: The is_modifiable of this DbParameter.
        :type is_modifiable: str
        """
        self._is_modifiable = is_modifiable

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
        if not isinstance(other, DbParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
