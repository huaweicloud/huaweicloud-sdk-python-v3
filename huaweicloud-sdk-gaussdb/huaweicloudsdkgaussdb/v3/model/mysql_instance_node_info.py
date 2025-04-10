# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlInstanceNodeInfo:

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
        'type': 'str',
        'status': 'str',
        'port': 'int',
        'private_read_ips': 'list[str]',
        'volume': 'MysqlInstanceNodeVolumeInfo',
        'az_code': 'str',
        'region_code': 'str',
        'created': 'str',
        'updated': 'str',
        'flavor_id': 'str',
        'flavor_ref': 'str',
        'max_connections': 'str',
        'vcpus': 'str',
        'ram': 'str',
        'need_restart': 'bool',
        'priority': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'port': 'port',
        'private_read_ips': 'private_read_ips',
        'volume': 'volume',
        'az_code': 'az_code',
        'region_code': 'region_code',
        'created': 'created',
        'updated': 'updated',
        'flavor_id': 'flavor_id',
        'flavor_ref': 'flavor_ref',
        'max_connections': 'max_connections',
        'vcpus': 'vcpus',
        'ram': 'ram',
        'need_restart': 'need_restart',
        'priority': 'priority'
    }

    def __init__(self, id=None, name=None, type=None, status=None, port=None, private_read_ips=None, volume=None, az_code=None, region_code=None, created=None, updated=None, flavor_id=None, flavor_ref=None, max_connections=None, vcpus=None, ram=None, need_restart=None, priority=None):
        r"""MysqlInstanceNodeInfo

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 节点名称。
        :type name: str
        :param type: 节点类型，master或slave。
        :type type: str
        :param status: 节点状态。
        :type status: str
        :param port: 数据库端口号。
        :type port: int
        :param private_read_ips: 节点的读内网地址。
        :type private_read_ips: list[str]
        :param volume: 
        :type volume: :class:`huaweicloudsdkgaussdb.v3.MysqlInstanceNodeVolumeInfo`
        :param az_code: 可用区。
        :type az_code: str
        :param region_code: 实例所在的区域。
        :type region_code: str
        :param created: 创建时间，格式为\&quot;yyyy-mm-ddThh:mm:ssZ\&quot;。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。说明：创建时返回值为空，数据库实例创建成功后该值不为空。
        :type created: str
        :param updated: 更新时间，格式与\&quot;created\&quot;字段对应格式完全相同。说明：创建时返回值为空，数据库实例创建成功后该值不为空。
        :type updated: str
        :param flavor_id: 规格ID。
        :type flavor_id: str
        :param flavor_ref: 规格码。
        :type flavor_ref: str
        :param max_connections: 允许的最大连接数。
        :type max_connections: str
        :param vcpus: CPU核数。
        :type vcpus: str
        :param ram: 内存大小，单位为GB。
        :type ram: str
        :param need_restart: 是否需要重启使修改的参数生效。
        :type need_restart: bool
        :param priority: 主备倒换优先级。
        :type priority: int
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._port = None
        self._private_read_ips = None
        self._volume = None
        self._az_code = None
        self._region_code = None
        self._created = None
        self._updated = None
        self._flavor_id = None
        self._flavor_ref = None
        self._max_connections = None
        self._vcpus = None
        self._ram = None
        self._need_restart = None
        self._priority = None
        self.discriminator = None

        self.id = id
        self.name = name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if port is not None:
            self.port = port
        if private_read_ips is not None:
            self.private_read_ips = private_read_ips
        if volume is not None:
            self.volume = volume
        if az_code is not None:
            self.az_code = az_code
        if region_code is not None:
            self.region_code = region_code
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if flavor_id is not None:
            self.flavor_id = flavor_id
        if flavor_ref is not None:
            self.flavor_ref = flavor_ref
        if max_connections is not None:
            self.max_connections = max_connections
        if vcpus is not None:
            self.vcpus = vcpus
        if ram is not None:
            self.ram = ram
        if need_restart is not None:
            self.need_restart = need_restart
        if priority is not None:
            self.priority = priority

    @property
    def id(self):
        r"""Gets the id of this MysqlInstanceNodeInfo.

        实例ID。

        :return: The id of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MysqlInstanceNodeInfo.

        实例ID。

        :param id: The id of this MysqlInstanceNodeInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this MysqlInstanceNodeInfo.

        节点名称。

        :return: The name of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MysqlInstanceNodeInfo.

        节点名称。

        :param name: The name of this MysqlInstanceNodeInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this MysqlInstanceNodeInfo.

        节点类型，master或slave。

        :return: The type of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this MysqlInstanceNodeInfo.

        节点类型，master或slave。

        :param type: The type of this MysqlInstanceNodeInfo.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this MysqlInstanceNodeInfo.

        节点状态。

        :return: The status of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this MysqlInstanceNodeInfo.

        节点状态。

        :param status: The status of this MysqlInstanceNodeInfo.
        :type status: str
        """
        self._status = status

    @property
    def port(self):
        r"""Gets the port of this MysqlInstanceNodeInfo.

        数据库端口号。

        :return: The port of this MysqlInstanceNodeInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this MysqlInstanceNodeInfo.

        数据库端口号。

        :param port: The port of this MysqlInstanceNodeInfo.
        :type port: int
        """
        self._port = port

    @property
    def private_read_ips(self):
        r"""Gets the private_read_ips of this MysqlInstanceNodeInfo.

        节点的读内网地址。

        :return: The private_read_ips of this MysqlInstanceNodeInfo.
        :rtype: list[str]
        """
        return self._private_read_ips

    @private_read_ips.setter
    def private_read_ips(self, private_read_ips):
        r"""Sets the private_read_ips of this MysqlInstanceNodeInfo.

        节点的读内网地址。

        :param private_read_ips: The private_read_ips of this MysqlInstanceNodeInfo.
        :type private_read_ips: list[str]
        """
        self._private_read_ips = private_read_ips

    @property
    def volume(self):
        r"""Gets the volume of this MysqlInstanceNodeInfo.

        :return: The volume of this MysqlInstanceNodeInfo.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.MysqlInstanceNodeVolumeInfo`
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        r"""Sets the volume of this MysqlInstanceNodeInfo.

        :param volume: The volume of this MysqlInstanceNodeInfo.
        :type volume: :class:`huaweicloudsdkgaussdb.v3.MysqlInstanceNodeVolumeInfo`
        """
        self._volume = volume

    @property
    def az_code(self):
        r"""Gets the az_code of this MysqlInstanceNodeInfo.

        可用区。

        :return: The az_code of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        r"""Sets the az_code of this MysqlInstanceNodeInfo.

        可用区。

        :param az_code: The az_code of this MysqlInstanceNodeInfo.
        :type az_code: str
        """
        self._az_code = az_code

    @property
    def region_code(self):
        r"""Gets the region_code of this MysqlInstanceNodeInfo.

        实例所在的区域。

        :return: The region_code of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        r"""Sets the region_code of this MysqlInstanceNodeInfo.

        实例所在的区域。

        :param region_code: The region_code of this MysqlInstanceNodeInfo.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def created(self):
        r"""Gets the created of this MysqlInstanceNodeInfo.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The created of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this MysqlInstanceNodeInfo.

        创建时间，格式为\"yyyy-mm-ddThh:mm:ssZ\"。  其中，T指某个时间的开始；Z指时区偏移量，例如偏移1个小时显示为+0100。说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param created: The created of this MysqlInstanceNodeInfo.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this MysqlInstanceNodeInfo.

        更新时间，格式与\"created\"字段对应格式完全相同。说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :return: The updated of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this MysqlInstanceNodeInfo.

        更新时间，格式与\"created\"字段对应格式完全相同。说明：创建时返回值为空，数据库实例创建成功后该值不为空。

        :param updated: The updated of this MysqlInstanceNodeInfo.
        :type updated: str
        """
        self._updated = updated

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this MysqlInstanceNodeInfo.

        规格ID。

        :return: The flavor_id of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this MysqlInstanceNodeInfo.

        规格ID。

        :param flavor_id: The flavor_id of this MysqlInstanceNodeInfo.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this MysqlInstanceNodeInfo.

        规格码。

        :return: The flavor_ref of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this MysqlInstanceNodeInfo.

        规格码。

        :param flavor_ref: The flavor_ref of this MysqlInstanceNodeInfo.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def max_connections(self):
        r"""Gets the max_connections of this MysqlInstanceNodeInfo.

        允许的最大连接数。

        :return: The max_connections of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        r"""Sets the max_connections of this MysqlInstanceNodeInfo.

        允许的最大连接数。

        :param max_connections: The max_connections of this MysqlInstanceNodeInfo.
        :type max_connections: str
        """
        self._max_connections = max_connections

    @property
    def vcpus(self):
        r"""Gets the vcpus of this MysqlInstanceNodeInfo.

        CPU核数。

        :return: The vcpus of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        r"""Sets the vcpus of this MysqlInstanceNodeInfo.

        CPU核数。

        :param vcpus: The vcpus of this MysqlInstanceNodeInfo.
        :type vcpus: str
        """
        self._vcpus = vcpus

    @property
    def ram(self):
        r"""Gets the ram of this MysqlInstanceNodeInfo.

        内存大小，单位为GB。

        :return: The ram of this MysqlInstanceNodeInfo.
        :rtype: str
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        r"""Sets the ram of this MysqlInstanceNodeInfo.

        内存大小，单位为GB。

        :param ram: The ram of this MysqlInstanceNodeInfo.
        :type ram: str
        """
        self._ram = ram

    @property
    def need_restart(self):
        r"""Gets the need_restart of this MysqlInstanceNodeInfo.

        是否需要重启使修改的参数生效。

        :return: The need_restart of this MysqlInstanceNodeInfo.
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        r"""Sets the need_restart of this MysqlInstanceNodeInfo.

        是否需要重启使修改的参数生效。

        :param need_restart: The need_restart of this MysqlInstanceNodeInfo.
        :type need_restart: bool
        """
        self._need_restart = need_restart

    @property
    def priority(self):
        r"""Gets the priority of this MysqlInstanceNodeInfo.

        主备倒换优先级。

        :return: The priority of this MysqlInstanceNodeInfo.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this MysqlInstanceNodeInfo.

        主备倒换优先级。

        :param priority: The priority of this MysqlInstanceNodeInfo.
        :type priority: int
        """
        self._priority = priority

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
        if not isinstance(other, MysqlInstanceNodeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
