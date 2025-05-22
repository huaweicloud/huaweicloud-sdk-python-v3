# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateEndpointResponse:

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
        'domain_name': 'str',
        'domain_name_suffix': 'str',
        'zone_name': 'str',
        'domain_name_ttl': 'int',
        'domain_name_status': 'str',
        'elb_ip': 'str',
        'bind_manage_ip_status': 'int'
    }

    attribute_map = {
        'ip': 'ip',
        'port': 'port',
        'domain_name': 'domain_name',
        'domain_name_suffix': 'domain_name_suffix',
        'zone_name': 'zone_name',
        'domain_name_ttl': 'domain_name_ttl',
        'domain_name_status': 'domain_name_status',
        'elb_ip': 'elb_ip',
        'bind_manage_ip_status': 'bind_manage_ip_status'
    }

    def __init__(self, ip=None, port=None, domain_name=None, domain_name_suffix=None, zone_name=None, domain_name_ttl=None, domain_name_status=None, elb_ip=None, bind_manage_ip_status=None):
        r"""PrivateEndpointResponse

        The model defined in huaweicloud sdk

        :param ip: **参数解释**： 内网IP信息，多个IP逗号分割。 **取值范围**： 不涉及。
        :type ip: str
        :param port: **参数解释**： 端口信息。 **取值范围**： 8000~30000
        :type port: int
        :param domain_name: **参数解释**： 子域名前缀。 **取值范围**： 不涉及。
        :type domain_name: str
        :param domain_name_suffix: **参数解释**： 子域名后缀。 **取值范围**： 不涉及。
        :type domain_name_suffix: str
        :param zone_name: **参数解释**： 子域名信息。 **取值范围**： 不涉及。
        :type zone_name: str
        :param domain_name_ttl: **参数解释**： 内网域名TTL。 **取值范围**： 不涉及。
        :type domain_name_ttl: int
        :param domain_name_status: **参数解释**： 内网域名状态。 **取值范围**： 不涉及。
        :type domain_name_status: str
        :param elb_ip: **参数解释**： ELB的内网IP信息。 **取值范围**： 不涉及。
        :type elb_ip: str
        :param bind_manage_ip_status: **参数解释**： IP绑定状态。 **取值范围**： 不涉及。
        :type bind_manage_ip_status: int
        """
        
        

        self._ip = None
        self._port = None
        self._domain_name = None
        self._domain_name_suffix = None
        self._zone_name = None
        self._domain_name_ttl = None
        self._domain_name_status = None
        self._elb_ip = None
        self._bind_manage_ip_status = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
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
        if elb_ip is not None:
            self.elb_ip = elb_ip
        if bind_manage_ip_status is not None:
            self.bind_manage_ip_status = bind_manage_ip_status

    @property
    def ip(self):
        r"""Gets the ip of this PrivateEndpointResponse.

        **参数解释**： 内网IP信息，多个IP逗号分割。 **取值范围**： 不涉及。

        :return: The ip of this PrivateEndpointResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this PrivateEndpointResponse.

        **参数解释**： 内网IP信息，多个IP逗号分割。 **取值范围**： 不涉及。

        :param ip: The ip of this PrivateEndpointResponse.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this PrivateEndpointResponse.

        **参数解释**： 端口信息。 **取值范围**： 8000~30000

        :return: The port of this PrivateEndpointResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this PrivateEndpointResponse.

        **参数解释**： 端口信息。 **取值范围**： 8000~30000

        :param port: The port of this PrivateEndpointResponse.
        :type port: int
        """
        self._port = port

    @property
    def domain_name(self):
        r"""Gets the domain_name of this PrivateEndpointResponse.

        **参数解释**： 子域名前缀。 **取值范围**： 不涉及。

        :return: The domain_name of this PrivateEndpointResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this PrivateEndpointResponse.

        **参数解释**： 子域名前缀。 **取值范围**： 不涉及。

        :param domain_name: The domain_name of this PrivateEndpointResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_name_suffix(self):
        r"""Gets the domain_name_suffix of this PrivateEndpointResponse.

        **参数解释**： 子域名后缀。 **取值范围**： 不涉及。

        :return: The domain_name_suffix of this PrivateEndpointResponse.
        :rtype: str
        """
        return self._domain_name_suffix

    @domain_name_suffix.setter
    def domain_name_suffix(self, domain_name_suffix):
        r"""Sets the domain_name_suffix of this PrivateEndpointResponse.

        **参数解释**： 子域名后缀。 **取值范围**： 不涉及。

        :param domain_name_suffix: The domain_name_suffix of this PrivateEndpointResponse.
        :type domain_name_suffix: str
        """
        self._domain_name_suffix = domain_name_suffix

    @property
    def zone_name(self):
        r"""Gets the zone_name of this PrivateEndpointResponse.

        **参数解释**： 子域名信息。 **取值范围**： 不涉及。

        :return: The zone_name of this PrivateEndpointResponse.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        r"""Sets the zone_name of this PrivateEndpointResponse.

        **参数解释**： 子域名信息。 **取值范围**： 不涉及。

        :param zone_name: The zone_name of this PrivateEndpointResponse.
        :type zone_name: str
        """
        self._zone_name = zone_name

    @property
    def domain_name_ttl(self):
        r"""Gets the domain_name_ttl of this PrivateEndpointResponse.

        **参数解释**： 内网域名TTL。 **取值范围**： 不涉及。

        :return: The domain_name_ttl of this PrivateEndpointResponse.
        :rtype: int
        """
        return self._domain_name_ttl

    @domain_name_ttl.setter
    def domain_name_ttl(self, domain_name_ttl):
        r"""Sets the domain_name_ttl of this PrivateEndpointResponse.

        **参数解释**： 内网域名TTL。 **取值范围**： 不涉及。

        :param domain_name_ttl: The domain_name_ttl of this PrivateEndpointResponse.
        :type domain_name_ttl: int
        """
        self._domain_name_ttl = domain_name_ttl

    @property
    def domain_name_status(self):
        r"""Gets the domain_name_status of this PrivateEndpointResponse.

        **参数解释**： 内网域名状态。 **取值范围**： 不涉及。

        :return: The domain_name_status of this PrivateEndpointResponse.
        :rtype: str
        """
        return self._domain_name_status

    @domain_name_status.setter
    def domain_name_status(self, domain_name_status):
        r"""Sets the domain_name_status of this PrivateEndpointResponse.

        **参数解释**： 内网域名状态。 **取值范围**： 不涉及。

        :param domain_name_status: The domain_name_status of this PrivateEndpointResponse.
        :type domain_name_status: str
        """
        self._domain_name_status = domain_name_status

    @property
    def elb_ip(self):
        r"""Gets the elb_ip of this PrivateEndpointResponse.

        **参数解释**： ELB的内网IP信息。 **取值范围**： 不涉及。

        :return: The elb_ip of this PrivateEndpointResponse.
        :rtype: str
        """
        return self._elb_ip

    @elb_ip.setter
    def elb_ip(self, elb_ip):
        r"""Sets the elb_ip of this PrivateEndpointResponse.

        **参数解释**： ELB的内网IP信息。 **取值范围**： 不涉及。

        :param elb_ip: The elb_ip of this PrivateEndpointResponse.
        :type elb_ip: str
        """
        self._elb_ip = elb_ip

    @property
    def bind_manage_ip_status(self):
        r"""Gets the bind_manage_ip_status of this PrivateEndpointResponse.

        **参数解释**： IP绑定状态。 **取值范围**： 不涉及。

        :return: The bind_manage_ip_status of this PrivateEndpointResponse.
        :rtype: int
        """
        return self._bind_manage_ip_status

    @bind_manage_ip_status.setter
    def bind_manage_ip_status(self, bind_manage_ip_status):
        r"""Sets the bind_manage_ip_status of this PrivateEndpointResponse.

        **参数解释**： IP绑定状态。 **取值范围**： 不涉及。

        :param bind_manage_ip_status: The bind_manage_ip_status of this PrivateEndpointResponse.
        :type bind_manage_ip_status: int
        """
        self._bind_manage_ip_status = bind_manage_ip_status

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
        if not isinstance(other, PrivateEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
