# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPoolsRequest:

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
        'admin_state_up': 'bool',
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
        'member_deletion_protection_enable': 'bool',
        'listener_id': 'list[str]',
        'member_instance_id': 'list[str]',
        'vpc_id': 'list[str]',
        'type': 'list[str]'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'page_reverse': 'page_reverse',
        'description': 'description',
        'admin_state_up': 'admin_state_up',
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
        'member_deletion_protection_enable': 'member_deletion_protection_enable',
        'listener_id': 'listener_id',
        'member_instance_id': 'member_instance_id',
        'vpc_id': 'vpc_id',
        'type': 'type'
    }

    def __init__(self, marker=None, limit=None, page_reverse=None, description=None, admin_state_up=None, healthmonitor_id=None, id=None, name=None, loadbalancer_id=None, protocol=None, lb_algorithm=None, enterprise_project_id=None, ip_version=None, member_address=None, member_device_id=None, member_deletion_protection_enable=None, listener_id=None, member_instance_id=None, vpc_id=None, type=None):
        """ListPoolsRequest

        The model defined in huaweicloud sdk

        :param marker: 上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。
        :type marker: str
        :param limit: 每页返回的个数。
        :type limit: int
        :param page_reverse: 是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse&#x3D;true时，若要查询上一页，marker取值为当前页返回值的previous_marker。
        :type page_reverse: bool
        :param description: 后端云服务器组的描述信息。  支持多值查询，查询条件格式：*description&#x3D;xxx&amp;description&#x3D;xxx*。
        :type description: list[str]
        :param admin_state_up: 后端云服务器组的管理状态。  不支持该字段，请勿使用。
        :type admin_state_up: bool
        :param healthmonitor_id: 后端云服务器组关联的健康检查的ID。  支持多值查询，查询条件格式：*healthmonitor_id&#x3D;xxx&amp;healthmonitor_id&#x3D;xxx*。
        :type healthmonitor_id: list[str]
        :param id: 后端云服务器组的ID。  支持多值查询，查询条件格式：*id&#x3D;xxx&amp;id&#x3D;xxx*。
        :type id: list[str]
        :param name: 后端云服务器组的名称。  支持多值查询，查询条件格式：*name&#x3D;xxx&amp;name&#x3D;xxx*。
        :type name: list[str]
        :param loadbalancer_id: 后端云服务器组绑定的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id&#x3D;xxx&amp;loadbalancer_id&#x3D;xxx*。
        :type loadbalancer_id: list[str]
        :param protocol: 后端云服务器组的后端协议。  取值：TCP、UDP、HTTP、HTTPS和QUIC。  支持多值查询，查询条件格式：*protocol&#x3D;xxx&amp;protocol&#x3D;xxx*。  [不支持QUIC协议。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)
        :type protocol: list[str]
        :param lb_algorithm: 后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  支持多值查询，查询条件格式：*lb_algorithm&#x3D;xxx&amp;lb_algorithm&#x3D;xxx*。  [不支持QUIC_CID算法。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)
        :type lb_algorithm: list[str]
        :param enterprise_project_id: 企业项目ID。不传时查询default企业项目\&quot;0\&quot;下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id&#x3D;xxx&amp;enterprise_project_id&#x3D;xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)
        :type enterprise_project_id: list[str]
        :param ip_version: 后端云服务器组支持的IP版本。  支持多值查询，查询条件格式：*ip_version&#x3D;xxx&amp;ip_version&#x3D;xxx*。
        :type ip_version: list[str]
        :param member_address: 后端云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address&#x3D;xxx&amp;member_address&#x3D;xxx*。
        :type member_address: list[str]
        :param member_device_id: 后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id&#x3D;xxx&amp;member_device_id&#x3D;xxx*。
        :type member_device_id: list[str]
        :param member_deletion_protection_enable: 是否开启删除保护，false不开启，true开启，不传查询全部。 [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)
        :type member_deletion_protection_enable: bool
        :param listener_id: 关联的监听器ID，包括通过l7policy关联的。  支持多值查询，查询条件格式：*listener_id&#x3D;xxx&amp;listener_id&#x3D;xxx*。
        :type listener_id: list[str]
        :param member_instance_id: 后端云服务器ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_instance_id&#x3D;xxx&amp;member_instance_id&#x3D;xxx*。
        :type member_instance_id: list[str]
        :param vpc_id: 后端云服务器组关联的虚拟私有云的ID。
        :type vpc_id: list[str]
        :param type: 后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\&quot;\&quot;）：允许任意类型的后端
        :type type: list[str]
        """
        
        

        self._marker = None
        self._limit = None
        self._page_reverse = None
        self._description = None
        self._admin_state_up = None
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
        self._member_deletion_protection_enable = None
        self._listener_id = None
        self._member_instance_id = None
        self._vpc_id = None
        self._type = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if description is not None:
            self.description = description
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
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
        if member_deletion_protection_enable is not None:
            self.member_deletion_protection_enable = member_deletion_protection_enable
        if listener_id is not None:
            self.listener_id = listener_id
        if member_instance_id is not None:
            self.member_instance_id = member_instance_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if type is not None:
            self.type = type

    @property
    def marker(self):
        """Gets the marker of this ListPoolsRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :return: The marker of this ListPoolsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListPoolsRequest.

        上一页最后一条记录的ID。  使用说明： - 必须与limit一起使用。 - 不指定时表示查询第一页。 - 该字段不允许为空或无效的ID。

        :param marker: The marker of this ListPoolsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListPoolsRequest.

        每页返回的个数。

        :return: The limit of this ListPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPoolsRequest.

        每页返回的个数。

        :param limit: The limit of this ListPoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def page_reverse(self):
        """Gets the page_reverse of this ListPoolsRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :return: The page_reverse of this ListPoolsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        """Sets the page_reverse of this ListPoolsRequest.

        是否反向查询。  取值： - true：查询上一页。 - false：查询下一页，默认。  使用说明： - 必须与limit一起使用。 - 当page_reverse=true时，若要查询上一页，marker取值为当前页返回值的previous_marker。

        :param page_reverse: The page_reverse of this ListPoolsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def description(self):
        """Gets the description of this ListPoolsRequest.

        后端云服务器组的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :return: The description of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListPoolsRequest.

        后端云服务器组的描述信息。  支持多值查询，查询条件格式：*description=xxx&description=xxx*。

        :param description: The description of this ListPoolsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this ListPoolsRequest.

        后端云服务器组的管理状态。  不支持该字段，请勿使用。

        :return: The admin_state_up of this ListPoolsRequest.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this ListPoolsRequest.

        后端云服务器组的管理状态。  不支持该字段，请勿使用。

        :param admin_state_up: The admin_state_up of this ListPoolsRequest.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def healthmonitor_id(self):
        """Gets the healthmonitor_id of this ListPoolsRequest.

        后端云服务器组关联的健康检查的ID。  支持多值查询，查询条件格式：*healthmonitor_id=xxx&healthmonitor_id=xxx*。

        :return: The healthmonitor_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        """Sets the healthmonitor_id of this ListPoolsRequest.

        后端云服务器组关联的健康检查的ID。  支持多值查询，查询条件格式：*healthmonitor_id=xxx&healthmonitor_id=xxx*。

        :param healthmonitor_id: The healthmonitor_id of this ListPoolsRequest.
        :type healthmonitor_id: list[str]
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def id(self):
        """Gets the id of this ListPoolsRequest.

        后端云服务器组的ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :return: The id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListPoolsRequest.

        后端云服务器组的ID。  支持多值查询，查询条件格式：*id=xxx&id=xxx*。

        :param id: The id of this ListPoolsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListPoolsRequest.

        后端云服务器组的名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :return: The name of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPoolsRequest.

        后端云服务器组的名称。  支持多值查询，查询条件格式：*name=xxx&name=xxx*。

        :param name: The name of this ListPoolsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this ListPoolsRequest.

        后端云服务器组绑定的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。

        :return: The loadbalancer_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this ListPoolsRequest.

        后端云服务器组绑定的负载均衡器ID。  支持多值查询，查询条件格式：*loadbalancer_id=xxx&loadbalancer_id=xxx*。

        :param loadbalancer_id: The loadbalancer_id of this ListPoolsRequest.
        :type loadbalancer_id: list[str]
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def protocol(self):
        """Gets the protocol of this ListPoolsRequest.

        后端云服务器组的后端协议。  取值：TCP、UDP、HTTP、HTTPS和QUIC。  支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  [不支持QUIC协议。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)

        :return: The protocol of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListPoolsRequest.

        后端云服务器组的后端协议。  取值：TCP、UDP、HTTP、HTTPS和QUIC。  支持多值查询，查询条件格式：*protocol=xxx&protocol=xxx*。  [不支持QUIC协议。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)

        :param protocol: The protocol of this ListPoolsRequest.
        :type protocol: list[str]
        """
        self._protocol = protocol

    @property
    def lb_algorithm(self):
        """Gets the lb_algorithm of this ListPoolsRequest.

        后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  支持多值查询，查询条件格式：*lb_algorithm=xxx&lb_algorithm=xxx*。  [不支持QUIC_CID算法。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)

        :return: The lb_algorithm of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._lb_algorithm

    @lb_algorithm.setter
    def lb_algorithm(self, lb_algorithm):
        """Sets the lb_algorithm of this ListPoolsRequest.

        后端云服务器组的负载均衡算法。  取值： - ROUND_ROBIN：加权轮询算法。 - LEAST_CONNECTIONS：加权最少连接算法。 - SOURCE_IP：源IP算法。 - QUIC_CID：连接ID算法。  支持多值查询，查询条件格式：*lb_algorithm=xxx&lb_algorithm=xxx*。  [不支持QUIC_CID算法。](tag:hws_eu,g42,hk_g42,hcso_dt)  [荷兰region不支持QUIC。](tag:dt)

        :param lb_algorithm: The lb_algorithm of this ListPoolsRequest.
        :type lb_algorithm: list[str]
        """
        self._lb_algorithm = lb_algorithm

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListPoolsRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :return: The enterprise_project_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListPoolsRequest.

        企业项目ID。不传时查询default企业项目\"0\"下的资源，鉴权按照default企业项目鉴权； 如果传值，则传已存在的企业项目ID或all_granted_eps（表示查询所有企业项目）进行查询。  支持多值查询，查询条件格式：*enterprise_project_id=xxx&enterprise_project_id=xxx*。  [不支持该字段，请勿使用。](tag:dt,dt_test,hcso_dt)

        :param enterprise_project_id: The enterprise_project_id of this ListPoolsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ip_version(self):
        """Gets the ip_version of this ListPoolsRequest.

        后端云服务器组支持的IP版本。  支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。

        :return: The ip_version of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this ListPoolsRequest.

        后端云服务器组支持的IP版本。  支持多值查询，查询条件格式：*ip_version=xxx&ip_version=xxx*。

        :param ip_version: The ip_version of this ListPoolsRequest.
        :type ip_version: list[str]
        """
        self._ip_version = ip_version

    @property
    def member_address(self):
        """Gets the member_address of this ListPoolsRequest.

        后端云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。

        :return: The member_address of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_address

    @member_address.setter
    def member_address(self, member_address):
        """Sets the member_address of this ListPoolsRequest.

        后端云服务器的IP地址。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_address=xxx&member_address=xxx*。

        :param member_address: The member_address of this ListPoolsRequest.
        :type member_address: list[str]
        """
        self._member_address = member_address

    @property
    def member_device_id(self):
        """Gets the member_device_id of this ListPoolsRequest.

        后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。

        :return: The member_device_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_device_id

    @member_device_id.setter
    def member_device_id(self, member_device_id):
        """Sets the member_device_id of this ListPoolsRequest.

        后端云服务器对应的弹性云服务器的ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_device_id=xxx&member_device_id=xxx*。

        :param member_device_id: The member_device_id of this ListPoolsRequest.
        :type member_device_id: list[str]
        """
        self._member_device_id = member_device_id

    @property
    def member_deletion_protection_enable(self):
        """Gets the member_deletion_protection_enable of this ListPoolsRequest.

        是否开启删除保护，false不开启，true开启，不传查询全部。 [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :return: The member_deletion_protection_enable of this ListPoolsRequest.
        :rtype: bool
        """
        return self._member_deletion_protection_enable

    @member_deletion_protection_enable.setter
    def member_deletion_protection_enable(self, member_deletion_protection_enable):
        """Sets the member_deletion_protection_enable of this ListPoolsRequest.

        是否开启删除保护，false不开启，true开启，不传查询全部。 [不支持该字段，请勿使用。](tag:hws_eu,g42,hk_g42)  [荷兰region不支持该字段，请勿使用。](tag:dt)

        :param member_deletion_protection_enable: The member_deletion_protection_enable of this ListPoolsRequest.
        :type member_deletion_protection_enable: bool
        """
        self._member_deletion_protection_enable = member_deletion_protection_enable

    @property
    def listener_id(self):
        """Gets the listener_id of this ListPoolsRequest.

        关联的监听器ID，包括通过l7policy关联的。  支持多值查询，查询条件格式：*listener_id=xxx&listener_id=xxx*。

        :return: The listener_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ListPoolsRequest.

        关联的监听器ID，包括通过l7policy关联的。  支持多值查询，查询条件格式：*listener_id=xxx&listener_id=xxx*。

        :param listener_id: The listener_id of this ListPoolsRequest.
        :type listener_id: list[str]
        """
        self._listener_id = listener_id

    @property
    def member_instance_id(self):
        """Gets the member_instance_id of this ListPoolsRequest.

        后端云服务器ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。

        :return: The member_instance_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._member_instance_id

    @member_instance_id.setter
    def member_instance_id(self, member_instance_id):
        """Sets the member_instance_id of this ListPoolsRequest.

        后端云服务器ID。仅用于查询条件，不作为响应参数字段。  支持多值查询，查询条件格式：*member_instance_id=xxx&member_instance_id=xxx*。

        :param member_instance_id: The member_instance_id of this ListPoolsRequest.
        :type member_instance_id: list[str]
        """
        self._member_instance_id = member_instance_id

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListPoolsRequest.

        后端云服务器组关联的虚拟私有云的ID。

        :return: The vpc_id of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListPoolsRequest.

        后端云服务器组关联的虚拟私有云的ID。

        :param vpc_id: The vpc_id of this ListPoolsRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def type(self):
        """Gets the type of this ListPoolsRequest.

        后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端

        :return: The type of this ListPoolsRequest.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListPoolsRequest.

        后端服务器组的类型。  取值： - instance：允许任意类型的后端，type指定为该类型时，vpc_id是必选字段。 - ip：只能添加跨VPC后端，type指定为该类型时，vpc_id不允许指定。 - 空字符串（\"\"）：允许任意类型的后端

        :param type: The type of this ListPoolsRequest.
        :type type: list[str]
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
        if not isinstance(other, ListPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
