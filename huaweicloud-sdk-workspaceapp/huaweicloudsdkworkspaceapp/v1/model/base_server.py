# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseServer:

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
        'host_id': 'str'
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
        'host_id': 'host_id'
    }

    def __init__(self, id=None, name=None, machine_name=None, description=None, server_group_id=None, flavor=None, status=None, create_time=None, update_time=None, image_id=None, availability_zone=None, domain=None, ou_name=None, sid=None, instance_id=None, os_version=None, os_type=None, order_id=None, maintain_status=None, scaling_auto_create=None, job_id=None, job_type=None, job_status=None, job_time=None, resource_pool_id=None, resource_pool_type=None, host_id=None):
        """BaseServer

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

    @property
    def id(self):
        """Gets the id of this BaseServer.

        aps实例的唯一标识

        :return: The id of this BaseServer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseServer.

        aps实例的唯一标识

        :param id: The id of this BaseServer.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BaseServer.

        服务器名称

        :return: The name of this BaseServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BaseServer.

        服务器名称

        :param name: The name of this BaseServer.
        :type name: str
        """
        self._name = name

    @property
    def machine_name(self):
        """Gets the machine_name of this BaseServer.

        计算机名称

        :return: The machine_name of this BaseServer.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """Sets the machine_name of this BaseServer.

        计算机名称

        :param machine_name: The machine_name of this BaseServer.
        :type machine_name: str
        """
        self._machine_name = machine_name

    @property
    def description(self):
        """Gets the description of this BaseServer.

        描述

        :return: The description of this BaseServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BaseServer.

        描述

        :param description: The description of this BaseServer.
        :type description: str
        """
        self._description = description

    @property
    def server_group_id(self):
        """Gets the server_group_id of this BaseServer.

        服务器组ID

        :return: The server_group_id of this BaseServer.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this BaseServer.

        服务器组ID

        :param server_group_id: The server_group_id of this BaseServer.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def flavor(self):
        """Gets the flavor of this BaseServer.

        :return: The flavor of this BaseServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this BaseServer.

        :param flavor: The flavor of this BaseServer.
        :type flavor: :class:`huaweicloudsdkworkspaceapp.v1.Flavor`
        """
        self._flavor = flavor

    @property
    def status(self):
        """Gets the status of this BaseServer.

        :return: The status of this BaseServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ServerStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BaseServer.

        :param status: The status of this BaseServer.
        :type status: :class:`huaweicloudsdkworkspaceapp.v1.ServerStatus`
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this BaseServer.

        服务器创建时间

        :return: The create_time of this BaseServer.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BaseServer.

        服务器创建时间

        :param create_time: The create_time of this BaseServer.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this BaseServer.

        更新时间

        :return: The update_time of this BaseServer.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BaseServer.

        更新时间

        :param update_time: The update_time of this BaseServer.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def image_id(self):
        """Gets the image_id of this BaseServer.

        镜像ID

        :return: The image_id of this BaseServer.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this BaseServer.

        镜像ID

        :param image_id: The image_id of this BaseServer.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def availability_zone(self):
        """Gets the availability_zone of this BaseServer.

        服务器可用分区

        :return: The availability_zone of this BaseServer.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this BaseServer.

        服务器可用分区

        :param availability_zone: The availability_zone of this BaseServer.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def domain(self):
        """Gets the domain of this BaseServer.

        域

        :return: The domain of this BaseServer.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this BaseServer.

        域

        :param domain: The domain of this BaseServer.
        :type domain: str
        """
        self._domain = domain

    @property
    def ou_name(self):
        """Gets the ou_name of this BaseServer.

        组织名称

        :return: The ou_name of this BaseServer.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this BaseServer.

        组织名称

        :param ou_name: The ou_name of this BaseServer.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def sid(self):
        """Gets the sid of this BaseServer.

        实例的SID

        :return: The sid of this BaseServer.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this BaseServer.

        实例的SID

        :param sid: The sid of this BaseServer.
        :type sid: str
        """
        self._sid = sid

    @property
    def instance_id(self):
        """Gets the instance_id of this BaseServer.

        实例的ID

        :return: The instance_id of this BaseServer.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BaseServer.

        实例的ID

        :param instance_id: The instance_id of this BaseServer.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def os_version(self):
        """Gets the os_version of this BaseServer.

        服务器系统版本

        :return: The os_version of this BaseServer.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this BaseServer.

        服务器系统版本

        :param os_version: The os_version of this BaseServer.
        :type os_version: str
        """
        self._os_version = os_version

    @property
    def os_type(self):
        """Gets the os_type of this BaseServer.

        操作系统类型，当前仅支持Windows - Linux - Windows - Other

        :return: The os_type of this BaseServer.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this BaseServer.

        操作系统类型，当前仅支持Windows - Linux - Windows - Other

        :param os_type: The os_type of this BaseServer.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def order_id(self):
        """Gets the order_id of this BaseServer.

        包周期产品的订单ID

        :return: The order_id of this BaseServer.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this BaseServer.

        包周期产品的订单ID

        :param order_id: The order_id of this BaseServer.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def maintain_status(self):
        """Gets the maintain_status of this BaseServer.

        是否维护状态

        :return: The maintain_status of this BaseServer.
        :rtype: bool
        """
        return self._maintain_status

    @maintain_status.setter
    def maintain_status(self, maintain_status):
        """Sets the maintain_status of this BaseServer.

        是否维护状态

        :param maintain_status: The maintain_status of this BaseServer.
        :type maintain_status: bool
        """
        self._maintain_status = maintain_status

    @property
    def scaling_auto_create(self):
        """Gets the scaling_auto_create of this BaseServer.

        配置弹性伸缩策略时，服务自动创建的实例。 - true : 通过弹性伸缩创建 - false: 不是通过弹性伸缩创建

        :return: The scaling_auto_create of this BaseServer.
        :rtype: bool
        """
        return self._scaling_auto_create

    @scaling_auto_create.setter
    def scaling_auto_create(self, scaling_auto_create):
        """Sets the scaling_auto_create of this BaseServer.

        配置弹性伸缩策略时，服务自动创建的实例。 - true : 通过弹性伸缩创建 - false: 不是通过弹性伸缩创建

        :param scaling_auto_create: The scaling_auto_create of this BaseServer.
        :type scaling_auto_create: bool
        """
        self._scaling_auto_create = scaling_auto_create

    @property
    def job_id(self):
        """Gets the job_id of this BaseServer.

        上一次执行job的id

        :return: The job_id of this BaseServer.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this BaseServer.

        上一次执行job的id

        :param job_id: The job_id of this BaseServer.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this BaseServer.

        :return: The job_type of this BaseServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this BaseServer.

        :param job_type: The job_type of this BaseServer.
        :type job_type: :class:`huaweicloudsdkworkspaceapp.v1.JobType`
        """
        self._job_type = job_type

    @property
    def job_status(self):
        """Gets the job_status of this BaseServer.

        :return: The job_status of this BaseServer.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.JobStatus`
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this BaseServer.

        :param job_status: The job_status of this BaseServer.
        :type job_status: :class:`huaweicloudsdkworkspaceapp.v1.JobStatus`
        """
        self._job_status = job_status

    @property
    def job_time(self):
        """Gets the job_time of this BaseServer.

        上一次执行job的执行时间

        :return: The job_time of this BaseServer.
        :rtype: datetime
        """
        return self._job_time

    @job_time.setter
    def job_time(self, job_time):
        """Sets the job_time of this BaseServer.

        上一次执行job的执行时间

        :param job_time: The job_time of this BaseServer.
        :type job_time: datetime
        """
        self._job_time = job_time

    @property
    def resource_pool_id(self):
        """Gets the resource_pool_id of this BaseServer.

        资源池ID

        :return: The resource_pool_id of this BaseServer.
        :rtype: str
        """
        return self._resource_pool_id

    @resource_pool_id.setter
    def resource_pool_id(self, resource_pool_id):
        """Sets the resource_pool_id of this BaseServer.

        资源池ID

        :param resource_pool_id: The resource_pool_id of this BaseServer.
        :type resource_pool_id: str
        """
        self._resource_pool_id = resource_pool_id

    @property
    def resource_pool_type(self):
        """Gets the resource_pool_type of this BaseServer.

        资源池类型 - private：私有资源池 - public: 工作资源池

        :return: The resource_pool_type of this BaseServer.
        :rtype: str
        """
        return self._resource_pool_type

    @resource_pool_type.setter
    def resource_pool_type(self, resource_pool_type):
        """Sets the resource_pool_type of this BaseServer.

        资源池类型 - private：私有资源池 - public: 工作资源池

        :param resource_pool_type: The resource_pool_type of this BaseServer.
        :type resource_pool_type: str
        """
        self._resource_pool_type = resource_pool_type

    @property
    def host_id(self):
        """Gets the host_id of this BaseServer.

        云专属主机id

        :return: The host_id of this BaseServer.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this BaseServer.

        云专属主机id

        :param host_id: The host_id of this BaseServer.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, BaseServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
