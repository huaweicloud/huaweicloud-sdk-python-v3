# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Instance:

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
        'updated': 'str',
        'host_id': 'str',
        'addresses': 'dict(str, list[InstanceAddress])',
        'created': 'str',
        'tags': 'list[str]',
        'locked': 'bool',
        'description': 'str',
        'tenant_id': 'str',
        'sys_tags': 'list[SysTags]',
        'flavor': 'FlavorInstance',
        'metadata': 'dict(str, str)',
        'security_groups': 'list[InstanceSecurityGroup]',
        'progress': 'int',
        'os_ext_st_spower_state': 'int',
        'os_ext_st_svm_state': 'str',
        'os_ext_st_stask_state': 'str',
        'os_dc_fdisk_config': 'str',
        'os_ext_a_zavailability_zone': 'str',
        'os_srv_us_glaunched_at': 'str',
        'os_srv_us_gterminated_at': 'str',
        'os_ext_srv_att_rroot_device_name': 'str',
        'os_ext_srv_att_rramdisk_id': 'str',
        'os_ext_srv_att_rkernel_id': 'str',
        'os_ext_srv_att_rlaunch_index': 'int',
        'os_ext_srv_att_rreservation_id': 'str',
        'os_ext_srv_att_rhostname': 'str',
        'os_ext_srv_att_ruser_data': 'str',
        'os_ext_srv_att_rhost': 'str',
        'os_ext_srv_att_rhypervisor_hostname': 'str',
        'os_extended_volumesvolumes_attached': 'list[VolumesAttached]',
        'geolocation': 'GeoLocation',
        'edgecloud_id': 'str',
        'edgecloud_name': 'str',
        'domain_id': 'str',
        'key_name': 'str',
        'os_ext_srv_att_rinstance_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'updated': 'updated',
        'host_id': 'hostId',
        'addresses': 'addresses',
        'created': 'created',
        'tags': 'tags',
        'locked': 'locked',
        'description': 'description',
        'tenant_id': 'tenant_id',
        'sys_tags': 'sys_tags',
        'flavor': 'flavor',
        'metadata': 'metadata',
        'security_groups': 'security_groups',
        'progress': 'progress',
        'os_ext_st_spower_state': 'OS-EXT-STS:power_state',
        'os_ext_st_svm_state': 'OS-EXT-STS:vm_state',
        'os_ext_st_stask_state': 'OS-EXT-STS:task_state',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'os_ext_a_zavailability_zone': 'OS-EXT-AZ:availability_zone',
        'os_srv_us_glaunched_at': 'OS-SRV-USG:launched_at',
        'os_srv_us_gterminated_at': 'OS-SRV-USG:terminated_at',
        'os_ext_srv_att_rroot_device_name': 'OS-EXT-SRV-ATTR:root_device_name',
        'os_ext_srv_att_rramdisk_id': 'OS-EXT-SRV-ATTR:ramdisk_id',
        'os_ext_srv_att_rkernel_id': 'OS-EXT-SRV-ATTR:kernel_id',
        'os_ext_srv_att_rlaunch_index': 'OS-EXT-SRV-ATTR:launch_index',
        'os_ext_srv_att_rreservation_id': 'OS-EXT-SRV-ATTR:reservation_id',
        'os_ext_srv_att_rhostname': 'OS-EXT-SRV-ATTR:hostname',
        'os_ext_srv_att_ruser_data': 'OS-EXT-SRV-ATTR:user_data',
        'os_ext_srv_att_rhost': 'OS-EXT-SRV-ATTR:host',
        'os_ext_srv_att_rhypervisor_hostname': 'OS-EXT-SRV-ATTR:hypervisor_hostname',
        'os_extended_volumesvolumes_attached': 'os-extended-volumes:volumes_attached',
        'geolocation': 'geolocation',
        'edgecloud_id': 'edgecloud_id',
        'edgecloud_name': 'edgecloud_name',
        'domain_id': 'domain_id',
        'key_name': 'key_name',
        'os_ext_srv_att_rinstance_name': 'OS-EXT-SRV-ATTR:instance_name'
    }

    def __init__(self, id=None, name=None, status=None, updated=None, host_id=None, addresses=None, created=None, tags=None, locked=None, description=None, tenant_id=None, sys_tags=None, flavor=None, metadata=None, security_groups=None, progress=None, os_ext_st_spower_state=None, os_ext_st_svm_state=None, os_ext_st_stask_state=None, os_dc_fdisk_config=None, os_ext_a_zavailability_zone=None, os_srv_us_glaunched_at=None, os_srv_us_gterminated_at=None, os_ext_srv_att_rroot_device_name=None, os_ext_srv_att_rramdisk_id=None, os_ext_srv_att_rkernel_id=None, os_ext_srv_att_rlaunch_index=None, os_ext_srv_att_rreservation_id=None, os_ext_srv_att_rhostname=None, os_ext_srv_att_ruser_data=None, os_ext_srv_att_rhost=None, os_ext_srv_att_rhypervisor_hostname=None, os_extended_volumesvolumes_attached=None, geolocation=None, edgecloud_id=None, edgecloud_name=None, domain_id=None, key_name=None, os_ext_srv_att_rinstance_name=None):
        """Instance

        The model defined in huaweicloud sdk

        :param id: 边缘实例ID。
        :type id: str
        :param name: 边缘实例名称。
        :type name: str
        :param status: 边缘实例状态。 取值范围： ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE
        :type status: str
        :param updated: 边缘实例修改时间。 UTC时间，格式：yyyy-mm-ddTss:ss:ssZ，例如：2021-04-25T03:21:39Z
        :type updated: str
        :param host_id: 边缘实例所在主机的主机ID。
        :type host_id: str
        :param addresses: 边缘实例对应的网络地址信息，详情请参见表addresses字段数据结构说明。
        :type addresses: dict(str, list[InstanceAddress])
        :param created: 边缘实例创建时间。 时间格式：yyyy-mm-ddTss:ss:ssZ，例如：2021-04-25T02:46:23Z
        :type created: str
        :param tags: 边缘实例标签。 主要用来存储边缘业务ID。
        :type tags: list[str]
        :param locked: 边缘实例是否为锁定状态。  - true：锁定 - false：未锁定
        :type locked: bool
        :param description: 边缘实例的描述信息。
        :type description: str
        :param tenant_id: 边缘实例所属租户ID，即项目ID，和project_id表示相同的概念，格式为UUID。
        :type tenant_id: str
        :param sys_tags: 边缘实例系统标签。
        :type sys_tags: list[:class:`huaweicloudsdkiec.v1.SysTags`]
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkiec.v1.FlavorInstance`
        :param metadata: 边缘实例元数据。
        :type metadata: dict(str, str)
        :param security_groups: 边缘实例所属安全组列表。
        :type security_groups: list[:class:`huaweicloudsdkiec.v1.InstanceSecurityGroup`]
        :param progress: 边缘实例进度。
        :type progress: int
        :param os_ext_st_spower_state: 扩展属性，边缘实例电源状态。
        :type os_ext_st_spower_state: int
        :param os_ext_st_svm_state: 扩展属性，边缘实例当前状态。
        :type os_ext_st_svm_state: str
        :param os_ext_st_stask_state: 边缘实例任务状态。
        :type os_ext_st_stask_state: str
        :param os_dc_fdisk_config: 扩展属性， diskConfig的类型。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。
        :type os_dc_fdisk_config: str
        :param os_ext_a_zavailability_zone: 扩展属性，边缘实例所在可用区名称。
        :type os_ext_a_zavailability_zone: str
        :param os_srv_us_glaunched_at: 边缘实例启动时间。 时间格式例如：2019-05-22T03:23:59.000000
        :type os_srv_us_glaunched_at: str
        :param os_srv_us_gterminated_at: 边缘实例删除时间。 时间格式例如：2019-05-22T03:23:59.000000
        :type os_srv_us_gterminated_at: str
        :param os_ext_srv_att_rroot_device_name: 边缘实例系统盘的设备名称。
        :type os_ext_srv_att_rroot_device_name: str
        :param os_ext_srv_att_rramdisk_id: 若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。
        :type os_ext_srv_att_rramdisk_id: str
        :param os_ext_srv_att_rkernel_id: 若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空。
        :type os_ext_srv_att_rkernel_id: str
        :param os_ext_srv_att_rlaunch_index: 批量创建场景，边缘实例的启动顺序。
        :type os_ext_srv_att_rlaunch_index: int
        :param os_ext_srv_att_rreservation_id: 批量创建场景，边缘实例的预留ID。
        :type os_ext_srv_att_rreservation_id: str
        :param os_ext_srv_att_rhostname: 边缘实例的主机名。
        :type os_ext_srv_att_rhostname: str
        :param os_ext_srv_att_ruser_data: 创建边缘实例时指定的user_data。
        :type os_ext_srv_att_ruser_data: str
        :param os_ext_srv_att_rhost: 边缘实例所在主机的主机名称。
        :type os_ext_srv_att_rhost: str
        :param os_ext_srv_att_rhypervisor_hostname: 扩展属性，边缘实例所在虚拟化主机名。
        :type os_ext_srv_att_rhypervisor_hostname: str
        :param os_extended_volumesvolumes_attached: 挂载到边缘实例上的磁盘。
        :type os_extended_volumesvolumes_attached: list[:class:`huaweicloudsdkiec.v1.VolumesAttached`]
        :param geolocation: 
        :type geolocation: :class:`huaweicloudsdkiec.v1.GeoLocation`
        :param edgecloud_id: 边缘实例所属边缘业务的ID。
        :type edgecloud_id: str
        :param edgecloud_name: 边缘实例所属边缘业务的名称
        :type edgecloud_name: str
        :param domain_id: 帐号ID。
        :type domain_id: str
        :param key_name: 使用的密钥对名称。
        :type key_name: str
        :param os_ext_srv_att_rinstance_name: 扩展属性，边缘实例别名。
        :type os_ext_srv_att_rinstance_name: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._updated = None
        self._host_id = None
        self._addresses = None
        self._created = None
        self._tags = None
        self._locked = None
        self._description = None
        self._tenant_id = None
        self._sys_tags = None
        self._flavor = None
        self._metadata = None
        self._security_groups = None
        self._progress = None
        self._os_ext_st_spower_state = None
        self._os_ext_st_svm_state = None
        self._os_ext_st_stask_state = None
        self._os_dc_fdisk_config = None
        self._os_ext_a_zavailability_zone = None
        self._os_srv_us_glaunched_at = None
        self._os_srv_us_gterminated_at = None
        self._os_ext_srv_att_rroot_device_name = None
        self._os_ext_srv_att_rramdisk_id = None
        self._os_ext_srv_att_rkernel_id = None
        self._os_ext_srv_att_rlaunch_index = None
        self._os_ext_srv_att_rreservation_id = None
        self._os_ext_srv_att_rhostname = None
        self._os_ext_srv_att_ruser_data = None
        self._os_ext_srv_att_rhost = None
        self._os_ext_srv_att_rhypervisor_hostname = None
        self._os_extended_volumesvolumes_attached = None
        self._geolocation = None
        self._edgecloud_id = None
        self._edgecloud_name = None
        self._domain_id = None
        self._key_name = None
        self._os_ext_srv_att_rinstance_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated
        if host_id is not None:
            self.host_id = host_id
        if addresses is not None:
            self.addresses = addresses
        if created is not None:
            self.created = created
        if tags is not None:
            self.tags = tags
        if locked is not None:
            self.locked = locked
        if description is not None:
            self.description = description
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if flavor is not None:
            self.flavor = flavor
        if metadata is not None:
            self.metadata = metadata
        if security_groups is not None:
            self.security_groups = security_groups
        if progress is not None:
            self.progress = progress
        if os_ext_st_spower_state is not None:
            self.os_ext_st_spower_state = os_ext_st_spower_state
        if os_ext_st_svm_state is not None:
            self.os_ext_st_svm_state = os_ext_st_svm_state
        if os_ext_st_stask_state is not None:
            self.os_ext_st_stask_state = os_ext_st_stask_state
        if os_dc_fdisk_config is not None:
            self.os_dc_fdisk_config = os_dc_fdisk_config
        if os_ext_a_zavailability_zone is not None:
            self.os_ext_a_zavailability_zone = os_ext_a_zavailability_zone
        if os_srv_us_glaunched_at is not None:
            self.os_srv_us_glaunched_at = os_srv_us_glaunched_at
        if os_srv_us_gterminated_at is not None:
            self.os_srv_us_gterminated_at = os_srv_us_gterminated_at
        if os_ext_srv_att_rroot_device_name is not None:
            self.os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name
        if os_ext_srv_att_rramdisk_id is not None:
            self.os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id
        if os_ext_srv_att_rkernel_id is not None:
            self.os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id
        if os_ext_srv_att_rlaunch_index is not None:
            self.os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index
        if os_ext_srv_att_rreservation_id is not None:
            self.os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id
        if os_ext_srv_att_rhostname is not None:
            self.os_ext_srv_att_rhostname = os_ext_srv_att_rhostname
        if os_ext_srv_att_ruser_data is not None:
            self.os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data
        if os_ext_srv_att_rhost is not None:
            self.os_ext_srv_att_rhost = os_ext_srv_att_rhost
        if os_ext_srv_att_rhypervisor_hostname is not None:
            self.os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname
        if os_extended_volumesvolumes_attached is not None:
            self.os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached
        if geolocation is not None:
            self.geolocation = geolocation
        if edgecloud_id is not None:
            self.edgecloud_id = edgecloud_id
        if edgecloud_name is not None:
            self.edgecloud_name = edgecloud_name
        if domain_id is not None:
            self.domain_id = domain_id
        if key_name is not None:
            self.key_name = key_name
        if os_ext_srv_att_rinstance_name is not None:
            self.os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name

    @property
    def id(self):
        """Gets the id of this Instance.

        边缘实例ID。

        :return: The id of this Instance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Instance.

        边缘实例ID。

        :param id: The id of this Instance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Instance.

        边缘实例名称。

        :return: The name of this Instance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Instance.

        边缘实例名称。

        :param name: The name of this Instance.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this Instance.

        边缘实例状态。 取值范围： ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE

        :return: The status of this Instance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Instance.

        边缘实例状态。 取值范围： ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE

        :param status: The status of this Instance.
        :type status: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this Instance.

        边缘实例修改时间。 UTC时间，格式：yyyy-mm-ddTss:ss:ssZ，例如：2021-04-25T03:21:39Z

        :return: The updated of this Instance.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Instance.

        边缘实例修改时间。 UTC时间，格式：yyyy-mm-ddTss:ss:ssZ，例如：2021-04-25T03:21:39Z

        :param updated: The updated of this Instance.
        :type updated: str
        """
        self._updated = updated

    @property
    def host_id(self):
        """Gets the host_id of this Instance.

        边缘实例所在主机的主机ID。

        :return: The host_id of this Instance.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this Instance.

        边缘实例所在主机的主机ID。

        :param host_id: The host_id of this Instance.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def addresses(self):
        """Gets the addresses of this Instance.

        边缘实例对应的网络地址信息，详情请参见表addresses字段数据结构说明。

        :return: The addresses of this Instance.
        :rtype: dict(str, list[InstanceAddress])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Instance.

        边缘实例对应的网络地址信息，详情请参见表addresses字段数据结构说明。

        :param addresses: The addresses of this Instance.
        :type addresses: dict(str, list[InstanceAddress])
        """
        self._addresses = addresses

    @property
    def created(self):
        """Gets the created of this Instance.

        边缘实例创建时间。 时间格式：yyyy-mm-ddTss:ss:ssZ，例如：2021-04-25T02:46:23Z

        :return: The created of this Instance.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Instance.

        边缘实例创建时间。 时间格式：yyyy-mm-ddTss:ss:ssZ，例如：2021-04-25T02:46:23Z

        :param created: The created of this Instance.
        :type created: str
        """
        self._created = created

    @property
    def tags(self):
        """Gets the tags of this Instance.

        边缘实例标签。 主要用来存储边缘业务ID。

        :return: The tags of this Instance.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Instance.

        边缘实例标签。 主要用来存储边缘业务ID。

        :param tags: The tags of this Instance.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def locked(self):
        """Gets the locked of this Instance.

        边缘实例是否为锁定状态。  - true：锁定 - false：未锁定

        :return: The locked of this Instance.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this Instance.

        边缘实例是否为锁定状态。  - true：锁定 - false：未锁定

        :param locked: The locked of this Instance.
        :type locked: bool
        """
        self._locked = locked

    @property
    def description(self):
        """Gets the description of this Instance.

        边缘实例的描述信息。

        :return: The description of this Instance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Instance.

        边缘实例的描述信息。

        :param description: The description of this Instance.
        :type description: str
        """
        self._description = description

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Instance.

        边缘实例所属租户ID，即项目ID，和project_id表示相同的概念，格式为UUID。

        :return: The tenant_id of this Instance.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Instance.

        边缘实例所属租户ID，即项目ID，和project_id表示相同的概念，格式为UUID。

        :param tenant_id: The tenant_id of this Instance.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def sys_tags(self):
        """Gets the sys_tags of this Instance.

        边缘实例系统标签。

        :return: The sys_tags of this Instance.
        :rtype: list[:class:`huaweicloudsdkiec.v1.SysTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this Instance.

        边缘实例系统标签。

        :param sys_tags: The sys_tags of this Instance.
        :type sys_tags: list[:class:`huaweicloudsdkiec.v1.SysTags`]
        """
        self._sys_tags = sys_tags

    @property
    def flavor(self):
        """Gets the flavor of this Instance.


        :return: The flavor of this Instance.
        :rtype: :class:`huaweicloudsdkiec.v1.FlavorInstance`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this Instance.


        :param flavor: The flavor of this Instance.
        :type flavor: :class:`huaweicloudsdkiec.v1.FlavorInstance`
        """
        self._flavor = flavor

    @property
    def metadata(self):
        """Gets the metadata of this Instance.

        边缘实例元数据。

        :return: The metadata of this Instance.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Instance.

        边缘实例元数据。

        :param metadata: The metadata of this Instance.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def security_groups(self):
        """Gets the security_groups of this Instance.

        边缘实例所属安全组列表。

        :return: The security_groups of this Instance.
        :rtype: list[:class:`huaweicloudsdkiec.v1.InstanceSecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this Instance.

        边缘实例所属安全组列表。

        :param security_groups: The security_groups of this Instance.
        :type security_groups: list[:class:`huaweicloudsdkiec.v1.InstanceSecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def progress(self):
        """Gets the progress of this Instance.

        边缘实例进度。

        :return: The progress of this Instance.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Instance.

        边缘实例进度。

        :param progress: The progress of this Instance.
        :type progress: int
        """
        self._progress = progress

    @property
    def os_ext_st_spower_state(self):
        """Gets the os_ext_st_spower_state of this Instance.

        扩展属性，边缘实例电源状态。

        :return: The os_ext_st_spower_state of this Instance.
        :rtype: int
        """
        return self._os_ext_st_spower_state

    @os_ext_st_spower_state.setter
    def os_ext_st_spower_state(self, os_ext_st_spower_state):
        """Sets the os_ext_st_spower_state of this Instance.

        扩展属性，边缘实例电源状态。

        :param os_ext_st_spower_state: The os_ext_st_spower_state of this Instance.
        :type os_ext_st_spower_state: int
        """
        self._os_ext_st_spower_state = os_ext_st_spower_state

    @property
    def os_ext_st_svm_state(self):
        """Gets the os_ext_st_svm_state of this Instance.

        扩展属性，边缘实例当前状态。

        :return: The os_ext_st_svm_state of this Instance.
        :rtype: str
        """
        return self._os_ext_st_svm_state

    @os_ext_st_svm_state.setter
    def os_ext_st_svm_state(self, os_ext_st_svm_state):
        """Sets the os_ext_st_svm_state of this Instance.

        扩展属性，边缘实例当前状态。

        :param os_ext_st_svm_state: The os_ext_st_svm_state of this Instance.
        :type os_ext_st_svm_state: str
        """
        self._os_ext_st_svm_state = os_ext_st_svm_state

    @property
    def os_ext_st_stask_state(self):
        """Gets the os_ext_st_stask_state of this Instance.

        边缘实例任务状态。

        :return: The os_ext_st_stask_state of this Instance.
        :rtype: str
        """
        return self._os_ext_st_stask_state

    @os_ext_st_stask_state.setter
    def os_ext_st_stask_state(self, os_ext_st_stask_state):
        """Sets the os_ext_st_stask_state of this Instance.

        边缘实例任务状态。

        :param os_ext_st_stask_state: The os_ext_st_stask_state of this Instance.
        :type os_ext_st_stask_state: str
        """
        self._os_ext_st_stask_state = os_ext_st_stask_state

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this Instance.

        扩展属性， diskConfig的类型。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。

        :return: The os_dc_fdisk_config of this Instance.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this Instance.

        扩展属性， diskConfig的类型。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this Instance.
        :type os_dc_fdisk_config: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def os_ext_a_zavailability_zone(self):
        """Gets the os_ext_a_zavailability_zone of this Instance.

        扩展属性，边缘实例所在可用区名称。

        :return: The os_ext_a_zavailability_zone of this Instance.
        :rtype: str
        """
        return self._os_ext_a_zavailability_zone

    @os_ext_a_zavailability_zone.setter
    def os_ext_a_zavailability_zone(self, os_ext_a_zavailability_zone):
        """Sets the os_ext_a_zavailability_zone of this Instance.

        扩展属性，边缘实例所在可用区名称。

        :param os_ext_a_zavailability_zone: The os_ext_a_zavailability_zone of this Instance.
        :type os_ext_a_zavailability_zone: str
        """
        self._os_ext_a_zavailability_zone = os_ext_a_zavailability_zone

    @property
    def os_srv_us_glaunched_at(self):
        """Gets the os_srv_us_glaunched_at of this Instance.

        边缘实例启动时间。 时间格式例如：2019-05-22T03:23:59.000000

        :return: The os_srv_us_glaunched_at of this Instance.
        :rtype: str
        """
        return self._os_srv_us_glaunched_at

    @os_srv_us_glaunched_at.setter
    def os_srv_us_glaunched_at(self, os_srv_us_glaunched_at):
        """Sets the os_srv_us_glaunched_at of this Instance.

        边缘实例启动时间。 时间格式例如：2019-05-22T03:23:59.000000

        :param os_srv_us_glaunched_at: The os_srv_us_glaunched_at of this Instance.
        :type os_srv_us_glaunched_at: str
        """
        self._os_srv_us_glaunched_at = os_srv_us_glaunched_at

    @property
    def os_srv_us_gterminated_at(self):
        """Gets the os_srv_us_gterminated_at of this Instance.

        边缘实例删除时间。 时间格式例如：2019-05-22T03:23:59.000000

        :return: The os_srv_us_gterminated_at of this Instance.
        :rtype: str
        """
        return self._os_srv_us_gterminated_at

    @os_srv_us_gterminated_at.setter
    def os_srv_us_gterminated_at(self, os_srv_us_gterminated_at):
        """Sets the os_srv_us_gterminated_at of this Instance.

        边缘实例删除时间。 时间格式例如：2019-05-22T03:23:59.000000

        :param os_srv_us_gterminated_at: The os_srv_us_gterminated_at of this Instance.
        :type os_srv_us_gterminated_at: str
        """
        self._os_srv_us_gterminated_at = os_srv_us_gterminated_at

    @property
    def os_ext_srv_att_rroot_device_name(self):
        """Gets the os_ext_srv_att_rroot_device_name of this Instance.

        边缘实例系统盘的设备名称。

        :return: The os_ext_srv_att_rroot_device_name of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_rroot_device_name

    @os_ext_srv_att_rroot_device_name.setter
    def os_ext_srv_att_rroot_device_name(self, os_ext_srv_att_rroot_device_name):
        """Sets the os_ext_srv_att_rroot_device_name of this Instance.

        边缘实例系统盘的设备名称。

        :param os_ext_srv_att_rroot_device_name: The os_ext_srv_att_rroot_device_name of this Instance.
        :type os_ext_srv_att_rroot_device_name: str
        """
        self._os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name

    @property
    def os_ext_srv_att_rramdisk_id(self):
        """Gets the os_ext_srv_att_rramdisk_id of this Instance.

        若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。

        :return: The os_ext_srv_att_rramdisk_id of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_rramdisk_id

    @os_ext_srv_att_rramdisk_id.setter
    def os_ext_srv_att_rramdisk_id(self, os_ext_srv_att_rramdisk_id):
        """Sets the os_ext_srv_att_rramdisk_id of this Instance.

        若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。

        :param os_ext_srv_att_rramdisk_id: The os_ext_srv_att_rramdisk_id of this Instance.
        :type os_ext_srv_att_rramdisk_id: str
        """
        self._os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id

    @property
    def os_ext_srv_att_rkernel_id(self):
        """Gets the os_ext_srv_att_rkernel_id of this Instance.

        若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空。

        :return: The os_ext_srv_att_rkernel_id of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_rkernel_id

    @os_ext_srv_att_rkernel_id.setter
    def os_ext_srv_att_rkernel_id(self, os_ext_srv_att_rkernel_id):
        """Sets the os_ext_srv_att_rkernel_id of this Instance.

        若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空。

        :param os_ext_srv_att_rkernel_id: The os_ext_srv_att_rkernel_id of this Instance.
        :type os_ext_srv_att_rkernel_id: str
        """
        self._os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id

    @property
    def os_ext_srv_att_rlaunch_index(self):
        """Gets the os_ext_srv_att_rlaunch_index of this Instance.

        批量创建场景，边缘实例的启动顺序。

        :return: The os_ext_srv_att_rlaunch_index of this Instance.
        :rtype: int
        """
        return self._os_ext_srv_att_rlaunch_index

    @os_ext_srv_att_rlaunch_index.setter
    def os_ext_srv_att_rlaunch_index(self, os_ext_srv_att_rlaunch_index):
        """Sets the os_ext_srv_att_rlaunch_index of this Instance.

        批量创建场景，边缘实例的启动顺序。

        :param os_ext_srv_att_rlaunch_index: The os_ext_srv_att_rlaunch_index of this Instance.
        :type os_ext_srv_att_rlaunch_index: int
        """
        self._os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index

    @property
    def os_ext_srv_att_rreservation_id(self):
        """Gets the os_ext_srv_att_rreservation_id of this Instance.

        批量创建场景，边缘实例的预留ID。

        :return: The os_ext_srv_att_rreservation_id of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_rreservation_id

    @os_ext_srv_att_rreservation_id.setter
    def os_ext_srv_att_rreservation_id(self, os_ext_srv_att_rreservation_id):
        """Sets the os_ext_srv_att_rreservation_id of this Instance.

        批量创建场景，边缘实例的预留ID。

        :param os_ext_srv_att_rreservation_id: The os_ext_srv_att_rreservation_id of this Instance.
        :type os_ext_srv_att_rreservation_id: str
        """
        self._os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id

    @property
    def os_ext_srv_att_rhostname(self):
        """Gets the os_ext_srv_att_rhostname of this Instance.

        边缘实例的主机名。

        :return: The os_ext_srv_att_rhostname of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_rhostname

    @os_ext_srv_att_rhostname.setter
    def os_ext_srv_att_rhostname(self, os_ext_srv_att_rhostname):
        """Sets the os_ext_srv_att_rhostname of this Instance.

        边缘实例的主机名。

        :param os_ext_srv_att_rhostname: The os_ext_srv_att_rhostname of this Instance.
        :type os_ext_srv_att_rhostname: str
        """
        self._os_ext_srv_att_rhostname = os_ext_srv_att_rhostname

    @property
    def os_ext_srv_att_ruser_data(self):
        """Gets the os_ext_srv_att_ruser_data of this Instance.

        创建边缘实例时指定的user_data。

        :return: The os_ext_srv_att_ruser_data of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_ruser_data

    @os_ext_srv_att_ruser_data.setter
    def os_ext_srv_att_ruser_data(self, os_ext_srv_att_ruser_data):
        """Sets the os_ext_srv_att_ruser_data of this Instance.

        创建边缘实例时指定的user_data。

        :param os_ext_srv_att_ruser_data: The os_ext_srv_att_ruser_data of this Instance.
        :type os_ext_srv_att_ruser_data: str
        """
        self._os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data

    @property
    def os_ext_srv_att_rhost(self):
        """Gets the os_ext_srv_att_rhost of this Instance.

        边缘实例所在主机的主机名称。

        :return: The os_ext_srv_att_rhost of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_rhost

    @os_ext_srv_att_rhost.setter
    def os_ext_srv_att_rhost(self, os_ext_srv_att_rhost):
        """Sets the os_ext_srv_att_rhost of this Instance.

        边缘实例所在主机的主机名称。

        :param os_ext_srv_att_rhost: The os_ext_srv_att_rhost of this Instance.
        :type os_ext_srv_att_rhost: str
        """
        self._os_ext_srv_att_rhost = os_ext_srv_att_rhost

    @property
    def os_ext_srv_att_rhypervisor_hostname(self):
        """Gets the os_ext_srv_att_rhypervisor_hostname of this Instance.

        扩展属性，边缘实例所在虚拟化主机名。

        :return: The os_ext_srv_att_rhypervisor_hostname of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_rhypervisor_hostname

    @os_ext_srv_att_rhypervisor_hostname.setter
    def os_ext_srv_att_rhypervisor_hostname(self, os_ext_srv_att_rhypervisor_hostname):
        """Sets the os_ext_srv_att_rhypervisor_hostname of this Instance.

        扩展属性，边缘实例所在虚拟化主机名。

        :param os_ext_srv_att_rhypervisor_hostname: The os_ext_srv_att_rhypervisor_hostname of this Instance.
        :type os_ext_srv_att_rhypervisor_hostname: str
        """
        self._os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname

    @property
    def os_extended_volumesvolumes_attached(self):
        """Gets the os_extended_volumesvolumes_attached of this Instance.

        挂载到边缘实例上的磁盘。

        :return: The os_extended_volumesvolumes_attached of this Instance.
        :rtype: list[:class:`huaweicloudsdkiec.v1.VolumesAttached`]
        """
        return self._os_extended_volumesvolumes_attached

    @os_extended_volumesvolumes_attached.setter
    def os_extended_volumesvolumes_attached(self, os_extended_volumesvolumes_attached):
        """Sets the os_extended_volumesvolumes_attached of this Instance.

        挂载到边缘实例上的磁盘。

        :param os_extended_volumesvolumes_attached: The os_extended_volumesvolumes_attached of this Instance.
        :type os_extended_volumesvolumes_attached: list[:class:`huaweicloudsdkiec.v1.VolumesAttached`]
        """
        self._os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached

    @property
    def geolocation(self):
        """Gets the geolocation of this Instance.


        :return: The geolocation of this Instance.
        :rtype: :class:`huaweicloudsdkiec.v1.GeoLocation`
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """Sets the geolocation of this Instance.


        :param geolocation: The geolocation of this Instance.
        :type geolocation: :class:`huaweicloudsdkiec.v1.GeoLocation`
        """
        self._geolocation = geolocation

    @property
    def edgecloud_id(self):
        """Gets the edgecloud_id of this Instance.

        边缘实例所属边缘业务的ID。

        :return: The edgecloud_id of this Instance.
        :rtype: str
        """
        return self._edgecloud_id

    @edgecloud_id.setter
    def edgecloud_id(self, edgecloud_id):
        """Sets the edgecloud_id of this Instance.

        边缘实例所属边缘业务的ID。

        :param edgecloud_id: The edgecloud_id of this Instance.
        :type edgecloud_id: str
        """
        self._edgecloud_id = edgecloud_id

    @property
    def edgecloud_name(self):
        """Gets the edgecloud_name of this Instance.

        边缘实例所属边缘业务的名称

        :return: The edgecloud_name of this Instance.
        :rtype: str
        """
        return self._edgecloud_name

    @edgecloud_name.setter
    def edgecloud_name(self, edgecloud_name):
        """Sets the edgecloud_name of this Instance.

        边缘实例所属边缘业务的名称

        :param edgecloud_name: The edgecloud_name of this Instance.
        :type edgecloud_name: str
        """
        self._edgecloud_name = edgecloud_name

    @property
    def domain_id(self):
        """Gets the domain_id of this Instance.

        帐号ID。

        :return: The domain_id of this Instance.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Instance.

        帐号ID。

        :param domain_id: The domain_id of this Instance.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def key_name(self):
        """Gets the key_name of this Instance.

        使用的密钥对名称。

        :return: The key_name of this Instance.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this Instance.

        使用的密钥对名称。

        :param key_name: The key_name of this Instance.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def os_ext_srv_att_rinstance_name(self):
        """Gets the os_ext_srv_att_rinstance_name of this Instance.

        扩展属性，边缘实例别名。

        :return: The os_ext_srv_att_rinstance_name of this Instance.
        :rtype: str
        """
        return self._os_ext_srv_att_rinstance_name

    @os_ext_srv_att_rinstance_name.setter
    def os_ext_srv_att_rinstance_name(self, os_ext_srv_att_rinstance_name):
        """Sets the os_ext_srv_att_rinstance_name of this Instance.

        扩展属性，边缘实例别名。

        :param os_ext_srv_att_rinstance_name: The os_ext_srv_att_rinstance_name of this Instance.
        :type os_ext_srv_att_rinstance_name: str
        """
        self._os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name

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
        if not isinstance(other, Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
