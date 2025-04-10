# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerDetails:

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
        'user_id': 'str',
        'name': 'str',
        'created': 'str',
        'updated': 'str',
        'tenant_id': 'str',
        'host_id': 'str',
        'addresses': 'dict(str, list[AddressInfo])',
        'key_name': 'str',
        'image': 'ImageInfo',
        'flavor': 'FlavorInfos',
        'security_groups': 'list[SecurityGroupsList]',
        'access_i_pv4': 'str',
        'access_i_pv6': 'str',
        'status': 'str',
        'progress': 'int',
        'config_drive': 'str',
        'metadata': 'MetadataList',
        'os_ext_st_stask_state': 'str',
        'os_ext_st_svm_state': 'str',
        'os_ext_srv_att_rhost': 'str',
        'os_ext_srv_att_rinstance_name': 'str',
        'os_ext_st_spower_state': 'int',
        'os_ext_srv_att_rhypervisor_hostname': 'str',
        'os_ext_a_zavailability_zone': 'str',
        'os_dc_fdisk_config': 'str',
        'fault': 'Fault',
        'os_srv_us_glaunched_at': 'str',
        'os_srv_us_gterminated_at': 'str',
        'os_extended_volumesvolumes_attached': 'list[OsExtendedVolumesInfo]',
        'description': 'str',
        'host_status': 'str',
        'os_ext_srv_att_rhostname': 'str',
        'os_ext_srv_att_rreservation_id': 'str',
        'os_ext_srv_att_rlaunch_index': 'int',
        'os_ext_srv_att_rkernel_id': 'str',
        'os_ext_srv_att_rramdisk_id': 'str',
        'os_ext_srv_att_rroot_device_name': 'str',
        'os_ext_srv_att_ruser_data': 'str',
        'locked': 'bool',
        'tags': 'list[str]',
        'osscheduler_hints': 'SchedulerHints',
        'enterprise_project_id': 'str',
        'sys_tags': 'list[SystemTags]'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'name': 'name',
        'created': 'created',
        'updated': 'updated',
        'tenant_id': 'tenant_id',
        'host_id': 'hostId',
        'addresses': 'addresses',
        'key_name': 'key_name',
        'image': 'image',
        'flavor': 'flavor',
        'security_groups': 'security_groups',
        'access_i_pv4': 'accessIPv4',
        'access_i_pv6': 'accessIPv6',
        'status': 'status',
        'progress': 'progress',
        'config_drive': 'config_drive',
        'metadata': 'metadata',
        'os_ext_st_stask_state': 'OS-EXT-STS:task_state',
        'os_ext_st_svm_state': 'OS-EXT-STS:vm_state',
        'os_ext_srv_att_rhost': 'OS-EXT-SRV-ATTR:host',
        'os_ext_srv_att_rinstance_name': 'OS-EXT-SRV-ATTR:instance_name',
        'os_ext_st_spower_state': 'OS-EXT-STS:power_state',
        'os_ext_srv_att_rhypervisor_hostname': 'OS-EXT-SRV-ATTR:hypervisor_hostname',
        'os_ext_a_zavailability_zone': 'OS-EXT-AZ:availability_zone',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'fault': 'fault',
        'os_srv_us_glaunched_at': 'OS-SRV-USG:launched_at',
        'os_srv_us_gterminated_at': 'OS-SRV-USG:terminated_at',
        'os_extended_volumesvolumes_attached': 'os-extended-volumes:volumes_attached',
        'description': 'description',
        'host_status': 'host_status',
        'os_ext_srv_att_rhostname': 'OS-EXT-SRV-ATTR:hostname',
        'os_ext_srv_att_rreservation_id': 'OS-EXT-SRV-ATTR:reservation_id',
        'os_ext_srv_att_rlaunch_index': 'OS-EXT-SRV-ATTR:launch_index',
        'os_ext_srv_att_rkernel_id': 'OS-EXT-SRV-ATTR:kernel_id',
        'os_ext_srv_att_rramdisk_id': 'OS-EXT-SRV-ATTR:ramdisk_id',
        'os_ext_srv_att_rroot_device_name': 'OS-EXT-SRV-ATTR:root_device_name',
        'os_ext_srv_att_ruser_data': 'OS-EXT-SRV-ATTR:user_data',
        'locked': 'locked',
        'tags': 'tags',
        'osscheduler_hints': 'os:scheduler_hints',
        'enterprise_project_id': 'enterprise_project_id',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, id=None, user_id=None, name=None, created=None, updated=None, tenant_id=None, host_id=None, addresses=None, key_name=None, image=None, flavor=None, security_groups=None, access_i_pv4=None, access_i_pv6=None, status=None, progress=None, config_drive=None, metadata=None, os_ext_st_stask_state=None, os_ext_st_svm_state=None, os_ext_srv_att_rhost=None, os_ext_srv_att_rinstance_name=None, os_ext_st_spower_state=None, os_ext_srv_att_rhypervisor_hostname=None, os_ext_a_zavailability_zone=None, os_dc_fdisk_config=None, fault=None, os_srv_us_glaunched_at=None, os_srv_us_gterminated_at=None, os_extended_volumesvolumes_attached=None, description=None, host_status=None, os_ext_srv_att_rhostname=None, os_ext_srv_att_rreservation_id=None, os_ext_srv_att_rlaunch_index=None, os_ext_srv_att_rkernel_id=None, os_ext_srv_att_rramdisk_id=None, os_ext_srv_att_rroot_device_name=None, os_ext_srv_att_ruser_data=None, locked=None, tags=None, osscheduler_hints=None, enterprise_project_id=None, sys_tags=None):
        r"""ServerDetails

        The model defined in huaweicloud sdk

        :param id: 裸金属服务器ID，格式为UUID
        :type id: str
        :param user_id: 创建裸金属服务器的用户ID，格式为UUID。
        :type user_id: str
        :param name: 裸金属服务器名称
        :type name: str
        :param created: 裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z
        :type created: str
        :param updated: 裸金属服务器更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z
        :type updated: str
        :param tenant_id: 裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。
        :type tenant_id: str
        :param host_id: 裸金属服务器对应的主机ID
        :type host_id: str
        :param addresses: 裸金属服务器的网络属性。详情请参见表3 addresses数据结构说明。
        :type addresses: dict(str, list[AddressInfo])
        :param key_name: 裸金属服务器使用的密钥对名称
        :type key_name: str
        :param image: 
        :type image: :class:`huaweicloudsdkbms.v1.ImageInfo`
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkbms.v1.FlavorInfos`
        :param security_groups: 裸金属服务器所属安全组。详情请参见表7 security_groups数据结构说明。
        :type security_groups: list[:class:`huaweicloudsdkbms.v1.SecurityGroupsList`]
        :param access_i_pv4: 预留属性
        :type access_i_pv4: str
        :param access_i_pv6: 预留属性
        :type access_i_pv6: str
        :param status: 裸金属服务器当前状态信息。  取值范围：  ACTIVE：运行中/正在关机/删除中 BUILD：创建中 ERROR：故障 HARD_REBOOT：强制重启中 REBOOT：重启中 DELETED：实例已被正常删除 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结
        :type status: str
        :param progress: 预留属性
        :type progress: int
        :param config_drive: 是否为裸金属服务器配置config drive分区。取值为：True或空字符串
        :type config_drive: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkbms.v1.MetadataList`
        :param os_ext_st_stask_state: 扩展属性，裸金属服务器当前的任务状态。例如：rebooting：重启中reboot_started：普通重启reboot_started_hard：强制重启powering-off：关机中powering-on：开机中rebuilding：重建中scheduling：调度中deleting：删除中
        :type os_ext_st_stask_state: str
        :param os_ext_st_svm_state: 扩展属性，裸金属服务器的稳定状态。例如：active：运行中shutoff：关机reboot：重启
        :type os_ext_st_svm_state: str
        :param os_ext_srv_att_rhost: 扩展属性，裸金属服务器宿主名称
        :type os_ext_srv_att_rhost: str
        :param os_ext_srv_att_rinstance_name: 扩展属性，裸金属服务器实例ID
        :type os_ext_srv_att_rinstance_name: str
        :param os_ext_st_spower_state: 扩展属性，裸金属服务器电源状态。例如：0表示“NO STATE”1表示“RUNNING”4表示“SHUTDOWN”
        :type os_ext_st_spower_state: int
        :param os_ext_srv_att_rhypervisor_hostname: 扩展属性，裸金属服务器所在虚拟化主机名。
        :type os_ext_srv_att_rhypervisor_hostname: str
        :param os_ext_a_zavailability_zone: 扩展属性，裸金属服务器所在可用分区名称。
        :type os_ext_a_zavailability_zone: str
        :param os_dc_fdisk_config: 扩展属性，磁盘配置，取值为以下两种：MANUAL：API使用镜像中的分区方案和文件系统创建裸金属服务器。如果目标flavor磁盘较大，则API不会对剩余磁盘空间进行分区。AUTO：API使用与目标flavor磁盘大小相同的单个分区创建裸金属服务器，API会自动调整文件系统以适应整个分区。
        :type os_dc_fdisk_config: str
        :param fault: 
        :type fault: :class:`huaweicloudsdkbms.v1.Fault`
        :param os_srv_us_glaunched_at: 裸金属服务器启动时间。时间戳格式为ISO 8601，例如：2019-05-22T03:23:59.000000
        :type os_srv_us_glaunched_at: str
        :param os_srv_us_gterminated_at: 裸金属服务器删除时间。时间戳格式为ISO 8601，例如：2019-05-22T04:23:59.000000
        :type os_srv_us_gterminated_at: str
        :param os_extended_volumesvolumes_attached: 挂载到裸金属服务器上的磁盘。详情请参见表9 os-extended-volumes:volumes_attached 数据结构说明。
        :type os_extended_volumesvolumes_attached: list[:class:`huaweicloudsdkbms.v1.OsExtendedVolumesInfo`]
        :param description: 裸金属服务器的描述信息
        :type description: str
        :param host_status: 裸金属服务器宿主机状态。UP：服务正常UNKNOWN：状态未知DOWN：服务异常MAINTENANCE：维护状态空字符串：裸金属服务器无主机信息
        :type host_status: str
        :param os_ext_srv_att_rhostname: 裸金属服务器的主机名
        :type os_ext_srv_att_rhostname: str
        :param os_ext_srv_att_rreservation_id: 批量创建场景，裸金属服务器的预留ID。当批量创建裸金属服务器时，这些服务器将拥有相同的reservation_id。您可以使用6.3.3-查询裸金属服务器详情列表API并指定reservation_id来过滤查询同一批创建的所有裸金属服务器。
        :type os_ext_srv_att_rreservation_id: str
        :param os_ext_srv_att_rlaunch_index: 批量创建场景，裸金属服务器的启动顺序
        :type os_ext_srv_att_rlaunch_index: int
        :param os_ext_srv_att_rkernel_id: 若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空
        :type os_ext_srv_att_rkernel_id: str
        :param os_ext_srv_att_rramdisk_id: 若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。
        :type os_ext_srv_att_rramdisk_id: str
        :param os_ext_srv_att_rroot_device_name: 裸金属服务器系统盘的设备名称，例如“/dev/sda”。
        :type os_ext_srv_att_rroot_device_name: str
        :param os_ext_srv_att_ruser_data: 创建裸金属服务器时指定的user_data，取值为base64编码后的结果或空字符串。
        :type os_ext_srv_att_ruser_data: str
        :param locked: 裸金属服务器是否为锁定状态。true：锁定false：未锁定
        :type locked: bool
        :param tags: 裸金属服务器标签。
        :type tags: list[str]
        :param osscheduler_hints: 
        :type osscheduler_hints: :class:`huaweicloudsdkbms.v1.SchedulerHints`
        :param enterprise_project_id: 裸金属服务器所属的企业项目ID
        :type enterprise_project_id: str
        :param sys_tags: 裸金属服务器系统标签。详情请参见表12 sys_tags数据结构说明。
        :type sys_tags: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        """
        
        

        self._id = None
        self._user_id = None
        self._name = None
        self._created = None
        self._updated = None
        self._tenant_id = None
        self._host_id = None
        self._addresses = None
        self._key_name = None
        self._image = None
        self._flavor = None
        self._security_groups = None
        self._access_i_pv4 = None
        self._access_i_pv6 = None
        self._status = None
        self._progress = None
        self._config_drive = None
        self._metadata = None
        self._os_ext_st_stask_state = None
        self._os_ext_st_svm_state = None
        self._os_ext_srv_att_rhost = None
        self._os_ext_srv_att_rinstance_name = None
        self._os_ext_st_spower_state = None
        self._os_ext_srv_att_rhypervisor_hostname = None
        self._os_ext_a_zavailability_zone = None
        self._os_dc_fdisk_config = None
        self._fault = None
        self._os_srv_us_glaunched_at = None
        self._os_srv_us_gterminated_at = None
        self._os_extended_volumesvolumes_attached = None
        self._description = None
        self._host_status = None
        self._os_ext_srv_att_rhostname = None
        self._os_ext_srv_att_rreservation_id = None
        self._os_ext_srv_att_rlaunch_index = None
        self._os_ext_srv_att_rkernel_id = None
        self._os_ext_srv_att_rramdisk_id = None
        self._os_ext_srv_att_rroot_device_name = None
        self._os_ext_srv_att_ruser_data = None
        self._locked = None
        self._tags = None
        self._osscheduler_hints = None
        self._enterprise_project_id = None
        self._sys_tags = None
        self.discriminator = None

        self.id = id
        if user_id is not None:
            self.user_id = user_id
        self.name = name
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        self.tenant_id = tenant_id
        if host_id is not None:
            self.host_id = host_id
        if addresses is not None:
            self.addresses = addresses
        if key_name is not None:
            self.key_name = key_name
        if image is not None:
            self.image = image
        if flavor is not None:
            self.flavor = flavor
        if security_groups is not None:
            self.security_groups = security_groups
        if access_i_pv4 is not None:
            self.access_i_pv4 = access_i_pv4
        if access_i_pv6 is not None:
            self.access_i_pv6 = access_i_pv6
        self.status = status
        if progress is not None:
            self.progress = progress
        if config_drive is not None:
            self.config_drive = config_drive
        self.metadata = metadata
        if os_ext_st_stask_state is not None:
            self.os_ext_st_stask_state = os_ext_st_stask_state
        if os_ext_st_svm_state is not None:
            self.os_ext_st_svm_state = os_ext_st_svm_state
        if os_ext_srv_att_rhost is not None:
            self.os_ext_srv_att_rhost = os_ext_srv_att_rhost
        if os_ext_srv_att_rinstance_name is not None:
            self.os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name
        if os_ext_st_spower_state is not None:
            self.os_ext_st_spower_state = os_ext_st_spower_state
        if os_ext_srv_att_rhypervisor_hostname is not None:
            self.os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname
        if os_ext_a_zavailability_zone is not None:
            self.os_ext_a_zavailability_zone = os_ext_a_zavailability_zone
        if os_dc_fdisk_config is not None:
            self.os_dc_fdisk_config = os_dc_fdisk_config
        if fault is not None:
            self.fault = fault
        if os_srv_us_glaunched_at is not None:
            self.os_srv_us_glaunched_at = os_srv_us_glaunched_at
        if os_srv_us_gterminated_at is not None:
            self.os_srv_us_gterminated_at = os_srv_us_gterminated_at
        if os_extended_volumesvolumes_attached is not None:
            self.os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached
        if description is not None:
            self.description = description
        if host_status is not None:
            self.host_status = host_status
        if os_ext_srv_att_rhostname is not None:
            self.os_ext_srv_att_rhostname = os_ext_srv_att_rhostname
        if os_ext_srv_att_rreservation_id is not None:
            self.os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id
        if os_ext_srv_att_rlaunch_index is not None:
            self.os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index
        if os_ext_srv_att_rkernel_id is not None:
            self.os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id
        if os_ext_srv_att_rramdisk_id is not None:
            self.os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id
        if os_ext_srv_att_rroot_device_name is not None:
            self.os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name
        if os_ext_srv_att_ruser_data is not None:
            self.os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data
        if locked is not None:
            self.locked = locked
        if tags is not None:
            self.tags = tags
        if osscheduler_hints is not None:
            self.osscheduler_hints = osscheduler_hints
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def id(self):
        r"""Gets the id of this ServerDetails.

        裸金属服务器ID，格式为UUID

        :return: The id of this ServerDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ServerDetails.

        裸金属服务器ID，格式为UUID

        :param id: The id of this ServerDetails.
        :type id: str
        """
        self._id = id

    @property
    def user_id(self):
        r"""Gets the user_id of this ServerDetails.

        创建裸金属服务器的用户ID，格式为UUID。

        :return: The user_id of this ServerDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ServerDetails.

        创建裸金属服务器的用户ID，格式为UUID。

        :param user_id: The user_id of this ServerDetails.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def name(self):
        r"""Gets the name of this ServerDetails.

        裸金属服务器名称

        :return: The name of this ServerDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServerDetails.

        裸金属服务器名称

        :param name: The name of this ServerDetails.
        :type name: str
        """
        self._name = name

    @property
    def created(self):
        r"""Gets the created of this ServerDetails.

        裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z

        :return: The created of this ServerDetails.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ServerDetails.

        裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z

        :param created: The created of this ServerDetails.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ServerDetails.

        裸金属服务器更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z

        :return: The updated of this ServerDetails.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ServerDetails.

        裸金属服务器更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z

        :param updated: The updated of this ServerDetails.
        :type updated: str
        """
        self._updated = updated

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ServerDetails.

        裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。

        :return: The tenant_id of this ServerDetails.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ServerDetails.

        裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。

        :param tenant_id: The tenant_id of this ServerDetails.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def host_id(self):
        r"""Gets the host_id of this ServerDetails.

        裸金属服务器对应的主机ID

        :return: The host_id of this ServerDetails.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ServerDetails.

        裸金属服务器对应的主机ID

        :param host_id: The host_id of this ServerDetails.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def addresses(self):
        r"""Gets the addresses of this ServerDetails.

        裸金属服务器的网络属性。详情请参见表3 addresses数据结构说明。

        :return: The addresses of this ServerDetails.
        :rtype: dict(str, list[AddressInfo])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this ServerDetails.

        裸金属服务器的网络属性。详情请参见表3 addresses数据结构说明。

        :param addresses: The addresses of this ServerDetails.
        :type addresses: dict(str, list[AddressInfo])
        """
        self._addresses = addresses

    @property
    def key_name(self):
        r"""Gets the key_name of this ServerDetails.

        裸金属服务器使用的密钥对名称

        :return: The key_name of this ServerDetails.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this ServerDetails.

        裸金属服务器使用的密钥对名称

        :param key_name: The key_name of this ServerDetails.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def image(self):
        r"""Gets the image of this ServerDetails.

        :return: The image of this ServerDetails.
        :rtype: :class:`huaweicloudsdkbms.v1.ImageInfo`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this ServerDetails.

        :param image: The image of this ServerDetails.
        :type image: :class:`huaweicloudsdkbms.v1.ImageInfo`
        """
        self._image = image

    @property
    def flavor(self):
        r"""Gets the flavor of this ServerDetails.

        :return: The flavor of this ServerDetails.
        :rtype: :class:`huaweicloudsdkbms.v1.FlavorInfos`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ServerDetails.

        :param flavor: The flavor of this ServerDetails.
        :type flavor: :class:`huaweicloudsdkbms.v1.FlavorInfos`
        """
        self._flavor = flavor

    @property
    def security_groups(self):
        r"""Gets the security_groups of this ServerDetails.

        裸金属服务器所属安全组。详情请参见表7 security_groups数据结构说明。

        :return: The security_groups of this ServerDetails.
        :rtype: list[:class:`huaweicloudsdkbms.v1.SecurityGroupsList`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this ServerDetails.

        裸金属服务器所属安全组。详情请参见表7 security_groups数据结构说明。

        :param security_groups: The security_groups of this ServerDetails.
        :type security_groups: list[:class:`huaweicloudsdkbms.v1.SecurityGroupsList`]
        """
        self._security_groups = security_groups

    @property
    def access_i_pv4(self):
        r"""Gets the access_i_pv4 of this ServerDetails.

        预留属性

        :return: The access_i_pv4 of this ServerDetails.
        :rtype: str
        """
        return self._access_i_pv4

    @access_i_pv4.setter
    def access_i_pv4(self, access_i_pv4):
        r"""Sets the access_i_pv4 of this ServerDetails.

        预留属性

        :param access_i_pv4: The access_i_pv4 of this ServerDetails.
        :type access_i_pv4: str
        """
        self._access_i_pv4 = access_i_pv4

    @property
    def access_i_pv6(self):
        r"""Gets the access_i_pv6 of this ServerDetails.

        预留属性

        :return: The access_i_pv6 of this ServerDetails.
        :rtype: str
        """
        return self._access_i_pv6

    @access_i_pv6.setter
    def access_i_pv6(self, access_i_pv6):
        r"""Sets the access_i_pv6 of this ServerDetails.

        预留属性

        :param access_i_pv6: The access_i_pv6 of this ServerDetails.
        :type access_i_pv6: str
        """
        self._access_i_pv6 = access_i_pv6

    @property
    def status(self):
        r"""Gets the status of this ServerDetails.

        裸金属服务器当前状态信息。  取值范围：  ACTIVE：运行中/正在关机/删除中 BUILD：创建中 ERROR：故障 HARD_REBOOT：强制重启中 REBOOT：重启中 DELETED：实例已被正常删除 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结

        :return: The status of this ServerDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ServerDetails.

        裸金属服务器当前状态信息。  取值范围：  ACTIVE：运行中/正在关机/删除中 BUILD：创建中 ERROR：故障 HARD_REBOOT：强制重启中 REBOOT：重启中 DELETED：实例已被正常删除 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结

        :param status: The status of this ServerDetails.
        :type status: str
        """
        self._status = status

    @property
    def progress(self):
        r"""Gets the progress of this ServerDetails.

        预留属性

        :return: The progress of this ServerDetails.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ServerDetails.

        预留属性

        :param progress: The progress of this ServerDetails.
        :type progress: int
        """
        self._progress = progress

    @property
    def config_drive(self):
        r"""Gets the config_drive of this ServerDetails.

        是否为裸金属服务器配置config drive分区。取值为：True或空字符串

        :return: The config_drive of this ServerDetails.
        :rtype: str
        """
        return self._config_drive

    @config_drive.setter
    def config_drive(self, config_drive):
        r"""Sets the config_drive of this ServerDetails.

        是否为裸金属服务器配置config drive分区。取值为：True或空字符串

        :param config_drive: The config_drive of this ServerDetails.
        :type config_drive: str
        """
        self._config_drive = config_drive

    @property
    def metadata(self):
        r"""Gets the metadata of this ServerDetails.

        :return: The metadata of this ServerDetails.
        :rtype: :class:`huaweicloudsdkbms.v1.MetadataList`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ServerDetails.

        :param metadata: The metadata of this ServerDetails.
        :type metadata: :class:`huaweicloudsdkbms.v1.MetadataList`
        """
        self._metadata = metadata

    @property
    def os_ext_st_stask_state(self):
        r"""Gets the os_ext_st_stask_state of this ServerDetails.

        扩展属性，裸金属服务器当前的任务状态。例如：rebooting：重启中reboot_started：普通重启reboot_started_hard：强制重启powering-off：关机中powering-on：开机中rebuilding：重建中scheduling：调度中deleting：删除中

        :return: The os_ext_st_stask_state of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_st_stask_state

    @os_ext_st_stask_state.setter
    def os_ext_st_stask_state(self, os_ext_st_stask_state):
        r"""Sets the os_ext_st_stask_state of this ServerDetails.

        扩展属性，裸金属服务器当前的任务状态。例如：rebooting：重启中reboot_started：普通重启reboot_started_hard：强制重启powering-off：关机中powering-on：开机中rebuilding：重建中scheduling：调度中deleting：删除中

        :param os_ext_st_stask_state: The os_ext_st_stask_state of this ServerDetails.
        :type os_ext_st_stask_state: str
        """
        self._os_ext_st_stask_state = os_ext_st_stask_state

    @property
    def os_ext_st_svm_state(self):
        r"""Gets the os_ext_st_svm_state of this ServerDetails.

        扩展属性，裸金属服务器的稳定状态。例如：active：运行中shutoff：关机reboot：重启

        :return: The os_ext_st_svm_state of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_st_svm_state

    @os_ext_st_svm_state.setter
    def os_ext_st_svm_state(self, os_ext_st_svm_state):
        r"""Sets the os_ext_st_svm_state of this ServerDetails.

        扩展属性，裸金属服务器的稳定状态。例如：active：运行中shutoff：关机reboot：重启

        :param os_ext_st_svm_state: The os_ext_st_svm_state of this ServerDetails.
        :type os_ext_st_svm_state: str
        """
        self._os_ext_st_svm_state = os_ext_st_svm_state

    @property
    def os_ext_srv_att_rhost(self):
        r"""Gets the os_ext_srv_att_rhost of this ServerDetails.

        扩展属性，裸金属服务器宿主名称

        :return: The os_ext_srv_att_rhost of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_rhost

    @os_ext_srv_att_rhost.setter
    def os_ext_srv_att_rhost(self, os_ext_srv_att_rhost):
        r"""Sets the os_ext_srv_att_rhost of this ServerDetails.

        扩展属性，裸金属服务器宿主名称

        :param os_ext_srv_att_rhost: The os_ext_srv_att_rhost of this ServerDetails.
        :type os_ext_srv_att_rhost: str
        """
        self._os_ext_srv_att_rhost = os_ext_srv_att_rhost

    @property
    def os_ext_srv_att_rinstance_name(self):
        r"""Gets the os_ext_srv_att_rinstance_name of this ServerDetails.

        扩展属性，裸金属服务器实例ID

        :return: The os_ext_srv_att_rinstance_name of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_rinstance_name

    @os_ext_srv_att_rinstance_name.setter
    def os_ext_srv_att_rinstance_name(self, os_ext_srv_att_rinstance_name):
        r"""Sets the os_ext_srv_att_rinstance_name of this ServerDetails.

        扩展属性，裸金属服务器实例ID

        :param os_ext_srv_att_rinstance_name: The os_ext_srv_att_rinstance_name of this ServerDetails.
        :type os_ext_srv_att_rinstance_name: str
        """
        self._os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name

    @property
    def os_ext_st_spower_state(self):
        r"""Gets the os_ext_st_spower_state of this ServerDetails.

        扩展属性，裸金属服务器电源状态。例如：0表示“NO STATE”1表示“RUNNING”4表示“SHUTDOWN”

        :return: The os_ext_st_spower_state of this ServerDetails.
        :rtype: int
        """
        return self._os_ext_st_spower_state

    @os_ext_st_spower_state.setter
    def os_ext_st_spower_state(self, os_ext_st_spower_state):
        r"""Sets the os_ext_st_spower_state of this ServerDetails.

        扩展属性，裸金属服务器电源状态。例如：0表示“NO STATE”1表示“RUNNING”4表示“SHUTDOWN”

        :param os_ext_st_spower_state: The os_ext_st_spower_state of this ServerDetails.
        :type os_ext_st_spower_state: int
        """
        self._os_ext_st_spower_state = os_ext_st_spower_state

    @property
    def os_ext_srv_att_rhypervisor_hostname(self):
        r"""Gets the os_ext_srv_att_rhypervisor_hostname of this ServerDetails.

        扩展属性，裸金属服务器所在虚拟化主机名。

        :return: The os_ext_srv_att_rhypervisor_hostname of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_rhypervisor_hostname

    @os_ext_srv_att_rhypervisor_hostname.setter
    def os_ext_srv_att_rhypervisor_hostname(self, os_ext_srv_att_rhypervisor_hostname):
        r"""Sets the os_ext_srv_att_rhypervisor_hostname of this ServerDetails.

        扩展属性，裸金属服务器所在虚拟化主机名。

        :param os_ext_srv_att_rhypervisor_hostname: The os_ext_srv_att_rhypervisor_hostname of this ServerDetails.
        :type os_ext_srv_att_rhypervisor_hostname: str
        """
        self._os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname

    @property
    def os_ext_a_zavailability_zone(self):
        r"""Gets the os_ext_a_zavailability_zone of this ServerDetails.

        扩展属性，裸金属服务器所在可用分区名称。

        :return: The os_ext_a_zavailability_zone of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_a_zavailability_zone

    @os_ext_a_zavailability_zone.setter
    def os_ext_a_zavailability_zone(self, os_ext_a_zavailability_zone):
        r"""Sets the os_ext_a_zavailability_zone of this ServerDetails.

        扩展属性，裸金属服务器所在可用分区名称。

        :param os_ext_a_zavailability_zone: The os_ext_a_zavailability_zone of this ServerDetails.
        :type os_ext_a_zavailability_zone: str
        """
        self._os_ext_a_zavailability_zone = os_ext_a_zavailability_zone

    @property
    def os_dc_fdisk_config(self):
        r"""Gets the os_dc_fdisk_config of this ServerDetails.

        扩展属性，磁盘配置，取值为以下两种：MANUAL：API使用镜像中的分区方案和文件系统创建裸金属服务器。如果目标flavor磁盘较大，则API不会对剩余磁盘空间进行分区。AUTO：API使用与目标flavor磁盘大小相同的单个分区创建裸金属服务器，API会自动调整文件系统以适应整个分区。

        :return: The os_dc_fdisk_config of this ServerDetails.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        r"""Sets the os_dc_fdisk_config of this ServerDetails.

        扩展属性，磁盘配置，取值为以下两种：MANUAL：API使用镜像中的分区方案和文件系统创建裸金属服务器。如果目标flavor磁盘较大，则API不会对剩余磁盘空间进行分区。AUTO：API使用与目标flavor磁盘大小相同的单个分区创建裸金属服务器，API会自动调整文件系统以适应整个分区。

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this ServerDetails.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def fault(self):
        r"""Gets the fault of this ServerDetails.

        :return: The fault of this ServerDetails.
        :rtype: :class:`huaweicloudsdkbms.v1.Fault`
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        r"""Sets the fault of this ServerDetails.

        :param fault: The fault of this ServerDetails.
        :type fault: :class:`huaweicloudsdkbms.v1.Fault`
        """
        self._fault = fault

    @property
    def os_srv_us_glaunched_at(self):
        r"""Gets the os_srv_us_glaunched_at of this ServerDetails.

        裸金属服务器启动时间。时间戳格式为ISO 8601，例如：2019-05-22T03:23:59.000000

        :return: The os_srv_us_glaunched_at of this ServerDetails.
        :rtype: str
        """
        return self._os_srv_us_glaunched_at

    @os_srv_us_glaunched_at.setter
    def os_srv_us_glaunched_at(self, os_srv_us_glaunched_at):
        r"""Sets the os_srv_us_glaunched_at of this ServerDetails.

        裸金属服务器启动时间。时间戳格式为ISO 8601，例如：2019-05-22T03:23:59.000000

        :param os_srv_us_glaunched_at: The os_srv_us_glaunched_at of this ServerDetails.
        :type os_srv_us_glaunched_at: str
        """
        self._os_srv_us_glaunched_at = os_srv_us_glaunched_at

    @property
    def os_srv_us_gterminated_at(self):
        r"""Gets the os_srv_us_gterminated_at of this ServerDetails.

        裸金属服务器删除时间。时间戳格式为ISO 8601，例如：2019-05-22T04:23:59.000000

        :return: The os_srv_us_gterminated_at of this ServerDetails.
        :rtype: str
        """
        return self._os_srv_us_gterminated_at

    @os_srv_us_gterminated_at.setter
    def os_srv_us_gterminated_at(self, os_srv_us_gterminated_at):
        r"""Sets the os_srv_us_gterminated_at of this ServerDetails.

        裸金属服务器删除时间。时间戳格式为ISO 8601，例如：2019-05-22T04:23:59.000000

        :param os_srv_us_gterminated_at: The os_srv_us_gterminated_at of this ServerDetails.
        :type os_srv_us_gterminated_at: str
        """
        self._os_srv_us_gterminated_at = os_srv_us_gterminated_at

    @property
    def os_extended_volumesvolumes_attached(self):
        r"""Gets the os_extended_volumesvolumes_attached of this ServerDetails.

        挂载到裸金属服务器上的磁盘。详情请参见表9 os-extended-volumes:volumes_attached 数据结构说明。

        :return: The os_extended_volumesvolumes_attached of this ServerDetails.
        :rtype: list[:class:`huaweicloudsdkbms.v1.OsExtendedVolumesInfo`]
        """
        return self._os_extended_volumesvolumes_attached

    @os_extended_volumesvolumes_attached.setter
    def os_extended_volumesvolumes_attached(self, os_extended_volumesvolumes_attached):
        r"""Sets the os_extended_volumesvolumes_attached of this ServerDetails.

        挂载到裸金属服务器上的磁盘。详情请参见表9 os-extended-volumes:volumes_attached 数据结构说明。

        :param os_extended_volumesvolumes_attached: The os_extended_volumesvolumes_attached of this ServerDetails.
        :type os_extended_volumesvolumes_attached: list[:class:`huaweicloudsdkbms.v1.OsExtendedVolumesInfo`]
        """
        self._os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached

    @property
    def description(self):
        r"""Gets the description of this ServerDetails.

        裸金属服务器的描述信息

        :return: The description of this ServerDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ServerDetails.

        裸金属服务器的描述信息

        :param description: The description of this ServerDetails.
        :type description: str
        """
        self._description = description

    @property
    def host_status(self):
        r"""Gets the host_status of this ServerDetails.

        裸金属服务器宿主机状态。UP：服务正常UNKNOWN：状态未知DOWN：服务异常MAINTENANCE：维护状态空字符串：裸金属服务器无主机信息

        :return: The host_status of this ServerDetails.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        r"""Sets the host_status of this ServerDetails.

        裸金属服务器宿主机状态。UP：服务正常UNKNOWN：状态未知DOWN：服务异常MAINTENANCE：维护状态空字符串：裸金属服务器无主机信息

        :param host_status: The host_status of this ServerDetails.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_ext_srv_att_rhostname(self):
        r"""Gets the os_ext_srv_att_rhostname of this ServerDetails.

        裸金属服务器的主机名

        :return: The os_ext_srv_att_rhostname of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_rhostname

    @os_ext_srv_att_rhostname.setter
    def os_ext_srv_att_rhostname(self, os_ext_srv_att_rhostname):
        r"""Sets the os_ext_srv_att_rhostname of this ServerDetails.

        裸金属服务器的主机名

        :param os_ext_srv_att_rhostname: The os_ext_srv_att_rhostname of this ServerDetails.
        :type os_ext_srv_att_rhostname: str
        """
        self._os_ext_srv_att_rhostname = os_ext_srv_att_rhostname

    @property
    def os_ext_srv_att_rreservation_id(self):
        r"""Gets the os_ext_srv_att_rreservation_id of this ServerDetails.

        批量创建场景，裸金属服务器的预留ID。当批量创建裸金属服务器时，这些服务器将拥有相同的reservation_id。您可以使用6.3.3-查询裸金属服务器详情列表API并指定reservation_id来过滤查询同一批创建的所有裸金属服务器。

        :return: The os_ext_srv_att_rreservation_id of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_rreservation_id

    @os_ext_srv_att_rreservation_id.setter
    def os_ext_srv_att_rreservation_id(self, os_ext_srv_att_rreservation_id):
        r"""Sets the os_ext_srv_att_rreservation_id of this ServerDetails.

        批量创建场景，裸金属服务器的预留ID。当批量创建裸金属服务器时，这些服务器将拥有相同的reservation_id。您可以使用6.3.3-查询裸金属服务器详情列表API并指定reservation_id来过滤查询同一批创建的所有裸金属服务器。

        :param os_ext_srv_att_rreservation_id: The os_ext_srv_att_rreservation_id of this ServerDetails.
        :type os_ext_srv_att_rreservation_id: str
        """
        self._os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id

    @property
    def os_ext_srv_att_rlaunch_index(self):
        r"""Gets the os_ext_srv_att_rlaunch_index of this ServerDetails.

        批量创建场景，裸金属服务器的启动顺序

        :return: The os_ext_srv_att_rlaunch_index of this ServerDetails.
        :rtype: int
        """
        return self._os_ext_srv_att_rlaunch_index

    @os_ext_srv_att_rlaunch_index.setter
    def os_ext_srv_att_rlaunch_index(self, os_ext_srv_att_rlaunch_index):
        r"""Sets the os_ext_srv_att_rlaunch_index of this ServerDetails.

        批量创建场景，裸金属服务器的启动顺序

        :param os_ext_srv_att_rlaunch_index: The os_ext_srv_att_rlaunch_index of this ServerDetails.
        :type os_ext_srv_att_rlaunch_index: int
        """
        self._os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index

    @property
    def os_ext_srv_att_rkernel_id(self):
        r"""Gets the os_ext_srv_att_rkernel_id of this ServerDetails.

        若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空

        :return: The os_ext_srv_att_rkernel_id of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_rkernel_id

    @os_ext_srv_att_rkernel_id.setter
    def os_ext_srv_att_rkernel_id(self, os_ext_srv_att_rkernel_id):
        r"""Sets the os_ext_srv_att_rkernel_id of this ServerDetails.

        若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空

        :param os_ext_srv_att_rkernel_id: The os_ext_srv_att_rkernel_id of this ServerDetails.
        :type os_ext_srv_att_rkernel_id: str
        """
        self._os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id

    @property
    def os_ext_srv_att_rramdisk_id(self):
        r"""Gets the os_ext_srv_att_rramdisk_id of this ServerDetails.

        若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。

        :return: The os_ext_srv_att_rramdisk_id of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_rramdisk_id

    @os_ext_srv_att_rramdisk_id.setter
    def os_ext_srv_att_rramdisk_id(self, os_ext_srv_att_rramdisk_id):
        r"""Sets the os_ext_srv_att_rramdisk_id of this ServerDetails.

        若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。

        :param os_ext_srv_att_rramdisk_id: The os_ext_srv_att_rramdisk_id of this ServerDetails.
        :type os_ext_srv_att_rramdisk_id: str
        """
        self._os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id

    @property
    def os_ext_srv_att_rroot_device_name(self):
        r"""Gets the os_ext_srv_att_rroot_device_name of this ServerDetails.

        裸金属服务器系统盘的设备名称，例如“/dev/sda”。

        :return: The os_ext_srv_att_rroot_device_name of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_rroot_device_name

    @os_ext_srv_att_rroot_device_name.setter
    def os_ext_srv_att_rroot_device_name(self, os_ext_srv_att_rroot_device_name):
        r"""Sets the os_ext_srv_att_rroot_device_name of this ServerDetails.

        裸金属服务器系统盘的设备名称，例如“/dev/sda”。

        :param os_ext_srv_att_rroot_device_name: The os_ext_srv_att_rroot_device_name of this ServerDetails.
        :type os_ext_srv_att_rroot_device_name: str
        """
        self._os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name

    @property
    def os_ext_srv_att_ruser_data(self):
        r"""Gets the os_ext_srv_att_ruser_data of this ServerDetails.

        创建裸金属服务器时指定的user_data，取值为base64编码后的结果或空字符串。

        :return: The os_ext_srv_att_ruser_data of this ServerDetails.
        :rtype: str
        """
        return self._os_ext_srv_att_ruser_data

    @os_ext_srv_att_ruser_data.setter
    def os_ext_srv_att_ruser_data(self, os_ext_srv_att_ruser_data):
        r"""Sets the os_ext_srv_att_ruser_data of this ServerDetails.

        创建裸金属服务器时指定的user_data，取值为base64编码后的结果或空字符串。

        :param os_ext_srv_att_ruser_data: The os_ext_srv_att_ruser_data of this ServerDetails.
        :type os_ext_srv_att_ruser_data: str
        """
        self._os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data

    @property
    def locked(self):
        r"""Gets the locked of this ServerDetails.

        裸金属服务器是否为锁定状态。true：锁定false：未锁定

        :return: The locked of this ServerDetails.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this ServerDetails.

        裸金属服务器是否为锁定状态。true：锁定false：未锁定

        :param locked: The locked of this ServerDetails.
        :type locked: bool
        """
        self._locked = locked

    @property
    def tags(self):
        r"""Gets the tags of this ServerDetails.

        裸金属服务器标签。

        :return: The tags of this ServerDetails.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ServerDetails.

        裸金属服务器标签。

        :param tags: The tags of this ServerDetails.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def osscheduler_hints(self):
        r"""Gets the osscheduler_hints of this ServerDetails.

        :return: The osscheduler_hints of this ServerDetails.
        :rtype: :class:`huaweicloudsdkbms.v1.SchedulerHints`
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        r"""Sets the osscheduler_hints of this ServerDetails.

        :param osscheduler_hints: The osscheduler_hints of this ServerDetails.
        :type osscheduler_hints: :class:`huaweicloudsdkbms.v1.SchedulerHints`
        """
        self._osscheduler_hints = osscheduler_hints

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ServerDetails.

        裸金属服务器所属的企业项目ID

        :return: The enterprise_project_id of this ServerDetails.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ServerDetails.

        裸金属服务器所属的企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ServerDetails.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ServerDetails.

        裸金属服务器系统标签。详情请参见表12 sys_tags数据结构说明。

        :return: The sys_tags of this ServerDetails.
        :rtype: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ServerDetails.

        裸金属服务器系统标签。详情请参见表12 sys_tags数据结构说明。

        :param sys_tags: The sys_tags of this ServerDetails.
        :type sys_tags: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, ServerDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
