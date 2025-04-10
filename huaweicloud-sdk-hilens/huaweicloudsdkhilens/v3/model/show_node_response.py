# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodeResponse(SdkResponse):

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
        'arch': 'str',
        'memory': 'int',
        'name': 'str',
        'description': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'user_name': 'str',
        'cluster_id': 'str',
        'cluster_node_state': 'str',
        'cluster_node_type': 'str',
        'firmware_name': 'str',
        'firmware_version': 'str',
        'upgrade_firmware_version': 'str',
        'firmware_status': 'str',
        'firmware_upgrade_record': 'list[FirmwareUpdateRecord]',
        'state': 'str',
        'type': 'str',
        'active_status': 'str',
        'cpu': 'int',
        'gpu_num': 'int',
        'npu_num': 'int',
        'npu_type': 'str',
        'os_name': 'str',
        'os_type': 'str',
        'os_version': 'str',
        'enable_container': 'bool',
        'enable_gpu': 'bool',
        'enable_npu': 'bool',
        'host_ips': 'list[str]',
        'tags': 'NodeDetailResponseTags',
        'npu_info': 'object',
        'active_content': 'list[str]',
        'log_configs': 'list[LogConfig]',
        'event_validity_period': 'int'
    }

    attribute_map = {
        'id': 'id',
        'arch': 'arch',
        'memory': 'memory',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'user_name': 'user_name',
        'cluster_id': 'cluster_id',
        'cluster_node_state': 'cluster_node_state',
        'cluster_node_type': 'cluster_node_type',
        'firmware_name': 'firmware_name',
        'firmware_version': 'firmware_version',
        'upgrade_firmware_version': 'upgrade_firmware_version',
        'firmware_status': 'firmware_status',
        'firmware_upgrade_record': 'firmware_upgrade_record',
        'state': 'state',
        'type': 'type',
        'active_status': 'active_status',
        'cpu': 'cpu',
        'gpu_num': 'gpu_num',
        'npu_num': 'npu_num',
        'npu_type': 'npu_type',
        'os_name': 'os_name',
        'os_type': 'os_type',
        'os_version': 'os_version',
        'enable_container': 'enable_container',
        'enable_gpu': 'enable_gpu',
        'enable_npu': 'enable_npu',
        'host_ips': 'host_ips',
        'tags': 'tags',
        'npu_info': 'npu_info',
        'active_content': 'active_content',
        'log_configs': 'log_configs',
        'event_validity_period': 'event_validity_period'
    }

    def __init__(self, id=None, arch=None, memory=None, name=None, description=None, created_at=None, updated_at=None, user_name=None, cluster_id=None, cluster_node_state=None, cluster_node_type=None, firmware_name=None, firmware_version=None, upgrade_firmware_version=None, firmware_status=None, firmware_upgrade_record=None, state=None, type=None, active_status=None, cpu=None, gpu_num=None, npu_num=None, npu_type=None, os_name=None, os_type=None, os_version=None, enable_container=None, enable_gpu=None, enable_npu=None, host_ips=None, tags=None, npu_info=None, active_content=None, log_configs=None, event_validity_period=None):
        r"""ShowNodeResponse

        The model defined in huaweicloud sdk

        :param id: 设备ID
        :type id: str
        :param arch: 设备架构
        :type arch: str
        :param memory: 设备内存
        :type memory: int
        :param name: 设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param description: 设备描述，最大长度255，不允许^, ~, ＃, $, %, &amp;, *, &lt;, &gt;, (, ), [, ], {, }, &#39;, \&quot;, \\
        :type description: str
        :param created_at: 产生时间，如2021-10-15 14:45:22 GMT+08:00
        :type created_at: str
        :param updated_at: 更新时间，如2021-10-15 14:45:22 GMT+08:00
        :type updated_at: str
        :param user_name: IAM用户名
        :type user_name: str
        :param cluster_id: 当该设备处于集群时，显示设备所属的集群ID
        :type cluster_id: str
        :param cluster_node_state: 设备所处集群状态，集群创建（cluster_create）、集群删除（cluster_delete）、添加集群工作节点设备（cluster_add_nodes）、删除集群工作节点设备（cluster_delete_node）、集群节点设备状态更新（cluster_node_state_update）
        :type cluster_node_state: str
        :param cluster_node_type: 当该设备处于集群时，显示所属的集群设备类型。 - cluster_controller 控制设备 - cluster_worker 工作设备
        :type cluster_node_type: str
        :param firmware_name: 固件名称。可包含大小写字母、数字、下划线、中划线,长度不超过60字符。必须以字母开头,字母或数字结尾
        :type firmware_name: str
        :param firmware_version: 固件版本。支持X.Y.Z格式。每一个子版本号不超过三位且为非负整数,禁止在数字前补0
        :type firmware_version: str
        :param upgrade_firmware_version: 固件正在升级的版本
        :type upgrade_firmware_version: str
        :param firmware_status: 固件升级状态，1、2、3分别代表升级中，升级失败，升级成
        :type firmware_status: str
        :param firmware_upgrade_record: 
        :type firmware_upgrade_record: list[:class:`huaweicloudsdkhilens.v3.FirmwareUpdateRecord`]
        :param state: 设备状态：UNCONNECTED(未注册)、RUNNING(运行中)、FAIL(故障)、STOPPED(停用)、UPGRADING(升级中)、FREEZE(冻结)
        :type state: str
        :param type: 设备类型
        :type type: str
        :param active_status: 设备激活状态，未激活（INACTIVE）和已激活（ACTIVATED）
        :type active_status: str
        :param cpu: 设备CPU个数
        :type cpu: int
        :param gpu_num: 设备GPU个数
        :type gpu_num: int
        :param npu_num: 设备NPU个数
        :type npu_num: int
        :param npu_type: 设备NPU类型
        :type npu_type: str
        :param os_name: 设备操作系统名称
        :type os_name: str
        :param os_type: 设备操作系统类型
        :type os_type: str
        :param os_version: 设备操作系统版本
        :type os_version: str
        :param enable_container: 是否启用容器
        :type enable_container: bool
        :param enable_gpu: 是否启用GPU
        :type enable_gpu: bool
        :param enable_npu: 是否启用NPU
        :type enable_npu: bool
        :param host_ips: 主机IP列表
        :type host_ips: list[str]
        :param tags: 
        :type tags: :class:`huaweicloudsdkhilens.v3.NodeDetailResponseTags`
        :param npu_info: NPU信息
        :type npu_info: object
        :param active_content: 激活订单号列表
        :type active_content: list[str]
        :param log_configs: 设备日志配置
        :type log_configs: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        :param event_validity_period: 事件有效时间(单位：分钟)
        :type event_validity_period: int
        """
        
        super(ShowNodeResponse, self).__init__()

        self._id = None
        self._arch = None
        self._memory = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._user_name = None
        self._cluster_id = None
        self._cluster_node_state = None
        self._cluster_node_type = None
        self._firmware_name = None
        self._firmware_version = None
        self._upgrade_firmware_version = None
        self._firmware_status = None
        self._firmware_upgrade_record = None
        self._state = None
        self._type = None
        self._active_status = None
        self._cpu = None
        self._gpu_num = None
        self._npu_num = None
        self._npu_type = None
        self._os_name = None
        self._os_type = None
        self._os_version = None
        self._enable_container = None
        self._enable_gpu = None
        self._enable_npu = None
        self._host_ips = None
        self._tags = None
        self._npu_info = None
        self._active_content = None
        self._log_configs = None
        self._event_validity_period = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if arch is not None:
            self.arch = arch
        if memory is not None:
            self.memory = memory
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if user_name is not None:
            self.user_name = user_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_node_state is not None:
            self.cluster_node_state = cluster_node_state
        if cluster_node_type is not None:
            self.cluster_node_type = cluster_node_type
        if firmware_name is not None:
            self.firmware_name = firmware_name
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if upgrade_firmware_version is not None:
            self.upgrade_firmware_version = upgrade_firmware_version
        if firmware_status is not None:
            self.firmware_status = firmware_status
        if firmware_upgrade_record is not None:
            self.firmware_upgrade_record = firmware_upgrade_record
        if state is not None:
            self.state = state
        if type is not None:
            self.type = type
        if active_status is not None:
            self.active_status = active_status
        if cpu is not None:
            self.cpu = cpu
        if gpu_num is not None:
            self.gpu_num = gpu_num
        if npu_num is not None:
            self.npu_num = npu_num
        if npu_type is not None:
            self.npu_type = npu_type
        if os_name is not None:
            self.os_name = os_name
        if os_type is not None:
            self.os_type = os_type
        if os_version is not None:
            self.os_version = os_version
        if enable_container is not None:
            self.enable_container = enable_container
        if enable_gpu is not None:
            self.enable_gpu = enable_gpu
        if enable_npu is not None:
            self.enable_npu = enable_npu
        if host_ips is not None:
            self.host_ips = host_ips
        if tags is not None:
            self.tags = tags
        if npu_info is not None:
            self.npu_info = npu_info
        if active_content is not None:
            self.active_content = active_content
        if log_configs is not None:
            self.log_configs = log_configs
        if event_validity_period is not None:
            self.event_validity_period = event_validity_period

    @property
    def id(self):
        r"""Gets the id of this ShowNodeResponse.

        设备ID

        :return: The id of this ShowNodeResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowNodeResponse.

        设备ID

        :param id: The id of this ShowNodeResponse.
        :type id: str
        """
        self._id = id

    @property
    def arch(self):
        r"""Gets the arch of this ShowNodeResponse.

        设备架构

        :return: The arch of this ShowNodeResponse.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this ShowNodeResponse.

        设备架构

        :param arch: The arch of this ShowNodeResponse.
        :type arch: str
        """
        self._arch = arch

    @property
    def memory(self):
        r"""Gets the memory of this ShowNodeResponse.

        设备内存

        :return: The memory of this ShowNodeResponse.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        r"""Sets the memory of this ShowNodeResponse.

        设备内存

        :param memory: The memory of this ShowNodeResponse.
        :type memory: int
        """
        self._memory = memory

    @property
    def name(self):
        r"""Gets the name of this ShowNodeResponse.

        设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this ShowNodeResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowNodeResponse.

        设备名称，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this ShowNodeResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowNodeResponse.

        设备描述，最大长度255，不允许^, ~, ＃, $, %, &, *, <, >, (, ), [, ], {, }, ', \", \\

        :return: The description of this ShowNodeResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowNodeResponse.

        设备描述，最大长度255，不允许^, ~, ＃, $, %, &, *, <, >, (, ), [, ], {, }, ', \", \\

        :param description: The description of this ShowNodeResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowNodeResponse.

        产生时间，如2021-10-15 14:45:22 GMT+08:00

        :return: The created_at of this ShowNodeResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowNodeResponse.

        产生时间，如2021-10-15 14:45:22 GMT+08:00

        :param created_at: The created_at of this ShowNodeResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowNodeResponse.

        更新时间，如2021-10-15 14:45:22 GMT+08:00

        :return: The updated_at of this ShowNodeResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowNodeResponse.

        更新时间，如2021-10-15 14:45:22 GMT+08:00

        :param updated_at: The updated_at of this ShowNodeResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowNodeResponse.

        IAM用户名

        :return: The user_name of this ShowNodeResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowNodeResponse.

        IAM用户名

        :param user_name: The user_name of this ShowNodeResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowNodeResponse.

        当该设备处于集群时，显示设备所属的集群ID

        :return: The cluster_id of this ShowNodeResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowNodeResponse.

        当该设备处于集群时，显示设备所属的集群ID

        :param cluster_id: The cluster_id of this ShowNodeResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_node_state(self):
        r"""Gets the cluster_node_state of this ShowNodeResponse.

        设备所处集群状态，集群创建（cluster_create）、集群删除（cluster_delete）、添加集群工作节点设备（cluster_add_nodes）、删除集群工作节点设备（cluster_delete_node）、集群节点设备状态更新（cluster_node_state_update）

        :return: The cluster_node_state of this ShowNodeResponse.
        :rtype: str
        """
        return self._cluster_node_state

    @cluster_node_state.setter
    def cluster_node_state(self, cluster_node_state):
        r"""Sets the cluster_node_state of this ShowNodeResponse.

        设备所处集群状态，集群创建（cluster_create）、集群删除（cluster_delete）、添加集群工作节点设备（cluster_add_nodes）、删除集群工作节点设备（cluster_delete_node）、集群节点设备状态更新（cluster_node_state_update）

        :param cluster_node_state: The cluster_node_state of this ShowNodeResponse.
        :type cluster_node_state: str
        """
        self._cluster_node_state = cluster_node_state

    @property
    def cluster_node_type(self):
        r"""Gets the cluster_node_type of this ShowNodeResponse.

        当该设备处于集群时，显示所属的集群设备类型。 - cluster_controller 控制设备 - cluster_worker 工作设备

        :return: The cluster_node_type of this ShowNodeResponse.
        :rtype: str
        """
        return self._cluster_node_type

    @cluster_node_type.setter
    def cluster_node_type(self, cluster_node_type):
        r"""Sets the cluster_node_type of this ShowNodeResponse.

        当该设备处于集群时，显示所属的集群设备类型。 - cluster_controller 控制设备 - cluster_worker 工作设备

        :param cluster_node_type: The cluster_node_type of this ShowNodeResponse.
        :type cluster_node_type: str
        """
        self._cluster_node_type = cluster_node_type

    @property
    def firmware_name(self):
        r"""Gets the firmware_name of this ShowNodeResponse.

        固件名称。可包含大小写字母、数字、下划线、中划线,长度不超过60字符。必须以字母开头,字母或数字结尾

        :return: The firmware_name of this ShowNodeResponse.
        :rtype: str
        """
        return self._firmware_name

    @firmware_name.setter
    def firmware_name(self, firmware_name):
        r"""Sets the firmware_name of this ShowNodeResponse.

        固件名称。可包含大小写字母、数字、下划线、中划线,长度不超过60字符。必须以字母开头,字母或数字结尾

        :param firmware_name: The firmware_name of this ShowNodeResponse.
        :type firmware_name: str
        """
        self._firmware_name = firmware_name

    @property
    def firmware_version(self):
        r"""Gets the firmware_version of this ShowNodeResponse.

        固件版本。支持X.Y.Z格式。每一个子版本号不超过三位且为非负整数,禁止在数字前补0

        :return: The firmware_version of this ShowNodeResponse.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        r"""Sets the firmware_version of this ShowNodeResponse.

        固件版本。支持X.Y.Z格式。每一个子版本号不超过三位且为非负整数,禁止在数字前补0

        :param firmware_version: The firmware_version of this ShowNodeResponse.
        :type firmware_version: str
        """
        self._firmware_version = firmware_version

    @property
    def upgrade_firmware_version(self):
        r"""Gets the upgrade_firmware_version of this ShowNodeResponse.

        固件正在升级的版本

        :return: The upgrade_firmware_version of this ShowNodeResponse.
        :rtype: str
        """
        return self._upgrade_firmware_version

    @upgrade_firmware_version.setter
    def upgrade_firmware_version(self, upgrade_firmware_version):
        r"""Sets the upgrade_firmware_version of this ShowNodeResponse.

        固件正在升级的版本

        :param upgrade_firmware_version: The upgrade_firmware_version of this ShowNodeResponse.
        :type upgrade_firmware_version: str
        """
        self._upgrade_firmware_version = upgrade_firmware_version

    @property
    def firmware_status(self):
        r"""Gets the firmware_status of this ShowNodeResponse.

        固件升级状态，1、2、3分别代表升级中，升级失败，升级成

        :return: The firmware_status of this ShowNodeResponse.
        :rtype: str
        """
        return self._firmware_status

    @firmware_status.setter
    def firmware_status(self, firmware_status):
        r"""Sets the firmware_status of this ShowNodeResponse.

        固件升级状态，1、2、3分别代表升级中，升级失败，升级成

        :param firmware_status: The firmware_status of this ShowNodeResponse.
        :type firmware_status: str
        """
        self._firmware_status = firmware_status

    @property
    def firmware_upgrade_record(self):
        r"""Gets the firmware_upgrade_record of this ShowNodeResponse.

        :return: The firmware_upgrade_record of this ShowNodeResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.FirmwareUpdateRecord`]
        """
        return self._firmware_upgrade_record

    @firmware_upgrade_record.setter
    def firmware_upgrade_record(self, firmware_upgrade_record):
        r"""Sets the firmware_upgrade_record of this ShowNodeResponse.

        :param firmware_upgrade_record: The firmware_upgrade_record of this ShowNodeResponse.
        :type firmware_upgrade_record: list[:class:`huaweicloudsdkhilens.v3.FirmwareUpdateRecord`]
        """
        self._firmware_upgrade_record = firmware_upgrade_record

    @property
    def state(self):
        r"""Gets the state of this ShowNodeResponse.

        设备状态：UNCONNECTED(未注册)、RUNNING(运行中)、FAIL(故障)、STOPPED(停用)、UPGRADING(升级中)、FREEZE(冻结)

        :return: The state of this ShowNodeResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ShowNodeResponse.

        设备状态：UNCONNECTED(未注册)、RUNNING(运行中)、FAIL(故障)、STOPPED(停用)、UPGRADING(升级中)、FREEZE(冻结)

        :param state: The state of this ShowNodeResponse.
        :type state: str
        """
        self._state = state

    @property
    def type(self):
        r"""Gets the type of this ShowNodeResponse.

        设备类型

        :return: The type of this ShowNodeResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowNodeResponse.

        设备类型

        :param type: The type of this ShowNodeResponse.
        :type type: str
        """
        self._type = type

    @property
    def active_status(self):
        r"""Gets the active_status of this ShowNodeResponse.

        设备激活状态，未激活（INACTIVE）和已激活（ACTIVATED）

        :return: The active_status of this ShowNodeResponse.
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        r"""Sets the active_status of this ShowNodeResponse.

        设备激活状态，未激活（INACTIVE）和已激活（ACTIVATED）

        :param active_status: The active_status of this ShowNodeResponse.
        :type active_status: str
        """
        self._active_status = active_status

    @property
    def cpu(self):
        r"""Gets the cpu of this ShowNodeResponse.

        设备CPU个数

        :return: The cpu of this ShowNodeResponse.
        :rtype: int
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ShowNodeResponse.

        设备CPU个数

        :param cpu: The cpu of this ShowNodeResponse.
        :type cpu: int
        """
        self._cpu = cpu

    @property
    def gpu_num(self):
        r"""Gets the gpu_num of this ShowNodeResponse.

        设备GPU个数

        :return: The gpu_num of this ShowNodeResponse.
        :rtype: int
        """
        return self._gpu_num

    @gpu_num.setter
    def gpu_num(self, gpu_num):
        r"""Sets the gpu_num of this ShowNodeResponse.

        设备GPU个数

        :param gpu_num: The gpu_num of this ShowNodeResponse.
        :type gpu_num: int
        """
        self._gpu_num = gpu_num

    @property
    def npu_num(self):
        r"""Gets the npu_num of this ShowNodeResponse.

        设备NPU个数

        :return: The npu_num of this ShowNodeResponse.
        :rtype: int
        """
        return self._npu_num

    @npu_num.setter
    def npu_num(self, npu_num):
        r"""Sets the npu_num of this ShowNodeResponse.

        设备NPU个数

        :param npu_num: The npu_num of this ShowNodeResponse.
        :type npu_num: int
        """
        self._npu_num = npu_num

    @property
    def npu_type(self):
        r"""Gets the npu_type of this ShowNodeResponse.

        设备NPU类型

        :return: The npu_type of this ShowNodeResponse.
        :rtype: str
        """
        return self._npu_type

    @npu_type.setter
    def npu_type(self, npu_type):
        r"""Sets the npu_type of this ShowNodeResponse.

        设备NPU类型

        :param npu_type: The npu_type of this ShowNodeResponse.
        :type npu_type: str
        """
        self._npu_type = npu_type

    @property
    def os_name(self):
        r"""Gets the os_name of this ShowNodeResponse.

        设备操作系统名称

        :return: The os_name of this ShowNodeResponse.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        r"""Sets the os_name of this ShowNodeResponse.

        设备操作系统名称

        :param os_name: The os_name of this ShowNodeResponse.
        :type os_name: str
        """
        self._os_name = os_name

    @property
    def os_type(self):
        r"""Gets the os_type of this ShowNodeResponse.

        设备操作系统类型

        :return: The os_type of this ShowNodeResponse.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this ShowNodeResponse.

        设备操作系统类型

        :param os_type: The os_type of this ShowNodeResponse.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def os_version(self):
        r"""Gets the os_version of this ShowNodeResponse.

        设备操作系统版本

        :return: The os_version of this ShowNodeResponse.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        r"""Sets the os_version of this ShowNodeResponse.

        设备操作系统版本

        :param os_version: The os_version of this ShowNodeResponse.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def enable_container(self):
        r"""Gets the enable_container of this ShowNodeResponse.

        是否启用容器

        :return: The enable_container of this ShowNodeResponse.
        :rtype: bool
        """
        return self._enable_container

    @enable_container.setter
    def enable_container(self, enable_container):
        r"""Sets the enable_container of this ShowNodeResponse.

        是否启用容器

        :param enable_container: The enable_container of this ShowNodeResponse.
        :type enable_container: bool
        """
        self._enable_container = enable_container

    @property
    def enable_gpu(self):
        r"""Gets the enable_gpu of this ShowNodeResponse.

        是否启用GPU

        :return: The enable_gpu of this ShowNodeResponse.
        :rtype: bool
        """
        return self._enable_gpu

    @enable_gpu.setter
    def enable_gpu(self, enable_gpu):
        r"""Sets the enable_gpu of this ShowNodeResponse.

        是否启用GPU

        :param enable_gpu: The enable_gpu of this ShowNodeResponse.
        :type enable_gpu: bool
        """
        self._enable_gpu = enable_gpu

    @property
    def enable_npu(self):
        r"""Gets the enable_npu of this ShowNodeResponse.

        是否启用NPU

        :return: The enable_npu of this ShowNodeResponse.
        :rtype: bool
        """
        return self._enable_npu

    @enable_npu.setter
    def enable_npu(self, enable_npu):
        r"""Sets the enable_npu of this ShowNodeResponse.

        是否启用NPU

        :param enable_npu: The enable_npu of this ShowNodeResponse.
        :type enable_npu: bool
        """
        self._enable_npu = enable_npu

    @property
    def host_ips(self):
        r"""Gets the host_ips of this ShowNodeResponse.

        主机IP列表

        :return: The host_ips of this ShowNodeResponse.
        :rtype: list[str]
        """
        return self._host_ips

    @host_ips.setter
    def host_ips(self, host_ips):
        r"""Sets the host_ips of this ShowNodeResponse.

        主机IP列表

        :param host_ips: The host_ips of this ShowNodeResponse.
        :type host_ips: list[str]
        """
        self._host_ips = host_ips

    @property
    def tags(self):
        r"""Gets the tags of this ShowNodeResponse.

        :return: The tags of this ShowNodeResponse.
        :rtype: :class:`huaweicloudsdkhilens.v3.NodeDetailResponseTags`
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowNodeResponse.

        :param tags: The tags of this ShowNodeResponse.
        :type tags: :class:`huaweicloudsdkhilens.v3.NodeDetailResponseTags`
        """
        self._tags = tags

    @property
    def npu_info(self):
        r"""Gets the npu_info of this ShowNodeResponse.

        NPU信息

        :return: The npu_info of this ShowNodeResponse.
        :rtype: object
        """
        return self._npu_info

    @npu_info.setter
    def npu_info(self, npu_info):
        r"""Sets the npu_info of this ShowNodeResponse.

        NPU信息

        :param npu_info: The npu_info of this ShowNodeResponse.
        :type npu_info: object
        """
        self._npu_info = npu_info

    @property
    def active_content(self):
        r"""Gets the active_content of this ShowNodeResponse.

        激活订单号列表

        :return: The active_content of this ShowNodeResponse.
        :rtype: list[str]
        """
        return self._active_content

    @active_content.setter
    def active_content(self, active_content):
        r"""Sets the active_content of this ShowNodeResponse.

        激活订单号列表

        :param active_content: The active_content of this ShowNodeResponse.
        :type active_content: list[str]
        """
        self._active_content = active_content

    @property
    def log_configs(self):
        r"""Gets the log_configs of this ShowNodeResponse.

        设备日志配置

        :return: The log_configs of this ShowNodeResponse.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        r"""Sets the log_configs of this ShowNodeResponse.

        设备日志配置

        :param log_configs: The log_configs of this ShowNodeResponse.
        :type log_configs: list[:class:`huaweicloudsdkhilens.v3.LogConfig`]
        """
        self._log_configs = log_configs

    @property
    def event_validity_period(self):
        r"""Gets the event_validity_period of this ShowNodeResponse.

        事件有效时间(单位：分钟)

        :return: The event_validity_period of this ShowNodeResponse.
        :rtype: int
        """
        return self._event_validity_period

    @event_validity_period.setter
    def event_validity_period(self, event_validity_period):
        r"""Sets the event_validity_period of this ShowNodeResponse.

        事件有效时间(单位：分钟)

        :param event_validity_period: The event_validity_period of this ShowNodeResponse.
        :type event_validity_period: int
        """
        self._event_validity_period = event_validity_period

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
        if not isinstance(other, ShowNodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
