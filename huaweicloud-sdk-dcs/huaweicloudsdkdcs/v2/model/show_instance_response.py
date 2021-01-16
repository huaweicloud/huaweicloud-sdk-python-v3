# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowInstanceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vpc_name': 'str',
        'charging_mode': 'int',
        'vpc_id': 'str',
        'user_name': 'str',
        'created_at': 'str',
        'description': 'str',
        'security_group_id': 'str',
        'security_group_name': 'str',
        'max_memory': 'int',
        'used_memory': 'int',
        'capacity': 'int',
        'capacity_minor': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'engine': 'str',
        'no_password_access': 'str',
        'ip': 'str',
        'instance_backup_policy': 'BackupPolicy',
        'az_codes': 'list[str]',
        'access_user': 'str',
        'instance_id': 'str',
        'port': 'int',
        'user_id': 'str',
        'name': 'str',
        'spec_code': 'str',
        'subnet_id': 'str',
        'subnet_name': 'str',
        'subnet_cidr': 'str',
        'engine_version': 'str',
        'order_id': 'str',
        'status': 'str',
        'domain_name': 'str',
        'enable_publicip': 'bool',
        'publicip_id': 'str',
        'publicip_address': 'str',
        'enable_ssl': 'bool',
        'service_upgrade': 'bool',
        'service_task_id': 'str',
        'enterprise_project_id': 'str',
        'backend_addrs': 'str'
    }

    attribute_map = {
        'vpc_name': 'vpc_name',
        'charging_mode': 'charging_mode',
        'vpc_id': 'vpc_id',
        'user_name': 'user_name',
        'created_at': 'created_at',
        'description': 'description',
        'security_group_id': 'security_group_id',
        'security_group_name': 'security_group_name',
        'max_memory': 'max_memory',
        'used_memory': 'used_memory',
        'capacity': 'capacity',
        'capacity_minor': 'capacity_minor',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'engine': 'engine',
        'no_password_access': 'no_password_access',
        'ip': 'ip',
        'instance_backup_policy': 'instance_backup_policy',
        'az_codes': 'az_codes',
        'access_user': 'access_user',
        'instance_id': 'instance_id',
        'port': 'port',
        'user_id': 'user_id',
        'name': 'name',
        'spec_code': 'spec_code',
        'subnet_id': 'subnet_id',
        'subnet_name': 'subnet_name',
        'subnet_cidr': 'subnet_cidr',
        'engine_version': 'engine_version',
        'order_id': 'order_id',
        'status': 'status',
        'domain_name': 'domain_name',
        'enable_publicip': 'enable_publicip',
        'publicip_id': 'publicip_id',
        'publicip_address': 'publicip_address',
        'enable_ssl': 'enable_ssl',
        'service_upgrade': 'service_upgrade',
        'service_task_id': 'service_task_id',
        'enterprise_project_id': 'enterprise_project_id',
        'backend_addrs': 'backend_addrs'
    }

    def __init__(self, vpc_name=None, charging_mode=None, vpc_id=None, user_name=None, created_at=None, description=None, security_group_id=None, security_group_name=None, max_memory=None, used_memory=None, capacity=None, capacity_minor=None, maintain_begin=None, maintain_end=None, engine=None, no_password_access=None, ip=None, instance_backup_policy=None, az_codes=None, access_user=None, instance_id=None, port=None, user_id=None, name=None, spec_code=None, subnet_id=None, subnet_name=None, subnet_cidr=None, engine_version=None, order_id=None, status=None, domain_name=None, enable_publicip=None, publicip_id=None, publicip_address=None, enable_ssl=None, service_upgrade=None, service_task_id=None, enterprise_project_id=None, backend_addrs=None):
        """ShowInstanceResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._vpc_name = None
        self._charging_mode = None
        self._vpc_id = None
        self._user_name = None
        self._created_at = None
        self._description = None
        self._security_group_id = None
        self._security_group_name = None
        self._max_memory = None
        self._used_memory = None
        self._capacity = None
        self._capacity_minor = None
        self._maintain_begin = None
        self._maintain_end = None
        self._engine = None
        self._no_password_access = None
        self._ip = None
        self._instance_backup_policy = None
        self._az_codes = None
        self._access_user = None
        self._instance_id = None
        self._port = None
        self._user_id = None
        self._name = None
        self._spec_code = None
        self._subnet_id = None
        self._subnet_name = None
        self._subnet_cidr = None
        self._engine_version = None
        self._order_id = None
        self._status = None
        self._domain_name = None
        self._enable_publicip = None
        self._publicip_id = None
        self._publicip_address = None
        self._enable_ssl = None
        self._service_upgrade = None
        self._service_task_id = None
        self._enterprise_project_id = None
        self._backend_addrs = None
        self.discriminator = None

        if vpc_name is not None:
            self.vpc_name = vpc_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if user_name is not None:
            self.user_name = user_name
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if security_group_name is not None:
            self.security_group_name = security_group_name
        if max_memory is not None:
            self.max_memory = max_memory
        if used_memory is not None:
            self.used_memory = used_memory
        if capacity is not None:
            self.capacity = capacity
        if capacity_minor is not None:
            self.capacity_minor = capacity_minor
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if engine is not None:
            self.engine = engine
        if no_password_access is not None:
            self.no_password_access = no_password_access
        if ip is not None:
            self.ip = ip
        if instance_backup_policy is not None:
            self.instance_backup_policy = instance_backup_policy
        if az_codes is not None:
            self.az_codes = az_codes
        if access_user is not None:
            self.access_user = access_user
        if instance_id is not None:
            self.instance_id = instance_id
        if port is not None:
            self.port = port
        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if spec_code is not None:
            self.spec_code = spec_code
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if subnet_name is not None:
            self.subnet_name = subnet_name
        if subnet_cidr is not None:
            self.subnet_cidr = subnet_cidr
        if engine_version is not None:
            self.engine_version = engine_version
        if order_id is not None:
            self.order_id = order_id
        if status is not None:
            self.status = status
        if domain_name is not None:
            self.domain_name = domain_name
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if publicip_id is not None:
            self.publicip_id = publicip_id
        if publicip_address is not None:
            self.publicip_address = publicip_address
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if service_upgrade is not None:
            self.service_upgrade = service_upgrade
        if service_task_id is not None:
            self.service_task_id = service_task_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if backend_addrs is not None:
            self.backend_addrs = backend_addrs

    @property
    def vpc_name(self):
        """Gets the vpc_name of this ShowInstanceResponse.

        VPC的名称。

        :return: The vpc_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this ShowInstanceResponse.

        VPC的名称。

        :param vpc_name: The vpc_name of this ShowInstanceResponse.
        :type: str
        """
        self._vpc_name = vpc_name

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ShowInstanceResponse.

        付费模式，0表示按需计费，1表示包年/包月计费。

        :return: The charging_mode of this ShowInstanceResponse.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ShowInstanceResponse.

        付费模式，0表示按需计费，1表示包年/包月计费。

        :param charging_mode: The charging_mode of this ShowInstanceResponse.
        :type: int
        """
        self._charging_mode = charging_mode

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowInstanceResponse.

        VPC ID

        :return: The vpc_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowInstanceResponse.

        VPC ID

        :param vpc_id: The vpc_id of this ShowInstanceResponse.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def user_name(self):
        """Gets the user_name of this ShowInstanceResponse.

        用户名。

        :return: The user_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowInstanceResponse.

        用户名。

        :param user_name: The user_name of this ShowInstanceResponse.
        :type: str
        """
        self._user_name = user_name

    @property
    def created_at(self):
        """Gets the created_at of this ShowInstanceResponse.

        完成创建时间。格式为：2017-03-31T12:24:46.297Z

        :return: The created_at of this ShowInstanceResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowInstanceResponse.

        完成创建时间。格式为：2017-03-31T12:24:46.297Z

        :param created_at: The created_at of this ShowInstanceResponse.
        :type: str
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ShowInstanceResponse.

        实例描述。

        :return: The description of this ShowInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowInstanceResponse.

        实例描述。

        :param description: The description of this ShowInstanceResponse.
        :type: str
        """
        self._description = description

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ShowInstanceResponse.

        安全组ID。

        :return: The security_group_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ShowInstanceResponse.

        安全组ID。

        :param security_group_id: The security_group_id of this ShowInstanceResponse.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def security_group_name(self):
        """Gets the security_group_name of this ShowInstanceResponse.

        租户安全组名称。

        :return: The security_group_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._security_group_name

    @security_group_name.setter
    def security_group_name(self, security_group_name):
        """Sets the security_group_name of this ShowInstanceResponse.

        租户安全组名称。

        :param security_group_name: The security_group_name of this ShowInstanceResponse.
        :type: str
        """
        self._security_group_name = security_group_name

    @property
    def max_memory(self):
        """Gets the max_memory of this ShowInstanceResponse.

        总内存，单位：MB。

        :return: The max_memory of this ShowInstanceResponse.
        :rtype: int
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """Sets the max_memory of this ShowInstanceResponse.

        总内存，单位：MB。

        :param max_memory: The max_memory of this ShowInstanceResponse.
        :type: int
        """
        self._max_memory = max_memory

    @property
    def used_memory(self):
        """Gets the used_memory of this ShowInstanceResponse.

        已使用的内存，单位：MB。

        :return: The used_memory of this ShowInstanceResponse.
        :rtype: int
        """
        return self._used_memory

    @used_memory.setter
    def used_memory(self, used_memory):
        """Sets the used_memory of this ShowInstanceResponse.

        已使用的内存，单位：MB。

        :param used_memory: The used_memory of this ShowInstanceResponse.
        :type: int
        """
        self._used_memory = used_memory

    @property
    def capacity(self):
        """Gets the capacity of this ShowInstanceResponse.

        缓存实例的容量（G Byte）。

        :return: The capacity of this ShowInstanceResponse.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this ShowInstanceResponse.

        缓存实例的容量（G Byte）。

        :param capacity: The capacity of this ShowInstanceResponse.
        :type: int
        """
        self._capacity = capacity

    @property
    def capacity_minor(self):
        """Gets the capacity_minor of this ShowInstanceResponse.

        单机小规格的缓存容量。

        :return: The capacity_minor of this ShowInstanceResponse.
        :rtype: str
        """
        return self._capacity_minor

    @capacity_minor.setter
    def capacity_minor(self, capacity_minor):
        """Sets the capacity_minor of this ShowInstanceResponse.

        单机小规格的缓存容量。

        :param capacity_minor: The capacity_minor of this ShowInstanceResponse.
        :type: str
        """
        self._capacity_minor = capacity_minor

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this ShowInstanceResponse.

        维护时间窗开始时间，为UTC时间，格式为HH:mm:ss

        :return: The maintain_begin of this ShowInstanceResponse.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this ShowInstanceResponse.

        维护时间窗开始时间，为UTC时间，格式为HH:mm:ss

        :param maintain_begin: The maintain_begin of this ShowInstanceResponse.
        :type: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this ShowInstanceResponse.

        维护时间窗结束时间，为UTC时间，格式为HH:mm:ss

        :return: The maintain_end of this ShowInstanceResponse.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this ShowInstanceResponse.

        维护时间窗结束时间，为UTC时间，格式为HH:mm:ss

        :param maintain_end: The maintain_end of this ShowInstanceResponse.
        :type: str
        """
        self._maintain_end = maintain_end

    @property
    def engine(self):
        """Gets the engine of this ShowInstanceResponse.

        缓存实例的引擎类型。

        :return: The engine of this ShowInstanceResponse.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ShowInstanceResponse.

        缓存实例的引擎类型。

        :param engine: The engine of this ShowInstanceResponse.
        :type: str
        """
        self._engine = engine

    @property
    def no_password_access(self):
        """Gets the no_password_access of this ShowInstanceResponse.

        是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 

        :return: The no_password_access of this ShowInstanceResponse.
        :rtype: str
        """
        return self._no_password_access

    @no_password_access.setter
    def no_password_access(self, no_password_access):
        """Sets the no_password_access of this ShowInstanceResponse.

        是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 

        :param no_password_access: The no_password_access of this ShowInstanceResponse.
        :type: str
        """
        self._no_password_access = no_password_access

    @property
    def ip(self):
        """Gets the ip of this ShowInstanceResponse.

        连接缓存实例的IP地址。如果是集群实例，返回多个IP地址，使用逗号分隔。如：192.168.0.1，192.168.0.2。

        :return: The ip of this ShowInstanceResponse.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ShowInstanceResponse.

        连接缓存实例的IP地址。如果是集群实例，返回多个IP地址，使用逗号分隔。如：192.168.0.1，192.168.0.2。

        :param ip: The ip of this ShowInstanceResponse.
        :type: str
        """
        self._ip = ip

    @property
    def instance_backup_policy(self):
        """Gets the instance_backup_policy of this ShowInstanceResponse.


        :return: The instance_backup_policy of this ShowInstanceResponse.
        :rtype: BackupPolicy
        """
        return self._instance_backup_policy

    @instance_backup_policy.setter
    def instance_backup_policy(self, instance_backup_policy):
        """Sets the instance_backup_policy of this ShowInstanceResponse.


        :param instance_backup_policy: The instance_backup_policy of this ShowInstanceResponse.
        :type: BackupPolicy
        """
        self._instance_backup_policy = instance_backup_policy

    @property
    def az_codes(self):
        """Gets the az_codes of this ShowInstanceResponse.

        实例所在的可用区。返回“可用区Code”

        :return: The az_codes of this ShowInstanceResponse.
        :rtype: list[str]
        """
        return self._az_codes

    @az_codes.setter
    def az_codes(self, az_codes):
        """Sets the az_codes of this ShowInstanceResponse.

        实例所在的可用区。返回“可用区Code”

        :param az_codes: The az_codes of this ShowInstanceResponse.
        :type: list[str]
        """
        self._az_codes = az_codes

    @property
    def access_user(self):
        """Gets the access_user of this ShowInstanceResponse.

        通过密码认证访问缓存实例的认证用户名。

        :return: The access_user of this ShowInstanceResponse.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this ShowInstanceResponse.

        通过密码认证访问缓存实例的认证用户名。

        :param access_user: The access_user of this ShowInstanceResponse.
        :type: str
        """
        self._access_user = access_user

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowInstanceResponse.

        实例ID。

        :return: The instance_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowInstanceResponse.

        实例ID。

        :param instance_id: The instance_id of this ShowInstanceResponse.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def port(self):
        """Gets the port of this ShowInstanceResponse.

        缓存的端口。

        :return: The port of this ShowInstanceResponse.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ShowInstanceResponse.

        缓存的端口。

        :param port: The port of this ShowInstanceResponse.
        :type: int
        """
        self._port = port

    @property
    def user_id(self):
        """Gets the user_id of this ShowInstanceResponse.

        用户id。

        :return: The user_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ShowInstanceResponse.

        用户id。

        :param user_id: The user_id of this ShowInstanceResponse.
        :type: str
        """
        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this ShowInstanceResponse.

        实例名称。

        :return: The name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowInstanceResponse.

        实例名称。

        :param name: The name of this ShowInstanceResponse.
        :type: str
        """
        self._name = name

    @property
    def spec_code(self):
        """Gets the spec_code of this ShowInstanceResponse.

        产品规格编码

        :return: The spec_code of this ShowInstanceResponse.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this ShowInstanceResponse.

        产品规格编码

        :param spec_code: The spec_code of this ShowInstanceResponse.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowInstanceResponse.

        子网ID。

        :return: The subnet_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowInstanceResponse.

        子网ID。

        :param subnet_id: The subnet_id of this ShowInstanceResponse.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def subnet_name(self):
        """Gets the subnet_name of this ShowInstanceResponse.

        子网名称。

        :return: The subnet_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this ShowInstanceResponse.

        子网名称。

        :param subnet_name: The subnet_name of this ShowInstanceResponse.
        :type: str
        """
        self._subnet_name = subnet_name

    @property
    def subnet_cidr(self):
        """Gets the subnet_cidr of this ShowInstanceResponse.

        子网网段。

        :return: The subnet_cidr of this ShowInstanceResponse.
        :rtype: str
        """
        return self._subnet_cidr

    @subnet_cidr.setter
    def subnet_cidr(self, subnet_cidr):
        """Sets the subnet_cidr of this ShowInstanceResponse.

        子网网段。

        :param subnet_cidr: The subnet_cidr of this ShowInstanceResponse.
        :type: str
        """
        self._subnet_cidr = subnet_cidr

    @property
    def engine_version(self):
        """Gets the engine_version of this ShowInstanceResponse.

        缓存版本。

        :return: The engine_version of this ShowInstanceResponse.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this ShowInstanceResponse.

        缓存版本。

        :param engine_version: The engine_version of this ShowInstanceResponse.
        :type: str
        """
        self._engine_version = engine_version

    @property
    def order_id(self):
        """Gets the order_id of this ShowInstanceResponse.

        订单ID。

        :return: The order_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowInstanceResponse.

        订单ID。

        :param order_id: The order_id of this ShowInstanceResponse.
        :type: str
        """
        self._order_id = order_id

    @property
    def status(self):
        """Gets the status of this ShowInstanceResponse.

        缓存实例的状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)

        :return: The status of this ShowInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowInstanceResponse.

        缓存实例的状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)

        :param status: The status of this ShowInstanceResponse.
        :type: str
        """
        self._status = status

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowInstanceResponse.

        实例的域名。

        :return: The domain_name of this ShowInstanceResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowInstanceResponse.

        实例的域名。

        :param domain_name: The domain_name of this ShowInstanceResponse.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def enable_publicip(self):
        """Gets the enable_publicip of this ShowInstanceResponse.

        Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 

        :return: The enable_publicip of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        """Sets the enable_publicip of this ShowInstanceResponse.

        Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 

        :param enable_publicip: The enable_publicip of this ShowInstanceResponse.
        :type: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def publicip_id(self):
        """Gets the publicip_id of this ShowInstanceResponse.

        Redis缓存实例绑定的弹性IP地址的id。 如果未开启公网访问功能，该字段值为null。 

        :return: The publicip_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this ShowInstanceResponse.

        Redis缓存实例绑定的弹性IP地址的id。 如果未开启公网访问功能，该字段值为null。 

        :param publicip_id: The publicip_id of this ShowInstanceResponse.
        :type: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_address(self):
        """Gets the publicip_address of this ShowInstanceResponse.

        Redis缓存实例绑定的弹性IP地址。 如果未开启公网访问功能，该字段值为null。 

        :return: The publicip_address of this ShowInstanceResponse.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        """Sets the publicip_address of this ShowInstanceResponse.

        Redis缓存实例绑定的弹性IP地址。 如果未开启公网访问功能，该字段值为null。 

        :param publicip_address: The publicip_address of this ShowInstanceResponse.
        :type: str
        """
        self._publicip_address = publicip_address

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this ShowInstanceResponse.

        Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 

        :return: The enable_ssl of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this ShowInstanceResponse.

        Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 

        :param enable_ssl: The enable_ssl of this ShowInstanceResponse.
        :type: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def service_upgrade(self):
        """Gets the service_upgrade of this ShowInstanceResponse.

        实例是否存在升级任务。 - true：存在 - false：不存在 

        :return: The service_upgrade of this ShowInstanceResponse.
        :rtype: bool
        """
        return self._service_upgrade

    @service_upgrade.setter
    def service_upgrade(self, service_upgrade):
        """Sets the service_upgrade of this ShowInstanceResponse.

        实例是否存在升级任务。 - true：存在 - false：不存在 

        :param service_upgrade: The service_upgrade of this ShowInstanceResponse.
        :type: bool
        """
        self._service_upgrade = service_upgrade

    @property
    def service_task_id(self):
        """Gets the service_task_id of this ShowInstanceResponse.

        升级任务的ID。 - 当service_upgrade为true时，为升级任务的ID。 - 当service_upgrade为false时，该参数为空。 

        :return: The service_task_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._service_task_id

    @service_task_id.setter
    def service_task_id(self, service_task_id):
        """Sets the service_task_id of this ShowInstanceResponse.

        升级任务的ID。 - 当service_upgrade为true时，为升级任务的ID。 - 当service_upgrade为false时，该参数为空。 

        :param service_task_id: The service_task_id of this ShowInstanceResponse.
        :type: str
        """
        self._service_task_id = service_task_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowInstanceResponse.

        企业项目ID。

        :return: The enterprise_project_id of this ShowInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowInstanceResponse.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ShowInstanceResponse.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def backend_addrs(self):
        """Gets the backend_addrs of this ShowInstanceResponse.

        集群实例的后端服务地址。

        :return: The backend_addrs of this ShowInstanceResponse.
        :rtype: str
        """
        return self._backend_addrs

    @backend_addrs.setter
    def backend_addrs(self, backend_addrs):
        """Sets the backend_addrs of this ShowInstanceResponse.

        集群实例的后端服务地址。

        :param backend_addrs: The backend_addrs of this ShowInstanceResponse.
        :type: str
        """
        self._backend_addrs = backend_addrs

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
        if not isinstance(other, ShowInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
