# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginInstallBasicParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'install_version': 'str',
        'domain_ak': 'str',
        'domain_sk': 'str'
    }

    attribute_map = {
        'install_version': 'install_version',
        'domain_ak': 'domain_ak',
        'domain_sk': 'domain_sk'
    }

    def __init__(self, install_version=None, domain_ak=None, domain_sk=None):
        r"""PluginInstallBasicParam

        The model defined in huaweicloud sdk

        :param install_version: 指定安装的ICAgent版本。
        :type install_version: str
        :param domain_ak: IAM账号AK，选填。.
        :type domain_ak: str
        :param domain_sk: IAM账号SK，选填。
        :type domain_sk: str
        """
        
        

        self._install_version = None
        self._domain_ak = None
        self._domain_sk = None
        self.discriminator = None

        if install_version is not None:
            self.install_version = install_version
        if domain_ak is not None:
            self.domain_ak = domain_ak
        if domain_sk is not None:
            self.domain_sk = domain_sk

    @property
    def install_version(self):
        r"""Gets the install_version of this PluginInstallBasicParam.

        指定安装的ICAgent版本。

        :return: The install_version of this PluginInstallBasicParam.
        :rtype: str
        """
        return self._install_version

    @install_version.setter
    def install_version(self, install_version):
        r"""Sets the install_version of this PluginInstallBasicParam.

        指定安装的ICAgent版本。

        :param install_version: The install_version of this PluginInstallBasicParam.
        :type install_version: str
        """
        self._install_version = install_version

    @property
    def domain_ak(self):
        r"""Gets the domain_ak of this PluginInstallBasicParam.

        IAM账号AK，选填。.

        :return: The domain_ak of this PluginInstallBasicParam.
        :rtype: str
        """
        return self._domain_ak

    @domain_ak.setter
    def domain_ak(self, domain_ak):
        r"""Sets the domain_ak of this PluginInstallBasicParam.

        IAM账号AK，选填。.

        :param domain_ak: The domain_ak of this PluginInstallBasicParam.
        :type domain_ak: str
        """
        self._domain_ak = domain_ak

    @property
    def domain_sk(self):
        r"""Gets the domain_sk of this PluginInstallBasicParam.

        IAM账号SK，选填。

        :return: The domain_sk of this PluginInstallBasicParam.
        :rtype: str
        """
        return self._domain_sk

    @domain_sk.setter
    def domain_sk(self, domain_sk):
        r"""Sets the domain_sk of this PluginInstallBasicParam.

        IAM账号SK，选填。

        :param domain_sk: The domain_sk of this PluginInstallBasicParam.
        :type domain_sk: str
        """
        self._domain_sk = domain_sk

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
        if not isinstance(other, PluginInstallBasicParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
