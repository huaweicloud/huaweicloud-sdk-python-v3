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
        'show_placeholder': 'str',
        'options': 'str',
        'disabled_conditions': 'str',
        'visible_conditions': 'str'
    }

    attribute_map = {
        'api_options': 'api_options',
        'api_type': 'api_type',
        'show_placeholder': 'show_placeholder',
        'options': 'options',
        'disabled_conditions': 'disabled_conditions',
        'visible_conditions': 'visible_conditions'
    }

    def __init__(self, api_options=None, api_type=None, show_placeholder=None, options=None, disabled_conditions=None, visible_conditions=None):
        r"""ExtensionExtendProp

        The model defined in huaweicloud sdk

        :param api_options: **参数解释**： API选项。 **取值范围**： 不涉及。 
        :type api_options: str
        :param api_type: **参数解释**： API类型。 **取值范围**： 不涉及。 
        :type api_type: str
        :param show_placeholder: **参数解释**： 显示占位符。 **取值范围**： 不涉及。 
        :type show_placeholder: str
        :param options: **参数解释**： 选项。 **取值范围**： 不涉及。 
        :type options: str
        :param disabled_conditions: **参数解释**： 禁用条件。 **取值范围**： 不涉及。 
        :type disabled_conditions: str
        :param visible_conditions: **参数解释**： 可见条件。 **取值范围**： 不涉及。 
        :type visible_conditions: str
        """
        
        

        self._api_options = None
        self._api_type = None
        self._show_placeholder = None
        self._options = None
        self._disabled_conditions = None
        self._visible_conditions = None
        self.discriminator = None

        if api_options is not None:
            self.api_options = api_options
        if api_type is not None:
            self.api_type = api_type
        if show_placeholder is not None:
            self.show_placeholder = show_placeholder
        if options is not None:
            self.options = options
        if disabled_conditions is not None:
            self.disabled_conditions = disabled_conditions
        if visible_conditions is not None:
            self.visible_conditions = visible_conditions

    @property
    def api_options(self):
        r"""Gets the api_options of this ExtensionExtendProp.

        **参数解释**： API选项。 **取值范围**： 不涉及。 

        :return: The api_options of this ExtensionExtendProp.
        :rtype: str
        """
        return self._api_options

    @api_options.setter
    def api_options(self, api_options):
        r"""Sets the api_options of this ExtensionExtendProp.

        **参数解释**： API选项。 **取值范围**： 不涉及。 

        :param api_options: The api_options of this ExtensionExtendProp.
        :type api_options: str
        """
        self._api_options = api_options

    @property
    def api_type(self):
        r"""Gets the api_type of this ExtensionExtendProp.

        **参数解释**： API类型。 **取值范围**： 不涉及。 

        :return: The api_type of this ExtensionExtendProp.
        :rtype: str
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this ExtensionExtendProp.

        **参数解释**： API类型。 **取值范围**： 不涉及。 

        :param api_type: The api_type of this ExtensionExtendProp.
        :type api_type: str
        """
        self._api_type = api_type

    @property
    def show_placeholder(self):
        r"""Gets the show_placeholder of this ExtensionExtendProp.

        **参数解释**： 显示占位符。 **取值范围**： 不涉及。 

        :return: The show_placeholder of this ExtensionExtendProp.
        :rtype: str
        """
        return self._show_placeholder

    @show_placeholder.setter
    def show_placeholder(self, show_placeholder):
        r"""Sets the show_placeholder of this ExtensionExtendProp.

        **参数解释**： 显示占位符。 **取值范围**： 不涉及。 

        :param show_placeholder: The show_placeholder of this ExtensionExtendProp.
        :type show_placeholder: str
        """
        self._show_placeholder = show_placeholder

    @property
    def options(self):
        r"""Gets the options of this ExtensionExtendProp.

        **参数解释**： 选项。 **取值范围**： 不涉及。 

        :return: The options of this ExtensionExtendProp.
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this ExtensionExtendProp.

        **参数解释**： 选项。 **取值范围**： 不涉及。 

        :param options: The options of this ExtensionExtendProp.
        :type options: str
        """
        self._options = options

    @property
    def disabled_conditions(self):
        r"""Gets the disabled_conditions of this ExtensionExtendProp.

        **参数解释**： 禁用条件。 **取值范围**： 不涉及。 

        :return: The disabled_conditions of this ExtensionExtendProp.
        :rtype: str
        """
        return self._disabled_conditions

    @disabled_conditions.setter
    def disabled_conditions(self, disabled_conditions):
        r"""Sets the disabled_conditions of this ExtensionExtendProp.

        **参数解释**： 禁用条件。 **取值范围**： 不涉及。 

        :param disabled_conditions: The disabled_conditions of this ExtensionExtendProp.
        :type disabled_conditions: str
        """
        self._disabled_conditions = disabled_conditions

    @property
    def visible_conditions(self):
        r"""Gets the visible_conditions of this ExtensionExtendProp.

        **参数解释**： 可见条件。 **取值范围**： 不涉及。 

        :return: The visible_conditions of this ExtensionExtendProp.
        :rtype: str
        """
        return self._visible_conditions

    @visible_conditions.setter
    def visible_conditions(self, visible_conditions):
        r"""Sets the visible_conditions of this ExtensionExtendProp.

        **参数解释**： 可见条件。 **取值范围**： 不涉及。 

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
