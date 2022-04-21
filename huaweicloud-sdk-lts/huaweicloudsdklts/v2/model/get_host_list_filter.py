# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHostListFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'host_name_list': 'list[str]',
        'host_ip_list': 'list[str]',
        'host_status': 'str',
        'host_version': 'str'
    }

    attribute_map = {
        'host_name_list': 'host_name_list',
        'host_ip_list': 'host_ip_list',
        'host_status': 'host_status',
        'host_version': 'host_version'
    }

    def __init__(self, host_name_list=None, host_ip_list=None, host_status=None, host_version=None):
        """GetHostListFilter

        The model defined in huaweicloud sdk

        :param host_name_list: 主机名称列表。可以根据主机名称列表，进行批量过滤。
        :type host_name_list: list[str]
        :param host_ip_list: 主机ID列表。可以根据主机IP列表，进行批量过滤。
        :type host_ip_list: list[str]
        :param host_status: 主机状态。可以根据主机状态进行过滤。 uninstall:未安装 running:运行 offline:离线 error:异常 plugin error:插件错误 installing:安装中 install-fail:安装失败 upgrading:升级中 upgrading-transient:升级中 upgrade failed:升级失败 upgrade-fail:升级失败 uninstalling:卸载中 uninstalling-transient:卸载中 authentication error:鉴权失败
        :type host_status: str
        :param host_version: 主机版本。可以根据主机版本进行过滤。
        :type host_version: str
        """
        
        

        self._host_name_list = None
        self._host_ip_list = None
        self._host_status = None
        self._host_version = None
        self.discriminator = None

        if host_name_list is not None:
            self.host_name_list = host_name_list
        if host_ip_list is not None:
            self.host_ip_list = host_ip_list
        if host_status is not None:
            self.host_status = host_status
        if host_version is not None:
            self.host_version = host_version

    @property
    def host_name_list(self):
        """Gets the host_name_list of this GetHostListFilter.

        主机名称列表。可以根据主机名称列表，进行批量过滤。

        :return: The host_name_list of this GetHostListFilter.
        :rtype: list[str]
        """
        return self._host_name_list

    @host_name_list.setter
    def host_name_list(self, host_name_list):
        """Sets the host_name_list of this GetHostListFilter.

        主机名称列表。可以根据主机名称列表，进行批量过滤。

        :param host_name_list: The host_name_list of this GetHostListFilter.
        :type host_name_list: list[str]
        """
        self._host_name_list = host_name_list

    @property
    def host_ip_list(self):
        """Gets the host_ip_list of this GetHostListFilter.

        主机ID列表。可以根据主机IP列表，进行批量过滤。

        :return: The host_ip_list of this GetHostListFilter.
        :rtype: list[str]
        """
        return self._host_ip_list

    @host_ip_list.setter
    def host_ip_list(self, host_ip_list):
        """Sets the host_ip_list of this GetHostListFilter.

        主机ID列表。可以根据主机IP列表，进行批量过滤。

        :param host_ip_list: The host_ip_list of this GetHostListFilter.
        :type host_ip_list: list[str]
        """
        self._host_ip_list = host_ip_list

    @property
    def host_status(self):
        """Gets the host_status of this GetHostListFilter.

        主机状态。可以根据主机状态进行过滤。 uninstall:未安装 running:运行 offline:离线 error:异常 plugin error:插件错误 installing:安装中 install-fail:安装失败 upgrading:升级中 upgrading-transient:升级中 upgrade failed:升级失败 upgrade-fail:升级失败 uninstalling:卸载中 uninstalling-transient:卸载中 authentication error:鉴权失败

        :return: The host_status of this GetHostListFilter.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this GetHostListFilter.

        主机状态。可以根据主机状态进行过滤。 uninstall:未安装 running:运行 offline:离线 error:异常 plugin error:插件错误 installing:安装中 install-fail:安装失败 upgrading:升级中 upgrading-transient:升级中 upgrade failed:升级失败 upgrade-fail:升级失败 uninstalling:卸载中 uninstalling-transient:卸载中 authentication error:鉴权失败

        :param host_status: The host_status of this GetHostListFilter.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def host_version(self):
        """Gets the host_version of this GetHostListFilter.

        主机版本。可以根据主机版本进行过滤。

        :return: The host_version of this GetHostListFilter.
        :rtype: str
        """
        return self._host_version

    @host_version.setter
    def host_version(self, host_version):
        """Sets the host_version of this GetHostListFilter.

        主机版本。可以根据主机版本进行过滤。

        :param host_version: The host_version of this GetHostListFilter.
        :type host_version: str
        """
        self._host_version = host_version

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
        if not isinstance(other, GetHostListFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
