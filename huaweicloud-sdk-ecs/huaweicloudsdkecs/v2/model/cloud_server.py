# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloudServer:

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
        'tenant_id': 'str',
        'user_id': 'str',
        'market_info': 'MarketModel',
        'availability_zone': 'str',
        'vm_state': 'str',
        'task_state': 'str',
        'power_state': 'int',
        'created': 'str',
        'in_recycle_bin': 'bool',
        'spod_id': 'str',
        'updated': 'str',
        'launched_at': 'str',
        'description': 'str',
        'key_name': 'str',
        'locked': 'bool',
        'root_device_name': 'str',
        'tenancy': 'str',
        'dedicated_host_id': 'str',
        'enterprise_project_id': 'str',
        'metadata': 'dict(str, str)',
        'tags': 'list[str]',
        'addresses': 'dict(str, list[NetworkAddresses])',
        'security_groups': 'list[SecurityGroup]',
        'volumes_attached': 'list[VolumeAttach]',
        'image': 'Image',
        'flavor': 'FlavorQuasar',
        'fault': 'Fault',
        'cpu_options': 'CpuOptions'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'tenant_id': 'tenant_id',
        'user_id': 'user_id',
        'market_info': 'market_info',
        'availability_zone': 'availability_zone',
        'vm_state': 'vm_state',
        'task_state': 'task_state',
        'power_state': 'power_state',
        'created': 'created',
        'in_recycle_bin': 'in_recycle_bin',
        'spod_id': 'spod_id',
        'updated': 'updated',
        'launched_at': 'launched_at',
        'description': 'description',
        'key_name': 'key_name',
        'locked': 'locked',
        'root_device_name': 'root_device_name',
        'tenancy': 'tenancy',
        'dedicated_host_id': 'dedicated_host_id',
        'enterprise_project_id': 'enterprise_project_id',
        'metadata': 'metadata',
        'tags': 'tags',
        'addresses': 'addresses',
        'security_groups': 'security_groups',
        'volumes_attached': 'volumes_attached',
        'image': 'image',
        'flavor': 'flavor',
        'fault': 'fault',
        'cpu_options': 'cpu_options'
    }

    def __init__(self, id=None, name=None, status=None, tenant_id=None, user_id=None, market_info=None, availability_zone=None, vm_state=None, task_state=None, power_state=None, created=None, in_recycle_bin=None, spod_id=None, updated=None, launched_at=None, description=None, key_name=None, locked=None, root_device_name=None, tenancy=None, dedicated_host_id=None, enterprise_project_id=None, metadata=None, tags=None, addresses=None, security_groups=None, volumes_attached=None, image=None, flavor=None, fault=None, cpu_options=None):
        r"""CloudServer

        The model defined in huaweicloud sdk

        :param id: 云服务器唯一标识。
        :type id: str
        :param name: 云服务器名称。
        :type name: str
        :param status: 云服务器当前状态信息。
        :type status: str
        :param tenant_id: 云服务器所属租户ID。即项目id，与project_id表示相同的概念。
        :type tenant_id: str
        :param user_id: 云服务器所属用户ID。
        :type user_id: str
        :param market_info: 
        :type market_info: :class:`huaweicloudsdkecs.v2.MarketModel`
        :param availability_zone: 可用分区
        :type availability_zone: str
        :param vm_state: 云服务器的状态。
        :type vm_state: str
        :param task_state: 云服务器任务状态。
        :type task_state: str
        :param power_state: 云服务器电源状态。
        :type power_state: int
        :param created: 云服务器创建时间。 时间格式例如：2020-05-22T07:48:53Z。
        :type created: str
        :param in_recycle_bin: 云服务器是否处于回收站中
        :type in_recycle_bin: bool
        :param spod_id: 共池裸机按整机柜发放的同一批次的批创ID
        :type spod_id: str
        :param updated: 云服务器上一次更新时间。时间格式例如：2020-05-22T07:48:53Z
        :type updated: str
        :param launched_at: 云服务器启动时间。时间格式例如：2020-05-22T07:48:53.000000。
        :type launched_at: str
        :param description: 云服务器的描述信息。
        :type description: str
        :param key_name: 云服务器使用的密钥对名称。
        :type key_name: str
        :param locked: 云服务器是否为锁定状态。  true：锁定 false：未锁定
        :type locked: bool
        :param root_device_name: 云服务器系统盘的设备名称，例如当系统盘的磁盘模式是VDB时，为/dev/vda。
        :type root_device_name: str
        :param tenancy: 在专属主机或共享池中创建云服务器。默认为在共享池创建。值为： shared或dedicated。  shared：表示共享池。 dedicated:表示专属主机。
        :type tenancy: str
        :param dedicated_host_id: 专属主机ID。此属性仅在tenancy值为dedicated时有效，不指定此属性，系统将自动分配租户可自动放置云服务器的专属主机。
        :type dedicated_host_id: str
        :param enterprise_project_id: 查询绑定某个企业项目的云服务器。 若需要查询当前用户所有企业项目绑定的云服务，请传参all_granted_eps。
        :type enterprise_project_id: str
        :param metadata: 云服务器元数据。
        :type metadata: dict(str, str)
        :param tags: 云服务器的标签列表。
        :type tags: list[str]
        :param addresses: 云服务器对应的网络地址信息。
        :type addresses: dict(str, list[NetworkAddresses])
        :param security_groups: 云服务器的安全组信息。
        :type security_groups: list[:class:`huaweicloudsdkecs.v2.SecurityGroup`]
        :param volumes_attached: 云服务器挂载磁盘信息。
        :type volumes_attached: list[:class:`huaweicloudsdkecs.v2.VolumeAttach`]
        :param image: 
        :type image: :class:`huaweicloudsdkecs.v2.Image`
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkecs.v2.FlavorQuasar`
        :param fault: 
        :type fault: :class:`huaweicloudsdkecs.v2.Fault`
        :param cpu_options: 
        :type cpu_options: :class:`huaweicloudsdkecs.v2.CpuOptions`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._tenant_id = None
        self._user_id = None
        self._market_info = None
        self._availability_zone = None
        self._vm_state = None
        self._task_state = None
        self._power_state = None
        self._created = None
        self._in_recycle_bin = None
        self._spod_id = None
        self._updated = None
        self._launched_at = None
        self._description = None
        self._key_name = None
        self._locked = None
        self._root_device_name = None
        self._tenancy = None
        self._dedicated_host_id = None
        self._enterprise_project_id = None
        self._metadata = None
        self._tags = None
        self._addresses = None
        self._security_groups = None
        self._volumes_attached = None
        self._image = None
        self._flavor = None
        self._fault = None
        self._cpu_options = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.status = status
        self.tenant_id = tenant_id
        self.user_id = user_id
        if market_info is not None:
            self.market_info = market_info
        self.availability_zone = availability_zone
        self.vm_state = vm_state
        self.task_state = task_state
        if power_state is not None:
            self.power_state = power_state
        self.created = created
        self.in_recycle_bin = in_recycle_bin
        self.spod_id = spod_id
        self.updated = updated
        if launched_at is not None:
            self.launched_at = launched_at
        if description is not None:
            self.description = description
        if key_name is not None:
            self.key_name = key_name
        if locked is not None:
            self.locked = locked
        if root_device_name is not None:
            self.root_device_name = root_device_name
        if tenancy is not None:
            self.tenancy = tenancy
        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if metadata is not None:
            self.metadata = metadata
        if tags is not None:
            self.tags = tags
        if addresses is not None:
            self.addresses = addresses
        if security_groups is not None:
            self.security_groups = security_groups
        if volumes_attached is not None:
            self.volumes_attached = volumes_attached
        if image is not None:
            self.image = image
        self.flavor = flavor
        self.fault = fault
        if cpu_options is not None:
            self.cpu_options = cpu_options

    @property
    def id(self):
        r"""Gets the id of this CloudServer.

        云服务器唯一标识。

        :return: The id of this CloudServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CloudServer.

        云服务器唯一标识。

        :param id: The id of this CloudServer.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CloudServer.

        云服务器名称。

        :return: The name of this CloudServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CloudServer.

        云服务器名称。

        :param name: The name of this CloudServer.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this CloudServer.

        云服务器当前状态信息。

        :return: The status of this CloudServer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CloudServer.

        云服务器当前状态信息。

        :param status: The status of this CloudServer.
        :type status: str
        """
        self._status = status

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this CloudServer.

        云服务器所属租户ID。即项目id，与project_id表示相同的概念。

        :return: The tenant_id of this CloudServer.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this CloudServer.

        云服务器所属租户ID。即项目id，与project_id表示相同的概念。

        :param tenant_id: The tenant_id of this CloudServer.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def user_id(self):
        r"""Gets the user_id of this CloudServer.

        云服务器所属用户ID。

        :return: The user_id of this CloudServer.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this CloudServer.

        云服务器所属用户ID。

        :param user_id: The user_id of this CloudServer.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def market_info(self):
        r"""Gets the market_info of this CloudServer.

        :return: The market_info of this CloudServer.
        :rtype: :class:`huaweicloudsdkecs.v2.MarketModel`
        """
        return self._market_info

    @market_info.setter
    def market_info(self, market_info):
        r"""Sets the market_info of this CloudServer.

        :param market_info: The market_info of this CloudServer.
        :type market_info: :class:`huaweicloudsdkecs.v2.MarketModel`
        """
        self._market_info = market_info

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CloudServer.

        可用分区

        :return: The availability_zone of this CloudServer.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CloudServer.

        可用分区

        :param availability_zone: The availability_zone of this CloudServer.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def vm_state(self):
        r"""Gets the vm_state of this CloudServer.

        云服务器的状态。

        :return: The vm_state of this CloudServer.
        :rtype: str
        """
        return self._vm_state

    @vm_state.setter
    def vm_state(self, vm_state):
        r"""Sets the vm_state of this CloudServer.

        云服务器的状态。

        :param vm_state: The vm_state of this CloudServer.
        :type vm_state: str
        """
        self._vm_state = vm_state

    @property
    def task_state(self):
        r"""Gets the task_state of this CloudServer.

        云服务器任务状态。

        :return: The task_state of this CloudServer.
        :rtype: str
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        r"""Sets the task_state of this CloudServer.

        云服务器任务状态。

        :param task_state: The task_state of this CloudServer.
        :type task_state: str
        """
        self._task_state = task_state

    @property
    def power_state(self):
        r"""Gets the power_state of this CloudServer.

        云服务器电源状态。

        :return: The power_state of this CloudServer.
        :rtype: int
        """
        return self._power_state

    @power_state.setter
    def power_state(self, power_state):
        r"""Sets the power_state of this CloudServer.

        云服务器电源状态。

        :param power_state: The power_state of this CloudServer.
        :type power_state: int
        """
        self._power_state = power_state

    @property
    def created(self):
        r"""Gets the created of this CloudServer.

        云服务器创建时间。 时间格式例如：2020-05-22T07:48:53Z。

        :return: The created of this CloudServer.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this CloudServer.

        云服务器创建时间。 时间格式例如：2020-05-22T07:48:53Z。

        :param created: The created of this CloudServer.
        :type created: str
        """
        self._created = created

    @property
    def in_recycle_bin(self):
        r"""Gets the in_recycle_bin of this CloudServer.

        云服务器是否处于回收站中

        :return: The in_recycle_bin of this CloudServer.
        :rtype: bool
        """
        return self._in_recycle_bin

    @in_recycle_bin.setter
    def in_recycle_bin(self, in_recycle_bin):
        r"""Sets the in_recycle_bin of this CloudServer.

        云服务器是否处于回收站中

        :param in_recycle_bin: The in_recycle_bin of this CloudServer.
        :type in_recycle_bin: bool
        """
        self._in_recycle_bin = in_recycle_bin

    @property
    def spod_id(self):
        r"""Gets the spod_id of this CloudServer.

        共池裸机按整机柜发放的同一批次的批创ID

        :return: The spod_id of this CloudServer.
        :rtype: str
        """
        return self._spod_id

    @spod_id.setter
    def spod_id(self, spod_id):
        r"""Sets the spod_id of this CloudServer.

        共池裸机按整机柜发放的同一批次的批创ID

        :param spod_id: The spod_id of this CloudServer.
        :type spod_id: str
        """
        self._spod_id = spod_id

    @property
    def updated(self):
        r"""Gets the updated of this CloudServer.

        云服务器上一次更新时间。时间格式例如：2020-05-22T07:48:53Z

        :return: The updated of this CloudServer.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this CloudServer.

        云服务器上一次更新时间。时间格式例如：2020-05-22T07:48:53Z

        :param updated: The updated of this CloudServer.
        :type updated: str
        """
        self._updated = updated

    @property
    def launched_at(self):
        r"""Gets the launched_at of this CloudServer.

        云服务器启动时间。时间格式例如：2020-05-22T07:48:53.000000。

        :return: The launched_at of this CloudServer.
        :rtype: str
        """
        return self._launched_at

    @launched_at.setter
    def launched_at(self, launched_at):
        r"""Sets the launched_at of this CloudServer.

        云服务器启动时间。时间格式例如：2020-05-22T07:48:53.000000。

        :param launched_at: The launched_at of this CloudServer.
        :type launched_at: str
        """
        self._launched_at = launched_at

    @property
    def description(self):
        r"""Gets the description of this CloudServer.

        云服务器的描述信息。

        :return: The description of this CloudServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CloudServer.

        云服务器的描述信息。

        :param description: The description of this CloudServer.
        :type description: str
        """
        self._description = description

    @property
    def key_name(self):
        r"""Gets the key_name of this CloudServer.

        云服务器使用的密钥对名称。

        :return: The key_name of this CloudServer.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this CloudServer.

        云服务器使用的密钥对名称。

        :param key_name: The key_name of this CloudServer.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def locked(self):
        r"""Gets the locked of this CloudServer.

        云服务器是否为锁定状态。  true：锁定 false：未锁定

        :return: The locked of this CloudServer.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        r"""Sets the locked of this CloudServer.

        云服务器是否为锁定状态。  true：锁定 false：未锁定

        :param locked: The locked of this CloudServer.
        :type locked: bool
        """
        self._locked = locked

    @property
    def root_device_name(self):
        r"""Gets the root_device_name of this CloudServer.

        云服务器系统盘的设备名称，例如当系统盘的磁盘模式是VDB时，为/dev/vda。

        :return: The root_device_name of this CloudServer.
        :rtype: str
        """
        return self._root_device_name

    @root_device_name.setter
    def root_device_name(self, root_device_name):
        r"""Sets the root_device_name of this CloudServer.

        云服务器系统盘的设备名称，例如当系统盘的磁盘模式是VDB时，为/dev/vda。

        :param root_device_name: The root_device_name of this CloudServer.
        :type root_device_name: str
        """
        self._root_device_name = root_device_name

    @property
    def tenancy(self):
        r"""Gets the tenancy of this CloudServer.

        在专属主机或共享池中创建云服务器。默认为在共享池创建。值为： shared或dedicated。  shared：表示共享池。 dedicated:表示专属主机。

        :return: The tenancy of this CloudServer.
        :rtype: str
        """
        return self._tenancy

    @tenancy.setter
    def tenancy(self, tenancy):
        r"""Sets the tenancy of this CloudServer.

        在专属主机或共享池中创建云服务器。默认为在共享池创建。值为： shared或dedicated。  shared：表示共享池。 dedicated:表示专属主机。

        :param tenancy: The tenancy of this CloudServer.
        :type tenancy: str
        """
        self._tenancy = tenancy

    @property
    def dedicated_host_id(self):
        r"""Gets the dedicated_host_id of this CloudServer.

        专属主机ID。此属性仅在tenancy值为dedicated时有效，不指定此属性，系统将自动分配租户可自动放置云服务器的专属主机。

        :return: The dedicated_host_id of this CloudServer.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        r"""Sets the dedicated_host_id of this CloudServer.

        专属主机ID。此属性仅在tenancy值为dedicated时有效，不指定此属性，系统将自动分配租户可自动放置云服务器的专属主机。

        :param dedicated_host_id: The dedicated_host_id of this CloudServer.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CloudServer.

        查询绑定某个企业项目的云服务器。 若需要查询当前用户所有企业项目绑定的云服务，请传参all_granted_eps。

        :return: The enterprise_project_id of this CloudServer.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CloudServer.

        查询绑定某个企业项目的云服务器。 若需要查询当前用户所有企业项目绑定的云服务，请传参all_granted_eps。

        :param enterprise_project_id: The enterprise_project_id of this CloudServer.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def metadata(self):
        r"""Gets the metadata of this CloudServer.

        云服务器元数据。

        :return: The metadata of this CloudServer.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CloudServer.

        云服务器元数据。

        :param metadata: The metadata of this CloudServer.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def tags(self):
        r"""Gets the tags of this CloudServer.

        云服务器的标签列表。

        :return: The tags of this CloudServer.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CloudServer.

        云服务器的标签列表。

        :param tags: The tags of this CloudServer.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def addresses(self):
        r"""Gets the addresses of this CloudServer.

        云服务器对应的网络地址信息。

        :return: The addresses of this CloudServer.
        :rtype: dict(str, list[NetworkAddresses])
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this CloudServer.

        云服务器对应的网络地址信息。

        :param addresses: The addresses of this CloudServer.
        :type addresses: dict(str, list[NetworkAddresses])
        """
        self._addresses = addresses

    @property
    def security_groups(self):
        r"""Gets the security_groups of this CloudServer.

        云服务器的安全组信息。

        :return: The security_groups of this CloudServer.
        :rtype: list[:class:`huaweicloudsdkecs.v2.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this CloudServer.

        云服务器的安全组信息。

        :param security_groups: The security_groups of this CloudServer.
        :type security_groups: list[:class:`huaweicloudsdkecs.v2.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def volumes_attached(self):
        r"""Gets the volumes_attached of this CloudServer.

        云服务器挂载磁盘信息。

        :return: The volumes_attached of this CloudServer.
        :rtype: list[:class:`huaweicloudsdkecs.v2.VolumeAttach`]
        """
        return self._volumes_attached

    @volumes_attached.setter
    def volumes_attached(self, volumes_attached):
        r"""Sets the volumes_attached of this CloudServer.

        云服务器挂载磁盘信息。

        :param volumes_attached: The volumes_attached of this CloudServer.
        :type volumes_attached: list[:class:`huaweicloudsdkecs.v2.VolumeAttach`]
        """
        self._volumes_attached = volumes_attached

    @property
    def image(self):
        r"""Gets the image of this CloudServer.

        :return: The image of this CloudServer.
        :rtype: :class:`huaweicloudsdkecs.v2.Image`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this CloudServer.

        :param image: The image of this CloudServer.
        :type image: :class:`huaweicloudsdkecs.v2.Image`
        """
        self._image = image

    @property
    def flavor(self):
        r"""Gets the flavor of this CloudServer.

        :return: The flavor of this CloudServer.
        :rtype: :class:`huaweicloudsdkecs.v2.FlavorQuasar`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CloudServer.

        :param flavor: The flavor of this CloudServer.
        :type flavor: :class:`huaweicloudsdkecs.v2.FlavorQuasar`
        """
        self._flavor = flavor

    @property
    def fault(self):
        r"""Gets the fault of this CloudServer.

        :return: The fault of this CloudServer.
        :rtype: :class:`huaweicloudsdkecs.v2.Fault`
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        r"""Sets the fault of this CloudServer.

        :param fault: The fault of this CloudServer.
        :type fault: :class:`huaweicloudsdkecs.v2.Fault`
        """
        self._fault = fault

    @property
    def cpu_options(self):
        r"""Gets the cpu_options of this CloudServer.

        :return: The cpu_options of this CloudServer.
        :rtype: :class:`huaweicloudsdkecs.v2.CpuOptions`
        """
        return self._cpu_options

    @cpu_options.setter
    def cpu_options(self, cpu_options):
        r"""Sets the cpu_options of this CloudServer.

        :param cpu_options: The cpu_options of this CloudServer.
        :type cpu_options: :class:`huaweicloudsdkecs.v2.CpuOptions`
        """
        self._cpu_options = cpu_options

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
        if not isinstance(other, CloudServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
