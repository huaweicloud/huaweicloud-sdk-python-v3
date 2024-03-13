# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEcnInfoResponse(SdkResponse):

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
        'project_id': 'str',
        'domain_id': 'str',
        'name': 'str',
        'description': 'str',
        'bandwidth_size': 'int',
        'type': 'str',
        'area_id': 'str',
        'region_id': 'str',
        'ecn_asn': 'int',
        'ieg_asn': 'int',
        'vni': 'int',
        'enterprise_router_ids': 'list[str]',
        'vpc_ids': 'list[str]',
        'bind_ieg_count': 'int',
        'enterprise_project_id': 'str',
        'status': 'str',
        'frozen_effect': 'int',
        'hub_enable': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'order_id': 'str',
        'product_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'domain_id': 'domain_id',
        'name': 'name',
        'description': 'description',
        'bandwidth_size': 'bandwidth_size',
        'type': 'type',
        'area_id': 'area_id',
        'region_id': 'region_id',
        'ecn_asn': 'ecn_asn',
        'ieg_asn': 'ieg_asn',
        'vni': 'vni',
        'enterprise_router_ids': 'enterprise_router_ids',
        'vpc_ids': 'vpc_ids',
        'bind_ieg_count': 'bind_ieg_count',
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'frozen_effect': 'frozen_effect',
        'hub_enable': 'hub_enable',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'order_id': 'order_id',
        'product_id': 'product_id'
    }

    def __init__(self, id=None, project_id=None, domain_id=None, name=None, description=None, bandwidth_size=None, type=None, area_id=None, region_id=None, ecn_asn=None, ieg_asn=None, vni=None, enterprise_router_ids=None, vpc_ids=None, bind_ieg_count=None, enterprise_project_id=None, status=None, frozen_effect=None, hub_enable=None, created_at=None, updated_at=None, order_id=None, product_id=None):
        """ShowEcnInfoResponse

        The model defined in huaweicloud sdk

        :param id: 企业连接网络ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param domain_id: 租户账号ID
        :type domain_id: str
        :param name: 企业连接网络名字
        :type name: str
        :param description: 描述信息
        :type description: str
        :param bandwidth_size: 带宽
        :type bandwidth_size: int
        :param type: 企业连接网络类型
        :type type: str
        :param area_id: 大区ID
        :type area_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param ecn_asn: 企业连接网络AS号
        :type ecn_asn: int
        :param ieg_asn: 智能企业网关AS号
        :type ieg_asn: int
        :param vni: VXLAN网络标识
        :type vni: int
        :param enterprise_router_ids: 企业路由器列表
        :type enterprise_router_ids: list[str]
        :param vpc_ids: 虚拟私有云列表
        :type vpc_ids: list[str]
        :param bind_ieg_count: 绑定智能企业网关数量
        :type bind_ieg_count: int
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        :param status: 状态
        :type status: str
        :param frozen_effect: 冻结效果
        :type frozen_effect: int
        :param hub_enable: 分支互联开关
        :type hub_enable: bool
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param order_id: 包周期场景下购买的订单号，按需场景下为空
        :type order_id: str
        :param product_id: 包周期场景下购买的订单号，按需场景下为空
        :type product_id: str
        """
        
        super(ShowEcnInfoResponse, self).__init__()

        self._id = None
        self._project_id = None
        self._domain_id = None
        self._name = None
        self._description = None
        self._bandwidth_size = None
        self._type = None
        self._area_id = None
        self._region_id = None
        self._ecn_asn = None
        self._ieg_asn = None
        self._vni = None
        self._enterprise_router_ids = None
        self._vpc_ids = None
        self._bind_ieg_count = None
        self._enterprise_project_id = None
        self._status = None
        self._frozen_effect = None
        self._hub_enable = None
        self._created_at = None
        self._updated_at = None
        self._order_id = None
        self._product_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if domain_id is not None:
            self.domain_id = domain_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if type is not None:
            self.type = type
        if area_id is not None:
            self.area_id = area_id
        if region_id is not None:
            self.region_id = region_id
        if ecn_asn is not None:
            self.ecn_asn = ecn_asn
        if ieg_asn is not None:
            self.ieg_asn = ieg_asn
        if vni is not None:
            self.vni = vni
        if enterprise_router_ids is not None:
            self.enterprise_router_ids = enterprise_router_ids
        if vpc_ids is not None:
            self.vpc_ids = vpc_ids
        if bind_ieg_count is not None:
            self.bind_ieg_count = bind_ieg_count
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status
        if frozen_effect is not None:
            self.frozen_effect = frozen_effect
        if hub_enable is not None:
            self.hub_enable = hub_enable
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id

    @property
    def id(self):
        """Gets the id of this ShowEcnInfoResponse.

        企业连接网络ID

        :return: The id of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowEcnInfoResponse.

        企业连接网络ID

        :param id: The id of this ShowEcnInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this ShowEcnInfoResponse.

        项目ID

        :return: The project_id of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowEcnInfoResponse.

        项目ID

        :param project_id: The project_id of this ShowEcnInfoResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def domain_id(self):
        """Gets the domain_id of this ShowEcnInfoResponse.

        租户账号ID

        :return: The domain_id of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ShowEcnInfoResponse.

        租户账号ID

        :param domain_id: The domain_id of this ShowEcnInfoResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this ShowEcnInfoResponse.

        企业连接网络名字

        :return: The name of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowEcnInfoResponse.

        企业连接网络名字

        :param name: The name of this ShowEcnInfoResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowEcnInfoResponse.

        描述信息

        :return: The description of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowEcnInfoResponse.

        描述信息

        :param description: The description of this ShowEcnInfoResponse.
        :type description: str
        """
        self._description = description

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this ShowEcnInfoResponse.

        带宽

        :return: The bandwidth_size of this ShowEcnInfoResponse.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this ShowEcnInfoResponse.

        带宽

        :param bandwidth_size: The bandwidth_size of this ShowEcnInfoResponse.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def type(self):
        """Gets the type of this ShowEcnInfoResponse.

        企业连接网络类型

        :return: The type of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowEcnInfoResponse.

        企业连接网络类型

        :param type: The type of this ShowEcnInfoResponse.
        :type type: str
        """
        self._type = type

    @property
    def area_id(self):
        """Gets the area_id of this ShowEcnInfoResponse.

        大区ID

        :return: The area_id of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._area_id

    @area_id.setter
    def area_id(self, area_id):
        """Sets the area_id of this ShowEcnInfoResponse.

        大区ID

        :param area_id: The area_id of this ShowEcnInfoResponse.
        :type area_id: str
        """
        self._area_id = area_id

    @property
    def region_id(self):
        """Gets the region_id of this ShowEcnInfoResponse.

        区域ID

        :return: The region_id of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this ShowEcnInfoResponse.

        区域ID

        :param region_id: The region_id of this ShowEcnInfoResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def ecn_asn(self):
        """Gets the ecn_asn of this ShowEcnInfoResponse.

        企业连接网络AS号

        :return: The ecn_asn of this ShowEcnInfoResponse.
        :rtype: int
        """
        return self._ecn_asn

    @ecn_asn.setter
    def ecn_asn(self, ecn_asn):
        """Sets the ecn_asn of this ShowEcnInfoResponse.

        企业连接网络AS号

        :param ecn_asn: The ecn_asn of this ShowEcnInfoResponse.
        :type ecn_asn: int
        """
        self._ecn_asn = ecn_asn

    @property
    def ieg_asn(self):
        """Gets the ieg_asn of this ShowEcnInfoResponse.

        智能企业网关AS号

        :return: The ieg_asn of this ShowEcnInfoResponse.
        :rtype: int
        """
        return self._ieg_asn

    @ieg_asn.setter
    def ieg_asn(self, ieg_asn):
        """Sets the ieg_asn of this ShowEcnInfoResponse.

        智能企业网关AS号

        :param ieg_asn: The ieg_asn of this ShowEcnInfoResponse.
        :type ieg_asn: int
        """
        self._ieg_asn = ieg_asn

    @property
    def vni(self):
        """Gets the vni of this ShowEcnInfoResponse.

        VXLAN网络标识

        :return: The vni of this ShowEcnInfoResponse.
        :rtype: int
        """
        return self._vni

    @vni.setter
    def vni(self, vni):
        """Sets the vni of this ShowEcnInfoResponse.

        VXLAN网络标识

        :param vni: The vni of this ShowEcnInfoResponse.
        :type vni: int
        """
        self._vni = vni

    @property
    def enterprise_router_ids(self):
        """Gets the enterprise_router_ids of this ShowEcnInfoResponse.

        企业路由器列表

        :return: The enterprise_router_ids of this ShowEcnInfoResponse.
        :rtype: list[str]
        """
        return self._enterprise_router_ids

    @enterprise_router_ids.setter
    def enterprise_router_ids(self, enterprise_router_ids):
        """Sets the enterprise_router_ids of this ShowEcnInfoResponse.

        企业路由器列表

        :param enterprise_router_ids: The enterprise_router_ids of this ShowEcnInfoResponse.
        :type enterprise_router_ids: list[str]
        """
        self._enterprise_router_ids = enterprise_router_ids

    @property
    def vpc_ids(self):
        """Gets the vpc_ids of this ShowEcnInfoResponse.

        虚拟私有云列表

        :return: The vpc_ids of this ShowEcnInfoResponse.
        :rtype: list[str]
        """
        return self._vpc_ids

    @vpc_ids.setter
    def vpc_ids(self, vpc_ids):
        """Sets the vpc_ids of this ShowEcnInfoResponse.

        虚拟私有云列表

        :param vpc_ids: The vpc_ids of this ShowEcnInfoResponse.
        :type vpc_ids: list[str]
        """
        self._vpc_ids = vpc_ids

    @property
    def bind_ieg_count(self):
        """Gets the bind_ieg_count of this ShowEcnInfoResponse.

        绑定智能企业网关数量

        :return: The bind_ieg_count of this ShowEcnInfoResponse.
        :rtype: int
        """
        return self._bind_ieg_count

    @bind_ieg_count.setter
    def bind_ieg_count(self, bind_ieg_count):
        """Sets the bind_ieg_count of this ShowEcnInfoResponse.

        绑定智能企业网关数量

        :param bind_ieg_count: The bind_ieg_count of this ShowEcnInfoResponse.
        :type bind_ieg_count: int
        """
        self._bind_ieg_count = bind_ieg_count

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowEcnInfoResponse.

        企业项目ID

        :return: The enterprise_project_id of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowEcnInfoResponse.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ShowEcnInfoResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        """Gets the status of this ShowEcnInfoResponse.

        状态

        :return: The status of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowEcnInfoResponse.

        状态

        :param status: The status of this ShowEcnInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def frozen_effect(self):
        """Gets the frozen_effect of this ShowEcnInfoResponse.

        冻结效果

        :return: The frozen_effect of this ShowEcnInfoResponse.
        :rtype: int
        """
        return self._frozen_effect

    @frozen_effect.setter
    def frozen_effect(self, frozen_effect):
        """Sets the frozen_effect of this ShowEcnInfoResponse.

        冻结效果

        :param frozen_effect: The frozen_effect of this ShowEcnInfoResponse.
        :type frozen_effect: int
        """
        self._frozen_effect = frozen_effect

    @property
    def hub_enable(self):
        """Gets the hub_enable of this ShowEcnInfoResponse.

        分支互联开关

        :return: The hub_enable of this ShowEcnInfoResponse.
        :rtype: bool
        """
        return self._hub_enable

    @hub_enable.setter
    def hub_enable(self, hub_enable):
        """Sets the hub_enable of this ShowEcnInfoResponse.

        分支互联开关

        :param hub_enable: The hub_enable of this ShowEcnInfoResponse.
        :type hub_enable: bool
        """
        self._hub_enable = hub_enable

    @property
    def created_at(self):
        """Gets the created_at of this ShowEcnInfoResponse.

        创建时间

        :return: The created_at of this ShowEcnInfoResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowEcnInfoResponse.

        创建时间

        :param created_at: The created_at of this ShowEcnInfoResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowEcnInfoResponse.

        更新时间

        :return: The updated_at of this ShowEcnInfoResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowEcnInfoResponse.

        更新时间

        :param updated_at: The updated_at of this ShowEcnInfoResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def order_id(self):
        """Gets the order_id of this ShowEcnInfoResponse.

        包周期场景下购买的订单号，按需场景下为空

        :return: The order_id of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowEcnInfoResponse.

        包周期场景下购买的订单号，按需场景下为空

        :param order_id: The order_id of this ShowEcnInfoResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this ShowEcnInfoResponse.

        包周期场景下购买的订单号，按需场景下为空

        :return: The product_id of this ShowEcnInfoResponse.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShowEcnInfoResponse.

        包周期场景下购买的订单号，按需场景下为空

        :param product_id: The product_id of this ShowEcnInfoResponse.
        :type product_id: str
        """
        self._product_id = product_id

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
        if not isinstance(other, ShowEcnInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
