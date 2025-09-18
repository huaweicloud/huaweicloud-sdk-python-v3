# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePremiumInstanceResponse(SdkResponse):

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
        'instancename': 'str',
        'server_id': 'str',
        'region': 'str',
        'zone': 'str',
        'arch': 'str',
        'cpu_flavor': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'service_ip': 'str',
        'service_ipv6': 'str',
        'float_ip': 'str',
        'security_group_ids': 'list[str]',
        'status': 'int',
        'run_status': 'int',
        'access_status': 'int',
        'upgradable': 'int',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'specification': 'str',
        'hosts': 'list[IdHostnameEntry]',
        'volume_type': 'str',
        'cluster_id': 'str',
        'pool_id': 'str',
        'charge_mode': 'int'
    }

    attribute_map = {
        'id': 'id',
        'instancename': 'instancename',
        'server_id': 'serverId',
        'region': 'region',
        'zone': 'zone',
        'arch': 'arch',
        'cpu_flavor': 'cpu_flavor',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'service_ip': 'service_ip',
        'service_ipv6': 'service_ipv6',
        'float_ip': 'floatIp',
        'security_group_ids': 'security_group_ids',
        'status': 'status',
        'run_status': 'run_status',
        'access_status': 'access_status',
        'upgradable': 'upgradable',
        'cloud_service_type': 'cloudServiceType',
        'resource_type': 'resourceType',
        'resource_spec_code': 'resourceSpecCode',
        'specification': 'specification',
        'hosts': 'hosts',
        'volume_type': 'volume_type',
        'cluster_id': 'cluster_id',
        'pool_id': 'pool_id',
        'charge_mode': 'charge_mode'
    }

    def __init__(self, id=None, instancename=None, server_id=None, region=None, zone=None, arch=None, cpu_flavor=None, vpc_id=None, subnet_id=None, service_ip=None, service_ipv6=None, float_ip=None, security_group_ids=None, status=None, run_status=None, access_status=None, upgradable=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, specification=None, hosts=None, volume_type=None, cluster_id=None, pool_id=None, charge_mode=None):
        r"""UpdatePremiumInstanceResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 独享引擎ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param instancename: **参数解释：** 独享引擎名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type instancename: str
        :param server_id: **参数解释：** 独享引擎ECS ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type server_id: str
        :param region: **参数解释：** Region代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type region: str
        :param zone: **参数解释：** 可用区代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type zone: str
        :param arch: **参数解释：** CPU架构代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type arch: str
        :param cpu_flavor: **参数解释：** ECS规格代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cpu_flavor: str
        :param vpc_id: **参数解释：** 独享引擎所在VPC ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type vpc_id: str
        :param subnet_id: **参数解释：** 独享引擎所在VPC的子网ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subnet_id: str
        :param service_ip: **参数解释：** 独享引擎的业务面IP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type service_ip: str
        :param service_ipv6: **参数解释：** 独享引擎的业务面IPV6地址 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type service_ipv6: str
        :param float_ip: **参数解释：** 独享引擎的管理面IP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type float_ip: str
        :param security_group_ids: **参数解释：** 独享引擎ECS绑定的安全组 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type security_group_ids: list[str]
        :param status: **参数解释：** 独享引擎计费状态（0：正常计费,1：冻结（资源和数据会保留，但租户无法再正常使用云服务）,2：终止（资源和数据将清除）,3：受限（UDS控制用户桶访问权限）） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type status: int
        :param run_status: **参数解释：** &#39;独享引擎运行状态（0：创建中,1：运行中,2：删除中,3：已删除,4：创建失败,5：已冻结,6：异常,7：更新中,8：更新失败）&#39; **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type run_status: int
        :param access_status: **参数解释：** 独享引擎接入状态（0：未接入，1：已接入） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type access_status: int
        :param upgradable: **参数解释：** 独享引擎是否可升级（0：不可升级，1：可升级） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type upgradable: int
        :param cloud_service_type: **参数解释：** 云服务代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cloud_service_type: str
        :param resource_type: **参数解释：** 云服务资源类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type resource_type: str
        :param resource_spec_code: **参数解释：** 云服务资源代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type resource_spec_code: str
        :param specification: **参数解释：** 独享引擎ECS规格，如\&quot;8vCPUs | 16GB\&quot; **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type specification: str
        :param hosts: **参数解释：** 独享引擎防护的域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type hosts: list[:class:`huaweicloudsdkwaf.v1.IdHostnameEntry`]
        :param volume_type: **参数解释：** 存储类型（可选） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type volume_type: str
        :param cluster_id: **参数解释：** 存储资源池ID（可选） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cluster_id: str
        :param pool_id: **参数解释：** 独享引擎所在WAF组的ID（仅适用特殊独享模式） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type pool_id: str
        :param charge_mode: **参数解释：** &#39;计费模式。0: 包周期；1:按需&#39; **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type charge_mode: int
        """
        
        super(UpdatePremiumInstanceResponse, self).__init__()

        self._id = None
        self._instancename = None
        self._server_id = None
        self._region = None
        self._zone = None
        self._arch = None
        self._cpu_flavor = None
        self._vpc_id = None
        self._subnet_id = None
        self._service_ip = None
        self._service_ipv6 = None
        self._float_ip = None
        self._security_group_ids = None
        self._status = None
        self._run_status = None
        self._access_status = None
        self._upgradable = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._specification = None
        self._hosts = None
        self._volume_type = None
        self._cluster_id = None
        self._pool_id = None
        self._charge_mode = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instancename is not None:
            self.instancename = instancename
        if server_id is not None:
            self.server_id = server_id
        if region is not None:
            self.region = region
        if zone is not None:
            self.zone = zone
        if arch is not None:
            self.arch = arch
        if cpu_flavor is not None:
            self.cpu_flavor = cpu_flavor
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if service_ip is not None:
            self.service_ip = service_ip
        if service_ipv6 is not None:
            self.service_ipv6 = service_ipv6
        if float_ip is not None:
            self.float_ip = float_ip
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if status is not None:
            self.status = status
        if run_status is not None:
            self.run_status = run_status
        if access_status is not None:
            self.access_status = access_status
        if upgradable is not None:
            self.upgradable = upgradable
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_spec_code is not None:
            self.resource_spec_code = resource_spec_code
        if specification is not None:
            self.specification = specification
        if hosts is not None:
            self.hosts = hosts
        if volume_type is not None:
            self.volume_type = volume_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if pool_id is not None:
            self.pool_id = pool_id
        if charge_mode is not None:
            self.charge_mode = charge_mode

    @property
    def id(self):
        r"""Gets the id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this UpdatePremiumInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def instancename(self):
        r"""Gets the instancename of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The instancename of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._instancename

    @instancename.setter
    def instancename(self, instancename):
        r"""Sets the instancename of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param instancename: The instancename of this UpdatePremiumInstanceResponse.
        :type instancename: str
        """
        self._instancename = instancename

    @property
    def server_id(self):
        r"""Gets the server_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎ECS ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The server_id of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎ECS ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param server_id: The server_id of this UpdatePremiumInstanceResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def region(self):
        r"""Gets the region of this UpdatePremiumInstanceResponse.

        **参数解释：** Region代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The region of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this UpdatePremiumInstanceResponse.

        **参数解释：** Region代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param region: The region of this UpdatePremiumInstanceResponse.
        :type region: str
        """
        self._region = region

    @property
    def zone(self):
        r"""Gets the zone of this UpdatePremiumInstanceResponse.

        **参数解释：** 可用区代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The zone of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        r"""Sets the zone of this UpdatePremiumInstanceResponse.

        **参数解释：** 可用区代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param zone: The zone of this UpdatePremiumInstanceResponse.
        :type zone: str
        """
        self._zone = zone

    @property
    def arch(self):
        r"""Gets the arch of this UpdatePremiumInstanceResponse.

        **参数解释：** CPU架构代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The arch of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this UpdatePremiumInstanceResponse.

        **参数解释：** CPU架构代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param arch: The arch of this UpdatePremiumInstanceResponse.
        :type arch: str
        """
        self._arch = arch

    @property
    def cpu_flavor(self):
        r"""Gets the cpu_flavor of this UpdatePremiumInstanceResponse.

        **参数解释：** ECS规格代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cpu_flavor of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._cpu_flavor

    @cpu_flavor.setter
    def cpu_flavor(self, cpu_flavor):
        r"""Sets the cpu_flavor of this UpdatePremiumInstanceResponse.

        **参数解释：** ECS规格代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cpu_flavor: The cpu_flavor of this UpdatePremiumInstanceResponse.
        :type cpu_flavor: str
        """
        self._cpu_flavor = cpu_flavor

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎所在VPC ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The vpc_id of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎所在VPC ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param vpc_id: The vpc_id of this UpdatePremiumInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎所在VPC的子网ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subnet_id of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎所在VPC的子网ID **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subnet_id: The subnet_id of this UpdatePremiumInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def service_ip(self):
        r"""Gets the service_ip of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎的业务面IP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The service_ip of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._service_ip

    @service_ip.setter
    def service_ip(self, service_ip):
        r"""Sets the service_ip of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎的业务面IP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param service_ip: The service_ip of this UpdatePremiumInstanceResponse.
        :type service_ip: str
        """
        self._service_ip = service_ip

    @property
    def service_ipv6(self):
        r"""Gets the service_ipv6 of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎的业务面IPV6地址 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The service_ipv6 of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._service_ipv6

    @service_ipv6.setter
    def service_ipv6(self, service_ipv6):
        r"""Sets the service_ipv6 of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎的业务面IPV6地址 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param service_ipv6: The service_ipv6 of this UpdatePremiumInstanceResponse.
        :type service_ipv6: str
        """
        self._service_ipv6 = service_ipv6

    @property
    def float_ip(self):
        r"""Gets the float_ip of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎的管理面IP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The float_ip of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._float_ip

    @float_ip.setter
    def float_ip(self, float_ip):
        r"""Sets the float_ip of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎的管理面IP **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param float_ip: The float_ip of this UpdatePremiumInstanceResponse.
        :type float_ip: str
        """
        self._float_ip = float_ip

    @property
    def security_group_ids(self):
        r"""Gets the security_group_ids of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎ECS绑定的安全组 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The security_group_ids of this UpdatePremiumInstanceResponse.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        r"""Sets the security_group_ids of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎ECS绑定的安全组 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param security_group_ids: The security_group_ids of this UpdatePremiumInstanceResponse.
        :type security_group_ids: list[str]
        """
        self._security_group_ids = security_group_ids

    @property
    def status(self):
        r"""Gets the status of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎计费状态（0：正常计费,1：冻结（资源和数据会保留，但租户无法再正常使用云服务）,2：终止（资源和数据将清除）,3：受限（UDS控制用户桶访问权限）） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The status of this UpdatePremiumInstanceResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎计费状态（0：正常计费,1：冻结（资源和数据会保留，但租户无法再正常使用云服务）,2：终止（资源和数据将清除）,3：受限（UDS控制用户桶访问权限）） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param status: The status of this UpdatePremiumInstanceResponse.
        :type status: int
        """
        self._status = status

    @property
    def run_status(self):
        r"""Gets the run_status of this UpdatePremiumInstanceResponse.

        **参数解释：** '独享引擎运行状态（0：创建中,1：运行中,2：删除中,3：已删除,4：创建失败,5：已冻结,6：异常,7：更新中,8：更新失败）' **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The run_status of this UpdatePremiumInstanceResponse.
        :rtype: int
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        r"""Sets the run_status of this UpdatePremiumInstanceResponse.

        **参数解释：** '独享引擎运行状态（0：创建中,1：运行中,2：删除中,3：已删除,4：创建失败,5：已冻结,6：异常,7：更新中,8：更新失败）' **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param run_status: The run_status of this UpdatePremiumInstanceResponse.
        :type run_status: int
        """
        self._run_status = run_status

    @property
    def access_status(self):
        r"""Gets the access_status of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎接入状态（0：未接入，1：已接入） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The access_status of this UpdatePremiumInstanceResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        r"""Sets the access_status of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎接入状态（0：未接入，1：已接入） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param access_status: The access_status of this UpdatePremiumInstanceResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def upgradable(self):
        r"""Gets the upgradable of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎是否可升级（0：不可升级，1：可升级） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The upgradable of this UpdatePremiumInstanceResponse.
        :rtype: int
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        r"""Sets the upgradable of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎是否可升级（0：不可升级，1：可升级） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param upgradable: The upgradable of this UpdatePremiumInstanceResponse.
        :type upgradable: int
        """
        self._upgradable = upgradable

    @property
    def cloud_service_type(self):
        r"""Gets the cloud_service_type of this UpdatePremiumInstanceResponse.

        **参数解释：** 云服务代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cloud_service_type of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        r"""Sets the cloud_service_type of this UpdatePremiumInstanceResponse.

        **参数解释：** 云服务代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cloud_service_type: The cloud_service_type of this UpdatePremiumInstanceResponse.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this UpdatePremiumInstanceResponse.

        **参数解释：** 云服务资源类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The resource_type of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this UpdatePremiumInstanceResponse.

        **参数解释：** 云服务资源类型 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param resource_type: The resource_type of this UpdatePremiumInstanceResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        r"""Gets the resource_spec_code of this UpdatePremiumInstanceResponse.

        **参数解释：** 云服务资源代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The resource_spec_code of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        r"""Sets the resource_spec_code of this UpdatePremiumInstanceResponse.

        **参数解释：** 云服务资源代码 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param resource_spec_code: The resource_spec_code of this UpdatePremiumInstanceResponse.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def specification(self):
        r"""Gets the specification of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎ECS规格，如\"8vCPUs | 16GB\" **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The specification of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎ECS规格，如\"8vCPUs | 16GB\" **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param specification: The specification of this UpdatePremiumInstanceResponse.
        :type specification: str
        """
        self._specification = specification

    @property
    def hosts(self):
        r"""Gets the hosts of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎防护的域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The hosts of this UpdatePremiumInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.IdHostnameEntry`]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        r"""Sets the hosts of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎防护的域名 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param hosts: The hosts of this UpdatePremiumInstanceResponse.
        :type hosts: list[:class:`huaweicloudsdkwaf.v1.IdHostnameEntry`]
        """
        self._hosts = hosts

    @property
    def volume_type(self):
        r"""Gets the volume_type of this UpdatePremiumInstanceResponse.

        **参数解释：** 存储类型（可选） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The volume_type of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this UpdatePremiumInstanceResponse.

        **参数解释：** 存储类型（可选） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param volume_type: The volume_type of this UpdatePremiumInstanceResponse.
        :type volume_type: str
        """
        self._volume_type = volume_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 存储资源池ID（可选） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cluster_id of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 存储资源池ID（可选） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cluster_id: The cluster_id of this UpdatePremiumInstanceResponse.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def pool_id(self):
        r"""Gets the pool_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎所在WAF组的ID（仅适用特殊独享模式） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The pool_id of this UpdatePremiumInstanceResponse.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        r"""Sets the pool_id of this UpdatePremiumInstanceResponse.

        **参数解释：** 独享引擎所在WAF组的ID（仅适用特殊独享模式） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param pool_id: The pool_id of this UpdatePremiumInstanceResponse.
        :type pool_id: str
        """
        self._pool_id = pool_id

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this UpdatePremiumInstanceResponse.

        **参数解释：** '计费模式。0: 包周期；1:按需' **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The charge_mode of this UpdatePremiumInstanceResponse.
        :rtype: int
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this UpdatePremiumInstanceResponse.

        **参数解释：** '计费模式。0: 包周期；1:按需' **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param charge_mode: The charge_mode of this UpdatePremiumInstanceResponse.
        :type charge_mode: int
        """
        self._charge_mode = charge_mode

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
        if not isinstance(other, UpdatePremiumInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
