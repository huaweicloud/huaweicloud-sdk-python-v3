# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionParameter:

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
        'label': 'str',
        'validation': 'ExtensionParameterValidation',
        'default_value': 'str',
        'help_markdown': 'str',
        'display_settings': 'ExtensionParameterDisplaySettings'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'validation': 'validation',
        'default_value': 'defaultValue',
        'help_markdown': 'helpMarkdown',
        'display_settings': 'displaySettings'
    }

    def __init__(self, name=None, label=None, validation=None, default_value=None, help_markdown=None, display_settings=None):
        r"""ExtensionParameter

        The model defined in huaweicloud sdk

        :param name: 参数名
        :type name: str
        :param label: 参数显示标签
        :type label: str
        :param validation: 
        :type validation: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameterValidation`
        :param default_value: 默认值
        :type default_value: str
        :param help_markdown: 帮助文档(markdown格式)。
        :type help_markdown: str
        :param display_settings: 
        :type display_settings: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameterDisplaySettings`
        """
        
        

        self._name = None
        self._label = None
        self._validation = None
        self._default_value = None
        self._help_markdown = None
        self._display_settings = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if label is not None:
            self.label = label
        if validation is not None:
            self.validation = validation
        if default_value is not None:
            self.default_value = default_value
        if help_markdown is not None:
            self.help_markdown = help_markdown
        if display_settings is not None:
            self.display_settings = display_settings

    @property
    def name(self):
        r"""Gets the name of this ExtensionParameter.

        参数名

        :return: The name of this ExtensionParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExtensionParameter.

        参数名

        :param name: The name of this ExtensionParameter.
        :type name: str
        """
        self._name = name

    @property
    def label(self):
        r"""Gets the label of this ExtensionParameter.

        参数显示标签

        :return: The label of this ExtensionParameter.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this ExtensionParameter.

        参数显示标签

        :param label: The label of this ExtensionParameter.
        :type label: str
        """
        self._label = label

    @property
    def validation(self):
        r"""Gets the validation of this ExtensionParameter.

        :return: The validation of this ExtensionParameter.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameterValidation`
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        r"""Sets the validation of this ExtensionParameter.

        :param validation: The validation of this ExtensionParameter.
        :type validation: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameterValidation`
        """
        self._validation = validation

    @property
    def default_value(self):
        r"""Gets the default_value of this ExtensionParameter.

        默认值

        :return: The default_value of this ExtensionParameter.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this ExtensionParameter.

        默认值

        :param default_value: The default_value of this ExtensionParameter.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def help_markdown(self):
        r"""Gets the help_markdown of this ExtensionParameter.

        帮助文档(markdown格式)。

        :return: The help_markdown of this ExtensionParameter.
        :rtype: str
        """
        return self._help_markdown

    @help_markdown.setter
    def help_markdown(self, help_markdown):
        r"""Sets the help_markdown of this ExtensionParameter.

        帮助文档(markdown格式)。

        :param help_markdown: The help_markdown of this ExtensionParameter.
        :type help_markdown: str
        """
        self._help_markdown = help_markdown

    @property
    def display_settings(self):
        r"""Gets the display_settings of this ExtensionParameter.

        :return: The display_settings of this ExtensionParameter.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameterDisplaySettings`
        """
        return self._display_settings

    @display_settings.setter
    def display_settings(self, display_settings):
        r"""Sets the display_settings of this ExtensionParameter.

        :param display_settings: The display_settings of this ExtensionParameter.
        :type display_settings: :class:`huaweicloudsdkcodeartspipeline.v2.ExtensionParameterDisplaySettings`
        """
        self._display_settings = display_settings

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
        if not isinstance(other, ExtensionParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
