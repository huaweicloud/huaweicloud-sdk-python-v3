# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginInstallScriptResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'package_type': 'str',
        'cmd': 'str',
        'package_download_url': 'str'
    }

    attribute_map = {
        'package_type': 'package_type',
        'cmd': 'cmd',
        'package_download_url': 'package_download_url'
    }

    def __init__(self, package_type=None, cmd=None, package_download_url=None):
        r"""PluginInstallScriptResponseInfo

        The model defined in huaweicloud sdk

        :param package_type: **参数解释**： 安装包类型 **取值范围**： 字符长度0-128位 
        :type package_type: str
        :param cmd: **参数解释**： 命令cmd **取值范围**： 字符长度1-256位 
        :type cmd: str
        :param package_download_url: **参数解释**： 包下载地址 **取值范围**： 字符长度1-256位 
        :type package_download_url: str
        """
        
        

        self._package_type = None
        self._cmd = None
        self._package_download_url = None
        self.discriminator = None

        if package_type is not None:
            self.package_type = package_type
        if cmd is not None:
            self.cmd = cmd
        if package_download_url is not None:
            self.package_download_url = package_download_url

    @property
    def package_type(self):
        r"""Gets the package_type of this PluginInstallScriptResponseInfo.

        **参数解释**： 安装包类型 **取值范围**： 字符长度0-128位 

        :return: The package_type of this PluginInstallScriptResponseInfo.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this PluginInstallScriptResponseInfo.

        **参数解释**： 安装包类型 **取值范围**： 字符长度0-128位 

        :param package_type: The package_type of this PluginInstallScriptResponseInfo.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def cmd(self):
        r"""Gets the cmd of this PluginInstallScriptResponseInfo.

        **参数解释**： 命令cmd **取值范围**： 字符长度1-256位 

        :return: The cmd of this PluginInstallScriptResponseInfo.
        :rtype: str
        """
        return self._cmd

    @cmd.setter
    def cmd(self, cmd):
        r"""Sets the cmd of this PluginInstallScriptResponseInfo.

        **参数解释**： 命令cmd **取值范围**： 字符长度1-256位 

        :param cmd: The cmd of this PluginInstallScriptResponseInfo.
        :type cmd: str
        """
        self._cmd = cmd

    @property
    def package_download_url(self):
        r"""Gets the package_download_url of this PluginInstallScriptResponseInfo.

        **参数解释**： 包下载地址 **取值范围**： 字符长度1-256位 

        :return: The package_download_url of this PluginInstallScriptResponseInfo.
        :rtype: str
        """
        return self._package_download_url

    @package_download_url.setter
    def package_download_url(self, package_download_url):
        r"""Sets the package_download_url of this PluginInstallScriptResponseInfo.

        **参数解释**： 包下载地址 **取值范围**： 字符长度1-256位 

        :param package_download_url: The package_download_url of this PluginInstallScriptResponseInfo.
        :type package_download_url: str
        """
        self._package_download_url = package_download_url

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
        if not isinstance(other, PluginInstallScriptResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
