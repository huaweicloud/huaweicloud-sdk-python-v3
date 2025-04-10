# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectGatewayResponse:

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
        'name': 'str',
        'description': 'str',
        'address_family': 'str',
        'status': 'str',
        'access_site': 'str',
        'bgp_asn': 'int',
        'current_geip_count': 'int',
        'created_time': 'datetime',
        'updated_time': 'datetime',
        'gcb_id': 'str',
        'gateway_site': 'str'
    }

    attribute_map = {
        'id': 'id',
        'tenant_id': 'tenant_id',
        'name': 'name',
        'description': 'description',
        'address_family': 'address_family',
        'status': 'status',
        'access_site': 'access_site',
        'bgp_asn': 'bgp_asn',
        'current_geip_count': 'current_geip_count',
        'created_time': 'created_time',
        'updated_time': 'updated_time',
        'gcb_id': 'gcb_id',
        'gateway_site': 'gateway_site'
    }

    def __init__(self, id=None, tenant_id=None, name=None, description=None, address_family=None, status=None, access_site=None, bgp_asn=None, current_geip_count=None, created_time=None, updated_time=None, gcb_id=None, gateway_site=None):
        r"""ConnectGatewayResponse

        The model defined in huaweicloud sdk

        :param id: 唯一ID
        :type id: str
        :param tenant_id: 租户项目ID
        :type tenant_id: str
        :param name: 网关名字
        :type name: str
        :param description: 描述信息
        :type description: str
        :param address_family: 地址族信息 - ipv4: 仅支持ipv4模式 - dual: 支持ipv4 和 ipv6 模式
        :type address_family: str
        :param status: 网关状态 - DOWN 未使用或关联设备状态为DOWN - ACTIVE 正常 - ERROR 异常
        :type status: str
        :param access_site: 网关站点值
        :type access_site: str
        :param bgp_asn: BGP类型AS号
        :type bgp_asn: int
        :param current_geip_count: 当前绑定的global eip数量
        :type current_geip_count: int
        :param created_time: 创建时间
        :type created_time: datetime
        :param updated_time: 更新时间
        :type updated_time: datetime
        :param gcb_id: 带宽包id
        :type gcb_id: str
        :param gateway_site: 网关位置
        :type gateway_site: str
        """
        
        

        self._id = None
        self._tenant_id = None
        self._name = None
        self._description = None
        self._address_family = None
        self._status = None
        self._access_site = None
        self._bgp_asn = None
        self._current_geip_count = None
        self._created_time = None
        self._updated_time = None
        self._gcb_id = None
        self._gateway_site = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if address_family is not None:
            self.address_family = address_family
        if status is not None:
            self.status = status
        if access_site is not None:
            self.access_site = access_site
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if current_geip_count is not None:
            self.current_geip_count = current_geip_count
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time
        if gcb_id is not None:
            self.gcb_id = gcb_id
        if gateway_site is not None:
            self.gateway_site = gateway_site

    @property
    def id(self):
        r"""Gets the id of this ConnectGatewayResponse.

        唯一ID

        :return: The id of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConnectGatewayResponse.

        唯一ID

        :param id: The id of this ConnectGatewayResponse.
        :type id: str
        """
        self._id = id

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ConnectGatewayResponse.

        租户项目ID

        :return: The tenant_id of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ConnectGatewayResponse.

        租户项目ID

        :param tenant_id: The tenant_id of this ConnectGatewayResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def name(self):
        r"""Gets the name of this ConnectGatewayResponse.

        网关名字

        :return: The name of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConnectGatewayResponse.

        网关名字

        :param name: The name of this ConnectGatewayResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ConnectGatewayResponse.

        描述信息

        :return: The description of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConnectGatewayResponse.

        描述信息

        :param description: The description of this ConnectGatewayResponse.
        :type description: str
        """
        self._description = description

    @property
    def address_family(self):
        r"""Gets the address_family of this ConnectGatewayResponse.

        地址族信息 - ipv4: 仅支持ipv4模式 - dual: 支持ipv4 和 ipv6 模式

        :return: The address_family of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        r"""Sets the address_family of this ConnectGatewayResponse.

        地址族信息 - ipv4: 仅支持ipv4模式 - dual: 支持ipv4 和 ipv6 模式

        :param address_family: The address_family of this ConnectGatewayResponse.
        :type address_family: str
        """
        self._address_family = address_family

    @property
    def status(self):
        r"""Gets the status of this ConnectGatewayResponse.

        网关状态 - DOWN 未使用或关联设备状态为DOWN - ACTIVE 正常 - ERROR 异常

        :return: The status of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ConnectGatewayResponse.

        网关状态 - DOWN 未使用或关联设备状态为DOWN - ACTIVE 正常 - ERROR 异常

        :param status: The status of this ConnectGatewayResponse.
        :type status: str
        """
        self._status = status

    @property
    def access_site(self):
        r"""Gets the access_site of this ConnectGatewayResponse.

        网关站点值

        :return: The access_site of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._access_site

    @access_site.setter
    def access_site(self, access_site):
        r"""Sets the access_site of this ConnectGatewayResponse.

        网关站点值

        :param access_site: The access_site of this ConnectGatewayResponse.
        :type access_site: str
        """
        self._access_site = access_site

    @property
    def bgp_asn(self):
        r"""Gets the bgp_asn of this ConnectGatewayResponse.

        BGP类型AS号

        :return: The bgp_asn of this ConnectGatewayResponse.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        r"""Sets the bgp_asn of this ConnectGatewayResponse.

        BGP类型AS号

        :param bgp_asn: The bgp_asn of this ConnectGatewayResponse.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def current_geip_count(self):
        r"""Gets the current_geip_count of this ConnectGatewayResponse.

        当前绑定的global eip数量

        :return: The current_geip_count of this ConnectGatewayResponse.
        :rtype: int
        """
        return self._current_geip_count

    @current_geip_count.setter
    def current_geip_count(self, current_geip_count):
        r"""Sets the current_geip_count of this ConnectGatewayResponse.

        当前绑定的global eip数量

        :param current_geip_count: The current_geip_count of this ConnectGatewayResponse.
        :type current_geip_count: int
        """
        self._current_geip_count = current_geip_count

    @property
    def created_time(self):
        r"""Gets the created_time of this ConnectGatewayResponse.

        创建时间

        :return: The created_time of this ConnectGatewayResponse.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ConnectGatewayResponse.

        创建时间

        :param created_time: The created_time of this ConnectGatewayResponse.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this ConnectGatewayResponse.

        更新时间

        :return: The updated_time of this ConnectGatewayResponse.
        :rtype: datetime
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this ConnectGatewayResponse.

        更新时间

        :param updated_time: The updated_time of this ConnectGatewayResponse.
        :type updated_time: datetime
        """
        self._updated_time = updated_time

    @property
    def gcb_id(self):
        r"""Gets the gcb_id of this ConnectGatewayResponse.

        带宽包id

        :return: The gcb_id of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._gcb_id

    @gcb_id.setter
    def gcb_id(self, gcb_id):
        r"""Sets the gcb_id of this ConnectGatewayResponse.

        带宽包id

        :param gcb_id: The gcb_id of this ConnectGatewayResponse.
        :type gcb_id: str
        """
        self._gcb_id = gcb_id

    @property
    def gateway_site(self):
        r"""Gets the gateway_site of this ConnectGatewayResponse.

        网关位置

        :return: The gateway_site of this ConnectGatewayResponse.
        :rtype: str
        """
        return self._gateway_site

    @gateway_site.setter
    def gateway_site(self, gateway_site):
        r"""Sets the gateway_site of this ConnectGatewayResponse.

        网关位置

        :param gateway_site: The gateway_site of this ConnectGatewayResponse.
        :type gateway_site: str
        """
        self._gateway_site = gateway_site

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
        if not isinstance(other, ConnectGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
