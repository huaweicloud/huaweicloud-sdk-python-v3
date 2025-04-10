# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeNodeResp:

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
        'created_at': 'str',
        'updated_at': 'str',
        'project_id': 'str',
        'private_key': 'str',
        'certificate': 'str',
        'ca': 'str',
        'state': 'str',
        'package': 'str',
        'master_addr': 'str',
        'cpu': 'int',
        'memory': 'int',
        'os_name': 'str',
        'os_version': 'str',
        'pause_docker_image': 'str',
        'arch': 'str',
        'os_type': 'str',
        'deployment_num': 'int',
        'enable_gpu': 'bool',
        'log_configs': 'list[LogConfigs]',
        'device_infos': 'list[DeviceInfos]',
        'edged_version': 'str',
        'gpu_num': 'int',
        'host_ips': 'list[str]',
        'relation': 'str',
        'comment': 'str',
        'gpu_info': 'list[GpuInfo]',
        'device_num': 'int',
        'enable_npu': 'bool',
        'npu_type': 'str',
        'nics': 'list[Nics]',
        'host_name': 'str',
        'ief_node_version': 'str',
        'upgrade_flag': 'bool',
        'product_id': 'str',
        'group_ids': 'list[str]',
        'upgrade_history': 'list[UpgradeHistory]',
        'attributes': 'list[Attributes]',
        'docker_enable': 'bool',
        'mqtt_mode': 'str',
        'mqtt_external': 'str',
        'mqtt_internal': 'str',
        'node_type': 'str',
        'ntp_configs': 'NtpConfigs',
        'error_reason': 'str',
        'tags': 'list[ResourceTag]',
        'npu_num': 'int',
        'npu_info': 'list[NpuInfo]',
        'container_runtime_version': 'str',
        'identifier': 'str',
        'purchase_id': 'str',
        'state_details': 'StateDetails',
        'cert_remaining_valid_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'project_id': 'project_id',
        'private_key': 'private_key',
        'certificate': 'certificate',
        'ca': 'ca',
        'state': 'state',
        'package': 'package',
        'master_addr': 'master_addr',
        'cpu': 'cpu',
        'memory': 'memory',
        'os_name': 'os_name',
        'os_version': 'os_version',
        'pause_docker_image': 'pause_docker_image',
        'arch': 'arch',
        'os_type': 'os_type',
        'deployment_num': 'deployment_num',
        'enable_gpu': 'enable_gpu',
        'log_configs': 'log_configs',
        'device_infos': 'device_infos',
        'edged_version': 'edged_version',
        'gpu_num': 'gpu_num',
        'host_ips': 'host_ips',
        'relation': 'relation',
        'comment': 'comment',
        'gpu_info': 'gpu_info',
        'device_num': 'device_num',
        'enable_npu': 'enable_npu',
        'npu_type': 'npu_type',
        'nics': 'nics',
        'host_name': 'host_name',
        'ief_node_version': 'ief_node_version',
        'upgrade_flag': 'upgrade_flag',
        'product_id': 'product_id',
        'group_ids': 'group_ids',
        'upgrade_history': 'upgrade_history',
        'attributes': 'attributes',
        'docker_enable': 'docker_enable',
        'mqtt_mode': 'mqtt_mode',
        'mqtt_external': 'mqtt_external',
        'mqtt_internal': 'mqtt_internal',
        'node_type': 'node_type',
        'ntp_configs': 'ntp_configs',
        'error_reason': 'error_reason',
        'tags': 'tags',
        'npu_num': 'npu_num',
        'npu_info': 'npu_info',
        'container_runtime_version': 'container_runtime_version',
        'identifier': 'identifier',
        'purchase_id': 'purchase_id',
        'state_details': 'state_details',
        'cert_remaining_valid_time': 'cert_remaining_valid_time'
    }

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, project_id=None, private_key=None, certificate=None, ca=None, state=None, package=None, master_addr=None, cpu=None, memory=None, os_name=None, os_version=None, pause_docker_image=None, arch=None, os_type=None, deployment_num=None, enable_gpu=None, log_configs=None, device_infos=None, edged_version=None, gpu_num=None, host_ips=None, relation=None, comment=None, gpu_info=None, device_num=None, enable_npu=None, npu_type=None, nics=None, host_name=None, ief_node_version=None, upgrade_flag=None, product_id=None, group_ids=None, upgrade_history=None, attributes=None, docker_enable=None, mqtt_mode=None, mqtt_external=None, mqtt_internal=None, node_type=None, ntp_configs=None, error_reason=None, tags=None, npu_num=None, npu_info=None, container_runtime_version=None, identifier=None, purchase_id=None, state_details=None, cert_remaining_valid_time=None):
        r"""EdgeNodeResp

        The model defined in huaweicloud sdk

        :param id: 边缘节点ID
        :type id: str
        :param name: 边缘节点名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64 Name为必填字段，且本账号中唯一。
        :type name: str
        :param description: 边缘节点描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param project_id: 项目ID
        :type project_id: str
        :param private_key: 私钥
        :type private_key: str
        :param certificate: 证书
        :type certificate: str
        :param ca: 根证书
        :type ca: str
        :param state: 边缘节点状态 - UNCONNECTED（未注册） - RUNNING（运行中） - FAIL（故障） - STOPPED（停用） - UPGRADING（升级中） - FREEZE（冻结）
        :type state: str
        :param package: 将证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。
        :type package: str
        :param master_addr: 云端服务URL
        :type master_addr: str
        :param cpu: 边缘节点CPU核心数
        :type cpu: int
        :param memory: 边缘节点内存大小，单位M
        :type memory: int
        :param os_name: 边缘节点操作系统名称
        :type os_name: str
        :param os_version: 边缘节点操作系统版本
        :type os_version: str
        :param pause_docker_image: pause容器镜像URL
        :type pause_docker_image: str
        :param arch: 边缘节点架构
        :type arch: str
        :param os_type: 边缘节点操作系统类型
        :type os_type: str
        :param deployment_num: 部署在该边缘节点上的应用实例个数
        :type deployment_num: int
        :param enable_gpu: 边缘节点是否开启GPU，默认为false
        :type enable_gpu: bool
        :param log_configs: 边缘节点日志配置，当用户未配置日志相关字段时，将默认打开日志上传到云端功能。
        :type log_configs: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        :param device_infos: 关联设备信息
        :type device_infos: list[:class:`huaweicloudsdkief.v1.DeviceInfos`]
        :param edged_version: edged版本
        :type edged_version: str
        :param gpu_num: gpu个数
        :type gpu_num: int
        :param host_ips: 主机IP，默认返回eth0网卡的IP。
        :type host_ips: list[str]
        :param relation: 与device绑定关系名称（通过device id查询node时有值）
        :type relation: str
        :param comment: 与device绑定关系描述（通过device id查询node时有值）
        :type comment: str
        :param gpu_info: gpu型号和gpu memory大小
        :type gpu_info: list[:class:`huaweicloudsdkief.v1.GpuInfo`]
        :param device_num: 关联设备数量
        :type device_num: int
        :param enable_npu: 边缘节点是否开启NPU，true表示开启，false表示不开启，默认为false
        :type enable_npu: bool
        :param npu_type: NPU类型，支持D310、D310B，支持填写： - D310：D310类型 - D310B：D310B类型 - 空值：D310类型。
        :type npu_type: str
        :param nics: 节点网卡和对应IP地址信息
        :type nics: list[:class:`huaweicloudsdkief.v1.Nics`]
        :param host_name: 边缘节点主机名
        :type host_name: str
        :param ief_node_version: 边缘节点版本
        :type ief_node_version: str
        :param upgrade_flag: 是否能升级的标志 - true：需要升级 - false：不需要升级
        :type upgrade_flag: bool
        :param product_id: 产品ID（通过产品证书方式纳管）
        :type product_id: str
        :param group_ids: 节点组ID（一个节点属于多个节点组）
        :type group_ids: list[str]
        :param upgrade_history: 节点安装或升级记录
        :type upgrade_history: list[:class:`huaweicloudsdkief.v1.UpgradeHistory`]
        :param attributes: 边缘节点属性，关联属性个数最多为32个
        :type attributes: list[:class:`huaweicloudsdkief.v1.Attributes`]
        :param docker_enable: 节点是否开启Docker
        :type docker_enable: bool
        :param mqtt_mode: mqtt集成模式 - internal：edgecore内置mqtt - external：外置开源mqtt
        :type mqtt_mode: str
        :param mqtt_external: 外置开源mqtt地址
        :type mqtt_external: str
        :param mqtt_internal: edgecore内置的mqtt地址
        :type mqtt_internal: str
        :param node_type: 节点类型，默认为空，非空时为小站节点
        :type node_type: str
        :param ntp_configs: 
        :type ntp_configs: :class:`huaweicloudsdkief.v1.NtpConfigs`
        :param error_reason: 节点故障原因
        :type error_reason: str
        :param tags: 边缘节点标签，标签个数最多为20个
        :type tags: list[:class:`huaweicloudsdkief.v1.ResourceTag`]
        :param npu_num: NPU数量
        :type npu_num: int
        :param npu_info: NPU型号和NPU Memory大小
        :type npu_info: list[:class:`huaweicloudsdkief.v1.NpuInfo`]
        :param container_runtime_version: 容器运行时版本
        :type container_runtime_version: str
        :param identifier: 边缘节点使用token注册时的凭证
        :type identifier: str
        :param purchase_id: IEC/IES节点id
        :type purchase_id: str
        :param state_details: 
        :type state_details: :class:`huaweicloudsdkief.v1.StateDetails`
        :param cert_remaining_valid_time: 证书有效期持续时间
        :type cert_remaining_valid_time: int
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._project_id = None
        self._private_key = None
        self._certificate = None
        self._ca = None
        self._state = None
        self._package = None
        self._master_addr = None
        self._cpu = None
        self._memory = None
        self._os_name = None
        self._os_version = None
        self._pause_docker_image = None
        self._arch = None
        self._os_type = None
        self._deployment_num = None
        self._enable_gpu = None
        self._log_configs = None
        self._device_infos = None
        self._edged_version = None
        self._gpu_num = None
        self._host_ips = None
        self._relation = None
        self._comment = None
        self._gpu_info = None
        self._device_num = None
        self._enable_npu = None
        self._npu_type = None
        self._nics = None
        self._host_name = None
        self._ief_node_version = None
        self._upgrade_flag = None
        self._product_id = None
        self._group_ids = None
        self._upgrade_history = None
        self._attributes = None
        self._docker_enable = None
        self._mqtt_mode = None
        self._mqtt_external = None
        self._mqtt_internal = None
        self._node_type = None
        self._ntp_configs = None
        self._error_reason = None
        self._tags = None
        self._npu_num = None
        self._npu_info = None
        self._container_runtime_version = None
        self._identifier = None
        self._purchase_id = None
        self._state_details = None
        self._cert_remaining_valid_time = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at
        self.project_id = project_id
        self.private_key = private_key
        self.certificate = certificate
        self.ca = ca
        self.state = state
        self.package = package
        self.master_addr = master_addr
        self.cpu = cpu
        self.memory = memory
        self.os_name = os_name
        self.os_version = os_version
        self.pause_docker_image = pause_docker_image
        self.arch = arch
        self.os_type = os_type
        self.deployment_num = deployment_num
        self.enable_gpu = enable_gpu
        self.log_configs = log_configs
        self.device_infos = device_infos
        self.edged_version = edged_version
        self.gpu_num = gpu_num
        self.host_ips = host_ips
        self.relation = relation
        self.comment = comment
        self.gpu_info = gpu_info
        self.device_num = device_num
        self.enable_npu = enable_npu
        self.npu_type = npu_type
        self.nics = nics
        self.host_name = host_name
        self.ief_node_version = ief_node_version
        self.upgrade_flag = upgrade_flag
        self.product_id = product_id
        self.group_ids = group_ids
        self.upgrade_history = upgrade_history
        self.attributes = attributes
        self.docker_enable = docker_enable
        self.mqtt_mode = mqtt_mode
        self.mqtt_external = mqtt_external
        self.mqtt_internal = mqtt_internal
        self.node_type = node_type
        self.ntp_configs = ntp_configs
        self.error_reason = error_reason
        self.tags = tags
        self.npu_num = npu_num
        self.npu_info = npu_info
        self.container_runtime_version = container_runtime_version
        if identifier is not None:
            self.identifier = identifier
        if purchase_id is not None:
            self.purchase_id = purchase_id
        if state_details is not None:
            self.state_details = state_details
        if cert_remaining_valid_time is not None:
            self.cert_remaining_valid_time = cert_remaining_valid_time

    @property
    def id(self):
        r"""Gets the id of this EdgeNodeResp.

        边缘节点ID

        :return: The id of this EdgeNodeResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EdgeNodeResp.

        边缘节点ID

        :param id: The id of this EdgeNodeResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this EdgeNodeResp.

        边缘节点名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64 Name为必填字段，且本账号中唯一。

        :return: The name of this EdgeNodeResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EdgeNodeResp.

        边缘节点名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64 Name为必填字段，且本账号中唯一。

        :param name: The name of this EdgeNodeResp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this EdgeNodeResp.

        边缘节点描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this EdgeNodeResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EdgeNodeResp.

        边缘节点描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this EdgeNodeResp.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this EdgeNodeResp.

        创建时间

        :return: The created_at of this EdgeNodeResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EdgeNodeResp.

        创建时间

        :param created_at: The created_at of this EdgeNodeResp.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this EdgeNodeResp.

        更新时间

        :return: The updated_at of this EdgeNodeResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this EdgeNodeResp.

        更新时间

        :param updated_at: The updated_at of this EdgeNodeResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def project_id(self):
        r"""Gets the project_id of this EdgeNodeResp.

        项目ID

        :return: The project_id of this EdgeNodeResp.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this EdgeNodeResp.

        项目ID

        :param project_id: The project_id of this EdgeNodeResp.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def private_key(self):
        r"""Gets the private_key of this EdgeNodeResp.

        私钥

        :return: The private_key of this EdgeNodeResp.
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        r"""Sets the private_key of this EdgeNodeResp.

        私钥

        :param private_key: The private_key of this EdgeNodeResp.
        :type private_key: str
        """
        self._private_key = private_key

    @property
    def certificate(self):
        r"""Gets the certificate of this EdgeNodeResp.

        证书

        :return: The certificate of this EdgeNodeResp.
        :rtype: str
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        r"""Sets the certificate of this EdgeNodeResp.

        证书

        :param certificate: The certificate of this EdgeNodeResp.
        :type certificate: str
        """
        self._certificate = certificate

    @property
    def ca(self):
        r"""Gets the ca of this EdgeNodeResp.

        根证书

        :return: The ca of this EdgeNodeResp.
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        r"""Sets the ca of this EdgeNodeResp.

        根证书

        :param ca: The ca of this EdgeNodeResp.
        :type ca: str
        """
        self._ca = ca

    @property
    def state(self):
        r"""Gets the state of this EdgeNodeResp.

        边缘节点状态 - UNCONNECTED（未注册） - RUNNING（运行中） - FAIL（故障） - STOPPED（停用） - UPGRADING（升级中） - FREEZE（冻结）

        :return: The state of this EdgeNodeResp.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this EdgeNodeResp.

        边缘节点状态 - UNCONNECTED（未注册） - RUNNING（运行中） - FAIL（故障） - STOPPED（停用） - UPGRADING（升级中） - FREEZE（冻结）

        :param state: The state of this EdgeNodeResp.
        :type state: str
        """
        self._state = state

    @property
    def package(self):
        r"""Gets the package of this EdgeNodeResp.

        将证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。

        :return: The package of this EdgeNodeResp.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package):
        r"""Sets the package of this EdgeNodeResp.

        将证书文件certificate/ca/private_key打成.tar.gz包后用base64编码的字符串。 使用时请使用base64解码成.tar.gz包。

        :param package: The package of this EdgeNodeResp.
        :type package: str
        """
        self._package = package

    @property
    def master_addr(self):
        r"""Gets the master_addr of this EdgeNodeResp.

        云端服务URL

        :return: The master_addr of this EdgeNodeResp.
        :rtype: str
        """
        return self._master_addr

    @master_addr.setter
    def master_addr(self, master_addr):
        r"""Sets the master_addr of this EdgeNodeResp.

        云端服务URL

        :param master_addr: The master_addr of this EdgeNodeResp.
        :type master_addr: str
        """
        self._master_addr = master_addr

    @property
    def cpu(self):
        r"""Gets the cpu of this EdgeNodeResp.

        边缘节点CPU核心数

        :return: The cpu of this EdgeNodeResp.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this EdgeNodeResp.

        边缘节点CPU核心数

        :param cpu: The cpu of this EdgeNodeResp.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def memory(self):
        r"""Gets the memory of this EdgeNodeResp.

        边缘节点内存大小，单位M

        :return: The memory of this EdgeNodeResp.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this EdgeNodeResp.

        边缘节点内存大小，单位M

        :param memory: The memory of this EdgeNodeResp.
        :type memory: int
        """
        self._memory = memory

    @property
    def os_name(self):
        r"""Gets the os_name of this EdgeNodeResp.

        边缘节点操作系统名称

        :return: The os_name of this EdgeNodeResp.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this EdgeNodeResp.

        边缘节点操作系统名称

        :param os_name: The os_name of this EdgeNodeResp.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_version(self):
        r"""Gets the os_version of this EdgeNodeResp.

        边缘节点操作系统版本

        :return: The os_version of this EdgeNodeResp.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this EdgeNodeResp.

        边缘节点操作系统版本

        :param os_version: The os_version of this EdgeNodeResp.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def pause_docker_image(self):
        r"""Gets the pause_docker_image of this EdgeNodeResp.

        pause容器镜像URL

        :return: The pause_docker_image of this EdgeNodeResp.
        :rtype: str
        """
        return self._pause_docker_image

    @pause_docker_image.setter
    def pause_docker_image(self, pause_docker_image):
        r"""Sets the pause_docker_image of this EdgeNodeResp.

        pause容器镜像URL

        :param pause_docker_image: The pause_docker_image of this EdgeNodeResp.
        :type pause_docker_image: str
        """
        self._pause_docker_image = pause_docker_image

    @property
    def arch(self):
        r"""Gets the arch of this EdgeNodeResp.

        边缘节点架构

        :return: The arch of this EdgeNodeResp.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this EdgeNodeResp.

        边缘节点架构

        :param arch: The arch of this EdgeNodeResp.
        :type arch: str
        """
        self._arch = arch

    @property
    def os_type(self):
        r"""Gets the os_type of this EdgeNodeResp.

        边缘节点操作系统类型

        :return: The os_type of this EdgeNodeResp.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this EdgeNodeResp.

        边缘节点操作系统类型

        :param os_type: The os_type of this EdgeNodeResp.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def deployment_num(self):
        r"""Gets the deployment_num of this EdgeNodeResp.

        部署在该边缘节点上的应用实例个数

        :return: The deployment_num of this EdgeNodeResp.
        :rtype: int
        """
        return self._deployment_num

    @deployment_num.setter
    def deployment_num(self, deployment_num):
        r"""Sets the deployment_num of this EdgeNodeResp.

        部署在该边缘节点上的应用实例个数

        :param deployment_num: The deployment_num of this EdgeNodeResp.
        :type deployment_num: int
        """
        self._deployment_num = deployment_num

    @property
    def enable_gpu(self):
        r"""Gets the enable_gpu of this EdgeNodeResp.

        边缘节点是否开启GPU，默认为false

        :return: The enable_gpu of this EdgeNodeResp.
        :rtype: bool
        """
        return self._enable_gpu

    @enable_gpu.setter
    def enable_gpu(self, enable_gpu):
        r"""Sets the enable_gpu of this EdgeNodeResp.

        边缘节点是否开启GPU，默认为false

        :param enable_gpu: The enable_gpu of this EdgeNodeResp.
        :type enable_gpu: bool
        """
        self._enable_gpu = enable_gpu

    @property
    def log_configs(self):
        r"""Gets the log_configs of this EdgeNodeResp.

        边缘节点日志配置，当用户未配置日志相关字段时，将默认打开日志上传到云端功能。

        :return: The log_configs of this EdgeNodeResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        r"""Sets the log_configs of this EdgeNodeResp.

        边缘节点日志配置，当用户未配置日志相关字段时，将默认打开日志上传到云端功能。

        :param log_configs: The log_configs of this EdgeNodeResp.
        :type log_configs: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        """
        self._log_configs = log_configs

    @property
    def device_infos(self):
        r"""Gets the device_infos of this EdgeNodeResp.

        关联设备信息

        :return: The device_infos of this EdgeNodeResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.DeviceInfos`]
        """
        return self._device_infos

    @device_infos.setter
    def device_infos(self, device_infos):
        r"""Sets the device_infos of this EdgeNodeResp.

        关联设备信息

        :param device_infos: The device_infos of this EdgeNodeResp.
        :type device_infos: list[:class:`huaweicloudsdkief.v1.DeviceInfos`]
        """
        self._device_infos = device_infos

    @property
    def edged_version(self):
        r"""Gets the edged_version of this EdgeNodeResp.

        edged版本

        :return: The edged_version of this EdgeNodeResp.
        :rtype: str
        """
        return self._edged_version

    @edged_version.setter
    def edged_version(self, edged_version):
        r"""Sets the edged_version of this EdgeNodeResp.

        edged版本

        :param edged_version: The edged_version of this EdgeNodeResp.
        :type edged_version: str
        """
        self._edged_version = edged_version

    @property
    def gpu_num(self):
        r"""Gets the gpu_num of this EdgeNodeResp.

        gpu个数

        :return: The gpu_num of this EdgeNodeResp.
        :rtype: int
        """
        return self._gpu_num

    @gpu_num.setter
    def gpu_num(self, gpu_num):
        r"""Sets the gpu_num of this EdgeNodeResp.

        gpu个数

        :param gpu_num: The gpu_num of this EdgeNodeResp.
        :type gpu_num: int
        """
        self._gpu_num = gpu_num

    @property
    def host_ips(self):
        r"""Gets the host_ips of this EdgeNodeResp.

        主机IP，默认返回eth0网卡的IP。

        :return: The host_ips of this EdgeNodeResp.
        :rtype: list[str]
        """
        return self._host_ips

    @host_ips.setter
    def host_ips(self, host_ips):
        r"""Sets the host_ips of this EdgeNodeResp.

        主机IP，默认返回eth0网卡的IP。

        :param host_ips: The host_ips of this EdgeNodeResp.
        :type host_ips: list[str]
        """
        self._host_ips = host_ips

    @property
    def relation(self):
        r"""Gets the relation of this EdgeNodeResp.

        与device绑定关系名称（通过device id查询node时有值）

        :return: The relation of this EdgeNodeResp.
        :rtype: str
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        r"""Sets the relation of this EdgeNodeResp.

        与device绑定关系名称（通过device id查询node时有值）

        :param relation: The relation of this EdgeNodeResp.
        :type relation: str
        """
        self._relation = relation

    @property
    def comment(self):
        r"""Gets the comment of this EdgeNodeResp.

        与device绑定关系描述（通过device id查询node时有值）

        :return: The comment of this EdgeNodeResp.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        r"""Sets the comment of this EdgeNodeResp.

        与device绑定关系描述（通过device id查询node时有值）

        :param comment: The comment of this EdgeNodeResp.
        :type comment: str
        """
        self._comment = comment

    @property
    def gpu_info(self):
        r"""Gets the gpu_info of this EdgeNodeResp.

        gpu型号和gpu memory大小

        :return: The gpu_info of this EdgeNodeResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.GpuInfo`]
        """
        return self._gpu_info

    @gpu_info.setter
    def gpu_info(self, gpu_info):
        r"""Sets the gpu_info of this EdgeNodeResp.

        gpu型号和gpu memory大小

        :param gpu_info: The gpu_info of this EdgeNodeResp.
        :type gpu_info: list[:class:`huaweicloudsdkief.v1.GpuInfo`]
        """
        self._gpu_info = gpu_info

    @property
    def device_num(self):
        r"""Gets the device_num of this EdgeNodeResp.

        关联设备数量

        :return: The device_num of this EdgeNodeResp.
        :rtype: int
        """
        return self._device_num

    @device_num.setter
    def device_num(self, device_num):
        r"""Sets the device_num of this EdgeNodeResp.

        关联设备数量

        :param device_num: The device_num of this EdgeNodeResp.
        :type device_num: int
        """
        self._device_num = device_num

    @property
    def enable_npu(self):
        r"""Gets the enable_npu of this EdgeNodeResp.

        边缘节点是否开启NPU，true表示开启，false表示不开启，默认为false

        :return: The enable_npu of this EdgeNodeResp.
        :rtype: bool
        """
        return self._enable_npu

    @enable_npu.setter
    def enable_npu(self, enable_npu):
        r"""Sets the enable_npu of this EdgeNodeResp.

        边缘节点是否开启NPU，true表示开启，false表示不开启，默认为false

        :param enable_npu: The enable_npu of this EdgeNodeResp.
        :type enable_npu: bool
        """
        self._enable_npu = enable_npu

    @property
    def npu_type(self):
        r"""Gets the npu_type of this EdgeNodeResp.

        NPU类型，支持D310、D310B，支持填写： - D310：D310类型 - D310B：D310B类型 - 空值：D310类型。

        :return: The npu_type of this EdgeNodeResp.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        r"""Sets the npu_type of this EdgeNodeResp.

        NPU类型，支持D310、D310B，支持填写： - D310：D310类型 - D310B：D310B类型 - 空值：D310类型。

        :param npu_type: The npu_type of this EdgeNodeResp.
        :type npu_type: str
        """
        self._npu_type = npu_type

    @property
    def nics(self):
        r"""Gets the nics of this EdgeNodeResp.

        节点网卡和对应IP地址信息

        :return: The nics of this EdgeNodeResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this EdgeNodeResp.

        节点网卡和对应IP地址信息

        :param nics: The nics of this EdgeNodeResp.
        :type nics: list[:class:`huaweicloudsdkief.v1.Nics`]
        """
        self._nics = nics

    @property
    def host_name(self):
        r"""Gets the host_name of this EdgeNodeResp.

        边缘节点主机名

        :return: The host_name of this EdgeNodeResp.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this EdgeNodeResp.

        边缘节点主机名

        :param host_name: The host_name of this EdgeNodeResp.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def ief_node_version(self):
        r"""Gets the ief_node_version of this EdgeNodeResp.

        边缘节点版本

        :return: The ief_node_version of this EdgeNodeResp.
        :rtype: str
        """
        return self._ief_node_version

    @ief_node_version.setter
    def ief_node_version(self, ief_node_version):
        r"""Sets the ief_node_version of this EdgeNodeResp.

        边缘节点版本

        :param ief_node_version: The ief_node_version of this EdgeNodeResp.
        :type ief_node_version: str
        """
        self._ief_node_version = ief_node_version

    @property
    def upgrade_flag(self):
        r"""Gets the upgrade_flag of this EdgeNodeResp.

        是否能升级的标志 - true：需要升级 - false：不需要升级

        :return: The upgrade_flag of this EdgeNodeResp.
        :rtype: bool
        """
        return self._upgrade_flag

    @upgrade_flag.setter
    def upgrade_flag(self, upgrade_flag):
        r"""Sets the upgrade_flag of this EdgeNodeResp.

        是否能升级的标志 - true：需要升级 - false：不需要升级

        :param upgrade_flag: The upgrade_flag of this EdgeNodeResp.
        :type upgrade_flag: bool
        """
        self._upgrade_flag = upgrade_flag

    @property
    def product_id(self):
        r"""Gets the product_id of this EdgeNodeResp.

        产品ID（通过产品证书方式纳管）

        :return: The product_id of this EdgeNodeResp.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this EdgeNodeResp.

        产品ID（通过产品证书方式纳管）

        :param product_id: The product_id of this EdgeNodeResp.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def group_ids(self):
        r"""Gets the group_ids of this EdgeNodeResp.

        节点组ID（一个节点属于多个节点组）

        :return: The group_ids of this EdgeNodeResp.
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        r"""Sets the group_ids of this EdgeNodeResp.

        节点组ID（一个节点属于多个节点组）

        :param group_ids: The group_ids of this EdgeNodeResp.
        :type group_ids: list[str]
        """
        self._group_ids = group_ids

    @property
    def upgrade_history(self):
        r"""Gets the upgrade_history of this EdgeNodeResp.

        节点安装或升级记录

        :return: The upgrade_history of this EdgeNodeResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.UpgradeHistory`]
        """
        return self._upgrade_history

    @upgrade_history.setter
    def upgrade_history(self, upgrade_history):
        r"""Sets the upgrade_history of this EdgeNodeResp.

        节点安装或升级记录

        :param upgrade_history: The upgrade_history of this EdgeNodeResp.
        :type upgrade_history: list[:class:`huaweicloudsdkief.v1.UpgradeHistory`]
        """
        self._upgrade_history = upgrade_history

    @property
    def attributes(self):
        r"""Gets the attributes of this EdgeNodeResp.

        边缘节点属性，关联属性个数最多为32个

        :return: The attributes of this EdgeNodeResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        r"""Sets the attributes of this EdgeNodeResp.

        边缘节点属性，关联属性个数最多为32个

        :param attributes: The attributes of this EdgeNodeResp.
        :type attributes: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._attributes = attributes

    @property
    def docker_enable(self):
        r"""Gets the docker_enable of this EdgeNodeResp.

        节点是否开启Docker

        :return: The docker_enable of this EdgeNodeResp.
        :rtype: bool
        """
        return self._docker_enable

    @docker_enable.setter
    def docker_enable(self, docker_enable):
        r"""Sets the docker_enable of this EdgeNodeResp.

        节点是否开启Docker

        :param docker_enable: The docker_enable of this EdgeNodeResp.
        :type docker_enable: bool
        """
        self._docker_enable = docker_enable

    @property
    def mqtt_mode(self):
        r"""Gets the mqtt_mode of this EdgeNodeResp.

        mqtt集成模式 - internal：edgecore内置mqtt - external：外置开源mqtt

        :return: The mqtt_mode of this EdgeNodeResp.
        :rtype: str
        """
        return self._mqtt_mode

    @mqtt_mode.setter
    def mqtt_mode(self, mqtt_mode):
        r"""Sets the mqtt_mode of this EdgeNodeResp.

        mqtt集成模式 - internal：edgecore内置mqtt - external：外置开源mqtt

        :param mqtt_mode: The mqtt_mode of this EdgeNodeResp.
        :type mqtt_mode: str
        """
        self._mqtt_mode = mqtt_mode

    @property
    def mqtt_external(self):
        r"""Gets the mqtt_external of this EdgeNodeResp.

        外置开源mqtt地址

        :return: The mqtt_external of this EdgeNodeResp.
        :rtype: str
        """
        return self._mqtt_external

    @mqtt_external.setter
    def mqtt_external(self, mqtt_external):
        r"""Sets the mqtt_external of this EdgeNodeResp.

        外置开源mqtt地址

        :param mqtt_external: The mqtt_external of this EdgeNodeResp.
        :type mqtt_external: str
        """
        self._mqtt_external = mqtt_external

    @property
    def mqtt_internal(self):
        r"""Gets the mqtt_internal of this EdgeNodeResp.

        edgecore内置的mqtt地址

        :return: The mqtt_internal of this EdgeNodeResp.
        :rtype: str
        """
        return self._mqtt_internal

    @mqtt_internal.setter
    def mqtt_internal(self, mqtt_internal):
        r"""Sets the mqtt_internal of this EdgeNodeResp.

        edgecore内置的mqtt地址

        :param mqtt_internal: The mqtt_internal of this EdgeNodeResp.
        :type mqtt_internal: str
        """
        self._mqtt_internal = mqtt_internal

    @property
    def node_type(self):
        r"""Gets the node_type of this EdgeNodeResp.

        节点类型，默认为空，非空时为小站节点

        :return: The node_type of this EdgeNodeResp.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this EdgeNodeResp.

        节点类型，默认为空，非空时为小站节点

        :param node_type: The node_type of this EdgeNodeResp.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def ntp_configs(self):
        r"""Gets the ntp_configs of this EdgeNodeResp.

        :return: The ntp_configs of this EdgeNodeResp.
        :rtype: :class:`huaweicloudsdkief.v1.NtpConfigs`
        """
        return self._ntp_configs

    @ntp_configs.setter
    def ntp_configs(self, ntp_configs):
        r"""Sets the ntp_configs of this EdgeNodeResp.

        :param ntp_configs: The ntp_configs of this EdgeNodeResp.
        :type ntp_configs: :class:`huaweicloudsdkief.v1.NtpConfigs`
        """
        self._ntp_configs = ntp_configs

    @property
    def error_reason(self):
        r"""Gets the error_reason of this EdgeNodeResp.

        节点故障原因

        :return: The error_reason of this EdgeNodeResp.
        :rtype: str
        """
        return self._error_reason

    @error_reason.setter
    def error_reason(self, error_reason):
        r"""Sets the error_reason of this EdgeNodeResp.

        节点故障原因

        :param error_reason: The error_reason of this EdgeNodeResp.
        :type error_reason: str
        """
        self._error_reason = error_reason

    @property
    def tags(self):
        r"""Gets the tags of this EdgeNodeResp.

        边缘节点标签，标签个数最多为20个

        :return: The tags of this EdgeNodeResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this EdgeNodeResp.

        边缘节点标签，标签个数最多为20个

        :param tags: The tags of this EdgeNodeResp.
        :type tags: list[:class:`huaweicloudsdkief.v1.ResourceTag`]
        """
        self._tags = tags

    @property
    def npu_num(self):
        r"""Gets the npu_num of this EdgeNodeResp.

        NPU数量

        :return: The npu_num of this EdgeNodeResp.
        :rtype: int
        """
        return self._npu_num

    @npu_num.setter
    def npu_num(self, npu_num):
        r"""Sets the npu_num of this EdgeNodeResp.

        NPU数量

        :param npu_num: The npu_num of this EdgeNodeResp.
        :type npu_num: int
        """
        self._npu_num = npu_num

    @property
    def npu_info(self):
        r"""Gets the npu_info of this EdgeNodeResp.

        NPU型号和NPU Memory大小

        :return: The npu_info of this EdgeNodeResp.
        :rtype: list[:class:`huaweicloudsdkief.v1.NpuInfo`]
        """
        return self._npu_info

    @npu_info.setter
    def npu_info(self, npu_info):
        r"""Sets the npu_info of this EdgeNodeResp.

        NPU型号和NPU Memory大小

        :param npu_info: The npu_info of this EdgeNodeResp.
        :type npu_info: list[:class:`huaweicloudsdkief.v1.NpuInfo`]
        """
        self._npu_info = npu_info

    @property
    def container_runtime_version(self):
        r"""Gets the container_runtime_version of this EdgeNodeResp.

        容器运行时版本

        :return: The container_runtime_version of this EdgeNodeResp.
        :rtype: str
        """
        return self._container_runtime_version

    @container_runtime_version.setter
    def container_runtime_version(self, container_runtime_version):
        r"""Sets the container_runtime_version of this EdgeNodeResp.

        容器运行时版本

        :param container_runtime_version: The container_runtime_version of this EdgeNodeResp.
        :type container_runtime_version: str
        """
        self._container_runtime_version = container_runtime_version

    @property
    def identifier(self):
        r"""Gets the identifier of this EdgeNodeResp.

        边缘节点使用token注册时的凭证

        :return: The identifier of this EdgeNodeResp.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        r"""Sets the identifier of this EdgeNodeResp.

        边缘节点使用token注册时的凭证

        :param identifier: The identifier of this EdgeNodeResp.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def purchase_id(self):
        r"""Gets the purchase_id of this EdgeNodeResp.

        IEC/IES节点id

        :return: The purchase_id of this EdgeNodeResp.
        :rtype: str
        """
        return self._purchase_id

    @purchase_id.setter
    def purchase_id(self, purchase_id):
        r"""Sets the purchase_id of this EdgeNodeResp.

        IEC/IES节点id

        :param purchase_id: The purchase_id of this EdgeNodeResp.
        :type purchase_id: str
        """
        self._purchase_id = purchase_id

    @property
    def state_details(self):
        r"""Gets the state_details of this EdgeNodeResp.

        :return: The state_details of this EdgeNodeResp.
        :rtype: :class:`huaweicloudsdkief.v1.StateDetails`
        """
        return self._state_details

    @state_details.setter
    def state_details(self, state_details):
        r"""Sets the state_details of this EdgeNodeResp.

        :param state_details: The state_details of this EdgeNodeResp.
        :type state_details: :class:`huaweicloudsdkief.v1.StateDetails`
        """
        self._state_details = state_details

    @property
    def cert_remaining_valid_time(self):
        r"""Gets the cert_remaining_valid_time of this EdgeNodeResp.

        证书有效期持续时间

        :return: The cert_remaining_valid_time of this EdgeNodeResp.
        :rtype: int
        """
        return self._cert_remaining_valid_time

    @cert_remaining_valid_time.setter
    def cert_remaining_valid_time(self, cert_remaining_valid_time):
        r"""Sets the cert_remaining_valid_time of this EdgeNodeResp.

        证书有效期持续时间

        :param cert_remaining_valid_time: The cert_remaining_valid_time of this EdgeNodeResp.
        :type cert_remaining_valid_time: int
        """
        self._cert_remaining_valid_time = cert_remaining_valid_time

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
        if not isinstance(other, EdgeNodeResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
