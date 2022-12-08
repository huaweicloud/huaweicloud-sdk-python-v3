# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthPackage:

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
        'description': 'str',
        'domain_id': 'str',
        'enterprise_project_id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'admin_state_up': 'bool',
        'order_id': 'str',
        'product_id': 'str',
        'spec_code': 'str',
        'billing_mode': 'str',
        'charge_mode': 'str',
        'bandwidth': 'int',
        'resource_id': 'str',
        'resource_type': 'str',
        'local_area_id': 'str',
        'remote_area_id': 'str',
        'project_id': 'str',
        'interflow_mode': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'domain_id': 'domain_id',
        'enterprise_project_id': 'enterprise_project_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'admin_state_up': 'admin_state_up',
        'order_id': 'order_id',
        'product_id': 'product_id',
        'spec_code': 'spec_code',
        'billing_mode': 'billing_mode',
        'charge_mode': 'charge_mode',
        'bandwidth': 'bandwidth',
        'resource_id': 'resource_id',
        'resource_type': 'resource_type',
        'local_area_id': 'local_area_id',
        'remote_area_id': 'remote_area_id',
        'project_id': 'project_id',
        'interflow_mode': 'interflow_mode',
        'tags': 'tags'
    }

    def __init__(self, id=None, name=None, description=None, domain_id=None, enterprise_project_id=None, status=None, created_at=None, updated_at=None, admin_state_up=None, order_id=None, product_id=None, spec_code=None, billing_mode=None, charge_mode=None, bandwidth=None, resource_id=None, resource_type=None, local_area_id=None, remote_area_id=None, project_id=None, interflow_mode=None, tags=None):
        """BandwidthPackage

        The model defined in huaweicloud sdk

        :param id: 带宽包实例的ID。
        :type id: str
        :param name: 带宽包实例的名字。
        :type name: str
        :param description: 带宽包实例的描述。
        :type description: str
        :param domain_id: 帐号ID。
        :type domain_id: str
        :param enterprise_project_id: 带宽包实例的企业项目ID。
        :type enterprise_project_id: str
        :param status: 带宽包实例的状态。ACTIVE表示状态
        :type status: str
        :param created_at: 带宽包实例的创建时间。
        :type created_at: datetime
        :param updated_at: 带宽包实例的更新时间。
        :type updated_at: datetime
        :param admin_state_up: 带宽包实例的管理状态。
        :type admin_state_up: bool
        :param order_id: 带宽包实例的订单ID。
        :type order_id: str
        :param product_id: 带宽包实例的产品ID。
        :type product_id: str
        :param spec_code: 带宽包实例的规格编码。 bandwidth.aftoela：大陆站+国际站南非-拉美东 bandwidth.aftonla：大陆站+国际站南非-拉美北 bandwidth.aftowla：大陆站+国际站南非-拉美西 bandwidth.aptoaf：国际站亚太-南非 bandwidth.aptoap：国际站亚太-亚太 bandwidth.aptoela：大陆站+国际站亚太-拉美东 bandwidth.aptonla：大陆站+国际站亚太-拉美北 bandwidth.aptowla：大陆站+国际站亚太-拉美西 bandwidth.cmtoaf：国际站中国大陆-南非 bandwidth.cmtoap：国际站中国大陆-亚太 bandwidth.cmtocm：国际站中国大陆-中国大陆 bandwidth.cmtoela：大陆站+国际站中国大陆-拉美东 bandwidth.cmtonla：大陆站+国际站中国大陆-拉美北 bandwidth.cmtowla：大陆站+国际站中国大陆-拉美西 bandwidth.elatoela：大陆站+国际站拉美东-拉美东 bandwidth.elatonla：大陆站+国际站拉美东-拉美北 bandwidth.wlatoela：大陆站+国际站拉美西-拉美东 bandwidth.wlatonla：大陆站+国际站拉美西-拉美北 bandwidth.wlatowla：大陆站+国际站拉美西-拉美西
        :type spec_code: str
        :param billing_mode: 带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期 2：国际站包周期 3：大陆站按需计费 4：国际站按需计费 5：大陆站按95方式计费 6：国际站按95方式计费
        :type billing_mode: str
        :param charge_mode: 带宽包实例的计费方式。 bandwidth是按带宽计费。
        :type charge_mode: str
        :param bandwidth: 带宽包实例中的带宽值。
        :type bandwidth: int
        :param resource_id: 带宽包实例绑定的资源ID。
        :type resource_id: str
        :param resource_type: 带宽包实例绑定的资源类型。 cloud_connection: 云连接实例。
        :type resource_type: str
        :param local_area_id: 本端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |
        :type local_area_id: str
        :param remote_area_id: 远端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |
        :type remote_area_id: str
        :param project_id: 项目ID。
        :type project_id: str
        :param interflow_mode: 互通类型: - Area: 大区互通 - Region: 城域互通
        :type interflow_mode: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._domain_id = None
        self._enterprise_project_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._admin_state_up = None
        self._order_id = None
        self._product_id = None
        self._spec_code = None
        self._billing_mode = None
        self._charge_mode = None
        self._bandwidth = None
        self._resource_id = None
        self._resource_type = None
        self._local_area_id = None
        self._remote_area_id = None
        self._project_id = None
        self._interflow_mode = None
        self._tags = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if domain_id is not None:
            self.domain_id = domain_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if order_id is not None:
            self.order_id = order_id
        if product_id is not None:
            self.product_id = product_id
        if spec_code is not None:
            self.spec_code = spec_code
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if local_area_id is not None:
            self.local_area_id = local_area_id
        if remote_area_id is not None:
            self.remote_area_id = remote_area_id
        if project_id is not None:
            self.project_id = project_id
        if interflow_mode is not None:
            self.interflow_mode = interflow_mode
        if tags is not None:
            self.tags = tags

    @property
    def id(self):
        """Gets the id of this BandwidthPackage.

        带宽包实例的ID。

        :return: The id of this BandwidthPackage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BandwidthPackage.

        带宽包实例的ID。

        :param id: The id of this BandwidthPackage.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BandwidthPackage.

        带宽包实例的名字。

        :return: The name of this BandwidthPackage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BandwidthPackage.

        带宽包实例的名字。

        :param name: The name of this BandwidthPackage.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this BandwidthPackage.

        带宽包实例的描述。

        :return: The description of this BandwidthPackage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BandwidthPackage.

        带宽包实例的描述。

        :param description: The description of this BandwidthPackage.
        :type description: str
        """
        self._description = description

    @property
    def domain_id(self):
        """Gets the domain_id of this BandwidthPackage.

        帐号ID。

        :return: The domain_id of this BandwidthPackage.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this BandwidthPackage.

        帐号ID。

        :param domain_id: The domain_id of this BandwidthPackage.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this BandwidthPackage.

        带宽包实例的企业项目ID。

        :return: The enterprise_project_id of this BandwidthPackage.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this BandwidthPackage.

        带宽包实例的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this BandwidthPackage.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def status(self):
        """Gets the status of this BandwidthPackage.

        带宽包实例的状态。ACTIVE表示状态

        :return: The status of this BandwidthPackage.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BandwidthPackage.

        带宽包实例的状态。ACTIVE表示状态

        :param status: The status of this BandwidthPackage.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this BandwidthPackage.

        带宽包实例的创建时间。

        :return: The created_at of this BandwidthPackage.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BandwidthPackage.

        带宽包实例的创建时间。

        :param created_at: The created_at of this BandwidthPackage.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BandwidthPackage.

        带宽包实例的更新时间。

        :return: The updated_at of this BandwidthPackage.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BandwidthPackage.

        带宽包实例的更新时间。

        :param updated_at: The updated_at of this BandwidthPackage.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this BandwidthPackage.

        带宽包实例的管理状态。

        :return: The admin_state_up of this BandwidthPackage.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this BandwidthPackage.

        带宽包实例的管理状态。

        :param admin_state_up: The admin_state_up of this BandwidthPackage.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def order_id(self):
        """Gets the order_id of this BandwidthPackage.

        带宽包实例的订单ID。

        :return: The order_id of this BandwidthPackage.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this BandwidthPackage.

        带宽包实例的订单ID。

        :param order_id: The order_id of this BandwidthPackage.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def product_id(self):
        """Gets the product_id of this BandwidthPackage.

        带宽包实例的产品ID。

        :return: The product_id of this BandwidthPackage.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this BandwidthPackage.

        带宽包实例的产品ID。

        :param product_id: The product_id of this BandwidthPackage.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def spec_code(self):
        """Gets the spec_code of this BandwidthPackage.

        带宽包实例的规格编码。 bandwidth.aftoela：大陆站+国际站南非-拉美东 bandwidth.aftonla：大陆站+国际站南非-拉美北 bandwidth.aftowla：大陆站+国际站南非-拉美西 bandwidth.aptoaf：国际站亚太-南非 bandwidth.aptoap：国际站亚太-亚太 bandwidth.aptoela：大陆站+国际站亚太-拉美东 bandwidth.aptonla：大陆站+国际站亚太-拉美北 bandwidth.aptowla：大陆站+国际站亚太-拉美西 bandwidth.cmtoaf：国际站中国大陆-南非 bandwidth.cmtoap：国际站中国大陆-亚太 bandwidth.cmtocm：国际站中国大陆-中国大陆 bandwidth.cmtoela：大陆站+国际站中国大陆-拉美东 bandwidth.cmtonla：大陆站+国际站中国大陆-拉美北 bandwidth.cmtowla：大陆站+国际站中国大陆-拉美西 bandwidth.elatoela：大陆站+国际站拉美东-拉美东 bandwidth.elatonla：大陆站+国际站拉美东-拉美北 bandwidth.wlatoela：大陆站+国际站拉美西-拉美东 bandwidth.wlatonla：大陆站+国际站拉美西-拉美北 bandwidth.wlatowla：大陆站+国际站拉美西-拉美西

        :return: The spec_code of this BandwidthPackage.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this BandwidthPackage.

        带宽包实例的规格编码。 bandwidth.aftoela：大陆站+国际站南非-拉美东 bandwidth.aftonla：大陆站+国际站南非-拉美北 bandwidth.aftowla：大陆站+国际站南非-拉美西 bandwidth.aptoaf：国际站亚太-南非 bandwidth.aptoap：国际站亚太-亚太 bandwidth.aptoela：大陆站+国际站亚太-拉美东 bandwidth.aptonla：大陆站+国际站亚太-拉美北 bandwidth.aptowla：大陆站+国际站亚太-拉美西 bandwidth.cmtoaf：国际站中国大陆-南非 bandwidth.cmtoap：国际站中国大陆-亚太 bandwidth.cmtocm：国际站中国大陆-中国大陆 bandwidth.cmtoela：大陆站+国际站中国大陆-拉美东 bandwidth.cmtonla：大陆站+国际站中国大陆-拉美北 bandwidth.cmtowla：大陆站+国际站中国大陆-拉美西 bandwidth.elatoela：大陆站+国际站拉美东-拉美东 bandwidth.elatonla：大陆站+国际站拉美东-拉美北 bandwidth.wlatoela：大陆站+国际站拉美西-拉美东 bandwidth.wlatonla：大陆站+国际站拉美西-拉美北 bandwidth.wlatowla：大陆站+国际站拉美西-拉美西

        :param spec_code: The spec_code of this BandwidthPackage.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def billing_mode(self):
        """Gets the billing_mode of this BandwidthPackage.

        带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期 2：国际站包周期 3：大陆站按需计费 4：国际站按需计费 5：大陆站按95方式计费 6：国际站按95方式计费

        :return: The billing_mode of this BandwidthPackage.
        :rtype: str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        """Sets the billing_mode of this BandwidthPackage.

        带宽包实例在大陆站或国际站的计费方式。 1：大陆站包周期 2：国际站包周期 3：大陆站按需计费 4：国际站按需计费 5：大陆站按95方式计费 6：国际站按95方式计费

        :param billing_mode: The billing_mode of this BandwidthPackage.
        :type billing_mode: str
        """
        self._billing_mode = billing_mode

    @property
    def charge_mode(self):
        """Gets the charge_mode of this BandwidthPackage.

        带宽包实例的计费方式。 bandwidth是按带宽计费。

        :return: The charge_mode of this BandwidthPackage.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this BandwidthPackage.

        带宽包实例的计费方式。 bandwidth是按带宽计费。

        :param charge_mode: The charge_mode of this BandwidthPackage.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def bandwidth(self):
        """Gets the bandwidth of this BandwidthPackage.

        带宽包实例中的带宽值。

        :return: The bandwidth of this BandwidthPackage.
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this BandwidthPackage.

        带宽包实例中的带宽值。

        :param bandwidth: The bandwidth of this BandwidthPackage.
        :type bandwidth: int
        """
        self._bandwidth = bandwidth

    @property
    def resource_id(self):
        """Gets the resource_id of this BandwidthPackage.

        带宽包实例绑定的资源ID。

        :return: The resource_id of this BandwidthPackage.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this BandwidthPackage.

        带宽包实例绑定的资源ID。

        :param resource_id: The resource_id of this BandwidthPackage.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this BandwidthPackage.

        带宽包实例绑定的资源类型。 cloud_connection: 云连接实例。

        :return: The resource_type of this BandwidthPackage.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this BandwidthPackage.

        带宽包实例绑定的资源类型。 cloud_connection: 云连接实例。

        :param resource_type: The resource_type of this BandwidthPackage.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def local_area_id(self):
        """Gets the local_area_id of this BandwidthPackage.

        本端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |

        :return: The local_area_id of this BandwidthPackage.
        :rtype: str
        """
        return self._local_area_id

    @local_area_id.setter
    def local_area_id(self, local_area_id):
        """Sets the local_area_id of this BandwidthPackage.

        本端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |

        :param local_area_id: The local_area_id of this BandwidthPackage.
        :type local_area_id: str
        """
        self._local_area_id = local_area_id

    @property
    def remote_area_id(self):
        """Gets the remote_area_id of this BandwidthPackage.

        远端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |

        :return: The remote_area_id of this BandwidthPackage.
        :rtype: str
        """
        return self._remote_area_id

    @remote_area_id.setter
    def remote_area_id(self, remote_area_id):
        """Sets the remote_area_id of this BandwidthPackage.

        远端大区。 云连接支持的大区有： | Chinese-Mainland | 中国大陆 | | Asia-Pacific | 亚太 | | Africa | 非洲 | | Western-Latin-America | 拉美西 | | Eastern-Latin-America | 拉美东 | | Northern-Latin-America | 拉美北 |

        :param remote_area_id: The remote_area_id of this BandwidthPackage.
        :type remote_area_id: str
        """
        self._remote_area_id = remote_area_id

    @property
    def project_id(self):
        """Gets the project_id of this BandwidthPackage.

        项目ID。

        :return: The project_id of this BandwidthPackage.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this BandwidthPackage.

        项目ID。

        :param project_id: The project_id of this BandwidthPackage.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def interflow_mode(self):
        """Gets the interflow_mode of this BandwidthPackage.

        互通类型: - Area: 大区互通 - Region: 城域互通

        :return: The interflow_mode of this BandwidthPackage.
        :rtype: str
        """
        return self._interflow_mode

    @interflow_mode.setter
    def interflow_mode(self, interflow_mode):
        """Sets the interflow_mode of this BandwidthPackage.

        互通类型: - Area: 大区互通 - Region: 城域互通

        :param interflow_mode: The interflow_mode of this BandwidthPackage.
        :type interflow_mode: str
        """
        self._interflow_mode = interflow_mode

    @property
    def tags(self):
        """Gets the tags of this BandwidthPackage.

        标签列表。

        :return: The tags of this BandwidthPackage.
        :rtype: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this BandwidthPackage.

        标签列表。

        :param tags: The tags of this BandwidthPackage.
        :type tags: list[:class:`huaweicloudsdkcc.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, BandwidthPackage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
