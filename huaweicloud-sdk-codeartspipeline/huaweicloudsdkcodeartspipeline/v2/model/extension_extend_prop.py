# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionExtendProp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_options': 'str',
        'api_type': 'str',
        'options': 'str',
        'disabled_conditions': 'str',
        'visible_conditions': 'str'
    }

    attribute_map = {
        'api_options': 'api_options',
        'api_type': 'api_type',
        'options': 'options',
        'disabled_conditions': 'disabled_conditions',
        'visible_conditions': 'visible_conditions'
    }

    def __init__(self, api_options=None, api_type=None, options=None, disabled_conditions=None, visible_conditions=None):
        """ExtensionExtendProp

        The model defined in huaweicloud sdk

        :param api_options: API 选项
        :type api_options: str
        :param api_type: API 类型
        :type api_type: str
        :param options: 选项
        :type options: str
        :param disabled_conditions: 禁用条件
        :type disabled_conditions: str
        :param visible_conditions: 可见条件
        :type visible_conditions: str
        """
        
        

        self._api_options = None
        self._api_type = None
        self._options = None
        self._disabled_conditions = None
        self._visible_conditions = None
        self.discriminator = None

        if api_options is not None:
            self.api_options = api_options
        if api_type is not None:
            self.api_type = api_type
        if options is not None:
            self.options = options
        if disabled_conditions is not None:
            self.disabled_conditions = disabled_conditions
        if visible_conditions is not None:
            self.visible_conditions = visible_conditions

    @property
    def api_options(self):
        """Gets the api_options of this ExtensionExtendProp.

        API 选项

        :return: The api_options of this ExtensionExtendProp.
        :rtype: str
        """
        return self._api_options

    @api_options.setter
    def api_options(self, api_options):
        """Sets the api_options of this ExtensionExtendProp.

        API 选项

        :param api_options: The api_options of this ExtensionExtendProp.
        :type api_options: str
        """
        self._api_options = api_options

    @property
    def api_type(self):
        """Gets the api_type of this ExtensionExtendProp.

        API 类型

        :return: The api_type of this ExtensionExtendProp.
        :rtype: str
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        """Sets the api_type of this ExtensionExtendProp.

        API 类型

        :param api_type: The api_type of this ExtensionExtendProp.
        :type api_type: str
        """
        self._api_type = api_type

    @property
    def options(self):
        """Gets the options of this ExtensionExtendProp.

        选项

        :return: The options of this ExtensionExtendProp.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ExtensionExtendProp.

        选项

        :param options: The options of this ExtensionExtendProp.
        :type options: str
        """
        self._options = options

    @property
    def disabled_conditions(self):
        """Gets the disabled_conditions of this ExtensionExtendProp.

        禁用条件

        :return: The disabled_conditions of this ExtensionExtendProp.
        :rtype: str
        """
        return self._disabled_conditions

    @disabled_conditions.setter
    def disabled_conditions(self, disabled_conditions):
        """Sets the disabled_conditions of this ExtensionExtendProp.

        禁用条件

        :param disabled_conditions: The disabled_conditions of this ExtensionExtendProp.
        :type disabled_conditions: str
        """
        self._disabled_conditions = disabled_conditions

    @property
    def visible_conditions(self):
        """Gets the visible_conditions of this ExtensionExtendProp.

        可见条件

        :return: The visible_conditions of this ExtensionExtendProp.
        :rtype: str
        """
        return self._visible_conditions

    @visible_conditions.setter
    def visible_conditions(self, visible_conditions):
        """Sets the visible_conditions of this ExtensionExtendProp.

        可见条件

        :param visible_conditions: The visible_conditions of this ExtensionExtendProp.
        :type visible_conditions: str
        """
        self._visible_conditions = visible_conditions

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
        if not isinstance(other, ExtensionExtendProp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
