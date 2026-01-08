# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHostsRspDedicatedHosts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dedicated_host_id': 'str',
        'name': 'str',
        'auto_placement': 'str',
        'availability_zone': 'str',
        'host_properties': 'ListHostsRspHostProperties',
        'product_id': 'str',
        'order_id': 'str',
        'resource_type': 'str',
        'state': 'str',
        'available_vcpus': 'int',
        'available_memory': 'int',
        'instance_total': 'int',
        'allocated_at': 'str',
        'released_at': 'str',
        'instance_uuids': 'list[str]',
        'enterprise_project_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'dedicated_host_id': 'dedicated_host_id',
        'name': 'name',
        'auto_placement': 'auto_placement',
        'availability_zone': 'availability_zone',
        'host_properties': 'host_properties',
        'product_id': 'product_id',
        'order_id': 'order_id',
        'resource_type': 'resource_type',
        'state': 'state',
        'available_vcpus': 'available_vcpus',
        'available_memory': 'available_memory',
        'instance_total': 'instance_total',
        'allocated_at': 'allocated_at',
        'released_at': 'released_at',
        'instance_uuids': 'instance_uuids',
        'enterprise_project_id': 'enterprise_project_id',
        'project_id': 'project_id'
    }

    def __init__(self, dedicated_host_id=None, name=None, auto_placement=None, availability_zone=None, host_properties=None, product_id=None, order_id=None, resource_type=None, state=None, available_vcpus=None, available_memory=None, instance_total=None, allocated_at=None, released_at=None, instance_uuids=None, enterprise_project_id=None, project_id=None):
        r"""ListHostsRspDedicatedHosts

        The model defined in huaweicloud sdk

        :param dedicated_host_id: 云办公主机ID。
        :type dedicated_host_id: str
        :param name: 云办公主机的名称。
        :type name: str
        :param auto_placement: 在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的云办公主机上。取值范围：“on”或“off”。
        :type auto_placement: str
        :param availability_zone: 云办公主机的区域。
        :type availability_zone: str
        :param host_properties: 
        :type host_properties: :class:`huaweicloudsdkworkspace.v2.ListHostsRspHostProperties`
        :param product_id: 云办公主机的产品id。
        :type product_id: str
        :param order_id: 云办公主机的订单id。
        :type order_id: str
        :param resource_type: 云服务资源类型。
        :type resource_type: str
        :param state: 云办公主机状态，该参数取值可以为：“available”、“fault”或“released”。
        :type state: str
        :param available_vcpus: 云办公主机可用的vCPU核数。
        :type available_vcpus: int
        :param available_memory: 云办公主机可用的内存大小。
        :type available_memory: int
        :param instance_total: 云办公主机上的实例总数。
        :type instance_total: int
        :param allocated_at: 云办公主机的分配时间。
        :type allocated_at: str
        :param released_at: 云办公主机的释放时间。
        :type released_at: str
        :param instance_uuids: 专属主机上的实例UUID。
        :type instance_uuids: list[str]
        :param enterprise_project_id: 企业项目ID。
        :type enterprise_project_id: str
        :param project_id: 项目ID。
        :type project_id: str
        """
        
        

        self._dedicated_host_id = None
        self._name = None
        self._auto_placement = None
        self._availability_zone = None
        self._host_properties = None
        self._product_id = None
        self._order_id = None
        self._resource_type = None
        self._state = None
        self._available_vcpus = None
        self._available_memory = None
        self._instance_total = None
        self._allocated_at = None
        self._released_at = None
        self._instance_uuids = None
        self._enterprise_project_id = None
        self._project_id = None
        self.discriminator = None

        if dedicated_host_id is not None:
            self.dedicated_host_id = dedicated_host_id
        if name is not None:
            self.name = name
        if auto_placement is not None:
            self.auto_placement = auto_placement
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if host_properties is not None:
            self.host_properties = host_properties
        if product_id is not None:
            self.product_id = product_id
        if order_id is not None:
            self.order_id = order_id
        if resource_type is not None:
            self.resource_type = resource_type
        if state is not None:
            self.state = state
        if available_vcpus is not None:
            self.available_vcpus = available_vcpus
        if available_memory is not None:
            self.available_memory = available_memory
        if instance_total is not None:
            self.instance_total = instance_total
        if allocated_at is not None:
            self.allocated_at = allocated_at
        if released_at is not None:
            self.released_at = released_at
        if instance_uuids is not None:
            self.instance_uuids = instance_uuids
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if project_id is not None:
            self.project_id = project_id

    @property
    def dedicated_host_id(self):
        r"""Gets the dedicated_host_id of this ListHostsRspDedicatedHosts.

        云办公主机ID。

        :return: The dedicated_host_id of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        r"""Sets the dedicated_host_id of this ListHostsRspDedicatedHosts.

        云办公主机ID。

        :param dedicated_host_id: The dedicated_host_id of this ListHostsRspDedicatedHosts.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def name(self):
        r"""Gets the name of this ListHostsRspDedicatedHosts.

        云办公主机的名称。

        :return: The name of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListHostsRspDedicatedHosts.

        云办公主机的名称。

        :param name: The name of this ListHostsRspDedicatedHosts.
        :type name: str
        """
        self._name = name

    @property
    def auto_placement(self):
        r"""Gets the auto_placement of this ListHostsRspDedicatedHosts.

        在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的云办公主机上。取值范围：“on”或“off”。

        :return: The auto_placement of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        r"""Sets the auto_placement of this ListHostsRspDedicatedHosts.

        在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的云办公主机上。取值范围：“on”或“off”。

        :param auto_placement: The auto_placement of this ListHostsRspDedicatedHosts.
        :type auto_placement: str
        """
        self._auto_placement = auto_placement

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ListHostsRspDedicatedHosts.

        云办公主机的区域。

        :return: The availability_zone of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ListHostsRspDedicatedHosts.

        云办公主机的区域。

        :param availability_zone: The availability_zone of this ListHostsRspDedicatedHosts.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def host_properties(self):
        r"""Gets the host_properties of this ListHostsRspDedicatedHosts.

        :return: The host_properties of this ListHostsRspDedicatedHosts.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ListHostsRspHostProperties`
        """
        return self._host_properties

    @host_properties.setter
    def host_properties(self, host_properties):
        r"""Sets the host_properties of this ListHostsRspDedicatedHosts.

        :param host_properties: The host_properties of this ListHostsRspDedicatedHosts.
        :type host_properties: :class:`huaweicloudsdkworkspace.v2.ListHostsRspHostProperties`
        """
        self._host_properties = host_properties

    @property
    def product_id(self):
        r"""Gets the product_id of this ListHostsRspDedicatedHosts.

        云办公主机的产品id。

        :return: The product_id of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        r"""Sets the product_id of this ListHostsRspDedicatedHosts.

        云办公主机的产品id。

        :param product_id: The product_id of this ListHostsRspDedicatedHosts.
        :type product_id: str
        """
        self._product_id = product_id

    @property
    def order_id(self):
        r"""Gets the order_id of this ListHostsRspDedicatedHosts.

        云办公主机的订单id。

        :return: The order_id of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this ListHostsRspDedicatedHosts.

        云办公主机的订单id。

        :param order_id: The order_id of this ListHostsRspDedicatedHosts.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListHostsRspDedicatedHosts.

        云服务资源类型。

        :return: The resource_type of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListHostsRspDedicatedHosts.

        云服务资源类型。

        :param resource_type: The resource_type of this ListHostsRspDedicatedHosts.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def state(self):
        r"""Gets the state of this ListHostsRspDedicatedHosts.

        云办公主机状态，该参数取值可以为：“available”、“fault”或“released”。

        :return: The state of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this ListHostsRspDedicatedHosts.

        云办公主机状态，该参数取值可以为：“available”、“fault”或“released”。

        :param state: The state of this ListHostsRspDedicatedHosts.
        :type state: str
        """
        self._state = state

    @property
    def available_vcpus(self):
        r"""Gets the available_vcpus of this ListHostsRspDedicatedHosts.

        云办公主机可用的vCPU核数。

        :return: The available_vcpus of this ListHostsRspDedicatedHosts.
        :rtype: int
        """
        return self._available_vcpus

    @available_vcpus.setter
    def available_vcpus(self, available_vcpus):
        r"""Sets the available_vcpus of this ListHostsRspDedicatedHosts.

        云办公主机可用的vCPU核数。

        :param available_vcpus: The available_vcpus of this ListHostsRspDedicatedHosts.
        :type available_vcpus: int
        """
        self._available_vcpus = available_vcpus

    @property
    def available_memory(self):
        r"""Gets the available_memory of this ListHostsRspDedicatedHosts.

        云办公主机可用的内存大小。

        :return: The available_memory of this ListHostsRspDedicatedHosts.
        :rtype: int
        """
        return self._available_memory

    @available_memory.setter
    def available_memory(self, available_memory):
        r"""Sets the available_memory of this ListHostsRspDedicatedHosts.

        云办公主机可用的内存大小。

        :param available_memory: The available_memory of this ListHostsRspDedicatedHosts.
        :type available_memory: int
        """
        self._available_memory = available_memory

    @property
    def instance_total(self):
        r"""Gets the instance_total of this ListHostsRspDedicatedHosts.

        云办公主机上的实例总数。

        :return: The instance_total of this ListHostsRspDedicatedHosts.
        :rtype: int
        """
        return self._instance_total

    @instance_total.setter
    def instance_total(self, instance_total):
        r"""Sets the instance_total of this ListHostsRspDedicatedHosts.

        云办公主机上的实例总数。

        :param instance_total: The instance_total of this ListHostsRspDedicatedHosts.
        :type instance_total: int
        """
        self._instance_total = instance_total

    @property
    def allocated_at(self):
        r"""Gets the allocated_at of this ListHostsRspDedicatedHosts.

        云办公主机的分配时间。

        :return: The allocated_at of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._allocated_at

    @allocated_at.setter
    def allocated_at(self, allocated_at):
        r"""Sets the allocated_at of this ListHostsRspDedicatedHosts.

        云办公主机的分配时间。

        :param allocated_at: The allocated_at of this ListHostsRspDedicatedHosts.
        :type allocated_at: str
        """
        self._allocated_at = allocated_at

    @property
    def released_at(self):
        r"""Gets the released_at of this ListHostsRspDedicatedHosts.

        云办公主机的释放时间。

        :return: The released_at of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._released_at

    @released_at.setter
    def released_at(self, released_at):
        r"""Sets the released_at of this ListHostsRspDedicatedHosts.

        云办公主机的释放时间。

        :param released_at: The released_at of this ListHostsRspDedicatedHosts.
        :type released_at: str
        """
        self._released_at = released_at

    @property
    def instance_uuids(self):
        r"""Gets the instance_uuids of this ListHostsRspDedicatedHosts.

        专属主机上的实例UUID。

        :return: The instance_uuids of this ListHostsRspDedicatedHosts.
        :rtype: list[str]
        """
        return self._instance_uuids

    @instance_uuids.setter
    def instance_uuids(self, instance_uuids):
        r"""Sets the instance_uuids of this ListHostsRspDedicatedHosts.

        专属主机上的实例UUID。

        :param instance_uuids: The instance_uuids of this ListHostsRspDedicatedHosts.
        :type instance_uuids: list[str]
        """
        self._instance_uuids = instance_uuids

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListHostsRspDedicatedHosts.

        企业项目ID。

        :return: The enterprise_project_id of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListHostsRspDedicatedHosts.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListHostsRspDedicatedHosts.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ListHostsRspDedicatedHosts.

        项目ID。

        :return: The project_id of this ListHostsRspDedicatedHosts.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListHostsRspDedicatedHosts.

        项目ID。

        :param project_id: The project_id of this ListHostsRspDedicatedHosts.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ListHostsRspDedicatedHosts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
