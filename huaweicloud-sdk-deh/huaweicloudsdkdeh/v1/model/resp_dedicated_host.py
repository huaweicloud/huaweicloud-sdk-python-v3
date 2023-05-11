# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespDedicatedHost:

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
        'project_id': 'str',
        'host_properties': 'RespHostProperty',
        'state': 'str',
        'available_vcpus': 'int',
        'available_memory': 'int',
        'allocated_at': 'str',
        'released_at': 'str',
        'instance_total': 'int',
        'instance_uuids': 'list[str]',
        'tags': 'object',
        'sys_tags': 'object'
    }

    attribute_map = {
        'dedicated_host_id': 'dedicated_host_id',
        'name': 'name',
        'auto_placement': 'auto_placement',
        'availability_zone': 'availability_zone',
        'project_id': 'project_id',
        'host_properties': 'host_properties',
        'state': 'state',
        'available_vcpus': 'available_vcpus',
        'available_memory': 'available_memory',
        'allocated_at': 'allocated_at',
        'released_at': 'released_at',
        'instance_total': 'instance_total',
        'instance_uuids': 'instance_uuids',
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, dedicated_host_id=None, name=None, auto_placement=None, availability_zone=None, project_id=None, host_properties=None, state=None, available_vcpus=None, available_memory=None, allocated_at=None, released_at=None, instance_total=None, instance_uuids=None, tags=None, sys_tags=None):
        """RespDedicatedHost

        The model defined in huaweicloud sdk

        :param dedicated_host_id: 专属主机ID。
        :type dedicated_host_id: str
        :param name: 专属主机的名称。  长度限制在255个字符以内，并且不能以空格开头或结尾。
        :type name: str
        :param auto_placement: 在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。
        :type auto_placement: str
        :param availability_zone: 专属主机所属的可用区。
        :type availability_zone: str
        :param project_id: 专属主机所属的租户ID。
        :type project_id: str
        :param host_properties: 
        :type host_properties: :class:`huaweicloudsdkdeh.v1.RespHostProperty`
        :param state: 专属主机状态。
        :type state: str
        :param available_vcpus: 专属主机可用的vCPU核数。
        :type available_vcpus: int
        :param available_memory: 专属主机可用的内存大小。
        :type available_memory: int
        :param allocated_at: 专属主机的分配时间。
        :type allocated_at: str
        :param released_at: 专属主机的释放时间。
        :type released_at: str
        :param instance_total: 专属主机上的实例总数。
        :type instance_total: int
        :param instance_uuids: 专属主机上的实例UUID。  查询专属主机列表接口不显示此参数。
        :type instance_uuids: list[str]
        :param tags: 专属主机标签。
        :type tags: object
        :param sys_tags: 专属主机系统标签。
        :type sys_tags: object
        """
        
        

        self._dedicated_host_id = None
        self._name = None
        self._auto_placement = None
        self._availability_zone = None
        self._project_id = None
        self._host_properties = None
        self._state = None
        self._available_vcpus = None
        self._available_memory = None
        self._allocated_at = None
        self._released_at = None
        self._instance_total = None
        self._instance_uuids = None
        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        self.dedicated_host_id = dedicated_host_id
        self.name = name
        self.auto_placement = auto_placement
        self.availability_zone = availability_zone
        self.project_id = project_id
        self.host_properties = host_properties
        self.state = state
        self.available_vcpus = available_vcpus
        self.available_memory = available_memory
        self.allocated_at = allocated_at
        self.released_at = released_at
        self.instance_total = instance_total
        self.instance_uuids = instance_uuids
        self.tags = tags
        self.sys_tags = sys_tags

    @property
    def dedicated_host_id(self):
        """Gets the dedicated_host_id of this RespDedicatedHost.

        专属主机ID。

        :return: The dedicated_host_id of this RespDedicatedHost.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        """Sets the dedicated_host_id of this RespDedicatedHost.

        专属主机ID。

        :param dedicated_host_id: The dedicated_host_id of this RespDedicatedHost.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def name(self):
        """Gets the name of this RespDedicatedHost.

        专属主机的名称。  长度限制在255个字符以内，并且不能以空格开头或结尾。

        :return: The name of this RespDedicatedHost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RespDedicatedHost.

        专属主机的名称。  长度限制在255个字符以内，并且不能以空格开头或结尾。

        :param name: The name of this RespDedicatedHost.
        :type name: str
        """
        self._name = name

    @property
    def auto_placement(self):
        """Gets the auto_placement of this RespDedicatedHost.

        在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。

        :return: The auto_placement of this RespDedicatedHost.
        :rtype: str
        """
        return self._auto_placement

    @auto_placement.setter
    def auto_placement(self, auto_placement):
        """Sets the auto_placement of this RespDedicatedHost.

        在创建云服务器时（未指定专属主机ID），是否允许云服务器自动分配在一台可用的专属主机上。

        :param auto_placement: The auto_placement of this RespDedicatedHost.
        :type auto_placement: str
        """
        self._auto_placement = auto_placement

    @property
    def availability_zone(self):
        """Gets the availability_zone of this RespDedicatedHost.

        专属主机所属的可用区。

        :return: The availability_zone of this RespDedicatedHost.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this RespDedicatedHost.

        专属主机所属的可用区。

        :param availability_zone: The availability_zone of this RespDedicatedHost.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def project_id(self):
        """Gets the project_id of this RespDedicatedHost.

        专属主机所属的租户ID。

        :return: The project_id of this RespDedicatedHost.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RespDedicatedHost.

        专属主机所属的租户ID。

        :param project_id: The project_id of this RespDedicatedHost.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def host_properties(self):
        """Gets the host_properties of this RespDedicatedHost.

        :return: The host_properties of this RespDedicatedHost.
        :rtype: :class:`huaweicloudsdkdeh.v1.RespHostProperty`
        """
        return self._host_properties

    @host_properties.setter
    def host_properties(self, host_properties):
        """Sets the host_properties of this RespDedicatedHost.

        :param host_properties: The host_properties of this RespDedicatedHost.
        :type host_properties: :class:`huaweicloudsdkdeh.v1.RespHostProperty`
        """
        self._host_properties = host_properties

    @property
    def state(self):
        """Gets the state of this RespDedicatedHost.

        专属主机状态。

        :return: The state of this RespDedicatedHost.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this RespDedicatedHost.

        专属主机状态。

        :param state: The state of this RespDedicatedHost.
        :type state: str
        """
        self._state = state

    @property
    def available_vcpus(self):
        """Gets the available_vcpus of this RespDedicatedHost.

        专属主机可用的vCPU核数。

        :return: The available_vcpus of this RespDedicatedHost.
        :rtype: int
        """
        return self._available_vcpus

    @available_vcpus.setter
    def available_vcpus(self, available_vcpus):
        """Sets the available_vcpus of this RespDedicatedHost.

        专属主机可用的vCPU核数。

        :param available_vcpus: The available_vcpus of this RespDedicatedHost.
        :type available_vcpus: int
        """
        self._available_vcpus = available_vcpus

    @property
    def available_memory(self):
        """Gets the available_memory of this RespDedicatedHost.

        专属主机可用的内存大小。

        :return: The available_memory of this RespDedicatedHost.
        :rtype: int
        """
        return self._available_memory

    @available_memory.setter
    def available_memory(self, available_memory):
        """Sets the available_memory of this RespDedicatedHost.

        专属主机可用的内存大小。

        :param available_memory: The available_memory of this RespDedicatedHost.
        :type available_memory: int
        """
        self._available_memory = available_memory

    @property
    def allocated_at(self):
        """Gets the allocated_at of this RespDedicatedHost.

        专属主机的分配时间。

        :return: The allocated_at of this RespDedicatedHost.
        :rtype: str
        """
        return self._allocated_at

    @allocated_at.setter
    def allocated_at(self, allocated_at):
        """Sets the allocated_at of this RespDedicatedHost.

        专属主机的分配时间。

        :param allocated_at: The allocated_at of this RespDedicatedHost.
        :type allocated_at: str
        """
        self._allocated_at = allocated_at

    @property
    def released_at(self):
        """Gets the released_at of this RespDedicatedHost.

        专属主机的释放时间。

        :return: The released_at of this RespDedicatedHost.
        :rtype: str
        """
        return self._released_at

    @released_at.setter
    def released_at(self, released_at):
        """Sets the released_at of this RespDedicatedHost.

        专属主机的释放时间。

        :param released_at: The released_at of this RespDedicatedHost.
        :type released_at: str
        """
        self._released_at = released_at

    @property
    def instance_total(self):
        """Gets the instance_total of this RespDedicatedHost.

        专属主机上的实例总数。

        :return: The instance_total of this RespDedicatedHost.
        :rtype: int
        """
        return self._instance_total

    @instance_total.setter
    def instance_total(self, instance_total):
        """Sets the instance_total of this RespDedicatedHost.

        专属主机上的实例总数。

        :param instance_total: The instance_total of this RespDedicatedHost.
        :type instance_total: int
        """
        self._instance_total = instance_total

    @property
    def instance_uuids(self):
        """Gets the instance_uuids of this RespDedicatedHost.

        专属主机上的实例UUID。  查询专属主机列表接口不显示此参数。

        :return: The instance_uuids of this RespDedicatedHost.
        :rtype: list[str]
        """
        return self._instance_uuids

    @instance_uuids.setter
    def instance_uuids(self, instance_uuids):
        """Sets the instance_uuids of this RespDedicatedHost.

        专属主机上的实例UUID。  查询专属主机列表接口不显示此参数。

        :param instance_uuids: The instance_uuids of this RespDedicatedHost.
        :type instance_uuids: list[str]
        """
        self._instance_uuids = instance_uuids

    @property
    def tags(self):
        """Gets the tags of this RespDedicatedHost.

        专属主机标签。

        :return: The tags of this RespDedicatedHost.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this RespDedicatedHost.

        专属主机标签。

        :param tags: The tags of this RespDedicatedHost.
        :type tags: object
        """
        self._tags = tags

    @property
    def sys_tags(self):
        """Gets the sys_tags of this RespDedicatedHost.

        专属主机系统标签。

        :return: The sys_tags of this RespDedicatedHost.
        :rtype: object
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        """Sets the sys_tags of this RespDedicatedHost.

        专属主机系统标签。

        :param sys_tags: The sys_tags of this RespDedicatedHost.
        :type sys_tags: object
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, RespDedicatedHost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
