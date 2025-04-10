# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpnGatewayRoutingTableEntryVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination': 'str',
        'nexthop': 'str',
        'outbound_interface_ip': 'str',
        'origin': 'str',
        'as_path': 'str',
        'med': 'int',
        'nexthop_resource': 'NexthopResourceVo'
    }

    attribute_map = {
        'destination': 'destination',
        'nexthop': 'nexthop',
        'outbound_interface_ip': 'outbound_interface_ip',
        'origin': 'origin',
        'as_path': 'as_path',
        'med': 'med',
        'nexthop_resource': 'nexthop_resource'
    }

    def __init__(self, destination=None, nexthop=None, outbound_interface_ip=None, origin=None, as_path=None, med=None, nexthop_resource=None):
        r"""VpnGatewayRoutingTableEntryVo

        The model defined in huaweicloud sdk

        :param destination: 目的地址
        :type destination: str
        :param nexthop: 下一跳地址
        :type nexthop: str
        :param outbound_interface_ip: 出接口地址
        :type outbound_interface_ip: str
        :param origin: BGP路由来源
        :type origin: str
        :param as_path: BGP路由的AS路径
        :type as_path: str
        :param med: BGP路由的MED值
        :type med: int
        :param nexthop_resource: 
        :type nexthop_resource: :class:`huaweicloudsdkvpn.v5.NexthopResourceVo`
        """
        
        

        self._destination = None
        self._nexthop = None
        self._outbound_interface_ip = None
        self._origin = None
        self._as_path = None
        self._med = None
        self._nexthop_resource = None
        self.discriminator = None

        if destination is not None:
            self.destination = destination
        if nexthop is not None:
            self.nexthop = nexthop
        if outbound_interface_ip is not None:
            self.outbound_interface_ip = outbound_interface_ip
        if origin is not None:
            self.origin = origin
        if as_path is not None:
            self.as_path = as_path
        if med is not None:
            self.med = med
        if nexthop_resource is not None:
            self.nexthop_resource = nexthop_resource

    @property
    def destination(self):
        r"""Gets the destination of this VpnGatewayRoutingTableEntryVo.

        目的地址

        :return: The destination of this VpnGatewayRoutingTableEntryVo.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this VpnGatewayRoutingTableEntryVo.

        目的地址

        :param destination: The destination of this VpnGatewayRoutingTableEntryVo.
        :type destination: str
        """
        self._destination = destination

    @property
    def nexthop(self):
        r"""Gets the nexthop of this VpnGatewayRoutingTableEntryVo.

        下一跳地址

        :return: The nexthop of this VpnGatewayRoutingTableEntryVo.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        r"""Sets the nexthop of this VpnGatewayRoutingTableEntryVo.

        下一跳地址

        :param nexthop: The nexthop of this VpnGatewayRoutingTableEntryVo.
        :type nexthop: str
        """
        self._nexthop = nexthop

    @property
    def outbound_interface_ip(self):
        r"""Gets the outbound_interface_ip of this VpnGatewayRoutingTableEntryVo.

        出接口地址

        :return: The outbound_interface_ip of this VpnGatewayRoutingTableEntryVo.
        :rtype: str
        """
        return self._outbound_interface_ip

    @outbound_interface_ip.setter
    def outbound_interface_ip(self, outbound_interface_ip):
        r"""Sets the outbound_interface_ip of this VpnGatewayRoutingTableEntryVo.

        出接口地址

        :param outbound_interface_ip: The outbound_interface_ip of this VpnGatewayRoutingTableEntryVo.
        :type outbound_interface_ip: str
        """
        self._outbound_interface_ip = outbound_interface_ip

    @property
    def origin(self):
        r"""Gets the origin of this VpnGatewayRoutingTableEntryVo.

        BGP路由来源

        :return: The origin of this VpnGatewayRoutingTableEntryVo.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        r"""Sets the origin of this VpnGatewayRoutingTableEntryVo.

        BGP路由来源

        :param origin: The origin of this VpnGatewayRoutingTableEntryVo.
        :type origin: str
        """
        self._origin = origin

    @property
    def as_path(self):
        r"""Gets the as_path of this VpnGatewayRoutingTableEntryVo.

        BGP路由的AS路径

        :return: The as_path of this VpnGatewayRoutingTableEntryVo.
        :rtype: str
        """
        return self._as_path

    @as_path.setter
    def as_path(self, as_path):
        r"""Sets the as_path of this VpnGatewayRoutingTableEntryVo.

        BGP路由的AS路径

        :param as_path: The as_path of this VpnGatewayRoutingTableEntryVo.
        :type as_path: str
        """
        self._as_path = as_path

    @property
    def med(self):
        r"""Gets the med of this VpnGatewayRoutingTableEntryVo.

        BGP路由的MED值

        :return: The med of this VpnGatewayRoutingTableEntryVo.
        :rtype: int
        """
        return self._med

    @med.setter
    def med(self, med):
        r"""Sets the med of this VpnGatewayRoutingTableEntryVo.

        BGP路由的MED值

        :param med: The med of this VpnGatewayRoutingTableEntryVo.
        :type med: int
        """
        self._med = med

    @property
    def nexthop_resource(self):
        r"""Gets the nexthop_resource of this VpnGatewayRoutingTableEntryVo.

        :return: The nexthop_resource of this VpnGatewayRoutingTableEntryVo.
        :rtype: :class:`huaweicloudsdkvpn.v5.NexthopResourceVo`
        """
        return self._nexthop_resource

    @nexthop_resource.setter
    def nexthop_resource(self, nexthop_resource):
        r"""Sets the nexthop_resource of this VpnGatewayRoutingTableEntryVo.

        :param nexthop_resource: The nexthop_resource of this VpnGatewayRoutingTableEntryVo.
        :type nexthop_resource: :class:`huaweicloudsdkvpn.v5.NexthopResourceVo`
        """
        self._nexthop_resource = nexthop_resource

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
        if not isinstance(other, VpnGatewayRoutingTableEntryVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
