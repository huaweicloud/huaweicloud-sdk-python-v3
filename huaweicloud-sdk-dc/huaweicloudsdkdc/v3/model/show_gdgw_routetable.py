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
        'type': 'str',
        'obtain_mode': 'str',
        'status': 'str',
        'address_family': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'gateway_id': 'gateway_id',
        'destination': 'destination',
        'nexthop': 'nexthop',
        'type': 'type',
        'obtain_mode': 'obtain_mode',
        'status': 'status',
        'address_family': 'address_family',
        'description': 'description'
    }

    def __init__(self, id=None, tenant_id=None, gateway_id=None, destination=None, nexthop=None, type=None, obtain_mode=None, status=None, address_family=None, description=None):
        """ShowGdgwRoutetable

        The model defined in huaweicloud sdk

        :param id: 唯一ID
        :type id: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param gateway_id: 网关ID
        :type gateway_id: str
        :param destination: 描述信息
        :type destination: str
        :param nexthop: 下一跳ID
        :type nexthop: str
        :param type: 类型
        :type type: str
        :param obtain_mode: 获得模式
        :type obtain_mode: str
        :param status: 状态：ACTIVE-正常，ERROR-异常
        :type status: str
        :param address_family: 地址簇：ipv4 | ipv6
        :type address_family: str
        :param description: 描述信息
        :type description: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._gateway_id = None
        self._destination = None
        self._nexthop = None
        self._type = None
        self._obtain_mode = None
        self._status = None
        self._address_family = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if gateway_id is not None:
            self.gateway_id = gateway_id
        if destination is not None:
            self.destination = destination
        if nexthop is not None:
            self.nexthop = nexthop
        if type is not None:
            self.type = type
        if obtain_mode is not None:
            self.obtain_mode = obtain_mode
        if status is not None:
            self.status = status
        if address_family is not None:
            self.address_family = address_family
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this ShowGdgwRoutetable.

        唯一ID

        :return: The id of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowGdgwRoutetable.

        唯一ID

        :param id: The id of this ShowGdgwRoutetable.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ShowGdgwRoutetable.

        租户ID

        :return: The tenant_id of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ShowGdgwRoutetable.

        租户ID

        :param tenant_id: The tenant_id of this ShowGdgwRoutetable.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def gateway_id(self):
        """Gets the gateway_id of this ShowGdgwRoutetable.

        网关ID

        :return: The gateway_id of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._gateway_id

    @gateway_id.setter
    def gateway_id(self, gateway_id):
        """Sets the gateway_id of this ShowGdgwRoutetable.

        网关ID

        :param gateway_id: The gateway_id of this ShowGdgwRoutetable.
        :type gateway_id: str
        """
        self._gateway_id = gateway_id

    @property
    def destination(self):
        """Gets the destination of this ShowGdgwRoutetable.

        描述信息

        :return: The destination of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this ShowGdgwRoutetable.

        描述信息

        :param destination: The destination of this ShowGdgwRoutetable.
        :type destination: str
        """
        self._destination = destination

    @property
    def nexthop(self):
        """Gets the nexthop of this ShowGdgwRoutetable.

        下一跳ID

        :return: The nexthop of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._nexthop

    @nexthop.setter
    def nexthop(self, nexthop):
        """Sets the nexthop of this ShowGdgwRoutetable.

        下一跳ID

        :param nexthop: The nexthop of this ShowGdgwRoutetable.
        :type nexthop: str
        """
        self._nexthop = nexthop

    @property
    def type(self):
        """Gets the type of this ShowGdgwRoutetable.

        类型

        :return: The type of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowGdgwRoutetable.

        类型

        :param type: The type of this ShowGdgwRoutetable.
        :type type: str
        """
        self._type = type

    @property
    def obtain_mode(self):
        """Gets the obtain_mode of this ShowGdgwRoutetable.

        获得模式

        :return: The obtain_mode of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._obtain_mode

    @obtain_mode.setter
    def obtain_mode(self, obtain_mode):
        """Sets the obtain_mode of this ShowGdgwRoutetable.

        获得模式

        :param obtain_mode: The obtain_mode of this ShowGdgwRoutetable.
        :type obtain_mode: str
        """
        self._obtain_mode = obtain_mode

    @property
    def status(self):
        """Gets the status of this ShowGdgwRoutetable.

        状态：ACTIVE-正常，ERROR-异常

        :return: The status of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowGdgwRoutetable.

        状态：ACTIVE-正常，ERROR-异常

        :param status: The status of this ShowGdgwRoutetable.
        :type status: str
        """
        self._status = status

    @property
    def address_family(self):
        """Gets the address_family of this ShowGdgwRoutetable.

        地址簇：ipv4 | ipv6

        :return: The address_family of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this ShowGdgwRoutetable.

        地址簇：ipv4 | ipv6

        :param address_family: The address_family of this ShowGdgwRoutetable.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def description(self):
        """Gets the description of this ShowGdgwRoutetable.

        描述信息

        :return: The description of this ShowGdgwRoutetable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowGdgwRoutetable.

        描述信息

        :param description: The description of this ShowGdgwRoutetable.
        :type description: str
        """
        self._description = description

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
