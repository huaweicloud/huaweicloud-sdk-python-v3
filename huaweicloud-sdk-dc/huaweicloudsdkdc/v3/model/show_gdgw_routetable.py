# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGdgwRoutetable:

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
        'tenant_id': 'str',
        'gateway_id': 'str',
        'destination': 'str',
        'nexthop': 'str',
        'obtain_mode': 'str',
        'status': 'str',
        'address_family': 'AddressFamily',
        'description': 'str',
        'type': 'RouteTypeOfGdgw'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'gateway_id': 'gateway_id',
        'destination': 'destination',
        'nexthop': 'nexthop',
        'obtain_mode': 'obtain_mode',
        'status': 'status',
        'address_family': 'address_family',
        'description': 'description',
        'type': 'type'
    }

    def __init__(self, id=None, tenant_id=None, gateway_id=None, destination=None, nexthop=None, obtain_mode=None, status=None, address_family=None, description=None, type=None):
        """ShowGdgwRoutetable

        The model defined in huaweicloud sdk

        :param id: 路由id
        :type id: str
        :param tenant_id: 租户id
        :type tenant_id: str
        :param gateway_id: 网关id
        :type gateway_id: str
        :param destination: 路由子网
        :type destination: str
        :param nexthop: 下一跳id
        :type nexthop: str
        :param obtain_mode: 路由类型: - customized: 默认路由 - specific: 自定义路由 - bgp: 动态路由
        :type obtain_mode: str
        :param status: 路由状态: - ACTIVE: 下发正常 - ERROR: 下发失败 - PENDING_CREATE: 待下发
        :type status: str
        :param address_family: 
        :type address_family: :class:`huaweicloudsdkdc.v3.AddressFamily`
        :param description: 路由描述
        :type description: str
        :param type: 
        :type type: :class:`huaweicloudsdkdc.v3.RouteTypeOfGdgw`
        """
        
        

        self._id = None
        self._tenant_id = None
        self._gateway_id = None
        self._destination = None
        self._nexthop = None
        self._obtain_mode = None
        self._status = None
        self._address_family = None
        self._description = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.tenant_id = tenant_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        self.destination = destination
        self.nexthop = nexthop
        self.obtain_mode = obtain_mode
        self.status = status
        self.address_family = address_family
        if description is not None:
            self.description = description
        self.type = type

    @property
    def id(self):
        """Gets the id of this ShowGdgwRoutetable.

        路由id

        :return: The id of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowGdgwRoutetable.

        路由id

        :param id: The id of this ShowGdgwRoutetable.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ShowGdgwRoutetable.

        租户id

        :return: The tenant_id of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ShowGdgwRoutetable.

        租户id

        :param tenant_id: The tenant_id of this ShowGdgwRoutetable.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ShowGdgwRoutetable.

        网关id

        :return: The gateway_id of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ShowGdgwRoutetable.

        网关id

        :param gateway_id: The gateway_id of this ShowGdgwRoutetable.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def destination(self):
        """Gets the destination of this ShowGdgwRoutetable.

        路由子网

        :return: The destination of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ShowGdgwRoutetable.

        路由子网

        :param destination: The destination of this ShowGdgwRoutetable.
        :type destination: str
        """
        self._destination = destination

    @property
    def nexthop(self):
        """Gets the nexthop of this ShowGdgwRoutetable.

        下一跳id

        :return: The nexthop of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """Sets the nexthop of this ShowGdgwRoutetable.

        下一跳id

        :param nexthop: The nexthop of this ShowGdgwRoutetable.
        :type nexthop: str
        """
        self._nexthop = nexthop

    @property
    def obtain_mode(self):
        """Gets the obtain_mode of this ShowGdgwRoutetable.

        路由类型: - customized: 默认路由 - specific: 自定义路由 - bgp: 动态路由

        :return: The obtain_mode of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._obtain_mode

    @obtain_mode.setter
    def obtain_mode(self, obtain_mode):
        """Sets the obtain_mode of this ShowGdgwRoutetable.

        路由类型: - customized: 默认路由 - specific: 自定义路由 - bgp: 动态路由

        :param obtain_mode: The obtain_mode of this ShowGdgwRoutetable.
        :type obtain_mode: str
        """
        self._obtain_mode = obtain_mode

    @property
    def status(self):
        """Gets the status of this ShowGdgwRoutetable.

        路由状态: - ACTIVE: 下发正常 - ERROR: 下发失败 - PENDING_CREATE: 待下发

        :return: The status of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowGdgwRoutetable.

        路由状态: - ACTIVE: 下发正常 - ERROR: 下发失败 - PENDING_CREATE: 待下发

        :param status: The status of this ShowGdgwRoutetable.
        :type status: str
        """
        self._status = status

    @property
    def address_family(self):
        """Gets the address_family of this ShowGdgwRoutetable.

        :return: The address_family of this ShowGdgwRoutetable.
        :rtype: :class:`huaweicloudsdkdc.v3.AddressFamily`
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this ShowGdgwRoutetable.

        :param address_family: The address_family of this ShowGdgwRoutetable.
        :type address_family: :class:`huaweicloudsdkdc.v3.AddressFamily`
        """
        self._address_family = address_family

    @property
    def description(self):
        """Gets the description of this ShowGdgwRoutetable.

        路由描述

        :return: The description of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowGdgwRoutetable.

        路由描述

        :param description: The description of this ShowGdgwRoutetable.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this ShowGdgwRoutetable.

        :return: The type of this ShowGdgwRoutetable.
        :rtype: :class:`huaweicloudsdkdc.v3.RouteTypeOfGdgw`
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowGdgwRoutetable.

        :param type: The type of this ShowGdgwRoutetable.
        :type type: :class:`huaweicloudsdkdc.v3.RouteTypeOfGdgw`
        """
        self._type = type

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
        if not isinstance(other, ShowGdgwRoutetable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
