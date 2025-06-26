# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResponseP2cVgw:

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
        'name': 'str',
        'status': 'str',
        'vpc_id': 'str',
        'connect_subnet': 'str',
        'flavor': 'str',
        'availability_zone_ids': 'list[str]',
        'eip': 'ResponseEipInfo',
        'max_connection_number': 'int',
        'current_connection_number': 'int',
        'enterprise_project_id': 'str',
        'tags': 'list[VpnResourceTag]',
        'order_id': 'str',
        'admin_state_up': 'bool',
        'frozen_effect': 'int',
        'version': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'applied_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'vpc_id': 'vpc_id',
        'connect_subnet': 'connect_subnet',
        'flavor': 'flavor',
        'availability_zone_ids': 'availability_zone_ids',
        'eip': 'eip',
        'max_connection_number': 'max_connection_number',
        'current_connection_number': 'current_connection_number',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'order_id': 'order_id',
        'admin_state_up': 'admin_state_up',
        'frozen_effect': 'frozen_effect',
        'version': 'version',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'applied_at': 'applied_at'
    }

    def __init__(self, id=None, name=None, status=None, vpc_id=None, connect_subnet=None, flavor=None, availability_zone_ids=None, eip=None, max_connection_number=None, current_connection_number=None, enterprise_project_id=None, tags=None, order_id=None, admin_state_up=None, frozen_effect=None, version=None, created_at=None, updated_at=None, applied_at=None):
        r"""ShowResponseP2cVgw

        The model defined in huaweicloud sdk

        :param id: P2C VPN网关ID
        :type id: str
        :param name: P2C VPN网关名称
        :type name: str
        :param status: P2C VPN网关状态
        :type status: str
        :param vpc_id: P2C VPN网关所连接的VPC的ID
        :type vpc_id: str
        :param connect_subnet: P2C VPN网关所使用的VPC子网ID
        :type connect_subnet: str
        :param flavor: P2C VPN网关的规格类型
        :type flavor: str
        :param availability_zone_ids: 可用区列表
        :type availability_zone_ids: list[str]
        :param eip: 
        :type eip: :class:`huaweicloudsdkvpn.v5.ResponseEipInfo`
        :param max_connection_number: 配置的最大并发客户端连接数
        :type max_connection_number: int
        :param current_connection_number: 当前建连的客户端连接数
        :type current_connection_number: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        :param order_id: 订单Id
        :type order_id: str
        :param admin_state_up: 冻结状态
        :type admin_state_up: bool
        :param frozen_effect: 冻结场景：0未冻结；1 冻结可删除；2冻结不可删除
        :type frozen_effect: int
        :param version: 网关版本
        :type version: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param applied_at: 生效时间
        :type applied_at: datetime
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._vpc_id = None
        self._connect_subnet = None
        self._flavor = None
        self._availability_zone_ids = None
        self._eip = None
        self._max_connection_number = None
        self._current_connection_number = None
        self._enterprise_project_id = None
        self._tags = None
        self._order_id = None
        self._admin_state_up = None
        self._frozen_effect = None
        self._version = None
        self._created_at = None
        self._updated_at = None
        self._applied_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if connect_subnet is not None:
            self.connect_subnet = connect_subnet
        if flavor is not None:
            self.flavor = flavor
        if availability_zone_ids is not None:
            self.availability_zone_ids = availability_zone_ids
        if eip is not None:
            self.eip = eip
        if max_connection_number is not None:
            self.max_connection_number = max_connection_number
        if current_connection_number is not None:
            self.current_connection_number = current_connection_number
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if order_id is not None:
            self.order_id = order_id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if frozen_effect is not None:
            self.frozen_effect = frozen_effect
        if version is not None:
            self.version = version
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if applied_at is not None:
            self.applied_at = applied_at

    @property
    def id(self):
        r"""Gets the id of this ShowResponseP2cVgw.

        P2C VPN网关ID

        :return: The id of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowResponseP2cVgw.

        P2C VPN网关ID

        :param id: The id of this ShowResponseP2cVgw.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowResponseP2cVgw.

        P2C VPN网关名称

        :return: The name of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowResponseP2cVgw.

        P2C VPN网关名称

        :param name: The name of this ShowResponseP2cVgw.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ShowResponseP2cVgw.

        P2C VPN网关状态

        :return: The status of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowResponseP2cVgw.

        P2C VPN网关状态

        :param status: The status of this ShowResponseP2cVgw.
        :type status: str
        """
        self._status = status

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ShowResponseP2cVgw.

        P2C VPN网关所连接的VPC的ID

        :return: The vpc_id of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ShowResponseP2cVgw.

        P2C VPN网关所连接的VPC的ID

        :param vpc_id: The vpc_id of this ShowResponseP2cVgw.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def connect_subnet(self):
        r"""Gets the connect_subnet of this ShowResponseP2cVgw.

        P2C VPN网关所使用的VPC子网ID

        :return: The connect_subnet of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._connect_subnet

    @connect_subnet.setter
    def connect_subnet(self, connect_subnet):
        r"""Sets the connect_subnet of this ShowResponseP2cVgw.

        P2C VPN网关所使用的VPC子网ID

        :param connect_subnet: The connect_subnet of this ShowResponseP2cVgw.
        :type connect_subnet: str
        """
        self._connect_subnet = connect_subnet

    @property
    def flavor(self):
        r"""Gets the flavor of this ShowResponseP2cVgw.

        P2C VPN网关的规格类型

        :return: The flavor of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ShowResponseP2cVgw.

        P2C VPN网关的规格类型

        :param flavor: The flavor of this ShowResponseP2cVgw.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def availability_zone_ids(self):
        r"""Gets the availability_zone_ids of this ShowResponseP2cVgw.

        可用区列表

        :return: The availability_zone_ids of this ShowResponseP2cVgw.
        :rtype: list[str]
        """
        return self._availability_zone_ids

    @availability_zone_ids.setter
    def availability_zone_ids(self, availability_zone_ids):
        r"""Sets the availability_zone_ids of this ShowResponseP2cVgw.

        可用区列表

        :param availability_zone_ids: The availability_zone_ids of this ShowResponseP2cVgw.
        :type availability_zone_ids: list[str]
        """
        self._availability_zone_ids = availability_zone_ids

    @property
    def eip(self):
        r"""Gets the eip of this ShowResponseP2cVgw.

        :return: The eip of this ShowResponseP2cVgw.
        :rtype: :class:`huaweicloudsdkvpn.v5.ResponseEipInfo`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this ShowResponseP2cVgw.

        :param eip: The eip of this ShowResponseP2cVgw.
        :type eip: :class:`huaweicloudsdkvpn.v5.ResponseEipInfo`
        """
        self._eip = eip

    @property
    def max_connection_number(self):
        r"""Gets the max_connection_number of this ShowResponseP2cVgw.

        配置的最大并发客户端连接数

        :return: The max_connection_number of this ShowResponseP2cVgw.
        :rtype: int
        """
        return self._max_connection_number

    @max_connection_number.setter
    def max_connection_number(self, max_connection_number):
        r"""Sets the max_connection_number of this ShowResponseP2cVgw.

        配置的最大并发客户端连接数

        :param max_connection_number: The max_connection_number of this ShowResponseP2cVgw.
        :type max_connection_number: int
        """
        self._max_connection_number = max_connection_number

    @property
    def current_connection_number(self):
        r"""Gets the current_connection_number of this ShowResponseP2cVgw.

        当前建连的客户端连接数

        :return: The current_connection_number of this ShowResponseP2cVgw.
        :rtype: int
        """
        return self._current_connection_number

    @current_connection_number.setter
    def current_connection_number(self, current_connection_number):
        r"""Sets the current_connection_number of this ShowResponseP2cVgw.

        当前建连的客户端连接数

        :param current_connection_number: The current_connection_number of this ShowResponseP2cVgw.
        :type current_connection_number: int
        """
        self._current_connection_number = current_connection_number

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowResponseP2cVgw.

        企业项目ID

        :return: The enterprise_project_id of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowResponseP2cVgw.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowResponseP2cVgw.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this ShowResponseP2cVgw.

        标签

        :return: The tags of this ShowResponseP2cVgw.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowResponseP2cVgw.

        标签

        :param tags: The tags of this ShowResponseP2cVgw.
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        self._tags = tags

    @property
    def order_id(self):
        r"""Gets the order_id of this ShowResponseP2cVgw.

        订单Id

        :return: The order_id of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ShowResponseP2cVgw.

        订单Id

        :param order_id: The order_id of this ShowResponseP2cVgw.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ShowResponseP2cVgw.

        冻结状态

        :return: The admin_state_up of this ShowResponseP2cVgw.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ShowResponseP2cVgw.

        冻结状态

        :param admin_state_up: The admin_state_up of this ShowResponseP2cVgw.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def frozen_effect(self):
        r"""Gets the frozen_effect of this ShowResponseP2cVgw.

        冻结场景：0未冻结；1 冻结可删除；2冻结不可删除

        :return: The frozen_effect of this ShowResponseP2cVgw.
        :rtype: int
        """
        return self._frozen_effect

    @frozen_effect.setter
    def frozen_effect(self, frozen_effect):
        r"""Sets the frozen_effect of this ShowResponseP2cVgw.

        冻结场景：0未冻结；1 冻结可删除；2冻结不可删除

        :param frozen_effect: The frozen_effect of this ShowResponseP2cVgw.
        :type frozen_effect: int
        """
        self._frozen_effect = frozen_effect

    @property
    def version(self):
        r"""Gets the version of this ShowResponseP2cVgw.

        网关版本

        :return: The version of this ShowResponseP2cVgw.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ShowResponseP2cVgw.

        网关版本

        :param version: The version of this ShowResponseP2cVgw.
        :type version: str
        """
        self._version = version

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowResponseP2cVgw.

        创建时间

        :return: The created_at of this ShowResponseP2cVgw.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowResponseP2cVgw.

        创建时间

        :param created_at: The created_at of this ShowResponseP2cVgw.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowResponseP2cVgw.

        更新时间

        :return: The updated_at of this ShowResponseP2cVgw.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowResponseP2cVgw.

        更新时间

        :param updated_at: The updated_at of this ShowResponseP2cVgw.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def applied_at(self):
        r"""Gets the applied_at of this ShowResponseP2cVgw.

        生效时间

        :return: The applied_at of this ShowResponseP2cVgw.
        :rtype: datetime
        """
        return self._applied_at

    @applied_at.setter
    def applied_at(self, applied_at):
        r"""Sets the applied_at of this ShowResponseP2cVgw.

        生效时间

        :param applied_at: The applied_at of this ShowResponseP2cVgw.
        :type applied_at: datetime
        """
        self._applied_at = applied_at

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
        if not isinstance(other, ShowResponseP2cVgw):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
