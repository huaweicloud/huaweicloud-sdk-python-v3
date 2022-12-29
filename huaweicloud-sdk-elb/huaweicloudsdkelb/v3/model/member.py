# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Member:

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
        'project_id': 'str',
        'pool_id': 'str',
        'admin_state_up': 'bool',
        'subnet_cidr_id': 'str',
        'protocol_port': 'int',
        'weight': 'int',
        'address': 'str',
        'ip_version': 'str',
        'device_owner': 'str',
        'device_id': 'str',
        'operating_status': 'str',
        'status': 'list[MemberStatus]',
        'loadbalancer_id': 'str',
        'loadbalancers': 'list[ResourceID]',
        'created_at': 'str',
        'updated_at': 'str',
        'member_type': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'pool_id': 'pool_id',
        'admin_state_up': 'admin_state_up',
        'subnet_cidr_id': 'subnet_cidr_id',
        'protocol_port': 'protocol_port',
        'weight': 'weight',
        'address': 'address',
        'ip_version': 'ip_version',
        'device_owner': 'device_owner',
        'device_id': 'device_id',
        'operating_status': 'operating_status',
        'status': 'status',
        'loadbalancer_id': 'loadbalancer_id',
        'loadbalancers': 'loadbalancers',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'member_type': 'member_type',
        'instance_id': 'instance_id'
    }

    def __init__(self, id=None, name=None, project_id=None, pool_id=None, admin_state_up=None, subnet_cidr_id=None, protocol_port=None, weight=None, address=None, ip_version=None, device_owner=None, device_id=None, operating_status=None, status=None, loadbalancer_id=None, loadbalancers=None, created_at=None, updated_at=None, member_type=None, instance_id=None):
        """Member

        The model defined in huaweicloud sdk

        :param id: 后端服务器ID。 &gt;说明： 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。
        :type id: str
        :param name: 后端服务器名称。
        :type name: str
        :param project_id: 后端服务器所在的项目ID。
        :type project_id: str
        :param pool_id: 所在后端服务器组ID。  不支持该字段，请勿使用。
        :type pool_id: str
        :param admin_state_up: 后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。
        :type admin_state_up: bool
        :param subnet_cidr_id: 后端云服务器所在子网的IPv4子网ID或IPv6子网ID。  若所属的LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。 此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。  使用说明：该子网和关联的负载均衡器的子网必须在同一VPC下。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)
        :type subnet_cidr_id: str
        :param protocol_port: 后端服务器业务端口号。
        :type protocol_port: int
        :param weight: 后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。
        :type weight: int
        :param address: 后端服务器对应的IP地址。  使用说明： - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址可以是IPv4或IPv6。 但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡IP。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)
        :type address: str
        :param ip_version: 当前后端服务器的IP地址版本，由后端系统自动根据传入的address字段确定。取值：v4、v6。
        :type ip_version: str
        :param device_owner: 设备所有者。  取值： - 空，表示后端服务器未关联到ECS。 - compute:{az_name}，表示关联到ECS，其中{az_name}表示ECS所在可用区名。  不支持该字段，请勿使用。
        :type device_owner: str
        :param device_id: 关联的ECS ID，为空表示后端服务器未关联到ECS。  不支持该字段，请勿使用。
        :type device_id: str
        :param operating_status: 后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。
        :type operating_status: str
        :param status: 后端云服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_stauts为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。
        :type status: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        :param loadbalancer_id: 所属负载均衡器ID。  不支持该字段，请勿使用。
        :type loadbalancer_id: str
        :param loadbalancers: 后端云服务器关联的负载均衡器ID列表。  不支持该字段，请勿使用。
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.ResourceID`]
        :param created_at: 创建时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)
        :type created_at: str
        :param updated_at: 更新时间。格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)
        :type updated_at: str
        :param member_type: 后端云服务器的类型。  取值： - ip：跨VPC的member。 - instance：关联到ECS的member。
        :type member_type: str
        :param instance_id: member关联的实例ID。空表示member关联的实例为非真实设备 （如：跨VPC场景）
        :type instance_id: str
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._pool_id = None
        self._admin_state_up = None
        self._subnet_cidr_id = None
        self._protocol_port = None
        self._weight = None
        self._address = None
        self._ip_version = None
        self._device_owner = None
        self._device_id = None
        self._operating_status = None
        self._status = None
        self._loadbalancer_id = None
        self._loadbalancers = None
        self._created_at = None
        self._updated_at = None
        self._member_type = None
        self._instance_id = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.project_id = project_id
        if pool_id is not None:
            self.pool_id = pool_id
        self.admin_state_up = admin_state_up
        if subnet_cidr_id is not None:
            self.subnet_cidr_id = subnet_cidr_id
        self.protocol_port = protocol_port
        self.weight = weight
        self.address = address
        self.ip_version = ip_version
        if device_owner is not None:
            self.device_owner = device_owner
        if device_id is not None:
            self.device_id = device_id
        self.operating_status = operating_status
        self.status = status
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id
        if loadbalancers is not None:
            self.loadbalancers = loadbalancers
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if member_type is not None:
            self.member_type = member_type
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def id(self):
        """Gets the id of this Member.

        后端服务器ID。 >说明： 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :return: The id of this Member.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Member.

        后端服务器ID。 >说明： 此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :param id: The id of this Member.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Member.

        后端服务器名称。

        :return: The name of this Member.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Member.

        后端服务器名称。

        :param name: The name of this Member.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this Member.

        后端服务器所在的项目ID。

        :return: The project_id of this Member.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Member.

        后端服务器所在的项目ID。

        :param project_id: The project_id of this Member.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def pool_id(self):
        """Gets the pool_id of this Member.

        所在后端服务器组ID。  不支持该字段，请勿使用。

        :return: The pool_id of this Member.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Member.

        所在后端服务器组ID。  不支持该字段，请勿使用。

        :param pool_id: The pool_id of this Member.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this Member.

        后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :return: The admin_state_up of this Member.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this Member.

        后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。

        :param admin_state_up: The admin_state_up of this Member.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def subnet_cidr_id(self):
        """Gets the subnet_cidr_id of this Member.

        后端云服务器所在子网的IPv4子网ID或IPv6子网ID。  若所属的LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。 此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。  使用说明：该子网和关联的负载均衡器的子网必须在同一VPC下。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)

        :return: The subnet_cidr_id of this Member.
        :rtype: str
        """
        return self._subnet_cidr_id

    @subnet_cidr_id.setter
    def subnet_cidr_id(self, subnet_cidr_id):
        """Sets the subnet_cidr_id of this Member.

        后端云服务器所在子网的IPv4子网ID或IPv6子网ID。  若所属的LB的跨VPC后端转发特性已开启，则该字段可以不传，表示添加跨VPC的后端服务器。 此时address必须为IPv4地址，所在的pool的协议必须为TCP/HTTP/HTTPS。  使用说明：该子网和关联的负载均衡器的子网必须在同一VPC下。  [不支持IPv6，请勿设置为IPv6子网ID。](tag:dt,dt_test)

        :param subnet_cidr_id: The subnet_cidr_id of this Member.
        :type subnet_cidr_id: str
        """
        self._subnet_cidr_id = subnet_cidr_id

    @property
    def protocol_port(self):
        """Gets the protocol_port of this Member.

        后端服务器业务端口号。

        :return: The protocol_port of this Member.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this Member.

        后端服务器业务端口号。

        :param protocol_port: The protocol_port of this Member.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        """Gets the weight of this Member.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。

        :return: The weight of this Member.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this Member.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。

        :param weight: The weight of this Member.
        :type weight: int
        """
        self._weight = weight

    @property
    def address(self):
        """Gets the address of this Member.

        后端服务器对应的IP地址。  使用说明： - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址可以是IPv4或IPv6。 但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡IP。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :return: The address of this Member.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Member.

        后端服务器对应的IP地址。  使用说明： - 若subnet_cidr_id为空，表示添加跨VPC后端，此时address必须为IPv4地址。 - 若subnet_cidr_id不为空，表示是一个关联到ECS的后端服务器。该IP地址可以是IPv4或IPv6。 但必须在subnet_cidr_id对应的子网网段中。且只能指定为关联ECS的主网卡IP。  [不支持IPv6，请勿设置为IPv6地址。](tag:dt,dt_test)

        :param address: The address of this Member.
        :type address: str
        """
        self._address = address

    @property
    def ip_version(self):
        """Gets the ip_version of this Member.

        当前后端服务器的IP地址版本，由后端系统自动根据传入的address字段确定。取值：v4、v6。

        :return: The ip_version of this Member.
        :rtype: str
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this Member.

        当前后端服务器的IP地址版本，由后端系统自动根据传入的address字段确定。取值：v4、v6。

        :param ip_version: The ip_version of this Member.
        :type ip_version: str
        """
        self._ip_version = ip_version

    @property
    def device_owner(self):
        """Gets the device_owner of this Member.

        设备所有者。  取值： - 空，表示后端服务器未关联到ECS。 - compute:{az_name}，表示关联到ECS，其中{az_name}表示ECS所在可用区名。  不支持该字段，请勿使用。

        :return: The device_owner of this Member.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this Member.

        设备所有者。  取值： - 空，表示后端服务器未关联到ECS。 - compute:{az_name}，表示关联到ECS，其中{az_name}表示ECS所在可用区名。  不支持该字段，请勿使用。

        :param device_owner: The device_owner of this Member.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def device_id(self):
        """Gets the device_id of this Member.

        关联的ECS ID，为空表示后端服务器未关联到ECS。  不支持该字段，请勿使用。

        :return: The device_id of this Member.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Member.

        关联的ECS ID，为空表示后端服务器未关联到ECS。  不支持该字段，请勿使用。

        :param device_id: The device_id of this Member.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def operating_status(self):
        """Gets the operating_status of this Member.

        后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。

        :return: The operating_status of this Member.
        :rtype: str
        """
        return self._operating_status

    @operating_status.setter
    def operating_status(self, operating_status):
        """Sets the operating_status of this Member.

        后端云服务器的健康状态。  取值： - ONLINE：后端云服务器正常。 - NO_MONITOR：后端云服务器所在的服务器组没有健康检查器。 - OFFLINE：后端云服务器关联的ECS服务器不存在或已关机。

        :param operating_status: The operating_status of this Member.
        :type operating_status: str
        """
        self._operating_status = operating_status

    @property
    def status(self):
        """Gets the status of this Member.

        后端云服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_stauts为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。

        :return: The status of this Member.
        :rtype: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Member.

        后端云服务器监听器粒度的的健康状态。 若绑定的监听器在该字段中，则以该字段中监听器对应的operating_stauts为准。 若绑定的监听器不在该字段中，则以外层的operating_status为准。

        :param status: The status of this Member.
        :type status: list[:class:`huaweicloudsdkelb.v3.MemberStatus`]
        """
        self._status = status

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this Member.

        所属负载均衡器ID。  不支持该字段，请勿使用。

        :return: The loadbalancer_id of this Member.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this Member.

        所属负载均衡器ID。  不支持该字段，请勿使用。

        :param loadbalancer_id: The loadbalancer_id of this Member.
        :type loadbalancer_id: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def loadbalancers(self):
        """Gets the loadbalancers of this Member.

        后端云服务器关联的负载均衡器ID列表。  不支持该字段，请勿使用。

        :return: The loadbalancers of this Member.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ResourceID`]
        """
        return self._loadbalancers

    @loadbalancers.setter
    def loadbalancers(self, loadbalancers):
        """Sets the loadbalancers of this Member.

        后端云服务器关联的负载均衡器ID列表。  不支持该字段，请勿使用。

        :param loadbalancers: The loadbalancers of this Member.
        :type loadbalancers: list[:class:`huaweicloudsdkelb.v3.ResourceID`]
        """
        self._loadbalancers = loadbalancers

    @property
    def created_at(self):
        """Gets the created_at of this Member.

        创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :return: The created_at of this Member.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Member.

        创建时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :param created_at: The created_at of this Member.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Member.

        更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :return: The updated_at of this Member.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Member.

        更新时间。格式：yyyy-MM-dd'T'HH:mm:ss'Z'，UTC时区。  [注意：独享型实例的历史数据以及共享型实例下的资源，不返回该字段。 ](tag:hws,hws_hk,ocb,ctc,g42,tm,cmcc,hk_g42,hws_ocb,fcs,dt,hk_tm)

        :param updated_at: The updated_at of this Member.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def member_type(self):
        """Gets the member_type of this Member.

        后端云服务器的类型。  取值： - ip：跨VPC的member。 - instance：关联到ECS的member。

        :return: The member_type of this Member.
        :rtype: str
        """
        return self._member_type

    @member_type.setter
    def member_type(self, member_type):
        """Sets the member_type of this Member.

        后端云服务器的类型。  取值： - ip：跨VPC的member。 - instance：关联到ECS的member。

        :param member_type: The member_type of this Member.
        :type member_type: str
        """
        self._member_type = member_type

    @property
    def instance_id(self):
        """Gets the instance_id of this Member.

        member关联的实例ID。空表示member关联的实例为非真实设备 （如：跨VPC场景）

        :return: The instance_id of this Member.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Member.

        member关联的实例ID。空表示member关联的实例为非真实设备 （如：跨VPC场景）

        :param instance_id: The instance_id of this Member.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, Member):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
