# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicEndpointResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip': 'str',
        'port': 'int',
        'enabled': 'bool',
        'ip_id': 'str',
        'ip_bandwidth': 'str',
        'domain_name': 'str',
        'domain_name_suffix': 'str',
        'zone_name': 'str',
        'domain_name_ttl': 'int',
        'domain_name_status': 'str',
        'ip_status': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'enabled': 'enabled',
        'ip_id': 'ip_id',
        'ip_bandwidth': 'ip_bandwidth',
        'domain_name': 'domain_name',
        'domain_name_suffix': 'domain_name_suffix',
        'zone_name': 'zone_name',
        'domain_name_ttl': 'domain_name_ttl',
        'domain_name_status': 'domain_name_status',
        'ip_status': 'ip_status'
    }

    def __init__(self, ip=None, port=None, enabled=None, ip_id=None, ip_bandwidth=None, domain_name=None, domain_name_suffix=None, zone_name=None, domain_name_ttl=None, domain_name_status=None, ip_status=None):
        r"""PublicEndpointResponse

        The model defined in huaweicloud sdk

        :param ip: **参数解释**： 公网IP信息。 **取值范围**： 不涉及。
        :type ip: str
        :param port: **参数解释**： 端口信息，创建集群时如果未指定端口则默认8000。 **取值范围**： 不涉及。
        :type port: int
        :param enabled: **参数解释**： 当前局点是否支持公网域名。 **取值范围**： 不涉及。
        :type enabled: bool
        :param ip_id: **参数解释**： 公网IP的ID。 **取值范围**： 不涉及。
        :type ip_id: str
        :param ip_bandwidth: **参数解释**： 公网IP的带宽信息。 **取值范围**： 不涉及。
        :type ip_bandwidth: str
        :param domain_name: **参数解释**： 公网域名子域名信息。 **取值范围**： 不涉及。
        :type domain_name: str
        :param domain_name_suffix: **参数解释**： 公网域名后缀信息。 **取值范围**： 不涉及。
        :type domain_name_suffix: str
        :param zone_name: **参数解释**： 公网域名后缀信息。 **取值范围**： 不涉及。
        :type zone_name: str
        :param domain_name_ttl: **参数解释**： 公网域名TTL。 **取值范围**： 不涉及。
        :type domain_name_ttl: int
        :param domain_name_status: **参数解释**： 公网域名状态。 **取值范围**： 不涉及。
        :type domain_name_status: str
        :param ip_status: **参数解释**： 公网IP状态。 **取值范围**： 不涉及。
        :type ip_status: str
        """
        
        

        self._ip = None
        self._port = None
        self._enabled = None
        self._ip_id = None
        self._ip_bandwidth = None
        self._domain_name = None
        self._domain_name_suffix = None
        self._zone_name = None
        self._domain_name_ttl = None
        self._domain_name_status = None
        self._ip_status = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if enabled is not None:
            self.enabled = enabled
        if ip_id is not None:
            self.ip_id = ip_id
        if ip_bandwidth is not None:
            self.ip_bandwidth = ip_bandwidth
        if domain_name is not None:
            self.domain_name = domain_name
        if domain_name_suffix is not None:
            self.domain_name_suffix = domain_name_suffix
        if zone_name is not None:
            self.zone_name = zone_name
        if domain_name_ttl is not None:
            self.domain_name_ttl = domain_name_ttl
        if domain_name_status is not None:
            self.domain_name_status = domain_name_status
        if ip_status is not None:
            self.ip_status = ip_status

    @property
    def ip(self):
        r"""Gets the ip of this PublicEndpointResponse.

        **参数解释**： 公网IP信息。 **取值范围**： 不涉及。

        :return: The ip of this PublicEndpointResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this PublicEndpointResponse.

        **参数解释**： 公网IP信息。 **取值范围**： 不涉及。

        :param ip: The ip of this PublicEndpointResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this PublicEndpointResponse.

        **参数解释**： 端口信息，创建集群时如果未指定端口则默认8000。 **取值范围**： 不涉及。

        :return: The port of this PublicEndpointResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this PublicEndpointResponse.

        **参数解释**： 端口信息，创建集群时如果未指定端口则默认8000。 **取值范围**： 不涉及。

        :param port: The port of this PublicEndpointResponse.
        :type port: int
        """
        self._port = port

    @property
    def enabled(self):
        r"""Gets the enabled of this PublicEndpointResponse.

        **参数解释**： 当前局点是否支持公网域名。 **取值范围**： 不涉及。

        :return: The enabled of this PublicEndpointResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this PublicEndpointResponse.

        **参数解释**： 当前局点是否支持公网域名。 **取值范围**： 不涉及。

        :param enabled: The enabled of this PublicEndpointResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def ip_id(self):
        r"""Gets the ip_id of this PublicEndpointResponse.

        **参数解释**： 公网IP的ID。 **取值范围**： 不涉及。

        :return: The ip_id of this PublicEndpointResponse.
        :rtype: str
        """
        return self._ip_id

    @ip_id.setter
    def ip_id(self, ip_id):
        r"""Sets the ip_id of this PublicEndpointResponse.

        **参数解释**： 公网IP的ID。 **取值范围**： 不涉及。

        :param ip_id: The ip_id of this PublicEndpointResponse.
        :type ip_id: str
        """
        self._ip_id = ip_id

    @property
    def ip_bandwidth(self):
        r"""Gets the ip_bandwidth of this PublicEndpointResponse.

        **参数解释**： 公网IP的带宽信息。 **取值范围**： 不涉及。

        :return: The ip_bandwidth of this PublicEndpointResponse.
        :rtype: str
        """
        return self._ip_bandwidth

    @ip_bandwidth.setter
    def ip_bandwidth(self, ip_bandwidth):
        r"""Sets the ip_bandwidth of this PublicEndpointResponse.

        **参数解释**： 公网IP的带宽信息。 **取值范围**： 不涉及。

        :param ip_bandwidth: The ip_bandwidth of this PublicEndpointResponse.
        :type ip_bandwidth: str
        """
        self._ip_bandwidth = ip_bandwidth

    @property
    def domain_name(self):
        r"""Gets the domain_name of this PublicEndpointResponse.

        **参数解释**： 公网域名子域名信息。 **取值范围**： 不涉及。

        :return: The domain_name of this PublicEndpointResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this PublicEndpointResponse.

        **参数解释**： 公网域名子域名信息。 **取值范围**： 不涉及。

        :param domain_name: The domain_name of this PublicEndpointResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_name_suffix(self):
        r"""Gets the domain_name_suffix of this PublicEndpointResponse.

        **参数解释**： 公网域名后缀信息。 **取值范围**： 不涉及。

        :return: The domain_name_suffix of this PublicEndpointResponse.
        :rtype: str
        """
        return self._domain_name_suffix

    @domain_name_suffix.setter
    def domain_name_suffix(self, domain_name_suffix):
        r"""Sets the domain_name_suffix of this PublicEndpointResponse.

        **参数解释**： 公网域名后缀信息。 **取值范围**： 不涉及。

        :param domain_name_suffix: The domain_name_suffix of this PublicEndpointResponse.
        :type domain_name_suffix: str
        """
        self._domain_name_suffix = domain_name_suffix

    @property
    def zone_name(self):
        r"""Gets the zone_name of this PublicEndpointResponse.

        **参数解释**： 公网域名后缀信息。 **取值范围**： 不涉及。

        :return: The zone_name of this PublicEndpointResponse.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this PublicEndpointResponse.

        **参数解释**： 公网域名后缀信息。 **取值范围**： 不涉及。

        :param zone_name: The zone_name of this PublicEndpointResponse.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def domain_name_ttl(self):
        r"""Gets the domain_name_ttl of this PublicEndpointResponse.

        **参数解释**： 公网域名TTL。 **取值范围**： 不涉及。

        :return: The domain_name_ttl of this PublicEndpointResponse.
        :rtype: int
        """
        return self._domain_name_ttl

    @domain_name_ttl.setter
    def domain_name_ttl(self, domain_name_ttl):
        r"""Sets the domain_name_ttl of this PublicEndpointResponse.

        **参数解释**： 公网域名TTL。 **取值范围**： 不涉及。

        :param domain_name_ttl: The domain_name_ttl of this PublicEndpointResponse.
        :type domain_name_ttl: int
        """
        self._domain_name_ttl = domain_name_ttl

    @property
    def domain_name_status(self):
        r"""Gets the domain_name_status of this PublicEndpointResponse.

        **参数解释**： 公网域名状态。 **取值范围**： 不涉及。

        :return: The domain_name_status of this PublicEndpointResponse.
        :rtype: str
        """
        return self._domain_name_status

    @domain_name_status.setter
    def domain_name_status(self, domain_name_status):
        r"""Sets the domain_name_status of this PublicEndpointResponse.

        **参数解释**： 公网域名状态。 **取值范围**： 不涉及。

        :param domain_name_status: The domain_name_status of this PublicEndpointResponse.
        :type domain_name_status: str
        """
        self._domain_name_status = domain_name_status

    @property
    def ip_status(self):
        r"""Gets the ip_status of this PublicEndpointResponse.

        **参数解释**： 公网IP状态。 **取值范围**： 不涉及。

        :return: The ip_status of this PublicEndpointResponse.
        :rtype: str
        """
        return self._ip_status

    @ip_status.setter
    def ip_status(self, ip_status):
        r"""Sets the ip_status of this PublicEndpointResponse.

        **参数解释**： 公网IP状态。 **取值范围**： 不涉及。

        :param ip_status: The ip_status of this PublicEndpointResponse.
        :type ip_status: str
        """
        self._ip_status = ip_status

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
        if not isinstance(other, PublicEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
