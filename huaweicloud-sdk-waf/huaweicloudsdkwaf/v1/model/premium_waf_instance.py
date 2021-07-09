# coding: utf-8

import re
import six





class PremiumWafInstance:


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
        'security_group_id': 'list[str]',
        'mgr_security_group_id': 'str',
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
        'pool_id': 'str'
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
        'security_group_id': 'securityGroupId',
        'mgr_security_group_id': 'mgrSecurityGroupId',
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
        'pool_id': 'pool_id'
    }

    def __init__(self, id=None, instancename=None, server_id=None, region=None, zone=None, arch=None, cpu_flavor=None, vpc_id=None, subnet_id=None, service_ip=None, service_ipv6=None, float_ip=None, security_group_id=None, mgr_security_group_id=None, status=None, run_status=None, access_status=None, upgradable=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, specification=None, hosts=None, volume_type=None, cluster_id=None, pool_id=None):
        """PremiumWafInstance - a model defined in huaweicloud sdk"""
        
        

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
        self._security_group_id = None
        self._mgr_security_group_id = None
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
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if mgr_security_group_id is not None:
            self.mgr_security_group_id = mgr_security_group_id
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

    @property
    def id(self):
        """Gets the id of this PremiumWafInstance.

        独享引擎ID

        :return: The id of this PremiumWafInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PremiumWafInstance.

        独享引擎ID

        :param id: The id of this PremiumWafInstance.
        :type: str
        """
        self._id = id

    @property
    def instancename(self):
        """Gets the instancename of this PremiumWafInstance.

        独享引擎名称

        :return: The instancename of this PremiumWafInstance.
        :rtype: str
        """
        return self._instancename

    @instancename.setter
    def instancename(self, instancename):
        """Sets the instancename of this PremiumWafInstance.

        独享引擎名称

        :param instancename: The instancename of this PremiumWafInstance.
        :type: str
        """
        self._instancename = instancename

    @property
    def server_id(self):
        """Gets the server_id of this PremiumWafInstance.

        独享引擎ECS ID

        :return: The server_id of this PremiumWafInstance.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this PremiumWafInstance.

        独享引擎ECS ID

        :param server_id: The server_id of this PremiumWafInstance.
        :type: str
        """
        self._server_id = server_id

    @property
    def region(self):
        """Gets the region of this PremiumWafInstance.

        Region代码

        :return: The region of this PremiumWafInstance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this PremiumWafInstance.

        Region代码

        :param region: The region of this PremiumWafInstance.
        :type: str
        """
        self._region = region

    @property
    def zone(self):
        """Gets the zone of this PremiumWafInstance.

        可用区代码

        :return: The zone of this PremiumWafInstance.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this PremiumWafInstance.

        可用区代码

        :param zone: The zone of this PremiumWafInstance.
        :type: str
        """
        self._zone = zone

    @property
    def arch(self):
        """Gets the arch of this PremiumWafInstance.

        CPU架构代码

        :return: The arch of this PremiumWafInstance.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this PremiumWafInstance.

        CPU架构代码

        :param arch: The arch of this PremiumWafInstance.
        :type: str
        """
        self._arch = arch

    @property
    def cpu_flavor(self):
        """Gets the cpu_flavor of this PremiumWafInstance.

        ECS规格代码

        :return: The cpu_flavor of this PremiumWafInstance.
        :rtype: str
        """
        return self._cpu_flavor

    @cpu_flavor.setter
    def cpu_flavor(self, cpu_flavor):
        """Sets the cpu_flavor of this PremiumWafInstance.

        ECS规格代码

        :param cpu_flavor: The cpu_flavor of this PremiumWafInstance.
        :type: str
        """
        self._cpu_flavor = cpu_flavor

    @property
    def vpc_id(self):
        """Gets the vpc_id of this PremiumWafInstance.

        独享引擎所在VPC ID

        :return: The vpc_id of this PremiumWafInstance.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this PremiumWafInstance.

        独享引擎所在VPC ID

        :param vpc_id: The vpc_id of this PremiumWafInstance.
        :type: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this PremiumWafInstance.

        独享引擎所在VPC的子网ID

        :return: The subnet_id of this PremiumWafInstance.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this PremiumWafInstance.

        独享引擎所在VPC的子网ID

        :param subnet_id: The subnet_id of this PremiumWafInstance.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def service_ip(self):
        """Gets the service_ip of this PremiumWafInstance.

        独享引擎的业务面IP

        :return: The service_ip of this PremiumWafInstance.
        :rtype: str
        """
        return self._service_ip

    @service_ip.setter
    def service_ip(self, service_ip):
        """Sets the service_ip of this PremiumWafInstance.

        独享引擎的业务面IP

        :param service_ip: The service_ip of this PremiumWafInstance.
        :type: str
        """
        self._service_ip = service_ip

    @property
    def service_ipv6(self):
        """Gets the service_ipv6 of this PremiumWafInstance.

        独享引擎的业务面IPV6地址

        :return: The service_ipv6 of this PremiumWafInstance.
        :rtype: str
        """
        return self._service_ipv6

    @service_ipv6.setter
    def service_ipv6(self, service_ipv6):
        """Sets the service_ipv6 of this PremiumWafInstance.

        独享引擎的业务面IPV6地址

        :param service_ipv6: The service_ipv6 of this PremiumWafInstance.
        :type: str
        """
        self._service_ipv6 = service_ipv6

    @property
    def float_ip(self):
        """Gets the float_ip of this PremiumWafInstance.

        独享引擎的管理面IP

        :return: The float_ip of this PremiumWafInstance.
        :rtype: str
        """
        return self._float_ip

    @float_ip.setter
    def float_ip(self, float_ip):
        """Sets the float_ip of this PremiumWafInstance.

        独享引擎的管理面IP

        :param float_ip: The float_ip of this PremiumWafInstance.
        :type: str
        """
        self._float_ip = float_ip

    @property
    def security_group_id(self):
        """Gets the security_group_id of this PremiumWafInstance.

        独享引擎ECS绑定的安全组

        :return: The security_group_id of this PremiumWafInstance.
        :rtype: list[str]
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this PremiumWafInstance.

        独享引擎ECS绑定的安全组

        :param security_group_id: The security_group_id of this PremiumWafInstance.
        :type: list[str]
        """
        self._security_group_id = security_group_id

    @property
    def mgr_security_group_id(self):
        """Gets the mgr_security_group_id of this PremiumWafInstance.

        独享引擎ECS绑定的用于WAF服务的安全组

        :return: The mgr_security_group_id of this PremiumWafInstance.
        :rtype: str
        """
        return self._mgr_security_group_id

    @mgr_security_group_id.setter
    def mgr_security_group_id(self, mgr_security_group_id):
        """Sets the mgr_security_group_id of this PremiumWafInstance.

        独享引擎ECS绑定的用于WAF服务的安全组

        :param mgr_security_group_id: The mgr_security_group_id of this PremiumWafInstance.
        :type: str
        """
        self._mgr_security_group_id = mgr_security_group_id

    @property
    def status(self):
        """Gets the status of this PremiumWafInstance.

        独享引擎计费状态

        :return: The status of this PremiumWafInstance.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PremiumWafInstance.

        独享引擎计费状态

        :param status: The status of this PremiumWafInstance.
        :type: int
        """
        self._status = status

    @property
    def run_status(self):
        """Gets the run_status of this PremiumWafInstance.

        独享引擎允许状态

        :return: The run_status of this PremiumWafInstance.
        :rtype: int
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this PremiumWafInstance.

        独享引擎允许状态

        :param run_status: The run_status of this PremiumWafInstance.
        :type: int
        """
        self._run_status = run_status

    @property
    def access_status(self):
        """Gets the access_status of this PremiumWafInstance.

        独享引擎接入状态

        :return: The access_status of this PremiumWafInstance.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this PremiumWafInstance.

        独享引擎接入状态

        :param access_status: The access_status of this PremiumWafInstance.
        :type: int
        """
        self._access_status = access_status

    @property
    def upgradable(self):
        """Gets the upgradable of this PremiumWafInstance.

        独享引擎是否可升级

        :return: The upgradable of this PremiumWafInstance.
        :rtype: int
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        """Sets the upgradable of this PremiumWafInstance.

        独享引擎是否可升级

        :param upgradable: The upgradable of this PremiumWafInstance.
        :type: int
        """
        self._upgradable = upgradable

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this PremiumWafInstance.

        云服务代码

        :return: The cloud_service_type of this PremiumWafInstance.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this PremiumWafInstance.

        云服务代码

        :param cloud_service_type: The cloud_service_type of this PremiumWafInstance.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this PremiumWafInstance.

        云服务资源类型

        :return: The resource_type of this PremiumWafInstance.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PremiumWafInstance.

        云服务资源类型

        :param resource_type: The resource_type of this PremiumWafInstance.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this PremiumWafInstance.

        云服务资源代码

        :return: The resource_spec_code of this PremiumWafInstance.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this PremiumWafInstance.

        云服务资源代码

        :param resource_spec_code: The resource_spec_code of this PremiumWafInstance.
        :type: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def specification(self):
        """Gets the specification of this PremiumWafInstance.

        独享引擎ECS规格，如\"8vCPUs | 16GB\"

        :return: The specification of this PremiumWafInstance.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this PremiumWafInstance.

        独享引擎ECS规格，如\"8vCPUs | 16GB\"

        :param specification: The specification of this PremiumWafInstance.
        :type: str
        """
        self._specification = specification

    @property
    def hosts(self):
        """Gets the hosts of this PremiumWafInstance.

        独享引擎防护的域名

        :return: The hosts of this PremiumWafInstance.
        :rtype: list[IdHostnameEntry]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this PremiumWafInstance.

        独享引擎防护的域名

        :param hosts: The hosts of this PremiumWafInstance.
        :type: list[IdHostnameEntry]
        """
        self._hosts = hosts

    @property
    def volume_type(self):
        """Gets the volume_type of this PremiumWafInstance.

        存储类型（可选）

        :return: The volume_type of this PremiumWafInstance.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        """Sets the volume_type of this PremiumWafInstance.

        存储类型（可选）

        :param volume_type: The volume_type of this PremiumWafInstance.
        :type: str
        """
        self._volume_type = volume_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this PremiumWafInstance.

        存储资源池ID（可选）

        :return: The cluster_id of this PremiumWafInstance.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this PremiumWafInstance.

        存储资源池ID（可选）

        :param cluster_id: The cluster_id of this PremiumWafInstance.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def pool_id(self):
        """Gets the pool_id of this PremiumWafInstance.

        独享引擎所在WAF组的ID（仅适用特殊独享模式）

        :return: The pool_id of this PremiumWafInstance.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this PremiumWafInstance.

        独享引擎所在WAF组的ID（仅适用特殊独享模式）

        :param pool_id: The pool_id of this PremiumWafInstance.
        :type: str
        """
        self._pool_id = pool_id

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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PremiumWafInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
