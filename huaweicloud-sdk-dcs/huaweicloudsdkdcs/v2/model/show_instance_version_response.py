# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_minor_version': 'str',
        'latest_engine_minor_version': 'str',
        'proxy_minor_version': 'str',
        'latest_proxy_minor_version': 'str',
        'engine_minor_version_upgradable': 'bool',
        'proxy_minor_version_upgradable': 'bool'
    }

    attribute_map = {
        'engine_minor_version': 'engine_minor_version',
        'latest_engine_minor_version': 'latest_engine_minor_version',
        'proxy_minor_version': 'proxy_minor_version',
        'latest_proxy_minor_version': 'latest_proxy_minor_version',
        'engine_minor_version_upgradable': 'engine_minor_version_upgradable',
        'proxy_minor_version_upgradable': 'proxy_minor_version_upgradable'
    }

    def __init__(self, engine_minor_version=None, latest_engine_minor_version=None, proxy_minor_version=None, latest_proxy_minor_version=None, engine_minor_version_upgradable=None, proxy_minor_version_upgradable=None):
        r"""ShowInstanceVersionResponse

        The model defined in huaweicloud sdk

        :param engine_minor_version: 当前实例内核小版本信息。
        :type engine_minor_version: str
        :param latest_engine_minor_version: DCS实例最新的内核小版本信息。
        :type latest_engine_minor_version: str
        :param proxy_minor_version: 当前实例proxy代理节点版本信息。
        :type proxy_minor_version: str
        :param latest_proxy_minor_version: DCS实例最新的proxy代理节点版本信息。
        :type latest_proxy_minor_version: str
        :param engine_minor_version_upgradable: 当前实例内核是否可以升级。
        :type engine_minor_version_upgradable: bool
        :param proxy_minor_version_upgradable: 当前实例proxy代理节点是否可以升级。
        :type proxy_minor_version_upgradable: bool
        """
        
        super(ShowInstanceVersionResponse, self).__init__()

        self._engine_minor_version = None
        self._latest_engine_minor_version = None
        self._proxy_minor_version = None
        self._latest_proxy_minor_version = None
        self._engine_minor_version_upgradable = None
        self._proxy_minor_version_upgradable = None
        self.discriminator = None

        if engine_minor_version is not None:
            self.engine_minor_version = engine_minor_version
        if latest_engine_minor_version is not None:
            self.latest_engine_minor_version = latest_engine_minor_version
        if proxy_minor_version is not None:
            self.proxy_minor_version = proxy_minor_version
        if latest_proxy_minor_version is not None:
            self.latest_proxy_minor_version = latest_proxy_minor_version
        if engine_minor_version_upgradable is not None:
            self.engine_minor_version_upgradable = engine_minor_version_upgradable
        if proxy_minor_version_upgradable is not None:
            self.proxy_minor_version_upgradable = proxy_minor_version_upgradable

    @property
    def engine_minor_version(self):
        r"""Gets the engine_minor_version of this ShowInstanceVersionResponse.

        当前实例内核小版本信息。

        :return: The engine_minor_version of this ShowInstanceVersionResponse.
        :rtype: str
        """
        return self._engine_minor_version

    @engine_minor_version.setter
    def engine_minor_version(self, engine_minor_version):
        r"""Sets the engine_minor_version of this ShowInstanceVersionResponse.

        当前实例内核小版本信息。

        :param engine_minor_version: The engine_minor_version of this ShowInstanceVersionResponse.
        :type engine_minor_version: str
        """
        self._engine_minor_version = engine_minor_version

    @property
    def latest_engine_minor_version(self):
        r"""Gets the latest_engine_minor_version of this ShowInstanceVersionResponse.

        DCS实例最新的内核小版本信息。

        :return: The latest_engine_minor_version of this ShowInstanceVersionResponse.
        :rtype: str
        """
        return self._latest_engine_minor_version

    @latest_engine_minor_version.setter
    def latest_engine_minor_version(self, latest_engine_minor_version):
        r"""Sets the latest_engine_minor_version of this ShowInstanceVersionResponse.

        DCS实例最新的内核小版本信息。

        :param latest_engine_minor_version: The latest_engine_minor_version of this ShowInstanceVersionResponse.
        :type latest_engine_minor_version: str
        """
        self._latest_engine_minor_version = latest_engine_minor_version

    @property
    def proxy_minor_version(self):
        r"""Gets the proxy_minor_version of this ShowInstanceVersionResponse.

        当前实例proxy代理节点版本信息。

        :return: The proxy_minor_version of this ShowInstanceVersionResponse.
        :rtype: str
        """
        return self._proxy_minor_version

    @proxy_minor_version.setter
    def proxy_minor_version(self, proxy_minor_version):
        r"""Sets the proxy_minor_version of this ShowInstanceVersionResponse.

        当前实例proxy代理节点版本信息。

        :param proxy_minor_version: The proxy_minor_version of this ShowInstanceVersionResponse.
        :type proxy_minor_version: str
        """
        self._proxy_minor_version = proxy_minor_version

    @property
    def latest_proxy_minor_version(self):
        r"""Gets the latest_proxy_minor_version of this ShowInstanceVersionResponse.

        DCS实例最新的proxy代理节点版本信息。

        :return: The latest_proxy_minor_version of this ShowInstanceVersionResponse.
        :rtype: str
        """
        return self._latest_proxy_minor_version

    @latest_proxy_minor_version.setter
    def latest_proxy_minor_version(self, latest_proxy_minor_version):
        r"""Sets the latest_proxy_minor_version of this ShowInstanceVersionResponse.

        DCS实例最新的proxy代理节点版本信息。

        :param latest_proxy_minor_version: The latest_proxy_minor_version of this ShowInstanceVersionResponse.
        :type latest_proxy_minor_version: str
        """
        self._latest_proxy_minor_version = latest_proxy_minor_version

    @property
    def engine_minor_version_upgradable(self):
        r"""Gets the engine_minor_version_upgradable of this ShowInstanceVersionResponse.

        当前实例内核是否可以升级。

        :return: The engine_minor_version_upgradable of this ShowInstanceVersionResponse.
        :rtype: bool
        """
        return self._engine_minor_version_upgradable

    @engine_minor_version_upgradable.setter
    def engine_minor_version_upgradable(self, engine_minor_version_upgradable):
        r"""Sets the engine_minor_version_upgradable of this ShowInstanceVersionResponse.

        当前实例内核是否可以升级。

        :param engine_minor_version_upgradable: The engine_minor_version_upgradable of this ShowInstanceVersionResponse.
        :type engine_minor_version_upgradable: bool
        """
        self._engine_minor_version_upgradable = engine_minor_version_upgradable

    @property
    def proxy_minor_version_upgradable(self):
        r"""Gets the proxy_minor_version_upgradable of this ShowInstanceVersionResponse.

        当前实例proxy代理节点是否可以升级。

        :return: The proxy_minor_version_upgradable of this ShowInstanceVersionResponse.
        :rtype: bool
        """
        return self._proxy_minor_version_upgradable

    @proxy_minor_version_upgradable.setter
    def proxy_minor_version_upgradable(self, proxy_minor_version_upgradable):
        r"""Sets the proxy_minor_version_upgradable of this ShowInstanceVersionResponse.

        当前实例proxy代理节点是否可以升级。

        :param proxy_minor_version_upgradable: The proxy_minor_version_upgradable of this ShowInstanceVersionResponse.
        :type proxy_minor_version_upgradable: bool
        """
        self._proxy_minor_version_upgradable = proxy_minor_version_upgradable

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
        if not isinstance(other, ShowInstanceVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
