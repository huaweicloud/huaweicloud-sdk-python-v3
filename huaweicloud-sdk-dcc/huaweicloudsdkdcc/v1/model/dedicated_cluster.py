# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DedicatedCluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'availability_zone': 'str',
        'host_total': 'int',
        'host_type': 'str',
        'service_type': 'str',
        'host_properties': 'HostProperties',
        'vcpus_used': 'int',
        'vcpus_total': 'int',
        'memory_mb_used': 'int',
        'memory_mb_total': 'int',
        'flavors': 'list[str]',
        'instance_total': 'int'
    }

    attribute_map = {
        'project_id': 'project_id',
        'availability_zone': 'availability_zone',
        'host_total': 'host_total',
        'host_type': 'host_type',
        'service_type': 'service_type',
        'host_properties': 'host_properties',
        'vcpus_used': 'vcpus_used',
        'vcpus_total': 'vcpus_total',
        'memory_mb_used': 'memory_mb_used',
        'memory_mb_total': 'memory_mb_total',
        'flavors': 'flavors',
        'instance_total': 'instance_total'
    }

    def __init__(self, project_id=None, availability_zone=None, host_total=None, host_type=None, service_type=None, host_properties=None, vcpus_used=None, vcpus_total=None, memory_mb_used=None, memory_mb_total=None, flavors=None, instance_total=None):
        r"""DedicatedCluster

        The model defined in huaweicloud sdk

        :param project_id: 项目id
        :type project_id: str
        :param availability_zone: 可用区
        :type availability_zone: str
        :param host_total: 主机数量
        :type host_total: int
        :param host_type: 主机规格编码。
        :type host_type: str
        :param service_type: 集群服务类型。
        :type service_type: str
        :param host_properties: 
        :type host_properties: :class:`huaweicloudsdkdcc.v1.HostProperties`
        :param vcpus_used: 已用vcpu个数。
        :type vcpus_used: int
        :param vcpus_total: 总的vcpu个数。。
        :type vcpus_total: int
        :param memory_mb_used: 已用内存。
        :type memory_mb_used: int
        :param memory_mb_total: 总内存。
        :type memory_mb_total: int
        :param flavors: 支持flavor列表
        :type flavors: list[str]
        :param instance_total: 运行的计算实例总数。
        :type instance_total: int
        """
        
        

        self._project_id = None
        self._availability_zone = None
        self._host_total = None
        self._host_type = None
        self._service_type = None
        self._host_properties = None
        self._vcpus_used = None
        self._vcpus_total = None
        self._memory_mb_used = None
        self._memory_mb_total = None
        self._flavors = None
        self._instance_total = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if host_total is not None:
            self.host_total = host_total
        if host_type is not None:
            self.host_type = host_type
        if service_type is not None:
            self.service_type = service_type
        if host_properties is not None:
            self.host_properties = host_properties
        if vcpus_used is not None:
            self.vcpus_used = vcpus_used
        if vcpus_total is not None:
            self.vcpus_total = vcpus_total
        if memory_mb_used is not None:
            self.memory_mb_used = memory_mb_used
        if memory_mb_total is not None:
            self.memory_mb_total = memory_mb_total
        if flavors is not None:
            self.flavors = flavors
        if instance_total is not None:
            self.instance_total = instance_total

    @property
    def project_id(self):
        r"""Gets the project_id of this DedicatedCluster.

        项目id

        :return: The project_id of this DedicatedCluster.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DedicatedCluster.

        项目id

        :param project_id: The project_id of this DedicatedCluster.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this DedicatedCluster.

        可用区

        :return: The availability_zone of this DedicatedCluster.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this DedicatedCluster.

        可用区

        :param availability_zone: The availability_zone of this DedicatedCluster.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def host_total(self):
        r"""Gets the host_total of this DedicatedCluster.

        主机数量

        :return: The host_total of this DedicatedCluster.
        :rtype: int
        """
        return self._host_total

    @host_total.setter
    def host_total(self, host_total):
        r"""Sets the host_total of this DedicatedCluster.

        主机数量

        :param host_total: The host_total of this DedicatedCluster.
        :type host_total: int
        """
        self._host_total = host_total

    @property
    def host_type(self):
        r"""Gets the host_type of this DedicatedCluster.

        主机规格编码。

        :return: The host_type of this DedicatedCluster.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this DedicatedCluster.

        主机规格编码。

        :param host_type: The host_type of this DedicatedCluster.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def service_type(self):
        r"""Gets the service_type of this DedicatedCluster.

        集群服务类型。

        :return: The service_type of this DedicatedCluster.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        r"""Sets the service_type of this DedicatedCluster.

        集群服务类型。

        :param service_type: The service_type of this DedicatedCluster.
        :type service_type: str
        """
        self._service_type = service_type

    @property
    def host_properties(self):
        r"""Gets the host_properties of this DedicatedCluster.

        :return: The host_properties of this DedicatedCluster.
        :rtype: :class:`huaweicloudsdkdcc.v1.HostProperties`
        """
        return self._host_properties

    @host_properties.setter
    def host_properties(self, host_properties):
        r"""Sets the host_properties of this DedicatedCluster.

        :param host_properties: The host_properties of this DedicatedCluster.
        :type host_properties: :class:`huaweicloudsdkdcc.v1.HostProperties`
        """
        self._host_properties = host_properties

    @property
    def vcpus_used(self):
        r"""Gets the vcpus_used of this DedicatedCluster.

        已用vcpu个数。

        :return: The vcpus_used of this DedicatedCluster.
        :rtype: int
        """
        return self._vcpus_used

    @vcpus_used.setter
    def vcpus_used(self, vcpus_used):
        r"""Sets the vcpus_used of this DedicatedCluster.

        已用vcpu个数。

        :param vcpus_used: The vcpus_used of this DedicatedCluster.
        :type vcpus_used: int
        """
        self._vcpus_used = vcpus_used

    @property
    def vcpus_total(self):
        r"""Gets the vcpus_total of this DedicatedCluster.

        总的vcpu个数。。

        :return: The vcpus_total of this DedicatedCluster.
        :rtype: int
        """
        return self._vcpus_total

    @vcpus_total.setter
    def vcpus_total(self, vcpus_total):
        r"""Sets the vcpus_total of this DedicatedCluster.

        总的vcpu个数。。

        :param vcpus_total: The vcpus_total of this DedicatedCluster.
        :type vcpus_total: int
        """
        self._vcpus_total = vcpus_total

    @property
    def memory_mb_used(self):
        r"""Gets the memory_mb_used of this DedicatedCluster.

        已用内存。

        :return: The memory_mb_used of this DedicatedCluster.
        :rtype: int
        """
        return self._memory_mb_used

    @memory_mb_used.setter
    def memory_mb_used(self, memory_mb_used):
        r"""Sets the memory_mb_used of this DedicatedCluster.

        已用内存。

        :param memory_mb_used: The memory_mb_used of this DedicatedCluster.
        :type memory_mb_used: int
        """
        self._memory_mb_used = memory_mb_used

    @property
    def memory_mb_total(self):
        r"""Gets the memory_mb_total of this DedicatedCluster.

        总内存。

        :return: The memory_mb_total of this DedicatedCluster.
        :rtype: int
        """
        return self._memory_mb_total

    @memory_mb_total.setter
    def memory_mb_total(self, memory_mb_total):
        r"""Sets the memory_mb_total of this DedicatedCluster.

        总内存。

        :param memory_mb_total: The memory_mb_total of this DedicatedCluster.
        :type memory_mb_total: int
        """
        self._memory_mb_total = memory_mb_total

    @property
    def flavors(self):
        r"""Gets the flavors of this DedicatedCluster.

        支持flavor列表

        :return: The flavors of this DedicatedCluster.
        :rtype: list[str]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this DedicatedCluster.

        支持flavor列表

        :param flavors: The flavors of this DedicatedCluster.
        :type flavors: list[str]
        """
        self._flavors = flavors

    @property
    def instance_total(self):
        r"""Gets the instance_total of this DedicatedCluster.

        运行的计算实例总数。

        :return: The instance_total of this DedicatedCluster.
        :rtype: int
        """
        return self._instance_total

    @instance_total.setter
    def instance_total(self, instance_total):
        r"""Sets the instance_total of this DedicatedCluster.

        运行的计算实例总数。

        :param instance_total: The instance_total of this DedicatedCluster.
        :type instance_total: int
        """
        self._instance_total = instance_total

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DedicatedCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
