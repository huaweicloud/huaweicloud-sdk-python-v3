# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseServer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connect_ip': 'str',
        'cpu': 'str',
        'created': 'str',
        'description': 'str',
        'effect': 'int',
        'instance_id': 'str',
        'is_active': 'int',
        'name': 'str',
        'ram': 'str',
        'region': 'str',
        'resource_spec_code': 'str',
        'scene': 'str',
        'security_group_id': 'str',
        'specification': 'str',
        'status': 'str',
        'subnet_id': 'str',
        'task_status': 'str',
        'update_status': 'str',
        'version': 'str',
        'vpc_id': 'str',
        'zone': 'str',
        'server_id': 'str'
    }

    attribute_map = {
        'connect_ip': 'connect_ip',
        'cpu': 'cpu',
        'created': 'created',
        'description': 'description',
        'effect': 'effect',
        'instance_id': 'instance_id',
        'is_active': 'is_active',
        'name': 'name',
        'ram': 'ram',
        'region': 'region',
        'resource_spec_code': 'resource_spec_code',
        'scene': 'scene',
        'security_group_id': 'security_group_id',
        'specification': 'specification',
        'status': 'status',
        'subnet_id': 'subnet_id',
        'task_status': 'task_status',
        'update_status': 'update_status',
        'version': 'version',
        'vpc_id': 'vpc_id',
        'zone': 'zone',
        'server_id': 'server_id'
    }

    def __init__(self, connect_ip=None, cpu=None, created=None, description=None, effect=None, instance_id=None, is_active=None, name=None, ram=None, region=None, resource_spec_code=None, scene=None, security_group_id=None, specification=None, status=None, subnet_id=None, task_status=None, update_status=None, version=None, vpc_id=None, zone=None, server_id=None):
        r"""ResponseServer

        The model defined in huaweicloud sdk

        :param connect_ip: 连接IP
        :type connect_ip: str
        :param cpu: CPU数
        :type cpu: str
        :param created: 创建时间
        :type created: str
        :param description: 描述
        :type description: str
        :param effect: 实例冻结状态  - 1：冻结可释放 （默认）  - 2：冻结不可释放  - 3：冻结后不可续费
        :type effect: int
        :param instance_id: 实例ID
        :type instance_id: str
        :param is_active: 双机实例HA中用来标注实例为主机还是备机, -0: 主机 -1:备机
        :type is_active: int
        :param name: 实例名称
        :type name: str
        :param ram: 内存大小
        :type ram: str
        :param region: 所属REGION
        :type region: str
        :param resource_spec_code: 实例所属规格编码
        :type resource_spec_code: str
        :param scene: 冻结场景  - POLICE: 公安冻结  - ILLEGAL: 违规冻结  - VERIFY: 未实名认证冻结  - PARTNER: 合作伙伴冻结 - ARREAR: 普通冻结（普通）
        :type scene: str
        :param security_group_id: 安全组ID
        :type security_group_id: str
        :param specification: 资源规格类型编码
        :type specification: str
        :param status: 实例状态
        :type status: str
        :param subnet_id: 子网ID
        :type subnet_id: str
        :param task_status: 实例处理中状态
        :type task_status: str
        :param update_status: 升级状态  - SUCCESS：成功  - FAILED：失败  - UPGRADING：升级中
        :type update_status: str
        :param version: 版本号
        :type version: str
        :param vpc_id: VPC ID
        :type vpc_id: str
        :param zone: 所属区域
        :type zone: str
        :param server_id: 服务器ID
        :type server_id: str
        """
        
        

        self._connect_ip = None
        self._cpu = None
        self._created = None
        self._description = None
        self._effect = None
        self._instance_id = None
        self._is_active = None
        self._name = None
        self._ram = None
        self._region = None
        self._resource_spec_code = None
        self._scene = None
        self._security_group_id = None
        self._specification = None
        self._status = None
        self._subnet_id = None
        self._task_status = None
        self._update_status = None
        self._version = None
        self._vpc_id = None
        self._zone = None
        self._server_id = None
        self.discriminator = None

        if connect_ip is not None:
            self.connect_ip = connect_ip
        if cpu is not None:
            self.cpu = cpu
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if effect is not None:
            self.effect = effect
        if instance_id is not None:
            self.instance_id = instance_id
        if is_active is not None:
            self.is_active = is_active
        if name is not None:
            self.name = name
        if ram is not None:
            self.ram = ram
        if region is not None:
            self.region = region
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if scene is not None:
            self.scene = scene
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if specification is not None:
            self.specification = specification
        if status is not None:
            self.status = status
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if task_status is not None:
            self.task_status = task_status
        if update_status is not None:
            self.update_status = update_status
        if version is not None:
            self.version = version
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if zone is not None:
            self.zone = zone
        if server_id is not None:
            self.server_id = server_id

    @property
    def connect_ip(self):
        r"""Gets the connect_ip of this ResponseServer.

        连接IP

        :return: The connect_ip of this ResponseServer.
        :rtype: str
        """
        return self._connect_ip

    @connect_ip.setter
    def connect_ip(self, connect_ip):
        r"""Sets the connect_ip of this ResponseServer.

        连接IP

        :param connect_ip: The connect_ip of this ResponseServer.
        :type connect_ip: str
        """
        self._connect_ip = connect_ip

    @property
    def cpu(self):
        r"""Gets the cpu of this ResponseServer.

        CPU数

        :return: The cpu of this ResponseServer.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        r"""Sets the cpu of this ResponseServer.

        CPU数

        :param cpu: The cpu of this ResponseServer.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def created(self):
        r"""Gets the created of this ResponseServer.

        创建时间

        :return: The created of this ResponseServer.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ResponseServer.

        创建时间

        :param created: The created of this ResponseServer.
        :type created: str
        """
        self._created = created

    @property
    def description(self):
        r"""Gets the description of this ResponseServer.

        描述

        :return: The description of this ResponseServer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ResponseServer.

        描述

        :param description: The description of this ResponseServer.
        :type description: str
        """
        self._description = description

    @property
    def effect(self):
        r"""Gets the effect of this ResponseServer.

        实例冻结状态  - 1：冻结可释放 （默认）  - 2：冻结不可释放  - 3：冻结后不可续费

        :return: The effect of this ResponseServer.
        :rtype: int
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this ResponseServer.

        实例冻结状态  - 1：冻结可释放 （默认）  - 2：冻结不可释放  - 3：冻结后不可续费

        :param effect: The effect of this ResponseServer.
        :type effect: int
        """
        self._effect = effect

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ResponseServer.

        实例ID

        :return: The instance_id of this ResponseServer.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ResponseServer.

        实例ID

        :param instance_id: The instance_id of this ResponseServer.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def is_active(self):
        r"""Gets the is_active of this ResponseServer.

        双机实例HA中用来标注实例为主机还是备机, -0: 主机 -1:备机

        :return: The is_active of this ResponseServer.
        :rtype: int
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        r"""Sets the is_active of this ResponseServer.

        双机实例HA中用来标注实例为主机还是备机, -0: 主机 -1:备机

        :param is_active: The is_active of this ResponseServer.
        :type is_active: int
        """
        self._is_active = is_active

    @property
    def name(self):
        r"""Gets the name of this ResponseServer.

        实例名称

        :return: The name of this ResponseServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResponseServer.

        实例名称

        :param name: The name of this ResponseServer.
        :type name: str
        """
        self._name = name

    @property
    def ram(self):
        r"""Gets the ram of this ResponseServer.

        内存大小

        :return: The ram of this ResponseServer.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this ResponseServer.

        内存大小

        :param ram: The ram of this ResponseServer.
        :type ram: str
        """
        self._ram = ram

    @property
    def region(self):
        r"""Gets the region of this ResponseServer.

        所属REGION

        :return: The region of this ResponseServer.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ResponseServer.

        所属REGION

        :param region: The region of this ResponseServer.
        :type region: str
        """
        self._region = region

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this ResponseServer.

        实例所属规格编码

        :return: The resource_spec_code of this ResponseServer.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this ResponseServer.

        实例所属规格编码

        :param resource_spec_code: The resource_spec_code of this ResponseServer.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def scene(self):
        r"""Gets the scene of this ResponseServer.

        冻结场景  - POLICE: 公安冻结  - ILLEGAL: 违规冻结  - VERIFY: 未实名认证冻结  - PARTNER: 合作伙伴冻结 - ARREAR: 普通冻结（普通）

        :return: The scene of this ResponseServer.
        :rtype: str
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        r"""Sets the scene of this ResponseServer.

        冻结场景  - POLICE: 公安冻结  - ILLEGAL: 违规冻结  - VERIFY: 未实名认证冻结  - PARTNER: 合作伙伴冻结 - ARREAR: 普通冻结（普通）

        :param scene: The scene of this ResponseServer.
        :type scene: str
        """
        self._scene = scene

    @property
    def security_group_id(self):
        r"""Gets the security_group_id of this ResponseServer.

        安全组ID

        :return: The security_group_id of this ResponseServer.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        r"""Sets the security_group_id of this ResponseServer.

        安全组ID

        :param security_group_id: The security_group_id of this ResponseServer.
        :type security_group_id: str
        """
        self._security_group_id = security_group_id

    @property
    def specification(self):
        r"""Gets the specification of this ResponseServer.

        资源规格类型编码

        :return: The specification of this ResponseServer.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this ResponseServer.

        资源规格类型编码

        :param specification: The specification of this ResponseServer.
        :type specification: str
        """
        self._specification = specification

    @property
    def status(self):
        r"""Gets the status of this ResponseServer.

        实例状态

        :return: The status of this ResponseServer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResponseServer.

        实例状态

        :param status: The status of this ResponseServer.
        :type status: str
        """
        self._status = status

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ResponseServer.

        子网ID

        :return: The subnet_id of this ResponseServer.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ResponseServer.

        子网ID

        :param subnet_id: The subnet_id of this ResponseServer.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def task_status(self):
        r"""Gets the task_status of this ResponseServer.

        实例处理中状态

        :return: The task_status of this ResponseServer.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this ResponseServer.

        实例处理中状态

        :param task_status: The task_status of this ResponseServer.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def update_status(self):
        r"""Gets the update_status of this ResponseServer.

        升级状态  - SUCCESS：成功  - FAILED：失败  - UPGRADING：升级中

        :return: The update_status of this ResponseServer.
        :rtype: str
        """
        return self._update_status

    @update_status.setter
    def update_status(self, update_status):
        r"""Sets the update_status of this ResponseServer.

        升级状态  - SUCCESS：成功  - FAILED：失败  - UPGRADING：升级中

        :param update_status: The update_status of this ResponseServer.
        :type update_status: str
        """
        self._update_status = update_status

    @property
    def version(self):
        r"""Gets the version of this ResponseServer.

        版本号

        :return: The version of this ResponseServer.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ResponseServer.

        版本号

        :param version: The version of this ResponseServer.
        :type version: str
        """
        self._version = version

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ResponseServer.

        VPC ID

        :return: The vpc_id of this ResponseServer.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ResponseServer.

        VPC ID

        :param vpc_id: The vpc_id of this ResponseServer.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def zone(self):
        r"""Gets the zone of this ResponseServer.

        所属区域

        :return: The zone of this ResponseServer.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        r"""Sets the zone of this ResponseServer.

        所属区域

        :param zone: The zone of this ResponseServer.
        :type zone: str
        """
        self._zone = zone

    @property
    def server_id(self):
        r"""Gets the server_id of this ResponseServer.

        服务器ID

        :return: The server_id of this ResponseServer.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ResponseServer.

        服务器ID

        :param server_id: The server_id of this ResponseServer.
        :type server_id: str
        """
        self._server_id = server_id

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
        if not isinstance(other, ResponseServer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
