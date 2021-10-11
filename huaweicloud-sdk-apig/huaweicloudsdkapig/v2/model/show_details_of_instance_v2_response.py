# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDetailsOfInstanceV2Response(SdkResponse):


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
        'project_id': 'str',
        'instance_name': 'str',
        'status': 'str',
        'instance_status': 'int',
        'type': 'str',
        'spec': 'str',
        'create_time': 'int',
        'enterprise_project_id': 'str',
        'eip_address': 'str',
        'charging_mode': 'int',
        'cbc_metadata': 'str',
        'description': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'security_group_id': 'str',
        'maintain_begin': 'str',
        'maintain_end': 'str',
        'ingress_ip': 'str',
        'user_id': 'str',
        'nat_eip_ipv6_cidr': 'str',
        'eip_ipv6_address': 'str',
        'nat_eip_address': 'str',
        'bandwidth_size': 'int',
        'available_zone_ids': 'str',
        'instance_version': 'str',
        'virsubnet_id': 'str',
        'roma_eip_address': 'str',
        'listeners': 'object',
        'supported_features': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'instance_name': 'instance_name',
        'status': 'status',
        'instance_status': 'instance_status',
        'type': 'type',
        'spec': 'spec',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'eip_address': 'eip_address',
        'charging_mode': 'charging_mode',
        'cbc_metadata': 'cbc_metadata',
        'description': 'description',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'security_group_id': 'security_group_id',
        'maintain_begin': 'maintain_begin',
        'maintain_end': 'maintain_end',
        'ingress_ip': 'ingress_ip',
        'user_id': 'user_id',
        'nat_eip_ipv6_cidr': 'nat_eip_ipv6_cidr',
        'eip_ipv6_address': 'eip_ipv6_address',
        'nat_eip_address': 'nat_eip_address',
        'bandwidth_size': 'bandwidth_size',
        'available_zone_ids': 'available_zone_ids',
        'instance_version': 'instance_version',
        'virsubnet_id': 'virsubnet_id',
        'roma_eip_address': 'roma_eip_address',
        'listeners': 'listeners',
        'supported_features': 'supported_features'
    }

    def __init__(self, id=None, project_id=None, instance_name=None, status=None, instance_status=None, type=None, spec=None, create_time=None, enterprise_project_id=None, eip_address=None, charging_mode=None, cbc_metadata=None, description=None, vpc_id=None, subnet_id=None, security_group_id=None, maintain_begin=None, maintain_end=None, ingress_ip=None, user_id=None, nat_eip_ipv6_cidr=None, eip_ipv6_address=None, nat_eip_address=None, bandwidth_size=None, available_zone_ids=None, instance_version=None, virsubnet_id=None, roma_eip_address=None, listeners=None, supported_features=None):
        """ShowDetailsOfInstanceV2Response - a model defined in huaweicloud sdk"""
        
        super(ShowDetailsOfInstanceV2Response, self).__init__()

        self._id = None
        self._project_id = None
        self._instance_name = None
        self._status = None
        self._instance_status = None
        self._type = None
        self._spec = None
        self._create_time = None
        self._enterprise_project_id = None
        self._eip_address = None
        self._charging_mode = None
        self._cbc_metadata = None
        self._description = None
        self._vpc_id = None
        self._subnet_id = None
        self._security_group_id = None
        self._maintain_begin = None
        self._maintain_end = None
        self._ingress_ip = None
        self._user_id = None
        self._nat_eip_ipv6_cidr = None
        self._eip_ipv6_address = None
        self._nat_eip_address = None
        self._bandwidth_size = None
        self._available_zone_ids = None
        self._instance_version = None
        self._virsubnet_id = None
        self._roma_eip_address = None
        self._listeners = None
        self._supported_features = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if instance_name is not None:
            self.instance_name = instance_name
        if status is not None:
            self.status = status
        if instance_status is not None:
            self.instance_status = instance_status
        if type is not None:
            self.type = type
        if spec is not None:
            self.spec = spec
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if eip_address is not None:
            self.eip_address = eip_address
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if cbc_metadata is not None:
            self.cbc_metadata = cbc_metadata
        if description is not None:
            self.description = description
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if maintain_begin is not None:
            self.maintain_begin = maintain_begin
        if maintain_end is not None:
            self.maintain_end = maintain_end
        if ingress_ip is not None:
            self.ingress_ip = ingress_ip
        if user_id is not None:
            self.user_id = user_id
        if nat_eip_ipv6_cidr is not None:
            self.nat_eip_ipv6_cidr = nat_eip_ipv6_cidr
        if eip_ipv6_address is not None:
            self.eip_ipv6_address = eip_ipv6_address
        if nat_eip_address is not None:
            self.nat_eip_address = nat_eip_address
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size
        if available_zone_ids is not None:
            self.available_zone_ids = available_zone_ids
        if instance_version is not None:
            self.instance_version = instance_version
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if roma_eip_address is not None:
            self.roma_eip_address = roma_eip_address
        if listeners is not None:
            self.listeners = listeners
        if supported_features is not None:
            self.supported_features = supported_features

    @property
    def id(self):
        """Gets the id of this ShowDetailsOfInstanceV2Response.

        实例ID

        :return: The id of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowDetailsOfInstanceV2Response.

        实例ID

        :param id: The id of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this ShowDetailsOfInstanceV2Response.

        实例所属租户ID

        :return: The project_id of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ShowDetailsOfInstanceV2Response.

        实例所属租户ID

        :param project_id: The project_id of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._project_id = project_id

    @property
    def instance_name(self):
        """Gets the instance_name of this ShowDetailsOfInstanceV2Response.

        实例名称

        :return: The instance_name of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ShowDetailsOfInstanceV2Response.

        实例名称

        :param instance_name: The instance_name of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def status(self):
        """Gets the status of this ShowDetailsOfInstanceV2Response.

        实例状态： - Creating：创建中 - CreateSuccess：创建成功 - CreateFail：创建失败 - Initing：初始化中 - Registering：注册中 - Running：运行中 - InitingFailed：初始化失败 - RegisterFailed：注册失败 - Installing：安装中 - InstallFailed：安装失败 - Updating：升级中 - UpdateFailed：升级失败 - Rollbacking：回滚中 - RollbackSuccess：回滚成功 - RollbackFailed：回滚失败 - Deleting：删除中 - DeleteFailed：删除失败 - Unregistering：注销中 - UnRegisterFailed：注销失败 - CreateTimeout：创建超时 - InitTimeout：初始化超时 - RegisterTimeout：注册超时 - InstallTimeout：安装超时 - UpdateTimeout：升级超时 - RollbackTimeout：回滚超时 - DeleteTimeout：删除超时 - UnregisterTimeout：注销超时 - Starting：启动中 - Freezing：冻结中 - Frozen：已冻结 - Restarting：重启中 - RestartFail：重启失败 - Unhealthy：实例异常 - RestartTimeout：重启超时

        :return: The status of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowDetailsOfInstanceV2Response.

        实例状态： - Creating：创建中 - CreateSuccess：创建成功 - CreateFail：创建失败 - Initing：初始化中 - Registering：注册中 - Running：运行中 - InitingFailed：初始化失败 - RegisterFailed：注册失败 - Installing：安装中 - InstallFailed：安装失败 - Updating：升级中 - UpdateFailed：升级失败 - Rollbacking：回滚中 - RollbackSuccess：回滚成功 - RollbackFailed：回滚失败 - Deleting：删除中 - DeleteFailed：删除失败 - Unregistering：注销中 - UnRegisterFailed：注销失败 - CreateTimeout：创建超时 - InitTimeout：初始化超时 - RegisterTimeout：注册超时 - InstallTimeout：安装超时 - UpdateTimeout：升级超时 - RollbackTimeout：回滚超时 - DeleteTimeout：删除超时 - UnregisterTimeout：注销超时 - Starting：启动中 - Freezing：冻结中 - Frozen：已冻结 - Restarting：重启中 - RestartFail：重启失败 - Unhealthy：实例异常 - RestartTimeout：重启超时

        :param status: The status of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._status = status

    @property
    def instance_status(self):
        """Gets the instance_status of this ShowDetailsOfInstanceV2Response.

        实例状态对应编号 - 1：创建中 - 2：创建成功 - 3：创建失败 - 4：初始化中 - 5：注册中 - 6：运行中 - 7：初始化失败 - 8：注册失败 - 10：安装中 - 11：安装失败 - 12：升级中 - 13：升级失败 - 20：回滚中 - 21：回滚成功 - 22：回滚失败 - 23：删除中 - 24：删除失败 - 25：注销中 - 26：注销失败 - 27：创建超时 - 28：初始化超时 - 29：注册超时 - 30：安装超时 - 31：升级超时 - 32：回滚超时 - 33：删除超时 - 34：注销超时 - 35：启动中 - 36：冻结中 - 37：已冻结 - 38：重启中 - 39：重启失败 - 40：实例异常 - 41：重启超时

        :return: The instance_status of this ShowDetailsOfInstanceV2Response.
        :rtype: int
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this ShowDetailsOfInstanceV2Response.

        实例状态对应编号 - 1：创建中 - 2：创建成功 - 3：创建失败 - 4：初始化中 - 5：注册中 - 6：运行中 - 7：初始化失败 - 8：注册失败 - 10：安装中 - 11：安装失败 - 12：升级中 - 13：升级失败 - 20：回滚中 - 21：回滚成功 - 22：回滚失败 - 23：删除中 - 24：删除失败 - 25：注销中 - 26：注销失败 - 27：创建超时 - 28：初始化超时 - 29：注册超时 - 30：安装超时 - 31：升级超时 - 32：回滚超时 - 33：删除超时 - 34：注销超时 - 35：启动中 - 36：冻结中 - 37：已冻结 - 38：重启中 - 39：重启失败 - 40：实例异常 - 41：重启超时

        :param instance_status: The instance_status of this ShowDetailsOfInstanceV2Response.
        :type: int
        """
        self._instance_status = instance_status

    @property
    def type(self):
        """Gets the type of this ShowDetailsOfInstanceV2Response.

        实例类型  默认apig

        :return: The type of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowDetailsOfInstanceV2Response.

        实例类型  默认apig

        :param type: The type of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._type = type

    @property
    def spec(self):
        """Gets the spec of this ShowDetailsOfInstanceV2Response.

        实例规格： - BASIC：基础版实例 - PROFESSIONAL：专业版实例 - ENTERPRISE：企业版实例 - PLATINUM：铂金版实例 - BASIC_IPV6：基础版IPV6实例 - PROFESSIONAL_IPV6：专业版IPV6实例 - ENTERPRISE_IPV6：企业版IPV6实例 - PLATINUM_IPV6：铂金版IPV6实例

        :return: The spec of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ShowDetailsOfInstanceV2Response.

        实例规格： - BASIC：基础版实例 - PROFESSIONAL：专业版实例 - ENTERPRISE：企业版实例 - PLATINUM：铂金版实例 - BASIC_IPV6：基础版IPV6实例 - PROFESSIONAL_IPV6：专业版IPV6实例 - ENTERPRISE_IPV6：企业版IPV6实例 - PLATINUM_IPV6：铂金版IPV6实例

        :param spec: The spec of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._spec = spec

    @property
    def create_time(self):
        """Gets the create_time of this ShowDetailsOfInstanceV2Response.

        实例创建时间。unix时间戳格式。

        :return: The create_time of this ShowDetailsOfInstanceV2Response.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowDetailsOfInstanceV2Response.

        实例创建时间。unix时间戳格式。

        :param create_time: The create_time of this ShowDetailsOfInstanceV2Response.
        :type: int
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowDetailsOfInstanceV2Response.

        企业项目ID，企业帐号必填

        :return: The enterprise_project_id of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowDetailsOfInstanceV2Response.

        企业项目ID，企业帐号必填

        :param enterprise_project_id: The enterprise_project_id of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def eip_address(self):
        """Gets the eip_address of this ShowDetailsOfInstanceV2Response.

        实例绑定的弹性IP地址

        :return: The eip_address of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this ShowDetailsOfInstanceV2Response.

        实例绑定的弹性IP地址

        :param eip_address: The eip_address of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._eip_address = eip_address

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ShowDetailsOfInstanceV2Response.

        实例计费方式： - 0：按需计费 - 1：包周期计费

        :return: The charging_mode of this ShowDetailsOfInstanceV2Response.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ShowDetailsOfInstanceV2Response.

        实例计费方式： - 0：按需计费 - 1：包周期计费

        :param charging_mode: The charging_mode of this ShowDetailsOfInstanceV2Response.
        :type: int
        """
        self._charging_mode = charging_mode

    @property
    def cbc_metadata(self):
        """Gets the cbc_metadata of this ShowDetailsOfInstanceV2Response.

        包周期计费订单编号

        :return: The cbc_metadata of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._cbc_metadata

    @cbc_metadata.setter
    def cbc_metadata(self, cbc_metadata):
        """Sets the cbc_metadata of this ShowDetailsOfInstanceV2Response.

        包周期计费订单编号

        :param cbc_metadata: The cbc_metadata of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._cbc_metadata = cbc_metadata

    @property
    def description(self):
        """Gets the description of this ShowDetailsOfInstanceV2Response.

        实例描述

        :return: The description of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowDetailsOfInstanceV2Response.

        实例描述

        :param description: The description of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._description = description

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ShowDetailsOfInstanceV2Response.

        虚拟私有云ID。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询VPC列表”章节。 

        :return: The vpc_id of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ShowDetailsOfInstanceV2Response.

        虚拟私有云ID。  获取方法如下：   - 方法1：登录虚拟私有云服务的控制台界面，在虚拟私有云的详情页面查找VPC ID。   - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询VPC列表”章节。 

        :param vpc_id: The vpc_id of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ShowDetailsOfInstanceV2Response.

        子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询子网列表”章节。 

        :return: The subnet_id of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ShowDetailsOfInstanceV2Response.

        子网的网络ID。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找网络ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询子网列表”章节。 

        :param subnet_id: The subnet_id of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ShowDetailsOfInstanceV2Response.

        指定实例所属的安全组。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询安全组列表”章节。 

        :return: The security_group_id of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ShowDetailsOfInstanceV2Response.

        指定实例所属的安全组。  获取方法如下： - 方法1：登录虚拟私有云服务的控制台界面，在安全组的详情页面查找安全组ID。 - 方法2：通过虚拟私有云服务的API接口查询，具体方法请参见《虚拟私有云服务API参考》的“查询安全组列表”章节。 

        :param security_group_id: The security_group_id of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._security_group_id = security_group_id

    @property
    def maintain_begin(self):
        """Gets the maintain_begin of this ShowDetailsOfInstanceV2Response.

        '维护时间窗开始时间。时间格式为 xx:00:00，xx取值为02,06,10,14,18,22。'  '在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。'

        :return: The maintain_begin of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._maintain_begin

    @maintain_begin.setter
    def maintain_begin(self, maintain_begin):
        """Sets the maintain_begin of this ShowDetailsOfInstanceV2Response.

        '维护时间窗开始时间。时间格式为 xx:00:00，xx取值为02,06,10,14,18,22。'  '在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次。'

        :param maintain_begin: The maintain_begin of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._maintain_begin = maintain_begin

    @property
    def maintain_end(self):
        """Gets the maintain_end of this ShowDetailsOfInstanceV2Response.

        '维护时间窗结束时间。时间格式为 xx:00:00，与维护时间窗开始时间相差4个小时。'  '在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次'。

        :return: The maintain_end of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._maintain_end

    @maintain_end.setter
    def maintain_end(self, maintain_end):
        """Sets the maintain_end of this ShowDetailsOfInstanceV2Response.

        '维护时间窗结束时间。时间格式为 xx:00:00，与维护时间窗开始时间相差4个小时。'  '在这个时间段内，运维人员可以对该实例的节点进行维护操作。维护期间，业务可以正常使用，可能会发生闪断。维护操作通常几个月一次'。

        :param maintain_end: The maintain_end of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._maintain_end = maintain_end

    @property
    def ingress_ip(self):
        """Gets the ingress_ip of this ShowDetailsOfInstanceV2Response.

        实例入口，虚拟私有云访问地址

        :return: The ingress_ip of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._ingress_ip

    @ingress_ip.setter
    def ingress_ip(self, ingress_ip):
        """Sets the ingress_ip of this ShowDetailsOfInstanceV2Response.

        实例入口，虚拟私有云访问地址

        :param ingress_ip: The ingress_ip of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._ingress_ip = ingress_ip

    @property
    def user_id(self):
        """Gets the user_id of this ShowDetailsOfInstanceV2Response.

        实例所属用户ID

        :return: The user_id of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ShowDetailsOfInstanceV2Response.

        实例所属用户ID

        :param user_id: The user_id of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._user_id = user_id

    @property
    def nat_eip_ipv6_cidr(self):
        """Gets the nat_eip_ipv6_cidr of this ShowDetailsOfInstanceV2Response.

        出公网网段 (IPv6)  。  当前仅部分region部分可用区支持IPv6

        :return: The nat_eip_ipv6_cidr of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._nat_eip_ipv6_cidr

    @nat_eip_ipv6_cidr.setter
    def nat_eip_ipv6_cidr(self, nat_eip_ipv6_cidr):
        """Sets the nat_eip_ipv6_cidr of this ShowDetailsOfInstanceV2Response.

        出公网网段 (IPv6)  。  当前仅部分region部分可用区支持IPv6

        :param nat_eip_ipv6_cidr: The nat_eip_ipv6_cidr of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._nat_eip_ipv6_cidr = nat_eip_ipv6_cidr

    @property
    def eip_ipv6_address(self):
        """Gets the eip_ipv6_address of this ShowDetailsOfInstanceV2Response.

        弹性IP地址(IPv6)。  当前仅部分region部分可用区支持IPv6

        :return: The eip_ipv6_address of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._eip_ipv6_address

    @eip_ipv6_address.setter
    def eip_ipv6_address(self, eip_ipv6_address):
        """Sets the eip_ipv6_address of this ShowDetailsOfInstanceV2Response.

        弹性IP地址(IPv6)。  当前仅部分region部分可用区支持IPv6

        :param eip_ipv6_address: The eip_ipv6_address of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._eip_ipv6_address = eip_ipv6_address

    @property
    def nat_eip_address(self):
        """Gets the nat_eip_address of this ShowDetailsOfInstanceV2Response.

        实例出公网IP

        :return: The nat_eip_address of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._nat_eip_address

    @nat_eip_address.setter
    def nat_eip_address(self, nat_eip_address):
        """Sets the nat_eip_address of this ShowDetailsOfInstanceV2Response.

        实例出公网IP

        :param nat_eip_address: The nat_eip_address of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._nat_eip_address = nat_eip_address

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this ShowDetailsOfInstanceV2Response.

        出公网带宽

        :return: The bandwidth_size of this ShowDetailsOfInstanceV2Response.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this ShowDetailsOfInstanceV2Response.

        出公网带宽

        :param bandwidth_size: The bandwidth_size of this ShowDetailsOfInstanceV2Response.
        :type: int
        """
        self._bandwidth_size = bandwidth_size

    @property
    def available_zone_ids(self):
        """Gets the available_zone_ids of this ShowDetailsOfInstanceV2Response.

        可用区

        :return: The available_zone_ids of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._available_zone_ids

    @available_zone_ids.setter
    def available_zone_ids(self, available_zone_ids):
        """Sets the available_zone_ids of this ShowDetailsOfInstanceV2Response.

        可用区

        :param available_zone_ids: The available_zone_ids of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._available_zone_ids = available_zone_ids

    @property
    def instance_version(self):
        """Gets the instance_version of this ShowDetailsOfInstanceV2Response.

        实例版本编号

        :return: The instance_version of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._instance_version

    @instance_version.setter
    def instance_version(self, instance_version):
        """Sets the instance_version of this ShowDetailsOfInstanceV2Response.

        实例版本编号

        :param instance_version: The instance_version of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._instance_version = instance_version

    @property
    def virsubnet_id(self):
        """Gets the virsubnet_id of this ShowDetailsOfInstanceV2Response.

        子网的网络ID。  暂不支持

        :return: The virsubnet_id of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        """Sets the virsubnet_id of this ShowDetailsOfInstanceV2Response.

        子网的网络ID。  暂不支持

        :param virsubnet_id: The virsubnet_id of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def roma_eip_address(self):
        """Gets the roma_eip_address of this ShowDetailsOfInstanceV2Response.

        roma弹性公网IP。  暂不支持

        :return: The roma_eip_address of this ShowDetailsOfInstanceV2Response.
        :rtype: str
        """
        return self._roma_eip_address

    @roma_eip_address.setter
    def roma_eip_address(self, roma_eip_address):
        """Sets the roma_eip_address of this ShowDetailsOfInstanceV2Response.

        roma弹性公网IP。  暂不支持

        :param roma_eip_address: The roma_eip_address of this ShowDetailsOfInstanceV2Response.
        :type: str
        """
        self._roma_eip_address = roma_eip_address

    @property
    def listeners(self):
        """Gets the listeners of this ShowDetailsOfInstanceV2Response.

        监听信息  暂不支持

        :return: The listeners of this ShowDetailsOfInstanceV2Response.
        :rtype: object
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this ShowDetailsOfInstanceV2Response.

        监听信息  暂不支持

        :param listeners: The listeners of this ShowDetailsOfInstanceV2Response.
        :type: object
        """
        self._listeners = listeners

    @property
    def supported_features(self):
        """Gets the supported_features of this ShowDetailsOfInstanceV2Response.

        实例支持的特性列表

        :return: The supported_features of this ShowDetailsOfInstanceV2Response.
        :rtype: list[str]
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this ShowDetailsOfInstanceV2Response.

        实例支持的特性列表

        :param supported_features: The supported_features of this ShowDetailsOfInstanceV2Response.
        :type: list[str]
        """
        self._supported_features = supported_features

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
        if not isinstance(other, ShowDetailsOfInstanceV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
