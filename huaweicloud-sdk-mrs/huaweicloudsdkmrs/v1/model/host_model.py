# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostModel:

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
        'name': 'str',
        'ip': 'str',
        'availability_zone_id': 'str',
        'tags': 'list[TagPlain]',
        'status': 'str',
        'resource_id': 'str',
        'flavor': 'str',
        'type': 'str',
        'mem': 'str',
        'cpu': 'str',
        'root_volume_size': 'str',
        'data_volume_type': 'str',
        'data_volume_size': 'int',
        'data_volume_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'ip': 'ip',
        'availability_zone_id': 'availability_zone_id',
        'tags': 'tags',
        'status': 'status',
        'resource_id': 'resource_id',
        'flavor': 'flavor',
        'type': 'type',
        'mem': 'mem',
        'cpu': 'cpu',
        'root_volume_size': 'root_volume_size',
        'data_volume_type': 'data_volume_type',
        'data_volume_size': 'data_volume_size',
        'data_volume_count': 'data_volume_count'
    }

    def __init__(self, id=None, name=None, ip=None, availability_zone_id=None, tags=None, status=None, resource_id=None, flavor=None, type=None, mem=None, cpu=None, root_volume_size=None, data_volume_type=None, data_volume_size=None, data_volume_count=None):
        """HostModel

        The model defined in huaweicloud sdk

        :param id: 虚拟机ID
        :type id: str
        :param name: 虚拟机名称
        :type name: str
        :param ip: 虚拟机IP地址
        :type ip: str
        :param availability_zone_id: 可用区域
        :type availability_zone_id: str
        :param tags: 标签列表信息
        :type tags: list[:class:`huaweicloudsdkmrs.v1.TagPlain`]
        :param status: 虚拟机当前状态
        :type status: str
        :param resource_id: 节点资源ID
        :type resource_id: str
        :param flavor: 虚拟机规格ID
        :type flavor: str
        :param type: 虚拟机类型，当前支持MasterNode，CoreNode，TaskNode
        :type type: str
        :param mem: 内存
        :type mem: str
        :param cpu: CPU核数
        :type cpu: str
        :param root_volume_size: 操作系统盘容量
        :type root_volume_size: str
        :param data_volume_type: 数据盘类型
        :type data_volume_type: str
        :param data_volume_size: 数据盘容量
        :type data_volume_size: int
        :param data_volume_count: 数据盘个数
        :type data_volume_count: int
        """
        
        

        self._id = None
        self._name = None
        self._ip = None
        self._availability_zone_id = None
        self._tags = None
        self._status = None
        self._resource_id = None
        self._flavor = None
        self._type = None
        self._mem = None
        self._cpu = None
        self._root_volume_size = None
        self._data_volume_type = None
        self._data_volume_size = None
        self._data_volume_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if ip is not None:
            self.ip = ip
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if resource_id is not None:
            self.resource_id = resource_id
        if flavor is not None:
            self.flavor = flavor
        if type is not None:
            self.type = type
        if mem is not None:
            self.mem = mem
        if cpu is not None:
            self.cpu = cpu
        if root_volume_size is not None:
            self.root_volume_size = root_volume_size
        if data_volume_type is not None:
            self.data_volume_type = data_volume_type
        if data_volume_size is not None:
            self.data_volume_size = data_volume_size
        if data_volume_count is not None:
            self.data_volume_count = data_volume_count

    @property
    def id(self):
        """Gets the id of this HostModel.

        虚拟机ID

        :return: The id of this HostModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostModel.

        虚拟机ID

        :param id: The id of this HostModel.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this HostModel.

        虚拟机名称

        :return: The name of this HostModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HostModel.

        虚拟机名称

        :param name: The name of this HostModel.
        :type name: str
        """
        self._name = name

    @property
    def ip(self):
        """Gets the ip of this HostModel.

        虚拟机IP地址

        :return: The ip of this HostModel.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this HostModel.

        虚拟机IP地址

        :param ip: The ip of this HostModel.
        :type ip: str
        """
        self._ip = ip

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this HostModel.

        可用区域

        :return: The availability_zone_id of this HostModel.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this HostModel.

        可用区域

        :param availability_zone_id: The availability_zone_id of this HostModel.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def tags(self):
        """Gets the tags of this HostModel.

        标签列表信息

        :return: The tags of this HostModel.
        :rtype: list[:class:`huaweicloudsdkmrs.v1.TagPlain`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this HostModel.

        标签列表信息

        :param tags: The tags of this HostModel.
        :type tags: list[:class:`huaweicloudsdkmrs.v1.TagPlain`]
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this HostModel.

        虚拟机当前状态

        :return: The status of this HostModel.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this HostModel.

        虚拟机当前状态

        :param status: The status of this HostModel.
        :type status: str
        """
        self._status = status

    @property
    def resource_id(self):
        """Gets the resource_id of this HostModel.

        节点资源ID

        :return: The resource_id of this HostModel.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this HostModel.

        节点资源ID

        :param resource_id: The resource_id of this HostModel.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def flavor(self):
        """Gets the flavor of this HostModel.

        虚拟机规格ID

        :return: The flavor of this HostModel.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this HostModel.

        虚拟机规格ID

        :param flavor: The flavor of this HostModel.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def type(self):
        """Gets the type of this HostModel.

        虚拟机类型，当前支持MasterNode，CoreNode，TaskNode

        :return: The type of this HostModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HostModel.

        虚拟机类型，当前支持MasterNode，CoreNode，TaskNode

        :param type: The type of this HostModel.
        :type type: str
        """
        self._type = type

    @property
    def mem(self):
        """Gets the mem of this HostModel.

        内存

        :return: The mem of this HostModel.
        :rtype: str
        """
        return self._mem

    @mem.setter
    def mem(self, mem):
        """Sets the mem of this HostModel.

        内存

        :param mem: The mem of this HostModel.
        :type mem: str
        """
        self._mem = mem

    @property
    def cpu(self):
        """Gets the cpu of this HostModel.

        CPU核数

        :return: The cpu of this HostModel.
        :rtype: str
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this HostModel.

        CPU核数

        :param cpu: The cpu of this HostModel.
        :type cpu: str
        """
        self._cpu = cpu

    @property
    def root_volume_size(self):
        """Gets the root_volume_size of this HostModel.

        操作系统盘容量

        :return: The root_volume_size of this HostModel.
        :rtype: str
        """
        return self._root_volume_size

    @root_volume_size.setter
    def root_volume_size(self, root_volume_size):
        """Sets the root_volume_size of this HostModel.

        操作系统盘容量

        :param root_volume_size: The root_volume_size of this HostModel.
        :type root_volume_size: str
        """
        self._root_volume_size = root_volume_size

    @property
    def data_volume_type(self):
        """Gets the data_volume_type of this HostModel.

        数据盘类型

        :return: The data_volume_type of this HostModel.
        :rtype: str
        """
        return self._data_volume_type

    @data_volume_type.setter
    def data_volume_type(self, data_volume_type):
        """Sets the data_volume_type of this HostModel.

        数据盘类型

        :param data_volume_type: The data_volume_type of this HostModel.
        :type data_volume_type: str
        """
        self._data_volume_type = data_volume_type

    @property
    def data_volume_size(self):
        """Gets the data_volume_size of this HostModel.

        数据盘容量

        :return: The data_volume_size of this HostModel.
        :rtype: int
        """
        return self._data_volume_size

    @data_volume_size.setter
    def data_volume_size(self, data_volume_size):
        """Sets the data_volume_size of this HostModel.

        数据盘容量

        :param data_volume_size: The data_volume_size of this HostModel.
        :type data_volume_size: int
        """
        self._data_volume_size = data_volume_size

    @property
    def data_volume_count(self):
        """Gets the data_volume_count of this HostModel.

        数据盘个数

        :return: The data_volume_count of this HostModel.
        :rtype: int
        """
        return self._data_volume_count

    @data_volume_count.setter
    def data_volume_count(self, data_volume_count):
        """Sets the data_volume_count of this HostModel.

        数据盘个数

        :param data_volume_count: The data_volume_count of this HostModel.
        :type data_volume_count: int
        """
        self._data_volume_count = data_volume_count

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
        if not isinstance(other, HostModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
