# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectionMonitorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vpn_connection_id': 'str',
        'type': 'str',
        'source_ip': 'str',
        'destination_ip': 'str',
        'proto_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'vpn_connection_id': 'vpn_connection_id',
        'type': 'type',
        'source_ip': 'source_ip',
        'destination_ip': 'destination_ip',
        'proto_type': 'proto_type'
    }

    def __init__(self, id=None, vpn_connection_id=None, type=None, source_ip=None, destination_ip=None, proto_type=None):
        """CreateConnectionMonitorInfo

        The model defined in huaweicloud sdk

        :param id: VPN连接监控ID
        :type id: str
        :param vpn_connection_id: VPN连接监控对应的VPN连接ID
        :type vpn_connection_id: str
        :param type: 网关连通性，取值范围：gateway
        :type type: str
        :param source_ip: VPN连接监控的源地址
        :type source_ip: str
        :param destination_ip: VPN连接监控的目的地址
        :type destination_ip: str
        :param proto_type: 预留字段，nqa使用的协议类型，目前使用默认值ICMP
        :type proto_type: str
        """
        
        

        self._id = None
        self._vpn_connection_id = None
        self._type = None
        self._source_ip = None
        self._destination_ip = None
        self._proto_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vpn_connection_id is not None:
            self.vpn_connection_id = vpn_connection_id
        if type is not None:
            self.type = type
        if source_ip is not None:
            self.source_ip = source_ip
        if destination_ip is not None:
            self.destination_ip = destination_ip
        if proto_type is not None:
            self.proto_type = proto_type

    @property
    def id(self):
        """Gets the id of this CreateConnectionMonitorInfo.

        VPN连接监控ID

        :return: The id of this CreateConnectionMonitorInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateConnectionMonitorInfo.

        VPN连接监控ID

        :param id: The id of this CreateConnectionMonitorInfo.
        :type id: str
        """
        self._id = id

    @property
    def vpn_connection_id(self):
        """Gets the vpn_connection_id of this CreateConnectionMonitorInfo.

        VPN连接监控对应的VPN连接ID

        :return: The vpn_connection_id of this CreateConnectionMonitorInfo.
        :rtype: str
        """
        return self._vpn_connection_id

    @vpn_connection_id.setter
    def vpn_connection_id(self, vpn_connection_id):
        """Sets the vpn_connection_id of this CreateConnectionMonitorInfo.

        VPN连接监控对应的VPN连接ID

        :param vpn_connection_id: The vpn_connection_id of this CreateConnectionMonitorInfo.
        :type vpn_connection_id: str
        """
        self._vpn_connection_id = vpn_connection_id

    @property
    def type(self):
        """Gets the type of this CreateConnectionMonitorInfo.

        网关连通性，取值范围：gateway

        :return: The type of this CreateConnectionMonitorInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateConnectionMonitorInfo.

        网关连通性，取值范围：gateway

        :param type: The type of this CreateConnectionMonitorInfo.
        :type type: str
        """
        self._type = type

    @property
    def source_ip(self):
        """Gets the source_ip of this CreateConnectionMonitorInfo.

        VPN连接监控的源地址

        :return: The source_ip of this CreateConnectionMonitorInfo.
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this CreateConnectionMonitorInfo.

        VPN连接监控的源地址

        :param source_ip: The source_ip of this CreateConnectionMonitorInfo.
        :type source_ip: str
        """
        self._source_ip = source_ip

    @property
    def destination_ip(self):
        """Gets the destination_ip of this CreateConnectionMonitorInfo.

        VPN连接监控的目的地址

        :return: The destination_ip of this CreateConnectionMonitorInfo.
        :rtype: str
        """
        return self._destination_ip

    @destination_ip.setter
    def destination_ip(self, destination_ip):
        """Sets the destination_ip of this CreateConnectionMonitorInfo.

        VPN连接监控的目的地址

        :param destination_ip: The destination_ip of this CreateConnectionMonitorInfo.
        :type destination_ip: str
        """
        self._destination_ip = destination_ip

    @property
    def proto_type(self):
        """Gets the proto_type of this CreateConnectionMonitorInfo.

        预留字段，nqa使用的协议类型，目前使用默认值ICMP

        :return: The proto_type of this CreateConnectionMonitorInfo.
        :rtype: str
        """
        return self._proto_type

    @proto_type.setter
    def proto_type(self, proto_type):
        """Sets the proto_type of this CreateConnectionMonitorInfo.

        预留字段，nqa使用的协议类型，目前使用默认值ICMP

        :param proto_type: The proto_type of this CreateConnectionMonitorInfo.
        :type proto_type: str
        """
        self._proto_type = proto_type

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
        if not isinstance(other, CreateConnectionMonitorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
