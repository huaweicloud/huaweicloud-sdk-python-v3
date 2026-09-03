# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtocolTestVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'http': 'HttpVo',
        'ping': 'list[PingVo]',
        'point_host': 'list[str]',
        'protocol': 'str'
    }

    attribute_map = {
        'http': 'http',
        'ping': 'ping',
        'point_host': 'point_host',
        'protocol': 'protocol'
    }

    def __init__(self, http=None, ping=None, point_host=None, protocol=None):
        r"""ProtocolTestVo

        The model defined in huaweicloud sdk

        :param http: 
        :type http: :class:`huaweicloudsdkcloudtest.v1.HttpVo`
        :param ping: ping拨测任务信息
        :type ping: list[:class:`huaweicloudsdkcloudtest.v1.PingVo`]
        :param point_host: ping/http节点地址
        :type point_host: list[str]
        :param protocol: 协议
        :type protocol: str
        """
        
        

        self._http = None
        self._ping = None
        self._point_host = None
        self._protocol = None
        self.discriminator = None

        if http is not None:
            self.http = http
        if ping is not None:
            self.ping = ping
        if point_host is not None:
            self.point_host = point_host
        if protocol is not None:
            self.protocol = protocol

    @property
    def http(self):
        r"""Gets the http of this ProtocolTestVo.

        :return: The http of this ProtocolTestVo.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.HttpVo`
        """
        return self._http

    @http.setter
    def http(self, http):
        r"""Sets the http of this ProtocolTestVo.

        :param http: The http of this ProtocolTestVo.
        :type http: :class:`huaweicloudsdkcloudtest.v1.HttpVo`
        """
        self._http = http

    @property
    def ping(self):
        r"""Gets the ping of this ProtocolTestVo.

        ping拨测任务信息

        :return: The ping of this ProtocolTestVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.PingVo`]
        """
        return self._ping

    @ping.setter
    def ping(self, ping):
        r"""Sets the ping of this ProtocolTestVo.

        ping拨测任务信息

        :param ping: The ping of this ProtocolTestVo.
        :type ping: list[:class:`huaweicloudsdkcloudtest.v1.PingVo`]
        """
        self._ping = ping

    @property
    def point_host(self):
        r"""Gets the point_host of this ProtocolTestVo.

        ping/http节点地址

        :return: The point_host of this ProtocolTestVo.
        :rtype: list[str]
        """
        return self._point_host

    @point_host.setter
    def point_host(self, point_host):
        r"""Sets the point_host of this ProtocolTestVo.

        ping/http节点地址

        :param point_host: The point_host of this ProtocolTestVo.
        :type point_host: list[str]
        """
        self._point_host = point_host

    @property
    def protocol(self):
        r"""Gets the protocol of this ProtocolTestVo.

        协议

        :return: The protocol of this ProtocolTestVo.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ProtocolTestVo.

        协议

        :param protocol: The protocol of this ProtocolTestVo.
        :type protocol: str
        """
        self._protocol = protocol

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
        if not isinstance(other, ProtocolTestVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
