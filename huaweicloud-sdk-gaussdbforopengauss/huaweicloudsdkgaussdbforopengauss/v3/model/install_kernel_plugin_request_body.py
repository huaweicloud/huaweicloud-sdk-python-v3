# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstallKernelPluginRequestBody:

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
        'url': 'str',
        'sha_256': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'url': 'url',
        'sha_256': 'sha_256'
    }

    def __init__(self, plugin_name=None, url=None, sha_256=None):
        r"""InstallKernelPluginRequestBody

        The model defined in huaweicloud sdk

        :param plugin_name: 插件名称
        :type plugin_name: str
        :param url: 插件安装包链接
        :type url: str
        :param sha_256: 插件安装包的sha256值
        :type sha_256: str
        """
        
        

        self._plugin_name = None
        self._url = None
        self._sha_256 = None
        self.discriminator = None

        self.plugin_name = plugin_name
        self.url = url
        self.sha_256 = sha_256

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this InstallKernelPluginRequestBody.

        插件名称

        :return: The plugin_name of this InstallKernelPluginRequestBody.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this InstallKernelPluginRequestBody.

        插件名称

        :param plugin_name: The plugin_name of this InstallKernelPluginRequestBody.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def url(self):
        r"""Gets the url of this InstallKernelPluginRequestBody.

        插件安装包链接

        :return: The url of this InstallKernelPluginRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this InstallKernelPluginRequestBody.

        插件安装包链接

        :param url: The url of this InstallKernelPluginRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def sha_256(self):
        r"""Gets the sha_256 of this InstallKernelPluginRequestBody.

        插件安装包的sha256值

        :return: The sha_256 of this InstallKernelPluginRequestBody.
        :rtype: str
        """
        return self._sha_256

    @sha_256.setter
    def sha_256(self, sha_256):
        r"""Sets the sha_256 of this InstallKernelPluginRequestBody.

        插件安装包的sha256值

        :param sha_256: The sha_256 of this InstallKernelPluginRequestBody.
        :type sha_256: str
        """
        self._sha_256 = sha_256

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
        if not isinstance(other, InstallKernelPluginRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
