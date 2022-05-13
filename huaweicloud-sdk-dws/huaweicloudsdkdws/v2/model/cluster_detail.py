# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDetail:

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
        'parameter_group': 'ParameterGroup',
        'node_type_id': 'str',
        'security_group_id': 'str',
        'private_ip': 'list[str]',
        'maintain_window': 'MaintainWindow',
        'resize_info': 'ResizeInfo',
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
        'parameter_group': 'parameter_group',
        'node_type_id': 'node_type_id',
        'security_group_id': 'security_group_id',
        'private_ip': 'private_ip',
        'maintain_window': 'maintain_window',
        'resize_info': 'resize_info',
        'failed_reasons': 'failed_reasons'
    }

    def __init__(self, id=None, name=None, status=None, version=None, updated=None, created=None, port=None, endpoints=None, nodes=None, tags=None, user_name=None, number_of_node=None, recent_event=None, availability_zone=None, enterprise_project_id=None, node_type=None, vpc_id=None, subnet_id=None, public_ip=None, public_endpoints=None, action_progress=None, sub_status=None, task_status=None, parameter_group=None, node_type_id=None, security_group_id=None, private_ip=None, maintain_window=None, resize_info=None, failed_reasons=None):
        """ClusterDetail

        The model defined in huaweicloud sdk

        :param id: 集群ID
        :type id: str
        :param name: 集群名称
        :type name: str
        :param status: 集群状态，有效值包括：  - CREATING：创建中 - AVAILABLE：可用 - UNAVAILABLE：不可用 - CREATION FAILED：创建失败 - FROZEN：已冻结
        :type status: str
        :param version: 数据仓库版本
        :type version: str
        :param updated: 集群上次修改时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type updated: str
        :param created: 集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ
        :type created: str
        :param port: 集群服务端口（8000~30000），默认值：8000
        :type port: int
        :param endpoints: 集群的内网连接信息。
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
        :param enterprise_project_id: 企业项目ID。值为0表示默认企业项目“default”。
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
        :param action_progress: Key值为正在进行的任务，有效值包括：  - GROWING：扩容中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - REPAIRING: 修复中 - CREATING: 创建中\\nvalue值为正在进行任务的进度。
        :type action_progress: dict(str, str)
        :param sub_status: “可用”集群状态的子状态，有效值包括：  - NORMAL：正常 - READONLY：只读 - REDISTRIBUTING：重分布中 - REDISTRIBUTION-FAILURE：重分布失败 - UNBALANCED：非均衡 - UNBALANCED | READONLY：非均衡，只读 - DEGRADED：节点故障 - DEGRADED | READONLY：节点故障，只读 - DEGRADED | UNBALANCED：节点故障，非均衡 - UNBALANCED | REDISTRIBUTING：非均衡，重分布中 - UNBALANCED | REDISTRIBUTION-FAILURE：非均衡，重分布失败 - READONLY | REDISTRIBUTION-FAILURE：只读，重分布失败 - UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：非均衡，只读，重分布失败 - DEGRADED | REDISTRIBUTION-FAILURE：节点故障，重分布失败 - DEGRADED | UNBALANCED | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY：节点故障，非均衡，只读
        :type sub_status: str
        :param task_status: 集群管理任务，有效值包括：  - UNFREEZING：解冻中 - FREEZING：冻结中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - DELETING_EXT_DATASOURCE：删除MRS连接 - REBOOT_FAILURE：重启失败 - RESIZE_FAILURE：扩容失败
        :type task_status: str
        :param parameter_group: 
        :type parameter_group: :class:`huaweicloudsdkdws.v2.ParameterGroup`
        :param node_type_id: 节点类型ID
        :type node_type_id: str
        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param private_ip: 内网IP地址列表
        :type private_ip: list[str]
        :param maintain_window: 
        :type maintain_window: :class:`huaweicloudsdkdws.v2.MaintainWindow`
        :param resize_info: 
        :type resize_info: :class:`huaweicloudsdkdws.v2.ResizeInfo`
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
        self._parameter_group = None
        self._node_type_id = None
        self._security_group_id = None
        self._private_ip = None
        self._maintain_window = None
        self._resize_info = None
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
        if parameter_group is not None:
            self.parameter_group = parameter_group
        self.node_type_id = node_type_id
        self.security_group_id = security_group_id
        self.private_ip = private_ip
        self.maintain_window = maintain_window
        if resize_info is not None:
            self.resize_info = resize_info
        if failed_reasons is not None:
            self.failed_reasons = failed_reasons

    @property
    def id(self):
        """Gets the id of this ClusterDetail.

        集群ID

        :return: The id of this ClusterDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterDetail.

        集群ID

        :param id: The id of this ClusterDetail.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ClusterDetail.

        集群名称

        :return: The name of this ClusterDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterDetail.

        集群名称

        :param name: The name of this ClusterDetail.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ClusterDetail.

        集群状态，有效值包括：  - CREATING：创建中 - AVAILABLE：可用 - UNAVAILABLE：不可用 - CREATION FAILED：创建失败 - FROZEN：已冻结

        :return: The status of this ClusterDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterDetail.

        集群状态，有效值包括：  - CREATING：创建中 - AVAILABLE：可用 - UNAVAILABLE：不可用 - CREATION FAILED：创建失败 - FROZEN：已冻结

        :param status: The status of this ClusterDetail.
        :type status: str
        """
        self._status = status

    @property
    def version(self):
        """Gets the version of this ClusterDetail.

        数据仓库版本

        :return: The version of this ClusterDetail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ClusterDetail.

        数据仓库版本

        :param version: The version of this ClusterDetail.
        :type version: str
        """
        self._version = version

    @property
    def updated(self):
        """Gets the updated of this ClusterDetail.

        集群上次修改时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The updated of this ClusterDetail.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ClusterDetail.

        集群上次修改时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param updated: The updated of this ClusterDetail.
        :type updated: str
        """
        self._updated = updated

    @property
    def created(self):
        """Gets the created of this ClusterDetail.

        集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :return: The created of this ClusterDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ClusterDetail.

        集群创建时间，格式为ISO8601：YYYY-MM-DDThh:mm:ssZ

        :param created: The created of this ClusterDetail.
        :type created: str
        """
        self._created = created

    @property
    def port(self):
        """Gets the port of this ClusterDetail.

        集群服务端口（8000~30000），默认值：8000

        :return: The port of this ClusterDetail.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ClusterDetail.

        集群服务端口（8000~30000），默认值：8000

        :param port: The port of this ClusterDetail.
        :type port: int
        """
        self._port = port

    @property
    def endpoints(self):
        """Gets the endpoints of this ClusterDetail.

        集群的内网连接信息。

        :return: The endpoints of this ClusterDetail.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Endpoints`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this ClusterDetail.

        集群的内网连接信息。

        :param endpoints: The endpoints of this ClusterDetail.
        :type endpoints: list[:class:`huaweicloudsdkdws.v2.Endpoints`]
        """
        self._endpoints = endpoints

    @property
    def nodes(self):
        """Gets the nodes of this ClusterDetail.

        集群实例

        :return: The nodes of this ClusterDetail.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Nodes`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ClusterDetail.

        集群实例

        :param nodes: The nodes of this ClusterDetail.
        :type nodes: list[:class:`huaweicloudsdkdws.v2.Nodes`]
        """
        self._nodes = nodes

    @property
    def tags(self):
        """Gets the tags of this ClusterDetail.

        集群标签

        :return: The tags of this ClusterDetail.
        :rtype: list[:class:`huaweicloudsdkdws.v2.Tags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ClusterDetail.

        集群标签

        :param tags: The tags of this ClusterDetail.
        :type tags: list[:class:`huaweicloudsdkdws.v2.Tags`]
        """
        self._tags = tags

    @property
    def user_name(self):
        """Gets the user_name of this ClusterDetail.

        管理员用户名

        :return: The user_name of this ClusterDetail.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ClusterDetail.

        管理员用户名

        :param user_name: The user_name of this ClusterDetail.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def number_of_node(self):
        """Gets the number_of_node of this ClusterDetail.

        节点数量

        :return: The number_of_node of this ClusterDetail.
        :rtype: int
        """
        return self._number_of_node

    @number_of_node.setter
    def number_of_node(self, number_of_node):
        """Sets the number_of_node of this ClusterDetail.

        节点数量

        :param number_of_node: The number_of_node of this ClusterDetail.
        :type number_of_node: int
        """
        self._number_of_node = number_of_node

    @property
    def recent_event(self):
        """Gets the recent_event of this ClusterDetail.

        事件数

        :return: The recent_event of this ClusterDetail.
        :rtype: int
        """
        return self._recent_event

    @recent_event.setter
    def recent_event(self, recent_event):
        """Sets the recent_event of this ClusterDetail.

        事件数

        :param recent_event: The recent_event of this ClusterDetail.
        :type recent_event: int
        """
        self._recent_event = recent_event

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ClusterDetail.

        可用区

        :return: The availability_zone of this ClusterDetail.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ClusterDetail.

        可用区

        :param availability_zone: The availability_zone of this ClusterDetail.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ClusterDetail.

        企业项目ID。值为0表示默认企业项目“default”。

        :return: The enterprise_project_id of this ClusterDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ClusterDetail.

        企业项目ID。值为0表示默认企业项目“default”。

        :param enterprise_project_id: The enterprise_project_id of this ClusterDetail.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def node_type(self):
        """Gets the node_type of this ClusterDetail.

        节点类型

        :return: The node_type of this ClusterDetail.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ClusterDetail.

        节点类型

        :param node_type: The node_type of this ClusterDetail.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ClusterDetail.

        虚拟私有云ID

        :return: The vpc_id of this ClusterDetail.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ClusterDetail.

        虚拟私有云ID

        :param vpc_id: The vpc_id of this ClusterDetail.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ClusterDetail.

        子网ID

        :return: The subnet_id of this ClusterDetail.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ClusterDetail.

        子网ID

        :param subnet_id: The subnet_id of this ClusterDetail.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def public_ip(self):
        """Gets the public_ip of this ClusterDetail.


        :return: The public_ip of this ClusterDetail.
        :rtype: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this ClusterDetail.


        :param public_ip: The public_ip of this ClusterDetail.
        :type public_ip: :class:`huaweicloudsdkdws.v2.PublicIp`
        """
        self._public_ip = public_ip

    @property
    def public_endpoints(self):
        """Gets the public_endpoints of this ClusterDetail.

        集群的公网连接信息，如果未指定，则默认不使用公网连接信息。

        :return: The public_endpoints of this ClusterDetail.
        :rtype: list[:class:`huaweicloudsdkdws.v2.PublicEndpoints`]
        """
        return self._public_endpoints

    @public_endpoints.setter
    def public_endpoints(self, public_endpoints):
        """Sets the public_endpoints of this ClusterDetail.

        集群的公网连接信息，如果未指定，则默认不使用公网连接信息。

        :param public_endpoints: The public_endpoints of this ClusterDetail.
        :type public_endpoints: list[:class:`huaweicloudsdkdws.v2.PublicEndpoints`]
        """
        self._public_endpoints = public_endpoints

    @property
    def action_progress(self):
        """Gets the action_progress of this ClusterDetail.

        Key值为正在进行的任务，有效值包括：  - GROWING：扩容中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - REPAIRING: 修复中 - CREATING: 创建中\\nvalue值为正在进行任务的进度。

        :return: The action_progress of this ClusterDetail.
        :rtype: dict(str, str)
        """
        return self._action_progress

    @action_progress.setter
    def action_progress(self, action_progress):
        """Sets the action_progress of this ClusterDetail.

        Key值为正在进行的任务，有效值包括：  - GROWING：扩容中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - REPAIRING: 修复中 - CREATING: 创建中\\nvalue值为正在进行任务的进度。

        :param action_progress: The action_progress of this ClusterDetail.
        :type action_progress: dict(str, str)
        """
        self._action_progress = action_progress

    @property
    def sub_status(self):
        """Gets the sub_status of this ClusterDetail.

        “可用”集群状态的子状态，有效值包括：  - NORMAL：正常 - READONLY：只读 - REDISTRIBUTING：重分布中 - REDISTRIBUTION-FAILURE：重分布失败 - UNBALANCED：非均衡 - UNBALANCED | READONLY：非均衡，只读 - DEGRADED：节点故障 - DEGRADED | READONLY：节点故障，只读 - DEGRADED | UNBALANCED：节点故障，非均衡 - UNBALANCED | REDISTRIBUTING：非均衡，重分布中 - UNBALANCED | REDISTRIBUTION-FAILURE：非均衡，重分布失败 - READONLY | REDISTRIBUTION-FAILURE：只读，重分布失败 - UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：非均衡，只读，重分布失败 - DEGRADED | REDISTRIBUTION-FAILURE：节点故障，重分布失败 - DEGRADED | UNBALANCED | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY：节点故障，非均衡，只读

        :return: The sub_status of this ClusterDetail.
        :rtype: str
        """
        return self._sub_status

    @sub_status.setter
    def sub_status(self, sub_status):
        """Sets the sub_status of this ClusterDetail.

        “可用”集群状态的子状态，有效值包括：  - NORMAL：正常 - READONLY：只读 - REDISTRIBUTING：重分布中 - REDISTRIBUTION-FAILURE：重分布失败 - UNBALANCED：非均衡 - UNBALANCED | READONLY：非均衡，只读 - DEGRADED：节点故障 - DEGRADED | READONLY：节点故障，只读 - DEGRADED | UNBALANCED：节点故障，非均衡 - UNBALANCED | REDISTRIBUTING：非均衡，重分布中 - UNBALANCED | REDISTRIBUTION-FAILURE：非均衡，重分布失败 - READONLY | REDISTRIBUTION-FAILURE：只读，重分布失败 - UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：非均衡，只读，重分布失败 - DEGRADED | REDISTRIBUTION-FAILURE：节点故障，重分布失败 - DEGRADED | UNBALANCED | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY | REDISTRIBUTION-FAILURE：节点故障，非均衡，只读，重分布失败 - DEGRADED | UNBALANCED | READONLY：节点故障，非均衡，只读

        :param sub_status: The sub_status of this ClusterDetail.
        :type sub_status: str
        """
        self._sub_status = sub_status

    @property
    def task_status(self):
        """Gets the task_status of this ClusterDetail.

        集群管理任务，有效值包括：  - UNFREEZING：解冻中 - FREEZING：冻结中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - DELETING_EXT_DATASOURCE：删除MRS连接 - REBOOT_FAILURE：重启失败 - RESIZE_FAILURE：扩容失败

        :return: The task_status of this ClusterDetail.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ClusterDetail.

        集群管理任务，有效值包括：  - UNFREEZING：解冻中 - FREEZING：冻结中 - RESTORING：恢复中 - SNAPSHOTTING：快照中 - GROWING：扩容中 - REBOOTING：重启中 - SETTING_CONFIGURATION：安全设置配置中 - CONFIGURING_EXT_DATASOURCE：MRS连接配置中 - DELETING_EXT_DATASOURCE：删除MRS连接 - REBOOT_FAILURE：重启失败 - RESIZE_FAILURE：扩容失败

        :param task_status: The task_status of this ClusterDetail.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def parameter_group(self):
        """Gets the parameter_group of this ClusterDetail.


        :return: The parameter_group of this ClusterDetail.
        :rtype: :class:`huaweicloudsdkdws.v2.ParameterGroup`
        """
        return self._parameter_group

    @parameter_group.setter
    def parameter_group(self, parameter_group):
        """Sets the parameter_group of this ClusterDetail.


        :param parameter_group: The parameter_group of this ClusterDetail.
        :type parameter_group: :class:`huaweicloudsdkdws.v2.ParameterGroup`
        """
        self._parameter_group = parameter_group

    @property
    def node_type_id(self):
        """Gets the node_type_id of this ClusterDetail.

        节点类型ID

        :return: The node_type_id of this ClusterDetail.
        :rtype: str
        """
        return self._node_type_id

    @node_type_id.setter
    def node_type_id(self, node_type_id):
        """Sets the node_type_id of this ClusterDetail.

        节点类型ID

        :param node_type_id: The node_type_id of this ClusterDetail.
        :type node_type_id: str
        """
        self._node_type_id = node_type_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ClusterDetail.

        安全组ID

        :return: The security_group_id of this ClusterDetail.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ClusterDetail.

        安全组ID

        :param security_group_id: The security_group_id of this ClusterDetail.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def private_ip(self):
        """Gets the private_ip of this ClusterDetail.

        内网IP地址列表

        :return: The private_ip of this ClusterDetail.
        :rtype: list[str]
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """Sets the private_ip of this ClusterDetail.

        内网IP地址列表

        :param private_ip: The private_ip of this ClusterDetail.
        :type private_ip: list[str]
        """
        self._private_ip = private_ip

    @property
    def maintain_window(self):
        """Gets the maintain_window of this ClusterDetail.


        :return: The maintain_window of this ClusterDetail.
        :rtype: :class:`huaweicloudsdkdws.v2.MaintainWindow`
        """
        return self._maintain_window

    @maintain_window.setter
    def maintain_window(self, maintain_window):
        """Sets the maintain_window of this ClusterDetail.


        :param maintain_window: The maintain_window of this ClusterDetail.
        :type maintain_window: :class:`huaweicloudsdkdws.v2.MaintainWindow`
        """
        self._maintain_window = maintain_window

    @property
    def resize_info(self):
        """Gets the resize_info of this ClusterDetail.


        :return: The resize_info of this ClusterDetail.
        :rtype: :class:`huaweicloudsdkdws.v2.ResizeInfo`
        """
        return self._resize_info

    @resize_info.setter
    def resize_info(self, resize_info):
        """Sets the resize_info of this ClusterDetail.


        :param resize_info: The resize_info of this ClusterDetail.
        :type resize_info: :class:`huaweicloudsdkdws.v2.ResizeInfo`
        """
        self._resize_info = resize_info

    @property
    def failed_reasons(self):
        """Gets the failed_reasons of this ClusterDetail.


        :return: The failed_reasons of this ClusterDetail.
        :rtype: :class:`huaweicloudsdkdws.v2.FailedReason`
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        """Sets the failed_reasons of this ClusterDetail.


        :param failed_reasons: The failed_reasons of this ClusterDetail.
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
        if not isinstance(other, ClusterDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
