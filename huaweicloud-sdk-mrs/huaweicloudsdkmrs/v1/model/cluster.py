# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Cluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'cluster_name': 'str',
        'total_node_num': 'str',
        'cluster_state': 'str',
        'stage_desc': 'str',
        'create_at': 'str',
        'update_at': 'str',
        'charging_start_time': 'str',
        'billing_type': 'str',
        'data_center': 'str',
        'vpc': 'str',
        'vpc_id': 'str',
        'duration': 'str',
        'fee': 'str',
        'hadoop_version': 'str',
        'component_list': 'list[ComponentAmb]',
        'external_ip': 'str',
        'external_alternate_ip': 'str',
        'internal_ip': 'str',
        'deployment_id': 'str',
        'remark': 'str',
        'order_id': 'str',
        'az_id': 'str',
        'az_name': 'str',
        'az_code': 'str',
        'availability_zone_id': 'str',
        'instance_id': 'str',
        'vnc': 'str',
        'tenant_id': 'str',
        'volume_size': 'int',
        'volume_type': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'security_groups_id': 'str',
        'slave_security_groups_id': 'str',
        'bootstrap_scripts': 'list[BootstrapScript]',
        'safe_mode': 'int',
        'cluster_version': 'str',
        'node_public_cert_name': 'str',
        'master_node_ip': 'str',
        'private_ip_first': 'str',
        'error_info': 'str',
        'tags': 'str',
        'master_node_num': 'str',
        'core_node_num': 'str',
        'master_node_size': 'str',
        'core_node_size': 'str',
        'master_node_product_id': 'str',
        'master_node_spec_id': 'str',
        'core_node_product_id': 'str',
        'core_node_spec_id': 'str',
        'master_data_volume_type': 'str',
        'master_data_volume_size': 'int',
        'master_data_volume_count': 'int',
        'core_data_volume_type': 'str',
        'core_data_volume_size': 'int',
        'core_data_volume_count': 'int',
        'enterprise_project_id': 'str',
        'is_mrs_manager_finish': 'bool',
        'cluster_type': 'int',
        'log_collection': 'int',
        'period_type': 'int',
        'scale': 'str',
        'node_groups': 'list[NodeGroupV10]',
        'task_node_groups': 'list[NodeGroupV10]',
        'eip_id': 'str',
        'eip_address': 'str',
        'eipv6_address': 'str'
    }

    attribute_map = {
        'cluster_id': 'clusterId',
        'cluster_name': 'clusterName',
        'total_node_num': 'totalNodeNum',
        'cluster_state': 'clusterState',
        'stage_desc': 'stageDesc',
        'create_at': 'createAt',
        'update_at': 'updateAt',
        'charging_start_time': 'chargingStartTime',
        'billing_type': 'billingType',
        'data_center': 'dataCenter',
        'vpc': 'vpc',
        'vpc_id': 'vpcId',
        'duration': 'duration',
        'fee': 'fee',
        'hadoop_version': 'hadoopVersion',
        'component_list': 'componentList',
        'external_ip': 'externalIp',
        'external_alternate_ip': 'externalAlternateIp',
        'internal_ip': 'internalIp',
        'deployment_id': 'deploymentId',
        'remark': 'remark',
        'order_id': 'orderId',
        'az_id': 'azId',
        'az_name': 'azName',
        'az_code': 'azCode',
        'availability_zone_id': 'availabilityZoneId',
        'instance_id': 'instanceId',
        'vnc': 'vnc',
        'tenant_id': 'tenantId',
        'volume_size': 'volumeSize',
        'volume_type': 'volumeType',
        'subnet_id': 'subnetId',
        'subnet_name': 'subnetName',
        'security_groups_id': 'securityGroupsId',
        'slave_security_groups_id': 'slaveSecurityGroupsId',
        'bootstrap_scripts': 'bootstrapScripts',
        'safe_mode': 'safeMode',
        'cluster_version': 'clusterVersion',
        'node_public_cert_name': 'nodePublicCertName',
        'master_node_ip': 'masterNodeIp',
        'private_ip_first': 'privateIpFirst',
        'error_info': 'errorInfo',
        'tags': 'tags',
        'master_node_num': 'masterNodeNum',
        'core_node_num': 'coreNodeNum',
        'master_node_size': 'masterNodeSize',
        'core_node_size': 'coreNodeSize',
        'master_node_product_id': 'masterNodeProductId',
        'master_node_spec_id': 'masterNodeSpecId',
        'core_node_product_id': 'coreNodeProductId',
        'core_node_spec_id': 'coreNodeSpecId',
        'master_data_volume_type': 'masterDataVolumeType',
        'master_data_volume_size': 'masterDataVolumeSize',
        'master_data_volume_count': 'masterDataVolumeCount',
        'core_data_volume_type': 'coreDataVolumeType',
        'core_data_volume_size': 'coreDataVolumeSize',
        'core_data_volume_count': 'coreDataVolumeCount',
        'enterprise_project_id': 'enterpriseProjectId',
        'is_mrs_manager_finish': 'isMrsManagerFinish',
        'cluster_type': 'clusterType',
        'log_collection': 'logCollection',
        'period_type': 'periodType',
        'scale': 'scale',
        'node_groups': 'nodeGroups',
        'task_node_groups': 'taskNodeGroups',
        'eip_id': 'eipId',
        'eip_address': 'eipAddress',
        'eipv6_address': 'eipv6Address'
    }

    def __init__(self, cluster_id=None, cluster_name=None, total_node_num=None, cluster_state=None, stage_desc=None, create_at=None, update_at=None, charging_start_time=None, billing_type=None, data_center=None, vpc=None, vpc_id=None, duration=None, fee=None, hadoop_version=None, component_list=None, external_ip=None, external_alternate_ip=None, internal_ip=None, deployment_id=None, remark=None, order_id=None, az_id=None, az_name=None, az_code=None, availability_zone_id=None, instance_id=None, vnc=None, tenant_id=None, volume_size=None, volume_type=None, subnet_id=None, subnet_name=None, security_groups_id=None, slave_security_groups_id=None, bootstrap_scripts=None, safe_mode=None, cluster_version=None, node_public_cert_name=None, master_node_ip=None, private_ip_first=None, error_info=None, tags=None, master_node_num=None, core_node_num=None, master_node_size=None, core_node_size=None, master_node_product_id=None, master_node_spec_id=None, core_node_product_id=None, core_node_spec_id=None, master_data_volume_type=None, master_data_volume_size=None, master_data_volume_count=None, core_data_volume_type=None, core_data_volume_size=None, core_data_volume_count=None, enterprise_project_id=None, is_mrs_manager_finish=None, cluster_type=None, log_collection=None, period_type=None, scale=None, node_groups=None, task_node_groups=None, eip_id=None, eip_address=None, eipv6_address=None):
        """Cluster

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID。
        :type cluster_id: str
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param total_node_num: 集群部署的节点总数。
        :type total_node_num: str
        :param cluster_state: 集群状态，包括： - starting：启动中的集群。 - running：运行中的集群。 - terminated：已删除的集群。 - failed：失败的集群。 - abnormal：异常的集群。 - terminating：删除中的集群。 - frozen：已冻结的集群。 - scaling-out：扩容中的集群。 - scaling-in：缩容中的集群。
        :type cluster_state: str
        :param stage_desc: 集群进度描述。  安装集群进度包括： - Verifying cluster parameters：校验集群参数中 - Applying for cluster resources：申请集群资源中 - Creating VM：创建虚拟机中 - Initializing VM：初始化虚拟机中 - Installing MRS Manager：安装MRS Manager中 - Deploying cluster：部署集群中 - Cluster installation failed：集群安装失败  扩容集群进度包括： - Preparing for cluster expansion：准备扩容中 - Creating VM：创建虚拟机中 - Initializing VM：初始化虚拟机中 - Adding node to the cluster：节点加入集群中 - Cluster expansion failed：集群扩容失败  缩容集群进度包括： - Preparing for cluster shrink：正在准备缩容 - Decommissioning instance：实例退服中 - Deleting VM：删除虚拟机中 - Deleting node from the cluster：从集群删除节点中 - Cluster shrink failed：集群缩容失败 集群安装、扩容、缩容失败，stageDesc会显示失败的原因。
        :type stage_desc: str
        :param create_at: 集群创建时间，十位时间戳。
        :type create_at: str
        :param update_at: 集群更新时间，十位时间戳。
        :type update_at: str
        :param charging_start_time: 开始计费时间。
        :type charging_start_time: str
        :param billing_type: 集群计费模式。
        :type billing_type: str
        :param data_center: 集群工作区域。
        :type data_center: str
        :param vpc: VPC名称。
        :type vpc: str
        :param vpc_id: VPC ID。
        :type vpc_id: str
        :param duration: 集群购买时长。
        :type duration: str
        :param fee: 创建集群所需费用，系统自动计算。
        :type fee: str
        :param hadoop_version: Hadoop组件版本信息。
        :type hadoop_version: str
        :param component_list: 组件列表信息。
        :type component_list: list[:class:`huaweicloudsdkmrs.v1.ComponentAmb`]
        :param external_ip: 公网IP地址。
        :type external_ip: str
        :param external_alternate_ip: 公网备用IP地址。
        :type external_alternate_ip: str
        :param internal_ip: 内网IP地址。
        :type internal_ip: str
        :param deployment_id: 集群部署ID。
        :type deployment_id: str
        :param remark: 集群备注信息。
        :type remark: str
        :param order_id: 创建集群的订单号。
        :type order_id: str
        :param az_id: 可用区域ID。
        :type az_id: str
        :param az_name: 可用区域名称。
        :type az_name: str
        :param az_code: 可用区域英文名称
        :type az_code: str
        :param availability_zone_id: 可用区域
        :type availability_zone_id: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param vnc: 远程登录弹性云服务器的URI地址。
        :type vnc: str
        :param tenant_id: 项目编号。
        :type tenant_id: str
        :param volume_size: 磁盘存储空间。
        :type volume_size: int
        :param volume_type: 磁盘类型。
        :type volume_type: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param subnet_name: 子网名称。
        :type subnet_name: str
        :param security_groups_id: 安全组ID。
        :type security_groups_id: str
        :param slave_security_groups_id: 非Master节点的安全组id，当前一个MRS集群只会使用一个安全组，所以该字段已经废弃，从兼容性考虑，该字段会返回和securityGroupsId同样的值。
        :type slave_security_groups_id: str
        :param bootstrap_scripts: 配置引导操作脚本信息。
        :type bootstrap_scripts: list[:class:`huaweicloudsdkmrs.v1.BootstrapScript`]
        :param safe_mode: MRS集群运行模式。 - 0：普通集群 - 1：安全集群
        :type safe_mode: int
        :param cluster_version: 集群版本。
        :type cluster_version: str
        :param node_public_cert_name: 密钥文件名称。
        :type node_public_cert_name: str
        :param master_node_ip: Master节点IP。
        :type master_node_ip: str
        :param private_ip_first: 首选私有IP。
        :type private_ip_first: str
        :param error_info: 错误信息。
        :type error_info: str
        :param tags: 标签信息
        :type tags: str
        :param master_node_num: 集群部署的Master节点数量。
        :type master_node_num: str
        :param core_node_num: 集群部署的Core节点数量。
        :type core_node_num: str
        :param master_node_size: Master节点的实例规格。
        :type master_node_size: str
        :param core_node_size: Core节点的实例规格。
        :type core_node_size: str
        :param master_node_product_id: Master节点产品ID。
        :type master_node_product_id: str
        :param master_node_spec_id: Master节点规格ID。
        :type master_node_spec_id: str
        :param core_node_product_id: Core节点产品ID。
        :type core_node_product_id: str
        :param core_node_spec_id: Core节点规格ID。
        :type core_node_spec_id: str
        :param master_data_volume_type: Master节点数据磁盘存储类别，目前支持SATA、SAS和SSD。
        :type master_data_volume_type: str
        :param master_data_volume_size: Master节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。 取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。
        :type master_data_volume_size: int
        :param master_data_volume_count: Master节点数据磁盘个数。 取值只能是1
        :type master_data_volume_count: int
        :param core_data_volume_type: Core节点数据磁盘存储类别，目前支持SATA、SAS和SSD。
        :type core_data_volume_type: str
        :param core_data_volume_size: Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。 取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。
        :type core_data_volume_size: int
        :param core_data_volume_count: Core节点数据磁盘个数。 取值范围：1～10
        :type core_data_volume_count: int
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param is_mrs_manager_finish: 表示集群创建过程中，MRS Manager是否安装完成。 - true：安装完成 - false：安装未完成
        :type is_mrs_manager_finish: bool
        :param cluster_type: 集群类型。
        :type cluster_type: int
        :param log_collection: 集群安装失败时，是否搜集日志。 - 0：不收集 - 1：收集
        :type log_collection: int
        :param period_type: 区分包周期，集群是包年还是包月。 - 0：包月 - 1：包年
        :type period_type: int
        :param scale: 集群节点的变更状态（扩容/缩容/变更规格）。当该参数取值为空时，表示集群节点没有进行变更操作。 取值范围： - scaling-out：扩容中 - scaling-in：缩容中 - scaling-error：处于running状态，且上一次扩容/缩容/升级规格失败的集群 - scaling-up：Master节点规格升级中 - scaling_up_first：备Master节点规格升级中 - scaled_up_first：备Master节点规格升级成功 - scaled-up-success：Master节点规格升级成功
        :type scale: str
        :param node_groups: Master节点、Core节点和Task节点列表信息。
        :type node_groups: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV10`]
        :param task_node_groups: Task节点列表信息。
        :type task_node_groups: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV10`]
        :param eip_id: 集群弹性公网ip的唯一标识
        :type eip_id: str
        :param eip_address: 集群弹性公网ip的IPV4地址
        :type eip_address: str
        :param eipv6_address: 集群弹性公网ip的IPV6地址，IPv4时无此字段。
        :type eipv6_address: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._total_node_num = None
        self._cluster_state = None
        self._stage_desc = None
        self._create_at = None
        self._update_at = None
        self._charging_start_time = None
        self._billing_type = None
        self._data_center = None
        self._vpc = None
        self._vpc_id = None
        self._duration = None
        self._fee = None
        self._hadoop_version = None
        self._component_list = None
        self._external_ip = None
        self._external_alternate_ip = None
        self._internal_ip = None
        self._deployment_id = None
        self._remark = None
        self._order_id = None
        self._az_id = None
        self._az_name = None
        self._az_code = None
        self._availability_zone_id = None
        self._instance_id = None
        self._vnc = None
        self._tenant_id = None
        self._volume_size = None
        self._volume_type = None
        self._subnet_id = None
        self._subnet_name = None
        self._security_groups_id = None
        self._slave_security_groups_id = None
        self._bootstrap_scripts = None
        self._safe_mode = None
        self._cluster_version = None
        self._node_public_cert_name = None
        self._master_node_ip = None
        self._private_ip_first = None
        self._error_info = None
        self._tags = None
        self._master_node_num = None
        self._core_node_num = None
        self._master_node_size = None
        self._core_node_size = None
        self._master_node_product_id = None
        self._master_node_spec_id = None
        self._core_node_product_id = None
        self._core_node_spec_id = None
        self._master_data_volume_type = None
        self._master_data_volume_size = None
        self._master_data_volume_count = None
        self._core_data_volume_type = None
        self._core_data_volume_size = None
        self._core_data_volume_count = None
        self._enterprise_project_id = None
        self._is_mrs_manager_finish = None
        self._cluster_type = None
        self._log_collection = None
        self._period_type = None
        self._scale = None
        self._node_groups = None
        self._task_node_groups = None
        self._eip_id = None
        self._eip_address = None
        self._eipv6_address = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if total_node_num is not None:
            self.total_node_num = total_node_num
        if cluster_state is not None:
            self.cluster_state = cluster_state
        if stage_desc is not None:
            self.stage_desc = stage_desc
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if charging_start_time is not None:
            self.charging_start_time = charging_start_time
        if billing_type is not None:
            self.billing_type = billing_type
        if data_center is not None:
            self.data_center = data_center
        if vpc is not None:
            self.vpc = vpc
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if duration is not None:
            self.duration = duration
        if fee is not None:
            self.fee = fee
        if hadoop_version is not None:
            self.hadoop_version = hadoop_version
        if component_list is not None:
            self.component_list = component_list
        if external_ip is not None:
            self.external_ip = external_ip
        if external_alternate_ip is not None:
            self.external_alternate_ip = external_alternate_ip
        if internal_ip is not None:
            self.internal_ip = internal_ip
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if remark is not None:
            self.remark = remark
        if order_id is not None:
            self.order_id = order_id
        if az_id is not None:
            self.az_id = az_id
        if az_name is not None:
            self.az_name = az_name
        if az_code is not None:
            self.az_code = az_code
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if instance_id is not None:
            self.instance_id = instance_id
        if vnc is not None:
            self.vnc = vnc
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if volume_size is not None:
            self.volume_size = volume_size
        if volume_type is not None:
            self.volume_type = volume_type
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if security_groups_id is not None:
            self.security_groups_id = security_groups_id
        if slave_security_groups_id is not None:
            self.slave_security_groups_id = slave_security_groups_id
        if bootstrap_scripts is not None:
            self.bootstrap_scripts = bootstrap_scripts
        if safe_mode is not None:
            self.safe_mode = safe_mode
        if cluster_version is not None:
            self.cluster_version = cluster_version
        if node_public_cert_name is not None:
            self.node_public_cert_name = node_public_cert_name
        if master_node_ip is not None:
            self.master_node_ip = master_node_ip
        if private_ip_first is not None:
            self.private_ip_first = private_ip_first
        if error_info is not None:
            self.error_info = error_info
        if tags is not None:
            self.tags = tags
        if master_node_num is not None:
            self.master_node_num = master_node_num
        if core_node_num is not None:
            self.core_node_num = core_node_num
        if master_node_size is not None:
            self.master_node_size = master_node_size
        if core_node_size is not None:
            self.core_node_size = core_node_size
        if master_node_product_id is not None:
            self.master_node_product_id = master_node_product_id
        if master_node_spec_id is not None:
            self.master_node_spec_id = master_node_spec_id
        if core_node_product_id is not None:
            self.core_node_product_id = core_node_product_id
        if core_node_spec_id is not None:
            self.core_node_spec_id = core_node_spec_id
        if master_data_volume_type is not None:
            self.master_data_volume_type = master_data_volume_type
        if master_data_volume_size is not None:
            self.master_data_volume_size = master_data_volume_size
        if master_data_volume_count is not None:
            self.master_data_volume_count = master_data_volume_count
        if core_data_volume_type is not None:
            self.core_data_volume_type = core_data_volume_type
        if core_data_volume_size is not None:
            self.core_data_volume_size = core_data_volume_size
        if core_data_volume_count is not None:
            self.core_data_volume_count = core_data_volume_count
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if is_mrs_manager_finish is not None:
            self.is_mrs_manager_finish = is_mrs_manager_finish
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if log_collection is not None:
            self.log_collection = log_collection
        if period_type is not None:
            self.period_type = period_type
        if scale is not None:
            self.scale = scale
        if node_groups is not None:
            self.node_groups = node_groups
        if task_node_groups is not None:
            self.task_node_groups = task_node_groups
        if eip_id is not None:
            self.eip_id = eip_id
        if eip_address is not None:
            self.eip_address = eip_address
        if eipv6_address is not None:
            self.eipv6_address = eipv6_address

    @property
    def cluster_id(self):
        """Gets the cluster_id of this Cluster.

        集群ID。

        :return: The cluster_id of this Cluster.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this Cluster.

        集群ID。

        :param cluster_id: The cluster_id of this Cluster.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        """Gets the cluster_name of this Cluster.

        集群名称。

        :return: The cluster_name of this Cluster.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this Cluster.

        集群名称。

        :param cluster_name: The cluster_name of this Cluster.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def total_node_num(self):
        """Gets the total_node_num of this Cluster.

        集群部署的节点总数。

        :return: The total_node_num of this Cluster.
        :rtype: str
        """
        return self._total_node_num

    @total_node_num.setter
    def total_node_num(self, total_node_num):
        """Sets the total_node_num of this Cluster.

        集群部署的节点总数。

        :param total_node_num: The total_node_num of this Cluster.
        :type total_node_num: str
        """
        self._total_node_num = total_node_num

    @property
    def cluster_state(self):
        """Gets the cluster_state of this Cluster.

        集群状态，包括： - starting：启动中的集群。 - running：运行中的集群。 - terminated：已删除的集群。 - failed：失败的集群。 - abnormal：异常的集群。 - terminating：删除中的集群。 - frozen：已冻结的集群。 - scaling-out：扩容中的集群。 - scaling-in：缩容中的集群。

        :return: The cluster_state of this Cluster.
        :rtype: str
        """
        return self._cluster_state

    @cluster_state.setter
    def cluster_state(self, cluster_state):
        """Sets the cluster_state of this Cluster.

        集群状态，包括： - starting：启动中的集群。 - running：运行中的集群。 - terminated：已删除的集群。 - failed：失败的集群。 - abnormal：异常的集群。 - terminating：删除中的集群。 - frozen：已冻结的集群。 - scaling-out：扩容中的集群。 - scaling-in：缩容中的集群。

        :param cluster_state: The cluster_state of this Cluster.
        :type cluster_state: str
        """
        self._cluster_state = cluster_state

    @property
    def stage_desc(self):
        """Gets the stage_desc of this Cluster.

        集群进度描述。  安装集群进度包括： - Verifying cluster parameters：校验集群参数中 - Applying for cluster resources：申请集群资源中 - Creating VM：创建虚拟机中 - Initializing VM：初始化虚拟机中 - Installing MRS Manager：安装MRS Manager中 - Deploying cluster：部署集群中 - Cluster installation failed：集群安装失败  扩容集群进度包括： - Preparing for cluster expansion：准备扩容中 - Creating VM：创建虚拟机中 - Initializing VM：初始化虚拟机中 - Adding node to the cluster：节点加入集群中 - Cluster expansion failed：集群扩容失败  缩容集群进度包括： - Preparing for cluster shrink：正在准备缩容 - Decommissioning instance：实例退服中 - Deleting VM：删除虚拟机中 - Deleting node from the cluster：从集群删除节点中 - Cluster shrink failed：集群缩容失败 集群安装、扩容、缩容失败，stageDesc会显示失败的原因。

        :return: The stage_desc of this Cluster.
        :rtype: str
        """
        return self._stage_desc

    @stage_desc.setter
    def stage_desc(self, stage_desc):
        """Sets the stage_desc of this Cluster.

        集群进度描述。  安装集群进度包括： - Verifying cluster parameters：校验集群参数中 - Applying for cluster resources：申请集群资源中 - Creating VM：创建虚拟机中 - Initializing VM：初始化虚拟机中 - Installing MRS Manager：安装MRS Manager中 - Deploying cluster：部署集群中 - Cluster installation failed：集群安装失败  扩容集群进度包括： - Preparing for cluster expansion：准备扩容中 - Creating VM：创建虚拟机中 - Initializing VM：初始化虚拟机中 - Adding node to the cluster：节点加入集群中 - Cluster expansion failed：集群扩容失败  缩容集群进度包括： - Preparing for cluster shrink：正在准备缩容 - Decommissioning instance：实例退服中 - Deleting VM：删除虚拟机中 - Deleting node from the cluster：从集群删除节点中 - Cluster shrink failed：集群缩容失败 集群安装、扩容、缩容失败，stageDesc会显示失败的原因。

        :param stage_desc: The stage_desc of this Cluster.
        :type stage_desc: str
        """
        self._stage_desc = stage_desc

    @property
    def create_at(self):
        """Gets the create_at of this Cluster.

        集群创建时间，十位时间戳。

        :return: The create_at of this Cluster.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this Cluster.

        集群创建时间，十位时间戳。

        :param create_at: The create_at of this Cluster.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        """Gets the update_at of this Cluster.

        集群更新时间，十位时间戳。

        :return: The update_at of this Cluster.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this Cluster.

        集群更新时间，十位时间戳。

        :param update_at: The update_at of this Cluster.
        :type update_at: str
        """
        self._update_at = update_at

    @property
    def charging_start_time(self):
        """Gets the charging_start_time of this Cluster.

        开始计费时间。

        :return: The charging_start_time of this Cluster.
        :rtype: str
        """
        return self._charging_start_time

    @charging_start_time.setter
    def charging_start_time(self, charging_start_time):
        """Sets the charging_start_time of this Cluster.

        开始计费时间。

        :param charging_start_time: The charging_start_time of this Cluster.
        :type charging_start_time: str
        """
        self._charging_start_time = charging_start_time

    @property
    def billing_type(self):
        """Gets the billing_type of this Cluster.

        集群计费模式。

        :return: The billing_type of this Cluster.
        :rtype: str
        """
        return self._billing_type

    @billing_type.setter
    def billing_type(self, billing_type):
        """Sets the billing_type of this Cluster.

        集群计费模式。

        :param billing_type: The billing_type of this Cluster.
        :type billing_type: str
        """
        self._billing_type = billing_type

    @property
    def data_center(self):
        """Gets the data_center of this Cluster.

        集群工作区域。

        :return: The data_center of this Cluster.
        :rtype: str
        """
        return self._data_center

    @data_center.setter
    def data_center(self, data_center):
        """Sets the data_center of this Cluster.

        集群工作区域。

        :param data_center: The data_center of this Cluster.
        :type data_center: str
        """
        self._data_center = data_center

    @property
    def vpc(self):
        """Gets the vpc of this Cluster.

        VPC名称。

        :return: The vpc of this Cluster.
        :rtype: str
        """
        return self._vpc

    @vpc.setter
    def vpc(self, vpc):
        """Sets the vpc of this Cluster.

        VPC名称。

        :param vpc: The vpc of this Cluster.
        :type vpc: str
        """
        self._vpc = vpc

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Cluster.

        VPC ID。

        :return: The vpc_id of this Cluster.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Cluster.

        VPC ID。

        :param vpc_id: The vpc_id of this Cluster.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def duration(self):
        """Gets the duration of this Cluster.

        集群购买时长。

        :return: The duration of this Cluster.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Cluster.

        集群购买时长。

        :param duration: The duration of this Cluster.
        :type duration: str
        """
        self._duration = duration

    @property
    def fee(self):
        """Gets the fee of this Cluster.

        创建集群所需费用，系统自动计算。

        :return: The fee of this Cluster.
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this Cluster.

        创建集群所需费用，系统自动计算。

        :param fee: The fee of this Cluster.
        :type fee: str
        """
        self._fee = fee

    @property
    def hadoop_version(self):
        """Gets the hadoop_version of this Cluster.

        Hadoop组件版本信息。

        :return: The hadoop_version of this Cluster.
        :rtype: str
        """
        return self._hadoop_version

    @hadoop_version.setter
    def hadoop_version(self, hadoop_version):
        """Sets the hadoop_version of this Cluster.

        Hadoop组件版本信息。

        :param hadoop_version: The hadoop_version of this Cluster.
        :type hadoop_version: str
        """
        self._hadoop_version = hadoop_version

    @property
    def component_list(self):
        """Gets the component_list of this Cluster.

        组件列表信息。

        :return: The component_list of this Cluster.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.ComponentAmb`]
        """
        return self._component_list

    @component_list.setter
    def component_list(self, component_list):
        """Sets the component_list of this Cluster.

        组件列表信息。

        :param component_list: The component_list of this Cluster.
        :type component_list: list[:class:`huaweicloudsdkmrs.v1.ComponentAmb`]
        """
        self._component_list = component_list

    @property
    def external_ip(self):
        """Gets the external_ip of this Cluster.

        公网IP地址。

        :return: The external_ip of this Cluster.
        :rtype: str
        """
        return self._external_ip

    @external_ip.setter
    def external_ip(self, external_ip):
        """Sets the external_ip of this Cluster.

        公网IP地址。

        :param external_ip: The external_ip of this Cluster.
        :type external_ip: str
        """
        self._external_ip = external_ip

    @property
    def external_alternate_ip(self):
        """Gets the external_alternate_ip of this Cluster.

        公网备用IP地址。

        :return: The external_alternate_ip of this Cluster.
        :rtype: str
        """
        return self._external_alternate_ip

    @external_alternate_ip.setter
    def external_alternate_ip(self, external_alternate_ip):
        """Sets the external_alternate_ip of this Cluster.

        公网备用IP地址。

        :param external_alternate_ip: The external_alternate_ip of this Cluster.
        :type external_alternate_ip: str
        """
        self._external_alternate_ip = external_alternate_ip

    @property
    def internal_ip(self):
        """Gets the internal_ip of this Cluster.

        内网IP地址。

        :return: The internal_ip of this Cluster.
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this Cluster.

        内网IP地址。

        :param internal_ip: The internal_ip of this Cluster.
        :type internal_ip: str
        """
        self._internal_ip = internal_ip

    @property
    def deployment_id(self):
        """Gets the deployment_id of this Cluster.

        集群部署ID。

        :return: The deployment_id of this Cluster.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this Cluster.

        集群部署ID。

        :param deployment_id: The deployment_id of this Cluster.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def remark(self):
        """Gets the remark of this Cluster.

        集群备注信息。

        :return: The remark of this Cluster.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this Cluster.

        集群备注信息。

        :param remark: The remark of this Cluster.
        :type remark: str
        """
        self._remark = remark

    @property
    def order_id(self):
        """Gets the order_id of this Cluster.

        创建集群的订单号。

        :return: The order_id of this Cluster.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Cluster.

        创建集群的订单号。

        :param order_id: The order_id of this Cluster.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def az_id(self):
        """Gets the az_id of this Cluster.

        可用区域ID。

        :return: The az_id of this Cluster.
        :rtype: str
        """
        return self._az_id

    @az_id.setter
    def az_id(self, az_id):
        """Sets the az_id of this Cluster.

        可用区域ID。

        :param az_id: The az_id of this Cluster.
        :type az_id: str
        """
        self._az_id = az_id

    @property
    def az_name(self):
        """Gets the az_name of this Cluster.

        可用区域名称。

        :return: The az_name of this Cluster.
        :rtype: str
        """
        return self._az_name

    @az_name.setter
    def az_name(self, az_name):
        """Sets the az_name of this Cluster.

        可用区域名称。

        :param az_name: The az_name of this Cluster.
        :type az_name: str
        """
        self._az_name = az_name

    @property
    def az_code(self):
        """Gets the az_code of this Cluster.

        可用区域英文名称

        :return: The az_code of this Cluster.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this Cluster.

        可用区域英文名称

        :param az_code: The az_code of this Cluster.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this Cluster.

        可用区域

        :return: The availability_zone_id of this Cluster.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this Cluster.

        可用区域

        :param availability_zone_id: The availability_zone_id of this Cluster.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def instance_id(self):
        """Gets the instance_id of this Cluster.

        实例ID。

        :return: The instance_id of this Cluster.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Cluster.

        实例ID。

        :param instance_id: The instance_id of this Cluster.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vnc(self):
        """Gets the vnc of this Cluster.

        远程登录弹性云服务器的URI地址。

        :return: The vnc of this Cluster.
        :rtype: str
        """
        return self._vnc

    @vnc.setter
    def vnc(self, vnc):
        """Sets the vnc of this Cluster.

        远程登录弹性云服务器的URI地址。

        :param vnc: The vnc of this Cluster.
        :type vnc: str
        """
        self._vnc = vnc

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Cluster.

        项目编号。

        :return: The tenant_id of this Cluster.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Cluster.

        项目编号。

        :param tenant_id: The tenant_id of this Cluster.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def volume_size(self):
        """Gets the volume_size of this Cluster.

        磁盘存储空间。

        :return: The volume_size of this Cluster.
        :rtype: int
        """
        return self._volume_size

    @volume_size.setter
    def volume_size(self, volume_size):
        """Sets the volume_size of this Cluster.

        磁盘存储空间。

        :param volume_size: The volume_size of this Cluster.
        :type volume_size: int
        """
        self._volume_size = volume_size

    @property
    def volume_type(self):
        """Gets the volume_type of this Cluster.

        磁盘类型。

        :return: The volume_type of this Cluster.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this Cluster.

        磁盘类型。

        :param volume_type: The volume_type of this Cluster.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def subnet_id(self):
        """Gets the subnet_id of this Cluster.

        子网ID。

        :return: The subnet_id of this Cluster.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this Cluster.

        子网ID。

        :param subnet_id: The subnet_id of this Cluster.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this Cluster.

        子网名称。

        :return: The subnet_name of this Cluster.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this Cluster.

        子网名称。

        :param subnet_name: The subnet_name of this Cluster.
        :type subnet_name: str
        """
        self._subnet_name = subnet_name

    @property
    def security_groups_id(self):
        """Gets the security_groups_id of this Cluster.

        安全组ID。

        :return: The security_groups_id of this Cluster.
        :rtype: str
        """
        return self._security_groups_id

    @security_groups_id.setter
    def security_groups_id(self, security_groups_id):
        """Sets the security_groups_id of this Cluster.

        安全组ID。

        :param security_groups_id: The security_groups_id of this Cluster.
        :type security_groups_id: str
        """
        self._security_groups_id = security_groups_id

    @property
    def slave_security_groups_id(self):
        """Gets the slave_security_groups_id of this Cluster.

        非Master节点的安全组id，当前一个MRS集群只会使用一个安全组，所以该字段已经废弃，从兼容性考虑，该字段会返回和securityGroupsId同样的值。

        :return: The slave_security_groups_id of this Cluster.
        :rtype: str
        """
        return self._slave_security_groups_id

    @slave_security_groups_id.setter
    def slave_security_groups_id(self, slave_security_groups_id):
        """Sets the slave_security_groups_id of this Cluster.

        非Master节点的安全组id，当前一个MRS集群只会使用一个安全组，所以该字段已经废弃，从兼容性考虑，该字段会返回和securityGroupsId同样的值。

        :param slave_security_groups_id: The slave_security_groups_id of this Cluster.
        :type slave_security_groups_id: str
        """
        self._slave_security_groups_id = slave_security_groups_id

    @property
    def bootstrap_scripts(self):
        """Gets the bootstrap_scripts of this Cluster.

        配置引导操作脚本信息。

        :return: The bootstrap_scripts of this Cluster.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.BootstrapScript`]
        """
        return self._bootstrap_scripts

    @bootstrap_scripts.setter
    def bootstrap_scripts(self, bootstrap_scripts):
        """Sets the bootstrap_scripts of this Cluster.

        配置引导操作脚本信息。

        :param bootstrap_scripts: The bootstrap_scripts of this Cluster.
        :type bootstrap_scripts: list[:class:`huaweicloudsdkmrs.v1.BootstrapScript`]
        """
        self._bootstrap_scripts = bootstrap_scripts

    @property
    def safe_mode(self):
        """Gets the safe_mode of this Cluster.

        MRS集群运行模式。 - 0：普通集群 - 1：安全集群

        :return: The safe_mode of this Cluster.
        :rtype: int
        """
        return self._safe_mode

    @safe_mode.setter
    def safe_mode(self, safe_mode):
        """Sets the safe_mode of this Cluster.

        MRS集群运行模式。 - 0：普通集群 - 1：安全集群

        :param safe_mode: The safe_mode of this Cluster.
        :type safe_mode: int
        """
        self._safe_mode = safe_mode

    @property
    def cluster_version(self):
        """Gets the cluster_version of this Cluster.

        集群版本。

        :return: The cluster_version of this Cluster.
        :rtype: str
        """
        return self._cluster_version

    @cluster_version.setter
    def cluster_version(self, cluster_version):
        """Sets the cluster_version of this Cluster.

        集群版本。

        :param cluster_version: The cluster_version of this Cluster.
        :type cluster_version: str
        """
        self._cluster_version = cluster_version

    @property
    def node_public_cert_name(self):
        """Gets the node_public_cert_name of this Cluster.

        密钥文件名称。

        :return: The node_public_cert_name of this Cluster.
        :rtype: str
        """
        return self._node_public_cert_name

    @node_public_cert_name.setter
    def node_public_cert_name(self, node_public_cert_name):
        """Sets the node_public_cert_name of this Cluster.

        密钥文件名称。

        :param node_public_cert_name: The node_public_cert_name of this Cluster.
        :type node_public_cert_name: str
        """
        self._node_public_cert_name = node_public_cert_name

    @property
    def master_node_ip(self):
        """Gets the master_node_ip of this Cluster.

        Master节点IP。

        :return: The master_node_ip of this Cluster.
        :rtype: str
        """
        return self._master_node_ip

    @master_node_ip.setter
    def master_node_ip(self, master_node_ip):
        """Sets the master_node_ip of this Cluster.

        Master节点IP。

        :param master_node_ip: The master_node_ip of this Cluster.
        :type master_node_ip: str
        """
        self._master_node_ip = master_node_ip

    @property
    def private_ip_first(self):
        """Gets the private_ip_first of this Cluster.

        首选私有IP。

        :return: The private_ip_first of this Cluster.
        :rtype: str
        """
        return self._private_ip_first

    @private_ip_first.setter
    def private_ip_first(self, private_ip_first):
        """Sets the private_ip_first of this Cluster.

        首选私有IP。

        :param private_ip_first: The private_ip_first of this Cluster.
        :type private_ip_first: str
        """
        self._private_ip_first = private_ip_first

    @property
    def error_info(self):
        """Gets the error_info of this Cluster.

        错误信息。

        :return: The error_info of this Cluster.
        :rtype: str
        """
        return self._error_info

    @error_info.setter
    def error_info(self, error_info):
        """Sets the error_info of this Cluster.

        错误信息。

        :param error_info: The error_info of this Cluster.
        :type error_info: str
        """
        self._error_info = error_info

    @property
    def tags(self):
        """Gets the tags of this Cluster.

        标签信息

        :return: The tags of this Cluster.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Cluster.

        标签信息

        :param tags: The tags of this Cluster.
        :type tags: str
        """
        self._tags = tags

    @property
    def master_node_num(self):
        """Gets the master_node_num of this Cluster.

        集群部署的Master节点数量。

        :return: The master_node_num of this Cluster.
        :rtype: str
        """
        return self._master_node_num

    @master_node_num.setter
    def master_node_num(self, master_node_num):
        """Sets the master_node_num of this Cluster.

        集群部署的Master节点数量。

        :param master_node_num: The master_node_num of this Cluster.
        :type master_node_num: str
        """
        self._master_node_num = master_node_num

    @property
    def core_node_num(self):
        """Gets the core_node_num of this Cluster.

        集群部署的Core节点数量。

        :return: The core_node_num of this Cluster.
        :rtype: str
        """
        return self._core_node_num

    @core_node_num.setter
    def core_node_num(self, core_node_num):
        """Sets the core_node_num of this Cluster.

        集群部署的Core节点数量。

        :param core_node_num: The core_node_num of this Cluster.
        :type core_node_num: str
        """
        self._core_node_num = core_node_num

    @property
    def master_node_size(self):
        """Gets the master_node_size of this Cluster.

        Master节点的实例规格。

        :return: The master_node_size of this Cluster.
        :rtype: str
        """
        return self._master_node_size

    @master_node_size.setter
    def master_node_size(self, master_node_size):
        """Sets the master_node_size of this Cluster.

        Master节点的实例规格。

        :param master_node_size: The master_node_size of this Cluster.
        :type master_node_size: str
        """
        self._master_node_size = master_node_size

    @property
    def core_node_size(self):
        """Gets the core_node_size of this Cluster.

        Core节点的实例规格。

        :return: The core_node_size of this Cluster.
        :rtype: str
        """
        return self._core_node_size

    @core_node_size.setter
    def core_node_size(self, core_node_size):
        """Sets the core_node_size of this Cluster.

        Core节点的实例规格。

        :param core_node_size: The core_node_size of this Cluster.
        :type core_node_size: str
        """
        self._core_node_size = core_node_size

    @property
    def master_node_product_id(self):
        """Gets the master_node_product_id of this Cluster.

        Master节点产品ID。

        :return: The master_node_product_id of this Cluster.
        :rtype: str
        """
        return self._master_node_product_id

    @master_node_product_id.setter
    def master_node_product_id(self, master_node_product_id):
        """Sets the master_node_product_id of this Cluster.

        Master节点产品ID。

        :param master_node_product_id: The master_node_product_id of this Cluster.
        :type master_node_product_id: str
        """
        self._master_node_product_id = master_node_product_id

    @property
    def master_node_spec_id(self):
        """Gets the master_node_spec_id of this Cluster.

        Master节点规格ID。

        :return: The master_node_spec_id of this Cluster.
        :rtype: str
        """
        return self._master_node_spec_id

    @master_node_spec_id.setter
    def master_node_spec_id(self, master_node_spec_id):
        """Sets the master_node_spec_id of this Cluster.

        Master节点规格ID。

        :param master_node_spec_id: The master_node_spec_id of this Cluster.
        :type master_node_spec_id: str
        """
        self._master_node_spec_id = master_node_spec_id

    @property
    def core_node_product_id(self):
        """Gets the core_node_product_id of this Cluster.

        Core节点产品ID。

        :return: The core_node_product_id of this Cluster.
        :rtype: str
        """
        return self._core_node_product_id

    @core_node_product_id.setter
    def core_node_product_id(self, core_node_product_id):
        """Sets the core_node_product_id of this Cluster.

        Core节点产品ID。

        :param core_node_product_id: The core_node_product_id of this Cluster.
        :type core_node_product_id: str
        """
        self._core_node_product_id = core_node_product_id

    @property
    def core_node_spec_id(self):
        """Gets the core_node_spec_id of this Cluster.

        Core节点规格ID。

        :return: The core_node_spec_id of this Cluster.
        :rtype: str
        """
        return self._core_node_spec_id

    @core_node_spec_id.setter
    def core_node_spec_id(self, core_node_spec_id):
        """Sets the core_node_spec_id of this Cluster.

        Core节点规格ID。

        :param core_node_spec_id: The core_node_spec_id of this Cluster.
        :type core_node_spec_id: str
        """
        self._core_node_spec_id = core_node_spec_id

    @property
    def master_data_volume_type(self):
        """Gets the master_data_volume_type of this Cluster.

        Master节点数据磁盘存储类别，目前支持SATA、SAS和SSD。

        :return: The master_data_volume_type of this Cluster.
        :rtype: str
        """
        return self._master_data_volume_type

    @master_data_volume_type.setter
    def master_data_volume_type(self, master_data_volume_type):
        """Sets the master_data_volume_type of this Cluster.

        Master节点数据磁盘存储类别，目前支持SATA、SAS和SSD。

        :param master_data_volume_type: The master_data_volume_type of this Cluster.
        :type master_data_volume_type: str
        """
        self._master_data_volume_type = master_data_volume_type

    @property
    def master_data_volume_size(self):
        """Gets the master_data_volume_size of this Cluster.

        Master节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。 取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :return: The master_data_volume_size of this Cluster.
        :rtype: int
        """
        return self._master_data_volume_size

    @master_data_volume_size.setter
    def master_data_volume_size(self, master_data_volume_size):
        """Sets the master_data_volume_size of this Cluster.

        Master节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。 取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :param master_data_volume_size: The master_data_volume_size of this Cluster.
        :type master_data_volume_size: int
        """
        self._master_data_volume_size = master_data_volume_size

    @property
    def master_data_volume_count(self):
        """Gets the master_data_volume_count of this Cluster.

        Master节点数据磁盘个数。 取值只能是1

        :return: The master_data_volume_count of this Cluster.
        :rtype: int
        """
        return self._master_data_volume_count

    @master_data_volume_count.setter
    def master_data_volume_count(self, master_data_volume_count):
        """Sets the master_data_volume_count of this Cluster.

        Master节点数据磁盘个数。 取值只能是1

        :param master_data_volume_count: The master_data_volume_count of this Cluster.
        :type master_data_volume_count: int
        """
        self._master_data_volume_count = master_data_volume_count

    @property
    def core_data_volume_type(self):
        """Gets the core_data_volume_type of this Cluster.

        Core节点数据磁盘存储类别，目前支持SATA、SAS和SSD。

        :return: The core_data_volume_type of this Cluster.
        :rtype: str
        """
        return self._core_data_volume_type

    @core_data_volume_type.setter
    def core_data_volume_type(self, core_data_volume_type):
        """Sets the core_data_volume_type of this Cluster.

        Core节点数据磁盘存储类别，目前支持SATA、SAS和SSD。

        :param core_data_volume_type: The core_data_volume_type of this Cluster.
        :type core_data_volume_type: str
        """
        self._core_data_volume_type = core_data_volume_type

    @property
    def core_data_volume_size(self):
        """Gets the core_data_volume_size of this Cluster.

        Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。 取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :return: The core_data_volume_size of this Cluster.
        :rtype: int
        """
        return self._core_data_volume_size

    @core_data_volume_size.setter
    def core_data_volume_size(self, core_data_volume_size):
        """Sets the core_data_volume_size of this Cluster.

        Core节点数据磁盘存储空间。为增大数据存储容量，创建集群时可同时添加磁盘。 取值范围：100GB～32000GB，传值只需填数字，不需要带单位GB。

        :param core_data_volume_size: The core_data_volume_size of this Cluster.
        :type core_data_volume_size: int
        """
        self._core_data_volume_size = core_data_volume_size

    @property
    def core_data_volume_count(self):
        """Gets the core_data_volume_count of this Cluster.

        Core节点数据磁盘个数。 取值范围：1～10

        :return: The core_data_volume_count of this Cluster.
        :rtype: int
        """
        return self._core_data_volume_count

    @core_data_volume_count.setter
    def core_data_volume_count(self, core_data_volume_count):
        """Sets the core_data_volume_count of this Cluster.

        Core节点数据磁盘个数。 取值范围：1～10

        :param core_data_volume_count: The core_data_volume_count of this Cluster.
        :type core_data_volume_count: int
        """
        self._core_data_volume_count = core_data_volume_count

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this Cluster.

        企业项目ID。

        :return: The enterprise_project_id of this Cluster.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this Cluster.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this Cluster.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def is_mrs_manager_finish(self):
        """Gets the is_mrs_manager_finish of this Cluster.

        表示集群创建过程中，MRS Manager是否安装完成。 - true：安装完成 - false：安装未完成

        :return: The is_mrs_manager_finish of this Cluster.
        :rtype: bool
        """
        return self._is_mrs_manager_finish

    @is_mrs_manager_finish.setter
    def is_mrs_manager_finish(self, is_mrs_manager_finish):
        """Sets the is_mrs_manager_finish of this Cluster.

        表示集群创建过程中，MRS Manager是否安装完成。 - true：安装完成 - false：安装未完成

        :param is_mrs_manager_finish: The is_mrs_manager_finish of this Cluster.
        :type is_mrs_manager_finish: bool
        """
        self._is_mrs_manager_finish = is_mrs_manager_finish

    @property
    def cluster_type(self):
        """Gets the cluster_type of this Cluster.

        集群类型。

        :return: The cluster_type of this Cluster.
        :rtype: int
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this Cluster.

        集群类型。

        :param cluster_type: The cluster_type of this Cluster.
        :type cluster_type: int
        """
        self._cluster_type = cluster_type

    @property
    def log_collection(self):
        """Gets the log_collection of this Cluster.

        集群安装失败时，是否搜集日志。 - 0：不收集 - 1：收集

        :return: The log_collection of this Cluster.
        :rtype: int
        """
        return self._log_collection

    @log_collection.setter
    def log_collection(self, log_collection):
        """Sets the log_collection of this Cluster.

        集群安装失败时，是否搜集日志。 - 0：不收集 - 1：收集

        :param log_collection: The log_collection of this Cluster.
        :type log_collection: int
        """
        self._log_collection = log_collection

    @property
    def period_type(self):
        """Gets the period_type of this Cluster.

        区分包周期，集群是包年还是包月。 - 0：包月 - 1：包年

        :return: The period_type of this Cluster.
        :rtype: int
        """
        return self._period_type

    @period_type.setter
    def period_type(self, period_type):
        """Sets the period_type of this Cluster.

        区分包周期，集群是包年还是包月。 - 0：包月 - 1：包年

        :param period_type: The period_type of this Cluster.
        :type period_type: int
        """
        self._period_type = period_type

    @property
    def scale(self):
        """Gets the scale of this Cluster.

        集群节点的变更状态（扩容/缩容/变更规格）。当该参数取值为空时，表示集群节点没有进行变更操作。 取值范围： - scaling-out：扩容中 - scaling-in：缩容中 - scaling-error：处于running状态，且上一次扩容/缩容/升级规格失败的集群 - scaling-up：Master节点规格升级中 - scaling_up_first：备Master节点规格升级中 - scaled_up_first：备Master节点规格升级成功 - scaled-up-success：Master节点规格升级成功

        :return: The scale of this Cluster.
        :rtype: str
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this Cluster.

        集群节点的变更状态（扩容/缩容/变更规格）。当该参数取值为空时，表示集群节点没有进行变更操作。 取值范围： - scaling-out：扩容中 - scaling-in：缩容中 - scaling-error：处于running状态，且上一次扩容/缩容/升级规格失败的集群 - scaling-up：Master节点规格升级中 - scaling_up_first：备Master节点规格升级中 - scaled_up_first：备Master节点规格升级成功 - scaled-up-success：Master节点规格升级成功

        :param scale: The scale of this Cluster.
        :type scale: str
        """
        self._scale = scale

    @property
    def node_groups(self):
        """Gets the node_groups of this Cluster.

        Master节点、Core节点和Task节点列表信息。

        :return: The node_groups of this Cluster.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV10`]
        """
        return self._node_groups

    @node_groups.setter
    def node_groups(self, node_groups):
        """Sets the node_groups of this Cluster.

        Master节点、Core节点和Task节点列表信息。

        :param node_groups: The node_groups of this Cluster.
        :type node_groups: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV10`]
        """
        self._node_groups = node_groups

    @property
    def task_node_groups(self):
        """Gets the task_node_groups of this Cluster.

        Task节点列表信息。

        :return: The task_node_groups of this Cluster.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV10`]
        """
        return self._task_node_groups

    @task_node_groups.setter
    def task_node_groups(self, task_node_groups):
        """Sets the task_node_groups of this Cluster.

        Task节点列表信息。

        :param task_node_groups: The task_node_groups of this Cluster.
        :type task_node_groups: list[:class:`huaweicloudsdkmrs.v1.NodeGroupV10`]
        """
        self._task_node_groups = task_node_groups

    @property
    def eip_id(self):
        """Gets the eip_id of this Cluster.

        集群弹性公网ip的唯一标识

        :return: The eip_id of this Cluster.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this Cluster.

        集群弹性公网ip的唯一标识

        :param eip_id: The eip_id of this Cluster.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def eip_address(self):
        """Gets the eip_address of this Cluster.

        集群弹性公网ip的IPV4地址

        :return: The eip_address of this Cluster.
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this Cluster.

        集群弹性公网ip的IPV4地址

        :param eip_address: The eip_address of this Cluster.
        :type eip_address: str
        """
        self._eip_address = eip_address

    @property
    def eipv6_address(self):
        """Gets the eipv6_address of this Cluster.

        集群弹性公网ip的IPV6地址，IPv4时无此字段。

        :return: The eipv6_address of this Cluster.
        :rtype: str
        """
        return self._eipv6_address

    @eipv6_address.setter
    def eipv6_address(self, eipv6_address):
        """Sets the eipv6_address of this Cluster.

        集群弹性公网ip的IPV6地址，IPv4时无此字段。

        :param eipv6_address: The eipv6_address of this Cluster.
        :type eipv6_address: str
        """
        self._eipv6_address = eipv6_address

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
        if not isinstance(other, Cluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
