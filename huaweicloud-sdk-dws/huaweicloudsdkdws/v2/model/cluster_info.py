# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterInfo:

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
        'version': 'str',
        'updated': 'str',
        'created': 'str',
        'port': 'int',
        'endpoints': 'list[Endpoints]',
        'nodes': 'list[Nodes]',
        'tags': 'list[Tags]',
        'user_name': 'str',
        'number_of_node': 'int',
        'recent_event': 'int',
        'availability_zone': 'str',
        'enterprise_project_id': 'str',
        'node_type': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'public_ip': 'PublicIp',
        'public_endpoints': 'list[PublicEndpoints]',
        'action_progress': 'dict(str, str)',
        'sub_status': 'str',
        'task_status': 'str',
        'security_group_id': 'str',
        'failed_reasons': 'FailedReason'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'version': 'version',
        'updated': 'updated',
        'created': 'created',
        'port': 'port',
        'endpoints': 'endpoints',
        'nodes': 'nodes',
        'tags': 'tags',
        'user_name': 'user_name',
        'number_of_node': 'number_of_node',
        'recent_event': 'recent_event',
        'availability_zone': 'availability_zone',
        'enterprise_project_id': 'enterprise_project_id',
        'node_type': 'node_type',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'public_ip': 'public_ip',
        'public_endpoints': 'public_endpoints',
        'action_progress': 'action_progress',
        'sub_status': 'sub_status',
        'task_status': 'task_status',
        'security_group_id': 'security_group_id',
        'failed_reasons': 'failed_reasons'
    }

    def __init__(self, id=None, name=None, status=None, version=None, updated=None, created=None, port=None, endpoints=None, nodes=None, tags=None, user_name=None, number_of_node=None, recent_event=None, availability_zone=None, enterprise_project_id=None, node_type=None, vpc_id=None, subnet_id=None, public_ip=None, public_endpoints=None, action_progress=None, sub_status=None, task_status=None, security_group_id=None, failed_reasons=None):
        """ClusterInfo

        The model defined in huaweicloud sdk

        :param id: 集群ID。
        :type id: str
        :param name: 集群名称
        :type name: str
        :param status: 集群状态，有效值包括： - CREATING：创建中 - ACTIVE：可用 - FAILED：不可用 - CREATE_FAILED：创建失败 - DELETING：删除中 - DELETE_FAILED：删除失败 - DELETED：已删除 - FROZEN：已冻结
        :type status: str
        :param version: 数据仓库版本
        :type version: str
        :param updated: 集群上次修改时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type updated: str
        :param created: 集群创建时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ。
        :type created: str
        :param port: 集群服务端口。
        :type port: int
        :param endpoints: 集群的内网连接信息
        :type endpoints: list[:class:`huaweicloudsdkdws.v2.Endpoints`]
        :param nodes: 集群实例
        :type nodes: list[:class:`huaweicloudsdkdws.v2.Nodes`]
        :param tags: 集群标签
        :type tags: list[:class:`huaweicloudsdkdws.v2.Tags`]
        :param user_name: 管理员用户名
        :type user_name: str
        :param number_of_node: 节点数量
        :type number_of_node: int
        :param recent_event: 事件数
        :type recent_event: int
        :param availability_zone: 可用区
        :type availability_zone: str
        :param enterprise_project_id: 企业项目ID。值为0表示默认企业项目“default”
        :type enterprise_project_id: str
        :param node_type: 节点类型
        :type node_type: str
        :param vpc_id: 虚拟私有云ID
        :type vpc_id: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param public_ip: 
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        :param public_endpoints: 集群的公网连接信息，如果未指定，则默认不使用公网连接信息。
        :type public_endpoints: list[:class:`huaweicloudsdkdws.v2.PublicEndpoints`]
        :param action_progress: 任务信息，由key、value组成。key值为正在进行的任务，value值为正在进行任务的进度。key值的有效值包括： - CREATING：创建中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - ADD_CN_ING：增加CN中 - DEL_CN_ING：删除CN中 - REDISTRIBUTING：重分布中 - ELB_BINDING：弹性负载均衡绑定中 - ELB_UNBINDING：弹性负载均衡解绑中 - ELB_SWITCHING：弹性负载均衡切换中 - NETWORK_CONFIGURING：网络配置中 - DISK_EXPANDING：磁盘扩容中 - ACTIVE_STANDY_SWITCHOVER：主备恢复中 - CLUSTER_SHRINKING：缩容中 - SHRINK_CHECKING：缩容检测中 - FLAVOR_RESIZING：规格变更中 - MANAGE_IP_BINDING：登录开通中 - FINE_GRAINED_RESTORING：细粒度恢复中 - DR_RECOVERING：容灾恢复中 - REPAIRING：修复中
        :type action_progress: dict(str, str)
        :param sub_status: “可用”集群状态的子状态，有效值包括：  - NORMAL：正常 - READONLY：只读 - REDISTRIBUTING：重分布中 - REDISTRIBUTION-FAILURE：重分布失败 - UNBALANCED：非均衡 - UNBALANCED | READONLY：非均衡，只读 - DEGRADED：节点故障 - DEGRADED | READONLY：节点故障，只读 - DEGRADED | UNBALANCED：节点故障，非均衡 - UNBALANCED | REDISTRIBUTING：非均衡，重分布中 - UNBALANCED | REDISTRIBUTION-FAILURE：非均衡，重分布失败 - READONLY | REDISTRIBUTION-FAILURE：只读，重分布失败 - UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：非均衡，只读，重分布失败 - DEGRADED | REDISTRIBUTION-FAILURE：节点故障，重分布失败 - DEGRADED | UNBALANCED | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY：节点故障，非均衡，只读
        :type sub_status: str
        :param task_status: 集群管理任务，有效值包括： - UNFREEZING：解冻中 - FREEZING：冻结中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - DELETING_EXT_DATASOURCE：删除MRS连接 - REBOOT_FAILURE：重启失败 - RESIZE_FAILURE：扩容失败 - ADD_CN_ING：增加CN中 - DEL_CN_ING：删除CN中 - CREATING_NODE：添加节点 - CREATE_NODE_FAILED：添加节点失败 - DELETING_NODE：删除节点 - DELETE_NODE_FAILED：删除节点失败 - REDISTRIBUTING：重分布中 - REDISTRIBUTE_FAILURE：重分布失败 - WAITING_REDISTRIBUTION：待重分布 - REDISTRIBUTION_PAUSED：重分布暂停 - ELB_BINDING：弹性负载均衡绑定中 - ELB_BIND_FAILED：弹性负载均衡绑定失败 - ELB_UNBINDING：弹性负载均衡解绑中 - ELB_UNBIND_FAILED：弹性负载均衡解绑失败 - ELB_SWITCHING：弹性负载均衡切换中 - ELB_SWITCHING_FAILED：弹性负载均衡切换失败 - NETWORK_CONFIGURING：网络配置中 - NETWORK_CONFIG_FAILED：网络配置失败 - DISK_EXPAND_FAILED：磁盘扩容失败 - DISK_EXPANDING：磁盘扩容中 - ACTIVE_STANDY_SWITCHOVER：主备恢复中 - ACTIVE_STANDY_SWITCHOVER_FAILURE：主备恢复失败 - CLUSTER_SHRINK_FAILED：缩容失败 - CLUSTER_SHRINKING：缩容中 - SHRINK_CHECK_FAILED：缩容检测失败 - SHRINK_CHECKING：缩容检测中 - FLAVOR_RESIZING_FAILED：规格变更失败 - FLAVOR_RESIZING：规格变更中 - MANAGE_IP_BIND_FAILED：登录开通失败 - MANAGE_IP_BINDING：登录开通中 - ORDER_PENDING：订单待支付 - FINE_GRAINED_RESTORING：细粒度恢复中 - DR_RECOVERING：容灾恢复中
        :type task_status: str
        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param failed_reasons: 
        :type failed_reasons: :class:`huaweicloudsdkdws.v2.FailedReason`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._version = None
        self._updated = None
        self._created = None
        self._port = None
        self._endpoints = None
        self._nodes = None
        self._tags = None
        self._user_name = None
        self._number_of_node = None
        self._recent_event = None
        self._availability_zone = None
        self._enterprise_project_id = None
        self._node_type = None
        self._vpc_id = None
        self._subnet_id = None
        self._public_ip = None
        self._public_endpoints = None
        self._action_progress = None
        self._sub_status = None
        self._task_status = None
        self._security_group_id = None
        self._failed_reasons = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.version = version
        self.updated = updated
        self.created = created
        self.port = port
        self.endpoints = endpoints
        self.nodes = nodes
        self.tags = tags
        self.user_name = user_name
        self.number_of_node = number_of_node
        self.recent_event = recent_event
        self.availability_zone = availability_zone
        self.enterprise_project_id = enterprise_project_id
        self.node_type = node_type
        self.vpc_id = vpc_id
        self.subnet_id = subnet_id
        self.public_ip = public_ip
        self.public_endpoints = public_endpoints
        self.action_progress = action_progress
        self.sub_status = sub_status
        self.task_status = task_status
        self.security_group_id = security_group_id
        if failed_reasons is not None:
            self.failed_reasons = failed_reasons

    @property
    def id(self):
        """Gets the id of this ClusterInfo.

        集群ID。

        :return: The id of this ClusterInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterInfo.

        集群ID。

        :param id: The id of this ClusterInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusterInfo.

        集群名称

        :return: The name of this ClusterInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterInfo.

        集群名称

        :param name: The name of this ClusterInfo.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ClusterInfo.

        集群状态，有效值包括： - CREATING：创建中 - ACTIVE：可用 - FAILED：不可用 - CREATE_FAILED：创建失败 - DELETING：删除中 - DELETE_FAILED：删除失败 - DELETED：已删除 - FROZEN：已冻结

        :return: The status of this ClusterInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterInfo.

        集群状态，有效值包括： - CREATING：创建中 - ACTIVE：可用 - FAILED：不可用 - CREATE_FAILED：创建失败 - DELETING：删除中 - DELETE_FAILED：删除失败 - DELETED：已删除 - FROZEN：已冻结

        :param status: The status of this ClusterInfo.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        """Gets the version of this ClusterInfo.

        数据仓库版本

        :return: The version of this ClusterInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterInfo.

        数据仓库版本

        :param version: The version of this ClusterInfo.
        :type version: str
        """
        self._version = version

    @property
    def updated(self):
        """Gets the updated of this ClusterInfo.

        集群上次修改时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The updated of this ClusterInfo.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ClusterInfo.

        集群上次修改时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param updated: The updated of this ClusterInfo.
        :type updated: str
        """
        self._updated = updated

    @property
    def created(self):
        """Gets the created of this ClusterInfo.

        集群创建时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ。

        :return: The created of this ClusterInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ClusterInfo.

        集群创建时间，格式为 ISO8601：YYYY-MM-DDThh:mm:ssZ。

        :param created: The created of this ClusterInfo.
        :type created: str
        """
        self._created = created

    @property
    def port(self):
        """Gets the port of this ClusterInfo.

        集群服务端口。

        :return: The port of this ClusterInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ClusterInfo.

        集群服务端口。

        :param port: The port of this ClusterInfo.
        :type port: int
        """
        self._port = port

    @property
    def endpoints(self):
        """Gets the endpoints of this ClusterInfo.

        集群的内网连接信息

        :return: The endpoints of this ClusterInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Endpoints`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this ClusterInfo.

        集群的内网连接信息

        :param endpoints: The endpoints of this ClusterInfo.
        :type endpoints: list[:class:`huaweicloudsdkdws.v2.Endpoints`]
        """
        self._endpoints = endpoints

    @property
    def nodes(self):
        """Gets the nodes of this ClusterInfo.

        集群实例

        :return: The nodes of this ClusterInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Nodes`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ClusterInfo.

        集群实例

        :param nodes: The nodes of this ClusterInfo.
        :type nodes: list[:class:`huaweicloudsdkdws.v2.Nodes`]
        """
        self._nodes = nodes

    @property
    def tags(self):
        """Gets the tags of this ClusterInfo.

        集群标签

        :return: The tags of this ClusterInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ClusterInfo.

        集群标签

        :param tags: The tags of this ClusterInfo.
        :type tags: list[:class:`huaweicloudsdkdws.v2.Tags`]
        """
        self._tags = tags

    @property
    def user_name(self):
        """Gets the user_name of this ClusterInfo.

        管理员用户名

        :return: The user_name of this ClusterInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ClusterInfo.

        管理员用户名

        :param user_name: The user_name of this ClusterInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def number_of_node(self):
        """Gets the number_of_node of this ClusterInfo.

        节点数量

        :return: The number_of_node of this ClusterInfo.
        :rtype: int
        """
        return self._number_of_node

    @number_of_node.setter
    def number_of_node(self, number_of_node):
        """Sets the number_of_node of this ClusterInfo.

        节点数量

        :param number_of_node: The number_of_node of this ClusterInfo.
        :type number_of_node: int
        """
        self._number_of_node = number_of_node

    @property
    def recent_event(self):
        """Gets the recent_event of this ClusterInfo.

        事件数

        :return: The recent_event of this ClusterInfo.
        :rtype: int
        """
        return self._recent_event

    @recent_event.setter
    def recent_event(self, recent_event):
        """Sets the recent_event of this ClusterInfo.

        事件数

        :param recent_event: The recent_event of this ClusterInfo.
        :type recent_event: int
        """
        self._recent_event = recent_event

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ClusterInfo.

        可用区

        :return: The availability_zone of this ClusterInfo.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ClusterInfo.

        可用区

        :param availability_zone: The availability_zone of this ClusterInfo.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ClusterInfo.

        企业项目ID。值为0表示默认企业项目“default”

        :return: The enterprise_project_id of this ClusterInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ClusterInfo.

        企业项目ID。值为0表示默认企业项目“default”

        :param enterprise_project_id: The enterprise_project_id of this ClusterInfo.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def node_type(self):
        """Gets the node_type of this ClusterInfo.

        节点类型

        :return: The node_type of this ClusterInfo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ClusterInfo.

        节点类型

        :param node_type: The node_type of this ClusterInfo.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ClusterInfo.

        虚拟私有云ID

        :return: The vpc_id of this ClusterInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ClusterInfo.

        虚拟私有云ID

        :param vpc_id: The vpc_id of this ClusterInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ClusterInfo.

        子网ID

        :return: The subnet_id of this ClusterInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ClusterInfo.

        子网ID

        :param subnet_id: The subnet_id of this ClusterInfo.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def public_ip(self):
        """Gets the public_ip of this ClusterInfo.

        :return: The public_ip of this ClusterInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ClusterInfo.

        :param public_ip: The public_ip of this ClusterInfo.
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def public_endpoints(self):
        """Gets the public_endpoints of this ClusterInfo.

        集群的公网连接信息，如果未指定，则默认不使用公网连接信息。

        :return: The public_endpoints of this ClusterInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.PublicEndpoints`]
        """
        return self._public_endpoints

    @public_endpoints.setter
    def public_endpoints(self, public_endpoints):
        """Sets the public_endpoints of this ClusterInfo.

        集群的公网连接信息，如果未指定，则默认不使用公网连接信息。

        :param public_endpoints: The public_endpoints of this ClusterInfo.
        :type public_endpoints: list[:class:`huaweicloudsdkdws.v2.PublicEndpoints`]
        """
        self._public_endpoints = public_endpoints

    @property
    def action_progress(self):
        """Gets the action_progress of this ClusterInfo.

        任务信息，由key、value组成。key值为正在进行的任务，value值为正在进行任务的进度。key值的有效值包括： - CREATING：创建中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - ADD_CN_ING：增加CN中 - DEL_CN_ING：删除CN中 - REDISTRIBUTING：重分布中 - ELB_BINDING：弹性负载均衡绑定中 - ELB_UNBINDING：弹性负载均衡解绑中 - ELB_SWITCHING：弹性负载均衡切换中 - NETWORK_CONFIGURING：网络配置中 - DISK_EXPANDING：磁盘扩容中 - ACTIVE_STANDY_SWITCHOVER：主备恢复中 - CLUSTER_SHRINKING：缩容中 - SHRINK_CHECKING：缩容检测中 - FLAVOR_RESIZING：规格变更中 - MANAGE_IP_BINDING：登录开通中 - FINE_GRAINED_RESTORING：细粒度恢复中 - DR_RECOVERING：容灾恢复中 - REPAIRING：修复中

        :return: The action_progress of this ClusterInfo.
        :rtype: dict(str, str)
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this ClusterInfo.

        任务信息，由key、value组成。key值为正在进行的任务，value值为正在进行任务的进度。key值的有效值包括： - CREATING：创建中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - ADD_CN_ING：增加CN中 - DEL_CN_ING：删除CN中 - REDISTRIBUTING：重分布中 - ELB_BINDING：弹性负载均衡绑定中 - ELB_UNBINDING：弹性负载均衡解绑中 - ELB_SWITCHING：弹性负载均衡切换中 - NETWORK_CONFIGURING：网络配置中 - DISK_EXPANDING：磁盘扩容中 - ACTIVE_STANDY_SWITCHOVER：主备恢复中 - CLUSTER_SHRINKING：缩容中 - SHRINK_CHECKING：缩容检测中 - FLAVOR_RESIZING：规格变更中 - MANAGE_IP_BINDING：登录开通中 - FINE_GRAINED_RESTORING：细粒度恢复中 - DR_RECOVERING：容灾恢复中 - REPAIRING：修复中

        :param action_progress: The action_progress of this ClusterInfo.
        :type action_progress: dict(str, str)
        """
        self._action_progress = action_progress

    @property
    def sub_status(self):
        """Gets the sub_status of this ClusterInfo.

        “可用”集群状态的子状态，有效值包括：  - NORMAL：正常 - READONLY：只读 - REDISTRIBUTING：重分布中 - REDISTRIBUTION-FAILURE：重分布失败 - UNBALANCED：非均衡 - UNBALANCED | READONLY：非均衡，只读 - DEGRADED：节点故障 - DEGRADED | READONLY：节点故障，只读 - DEGRADED | UNBALANCED：节点故障，非均衡 - UNBALANCED | REDISTRIBUTING：非均衡，重分布中 - UNBALANCED | REDISTRIBUTION-FAILURE：非均衡，重分布失败 - READONLY | REDISTRIBUTION-FAILURE：只读，重分布失败 - UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：非均衡，只读，重分布失败 - DEGRADED | REDISTRIBUTION-FAILURE：节点故障，重分布失败 - DEGRADED | UNBALANCED | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY：节点故障，非均衡，只读

        :return: The sub_status of this ClusterInfo.
        :rtype: str
        """
        return self._sub_status

    @sub_status.setter
    def sub_status(self, sub_status):
        """Sets the sub_status of this ClusterInfo.

        “可用”集群状态的子状态，有效值包括：  - NORMAL：正常 - READONLY：只读 - REDISTRIBUTING：重分布中 - REDISTRIBUTION-FAILURE：重分布失败 - UNBALANCED：非均衡 - UNBALANCED | READONLY：非均衡，只读 - DEGRADED：节点故障 - DEGRADED | READONLY：节点故障，只读 - DEGRADED | UNBALANCED：节点故障，非均衡 - UNBALANCED | REDISTRIBUTING：非均衡，重分布中 - UNBALANCED | REDISTRIBUTION-FAILURE：非均衡，重分布失败 - READONLY | REDISTRIBUTION-FAILURE：只读，重分布失败 - UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：非均衡，只读，重分布失败 - DEGRADED | REDISTRIBUTION-FAILURE：节点故障，重分布失败 - DEGRADED | UNBALANCED | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY：节点故障，非均衡，只读

        :param sub_status: The sub_status of this ClusterInfo.
        :type sub_status: str
        """
        self._sub_status = sub_status

    @property
    def task_status(self):
        """Gets the task_status of this ClusterInfo.

        集群管理任务，有效值包括： - UNFREEZING：解冻中 - FREEZING：冻结中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - DELETING_EXT_DATASOURCE：删除MRS连接 - REBOOT_FAILURE：重启失败 - RESIZE_FAILURE：扩容失败 - ADD_CN_ING：增加CN中 - DEL_CN_ING：删除CN中 - CREATING_NODE：添加节点 - CREATE_NODE_FAILED：添加节点失败 - DELETING_NODE：删除节点 - DELETE_NODE_FAILED：删除节点失败 - REDISTRIBUTING：重分布中 - REDISTRIBUTE_FAILURE：重分布失败 - WAITING_REDISTRIBUTION：待重分布 - REDISTRIBUTION_PAUSED：重分布暂停 - ELB_BINDING：弹性负载均衡绑定中 - ELB_BIND_FAILED：弹性负载均衡绑定失败 - ELB_UNBINDING：弹性负载均衡解绑中 - ELB_UNBIND_FAILED：弹性负载均衡解绑失败 - ELB_SWITCHING：弹性负载均衡切换中 - ELB_SWITCHING_FAILED：弹性负载均衡切换失败 - NETWORK_CONFIGURING：网络配置中 - NETWORK_CONFIG_FAILED：网络配置失败 - DISK_EXPAND_FAILED：磁盘扩容失败 - DISK_EXPANDING：磁盘扩容中 - ACTIVE_STANDY_SWITCHOVER：主备恢复中 - ACTIVE_STANDY_SWITCHOVER_FAILURE：主备恢复失败 - CLUSTER_SHRINK_FAILED：缩容失败 - CLUSTER_SHRINKING：缩容中 - SHRINK_CHECK_FAILED：缩容检测失败 - SHRINK_CHECKING：缩容检测中 - FLAVOR_RESIZING_FAILED：规格变更失败 - FLAVOR_RESIZING：规格变更中 - MANAGE_IP_BIND_FAILED：登录开通失败 - MANAGE_IP_BINDING：登录开通中 - ORDER_PENDING：订单待支付 - FINE_GRAINED_RESTORING：细粒度恢复中 - DR_RECOVERING：容灾恢复中

        :return: The task_status of this ClusterInfo.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ClusterInfo.

        集群管理任务，有效值包括： - UNFREEZING：解冻中 - FREEZING：冻结中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - DELETING_EXT_DATASOURCE：删除MRS连接 - REBOOT_FAILURE：重启失败 - RESIZE_FAILURE：扩容失败 - ADD_CN_ING：增加CN中 - DEL_CN_ING：删除CN中 - CREATING_NODE：添加节点 - CREATE_NODE_FAILED：添加节点失败 - DELETING_NODE：删除节点 - DELETE_NODE_FAILED：删除节点失败 - REDISTRIBUTING：重分布中 - REDISTRIBUTE_FAILURE：重分布失败 - WAITING_REDISTRIBUTION：待重分布 - REDISTRIBUTION_PAUSED：重分布暂停 - ELB_BINDING：弹性负载均衡绑定中 - ELB_BIND_FAILED：弹性负载均衡绑定失败 - ELB_UNBINDING：弹性负载均衡解绑中 - ELB_UNBIND_FAILED：弹性负载均衡解绑失败 - ELB_SWITCHING：弹性负载均衡切换中 - ELB_SWITCHING_FAILED：弹性负载均衡切换失败 - NETWORK_CONFIGURING：网络配置中 - NETWORK_CONFIG_FAILED：网络配置失败 - DISK_EXPAND_FAILED：磁盘扩容失败 - DISK_EXPANDING：磁盘扩容中 - ACTIVE_STANDY_SWITCHOVER：主备恢复中 - ACTIVE_STANDY_SWITCHOVER_FAILURE：主备恢复失败 - CLUSTER_SHRINK_FAILED：缩容失败 - CLUSTER_SHRINKING：缩容中 - SHRINK_CHECK_FAILED：缩容检测失败 - SHRINK_CHECKING：缩容检测中 - FLAVOR_RESIZING_FAILED：规格变更失败 - FLAVOR_RESIZING：规格变更中 - MANAGE_IP_BIND_FAILED：登录开通失败 - MANAGE_IP_BINDING：登录开通中 - ORDER_PENDING：订单待支付 - FINE_GRAINED_RESTORING：细粒度恢复中 - DR_RECOVERING：容灾恢复中

        :param task_status: The task_status of this ClusterInfo.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ClusterInfo.

        安全组ID

        :return: The security_group_id of this ClusterInfo.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ClusterInfo.

        安全组ID

        :param security_group_id: The security_group_id of this ClusterInfo.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def failed_reasons(self):
        """Gets the failed_reasons of this ClusterInfo.

        :return: The failed_reasons of this ClusterInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.FailedReason`
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        """Sets the failed_reasons of this ClusterInfo.

        :param failed_reasons: The failed_reasons of this ClusterInfo.
        :type failed_reasons: :class:`huaweicloudsdkdws.v2.FailedReason`
        """
        self._failed_reasons = failed_reasons

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
        if not isinstance(other, ClusterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
