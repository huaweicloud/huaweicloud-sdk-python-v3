# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeBaremetalNameResponsesServers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'str',
        'status': 'str',
        'created': 'datetime',
        'updated': 'datetime',
        'flavor': 'FlavorInfo',
        'image': 'Image',
        'tenant_id': 'str',
        'key_name': 'str',
        'user_id': 'str',
        'metadata': 'MetadataInfos',
        'host_id': 'str',
        'addresses': 'Addresses',
        'security_groups': 'list[SecurityGroups]',
        'links': 'list[Links]',
        'os_dc_fdisk_config': 'str',
        'os_ext_a_zavailability_zone': 'str',
        'os_ext_srv_att_rhost': 'str',
        'os_ext_srv_att_rhypervisor_hostname': 'str',
        'os_ext_srv_att_rinstance_name': 'str',
        'os_ext_st_spower_state': 'int',
        'os_ext_st_stask_state': 'str',
        'os_ext_st_svm_state': 'str',
        'os_srv_us_glaunched_at': 'datetime',
        'os_srv_us_gterminated_at': 'datetime',
        'os_extended_volumesvolumes_attached': 'list[OsExtendedVolumes]',
        'access_i_pv4': 'str',
        'access_i_pv6': 'str',
        'fault': 'Fault',
        'config_drive': 'str',
        'progress': 'int',
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
        'sys_tags': 'list[SystemTags]',
        'enterprise_project_id': 'str',
        'osscheduler_hints': 'ServerOsSchedulerHints'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'status': 'status',
        'created': 'created',
        'updated': 'updated',
        'flavor': 'flavor',
        'image': 'image',
        'tenant_id': 'tenant_id',
        'key_name': 'key_name',
        'user_id': 'user_id',
        'metadata': 'metadata',
        'host_id': 'hostId',
        'addresses': 'addresses',
        'security_groups': 'security_groups',
        'links': 'links',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'os_ext_a_zavailability_zone': 'OS-EXT-AZ:availability_zone',
        'os_ext_srv_att_rhost': 'OS-EXT-SRV-ATTR:host',
        'os_ext_srv_att_rhypervisor_hostname': 'OS-EXT-SRV-ATTR:hypervisor_hostname',
        'os_ext_srv_att_rinstance_name': 'OS-EXT-SRV-ATTR:instance_name',
        'os_ext_st_spower_state': 'OS-EXT-STS:power_state',
        'os_ext_st_stask_state': 'OS-EXT-STS:task_state',
        'os_ext_st_svm_state': 'OS-EXT-STS:vm_state',
        'os_srv_us_glaunched_at': 'OS-SRV-USG:launched_at',
        'os_srv_us_gterminated_at': 'OS-SRV-USG:terminated_at',
        'os_extended_volumesvolumes_attached': 'os-extended-volumes:volumes_attached',
        'access_i_pv4': 'accessIPv4',
        'access_i_pv6': 'accessIPv6',
        'fault': 'fault',
        'config_drive': 'config_drive',
        'progress': 'progress',
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
        'sys_tags': 'sys_tags',
        'enterprise_project_id': 'enterprise_project_id',
        'osscheduler_hints': 'os:scheduler_hints'
    }

    def __init__(self, name=None, id=None, status=None, created=None, updated=None, flavor=None, image=None, tenant_id=None, key_name=None, user_id=None, metadata=None, host_id=None, addresses=None, security_groups=None, links=None, os_dc_fdisk_config=None, os_ext_a_zavailability_zone=None, os_ext_srv_att_rhost=None, os_ext_srv_att_rhypervisor_hostname=None, os_ext_srv_att_rinstance_name=None, os_ext_st_spower_state=None, os_ext_st_stask_state=None, os_ext_st_svm_state=None, os_srv_us_glaunched_at=None, os_srv_us_gterminated_at=None, os_extended_volumesvolumes_attached=None, access_i_pv4=None, access_i_pv6=None, fault=None, config_drive=None, progress=None, description=None, host_status=None, os_ext_srv_att_rhostname=None, os_ext_srv_att_rreservation_id=None, os_ext_srv_att_rlaunch_index=None, os_ext_srv_att_rkernel_id=None, os_ext_srv_att_rramdisk_id=None, os_ext_srv_att_rroot_device_name=None, os_ext_srv_att_ruser_data=None, locked=None, tags=None, sys_tags=None, enterprise_project_id=None, osscheduler_hints=None):
        """ChangeBaremetalNameResponsesServers

        The model defined in huaweicloud sdk

        :param name: 裸金属服务器名称
        :type name: str
        :param id: 裸金属服务器唯一标识ID
        :type id: str
        :param status: 裸金属服务器当前状态。ACTIVE：运行中/正在关机/删除中BUILD：创建中ERROR：故障HARD_REBOOT：强制重启中REBOOT：重启中 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结
        :type status: str
        :param created: 裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z
        :type created: datetime
        :param updated: 裸金属服务器上一次更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z
        :type updated: datetime
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkbms.v1.FlavorInfo`
        :param image: 
        :type image: :class:`huaweicloudsdkbms.v1.Image`
        :param tenant_id: 裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。
        :type tenant_id: str
        :param key_name: SSH密钥名称
        :type key_name: str
        :param user_id: 裸金属服务器所属用户ID。
        :type user_id: str
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkbms.v1.MetadataInfos`
        :param host_id: 裸金属服务器的主机ID
        :type host_id: str
        :param addresses: 
        :type addresses: :class:`huaweicloudsdkbms.v1.Addresses`
        :param security_groups: 裸金属服务器所属安全组列表。
        :type security_groups: list[:class:`huaweicloudsdkbms.v1.SecurityGroups`]
        :param links: 裸金属服务器相关信息快捷链接
        :type links: list[:class:`huaweicloudsdkbms.v1.Links`]
        :param os_dc_fdisk_config: 扩展属性，磁盘配置方式，取值为如下两种：MANUAL：API使用镜像中的分区方案和文件系统创建裸金属服务器。如果目标flavor磁盘较大，则API不会对剩余磁盘空间进行分区。AUTO：API使用与目标flavor磁盘大小相同的单个分区创建裸金属服务器，API会自动调整文件系统以适应整个分区。
        :type os_dc_fdisk_config: str
        :param os_ext_a_zavailability_zone: 扩展属性，可用分区编码。
        :type os_ext_a_zavailability_zone: str
        :param os_ext_srv_att_rhost: 扩展属性，裸金属服务器宿主名称
        :type os_ext_srv_att_rhost: str
        :param os_ext_srv_att_rhypervisor_hostname: 扩展属性，hypervisor主机名称，由Nova virt驱动提供
        :type os_ext_srv_att_rhypervisor_hostname: str
        :param os_ext_srv_att_rinstance_name: 扩展属性，裸金属服务器实例ID
        :type os_ext_srv_att_rinstance_name: str
        :param os_ext_st_spower_state: 扩展属性，裸金属服务器电源状态。例如：0表示“NO STATE”1表示“RUNNING”4表示“SHUTDOWN”
        :type os_ext_st_spower_state: int
        :param os_ext_st_stask_state: 扩展属性，裸金属服务器任务状态。例如：rebooting表示重启中reboot_started表示普通重启reboot_started_hard表示强制重启powering-off表示关机中powering-on表示开机中rebuilding表示重建中scheduling表示调度中deleting表示删除中
        :type os_ext_st_stask_state: str
        :param os_ext_st_svm_state: 扩展属性，裸金属服务器状态。例如：RUNNING表示运行中SHUTOFF表示关机REBOOT表示重启
        :type os_ext_st_svm_state: str
        :param os_srv_us_glaunched_at: 扩展属性，裸金属服务器启动时间。时间戳格式为ISO 8601，例如：2019-05-25T03:40:25.000000
        :type os_srv_us_glaunched_at: datetime
        :param os_srv_us_gterminated_at: 扩展属性，裸金属服务器关闭时间。时间戳格式为ISO 8601，例如：2019-06-25T03:40:25.000000
        :type os_srv_us_gterminated_at: datetime
        :param os_extended_volumesvolumes_attached: 裸金属服务器挂载的云硬盘信息。详情请参见表 os-extended-volumes:volumes_attached字段数据结构说明。
        :type os_extended_volumesvolumes_attached: list[:class:`huaweicloudsdkbms.v1.OsExtendedVolumes`]
        :param access_i_pv4: 预留属性
        :type access_i_pv4: str
        :param access_i_pv6: 预留属性
        :type access_i_pv6: str
        :param fault: 
        :type fault: :class:`huaweicloudsdkbms.v1.Fault`
        :param config_drive: config drive信息
        :type config_drive: str
        :param progress: 预留属性
        :type progress: int
        :param description: 裸金属服务器的描述信息。
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
        :param os_ext_srv_att_rroot_device_name: 裸金属服务器系统盘的设备名称，例如“/dev/sdb”。
        :type os_ext_srv_att_rroot_device_name: str
        :param os_ext_srv_att_ruser_data: 创建裸金属服务器时指定的user_data。取值为base64编码后的结果或空字符串。
        :type os_ext_srv_att_ruser_data: str
        :param locked: 裸金属服务器实例是否为锁定状态。true：锁定false：未锁定
        :type locked: bool
        :param tags: 裸金属服务器标签
        :type tags: list[str]
        :param sys_tags: 裸金属服务器的系统标签
        :type sys_tags: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        :param enterprise_project_id: enterprise_project_id。
        :type enterprise_project_id: str
        :param osscheduler_hints: 
        :type osscheduler_hints: :class:`huaweicloudsdkbms.v1.ServerOsSchedulerHints`
        """
        
        

        self._name = None
        self._id = None
        self._status = None
        self._created = None
        self._updated = None
        self._flavor = None
        self._image = None
        self._tenant_id = None
        self._key_name = None
        self._user_id = None
        self._metadata = None
        self._host_id = None
        self._addresses = None
        self._security_groups = None
        self._links = None
        self._os_dc_fdisk_config = None
        self._os_ext_a_zavailability_zone = None
        self._os_ext_srv_att_rhost = None
        self._os_ext_srv_att_rhypervisor_hostname = None
        self._os_ext_srv_att_rinstance_name = None
        self._os_ext_st_spower_state = None
        self._os_ext_st_stask_state = None
        self._os_ext_st_svm_state = None
        self._os_srv_us_glaunched_at = None
        self._os_srv_us_gterminated_at = None
        self._os_extended_volumesvolumes_attached = None
        self._access_i_pv4 = None
        self._access_i_pv6 = None
        self._fault = None
        self._config_drive = None
        self._progress = None
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
        self._sys_tags = None
        self._enterprise_project_id = None
        self._osscheduler_hints = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if flavor is not None:
            self.flavor = flavor
        if image is not None:
            self.image = image
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if key_name is not None:
            self.key_name = key_name
        if user_id is not None:
            self.user_id = user_id
        if metadata is not None:
            self.metadata = metadata
        if host_id is not None:
            self.host_id = host_id
        if addresses is not None:
            self.addresses = addresses
        if security_groups is not None:
            self.security_groups = security_groups
        if links is not None:
            self.links = links
        if os_dc_fdisk_config is not None:
            self.os_dc_fdisk_config = os_dc_fdisk_config
        if os_ext_a_zavailability_zone is not None:
            self.os_ext_a_zavailability_zone = os_ext_a_zavailability_zone
        if os_ext_srv_att_rhost is not None:
            self.os_ext_srv_att_rhost = os_ext_srv_att_rhost
        if os_ext_srv_att_rhypervisor_hostname is not None:
            self.os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname
        if os_ext_srv_att_rinstance_name is not None:
            self.os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name
        if os_ext_st_spower_state is not None:
            self.os_ext_st_spower_state = os_ext_st_spower_state
        if os_ext_st_stask_state is not None:
            self.os_ext_st_stask_state = os_ext_st_stask_state
        if os_ext_st_svm_state is not None:
            self.os_ext_st_svm_state = os_ext_st_svm_state
        if os_srv_us_glaunched_at is not None:
            self.os_srv_us_glaunched_at = os_srv_us_glaunched_at
        if os_srv_us_gterminated_at is not None:
            self.os_srv_us_gterminated_at = os_srv_us_gterminated_at
        if os_extended_volumesvolumes_attached is not None:
            self.os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached
        if access_i_pv4 is not None:
            self.access_i_pv4 = access_i_pv4
        if access_i_pv6 is not None:
            self.access_i_pv6 = access_i_pv6
        if fault is not None:
            self.fault = fault
        if config_drive is not None:
            self.config_drive = config_drive
        if progress is not None:
            self.progress = progress
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
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if osscheduler_hints is not None:
            self.osscheduler_hints = osscheduler_hints

    @property
    def name(self):
        """Gets the name of this ChangeBaremetalNameResponsesServers.

        裸金属服务器名称

        :return: The name of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChangeBaremetalNameResponsesServers.

        裸金属服务器名称

        :param name: The name of this ChangeBaremetalNameResponsesServers.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this ChangeBaremetalNameResponsesServers.

        裸金属服务器唯一标识ID

        :return: The id of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChangeBaremetalNameResponsesServers.

        裸金属服务器唯一标识ID

        :param id: The id of this ChangeBaremetalNameResponsesServers.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this ChangeBaremetalNameResponsesServers.

        裸金属服务器当前状态。ACTIVE：运行中/正在关机/删除中BUILD：创建中ERROR：故障HARD_REBOOT：强制重启中REBOOT：重启中 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结

        :return: The status of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ChangeBaremetalNameResponsesServers.

        裸金属服务器当前状态。ACTIVE：运行中/正在关机/删除中BUILD：创建中ERROR：故障HARD_REBOOT：强制重启中REBOOT：重启中 SHUTOFF：关机/正在开机/删除中/重建中/重装操作系统中/重装操作系统失败/冻结

        :param status: The status of this ChangeBaremetalNameResponsesServers.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        """Gets the created of this ChangeBaremetalNameResponsesServers.

        裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z

        :return: The created of this ChangeBaremetalNameResponsesServers.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ChangeBaremetalNameResponsesServers.

        裸金属服务器创建时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T03:30:52Z

        :param created: The created of this ChangeBaremetalNameResponsesServers.
        :type created: datetime
        """
        self._created = created

    @property
    def updated(self):
        """Gets the updated of this ChangeBaremetalNameResponsesServers.

        裸金属服务器上一次更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z

        :return: The updated of this ChangeBaremetalNameResponsesServers.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ChangeBaremetalNameResponsesServers.

        裸金属服务器上一次更新时间。时间戳格式为ISO 8601：YYYY-MM-DDTHH:MM:SSZ，例如：2019-05-22T04:30:52Z

        :param updated: The updated of this ChangeBaremetalNameResponsesServers.
        :type updated: datetime
        """
        self._updated = updated

    @property
    def flavor(self):
        """Gets the flavor of this ChangeBaremetalNameResponsesServers.

        :return: The flavor of this ChangeBaremetalNameResponsesServers.
        :rtype: :class:`huaweicloudsdkbms.v1.FlavorInfo`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ChangeBaremetalNameResponsesServers.

        :param flavor: The flavor of this ChangeBaremetalNameResponsesServers.
        :type flavor: :class:`huaweicloudsdkbms.v1.FlavorInfo`
        """
        self._flavor = flavor

    @property
    def image(self):
        """Gets the image of this ChangeBaremetalNameResponsesServers.

        :return: The image of this ChangeBaremetalNameResponsesServers.
        :rtype: :class:`huaweicloudsdkbms.v1.Image`
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ChangeBaremetalNameResponsesServers.

        :param image: The image of this ChangeBaremetalNameResponsesServers.
        :type image: :class:`huaweicloudsdkbms.v1.Image`
        """
        self._image = image

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ChangeBaremetalNameResponsesServers.

        裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。

        :return: The tenant_id of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ChangeBaremetalNameResponsesServers.

        裸金属服务器所属租户ID，格式为UUID。该参数和project_id表示相同的概念。

        :param tenant_id: The tenant_id of this ChangeBaremetalNameResponsesServers.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def key_name(self):
        """Gets the key_name of this ChangeBaremetalNameResponsesServers.

        SSH密钥名称

        :return: The key_name of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this ChangeBaremetalNameResponsesServers.

        SSH密钥名称

        :param key_name: The key_name of this ChangeBaremetalNameResponsesServers.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def user_id(self):
        """Gets the user_id of this ChangeBaremetalNameResponsesServers.

        裸金属服务器所属用户ID。

        :return: The user_id of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ChangeBaremetalNameResponsesServers.

        裸金属服务器所属用户ID。

        :param user_id: The user_id of this ChangeBaremetalNameResponsesServers.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def metadata(self):
        """Gets the metadata of this ChangeBaremetalNameResponsesServers.

        :return: The metadata of this ChangeBaremetalNameResponsesServers.
        :rtype: :class:`huaweicloudsdkbms.v1.MetadataInfos`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ChangeBaremetalNameResponsesServers.

        :param metadata: The metadata of this ChangeBaremetalNameResponsesServers.
        :type metadata: :class:`huaweicloudsdkbms.v1.MetadataInfos`
        """
        self._metadata = metadata

    @property
    def host_id(self):
        """Gets the host_id of this ChangeBaremetalNameResponsesServers.

        裸金属服务器的主机ID

        :return: The host_id of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ChangeBaremetalNameResponsesServers.

        裸金属服务器的主机ID

        :param host_id: The host_id of this ChangeBaremetalNameResponsesServers.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def addresses(self):
        """Gets the addresses of this ChangeBaremetalNameResponsesServers.

        :return: The addresses of this ChangeBaremetalNameResponsesServers.
        :rtype: :class:`huaweicloudsdkbms.v1.Addresses`
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ChangeBaremetalNameResponsesServers.

        :param addresses: The addresses of this ChangeBaremetalNameResponsesServers.
        :type addresses: :class:`huaweicloudsdkbms.v1.Addresses`
        """
        self._addresses = addresses

    @property
    def security_groups(self):
        """Gets the security_groups of this ChangeBaremetalNameResponsesServers.

        裸金属服务器所属安全组列表。

        :return: The security_groups of this ChangeBaremetalNameResponsesServers.
        :rtype: list[:class:`huaweicloudsdkbms.v1.SecurityGroups`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ChangeBaremetalNameResponsesServers.

        裸金属服务器所属安全组列表。

        :param security_groups: The security_groups of this ChangeBaremetalNameResponsesServers.
        :type security_groups: list[:class:`huaweicloudsdkbms.v1.SecurityGroups`]
        """
        self._security_groups = security_groups

    @property
    def links(self):
        """Gets the links of this ChangeBaremetalNameResponsesServers.

        裸金属服务器相关信息快捷链接

        :return: The links of this ChangeBaremetalNameResponsesServers.
        :rtype: list[:class:`huaweicloudsdkbms.v1.Links`]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ChangeBaremetalNameResponsesServers.

        裸金属服务器相关信息快捷链接

        :param links: The links of this ChangeBaremetalNameResponsesServers.
        :type links: list[:class:`huaweicloudsdkbms.v1.Links`]
        """
        self._links = links

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this ChangeBaremetalNameResponsesServers.

        扩展属性，磁盘配置方式，取值为如下两种：MANUAL：API使用镜像中的分区方案和文件系统创建裸金属服务器。如果目标flavor磁盘较大，则API不会对剩余磁盘空间进行分区。AUTO：API使用与目标flavor磁盘大小相同的单个分区创建裸金属服务器，API会自动调整文件系统以适应整个分区。

        :return: The os_dc_fdisk_config of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this ChangeBaremetalNameResponsesServers.

        扩展属性，磁盘配置方式，取值为如下两种：MANUAL：API使用镜像中的分区方案和文件系统创建裸金属服务器。如果目标flavor磁盘较大，则API不会对剩余磁盘空间进行分区。AUTO：API使用与目标flavor磁盘大小相同的单个分区创建裸金属服务器，API会自动调整文件系统以适应整个分区。

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this ChangeBaremetalNameResponsesServers.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def os_ext_a_zavailability_zone(self):
        """Gets the os_ext_a_zavailability_zone of this ChangeBaremetalNameResponsesServers.

        扩展属性，可用分区编码。

        :return: The os_ext_a_zavailability_zone of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_a_zavailability_zone

    @os_ext_a_zavailability_zone.setter
    def os_ext_a_zavailability_zone(self, os_ext_a_zavailability_zone):
        """Sets the os_ext_a_zavailability_zone of this ChangeBaremetalNameResponsesServers.

        扩展属性，可用分区编码。

        :param os_ext_a_zavailability_zone: The os_ext_a_zavailability_zone of this ChangeBaremetalNameResponsesServers.
        :type os_ext_a_zavailability_zone: str
        """
        self._os_ext_a_zavailability_zone = os_ext_a_zavailability_zone

    @property
    def os_ext_srv_att_rhost(self):
        """Gets the os_ext_srv_att_rhost of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器宿主名称

        :return: The os_ext_srv_att_rhost of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_rhost

    @os_ext_srv_att_rhost.setter
    def os_ext_srv_att_rhost(self, os_ext_srv_att_rhost):
        """Sets the os_ext_srv_att_rhost of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器宿主名称

        :param os_ext_srv_att_rhost: The os_ext_srv_att_rhost of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rhost: str
        """
        self._os_ext_srv_att_rhost = os_ext_srv_att_rhost

    @property
    def os_ext_srv_att_rhypervisor_hostname(self):
        """Gets the os_ext_srv_att_rhypervisor_hostname of this ChangeBaremetalNameResponsesServers.

        扩展属性，hypervisor主机名称，由Nova virt驱动提供

        :return: The os_ext_srv_att_rhypervisor_hostname of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_rhypervisor_hostname

    @os_ext_srv_att_rhypervisor_hostname.setter
    def os_ext_srv_att_rhypervisor_hostname(self, os_ext_srv_att_rhypervisor_hostname):
        """Sets the os_ext_srv_att_rhypervisor_hostname of this ChangeBaremetalNameResponsesServers.

        扩展属性，hypervisor主机名称，由Nova virt驱动提供

        :param os_ext_srv_att_rhypervisor_hostname: The os_ext_srv_att_rhypervisor_hostname of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rhypervisor_hostname: str
        """
        self._os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname

    @property
    def os_ext_srv_att_rinstance_name(self):
        """Gets the os_ext_srv_att_rinstance_name of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器实例ID

        :return: The os_ext_srv_att_rinstance_name of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_rinstance_name

    @os_ext_srv_att_rinstance_name.setter
    def os_ext_srv_att_rinstance_name(self, os_ext_srv_att_rinstance_name):
        """Sets the os_ext_srv_att_rinstance_name of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器实例ID

        :param os_ext_srv_att_rinstance_name: The os_ext_srv_att_rinstance_name of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rinstance_name: str
        """
        self._os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name

    @property
    def os_ext_st_spower_state(self):
        """Gets the os_ext_st_spower_state of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器电源状态。例如：0表示“NO STATE”1表示“RUNNING”4表示“SHUTDOWN”

        :return: The os_ext_st_spower_state of this ChangeBaremetalNameResponsesServers.
        :rtype: int
        """
        return self._os_ext_st_spower_state

    @os_ext_st_spower_state.setter
    def os_ext_st_spower_state(self, os_ext_st_spower_state):
        """Sets the os_ext_st_spower_state of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器电源状态。例如：0表示“NO STATE”1表示“RUNNING”4表示“SHUTDOWN”

        :param os_ext_st_spower_state: The os_ext_st_spower_state of this ChangeBaremetalNameResponsesServers.
        :type os_ext_st_spower_state: int
        """
        self._os_ext_st_spower_state = os_ext_st_spower_state

    @property
    def os_ext_st_stask_state(self):
        """Gets the os_ext_st_stask_state of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器任务状态。例如：rebooting表示重启中reboot_started表示普通重启reboot_started_hard表示强制重启powering-off表示关机中powering-on表示开机中rebuilding表示重建中scheduling表示调度中deleting表示删除中

        :return: The os_ext_st_stask_state of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_st_stask_state

    @os_ext_st_stask_state.setter
    def os_ext_st_stask_state(self, os_ext_st_stask_state):
        """Sets the os_ext_st_stask_state of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器任务状态。例如：rebooting表示重启中reboot_started表示普通重启reboot_started_hard表示强制重启powering-off表示关机中powering-on表示开机中rebuilding表示重建中scheduling表示调度中deleting表示删除中

        :param os_ext_st_stask_state: The os_ext_st_stask_state of this ChangeBaremetalNameResponsesServers.
        :type os_ext_st_stask_state: str
        """
        self._os_ext_st_stask_state = os_ext_st_stask_state

    @property
    def os_ext_st_svm_state(self):
        """Gets the os_ext_st_svm_state of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器状态。例如：RUNNING表示运行中SHUTOFF表示关机REBOOT表示重启

        :return: The os_ext_st_svm_state of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_st_svm_state

    @os_ext_st_svm_state.setter
    def os_ext_st_svm_state(self, os_ext_st_svm_state):
        """Sets the os_ext_st_svm_state of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器状态。例如：RUNNING表示运行中SHUTOFF表示关机REBOOT表示重启

        :param os_ext_st_svm_state: The os_ext_st_svm_state of this ChangeBaremetalNameResponsesServers.
        :type os_ext_st_svm_state: str
        """
        self._os_ext_st_svm_state = os_ext_st_svm_state

    @property
    def os_srv_us_glaunched_at(self):
        """Gets the os_srv_us_glaunched_at of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器启动时间。时间戳格式为ISO 8601，例如：2019-05-25T03:40:25.000000

        :return: The os_srv_us_glaunched_at of this ChangeBaremetalNameResponsesServers.
        :rtype: datetime
        """
        return self._os_srv_us_glaunched_at

    @os_srv_us_glaunched_at.setter
    def os_srv_us_glaunched_at(self, os_srv_us_glaunched_at):
        """Sets the os_srv_us_glaunched_at of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器启动时间。时间戳格式为ISO 8601，例如：2019-05-25T03:40:25.000000

        :param os_srv_us_glaunched_at: The os_srv_us_glaunched_at of this ChangeBaremetalNameResponsesServers.
        :type os_srv_us_glaunched_at: datetime
        """
        self._os_srv_us_glaunched_at = os_srv_us_glaunched_at

    @property
    def os_srv_us_gterminated_at(self):
        """Gets the os_srv_us_gterminated_at of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器关闭时间。时间戳格式为ISO 8601，例如：2019-06-25T03:40:25.000000

        :return: The os_srv_us_gterminated_at of this ChangeBaremetalNameResponsesServers.
        :rtype: datetime
        """
        return self._os_srv_us_gterminated_at

    @os_srv_us_gterminated_at.setter
    def os_srv_us_gterminated_at(self, os_srv_us_gterminated_at):
        """Sets the os_srv_us_gterminated_at of this ChangeBaremetalNameResponsesServers.

        扩展属性，裸金属服务器关闭时间。时间戳格式为ISO 8601，例如：2019-06-25T03:40:25.000000

        :param os_srv_us_gterminated_at: The os_srv_us_gterminated_at of this ChangeBaremetalNameResponsesServers.
        :type os_srv_us_gterminated_at: datetime
        """
        self._os_srv_us_gterminated_at = os_srv_us_gterminated_at

    @property
    def os_extended_volumesvolumes_attached(self):
        """Gets the os_extended_volumesvolumes_attached of this ChangeBaremetalNameResponsesServers.

        裸金属服务器挂载的云硬盘信息。详情请参见表 os-extended-volumes:volumes_attached字段数据结构说明。

        :return: The os_extended_volumesvolumes_attached of this ChangeBaremetalNameResponsesServers.
        :rtype: list[:class:`huaweicloudsdkbms.v1.OsExtendedVolumes`]
        """
        return self._os_extended_volumesvolumes_attached

    @os_extended_volumesvolumes_attached.setter
    def os_extended_volumesvolumes_attached(self, os_extended_volumesvolumes_attached):
        """Sets the os_extended_volumesvolumes_attached of this ChangeBaremetalNameResponsesServers.

        裸金属服务器挂载的云硬盘信息。详情请参见表 os-extended-volumes:volumes_attached字段数据结构说明。

        :param os_extended_volumesvolumes_attached: The os_extended_volumesvolumes_attached of this ChangeBaremetalNameResponsesServers.
        :type os_extended_volumesvolumes_attached: list[:class:`huaweicloudsdkbms.v1.OsExtendedVolumes`]
        """
        self._os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached

    @property
    def access_i_pv4(self):
        """Gets the access_i_pv4 of this ChangeBaremetalNameResponsesServers.

        预留属性

        :return: The access_i_pv4 of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._access_i_pv4

    @access_i_pv4.setter
    def access_i_pv4(self, access_i_pv4):
        """Sets the access_i_pv4 of this ChangeBaremetalNameResponsesServers.

        预留属性

        :param access_i_pv4: The access_i_pv4 of this ChangeBaremetalNameResponsesServers.
        :type access_i_pv4: str
        """
        self._access_i_pv4 = access_i_pv4

    @property
    def access_i_pv6(self):
        """Gets the access_i_pv6 of this ChangeBaremetalNameResponsesServers.

        预留属性

        :return: The access_i_pv6 of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._access_i_pv6

    @access_i_pv6.setter
    def access_i_pv6(self, access_i_pv6):
        """Sets the access_i_pv6 of this ChangeBaremetalNameResponsesServers.

        预留属性

        :param access_i_pv6: The access_i_pv6 of this ChangeBaremetalNameResponsesServers.
        :type access_i_pv6: str
        """
        self._access_i_pv6 = access_i_pv6

    @property
    def fault(self):
        """Gets the fault of this ChangeBaremetalNameResponsesServers.

        :return: The fault of this ChangeBaremetalNameResponsesServers.
        :rtype: :class:`huaweicloudsdkbms.v1.Fault`
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        """Sets the fault of this ChangeBaremetalNameResponsesServers.

        :param fault: The fault of this ChangeBaremetalNameResponsesServers.
        :type fault: :class:`huaweicloudsdkbms.v1.Fault`
        """
        self._fault = fault

    @property
    def config_drive(self):
        """Gets the config_drive of this ChangeBaremetalNameResponsesServers.

        config drive信息

        :return: The config_drive of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._config_drive

    @config_drive.setter
    def config_drive(self, config_drive):
        """Sets the config_drive of this ChangeBaremetalNameResponsesServers.

        config drive信息

        :param config_drive: The config_drive of this ChangeBaremetalNameResponsesServers.
        :type config_drive: str
        """
        self._config_drive = config_drive

    @property
    def progress(self):
        """Gets the progress of this ChangeBaremetalNameResponsesServers.

        预留属性

        :return: The progress of this ChangeBaremetalNameResponsesServers.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ChangeBaremetalNameResponsesServers.

        预留属性

        :param progress: The progress of this ChangeBaremetalNameResponsesServers.
        :type progress: int
        """
        self._progress = progress

    @property
    def description(self):
        """Gets the description of this ChangeBaremetalNameResponsesServers.

        裸金属服务器的描述信息。

        :return: The description of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChangeBaremetalNameResponsesServers.

        裸金属服务器的描述信息。

        :param description: The description of this ChangeBaremetalNameResponsesServers.
        :type description: str
        """
        self._description = description

    @property
    def host_status(self):
        """Gets the host_status of this ChangeBaremetalNameResponsesServers.

        裸金属服务器宿主机状态。UP：服务正常UNKNOWN：状态未知DOWN：服务异常MAINTENANCE：维护状态空字符串：裸金属服务器无主机信息

        :return: The host_status of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ChangeBaremetalNameResponsesServers.

        裸金属服务器宿主机状态。UP：服务正常UNKNOWN：状态未知DOWN：服务异常MAINTENANCE：维护状态空字符串：裸金属服务器无主机信息

        :param host_status: The host_status of this ChangeBaremetalNameResponsesServers.
        :type host_status: str
        """
        self._host_status = host_status

    @property
    def os_ext_srv_att_rhostname(self):
        """Gets the os_ext_srv_att_rhostname of this ChangeBaremetalNameResponsesServers.

        裸金属服务器的主机名

        :return: The os_ext_srv_att_rhostname of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_rhostname

    @os_ext_srv_att_rhostname.setter
    def os_ext_srv_att_rhostname(self, os_ext_srv_att_rhostname):
        """Sets the os_ext_srv_att_rhostname of this ChangeBaremetalNameResponsesServers.

        裸金属服务器的主机名

        :param os_ext_srv_att_rhostname: The os_ext_srv_att_rhostname of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rhostname: str
        """
        self._os_ext_srv_att_rhostname = os_ext_srv_att_rhostname

    @property
    def os_ext_srv_att_rreservation_id(self):
        """Gets the os_ext_srv_att_rreservation_id of this ChangeBaremetalNameResponsesServers.

        批量创建场景，裸金属服务器的预留ID。当批量创建裸金属服务器时，这些服务器将拥有相同的reservation_id。您可以使用6.3.3-查询裸金属服务器详情列表API并指定reservation_id来过滤查询同一批创建的所有裸金属服务器。

        :return: The os_ext_srv_att_rreservation_id of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_rreservation_id

    @os_ext_srv_att_rreservation_id.setter
    def os_ext_srv_att_rreservation_id(self, os_ext_srv_att_rreservation_id):
        """Sets the os_ext_srv_att_rreservation_id of this ChangeBaremetalNameResponsesServers.

        批量创建场景，裸金属服务器的预留ID。当批量创建裸金属服务器时，这些服务器将拥有相同的reservation_id。您可以使用6.3.3-查询裸金属服务器详情列表API并指定reservation_id来过滤查询同一批创建的所有裸金属服务器。

        :param os_ext_srv_att_rreservation_id: The os_ext_srv_att_rreservation_id of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rreservation_id: str
        """
        self._os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id

    @property
    def os_ext_srv_att_rlaunch_index(self):
        """Gets the os_ext_srv_att_rlaunch_index of this ChangeBaremetalNameResponsesServers.

        批量创建场景，裸金属服务器的启动顺序

        :return: The os_ext_srv_att_rlaunch_index of this ChangeBaremetalNameResponsesServers.
        :rtype: int
        """
        return self._os_ext_srv_att_rlaunch_index

    @os_ext_srv_att_rlaunch_index.setter
    def os_ext_srv_att_rlaunch_index(self, os_ext_srv_att_rlaunch_index):
        """Sets the os_ext_srv_att_rlaunch_index of this ChangeBaremetalNameResponsesServers.

        批量创建场景，裸金属服务器的启动顺序

        :param os_ext_srv_att_rlaunch_index: The os_ext_srv_att_rlaunch_index of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rlaunch_index: int
        """
        self._os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index

    @property
    def os_ext_srv_att_rkernel_id(self):
        """Gets the os_ext_srv_att_rkernel_id of this ChangeBaremetalNameResponsesServers.

        若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空

        :return: The os_ext_srv_att_rkernel_id of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_rkernel_id

    @os_ext_srv_att_rkernel_id.setter
    def os_ext_srv_att_rkernel_id(self, os_ext_srv_att_rkernel_id):
        """Sets the os_ext_srv_att_rkernel_id of this ChangeBaremetalNameResponsesServers.

        若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空

        :param os_ext_srv_att_rkernel_id: The os_ext_srv_att_rkernel_id of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rkernel_id: str
        """
        self._os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id

    @property
    def os_ext_srv_att_rramdisk_id(self):
        """Gets the os_ext_srv_att_rramdisk_id of this ChangeBaremetalNameResponsesServers.

        若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。

        :return: The os_ext_srv_att_rramdisk_id of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_rramdisk_id

    @os_ext_srv_att_rramdisk_id.setter
    def os_ext_srv_att_rramdisk_id(self, os_ext_srv_att_rramdisk_id):
        """Sets the os_ext_srv_att_rramdisk_id of this ChangeBaremetalNameResponsesServers.

        若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。

        :param os_ext_srv_att_rramdisk_id: The os_ext_srv_att_rramdisk_id of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rramdisk_id: str
        """
        self._os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id

    @property
    def os_ext_srv_att_rroot_device_name(self):
        """Gets the os_ext_srv_att_rroot_device_name of this ChangeBaremetalNameResponsesServers.

        裸金属服务器系统盘的设备名称，例如“/dev/sdb”。

        :return: The os_ext_srv_att_rroot_device_name of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_rroot_device_name

    @os_ext_srv_att_rroot_device_name.setter
    def os_ext_srv_att_rroot_device_name(self, os_ext_srv_att_rroot_device_name):
        """Sets the os_ext_srv_att_rroot_device_name of this ChangeBaremetalNameResponsesServers.

        裸金属服务器系统盘的设备名称，例如“/dev/sdb”。

        :param os_ext_srv_att_rroot_device_name: The os_ext_srv_att_rroot_device_name of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_rroot_device_name: str
        """
        self._os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name

    @property
    def os_ext_srv_att_ruser_data(self):
        """Gets the os_ext_srv_att_ruser_data of this ChangeBaremetalNameResponsesServers.

        创建裸金属服务器时指定的user_data。取值为base64编码后的结果或空字符串。

        :return: The os_ext_srv_att_ruser_data of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._os_ext_srv_att_ruser_data

    @os_ext_srv_att_ruser_data.setter
    def os_ext_srv_att_ruser_data(self, os_ext_srv_att_ruser_data):
        """Sets the os_ext_srv_att_ruser_data of this ChangeBaremetalNameResponsesServers.

        创建裸金属服务器时指定的user_data。取值为base64编码后的结果或空字符串。

        :param os_ext_srv_att_ruser_data: The os_ext_srv_att_ruser_data of this ChangeBaremetalNameResponsesServers.
        :type os_ext_srv_att_ruser_data: str
        """
        self._os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data

    @property
    def locked(self):
        """Gets the locked of this ChangeBaremetalNameResponsesServers.

        裸金属服务器实例是否为锁定状态。true：锁定false：未锁定

        :return: The locked of this ChangeBaremetalNameResponsesServers.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this ChangeBaremetalNameResponsesServers.

        裸金属服务器实例是否为锁定状态。true：锁定false：未锁定

        :param locked: The locked of this ChangeBaremetalNameResponsesServers.
        :type locked: bool
        """
        self._locked = locked

    @property
    def tags(self):
        """Gets the tags of this ChangeBaremetalNameResponsesServers.

        裸金属服务器标签

        :return: The tags of this ChangeBaremetalNameResponsesServers.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ChangeBaremetalNameResponsesServers.

        裸金属服务器标签

        :param tags: The tags of this ChangeBaremetalNameResponsesServers.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ChangeBaremetalNameResponsesServers.

        裸金属服务器的系统标签

        :return: The sys_tags of this ChangeBaremetalNameResponsesServers.
        :rtype: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ChangeBaremetalNameResponsesServers.

        裸金属服务器的系统标签

        :param sys_tags: The sys_tags of this ChangeBaremetalNameResponsesServers.
        :type sys_tags: list[:class:`huaweicloudsdkbms.v1.SystemTags`]
        """
        self._sys_tags = sys_tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ChangeBaremetalNameResponsesServers.

        enterprise_project_id。

        :return: The enterprise_project_id of this ChangeBaremetalNameResponsesServers.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ChangeBaremetalNameResponsesServers.

        enterprise_project_id。

        :param enterprise_project_id: The enterprise_project_id of this ChangeBaremetalNameResponsesServers.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def osscheduler_hints(self):
        """Gets the osscheduler_hints of this ChangeBaremetalNameResponsesServers.

        :return: The osscheduler_hints of this ChangeBaremetalNameResponsesServers.
        :rtype: :class:`huaweicloudsdkbms.v1.ServerOsSchedulerHints`
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        """Sets the osscheduler_hints of this ChangeBaremetalNameResponsesServers.

        :param osscheduler_hints: The osscheduler_hints of this ChangeBaremetalNameResponsesServers.
        :type osscheduler_hints: :class:`huaweicloudsdkbms.v1.ServerOsSchedulerHints`
        """
        self._osscheduler_hints = osscheduler_hints

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
        if not isinstance(other, ChangeBaremetalNameResponsesServers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
