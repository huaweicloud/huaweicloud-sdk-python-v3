# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'include_ip_ranges': 'str',
        'exclude_ip_ranges': 'str',
        'exclude_outbound_ports': 'str',
        'exclude_inbound_ports': 'str',
        'include_outbound_ports': 'str',
        'include_inbound_ports': 'str'
    }

    attribute_map = {
        'include_ip_ranges': 'includeIPRanges',
        'exclude_ip_ranges': 'excludeIPRanges',
        'exclude_outbound_ports': 'excludeOutboundPorts',
        'exclude_inbound_ports': 'excludeInboundPorts',
        'include_outbound_ports': 'includeOutboundPorts',
        'include_inbound_ports': 'includeInboundPorts'
    }

    def __init__(self, include_ip_ranges=None, exclude_ip_ranges=None, exclude_outbound_ports=None, exclude_inbound_ports=None, include_outbound_ports=None, include_inbound_ports=None):
        r"""ProxyConfig

        The model defined in huaweicloud sdk

        :param include_ip_ranges: 拦截对外访问的地址范围，以半角英文逗号（,）分隔的IP网段
        :type include_ip_ranges: str
        :param exclude_ip_ranges: 排除拦截对外访问的地址范围，以半角英文逗号（,）分隔的IP网段
        :type exclude_ip_ranges: str
        :param exclude_outbound_ports: 排除拦截对外访问端口，以半角英文逗号（,）分隔的出站端口列表
        :type exclude_outbound_ports: str
        :param exclude_inbound_ports: 排除拦截访问服务的端口，以半角英文逗号（,）分隔的入站端口列表
        :type exclude_inbound_ports: str
        :param include_outbound_ports: 拦截对外访问端口，以半角英文逗号（,）分隔的出站端口列表
        :type include_outbound_ports: str
        :param include_inbound_ports: 拦截访问服务的端口，以半角英文逗号（,）分隔的入站端口列表
        :type include_inbound_ports: str
        """
        
        

        self._include_ip_ranges = None
        self._exclude_ip_ranges = None
        self._exclude_outbound_ports = None
        self._exclude_inbound_ports = None
        self._include_outbound_ports = None
        self._include_inbound_ports = None
        self.discriminator = None

        if include_ip_ranges is not None:
            self.include_ip_ranges = include_ip_ranges
        if exclude_ip_ranges is not None:
            self.exclude_ip_ranges = exclude_ip_ranges
        if exclude_outbound_ports is not None:
            self.exclude_outbound_ports = exclude_outbound_ports
        if exclude_inbound_ports is not None:
            self.exclude_inbound_ports = exclude_inbound_ports
        if include_outbound_ports is not None:
            self.include_outbound_ports = include_outbound_ports
        if include_inbound_ports is not None:
            self.include_inbound_ports = include_inbound_ports

    @property
    def include_ip_ranges(self):
        r"""Gets the include_ip_ranges of this ProxyConfig.

        拦截对外访问的地址范围，以半角英文逗号（,）分隔的IP网段

        :return: The include_ip_ranges of this ProxyConfig.
        :rtype: str
        """
        return self._include_ip_ranges

    @include_ip_ranges.setter
    def include_ip_ranges(self, include_ip_ranges):
        r"""Sets the include_ip_ranges of this ProxyConfig.

        拦截对外访问的地址范围，以半角英文逗号（,）分隔的IP网段

        :param include_ip_ranges: The include_ip_ranges of this ProxyConfig.
        :type include_ip_ranges: str
        """
        self._include_ip_ranges = include_ip_ranges

    @property
    def exclude_ip_ranges(self):
        r"""Gets the exclude_ip_ranges of this ProxyConfig.

        排除拦截对外访问的地址范围，以半角英文逗号（,）分隔的IP网段

        :return: The exclude_ip_ranges of this ProxyConfig.
        :rtype: str
        """
        return self._exclude_ip_ranges

    @exclude_ip_ranges.setter
    def exclude_ip_ranges(self, exclude_ip_ranges):
        r"""Sets the exclude_ip_ranges of this ProxyConfig.

        排除拦截对外访问的地址范围，以半角英文逗号（,）分隔的IP网段

        :param exclude_ip_ranges: The exclude_ip_ranges of this ProxyConfig.
        :type exclude_ip_ranges: str
        """
        self._exclude_ip_ranges = exclude_ip_ranges

    @property
    def exclude_outbound_ports(self):
        r"""Gets the exclude_outbound_ports of this ProxyConfig.

        排除拦截对外访问端口，以半角英文逗号（,）分隔的出站端口列表

        :return: The exclude_outbound_ports of this ProxyConfig.
        :rtype: str
        """
        return self._exclude_outbound_ports

    @exclude_outbound_ports.setter
    def exclude_outbound_ports(self, exclude_outbound_ports):
        r"""Sets the exclude_outbound_ports of this ProxyConfig.

        排除拦截对外访问端口，以半角英文逗号（,）分隔的出站端口列表

        :param exclude_outbound_ports: The exclude_outbound_ports of this ProxyConfig.
        :type exclude_outbound_ports: str
        """
        self._exclude_outbound_ports = exclude_outbound_ports

    @property
    def exclude_inbound_ports(self):
        r"""Gets the exclude_inbound_ports of this ProxyConfig.

        排除拦截访问服务的端口，以半角英文逗号（,）分隔的入站端口列表

        :return: The exclude_inbound_ports of this ProxyConfig.
        :rtype: str
        """
        return self._exclude_inbound_ports

    @exclude_inbound_ports.setter
    def exclude_inbound_ports(self, exclude_inbound_ports):
        r"""Sets the exclude_inbound_ports of this ProxyConfig.

        排除拦截访问服务的端口，以半角英文逗号（,）分隔的入站端口列表

        :param exclude_inbound_ports: The exclude_inbound_ports of this ProxyConfig.
        :type exclude_inbound_ports: str
        """
        self._exclude_inbound_ports = exclude_inbound_ports

    @property
    def include_outbound_ports(self):
        r"""Gets the include_outbound_ports of this ProxyConfig.

        拦截对外访问端口，以半角英文逗号（,）分隔的出站端口列表

        :return: The include_outbound_ports of this ProxyConfig.
        :rtype: str
        """
        return self._include_outbound_ports

    @include_outbound_ports.setter
    def include_outbound_ports(self, include_outbound_ports):
        r"""Sets the include_outbound_ports of this ProxyConfig.

        拦截对外访问端口，以半角英文逗号（,）分隔的出站端口列表

        :param include_outbound_ports: The include_outbound_ports of this ProxyConfig.
        :type include_outbound_ports: str
        """
        self._include_outbound_ports = include_outbound_ports

    @property
    def include_inbound_ports(self):
        r"""Gets the include_inbound_ports of this ProxyConfig.

        拦截访问服务的端口，以半角英文逗号（,）分隔的入站端口列表

        :return: The include_inbound_ports of this ProxyConfig.
        :rtype: str
        """
        return self._include_inbound_ports

    @include_inbound_ports.setter
    def include_inbound_ports(self, include_inbound_ports):
        r"""Sets the include_inbound_ports of this ProxyConfig.

        拦截访问服务的端口，以半角英文逗号（,）分隔的入站端口列表

        :param include_inbound_ports: The include_inbound_ports of this ProxyConfig.
        :type include_inbound_ports: str
        """
        self._include_inbound_ports = include_inbound_ports

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
        if not isinstance(other, ProxyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
