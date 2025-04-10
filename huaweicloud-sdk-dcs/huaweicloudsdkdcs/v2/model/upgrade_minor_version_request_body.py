# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpgradeMinorVersionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy_minor_version': 'str',
        'engine_minor_version': 'str'
    }

    attribute_map = {
        'proxy_minor_version': 'proxy_minor_version',
        'engine_minor_version': 'engine_minor_version'
    }

    def __init__(self, proxy_minor_version=None, engine_minor_version=None):
        r"""UpgradeMinorVersionRequestBody

        The model defined in huaweicloud sdk

        :param proxy_minor_version: Proxy代理节点目标版本号，设置为latest时，即升级到最新版本。
        :type proxy_minor_version: str
        :param engine_minor_version: 引擎目标小版本号，设置为latest时，即升级到最新版本。
        :type engine_minor_version: str
        """
        
        

        self._proxy_minor_version = None
        self._engine_minor_version = None
        self.discriminator = None

        if proxy_minor_version is not None:
            self.proxy_minor_version = proxy_minor_version
        if engine_minor_version is not None:
            self.engine_minor_version = engine_minor_version

    @property
    def proxy_minor_version(self):
        r"""Gets the proxy_minor_version of this UpgradeMinorVersionRequestBody.

        Proxy代理节点目标版本号，设置为latest时，即升级到最新版本。

        :return: The proxy_minor_version of this UpgradeMinorVersionRequestBody.
        :rtype: str
        """
        return self._proxy_minor_version

    @proxy_minor_version.setter
    def proxy_minor_version(self, proxy_minor_version):
        r"""Sets the proxy_minor_version of this UpgradeMinorVersionRequestBody.

        Proxy代理节点目标版本号，设置为latest时，即升级到最新版本。

        :param proxy_minor_version: The proxy_minor_version of this UpgradeMinorVersionRequestBody.
        :type proxy_minor_version: str
        """
        self._proxy_minor_version = proxy_minor_version

    @property
    def engine_minor_version(self):
        r"""Gets the engine_minor_version of this UpgradeMinorVersionRequestBody.

        引擎目标小版本号，设置为latest时，即升级到最新版本。

        :return: The engine_minor_version of this UpgradeMinorVersionRequestBody.
        :rtype: str
        """
        return self._engine_minor_version

    @engine_minor_version.setter
    def engine_minor_version(self, engine_minor_version):
        r"""Sets the engine_minor_version of this UpgradeMinorVersionRequestBody.

        引擎目标小版本号，设置为latest时，即升级到最新版本。

        :param engine_minor_version: The engine_minor_version of this UpgradeMinorVersionRequestBody.
        :type engine_minor_version: str
        """
        self._engine_minor_version = engine_minor_version

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
        if not isinstance(other, UpgradeMinorVersionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
