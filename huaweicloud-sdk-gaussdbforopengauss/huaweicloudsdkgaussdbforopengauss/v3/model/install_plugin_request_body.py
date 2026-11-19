# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstallPluginRequestBody:

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
        'version': 'str',
        'port': 'str',
        'obs_url': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'version': 'version',
        'port': 'port',
        'obs_url': 'obs_url'
    }

    def __init__(self, plugin_name=None, version=None, port=None, obs_url=None):
        r"""InstallPluginRequestBody

        The model defined in huaweicloud sdk

        :param plugin_name: **参数解释**: 插件名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type plugin_name: str
        :param version: **参数解释**: 插件版本。 **约束限制**: 不涉及。 **取值范围**: 长度为2~64个字符。 **默认取值**: 不涉及。
        :type version: str
        :param port: **参数解释**: 插件安装端口。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type port: str
        :param obs_url: **参数解释**: 安装插件的OBS地址。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type obs_url: str
        """
        
        

        self._plugin_name = None
        self._version = None
        self._port = None
        self._obs_url = None
        self.discriminator = None

        self.plugin_name = plugin_name
        if version is not None:
            self.version = version
        if port is not None:
            self.port = port
        if obs_url is not None:
            self.obs_url = obs_url

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this InstallPluginRequestBody.

        **参数解释**: 插件名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The plugin_name of this InstallPluginRequestBody.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this InstallPluginRequestBody.

        **参数解释**: 插件名称。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param plugin_name: The plugin_name of this InstallPluginRequestBody.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def version(self):
        r"""Gets the version of this InstallPluginRequestBody.

        **参数解释**: 插件版本。 **约束限制**: 不涉及。 **取值范围**: 长度为2~64个字符。 **默认取值**: 不涉及。

        :return: The version of this InstallPluginRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this InstallPluginRequestBody.

        **参数解释**: 插件版本。 **约束限制**: 不涉及。 **取值范围**: 长度为2~64个字符。 **默认取值**: 不涉及。

        :param version: The version of this InstallPluginRequestBody.
        :type version: str
        """
        self._version = version

    @property
    def port(self):
        r"""Gets the port of this InstallPluginRequestBody.

        **参数解释**: 插件安装端口。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The port of this InstallPluginRequestBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this InstallPluginRequestBody.

        **参数解释**: 插件安装端口。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param port: The port of this InstallPluginRequestBody.
        :type port: str
        """
        self._port = port

    @property
    def obs_url(self):
        r"""Gets the obs_url of this InstallPluginRequestBody.

        **参数解释**: 安装插件的OBS地址。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The obs_url of this InstallPluginRequestBody.
        :rtype: str
        """
        return self._obs_url

    @obs_url.setter
    def obs_url(self, obs_url):
        r"""Sets the obs_url of this InstallPluginRequestBody.

        **参数解释**: 安装插件的OBS地址。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param obs_url: The obs_url of this InstallPluginRequestBody.
        :type obs_url: str
        """
        self._obs_url = obs_url

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
        if not isinstance(other, InstallPluginRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
