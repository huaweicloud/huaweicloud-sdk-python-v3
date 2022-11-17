# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenameInstanceResponse(SdkResponse):

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
        'region': 'str',
        'zone': 'str',
        'arch': 'str',
        'cpu_flavor': 'str',
        'vpc_id': 'str',
        'subnet_id': 'str',
        'service_ip': 'str',
        'security_group_ids': 'list[str]',
        'status': 'int',
        'run_status': 'int',
        'access_status': 'int',
        'upgradable': 'int',
        'cloud_service_type': 'str',
        'resource_type': 'str',
        'resource_spec_code': 'str',
        'specification': 'str',
        'server_id': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'instancename': 'instancename',
        'region': 'region',
        'zone': 'zone',
        'arch': 'arch',
        'cpu_flavor': 'cpu_flavor',
        'vpc_id': 'vpc_id',
        'subnet_id': 'subnet_id',
        'service_ip': 'service_ip',
        'security_group_ids': 'security_group_ids',
        'status': 'status',
        'run_status': 'run_status',
        'access_status': 'access_status',
        'upgradable': 'upgradable',
        'cloud_service_type': 'cloudServiceType',
        'resource_type': 'resourceType',
        'resource_spec_code': 'resourceSpecCode',
        'specification': 'specification',
        'server_id': 'serverId',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, instancename=None, region=None, zone=None, arch=None, cpu_flavor=None, vpc_id=None, subnet_id=None, service_ip=None, security_group_ids=None, status=None, run_status=None, access_status=None, upgradable=None, cloud_service_type=None, resource_type=None, resource_spec_code=None, specification=None, server_id=None, create_time=None):
        """RenameInstanceResponse

        The model defined in huaweicloud sdk

        :param id: 独享引擎实例ID
        :type id: str
        :param instancename: 独享引擎实例名称
        :type instancename: str
        :param region: 独享引擎实例Region ID
        :type region: str
        :param zone: 可用区ID
        :type zone: str
        :param arch: CPU架构
        :type arch: str
        :param cpu_flavor: ECS规格
        :type cpu_flavor: str
        :param vpc_id: 独享引擎实例所在VPC ID
        :type vpc_id: str
        :param subnet_id: 独享引擎实例所在VPC的子网ID
        :type subnet_id: str
        :param service_ip: 独享引擎实例的业务面IP
        :type service_ip: str
        :param security_group_ids: 独享引擎绑定的安全组
        :type security_group_ids: list[str]
        :param status: 独享引擎计费状态   - 0：正常计费   - 1：冻结,资源和数据会保留，但租户无法再正常使用云服务   - 2：终止，资源和数据将清除
        :type status: int
        :param run_status: 独享引擎运行状态   - 0：创建中   - 1：运行中   - 2：删除中   - 3：已删除   - 4：创建失败   - 5：已冻结   - 6：异常   - 7：更新中   - 8：更新失败
        :type run_status: int
        :param access_status: 独享引擎接入状态（0：未接入，1：已接入）
        :type access_status: int
        :param upgradable: 独享引擎是否可升级（0：不可升级，1：可升级）
        :type upgradable: int
        :param cloud_service_type: 云服务代码。 仅作为标记，用户可忽略。
        :type cloud_service_type: str
        :param resource_type: 云服务资源类型，仅作为标记，用户可忽略。
        :type resource_type: str
        :param resource_spec_code: 云服务资源代码。仅作为标记，用户可忽略。
        :type resource_spec_code: str
        :param specification: 独享引擎ECS规格，如\&quot;8vCPUs | 16GB\&quot;
        :type specification: str
        :param server_id: 独享引擎ECS ID
        :type server_id: str
        :param create_time: 引擎实例创建时间
        :type create_time: int
        """
        
        super(RenameInstanceResponse, self).__init__()

        self._id = None
        self._instancename = None
        self._region = None
        self._zone = None
        self._arch = None
        self._cpu_flavor = None
        self._vpc_id = None
        self._subnet_id = None
        self._service_ip = None
        self._security_group_ids = None
        self._status = None
        self._run_status = None
        self._access_status = None
        self._upgradable = None
        self._cloud_service_type = None
        self._resource_type = None
        self._resource_spec_code = None
        self._specification = None
        self._server_id = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instancename is not None:
            self.instancename = instancename
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
        if server_id is not None:
            self.server_id = server_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        """Gets the id of this RenameInstanceResponse.

        独享引擎实例ID

        :return: The id of this RenameInstanceResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RenameInstanceResponse.

        独享引擎实例ID

        :param id: The id of this RenameInstanceResponse.
        :type id: str
        """
        self._id = id

    @property
    def instancename(self):
        """Gets the instancename of this RenameInstanceResponse.

        独享引擎实例名称

        :return: The instancename of this RenameInstanceResponse.
        :rtype: str
        """
        return self._instancename

    @instancename.setter
    def instancename(self, instancename):
        """Sets the instancename of this RenameInstanceResponse.

        独享引擎实例名称

        :param instancename: The instancename of this RenameInstanceResponse.
        :type instancename: str
        """
        self._instancename = instancename

    @property
    def region(self):
        """Gets the region of this RenameInstanceResponse.

        独享引擎实例Region ID

        :return: The region of this RenameInstanceResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this RenameInstanceResponse.

        独享引擎实例Region ID

        :param region: The region of this RenameInstanceResponse.
        :type region: str
        """
        self._region = region

    @property
    def zone(self):
        """Gets the zone of this RenameInstanceResponse.

        可用区ID

        :return: The zone of this RenameInstanceResponse.
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this RenameInstanceResponse.

        可用区ID

        :param zone: The zone of this RenameInstanceResponse.
        :type zone: str
        """
        self._zone = zone

    @property
    def arch(self):
        """Gets the arch of this RenameInstanceResponse.

        CPU架构

        :return: The arch of this RenameInstanceResponse.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this RenameInstanceResponse.

        CPU架构

        :param arch: The arch of this RenameInstanceResponse.
        :type arch: str
        """
        self._arch = arch

    @property
    def cpu_flavor(self):
        """Gets the cpu_flavor of this RenameInstanceResponse.

        ECS规格

        :return: The cpu_flavor of this RenameInstanceResponse.
        :rtype: str
        """
        return self._cpu_flavor

    @cpu_flavor.setter
    def cpu_flavor(self, cpu_flavor):
        """Sets the cpu_flavor of this RenameInstanceResponse.

        ECS规格

        :param cpu_flavor: The cpu_flavor of this RenameInstanceResponse.
        :type cpu_flavor: str
        """
        self._cpu_flavor = cpu_flavor

    @property
    def vpc_id(self):
        """Gets the vpc_id of this RenameInstanceResponse.

        独享引擎实例所在VPC ID

        :return: The vpc_id of this RenameInstanceResponse.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this RenameInstanceResponse.

        独享引擎实例所在VPC ID

        :param vpc_id: The vpc_id of this RenameInstanceResponse.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this RenameInstanceResponse.

        独享引擎实例所在VPC的子网ID

        :return: The subnet_id of this RenameInstanceResponse.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this RenameInstanceResponse.

        独享引擎实例所在VPC的子网ID

        :param subnet_id: The subnet_id of this RenameInstanceResponse.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def service_ip(self):
        """Gets the service_ip of this RenameInstanceResponse.

        独享引擎实例的业务面IP

        :return: The service_ip of this RenameInstanceResponse.
        :rtype: str
        """
        return self._service_ip

    @service_ip.setter
    def service_ip(self, service_ip):
        """Sets the service_ip of this RenameInstanceResponse.

        独享引擎实例的业务面IP

        :param service_ip: The service_ip of this RenameInstanceResponse.
        :type service_ip: str
        """
        self._service_ip = service_ip

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this RenameInstanceResponse.

        独享引擎绑定的安全组

        :return: The security_group_ids of this RenameInstanceResponse.
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this RenameInstanceResponse.

        独享引擎绑定的安全组

        :param security_group_ids: The security_group_ids of this RenameInstanceResponse.
        :type security_group_ids: list[str]
        """
        self._security_group_ids = security_group_ids

    @property
    def status(self):
        """Gets the status of this RenameInstanceResponse.

        独享引擎计费状态   - 0：正常计费   - 1：冻结,资源和数据会保留，但租户无法再正常使用云服务   - 2：终止，资源和数据将清除

        :return: The status of this RenameInstanceResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RenameInstanceResponse.

        独享引擎计费状态   - 0：正常计费   - 1：冻结,资源和数据会保留，但租户无法再正常使用云服务   - 2：终止，资源和数据将清除

        :param status: The status of this RenameInstanceResponse.
        :type status: int
        """
        self._status = status

    @property
    def run_status(self):
        """Gets the run_status of this RenameInstanceResponse.

        独享引擎运行状态   - 0：创建中   - 1：运行中   - 2：删除中   - 3：已删除   - 4：创建失败   - 5：已冻结   - 6：异常   - 7：更新中   - 8：更新失败

        :return: The run_status of this RenameInstanceResponse.
        :rtype: int
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this RenameInstanceResponse.

        独享引擎运行状态   - 0：创建中   - 1：运行中   - 2：删除中   - 3：已删除   - 4：创建失败   - 5：已冻结   - 6：异常   - 7：更新中   - 8：更新失败

        :param run_status: The run_status of this RenameInstanceResponse.
        :type run_status: int
        """
        self._run_status = run_status

    @property
    def access_status(self):
        """Gets the access_status of this RenameInstanceResponse.

        独享引擎接入状态（0：未接入，1：已接入）

        :return: The access_status of this RenameInstanceResponse.
        :rtype: int
        """
        return self._access_status

    @access_status.setter
    def access_status(self, access_status):
        """Sets the access_status of this RenameInstanceResponse.

        独享引擎接入状态（0：未接入，1：已接入）

        :param access_status: The access_status of this RenameInstanceResponse.
        :type access_status: int
        """
        self._access_status = access_status

    @property
    def upgradable(self):
        """Gets the upgradable of this RenameInstanceResponse.

        独享引擎是否可升级（0：不可升级，1：可升级）

        :return: The upgradable of this RenameInstanceResponse.
        :rtype: int
        """
        return self._upgradable

    @upgradable.setter
    def upgradable(self, upgradable):
        """Sets the upgradable of this RenameInstanceResponse.

        独享引擎是否可升级（0：不可升级，1：可升级）

        :param upgradable: The upgradable of this RenameInstanceResponse.
        :type upgradable: int
        """
        self._upgradable = upgradable

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this RenameInstanceResponse.

        云服务代码。 仅作为标记，用户可忽略。

        :return: The cloud_service_type of this RenameInstanceResponse.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this RenameInstanceResponse.

        云服务代码。 仅作为标记，用户可忽略。

        :param cloud_service_type: The cloud_service_type of this RenameInstanceResponse.
        :type cloud_service_type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def resource_type(self):
        """Gets the resource_type of this RenameInstanceResponse.

        云服务资源类型，仅作为标记，用户可忽略。

        :return: The resource_type of this RenameInstanceResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RenameInstanceResponse.

        云服务资源类型，仅作为标记，用户可忽略。

        :param resource_type: The resource_type of this RenameInstanceResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_spec_code(self):
        """Gets the resource_spec_code of this RenameInstanceResponse.

        云服务资源代码。仅作为标记，用户可忽略。

        :return: The resource_spec_code of this RenameInstanceResponse.
        :rtype: str
        """
        return self._resource_spec_code

    @resource_spec_code.setter
    def resource_spec_code(self, resource_spec_code):
        """Sets the resource_spec_code of this RenameInstanceResponse.

        云服务资源代码。仅作为标记，用户可忽略。

        :param resource_spec_code: The resource_spec_code of this RenameInstanceResponse.
        :type resource_spec_code: str
        """
        self._resource_spec_code = resource_spec_code

    @property
    def specification(self):
        """Gets the specification of this RenameInstanceResponse.

        独享引擎ECS规格，如\"8vCPUs | 16GB\"

        :return: The specification of this RenameInstanceResponse.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        """Sets the specification of this RenameInstanceResponse.

        独享引擎ECS规格，如\"8vCPUs | 16GB\"

        :param specification: The specification of this RenameInstanceResponse.
        :type specification: str
        """
        self._specification = specification

    @property
    def server_id(self):
        """Gets the server_id of this RenameInstanceResponse.

        独享引擎ECS ID

        :return: The server_id of this RenameInstanceResponse.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this RenameInstanceResponse.

        独享引擎ECS ID

        :param server_id: The server_id of this RenameInstanceResponse.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def create_time(self):
        """Gets the create_time of this RenameInstanceResponse.

        引擎实例创建时间

        :return: The create_time of this RenameInstanceResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RenameInstanceResponse.

        引擎实例创建时间

        :param create_time: The create_time of this RenameInstanceResponse.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, RenameInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
