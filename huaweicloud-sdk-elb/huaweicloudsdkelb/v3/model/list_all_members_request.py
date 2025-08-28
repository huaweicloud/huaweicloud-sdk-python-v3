# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllMembersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'page_reverse': 'bool',
        'name': 'list[str]',
        'weight': 'list[int]',
        'admin_state_up': 'bool',
        'subnet_cidr_id': 'list[str]',
        'address': 'list[str]',
        'protocol_port': 'list[int]',
        'id': 'list[str]',
        'operating_status': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'ip_version': 'list[str]',
        'pool_id': 'list[str]',
        'loadbalancer_id': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'name': 'name',
        'weight': 'weight',
        'admin_state_up': 'admin_state_up',
        'subnet_cidr_id': 'subnet_cidr_id',
        'address': 'address',
        'protocol_port': 'protocol_port',
        'id': 'id',
        'operating_status': 'operating_status',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'pool_id': 'pool_id',
        'loadbalancer_id': 'loadbalancer_id'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, name=None, weight=None, admin_state_up=None, subnet_cidr_id=None, address=None, protocol_port=None, id=None, operating_status=None, enterprise_project_id=None, ip_version=None, pool_id=None, loadbalancer_id=None):
        r"""ListAllMembersRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param name: **参数解释**：后端服务器名称。 支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param weight: **参数解释**：后端服务器的权重，请求按权重在同一后端服务器组下的后端服务器间分发。权重为0的后端不再接受新的请求。当后端服务器所在的后端服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。 支持多值查询，查询条件格式：*weight&#x3D;xxx&amp;weight&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type weight: list[int]
        :param admin_state_up: **参数解释**：后端服务器的管理状态。  **约束限制**：不涉及  **取值范围**：true、false  **默认取值**：不涉及
        :type admin_state_up: bool
        :param subnet_cidr_id: **参数解释**：后端服务器所在的子网ID。该子网和后端服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。 支持多值查询，查询条件格式：***subnet_cidr_id&#x3D;xxx&amp;subnet_cidr_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type subnet_cidr_id: list[str]
        :param address: **参数解释**：后端服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。 支持多值查询，查询条件格式：*address&#x3D;xxx&amp;address&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type address: list[str]
        :param protocol_port: **参数解释**：后端服务器端口号。 支持多值查询，查询条件格式：*protocol_port&#x3D;xxx&amp;protocol_port&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type protocol_port: list[int]
        :param id: **参数解释**：后端服务器ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param operating_status: **参数解释**：后端服务器的健康状态。 支持多值查询，查询条件格式：*operating_status&#x3D;xxx&amp;operating_status&#x3D;*。  **约束限制**：不涉及  **取值范围**： - NO_MONITOR：后端服务器所在的服务器组没有开启健康检查。 - INITIAL：初始化中，表示负载均衡实例配置了健康检查，但查不到数据。 - ONLINE：后端服务器正常。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。 - UNKNOWN：未关联LB实例的pool下的member，或者创建后从未关联ECS的云服务器类型member，状态置为UNKNOWN。  **默认取值**：不涉及
        :type operating_status: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:members:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        :param ip_version: **参数解释**：IP版本。 支持多值查询，查询条件格式：*ip_version&#x3D;xxx&amp;ip_version&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：v4、v6  **默认取值**：不涉及
        :type ip_version: list[str]
        :param pool_id: **参数解释**：member所属的服务器组ID。 支持多值查询，查询条件格式：*pool_id&#x3D;xxx&amp;pool_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type pool_id: list[str]
        :param loadbalancer_id: **参数解释**：负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id&#x3D;xxx&amp;loadbalancer_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._name = None
        self._weight = None
        self._admin_state_up = None
        self._subnet_cidr_id = None
        self._address = None
        self._protocol_port = None
        self._id = None
        self._operating_status = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._pool_id = None
        self._loadbalancer_id = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        if address is not None:
            self.address = address
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if id is not None:
            self.id = id
        if operating_status is not None:
            self.operating_status = operating_status
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if pool_id is not None:
            self.pool_id = pool_id
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id

    @property
    def marker(self):
        r"""Gets the marker of this ListAllMembersRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListAllMembersRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAllMembersRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListAllMembersRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListAllMembersRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListAllMembersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAllMembersRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListAllMembersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListAllMembersRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListAllMembersRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListAllMembersRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListAllMembersRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def name(self):
        r"""Gets the name of this ListAllMembersRequest.

        **参数解释**：后端服务器名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAllMembersRequest.

        **参数解释**：后端服务器名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListAllMembersRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def weight(self):
        r"""Gets the weight of this ListAllMembersRequest.

        **参数解释**：后端服务器的权重，请求按权重在同一后端服务器组下的后端服务器间分发。权重为0的后端不再接受新的请求。当后端服务器所在的后端服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。 支持多值查询，查询条件格式：*weight=xxx&weight=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The weight of this ListAllMembersRequest.
        :rtype: list[int]
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this ListAllMembersRequest.

        **参数解释**：后端服务器的权重，请求按权重在同一后端服务器组下的后端服务器间分发。权重为0的后端不再接受新的请求。当后端服务器所在的后端服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。 支持多值查询，查询条件格式：*weight=xxx&weight=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param weight: The weight of this ListAllMembersRequest.
        :type weight: list[int]
        """
        self._weight = weight

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this ListAllMembersRequest.

        **参数解释**：后端服务器的管理状态。  **约束限制**：不涉及  **取值范围**：true、false  **默认取值**：不涉及

        :return: The admin_state_up of this ListAllMembersRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this ListAllMembersRequest.

        **参数解释**：后端服务器的管理状态。  **约束限制**：不涉及  **取值范围**：true、false  **默认取值**：不涉及

        :param admin_state_up: The admin_state_up of this ListAllMembersRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        r"""Gets the subnet_cidr_id of this ListAllMembersRequest.

        **参数解释**：后端服务器所在的子网ID。该子网和后端服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。 支持多值查询，查询条件格式：***subnet_cidr_id=xxx&subnet_cidr_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The subnet_cidr_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        r"""Sets the subnet_cidr_id of this ListAllMembersRequest.

        **参数解释**：后端服务器所在的子网ID。该子网和后端服务器关联的负载均衡器的子网必须在同一VPC下。只支持指定IPv4的子网ID。 支持多值查询，查询条件格式：***subnet_cidr_id=xxx&subnet_cidr_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param subnet_cidr_id: The subnet_cidr_id of this ListAllMembersRequest.
        :type subnet_cidr_id: list[str]
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def address(self):
        r"""Gets the address of this ListAllMembersRequest.

        **参数解释**：后端服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。 支持多值查询，查询条件格式：*address=xxx&address=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The address of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ListAllMembersRequest.

        **参数解释**：后端服务器的对应的IP地址，这个IP必须在subnet_cidr_id字段的子网网段中。例如：192.168.3.11。 支持多值查询，查询条件格式：*address=xxx&address=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param address: The address of this ListAllMembersRequest.
        :type address: list[str]
        """
        self._address = address

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this ListAllMembersRequest.

        **参数解释**：后端服务器端口号。 支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The protocol_port of this ListAllMembersRequest.
        :rtype: list[int]
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this ListAllMembersRequest.

        **参数解释**：后端服务器端口号。 支持多值查询，查询条件格式：*protocol_port=xxx&protocol_port=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param protocol_port: The protocol_port of this ListAllMembersRequest.
        :type protocol_port: list[int]
        """
        self._protocol_port = protocol_port

    @property
    def id(self):
        r"""Gets the id of this ListAllMembersRequest.

        **参数解释**：后端服务器ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAllMembersRequest.

        **参数解释**：后端服务器ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListAllMembersRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def operating_status(self):
        r"""Gets the operating_status of this ListAllMembersRequest.

        **参数解释**：后端服务器的健康状态。 支持多值查询，查询条件格式：*operating_status=xxx&operating_status=*。  **约束限制**：不涉及  **取值范围**： - NO_MONITOR：后端服务器所在的服务器组没有开启健康检查。 - INITIAL：初始化中，表示负载均衡实例配置了健康检查，但查不到数据。 - ONLINE：后端服务器正常。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。 - UNKNOWN：未关联LB实例的pool下的member，或者创建后从未关联ECS的云服务器类型member，状态置为UNKNOWN。  **默认取值**：不涉及

        :return: The operating_status of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        r"""Sets the operating_status of this ListAllMembersRequest.

        **参数解释**：后端服务器的健康状态。 支持多值查询，查询条件格式：*operating_status=xxx&operating_status=*。  **约束限制**：不涉及  **取值范围**： - NO_MONITOR：后端服务器所在的服务器组没有开启健康检查。 - INITIAL：初始化中，表示负载均衡实例配置了健康检查，但查不到数据。 - ONLINE：后端服务器正常。 - OFFLINE：后端服务器关联的ECS服务器不存在或已关机。 - UNKNOWN：未关联LB实例的pool下的member，或者创建后从未关联ECS的云服务器类型member，状态置为UNKNOWN。  **默认取值**：不涉及

        :param operating_status: The operating_status of this ListAllMembersRequest.
        :type operating_status: list[str]
        """
        self._operating_status = operating_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListAllMembersRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:members:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListAllMembersRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:members:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListAllMembersRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this ListAllMembersRequest.

        **参数解释**：IP版本。 支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  **约束限制**：不涉及  **取值范围**：v4、v6  **默认取值**：不涉及

        :return: The ip_version of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this ListAllMembersRequest.

        **参数解释**：IP版本。 支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  **约束限制**：不涉及  **取值范围**：v4、v6  **默认取值**：不涉及

        :param ip_version: The ip_version of this ListAllMembersRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def pool_id(self):
        r"""Gets the pool_id of this ListAllMembersRequest.

        **参数解释**：member所属的服务器组ID。 支持多值查询，查询条件格式：*pool_id=xxx&pool_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The pool_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this ListAllMembersRequest.

        **参数解释**：member所属的服务器组ID。 支持多值查询，查询条件格式：*pool_id=xxx&pool_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param pool_id: The pool_id of this ListAllMembersRequest.
        :type pool_id: list[str]
        """
        self._pool_id = pool_id

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ListAllMembersRequest.

        **参数解释**：负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this ListAllMembersRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ListAllMembersRequest.

        **参数解释**：负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this ListAllMembersRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

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
        if not isinstance(other, ListAllMembersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
