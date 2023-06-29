# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppServer:

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
        'machine_name': 'str',
        'description': 'str',
        'server_group_id': 'str',
        'flavor': 'Flavor',
        'status': 'ServerStatus',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'image_id': 'str',
        'availability_zone': 'str',
        'domain': 'str',
        'ou_name': 'str',
        'sid': 'str',
        'instance_id': 'str',
        'os_version': 'str',
        'os_type': 'str',
        'order_id': 'str',
        'maintain_status': 'bool',
        'scaling_auto_create': 'bool',
        'job_id': 'str',
        'job_type': 'JobType',
        'job_status': 'JobStatus',
        'job_time': 'datetime',
        'resource_pool_id': 'str',
        'resource_pool_type': 'str',
        'host_id': 'str',
        'server_group_name': 'str',
        'product_info': 'ProductInfo',
        'metadata': 'dict(str, str)',
        'session_count': 'int',
        'vm_status': 'AppServerStatus',
        'task_status': 'AppServerTaskStatus',
        'freeze': 'list[CbcFreezeInfo]',
        'host_address': 'list[EcsNetWork]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'machine_name': 'machine_name',
        'description': 'description',
        'server_group_id': 'server_group_id',
        'flavor': 'flavor',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'image_id': 'image_id',
        'availability_zone': 'availability_zone',
        'domain': 'domain',
        'ou_name': 'ou_name',
        'sid': 'sid',
        'instance_id': 'instance_id',
        'os_version': 'os_version',
        'os_type': 'os_type',
        'order_id': 'order_id',
        'maintain_status': 'maintain_status',
        'scaling_auto_create': 'scaling_auto_create',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'job_status': 'job_status',
        'job_time': 'job_time',
        'resource_pool_id': 'resource_pool_id',
        'resource_pool_type': 'resource_pool_type',
        'host_id': 'host_id',
        'server_group_name': 'server_group_name',
        'product_info': 'product_info',
        'metadata': 'metadata',
        'session_count': 'session_count',
        'vm_status': 'vm_status',
        'task_status': 'task_status',
        'freeze': 'freeze',
        'host_address': 'host_address'
    }

    def __init__(self, id=None, name=None, machine_name=None, description=None, server_group_id=None, flavor=None, status=None, create_time=None, update_time=None, image_id=None, availability_zone=None, domain=None, ou_name=None, sid=None, instance_id=None, os_version=None, os_type=None, order_id=None, maintain_status=None, scaling_auto_create=None, job_id=None, job_type=None, job_status=None, job_time=None, resource_pool_id=None, resource_pool_type=None, host_id=None, server_group_name=None, product_info=None, metadata=None, session_count=None, vm_status=None, task_status=None, freeze=None, host_address=None):
        """AppServer

        The model defined in huaweicloud sdk

        :param id: aps实例的唯一标识
        :type id: str
        :param name: 服务器名称
        :type name: str
        :param machine_name: 计算机名称
        :type machine_name: str
        :param description: 描述
        :type description: str
        :param server_group_id: 服务器组ID
        :type server_group_id: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkworkspaceapp.v1.Flavor`
        :param status: 
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ServerStatus`
        :param create_time: 服务器创建时间
        :type create_time: datetime
        :param update_time: 更新时间
        :type update_time: datetime
        :param image_id: 镜像ID
        :type image_id: str
        :param availability_zone: 服务器可用分区
        :type availability_zone: str
        :param domain: 域
        :type domain: str
        :param ou_name: 组织名称
        :type ou_name: str
        :param sid: 实例的SID
        :type sid: str
        :param instance_id: 实例的ID
        :type instance_id: str
        :param os_version: 服务器系统版本
        :type os_version: str
        :param os_type: 操作系统类型，当前仅支持Windows - Linux - Windows - Other
        :type os_type: str
        :param order_id: 包周期产品的订单ID
        :type order_id: str
        :param maintain_status: 是否维护状态
        :type maintain_status: bool
        :param scaling_auto_create: 配置弹性伸缩策略时，服务自动创建的实例。 - true : 通过弹性伸缩创建 - false: 不是通过弹性伸缩创建
        :type scaling_auto_create: bool
        :param job_id: 上一次执行job的id
        :type job_id: str
        :param job_type: 
        :type job_type: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        :param job_status: 
        :type job_status: :class:`huaweicloudsdkworkspaceapp.v1.JobStatus`
        :param job_time: 上一次执行job的执行时间
        :type job_time: datetime
        :param resource_pool_id: 资源池ID
        :type resource_pool_id: str
        :param resource_pool_type: 资源池类型 - private：私有资源池 - public: 工作资源池
        :type resource_pool_type: str
        :param host_id: 云专属主机id
        :type host_id: str
        :param server_group_name: 服务器组名称
        :type server_group_name: str
        :param product_info: 
        :type product_info: :class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`
        :param metadata: 弹性云服务器元数据。  &gt;   1. charging_mode 云服务器的计费类型。  - “0”：按需计费（即postPaid-后付费方式）。 - “1”：按包年包月计费（即prePaid-预付费方式）。\&quot;2\&quot;：竞价实例计费  2. metering.order_id 按“包年/包月”计费的云服务器对应的订单ID。  3. metering.product_id 按“包年/包月”计费的云服务器对应的产品ID。  4. vpc_id 云服务器所属的虚拟私有云ID。  5. EcmResStatus 云服务器的冻结状态。  - normal：云服务器正常状态（未被冻结）。 - freeze：云服务器被冻结。  &gt; 当云服务器被冻结或者解冻后，系统默认添加该字段，且该字段必选。  6. metering.image_id 云服务器操作系统对应的镜像ID  7.  metering.imagetype 镜像类型，目前支持：  - 公共镜像（gold） - 私有镜像（private） - 共享镜像（shared）  8. metering.resourcespeccode 云服务器对应的资源规格。  9. image_name 云服务器操作系统对应的镜像名称。  10. os_bit 操作系统位数，一般取值为“32”或者“64”。  11. lockCheckEndpoint 回调URL，用于检查弹性云服务器的加锁是否有效。  - 如果有效，则云服务器保持锁定状态。 - 如果无效，解除锁定状态，删除失效的锁。  12. lockSource 弹性云服务器来自哪个服务。订单加锁（ORDER）  13. lockSourceId 弹性云服务器的加锁来自哪个ID。lockSource为“ORDER”时，lockSourceId为订单ID。  14. lockScene 弹性云服务器的加锁类型。  - 按需转包周期（TO_PERIOD_LOCK）  15. virtual_env_type  - IOS镜像创建虚拟机，\&quot;virtual_env_type\&quot;: \&quot;IsoImage\&quot; 属性； - 非IOS镜像创建虚拟机，在19.5.0版本以后创建的虚拟机将不会添加virtual_env_type 属性，而在此之前的版本创建的虚拟机可能会返回\&quot;virtual_env_type\&quot;: \&quot;FusionCompute\&quot;属性 。  &gt; virtual_env_type属性不允许用户增加、删除和修改。  16. metering.resourcetype 云服务器对应的资源类型。  17. os_type 操作系统类型，取值为：Linux、Windows。  18. cascaded.instance_extrainfo 系统内部虚拟机扩展信息。  19. __support_agent_list 云服务器是否支持企业主机安全、主机监控。  - “hss”：企业主机安全 -  “ces”：主机监控  20. agency_name 委托的名称。  委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。
        :type metadata: dict(str, str)
        :param session_count: 会话数量
        :type session_count: int
        :param vm_status: 
        :type vm_status: :class:`huaweicloudsdkworkspaceapp.v1.AppServerStatus`
        :param task_status: 
        :type task_status: :class:`huaweicloudsdkworkspaceapp.v1.AppServerTaskStatus`
        :param freeze: 冻结信息
        :type freeze: list[:class:`huaweicloudsdkworkspaceapp.v1.CbcFreezeInfo`]
        :param host_address: vpc和子网信息
        :type host_address: list[:class:`huaweicloudsdkworkspaceapp.v1.EcsNetWork`]
        """
        
        

        self._id = None
        self._name = None
        self._machine_name = None
        self._description = None
        self._server_group_id = None
        self._flavor = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self._image_id = None
        self._availability_zone = None
        self._domain = None
        self._ou_name = None
        self._sid = None
        self._instance_id = None
        self._os_version = None
        self._os_type = None
        self._order_id = None
        self._maintain_status = None
        self._scaling_auto_create = None
        self._job_id = None
        self._job_type = None
        self._job_status = None
        self._job_time = None
        self._resource_pool_id = None
        self._resource_pool_type = None
        self._host_id = None
        self._server_group_name = None
        self._product_info = None
        self._metadata = None
        self._session_count = None
        self._vm_status = None
        self._task_status = None
        self._freeze = None
        self._host_address = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if machine_name is not None:
            self.machine_name = machine_name
        if description is not None:
            self.description = description
        if server_group_id is not None:
            self.server_group_id = server_group_id
        if flavor is not None:
            self.flavor = flavor
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if image_id is not None:
            self.image_id = image_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if domain is not None:
            self.domain = domain
        if ou_name is not None:
            self.ou_name = ou_name
        if sid is not None:
            self.sid = sid
        if instance_id is not None:
            self.instance_id = instance_id
        if os_version is not None:
            self.os_version = os_version
        if os_type is not None:
            self.os_type = os_type
        if order_id is not None:
            self.order_id = order_id
        if maintain_status is not None:
            self.maintain_status = maintain_status
        if scaling_auto_create is not None:
            self.scaling_auto_create = scaling_auto_create
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if job_status is not None:
            self.job_status = job_status
        if job_time is not None:
            self.job_time = job_time
        if resource_pool_id is not None:
            self.resource_pool_id = resource_pool_id
        if resource_pool_type is not None:
            self.resource_pool_type = resource_pool_type
        if host_id is not None:
            self.host_id = host_id
        if server_group_name is not None:
            self.server_group_name = server_group_name
        if product_info is not None:
            self.product_info = product_info
        if metadata is not None:
            self.metadata = metadata
        if session_count is not None:
            self.session_count = session_count
        if vm_status is not None:
            self.vm_status = vm_status
        if task_status is not None:
            self.task_status = task_status
        if freeze is not None:
            self.freeze = freeze
        if host_address is not None:
            self.host_address = host_address

    @property
    def id(self):
        """Gets the id of this AppServer.

        aps实例的唯一标识

        :return: The id of this AppServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AppServer.

        aps实例的唯一标识

        :param id: The id of this AppServer.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this AppServer.

        服务器名称

        :return: The name of this AppServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AppServer.

        服务器名称

        :param name: The name of this AppServer.
        :type name: str
        """
        self._name = name

    @property
    def machine_name(self):
        """Gets the machine_name of this AppServer.

        计算机名称

        :return: The machine_name of this AppServer.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this AppServer.

        计算机名称

        :param machine_name: The machine_name of this AppServer.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def description(self):
        """Gets the description of this AppServer.

        描述

        :return: The description of this AppServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AppServer.

        描述

        :param description: The description of this AppServer.
        :type description: str
        """
        self._description = description

    @property
    def server_group_id(self):
        """Gets the server_group_id of this AppServer.

        服务器组ID

        :return: The server_group_id of this AppServer.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this AppServer.

        服务器组ID

        :param server_group_id: The server_group_id of this AppServer.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def flavor(self):
        """Gets the flavor of this AppServer.

        :return: The flavor of this AppServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this AppServer.

        :param flavor: The flavor of this AppServer.
        :type flavor: :class:`huaweicloudsdkworkspaceapp.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def status(self):
        """Gets the status of this AppServer.

        :return: The status of this AppServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ServerStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AppServer.

        :param status: The status of this AppServer.
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ServerStatus`
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this AppServer.

        服务器创建时间

        :return: The create_time of this AppServer.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AppServer.

        服务器创建时间

        :param create_time: The create_time of this AppServer.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this AppServer.

        更新时间

        :return: The update_time of this AppServer.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this AppServer.

        更新时间

        :param update_time: The update_time of this AppServer.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def image_id(self):
        """Gets the image_id of this AppServer.

        镜像ID

        :return: The image_id of this AppServer.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this AppServer.

        镜像ID

        :param image_id: The image_id of this AppServer.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this AppServer.

        服务器可用分区

        :return: The availability_zone of this AppServer.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this AppServer.

        服务器可用分区

        :param availability_zone: The availability_zone of this AppServer.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def domain(self):
        """Gets the domain of this AppServer.

        域

        :return: The domain of this AppServer.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AppServer.

        域

        :param domain: The domain of this AppServer.
        :type domain: str
        """
        self._domain = domain

    @property
    def ou_name(self):
        """Gets the ou_name of this AppServer.

        组织名称

        :return: The ou_name of this AppServer.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this AppServer.

        组织名称

        :param ou_name: The ou_name of this AppServer.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def sid(self):
        """Gets the sid of this AppServer.

        实例的SID

        :return: The sid of this AppServer.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AppServer.

        实例的SID

        :param sid: The sid of this AppServer.
        :type sid: str
        """
        self._sid = sid

    @property
    def instance_id(self):
        """Gets the instance_id of this AppServer.

        实例的ID

        :return: The instance_id of this AppServer.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this AppServer.

        实例的ID

        :param instance_id: The instance_id of this AppServer.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def os_version(self):
        """Gets the os_version of this AppServer.

        服务器系统版本

        :return: The os_version of this AppServer.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this AppServer.

        服务器系统版本

        :param os_version: The os_version of this AppServer.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def os_type(self):
        """Gets the os_type of this AppServer.

        操作系统类型，当前仅支持Windows - Linux - Windows - Other

        :return: The os_type of this AppServer.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this AppServer.

        操作系统类型，当前仅支持Windows - Linux - Windows - Other

        :param os_type: The os_type of this AppServer.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def order_id(self):
        """Gets the order_id of this AppServer.

        包周期产品的订单ID

        :return: The order_id of this AppServer.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this AppServer.

        包周期产品的订单ID

        :param order_id: The order_id of this AppServer.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def maintain_status(self):
        """Gets the maintain_status of this AppServer.

        是否维护状态

        :return: The maintain_status of this AppServer.
        :rtype: bool
        """
        return self._maintain_status

    @maintain_status.setter
    def maintain_status(self, maintain_status):
        """Sets the maintain_status of this AppServer.

        是否维护状态

        :param maintain_status: The maintain_status of this AppServer.
        :type maintain_status: bool
        """
        self._maintain_status = maintain_status

    @property
    def scaling_auto_create(self):
        """Gets the scaling_auto_create of this AppServer.

        配置弹性伸缩策略时，服务自动创建的实例。 - true : 通过弹性伸缩创建 - false: 不是通过弹性伸缩创建

        :return: The scaling_auto_create of this AppServer.
        :rtype: bool
        """
        return self._scaling_auto_create

    @scaling_auto_create.setter
    def scaling_auto_create(self, scaling_auto_create):
        """Sets the scaling_auto_create of this AppServer.

        配置弹性伸缩策略时，服务自动创建的实例。 - true : 通过弹性伸缩创建 - false: 不是通过弹性伸缩创建

        :param scaling_auto_create: The scaling_auto_create of this AppServer.
        :type scaling_auto_create: bool
        """
        self._scaling_auto_create = scaling_auto_create

    @property
    def job_id(self):
        """Gets the job_id of this AppServer.

        上一次执行job的id

        :return: The job_id of this AppServer.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this AppServer.

        上一次执行job的id

        :param job_id: The job_id of this AppServer.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this AppServer.

        :return: The job_type of this AppServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this AppServer.

        :param job_type: The job_type of this AppServer.
        :type job_type: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        """
        self._job_type = job_type

    @property
    def job_status(self):
        """Gets the job_status of this AppServer.

        :return: The job_status of this AppServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobStatus`
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this AppServer.

        :param job_status: The job_status of this AppServer.
        :type job_status: :class:`huaweicloudsdkworkspaceapp.v1.JobStatus`
        """
        self._job_status = job_status

    @property
    def job_time(self):
        """Gets the job_time of this AppServer.

        上一次执行job的执行时间

        :return: The job_time of this AppServer.
        :rtype: datetime
        """
        return self._job_time

    @job_time.setter
    def job_time(self, job_time):
        """Sets the job_time of this AppServer.

        上一次执行job的执行时间

        :param job_time: The job_time of this AppServer.
        :type job_time: datetime
        """
        self._job_time = job_time

    @property
    def resource_pool_id(self):
        """Gets the resource_pool_id of this AppServer.

        资源池ID

        :return: The resource_pool_id of this AppServer.
        :rtype: str
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        """Sets the resource_pool_id of this AppServer.

        资源池ID

        :param resource_pool_id: The resource_pool_id of this AppServer.
        :type resource_pool_id: str
        """
        self._resource_pool_id = resource_pool_id

    @property
    def resource_pool_type(self):
        """Gets the resource_pool_type of this AppServer.

        资源池类型 - private：私有资源池 - public: 工作资源池

        :return: The resource_pool_type of this AppServer.
        :rtype: str
        """
        return self._resource_pool_type

    @resource_pool_type.setter
    def resource_pool_type(self, resource_pool_type):
        """Sets the resource_pool_type of this AppServer.

        资源池类型 - private：私有资源池 - public: 工作资源池

        :param resource_pool_type: The resource_pool_type of this AppServer.
        :type resource_pool_type: str
        """
        self._resource_pool_type = resource_pool_type

    @property
    def host_id(self):
        """Gets the host_id of this AppServer.

        云专属主机id

        :return: The host_id of this AppServer.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this AppServer.

        云专属主机id

        :param host_id: The host_id of this AppServer.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def server_group_name(self):
        """Gets the server_group_name of this AppServer.

        服务器组名称

        :return: The server_group_name of this AppServer.
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        """Sets the server_group_name of this AppServer.

        服务器组名称

        :param server_group_name: The server_group_name of this AppServer.
        :type server_group_name: str
        """
        self._server_group_name = server_group_name

    @property
    def product_info(self):
        """Gets the product_info of this AppServer.

        :return: The product_info of this AppServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`
        """
        return self._product_info

    @product_info.setter
    def product_info(self, product_info):
        """Sets the product_info of this AppServer.

        :param product_info: The product_info of this AppServer.
        :type product_info: :class:`huaweicloudsdkworkspaceapp.v1.ProductInfo`
        """
        self._product_info = product_info

    @property
    def metadata(self):
        """Gets the metadata of this AppServer.

        弹性云服务器元数据。  >   1. charging_mode 云服务器的计费类型。  - “0”：按需计费（即postPaid-后付费方式）。 - “1”：按包年包月计费（即prePaid-预付费方式）。\"2\"：竞价实例计费  2. metering.order_id 按“包年/包月”计费的云服务器对应的订单ID。  3. metering.product_id 按“包年/包月”计费的云服务器对应的产品ID。  4. vpc_id 云服务器所属的虚拟私有云ID。  5. EcmResStatus 云服务器的冻结状态。  - normal：云服务器正常状态（未被冻结）。 - freeze：云服务器被冻结。  > 当云服务器被冻结或者解冻后，系统默认添加该字段，且该字段必选。  6. metering.image_id 云服务器操作系统对应的镜像ID  7.  metering.imagetype 镜像类型，目前支持：  - 公共镜像（gold） - 私有镜像（private） - 共享镜像（shared）  8. metering.resourcespeccode 云服务器对应的资源规格。  9. image_name 云服务器操作系统对应的镜像名称。  10. os_bit 操作系统位数，一般取值为“32”或者“64”。  11. lockCheckEndpoint 回调URL，用于检查弹性云服务器的加锁是否有效。  - 如果有效，则云服务器保持锁定状态。 - 如果无效，解除锁定状态，删除失效的锁。  12. lockSource 弹性云服务器来自哪个服务。订单加锁（ORDER）  13. lockSourceId 弹性云服务器的加锁来自哪个ID。lockSource为“ORDER”时，lockSourceId为订单ID。  14. lockScene 弹性云服务器的加锁类型。  - 按需转包周期（TO_PERIOD_LOCK）  15. virtual_env_type  - IOS镜像创建虚拟机，\"virtual_env_type\": \"IsoImage\" 属性； - 非IOS镜像创建虚拟机，在19.5.0版本以后创建的虚拟机将不会添加virtual_env_type 属性，而在此之前的版本创建的虚拟机可能会返回\"virtual_env_type\": \"FusionCompute\"属性 。  > virtual_env_type属性不允许用户增加、删除和修改。  16. metering.resourcetype 云服务器对应的资源类型。  17. os_type 操作系统类型，取值为：Linux、Windows。  18. cascaded.instance_extrainfo 系统内部虚拟机扩展信息。  19. __support_agent_list 云服务器是否支持企业主机安全、主机监控。  - “hss”：企业主机安全 -  “ces”：主机监控  20. agency_name 委托的名称。  委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。

        :return: The metadata of this AppServer.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AppServer.

        弹性云服务器元数据。  >   1. charging_mode 云服务器的计费类型。  - “0”：按需计费（即postPaid-后付费方式）。 - “1”：按包年包月计费（即prePaid-预付费方式）。\"2\"：竞价实例计费  2. metering.order_id 按“包年/包月”计费的云服务器对应的订单ID。  3. metering.product_id 按“包年/包月”计费的云服务器对应的产品ID。  4. vpc_id 云服务器所属的虚拟私有云ID。  5. EcmResStatus 云服务器的冻结状态。  - normal：云服务器正常状态（未被冻结）。 - freeze：云服务器被冻结。  > 当云服务器被冻结或者解冻后，系统默认添加该字段，且该字段必选。  6. metering.image_id 云服务器操作系统对应的镜像ID  7.  metering.imagetype 镜像类型，目前支持：  - 公共镜像（gold） - 私有镜像（private） - 共享镜像（shared）  8. metering.resourcespeccode 云服务器对应的资源规格。  9. image_name 云服务器操作系统对应的镜像名称。  10. os_bit 操作系统位数，一般取值为“32”或者“64”。  11. lockCheckEndpoint 回调URL，用于检查弹性云服务器的加锁是否有效。  - 如果有效，则云服务器保持锁定状态。 - 如果无效，解除锁定状态，删除失效的锁。  12. lockSource 弹性云服务器来自哪个服务。订单加锁（ORDER）  13. lockSourceId 弹性云服务器的加锁来自哪个ID。lockSource为“ORDER”时，lockSourceId为订单ID。  14. lockScene 弹性云服务器的加锁类型。  - 按需转包周期（TO_PERIOD_LOCK）  15. virtual_env_type  - IOS镜像创建虚拟机，\"virtual_env_type\": \"IsoImage\" 属性； - 非IOS镜像创建虚拟机，在19.5.0版本以后创建的虚拟机将不会添加virtual_env_type 属性，而在此之前的版本创建的虚拟机可能会返回\"virtual_env_type\": \"FusionCompute\"属性 。  > virtual_env_type属性不允许用户增加、删除和修改。  16. metering.resourcetype 云服务器对应的资源类型。  17. os_type 操作系统类型，取值为：Linux、Windows。  18. cascaded.instance_extrainfo 系统内部虚拟机扩展信息。  19. __support_agent_list 云服务器是否支持企业主机安全、主机监控。  - “hss”：企业主机安全 -  “ces”：主机监控  20. agency_name 委托的名称。  委托是由租户管理员在统一身份认证服务（Identity and Access Management，IAM）上创建的，可以为弹性云服务器提供访问云服务的临时凭证。

        :param metadata: The metadata of this AppServer.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def session_count(self):
        """Gets the session_count of this AppServer.

        会话数量

        :return: The session_count of this AppServer.
        :rtype: int
        """
        return self._session_count

    @session_count.setter
    def session_count(self, session_count):
        """Sets the session_count of this AppServer.

        会话数量

        :param session_count: The session_count of this AppServer.
        :type session_count: int
        """
        self._session_count = session_count

    @property
    def vm_status(self):
        """Gets the vm_status of this AppServer.

        :return: The vm_status of this AppServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppServerStatus`
        """
        return self._vm_status

    @vm_status.setter
    def vm_status(self, vm_status):
        """Sets the vm_status of this AppServer.

        :param vm_status: The vm_status of this AppServer.
        :type vm_status: :class:`huaweicloudsdkworkspaceapp.v1.AppServerStatus`
        """
        self._vm_status = vm_status

    @property
    def task_status(self):
        """Gets the task_status of this AppServer.

        :return: The task_status of this AppServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AppServerTaskStatus`
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this AppServer.

        :param task_status: The task_status of this AppServer.
        :type task_status: :class:`huaweicloudsdkworkspaceapp.v1.AppServerTaskStatus`
        """
        self._task_status = task_status

    @property
    def freeze(self):
        """Gets the freeze of this AppServer.

        冻结信息

        :return: The freeze of this AppServer.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.CbcFreezeInfo`]
        """
        return self._freeze

    @freeze.setter
    def freeze(self, freeze):
        """Sets the freeze of this AppServer.

        冻结信息

        :param freeze: The freeze of this AppServer.
        :type freeze: list[:class:`huaweicloudsdkworkspaceapp.v1.CbcFreezeInfo`]
        """
        self._freeze = freeze

    @property
    def host_address(self):
        """Gets the host_address of this AppServer.

        vpc和子网信息

        :return: The host_address of this AppServer.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.EcsNetWork`]
        """
        return self._host_address

    @host_address.setter
    def host_address(self, host_address):
        """Sets the host_address of this AppServer.

        vpc和子网信息

        :param host_address: The host_address of this AppServer.
        :type host_address: list[:class:`huaweicloudsdkworkspaceapp.v1.EcsNetWork`]
        """
        self._host_address = host_address

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
        if not isinstance(other, AppServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
