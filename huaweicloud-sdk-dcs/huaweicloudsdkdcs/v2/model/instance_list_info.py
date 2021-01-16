# coding: utf-8

import pprint
import re

import six





class InstanceListInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publicip_id': 'str',
        'vpc_name': 'str',
        'charging_mode': 'int',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'created_at': 'str',
        'enable_ssl': 'bool',
        'max_memory': 'int',
        'used_memory': 'int',
        'publicip_address': 'str',
        'capacity': 'int',
        'capacity_minor': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'engine': 'str',
        'engine_version': 'str',
        'service_upgrade': 'bool',
        'no_password_access': 'str',
        'service_task_id': 'str',
        'ip': 'str',
        'access_user': 'str',
        'instance_id': 'str',
        'enable_publicip': 'bool',
        'port': 'int',
        'user_id': 'str',
        'user_name': 'str',
        'domain_name': 'str',
        'name': 'str',
        'spec_code': 'str',
        'status': 'str',
        'tags': 'list[ResourceTag]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'publicip_id': 'publicip_id',
        'vpc_name': 'vpc_name',
        'charging_mode': 'charging_mode',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'created_at': 'created_at',
        'enable_ssl': 'enable_ssl',
        'max_memory': 'max_memory',
        'used_memory': 'used_memory',
        'publicip_address': 'publicip_address',
        'capacity': 'capacity',
        'capacity_minor': 'capacity_minor',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'engine': 'engine',
        'engine_version': 'engine_version',
        'service_upgrade': 'service_upgrade',
        'no_password_access': 'no_password_access',
        'service_task_id': 'service_task_id',
        'ip': 'ip',
        'access_user': 'access_user',
        'instance_id': 'instance_id',
        'enable_publicip': 'enable_publicip',
        'port': 'port',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'domain_name': 'domain_name',
        'name': 'name',
        'spec_code': 'spec_code',
        'status': 'status',
        'tags': 'tags',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, publicip_id=None, vpc_name=None, charging_mode=None, vpc_id=None, subnet_id=None, security_group_id=None, created_at=None, enable_ssl=None, max_memory=None, used_memory=None, publicip_address=None, capacity=None, capacity_minor=None, maintain_begin=None, maintain_end=None, engine=None, engine_version=None, service_upgrade=None, no_password_access=None, service_task_id=None, ip=None, access_user=None, instance_id=None, enable_publicip=None, port=None, user_id=None, user_name=None, domain_name=None, name=None, spec_code=None, status=None, tags=None, enterprise_project_id=None):
        """InstanceListInfo - a model defined in huaweicloud sdk"""
        
        

        self._publicip_id = None
        self._vpc_name = None
        self._charging_mode = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._created_at = None
        self._enable_ssl = None
        self._max_memory = None
        self._used_memory = None
        self._publicip_address = None
        self._capacity = None
        self._capacity_minor = None
        self._maintain_begin = None
        self._maintain_end = None
        self._engine = None
        self._engine_version = None
        self._service_upgrade = None
        self._no_password_access = None
        self._service_task_id = None
        self._ip = None
        self._access_user = None
        self._instance_id = None
        self._enable_publicip = None
        self._port = None
        self._user_id = None
        self._user_name = None
        self._domain_name = None
        self._name = None
        self._spec_code = None
        self._status = None
        self._tags = None
        self._enterprise_project_id = None
        self.discriminator = None

        if publicip_id is not None:
            self.publicip_id = publicip_id
        if vpc_name is not None:
            self.vpc_name = vpc_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if created_at is not None:
            self.created_at = created_at
        if enable_ssl is not None:
            self.enable_ssl = enable_ssl
        if max_memory is not None:
            self.max_memory = max_memory
        if used_memory is not None:
            self.used_memory = used_memory
        if publicip_address is not None:
            self.publicip_address = publicip_address
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
        if engine_version is not None:
            self.engine_version = engine_version
        if service_upgrade is not None:
            self.service_upgrade = service_upgrade
        if no_password_access is not None:
            self.no_password_access = no_password_access
        if service_task_id is not None:
            self.service_task_id = service_task_id
        if ip is not None:
            self.ip = ip
        if access_user is not None:
            self.access_user = access_user
        if instance_id is not None:
            self.instance_id = instance_id
        if enable_publicip is not None:
            self.enable_publicip = enable_publicip
        if port is not None:
            self.port = port
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if domain_name is not None:
            self.domain_name = domain_name
        if name is not None:
            self.name = name
        if spec_code is not None:
            self.spec_code = spec_code
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def publicip_id(self):
        """Gets the publicip_id of this InstanceListInfo.

        Redis缓存实例绑定的弹性IP地址的id。 如果未开启公网访问功能，该字段值为null。 

        :return: The publicip_id of this InstanceListInfo.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this InstanceListInfo.

        Redis缓存实例绑定的弹性IP地址的id。 如果未开启公网访问功能，该字段值为null。 

        :param publicip_id: The publicip_id of this InstanceListInfo.
        :type: str
        """
        self._publicip_id = publicip_id

    @property
    def vpc_name(self):
        """Gets the vpc_name of this InstanceListInfo.

        VPC的名称。

        :return: The vpc_name of this InstanceListInfo.
        :rtype: str
        """
        return self._vpc_name

    @vpc_name.setter
    def vpc_name(self, vpc_name):
        """Sets the vpc_name of this InstanceListInfo.

        VPC的名称。

        :param vpc_name: The vpc_name of this InstanceListInfo.
        :type: str
        """
        self._vpc_name = vpc_name

    @property
    def charging_mode(self):
        """Gets the charging_mode of this InstanceListInfo.

        计费模式，0表示按需计费，1表示包年/包月计费。

        :return: The charging_mode of this InstanceListInfo.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this InstanceListInfo.

        计费模式，0表示按需计费，1表示包年/包月计费。

        :param charging_mode: The charging_mode of this InstanceListInfo.
        :type: int
        """
        self._charging_mode = charging_mode

    @property
    def vpc_id(self):
        """Gets the vpc_id of this InstanceListInfo.

        VPC ID。

        :return: The vpc_id of this InstanceListInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this InstanceListInfo.

        VPC ID。

        :param vpc_id: The vpc_id of this InstanceListInfo.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this InstanceListInfo.

        子网ID。

        :return: The subnet_id of this InstanceListInfo.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this InstanceListInfo.

        子网ID。

        :param subnet_id: The subnet_id of this InstanceListInfo.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this InstanceListInfo.

        安全组ID。

        :return: The security_group_id of this InstanceListInfo.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this InstanceListInfo.

        安全组ID。

        :param security_group_id: The security_group_id of this InstanceListInfo.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def created_at(self):
        """Gets the created_at of this InstanceListInfo.

        创建时间。格式为：2017-03-31T12:24:46.297Z

        :return: The created_at of this InstanceListInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InstanceListInfo.

        创建时间。格式为：2017-03-31T12:24:46.297Z

        :param created_at: The created_at of this InstanceListInfo.
        :type: str
        """
        self._created_at = created_at

    @property
    def enable_ssl(self):
        """Gets the enable_ssl of this InstanceListInfo.

        Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 

        :return: The enable_ssl of this InstanceListInfo.
        :rtype: bool
        """
        return self._enable_ssl

    @enable_ssl.setter
    def enable_ssl(self, enable_ssl):
        """Sets the enable_ssl of this InstanceListInfo.

        Redis缓存实例开启公网访问功能时，是否选择支持ssl。 - true：开启 - false：不开启 

        :param enable_ssl: The enable_ssl of this InstanceListInfo.
        :type: bool
        """
        self._enable_ssl = enable_ssl

    @property
    def max_memory(self):
        """Gets the max_memory of this InstanceListInfo.

        总内存，单位：MB。

        :return: The max_memory of this InstanceListInfo.
        :rtype: int
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        """Sets the max_memory of this InstanceListInfo.

        总内存，单位：MB。

        :param max_memory: The max_memory of this InstanceListInfo.
        :type: int
        """
        self._max_memory = max_memory

    @property
    def used_memory(self):
        """Gets the used_memory of this InstanceListInfo.

        已使用的内存，单位：MB。

        :return: The used_memory of this InstanceListInfo.
        :rtype: int
        """
        return self._used_memory

    @used_memory.setter
    def used_memory(self, used_memory):
        """Sets the used_memory of this InstanceListInfo.

        已使用的内存，单位：MB。

        :param used_memory: The used_memory of this InstanceListInfo.
        :type: int
        """
        self._used_memory = used_memory

    @property
    def publicip_address(self):
        """Gets the publicip_address of this InstanceListInfo.

        Redis缓存实例绑定的弹性IP地址。 如果未开启公网访问功能，该字段值为null。 

        :return: The publicip_address of this InstanceListInfo.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        """Sets the publicip_address of this InstanceListInfo.

        Redis缓存实例绑定的弹性IP地址。 如果未开启公网访问功能，该字段值为null。 

        :param publicip_address: The publicip_address of this InstanceListInfo.
        :type: str
        """
        self._publicip_address = publicip_address

    @property
    def capacity(self):
        """Gets the capacity of this InstanceListInfo.

        缓存容量（G Byte）。

        :return: The capacity of this InstanceListInfo.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this InstanceListInfo.

        缓存容量（G Byte）。

        :param capacity: The capacity of this InstanceListInfo.
        :type: int
        """
        self._capacity = capacity

    @property
    def capacity_minor(self):
        """Gets the capacity_minor of this InstanceListInfo.

        小规格缓存容量（G Byte）。

        :return: The capacity_minor of this InstanceListInfo.
        :rtype: str
        """
        return self._capacity_minor

    @capacity_minor.setter
    def capacity_minor(self, capacity_minor):
        """Sets the capacity_minor of this InstanceListInfo.

        小规格缓存容量（G Byte）。

        :param capacity_minor: The capacity_minor of this InstanceListInfo.
        :type: str
        """
        self._capacity_minor = capacity_minor

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this InstanceListInfo.

        维护时间窗开始时间，为UTC时间，格式为HH:mm:ss。

        :return: The maintain_begin of this InstanceListInfo.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this InstanceListInfo.

        维护时间窗开始时间，为UTC时间，格式为HH:mm:ss。

        :param maintain_begin: The maintain_begin of this InstanceListInfo.
        :type: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this InstanceListInfo.

        维护时间窗结束时间，为UTC时间，格式为HH:mm:ss。

        :return: The maintain_end of this InstanceListInfo.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this InstanceListInfo.

        维护时间窗结束时间，为UTC时间，格式为HH:mm:ss。

        :param maintain_end: The maintain_end of this InstanceListInfo.
        :type: str
        """
        self._maintain_end = maintain_end

    @property
    def engine(self):
        """Gets the engine of this InstanceListInfo.

        缓存引擎。

        :return: The engine of this InstanceListInfo.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this InstanceListInfo.

        缓存引擎。

        :param engine: The engine of this InstanceListInfo.
        :type: str
        """
        self._engine = engine

    @property
    def engine_version(self):
        """Gets the engine_version of this InstanceListInfo.

        缓存版本。

        :return: The engine_version of this InstanceListInfo.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this InstanceListInfo.

        缓存版本。

        :param engine_version: The engine_version of this InstanceListInfo.
        :type: str
        """
        self._engine_version = engine_version

    @property
    def service_upgrade(self):
        """Gets the service_upgrade of this InstanceListInfo.

        实例是否存在升级任务。 - true：存在 - false：不存在 

        :return: The service_upgrade of this InstanceListInfo.
        :rtype: bool
        """
        return self._service_upgrade

    @service_upgrade.setter
    def service_upgrade(self, service_upgrade):
        """Sets the service_upgrade of this InstanceListInfo.

        实例是否存在升级任务。 - true：存在 - false：不存在 

        :param service_upgrade: The service_upgrade of this InstanceListInfo.
        :type: bool
        """
        self._service_upgrade = service_upgrade

    @property
    def no_password_access(self):
        """Gets the no_password_access of this InstanceListInfo.

        是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 

        :return: The no_password_access of this InstanceListInfo.
        :rtype: str
        """
        return self._no_password_access

    @no_password_access.setter
    def no_password_access(self, no_password_access):
        """Sets the no_password_access of this InstanceListInfo.

        是否允许免密码访问缓存实例。 - true：该实例无需密码即可访问。 - false：该实例必须通过密码认证才能访问。 

        :param no_password_access: The no_password_access of this InstanceListInfo.
        :type: str
        """
        self._no_password_access = no_password_access

    @property
    def service_task_id(self):
        """Gets the service_task_id of this InstanceListInfo.

        升级任务的ID。 - 当service_upgrade为true时，为升级任务的ID。 - 当service_upgrade为false时，该参数为空。 

        :return: The service_task_id of this InstanceListInfo.
        :rtype: str
        """
        return self._service_task_id

    @service_task_id.setter
    def service_task_id(self, service_task_id):
        """Sets the service_task_id of this InstanceListInfo.

        升级任务的ID。 - 当service_upgrade为true时，为升级任务的ID。 - 当service_upgrade为false时，该参数为空。 

        :param service_task_id: The service_task_id of this InstanceListInfo.
        :type: str
        """
        self._service_task_id = service_task_id

    @property
    def ip(self):
        """Gets the ip of this InstanceListInfo.

        连接缓存实例的IP地址。如果是集群实例，返回多个IP地址，使用逗号分隔。如：192.168.0.1，192.168.0.2。

        :return: The ip of this InstanceListInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this InstanceListInfo.

        连接缓存实例的IP地址。如果是集群实例，返回多个IP地址，使用逗号分隔。如：192.168.0.1，192.168.0.2。

        :param ip: The ip of this InstanceListInfo.
        :type: str
        """
        self._ip = ip

    @property
    def access_user(self):
        """Gets the access_user of this InstanceListInfo.

        通过密码认证访问缓存实例的认证用户名。 

        :return: The access_user of this InstanceListInfo.
        :rtype: str
        """
        return self._access_user

    @access_user.setter
    def access_user(self, access_user):
        """Sets the access_user of this InstanceListInfo.

        通过密码认证访问缓存实例的认证用户名。 

        :param access_user: The access_user of this InstanceListInfo.
        :type: str
        """
        self._access_user = access_user

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceListInfo.

        实例ID。

        :return: The instance_id of this InstanceListInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceListInfo.

        实例ID。

        :param instance_id: The instance_id of this InstanceListInfo.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def enable_publicip(self):
        """Gets the enable_publicip of this InstanceListInfo.

        Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 

        :return: The enable_publicip of this InstanceListInfo.
        :rtype: bool
        """
        return self._enable_publicip

    @enable_publicip.setter
    def enable_publicip(self, enable_publicip):
        """Sets the enable_publicip of this InstanceListInfo.

        Redis缓存实例是否开启公网访问功能。 - true：开启 - false：不开启 

        :param enable_publicip: The enable_publicip of this InstanceListInfo.
        :type: bool
        """
        self._enable_publicip = enable_publicip

    @property
    def port(self):
        """Gets the port of this InstanceListInfo.

        缓存的端口。

        :return: The port of this InstanceListInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InstanceListInfo.

        缓存的端口。

        :param port: The port of this InstanceListInfo.
        :type: int
        """
        self._port = port

    @property
    def user_id(self):
        """Gets the user_id of this InstanceListInfo.

        用户id。

        :return: The user_id of this InstanceListInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InstanceListInfo.

        用户id。

        :param user_id: The user_id of this InstanceListInfo.
        :type: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this InstanceListInfo.

        用户名。

        :return: The user_name of this InstanceListInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this InstanceListInfo.

        用户名。

        :param user_name: The user_name of this InstanceListInfo.
        :type: str
        """
        self._user_name = user_name

    @property
    def domain_name(self):
        """Gets the domain_name of this InstanceListInfo.

        实例的域名。

        :return: The domain_name of this InstanceListInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this InstanceListInfo.

        实例的域名。

        :param domain_name: The domain_name of this InstanceListInfo.
        :type: str
        """
        self._domain_name = domain_name

    @property
    def name(self):
        """Gets the name of this InstanceListInfo.

        实例名称。

        :return: The name of this InstanceListInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceListInfo.

        实例名称。

        :param name: The name of this InstanceListInfo.
        :type: str
        """
        self._name = name

    @property
    def spec_code(self):
        """Gets the spec_code of this InstanceListInfo.

        产品规格编码。

        :return: The spec_code of this InstanceListInfo.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this InstanceListInfo.

        产品规格编码。

        :param spec_code: The spec_code of this InstanceListInfo.
        :type: str
        """
        self._spec_code = spec_code

    @property
    def status(self):
        """Gets the status of this InstanceListInfo.

        实例状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)。

        :return: The status of this InstanceListInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceListInfo.

        实例状态。详细状态说明见[缓存实例状态说明](https://support.huaweicloud.com/api-dcs/dcs-api-0312047.html)。

        :param status: The status of this InstanceListInfo.
        :type: str
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this InstanceListInfo.

        实例标签键值。

        :return: The tags of this InstanceListInfo.
        :rtype: list[ResourceTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InstanceListInfo.

        实例标签键值。

        :param tags: The tags of this InstanceListInfo.
        :type: list[ResourceTag]
        """
        self._tags = tags

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this InstanceListInfo.

        企业项目ID。

        :return: The enterprise_project_id of this InstanceListInfo.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this InstanceListInfo.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this InstanceListInfo.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, InstanceListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
