# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomerPluginInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_name': 'str',
        'installed': 'bool',
        'port': 'str',
        'plugin_version': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'installed': 'installed',
        'port': 'port',
        'plugin_version': 'plugin_version'
    }

    def __init__(self, plugin_name=None, installed=None, port=None, plugin_version=None):
        r"""CustomerPluginInfoResult

        The model defined in huaweicloud sdk

        :param plugin_name: **参数解释**: 插件名称。 **取值范围**: 不涉及。 
        :type plugin_name: str
        :param installed: **参数解释**: 是否安装此插件。 **取值范围**: 不涉及。 
        :type installed: bool
        :param port: **参数解释**: 插件端口。 **取值范围**: 不涉及。 
        :type port: str
        :param plugin_version: **参数解释**: 插件版本。 **取值范围**: 不涉及。 
        :type plugin_version: str
        """
        
        

        self._plugin_name = None
        self._installed = None
        self._port = None
        self._plugin_version = None
        self.discriminator = None

        if plugin_name is not None:
            self.plugin_name = plugin_name
        if installed is not None:
            self.installed = installed
        if port is not None:
            self.port = port
        if plugin_version is not None:
            self.plugin_version = plugin_version

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this CustomerPluginInfoResult.

        **参数解释**: 插件名称。 **取值范围**: 不涉及。 

        :return: The plugin_name of this CustomerPluginInfoResult.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this CustomerPluginInfoResult.

        **参数解释**: 插件名称。 **取值范围**: 不涉及。 

        :param plugin_name: The plugin_name of this CustomerPluginInfoResult.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def installed(self):
        r"""Gets the installed of this CustomerPluginInfoResult.

        **参数解释**: 是否安装此插件。 **取值范围**: 不涉及。 

        :return: The installed of this CustomerPluginInfoResult.
        :rtype: bool
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        r"""Sets the installed of this CustomerPluginInfoResult.

        **参数解释**: 是否安装此插件。 **取值范围**: 不涉及。 

        :param installed: The installed of this CustomerPluginInfoResult.
        :type installed: bool
        """
        self._installed = installed

    @property
    def port(self):
        r"""Gets the port of this CustomerPluginInfoResult.

        **参数解释**: 插件端口。 **取值范围**: 不涉及。 

        :return: The port of this CustomerPluginInfoResult.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this CustomerPluginInfoResult.

        **参数解释**: 插件端口。 **取值范围**: 不涉及。 

        :param port: The port of this CustomerPluginInfoResult.
        :type port: str
        """
        self._port = port

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this CustomerPluginInfoResult.

        **参数解释**: 插件版本。 **取值范围**: 不涉及。 

        :return: The plugin_version of this CustomerPluginInfoResult.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this CustomerPluginInfoResult.

        **参数解释**: 插件版本。 **取值范围**: 不涉及。 

        :param plugin_version: The plugin_version of this CustomerPluginInfoResult.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

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
        if not isinstance(other, CustomerPluginInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
