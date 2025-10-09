# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginInfoListResponse(SdkResponse):

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
        'port': 'str',
        'plugin_version': 'str',
        'installed': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'port': 'port',
        'plugin_version': 'plugin_version',
        'installed': 'installed'
    }

    def __init__(self, plugin_name=None, port=None, plugin_version=None, installed=None):
        r"""ListPluginInfoListResponse

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名称
        :type plugin_name: str
        :param port: 端口
        :type port: str
        :param plugin_version: 插件版本
        :type plugin_version: str
        :param installed: 是否已安装
        :type installed: str
        """
        
        super(ListPluginInfoListResponse, self).__init__()

        self._plugin_name = None
        self._port = None
        self._plugin_version = None
        self._installed = None
        self.discriminator = None

        if plugin_name is not None:
            self.plugin_name = plugin_name
        if port is not None:
            self.port = port
        if plugin_version is not None:
            self.plugin_version = plugin_version
        if installed is not None:
            self.installed = installed

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this ListPluginInfoListResponse.

        插件名称

        :return: The plugin_name of this ListPluginInfoListResponse.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this ListPluginInfoListResponse.

        插件名称

        :param plugin_name: The plugin_name of this ListPluginInfoListResponse.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def port(self):
        r"""Gets the port of this ListPluginInfoListResponse.

        端口

        :return: The port of this ListPluginInfoListResponse.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ListPluginInfoListResponse.

        端口

        :param port: The port of this ListPluginInfoListResponse.
        :type port: str
        """
        self._port = port

    @property
    def plugin_version(self):
        r"""Gets the plugin_version of this ListPluginInfoListResponse.

        插件版本

        :return: The plugin_version of this ListPluginInfoListResponse.
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        r"""Sets the plugin_version of this ListPluginInfoListResponse.

        插件版本

        :param plugin_version: The plugin_version of this ListPluginInfoListResponse.
        :type plugin_version: str
        """
        self._plugin_version = plugin_version

    @property
    def installed(self):
        r"""Gets the installed of this ListPluginInfoListResponse.

        是否已安装

        :return: The installed of this ListPluginInfoListResponse.
        :rtype: str
        """
        return self._installed

    @installed.setter
    def installed(self, installed):
        r"""Sets the installed of this ListPluginInfoListResponse.

        是否已安装

        :param installed: The installed of this ListPluginInfoListResponse.
        :type installed: str
        """
        self._installed = installed

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
        if not isinstance(other, ListPluginInfoListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
