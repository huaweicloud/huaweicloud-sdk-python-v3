# coding: utf-8

import pprint
import re

import six





class ServerDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'updated': 'str',
        'host_id': 'str',
        'os_ext_srv_att_rhost': 'str',
        'addresses': 'dict(str, list[ServerAddress])',
        'key_name': 'str',
        'image': 'ServerImage',
        'os_ext_st_stask_state': 'str',
        'os_ext_st_svm_state': 'str',
        'os_ext_srv_att_rinstance_name': 'str',
        'os_ext_srv_att_rhypervisor_hostname': 'str',
        'flavor': 'ServerFlavor',
        'id': 'str',
        'security_groups': 'list[ServerSecurityGroup]',
        'os_ext_a_zavailability_zone': 'str',
        'user_id': 'str',
        'name': 'str',
        'created': 'str',
        'tenant_id': 'str',
        'os_dc_fdisk_config': 'str',
        'access_i_pv4': 'str',
        'access_i_pv6': 'str',
        'fault': 'ServerFault',
        'progress': 'int',
        'os_ext_st_spower_state': 'int',
        'config_drive': 'str',
        'metadata': 'dict(str, str)',
        'os_srv_us_glaunched_at': 'str',
        'os_srv_us_gterminated_at': 'str',
        'os_extended_volumesvolumes_attached': 'list[ServerExtendVolumeAttachment]',
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
        'osscheduler_hints': 'ServerSchedulerHints',
        'enterprise_project_id': 'str',
        'sys_tags': 'list[ServerSystemTag]'
    }

    attribute_map = {
        'status': 'status',
        'updated': 'updated',
        'host_id': 'hostId',
        'os_ext_srv_att_rhost': 'OS-EXT-SRV-ATTR:host',
        'addresses': 'addresses',
        'key_name': 'key_name',
        'image': 'image',
        'os_ext_st_stask_state': 'OS-EXT-STS:task_state',
        'os_ext_st_svm_state': 'OS-EXT-STS:vm_state',
        'os_ext_srv_att_rinstance_name': 'OS-EXT-SRV-ATTR:instance_name',
        'os_ext_srv_att_rhypervisor_hostname': 'OS-EXT-SRV-ATTR:hypervisor_hostname',
        'flavor': 'flavor',
        'id': 'id',
        'security_groups': 'security_groups',
        'os_ext_a_zavailability_zone': 'OS-EXT-AZ:availability_zone',
        'user_id': 'user_id',
        'name': 'name',
        'created': 'created',
        'tenant_id': 'tenant_id',
        'os_dc_fdisk_config': 'OS-DCF:diskConfig',
        'access_i_pv4': 'accessIPv4',
        'access_i_pv6': 'accessIPv6',
        'fault': 'fault',
        'progress': 'progress',
        'os_ext_st_spower_state': 'OS-EXT-STS:power_state',
        'config_drive': 'config_drive',
        'metadata': 'metadata',
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

    def __init__(self, status=None, updated=None, host_id=None, os_ext_srv_att_rhost=None, addresses=None, key_name=None, image=None, os_ext_st_stask_state=None, os_ext_st_svm_state=None, os_ext_srv_att_rinstance_name=None, os_ext_srv_att_rhypervisor_hostname=None, flavor=None, id=None, security_groups=None, os_ext_a_zavailability_zone=None, user_id=None, name=None, created=None, tenant_id=None, os_dc_fdisk_config=None, access_i_pv4=None, access_i_pv6=None, fault=None, progress=None, os_ext_st_spower_state=None, config_drive=None, metadata=None, os_srv_us_glaunched_at=None, os_srv_us_gterminated_at=None, os_extended_volumesvolumes_attached=None, description=None, host_status=None, os_ext_srv_att_rhostname=None, os_ext_srv_att_rreservation_id=None, os_ext_srv_att_rlaunch_index=None, os_ext_srv_att_rkernel_id=None, os_ext_srv_att_rramdisk_id=None, os_ext_srv_att_rroot_device_name=None, os_ext_srv_att_ruser_data=None, locked=None, tags=None, osscheduler_hints=None, enterprise_project_id=None, sys_tags=None):
        """ServerDetail - a model defined in huaweicloud sdk"""
        
        

        self._status = None
        self._updated = None
        self._host_id = None
        self._os_ext_srv_att_rhost = None
        self._addresses = None
        self._key_name = None
        self._image = None
        self._os_ext_st_stask_state = None
        self._os_ext_st_svm_state = None
        self._os_ext_srv_att_rinstance_name = None
        self._os_ext_srv_att_rhypervisor_hostname = None
        self._flavor = None
        self._id = None
        self._security_groups = None
        self._os_ext_a_zavailability_zone = None
        self._user_id = None
        self._name = None
        self._created = None
        self._tenant_id = None
        self._os_dc_fdisk_config = None
        self._access_i_pv4 = None
        self._access_i_pv6 = None
        self._fault = None
        self._progress = None
        self._os_ext_st_spower_state = None
        self._config_drive = None
        self._metadata = None
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

        self.status = status
        self.updated = updated
        self.host_id = host_id
        self.os_ext_srv_att_rhost = os_ext_srv_att_rhost
        self.addresses = addresses
        self.key_name = key_name
        self.image = image
        self.os_ext_st_stask_state = os_ext_st_stask_state
        self.os_ext_st_svm_state = os_ext_st_svm_state
        self.os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name
        self.os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname
        self.flavor = flavor
        self.id = id
        self.security_groups = security_groups
        self.os_ext_a_zavailability_zone = os_ext_a_zavailability_zone
        self.user_id = user_id
        self.name = name
        self.created = created
        self.tenant_id = tenant_id
        if os_dc_fdisk_config is not None:
            self.os_dc_fdisk_config = os_dc_fdisk_config
        self.access_i_pv4 = access_i_pv4
        self.access_i_pv6 = access_i_pv6
        if fault is not None:
            self.fault = fault
        if progress is not None:
            self.progress = progress
        self.os_ext_st_spower_state = os_ext_st_spower_state
        self.config_drive = config_drive
        self.metadata = metadata
        self.os_srv_us_glaunched_at = os_srv_us_glaunched_at
        self.os_srv_us_gterminated_at = os_srv_us_gterminated_at
        self.os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached
        if description is not None:
            self.description = description
        self.host_status = host_status
        self.os_ext_srv_att_rhostname = os_ext_srv_att_rhostname
        if os_ext_srv_att_rreservation_id is not None:
            self.os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id
        self.os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index
        self.os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id
        self.os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id
        self.os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name
        if os_ext_srv_att_ruser_data is not None:
            self.os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data
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
    def status(self):
        """Gets the status of this ServerDetail.

        弹性云服务器状态。  取值范围：  ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE

        :return: The status of this ServerDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ServerDetail.

        弹性云服务器状态。  取值范围：  ACTIVE、BUILD、DELETED、ERROR、HARD_REBOOT、MIGRATING、PAUSED、REBOOT、REBUILD、RESIZE、REVERT_RESIZE、SHUTOFF、SHELVED、SHELVED_OFFLOADED、SOFT_DELETED、SUSPENDED、VERIFY_RESIZE

        :param status: The status of this ServerDetail.
        :type: str
        """
        self._status = status

    @property
    def updated(self):
        """Gets the updated of this ServerDetail.

        弹性云服务器更新时间。  时间格式例如：2019-05-22T03:30:52Z

        :return: The updated of this ServerDetail.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ServerDetail.

        弹性云服务器更新时间。  时间格式例如：2019-05-22T03:30:52Z

        :param updated: The updated of this ServerDetail.
        :type: str
        """
        self._updated = updated

    @property
    def host_id(self):
        """Gets the host_id of this ServerDetail.

        弹性云服务器所在主机的主机ID。

        :return: The host_id of this ServerDetail.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this ServerDetail.

        弹性云服务器所在主机的主机ID。

        :param host_id: The host_id of this ServerDetail.
        :type: str
        """
        self._host_id = host_id

    @property
    def os_ext_srv_att_rhost(self):
        """Gets the os_ext_srv_att_rhost of this ServerDetail.

        弹性云服务器所在主机的主机名称。

        :return: The os_ext_srv_att_rhost of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rhost

    @os_ext_srv_att_rhost.setter
    def os_ext_srv_att_rhost(self, os_ext_srv_att_rhost):
        """Sets the os_ext_srv_att_rhost of this ServerDetail.

        弹性云服务器所在主机的主机名称。

        :param os_ext_srv_att_rhost: The os_ext_srv_att_rhost of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_rhost = os_ext_srv_att_rhost

    @property
    def addresses(self):
        """Gets the addresses of this ServerDetail.

        弹性云服务器的网络属性。

        :return: The addresses of this ServerDetail.
        :rtype: dict(str, list[ServerAddress])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ServerDetail.

        弹性云服务器的网络属性。

        :param addresses: The addresses of this ServerDetail.
        :type: dict(str, list[ServerAddress])
        """
        self._addresses = addresses

    @property
    def key_name(self):
        """Gets the key_name of this ServerDetail.

        弹性云服务器使用的密钥对名称。

        :return: The key_name of this ServerDetail.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this ServerDetail.

        弹性云服务器使用的密钥对名称。

        :param key_name: The key_name of this ServerDetail.
        :type: str
        """
        self._key_name = key_name

    @property
    def image(self):
        """Gets the image of this ServerDetail.


        :return: The image of this ServerDetail.
        :rtype: ServerImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ServerDetail.


        :param image: The image of this ServerDetail.
        :type: ServerImage
        """
        self._image = image

    @property
    def os_ext_st_stask_state(self):
        """Gets the os_ext_st_stask_state of this ServerDetail.

        扩展属性，弹性云服务器当前任务的状态。

        :return: The os_ext_st_stask_state of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_st_stask_state

    @os_ext_st_stask_state.setter
    def os_ext_st_stask_state(self, os_ext_st_stask_state):
        """Sets the os_ext_st_stask_state of this ServerDetail.

        扩展属性，弹性云服务器当前任务的状态。

        :param os_ext_st_stask_state: The os_ext_st_stask_state of this ServerDetail.
        :type: str
        """
        self._os_ext_st_stask_state = os_ext_st_stask_state

    @property
    def os_ext_st_svm_state(self):
        """Gets the os_ext_st_svm_state of this ServerDetail.

        扩展属性，弹性云服务器当前状态。

        :return: The os_ext_st_svm_state of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_st_svm_state

    @os_ext_st_svm_state.setter
    def os_ext_st_svm_state(self, os_ext_st_svm_state):
        """Sets the os_ext_st_svm_state of this ServerDetail.

        扩展属性，弹性云服务器当前状态。

        :param os_ext_st_svm_state: The os_ext_st_svm_state of this ServerDetail.
        :type: str
        """
        self._os_ext_st_svm_state = os_ext_st_svm_state

    @property
    def os_ext_srv_att_rinstance_name(self):
        """Gets the os_ext_srv_att_rinstance_name of this ServerDetail.

        扩展属性，弹性云服务器别名。

        :return: The os_ext_srv_att_rinstance_name of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rinstance_name

    @os_ext_srv_att_rinstance_name.setter
    def os_ext_srv_att_rinstance_name(self, os_ext_srv_att_rinstance_name):
        """Sets the os_ext_srv_att_rinstance_name of this ServerDetail.

        扩展属性，弹性云服务器别名。

        :param os_ext_srv_att_rinstance_name: The os_ext_srv_att_rinstance_name of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_rinstance_name = os_ext_srv_att_rinstance_name

    @property
    def os_ext_srv_att_rhypervisor_hostname(self):
        """Gets the os_ext_srv_att_rhypervisor_hostname of this ServerDetail.

        扩展属性，弹性云服务器所在虚拟化主机名。

        :return: The os_ext_srv_att_rhypervisor_hostname of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rhypervisor_hostname

    @os_ext_srv_att_rhypervisor_hostname.setter
    def os_ext_srv_att_rhypervisor_hostname(self, os_ext_srv_att_rhypervisor_hostname):
        """Sets the os_ext_srv_att_rhypervisor_hostname of this ServerDetail.

        扩展属性，弹性云服务器所在虚拟化主机名。

        :param os_ext_srv_att_rhypervisor_hostname: The os_ext_srv_att_rhypervisor_hostname of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_rhypervisor_hostname = os_ext_srv_att_rhypervisor_hostname

    @property
    def flavor(self):
        """Gets the flavor of this ServerDetail.


        :return: The flavor of this ServerDetail.
        :rtype: ServerFlavor
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this ServerDetail.


        :param flavor: The flavor of this ServerDetail.
        :type: ServerFlavor
        """
        self._flavor = flavor

    @property
    def id(self):
        """Gets the id of this ServerDetail.

        弹性云服务器ID，格式为UUID。

        :return: The id of this ServerDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerDetail.

        弹性云服务器ID，格式为UUID。

        :param id: The id of this ServerDetail.
        :type: str
        """
        self._id = id

    @property
    def security_groups(self):
        """Gets the security_groups of this ServerDetail.

        弹性云服务器所属安全组列表。

        :return: The security_groups of this ServerDetail.
        :rtype: list[ServerSecurityGroup]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ServerDetail.

        弹性云服务器所属安全组列表。

        :param security_groups: The security_groups of this ServerDetail.
        :type: list[ServerSecurityGroup]
        """
        self._security_groups = security_groups

    @property
    def os_ext_a_zavailability_zone(self):
        """Gets the os_ext_a_zavailability_zone of this ServerDetail.

        扩展属性，弹性云服务器所在可用区名称。

        :return: The os_ext_a_zavailability_zone of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_a_zavailability_zone

    @os_ext_a_zavailability_zone.setter
    def os_ext_a_zavailability_zone(self, os_ext_a_zavailability_zone):
        """Sets the os_ext_a_zavailability_zone of this ServerDetail.

        扩展属性，弹性云服务器所在可用区名称。

        :param os_ext_a_zavailability_zone: The os_ext_a_zavailability_zone of this ServerDetail.
        :type: str
        """
        self._os_ext_a_zavailability_zone = os_ext_a_zavailability_zone

    @property
    def user_id(self):
        """Gets the user_id of this ServerDetail.

        创建弹性云服务器的用户ID，格式为UUID。

        :return: The user_id of this ServerDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ServerDetail.

        创建弹性云服务器的用户ID，格式为UUID。

        :param user_id: The user_id of this ServerDetail.
        :type: str
        """
        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this ServerDetail.

        弹性云服务器名称。

        :return: The name of this ServerDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ServerDetail.

        弹性云服务器名称。

        :param name: The name of this ServerDetail.
        :type: str
        """
        self._name = name

    @property
    def created(self):
        """Gets the created of this ServerDetail.

        弹性云服务器创建时间。  时间格式例如：2019-05-22T03:19:19Z

        :return: The created of this ServerDetail.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ServerDetail.

        弹性云服务器创建时间。  时间格式例如：2019-05-22T03:19:19Z

        :param created: The created of this ServerDetail.
        :type: str
        """
        self._created = created

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ServerDetail.

        弹性云服务器所属租户ID，即项目id，和project_id表示相同的概念，格式为UUID。

        :return: The tenant_id of this ServerDetail.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ServerDetail.

        弹性云服务器所属租户ID，即项目id，和project_id表示相同的概念，格式为UUID。

        :param tenant_id: The tenant_id of this ServerDetail.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def os_dc_fdisk_config(self):
        """Gets the os_dc_fdisk_config of this ServerDetail.

        扩展属性， diskConfig的类型。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。

        :return: The os_dc_fdisk_config of this ServerDetail.
        :rtype: str
        """
        return self._os_dc_fdisk_config

    @os_dc_fdisk_config.setter
    def os_dc_fdisk_config(self, os_dc_fdisk_config):
        """Sets the os_dc_fdisk_config of this ServerDetail.

        扩展属性， diskConfig的类型。  - MANUAL，镜像空间不会扩展。 - AUTO，系统盘镜像空间会自动扩展为与flavor大小一致。

        :param os_dc_fdisk_config: The os_dc_fdisk_config of this ServerDetail.
        :type: str
        """
        self._os_dc_fdisk_config = os_dc_fdisk_config

    @property
    def access_i_pv4(self):
        """Gets the access_i_pv4 of this ServerDetail.

        预留属性。

        :return: The access_i_pv4 of this ServerDetail.
        :rtype: str
        """
        return self._access_i_pv4

    @access_i_pv4.setter
    def access_i_pv4(self, access_i_pv4):
        """Sets the access_i_pv4 of this ServerDetail.

        预留属性。

        :param access_i_pv4: The access_i_pv4 of this ServerDetail.
        :type: str
        """
        self._access_i_pv4 = access_i_pv4

    @property
    def access_i_pv6(self):
        """Gets the access_i_pv6 of this ServerDetail.

        预留属性。

        :return: The access_i_pv6 of this ServerDetail.
        :rtype: str
        """
        return self._access_i_pv6

    @access_i_pv6.setter
    def access_i_pv6(self, access_i_pv6):
        """Sets the access_i_pv6 of this ServerDetail.

        预留属性。

        :param access_i_pv6: The access_i_pv6 of this ServerDetail.
        :type: str
        """
        self._access_i_pv6 = access_i_pv6

    @property
    def fault(self):
        """Gets the fault of this ServerDetail.


        :return: The fault of this ServerDetail.
        :rtype: ServerFault
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        """Sets the fault of this ServerDetail.


        :param fault: The fault of this ServerDetail.
        :type: ServerFault
        """
        self._fault = fault

    @property
    def progress(self):
        """Gets the progress of this ServerDetail.

        弹性云服务器进度。

        :return: The progress of this ServerDetail.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ServerDetail.

        弹性云服务器进度。

        :param progress: The progress of this ServerDetail.
        :type: int
        """
        self._progress = progress

    @property
    def os_ext_st_spower_state(self):
        """Gets the os_ext_st_spower_state of this ServerDetail.

        扩展属性，弹性云服务器电源状态。

        :return: The os_ext_st_spower_state of this ServerDetail.
        :rtype: int
        """
        return self._os_ext_st_spower_state

    @os_ext_st_spower_state.setter
    def os_ext_st_spower_state(self, os_ext_st_spower_state):
        """Sets the os_ext_st_spower_state of this ServerDetail.

        扩展属性，弹性云服务器电源状态。

        :param os_ext_st_spower_state: The os_ext_st_spower_state of this ServerDetail.
        :type: int
        """
        self._os_ext_st_spower_state = os_ext_st_spower_state

    @property
    def config_drive(self):
        """Gets the config_drive of this ServerDetail.

        config drive信息。

        :return: The config_drive of this ServerDetail.
        :rtype: str
        """
        return self._config_drive

    @config_drive.setter
    def config_drive(self, config_drive):
        """Sets the config_drive of this ServerDetail.

        config drive信息。

        :param config_drive: The config_drive of this ServerDetail.
        :type: str
        """
        self._config_drive = config_drive

    @property
    def metadata(self):
        """Gets the metadata of this ServerDetail.

        弹性云服务器元数据。  > 说明： >  > 元数据包含系统默认添加字段和用户设置的字段。  系统默认添加字段  1. charging_mode 云服务器的计费类型。  - “0”：按需计费（即postPaid-后付费方式）。 - “1”：按包年包月计费（即prePaid-预付费方式）。\"2\"：竞价实例计费  2. metering.order_id 按“包年/包月”计费的云服务器对应的订单ID。  3. metering.product_id 按“包年/包月”计费的云服务器对应的产品ID。  4. vpc_id 云服务器所属的虚拟私有云ID。  5. EcmResStatus 云服务器的冻结状态。  - normal：云服务器正常状态（未被冻结）。 - freeze：云服务器被冻结。  > 当云服务器被冻结或者解冻后，系统默认添加该字段，且该字段必选。  6. metering.image_id 云服务器操作系统对应的镜像ID  7.  metering.imagetype 镜像类型，目前支持：  - 公共镜像（gold） - 私有镜像（private） - 共享镜像（shared）  8. metering.resourcespeccode 云服务器对应的资源规格。  9. image_name 云服务器操作系统对应的镜像名称。  10. os_bit 操作系统位数，一般取值为“32”或者“64”。  11. lockCheckEndpoint 回调URL，用于检查弹性云服务器的加锁是否有效。  - 如果有效，则云服务器保持锁定状态。 - 如果无效，解除锁定状态，删除失效的锁。  12. lockSource 弹性云服务器来自哪个服务。订单加锁（ORDER）  13. lockSourceId 弹性云服务器的加锁来自哪个ID。lockSource为“ORDER”时，lockSourceId为订单ID。  14. lockScene 弹性云服务器的加锁类型。  - 按需转包周期（TO_PERIOD_LOCK）  15. virtual_env_type  - IOS镜像创建虚拟机，\"virtual_env_type\": \"IsoImage\" 属性； - 非IOS镜像创建虚拟机，在19.5.0版本以后创建的虚拟机将不会添加virtual_env_type 属性，而在此之前的版本创建的虚拟机可能会返回\"virtual_env_type\": \"FusionCompute\"属性 。  > virtual_env_type属性不允许用户增加、删除和修改。  16. metering.resourcetype 云服务器对应的资源类型。  17. os_type 操作系统类型，取值为：Linux、Windows。  18. cascaded.instance_extrainfo 系统内部虚拟机扩展信息。  19. __support_agent_list 云服务器是否支持企业主机安全、主机监控。  - “hss”：企业主机安全 -  “ces”：主机监控  20. agency_name 委托的名称。  委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。

        :return: The metadata of this ServerDetail.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ServerDetail.

        弹性云服务器元数据。  > 说明： >  > 元数据包含系统默认添加字段和用户设置的字段。  系统默认添加字段  1. charging_mode 云服务器的计费类型。  - “0”：按需计费（即postPaid-后付费方式）。 - “1”：按包年包月计费（即prePaid-预付费方式）。\"2\"：竞价实例计费  2. metering.order_id 按“包年/包月”计费的云服务器对应的订单ID。  3. metering.product_id 按“包年/包月”计费的云服务器对应的产品ID。  4. vpc_id 云服务器所属的虚拟私有云ID。  5. EcmResStatus 云服务器的冻结状态。  - normal：云服务器正常状态（未被冻结）。 - freeze：云服务器被冻结。  > 当云服务器被冻结或者解冻后，系统默认添加该字段，且该字段必选。  6. metering.image_id 云服务器操作系统对应的镜像ID  7.  metering.imagetype 镜像类型，目前支持：  - 公共镜像（gold） - 私有镜像（private） - 共享镜像（shared）  8. metering.resourcespeccode 云服务器对应的资源规格。  9. image_name 云服务器操作系统对应的镜像名称。  10. os_bit 操作系统位数，一般取值为“32”或者“64”。  11. lockCheckEndpoint 回调URL，用于检查弹性云服务器的加锁是否有效。  - 如果有效，则云服务器保持锁定状态。 - 如果无效，解除锁定状态，删除失效的锁。  12. lockSource 弹性云服务器来自哪个服务。订单加锁（ORDER）  13. lockSourceId 弹性云服务器的加锁来自哪个ID。lockSource为“ORDER”时，lockSourceId为订单ID。  14. lockScene 弹性云服务器的加锁类型。  - 按需转包周期（TO_PERIOD_LOCK）  15. virtual_env_type  - IOS镜像创建虚拟机，\"virtual_env_type\": \"IsoImage\" 属性； - 非IOS镜像创建虚拟机，在19.5.0版本以后创建的虚拟机将不会添加virtual_env_type 属性，而在此之前的版本创建的虚拟机可能会返回\"virtual_env_type\": \"FusionCompute\"属性 。  > virtual_env_type属性不允许用户增加、删除和修改。  16. metering.resourcetype 云服务器对应的资源类型。  17. os_type 操作系统类型，取值为：Linux、Windows。  18. cascaded.instance_extrainfo 系统内部虚拟机扩展信息。  19. __support_agent_list 云服务器是否支持企业主机安全、主机监控。  - “hss”：企业主机安全 -  “ces”：主机监控  20. agency_name 委托的名称。  委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。

        :param metadata: The metadata of this ServerDetail.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def os_srv_us_glaunched_at(self):
        """Gets the os_srv_us_glaunched_at of this ServerDetail.

        弹性云服务器启动时间。时间格式例如：2019-05-22T03:23:59.000000

        :return: The os_srv_us_glaunched_at of this ServerDetail.
        :rtype: str
        """
        return self._os_srv_us_glaunched_at

    @os_srv_us_glaunched_at.setter
    def os_srv_us_glaunched_at(self, os_srv_us_glaunched_at):
        """Sets the os_srv_us_glaunched_at of this ServerDetail.

        弹性云服务器启动时间。时间格式例如：2019-05-22T03:23:59.000000

        :param os_srv_us_glaunched_at: The os_srv_us_glaunched_at of this ServerDetail.
        :type: str
        """
        self._os_srv_us_glaunched_at = os_srv_us_glaunched_at

    @property
    def os_srv_us_gterminated_at(self):
        """Gets the os_srv_us_gterminated_at of this ServerDetail.

        弹性云服务器删除时间。  时间格式例如：2019-05-22T03:23:59.000000

        :return: The os_srv_us_gterminated_at of this ServerDetail.
        :rtype: str
        """
        return self._os_srv_us_gterminated_at

    @os_srv_us_gterminated_at.setter
    def os_srv_us_gterminated_at(self, os_srv_us_gterminated_at):
        """Sets the os_srv_us_gterminated_at of this ServerDetail.

        弹性云服务器删除时间。  时间格式例如：2019-05-22T03:23:59.000000

        :param os_srv_us_gterminated_at: The os_srv_us_gterminated_at of this ServerDetail.
        :type: str
        """
        self._os_srv_us_gterminated_at = os_srv_us_gterminated_at

    @property
    def os_extended_volumesvolumes_attached(self):
        """Gets the os_extended_volumesvolumes_attached of this ServerDetail.

        挂载到弹性云服务器上的磁盘。

        :return: The os_extended_volumesvolumes_attached of this ServerDetail.
        :rtype: list[ServerExtendVolumeAttachment]
        """
        return self._os_extended_volumesvolumes_attached

    @os_extended_volumesvolumes_attached.setter
    def os_extended_volumesvolumes_attached(self, os_extended_volumesvolumes_attached):
        """Sets the os_extended_volumesvolumes_attached of this ServerDetail.

        挂载到弹性云服务器上的磁盘。

        :param os_extended_volumesvolumes_attached: The os_extended_volumesvolumes_attached of this ServerDetail.
        :type: list[ServerExtendVolumeAttachment]
        """
        self._os_extended_volumesvolumes_attached = os_extended_volumesvolumes_attached

    @property
    def description(self):
        """Gets the description of this ServerDetail.

        弹性云服务器的描述信息。

        :return: The description of this ServerDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServerDetail.

        弹性云服务器的描述信息。

        :param description: The description of this ServerDetail.
        :type: str
        """
        self._description = description

    @property
    def host_status(self):
        """Gets the host_status of this ServerDetail.

        nova-compute状态。  - UP：服务正常 - UNKNOWN：状态未知 - DOWN：服务异常 - MAINTENANCE：维护状态 - 空字符串：弹性云服务器无主机信息

        :return: The host_status of this ServerDetail.
        :rtype: str
        """
        return self._host_status

    @host_status.setter
    def host_status(self, host_status):
        """Sets the host_status of this ServerDetail.

        nova-compute状态。  - UP：服务正常 - UNKNOWN：状态未知 - DOWN：服务异常 - MAINTENANCE：维护状态 - 空字符串：弹性云服务器无主机信息

        :param host_status: The host_status of this ServerDetail.
        :type: str
        """
        self._host_status = host_status

    @property
    def os_ext_srv_att_rhostname(self):
        """Gets the os_ext_srv_att_rhostname of this ServerDetail.

        弹性云服务器的主机名。

        :return: The os_ext_srv_att_rhostname of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rhostname

    @os_ext_srv_att_rhostname.setter
    def os_ext_srv_att_rhostname(self, os_ext_srv_att_rhostname):
        """Sets the os_ext_srv_att_rhostname of this ServerDetail.

        弹性云服务器的主机名。

        :param os_ext_srv_att_rhostname: The os_ext_srv_att_rhostname of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_rhostname = os_ext_srv_att_rhostname

    @property
    def os_ext_srv_att_rreservation_id(self):
        """Gets the os_ext_srv_att_rreservation_id of this ServerDetail.

        批量创建场景，弹性云服务器的预留ID。

        :return: The os_ext_srv_att_rreservation_id of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rreservation_id

    @os_ext_srv_att_rreservation_id.setter
    def os_ext_srv_att_rreservation_id(self, os_ext_srv_att_rreservation_id):
        """Sets the os_ext_srv_att_rreservation_id of this ServerDetail.

        批量创建场景，弹性云服务器的预留ID。

        :param os_ext_srv_att_rreservation_id: The os_ext_srv_att_rreservation_id of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_rreservation_id = os_ext_srv_att_rreservation_id

    @property
    def os_ext_srv_att_rlaunch_index(self):
        """Gets the os_ext_srv_att_rlaunch_index of this ServerDetail.

        批量创建场景，弹性云服务器的启动顺序。

        :return: The os_ext_srv_att_rlaunch_index of this ServerDetail.
        :rtype: int
        """
        return self._os_ext_srv_att_rlaunch_index

    @os_ext_srv_att_rlaunch_index.setter
    def os_ext_srv_att_rlaunch_index(self, os_ext_srv_att_rlaunch_index):
        """Sets the os_ext_srv_att_rlaunch_index of this ServerDetail.

        批量创建场景，弹性云服务器的启动顺序。

        :param os_ext_srv_att_rlaunch_index: The os_ext_srv_att_rlaunch_index of this ServerDetail.
        :type: int
        """
        self._os_ext_srv_att_rlaunch_index = os_ext_srv_att_rlaunch_index

    @property
    def os_ext_srv_att_rkernel_id(self):
        """Gets the os_ext_srv_att_rkernel_id of this ServerDetail.

        若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空。

        :return: The os_ext_srv_att_rkernel_id of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rkernel_id

    @os_ext_srv_att_rkernel_id.setter
    def os_ext_srv_att_rkernel_id(self, os_ext_srv_att_rkernel_id):
        """Sets the os_ext_srv_att_rkernel_id of this ServerDetail.

        若使用AMI格式的镜像，则表示kernel image的UUID；否则，留空。

        :param os_ext_srv_att_rkernel_id: The os_ext_srv_att_rkernel_id of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_rkernel_id = os_ext_srv_att_rkernel_id

    @property
    def os_ext_srv_att_rramdisk_id(self):
        """Gets the os_ext_srv_att_rramdisk_id of this ServerDetail.

        若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。

        :return: The os_ext_srv_att_rramdisk_id of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rramdisk_id

    @os_ext_srv_att_rramdisk_id.setter
    def os_ext_srv_att_rramdisk_id(self, os_ext_srv_att_rramdisk_id):
        """Sets the os_ext_srv_att_rramdisk_id of this ServerDetail.

        若使用AMI格式镜像，则表示ramdisk image的UUID；否则，留空。

        :param os_ext_srv_att_rramdisk_id: The os_ext_srv_att_rramdisk_id of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_rramdisk_id = os_ext_srv_att_rramdisk_id

    @property
    def os_ext_srv_att_rroot_device_name(self):
        """Gets the os_ext_srv_att_rroot_device_name of this ServerDetail.

        弹性云服务器系统盘的设备名称。

        :return: The os_ext_srv_att_rroot_device_name of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_rroot_device_name

    @os_ext_srv_att_rroot_device_name.setter
    def os_ext_srv_att_rroot_device_name(self, os_ext_srv_att_rroot_device_name):
        """Sets the os_ext_srv_att_rroot_device_name of this ServerDetail.

        弹性云服务器系统盘的设备名称。

        :param os_ext_srv_att_rroot_device_name: The os_ext_srv_att_rroot_device_name of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_rroot_device_name = os_ext_srv_att_rroot_device_name

    @property
    def os_ext_srv_att_ruser_data(self):
        """Gets the os_ext_srv_att_ruser_data of this ServerDetail.

        创建弹性云服务器时指定的user_data。

        :return: The os_ext_srv_att_ruser_data of this ServerDetail.
        :rtype: str
        """
        return self._os_ext_srv_att_ruser_data

    @os_ext_srv_att_ruser_data.setter
    def os_ext_srv_att_ruser_data(self, os_ext_srv_att_ruser_data):
        """Sets the os_ext_srv_att_ruser_data of this ServerDetail.

        创建弹性云服务器时指定的user_data。

        :param os_ext_srv_att_ruser_data: The os_ext_srv_att_ruser_data of this ServerDetail.
        :type: str
        """
        self._os_ext_srv_att_ruser_data = os_ext_srv_att_ruser_data

    @property
    def locked(self):
        """Gets the locked of this ServerDetail.

        弹性云服务器是否为锁定状态。  - true：锁定 - false：未锁定

        :return: The locked of this ServerDetail.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this ServerDetail.

        弹性云服务器是否为锁定状态。  - true：锁定 - false：未锁定

        :param locked: The locked of this ServerDetail.
        :type: bool
        """
        self._locked = locked

    @property
    def tags(self):
        """Gets the tags of this ServerDetail.

        弹性云服务器标签。

        :return: The tags of this ServerDetail.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ServerDetail.

        弹性云服务器标签。

        :param tags: The tags of this ServerDetail.
        :type: list[str]
        """
        self._tags = tags

    @property
    def osscheduler_hints(self):
        """Gets the osscheduler_hints of this ServerDetail.


        :return: The osscheduler_hints of this ServerDetail.
        :rtype: ServerSchedulerHints
        """
        return self._osscheduler_hints

    @osscheduler_hints.setter
    def osscheduler_hints(self, osscheduler_hints):
        """Sets the osscheduler_hints of this ServerDetail.


        :param osscheduler_hints: The osscheduler_hints of this ServerDetail.
        :type: ServerSchedulerHints
        """
        self._osscheduler_hints = osscheduler_hints

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ServerDetail.

        弹性云服务器所属的企业项目ID。

        :return: The enterprise_project_id of this ServerDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ServerDetail.

        弹性云服务器所属的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ServerDetail.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def sys_tags(self):
        """Gets the sys_tags of this ServerDetail.

        弹性云服务器系统标签。

        :return: The sys_tags of this ServerDetail.
        :rtype: list[ServerSystemTag]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this ServerDetail.

        弹性云服务器系统标签。

        :param sys_tags: The sys_tags of this ServerDetail.
        :type: list[ServerSystemTag]
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServerDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
