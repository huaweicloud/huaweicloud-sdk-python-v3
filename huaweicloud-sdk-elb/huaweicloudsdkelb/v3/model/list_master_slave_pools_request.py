# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMasterSlavePoolsRequest:

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
        'description': 'list[str]',
        'healthmonitor_id': 'list[str]',
        'id': 'list[str]',
        'name': 'list[str]',
        'loadbalancer_id': 'list[str]',
        'protocol': 'list[str]',
        'lb_algorithm': 'list[str]',
        'enterprise_project_id': 'list[str]',
        'ip_version': 'list[str]',
        'member_address': 'list[str]',
        'member_device_id': 'list[str]',
        'listener_id': 'list[str]',
        'member_instance_id': 'list[str]',
        'vpc_id': 'list[str]',
        'type': 'list[str]',
        'connection_drain': 'bool'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'description': 'description',
        'healthmonitor_id': 'healthmonitor_id',
        'id': 'id',
        'name': 'name',
        'loadbalancer_id': 'loadbalancer_id',
        'protocol': 'protocol',
        'lb_algorithm': 'lb_algorithm',
        'enterprise_project_id': 'enterprise_project_id',
        'ip_version': 'ip_version',
        'member_address': 'member_address',
        'member_device_id': 'member_device_id',
        'listener_id': 'listener_id',
        'member_instance_id': 'member_instance_id',
        'vpc_id': 'vpc_id',
        'type': 'type',
        'connection_drain': 'connection_drain'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, description=None, healthmonitor_id=None, id=None, name=None, loadbalancer_id=None, protocol=None, lb_algorithm=None, enterprise_project_id=None, ip_version=None, member_address=None, member_device_id=None, listener_id=None, member_instance_id=None, vpc_id=None, type=None, connection_drain=None):
        r"""ListMasterSlavePoolsRequest

        The model defined in huaweicloud sdk

        :param marker: **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及
        :type marker: str
        :param limit: **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000
        :type limit: int
        :param page_reverse: **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false
        :type page_reverse: bool
        :param description: **参数解释**：后端服务器组的描述信息。 支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type description: list[str]
        :param healthmonitor_id: **参数解释**：后端服务器组关联的健康检查的ID。 支持多值查询，查询条件格式：*healthmonitor_id&#x3D;xxx&amp;healthmonitor_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type healthmonitor_id: list[str]
        :param id: **参数解释**：后端服务器组的ID。 支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type id: list[str]
        :param name: **参数解释**：后端服务器组的名称。 支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: list[str]
        :param loadbalancer_id: **参数解释**：后端服务器组绑定的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id&#x3D;xxx&amp;loadbalancer_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type loadbalancer_id: list[str]
        :param protocol: **参数解释**：后端服务器组的后端协议。 支持多值查询，查询条件格式：*protocol&#x3D;xxx&amp;protocol&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  **默认取值**：不涉及
        :type protocol: list[str]
        :param lb_algorithm: **参数解释**：后端服务器组的负载均衡算法。 支持多值查询，查询条件格式：*lb_algorithm&#x3D;xxx&amp;lb_algorithm&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**： 1、ROUND_ROBIN：加权轮询算法。 2、LEAST_CONNECTIONS：加权最少连接算法。 3、SOURCE_IP：源IP算法。 4、QUIC_CID：连接ID算法。  **默认取值**：不涉及
        :type lb_algorithm: list[str]
        :param enterprise_project_id: **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:pools:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)
        :type enterprise_project_id: list[str]
        :param ip_version: **参数解释**：后端服务器组支持的IP版本。 支持多值查询，查询条件格式：*ip_version&#x3D;xxx&amp;ip_version&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type ip_version: list[str]
        :param member_address: **参数解释**：后端服务器的IP地址。 支持多值查询，查询条件格式：*member_address&#x3D;xxx&amp;member_address&#x3D;xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_address: list[str]
        :param member_device_id: **参数解释**：后端服务器对应的弹性云服务器的ID。 支持多值查询，查询条件格式：*member_device_id&#x3D;xxx&amp;member_device_id&#x3D;xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_device_id: list[str]
        :param listener_id: **参数解释**：关联的监听器ID，包括通过l7policy关联的。 支持多值查询，查询条件格式：*listener_id&#x3D;xxx&amp;listener_id&#x3D;xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type listener_id: list[str]
        :param member_instance_id: **参数解释**：后端服务器ID。 支持多值查询，查询条件格式：*member_instance_id&#x3D;xxx&amp;member_instance_id&#x3D;xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及
        :type member_instance_id: list[str]
        :param vpc_id: **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type vpc_id: list[str]
        :param type: **参数解释**：后端服务器组的类型。  **约束限制**：不涉及  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\&quot;\&quot;）：允许任意类型的后端  **默认取值**：不涉及
        :type type: list[str]
        :param connection_drain: **参数解释**：查询是否开启延迟注销的功能，查询条件格式：*connection_drain&#x3D;true或者*connection_drain&#x3D;false  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及
        :type connection_drain: bool
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._description = None
        self._healthmonitor_id = None
        self._id = None
        self._name = None
        self._loadbalancer_id = None
        self._protocol = None
        self._lb_algorithm = None
        self._enterprise_project_id = None
        self._ip_version = None
        self._member_address = None
        self._member_device_id = None
        self._listener_id = None
        self._member_instance_id = None
        self._vpc_id = None
        self._type = None
        self._connection_drain = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if description is not None:
            self.description = description
        if healthmonitor_id is not None:
            self.healthmonitor_id = healthmonitor_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if protocol is not None:
            self.protocol = protocol
        if lb_algorithm is not None:
            self.lb_algorithm = lb_algorithm
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if ip_version is not None:
            self.ip_version = ip_version
        if member_address is not None:
            self.member_address = member_address
        if member_device_id is not None:
            self.member_device_id = member_device_id
        if listener_id is not None:
            self.listener_id = listener_id
        if member_instance_id is not None:
            self.member_instance_id = member_instance_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if type is not None:
            self.type = type
        if connection_drain is not None:
            self.connection_drain = connection_drain

    @property
    def marker(self):
        r"""Gets the marker of this ListMasterSlavePoolsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The marker of this ListMasterSlavePoolsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListMasterSlavePoolsRequest.

        **参数解释**：上一页最后一条记录的ID。  **约束限制**： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。  **取值范围**：不涉及  **默认取值**：不涉及

        :param marker: The marker of this ListMasterSlavePoolsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListMasterSlavePoolsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :return: The limit of this ListMasterSlavePoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListMasterSlavePoolsRequest.

        **参数解释**：每页返回的个数。  **约束限制**：不涉及  **取值范围**：0-2000  **默认取值**：2000

        :param limit: The limit of this ListMasterSlavePoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListMasterSlavePoolsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :return: The page_reverse of this ListMasterSlavePoolsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListMasterSlavePoolsRequest.

        **参数解释**：是否反向查询。  **约束限制**： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。  **取值范围**： - true：查询上一页。 - false：查询下一页。  **默认取值**：false

        :param page_reverse: The page_reverse of this ListMasterSlavePoolsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def description(self):
        r"""Gets the description of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的描述信息。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The description of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的描述信息。 支持多值查询，查询条件格式：*description=xxx&description=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param description: The description of this ListMasterSlavePoolsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def healthmonitor_id(self):
        r"""Gets the healthmonitor_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组关联的健康检查的ID。 支持多值查询，查询条件格式：*healthmonitor_id=xxx&healthmonitor_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The healthmonitor_id of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        r"""Sets the healthmonitor_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组关联的健康检查的ID。 支持多值查询，查询条件格式：*healthmonitor_id=xxx&healthmonitor_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param healthmonitor_id: The healthmonitor_id of this ListMasterSlavePoolsRequest.
        :type healthmonitor_id: list[str]
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def id(self):
        r"""Gets the id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The id of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的ID。 支持多值查询，查询条件格式：*id=xxx&id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param id: The id of this ListMasterSlavePoolsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的名称。 支持多值查询，查询条件格式：*name=xxx&name=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this ListMasterSlavePoolsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def loadbalancer_id(self):
        r"""Gets the loadbalancer_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组绑定的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The loadbalancer_id of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        r"""Sets the loadbalancer_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组绑定的负载均衡器ID。 支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param loadbalancer_id: The loadbalancer_id of this ListMasterSlavePoolsRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol(self):
        r"""Gets the protocol of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的后端协议。 支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  **约束限制**：不涉及  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  **默认取值**：不涉及

        :return: The protocol of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        r"""Sets the protocol of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的后端协议。 支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  **约束限制**：不涉及  **取值范围**：TCP、UDP、[IP、](tag:hws_eu)TLS、GRPC、HTTP、HTTPS和QUIC。  **默认取值**：不涉及

        :param protocol: The protocol of this ListMasterSlavePoolsRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def lb_algorithm(self):
        r"""Gets the lb_algorithm of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的负载均衡算法。 支持多值查询，查询条件格式：*lb_algorithm=xxx&lb_algorithm=xxx*。  **约束限制**：不涉及  **取值范围**： 1、ROUND_ROBIN：加权轮询算法。 2、LEAST_CONNECTIONS：加权最少连接算法。 3、SOURCE_IP：源IP算法。 4、QUIC_CID：连接ID算法。  **默认取值**：不涉及

        :return: The lb_algorithm of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        r"""Sets the lb_algorithm of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的负载均衡算法。 支持多值查询，查询条件格式：*lb_algorithm=xxx&lb_algorithm=xxx*。  **约束限制**：不涉及  **取值范围**： 1、ROUND_ROBIN：加权轮询算法。 2、LEAST_CONNECTIONS：加权最少连接算法。 3、SOURCE_IP：源IP算法。 4、QUIC_CID：连接ID算法。  **默认取值**：不涉及

        :param lb_algorithm: The lb_algorithm of this ListMasterSlavePoolsRequest.
        :type lb_algorithm: list[str]
        """
        self._lb_algorithm = lb_algorithm

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListMasterSlavePoolsRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:pools:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :return: The enterprise_project_id of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListMasterSlavePoolsRequest.

        **参数解释**：资源所属的企业项目ID。 支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  **约束限制**： - 如果enterprise_project_id不传值，默认查询所有企业项目下的资源，鉴权按照细粒度权限鉴权，必须在用户组下分配elb:pools:list权限。 - 如果enterprise_project_id传值，鉴权按照企业项目权限鉴权，分为传入具体eps_id和all_granted_eps两种场景，前者查询指定eps_id的eps下的资源，后者查询的是所有有list权限的eps下的资源。  **取值范围**：不涉及  **默认取值**：不涉及  [不支持该字段，请勿使用。](tag:dt,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListMasterSlavePoolsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        r"""Gets the ip_version of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组支持的IP版本。 支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ip_version of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组支持的IP版本。 支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param ip_version: The ip_version of this ListMasterSlavePoolsRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def member_address(self):
        r"""Gets the member_address of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器的IP地址。 支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_address of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        r"""Sets the member_address of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器的IP地址。 支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_address: The member_address of this ListMasterSlavePoolsRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        r"""Gets the member_device_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器对应的弹性云服务器的ID。 支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_device_id of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        r"""Sets the member_device_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器对应的弹性云服务器的ID。 支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_device_id: The member_device_id of this ListMasterSlavePoolsRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def listener_id(self):
        r"""Gets the listener_id of this ListMasterSlavePoolsRequest.

        **参数解释**：关联的监听器ID，包括通过l7policy关联的。 支持多值查询，查询条件格式：*listener_id=xxx&listener_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The listener_id of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        r"""Sets the listener_id of this ListMasterSlavePoolsRequest.

        **参数解释**：关联的监听器ID，包括通过l7policy关联的。 支持多值查询，查询条件格式：*listener_id=xxx&listener_id=xxx*。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param listener_id: The listener_id of this ListMasterSlavePoolsRequest.
        :type listener_id: list[str]
        """
        self._listener_id = listener_id

    @property
    def member_instance_id(self):
        r"""Gets the member_instance_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器ID。 支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The member_instance_id of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._member_instance_id

    @member_instance_id.setter
    def member_instance_id(self, member_instance_id):
        r"""Sets the member_instance_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器ID。 支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。  **约束限制**：仅用于查询条件，不作为响应参数字段。  **取值范围**：不涉及  **默认取值**：不涉及

        :param member_instance_id: The member_instance_id of this ListMasterSlavePoolsRequest.
        :type member_instance_id: list[str]
        """
        self._member_instance_id = member_instance_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The vpc_id of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组关联的虚拟私有云的ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param vpc_id: The vpc_id of this ListMasterSlavePoolsRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        r"""Gets the type of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的类型。  **约束限制**：不涉及  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端  **默认取值**：不涉及

        :return: The type of this ListMasterSlavePoolsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListMasterSlavePoolsRequest.

        **参数解释**：后端服务器组的类型。  **约束限制**：不涉及  **取值范围**： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加IP类型后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端  **默认取值**：不涉及

        :param type: The type of this ListMasterSlavePoolsRequest.
        :type type: list[str]
        """
        self._type = type

    @property
    def connection_drain(self):
        r"""Gets the connection_drain of this ListMasterSlavePoolsRequest.

        **参数解释**：查询是否开启延迟注销的功能，查询条件格式：*connection_drain=true或者*connection_drain=false  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及

        :return: The connection_drain of this ListMasterSlavePoolsRequest.
        :rtype: bool
        """
        return self._connection_drain

    @connection_drain.setter
    def connection_drain(self, connection_drain):
        r"""Sets the connection_drain of this ListMasterSlavePoolsRequest.

        **参数解释**：查询是否开启延迟注销的功能，查询条件格式：*connection_drain=true或者*connection_drain=false  **约束限制**：不涉及  **取值范围**：true 开启，false 不开启。  **默认取值**：不涉及

        :param connection_drain: The connection_drain of this ListMasterSlavePoolsRequest.
        :type connection_drain: bool
        """
        self._connection_drain = connection_drain

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
        if not isinstance(other, ListMasterSlavePoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
