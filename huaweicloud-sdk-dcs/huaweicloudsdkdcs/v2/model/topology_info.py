# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopologyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'node_name': 'str',
        'ip': 'str',
        'port': 'str',
        'node_type': 'str',
        'max_memory': 'str',
        'used_memory': 'str',
        'qps': 'str',
        'bandwidth': 'BandWidth',
        'db_num': 'str',
        'dbs': 'KeySpace',
        'relation_ip': 'str',
        'relation_port': 'str',
        'group_id': 'str',
        'status': 'str',
        'dims': 'DimsInfo'
    }

    attribute_map = {
        'node_id': 'node_id',
        'node_name': 'node_name',
        'ip': 'ip',
        'port': 'port',
        'node_type': 'node_type',
        'max_memory': 'max_memory',
        'used_memory': 'used_memory',
        'qps': 'qps',
        'bandwidth': 'bandwidth',
        'db_num': 'db_num',
        'dbs': 'dbs',
        'relation_ip': 'relation_ip',
        'relation_port': 'relation_port',
        'group_id': 'group_id',
        'status': 'status',
        'dims': 'dims'
    }

    def __init__(self, node_id=None, node_name=None, ip=None, port=None, node_type=None, max_memory=None, used_memory=None, qps=None, bandwidth=None, db_num=None, dbs=None, relation_ip=None, relation_port=None, group_id=None, status=None, dims=None):
        r"""TopologyInfo

        The model defined in huaweicloud sdk

        :param node_id: **参数解释**： 节点ID。 **取值范围**： 不涉及。 
        :type node_id: str
        :param node_name: **参数解释**： 节点名称。 **取值范围**： 不涉及。 
        :type node_name: str
        :param ip: **参数解释**： 节点IP。 **取值范围**： 不涉及。 
        :type ip: str
        :param port: **参数解释**： 节点端口。 **取值范围**： 不涉及。 
        :type port: str
        :param node_type: **参数解释**： 节点主从角色。 **取值范围**： master：主节点 slave：从节点 proxy：proxy节点 
        :type node_type: str
        :param max_memory: **参数解释**： 总内存，单位：MB。 **取值范围**： 不涉及。 
        :type max_memory: str
        :param used_memory: **参数解释**： 已使用的内存，单位：MB。 **取值范围**： 不涉及。 
        :type used_memory: str
        :param qps: **参数解释**： 每秒查询率。 **取值范围**： 不涉及。 
        :type qps: str
        :param bandwidth: 
        :type bandwidth: :class:`huaweicloudsdkdcs.v2.BandWidth`
        :param db_num: **参数解释**： 该实例的DB数量。 **取值范围**： 不涉及。 
        :type db_num: str
        :param dbs: 
        :type dbs: :class:`huaweicloudsdkdcs.v2.KeySpace`
        :param relation_ip: **参数解释**： 关联IP。 **取值范围**： 不涉及。 
        :type relation_ip: str
        :param relation_port: **参数解释**： 关联端口。 **取值范围**： 不涉及。 
        :type relation_port: str
        :param group_id: **参数解释**： 分片ID。 **取值范围**： 不涉及。 
        :type group_id: str
        :param status: **参数解释**： 节点状态。 **取值范围**： 不涉及。 
        :type status: str
        :param dims: 
        :type dims: :class:`huaweicloudsdkdcs.v2.DimsInfo`
        """
        
        

        self._node_id = None
        self._node_name = None
        self._ip = None
        self._port = None
        self._node_type = None
        self._max_memory = None
        self._used_memory = None
        self._qps = None
        self._bandwidth = None
        self._db_num = None
        self._dbs = None
        self._relation_ip = None
        self._relation_port = None
        self._group_id = None
        self._status = None
        self._dims = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if ip is not None:
            self.ip = ip
        if port is not None:
            self.port = port
        if node_type is not None:
            self.node_type = node_type
        if max_memory is not None:
            self.max_memory = max_memory
        if used_memory is not None:
            self.used_memory = used_memory
        if qps is not None:
            self.qps = qps
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if db_num is not None:
            self.db_num = db_num
        if dbs is not None:
            self.dbs = dbs
        if relation_ip is not None:
            self.relation_ip = relation_ip
        if relation_port is not None:
            self.relation_port = relation_port
        if group_id is not None:
            self.group_id = group_id
        if status is not None:
            self.status = status
        if dims is not None:
            self.dims = dims

    @property
    def node_id(self):
        r"""Gets the node_id of this TopologyInfo.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。 

        :return: The node_id of this TopologyInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this TopologyInfo.

        **参数解释**： 节点ID。 **取值范围**： 不涉及。 

        :param node_id: The node_id of this TopologyInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this TopologyInfo.

        **参数解释**： 节点名称。 **取值范围**： 不涉及。 

        :return: The node_name of this TopologyInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this TopologyInfo.

        **参数解释**： 节点名称。 **取值范围**： 不涉及。 

        :param node_name: The node_name of this TopologyInfo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def ip(self):
        r"""Gets the ip of this TopologyInfo.

        **参数解释**： 节点IP。 **取值范围**： 不涉及。 

        :return: The ip of this TopologyInfo.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this TopologyInfo.

        **参数解释**： 节点IP。 **取值范围**： 不涉及。 

        :param ip: The ip of this TopologyInfo.
        :type ip: str
        """
        self._ip = ip

    @property
    def port(self):
        r"""Gets the port of this TopologyInfo.

        **参数解释**： 节点端口。 **取值范围**： 不涉及。 

        :return: The port of this TopologyInfo.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this TopologyInfo.

        **参数解释**： 节点端口。 **取值范围**： 不涉及。 

        :param port: The port of this TopologyInfo.
        :type port: str
        """
        self._port = port

    @property
    def node_type(self):
        r"""Gets the node_type of this TopologyInfo.

        **参数解释**： 节点主从角色。 **取值范围**： master：主节点 slave：从节点 proxy：proxy节点 

        :return: The node_type of this TopologyInfo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this TopologyInfo.

        **参数解释**： 节点主从角色。 **取值范围**： master：主节点 slave：从节点 proxy：proxy节点 

        :param node_type: The node_type of this TopologyInfo.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def max_memory(self):
        r"""Gets the max_memory of this TopologyInfo.

        **参数解释**： 总内存，单位：MB。 **取值范围**： 不涉及。 

        :return: The max_memory of this TopologyInfo.
        :rtype: str
        """
        return self._max_memory

    @max_memory.setter
    def max_memory(self, max_memory):
        r"""Sets the max_memory of this TopologyInfo.

        **参数解释**： 总内存，单位：MB。 **取值范围**： 不涉及。 

        :param max_memory: The max_memory of this TopologyInfo.
        :type max_memory: str
        """
        self._max_memory = max_memory

    @property
    def used_memory(self):
        r"""Gets the used_memory of this TopologyInfo.

        **参数解释**： 已使用的内存，单位：MB。 **取值范围**： 不涉及。 

        :return: The used_memory of this TopologyInfo.
        :rtype: str
        """
        return self._used_memory

    @used_memory.setter
    def used_memory(self, used_memory):
        r"""Sets the used_memory of this TopologyInfo.

        **参数解释**： 已使用的内存，单位：MB。 **取值范围**： 不涉及。 

        :param used_memory: The used_memory of this TopologyInfo.
        :type used_memory: str
        """
        self._used_memory = used_memory

    @property
    def qps(self):
        r"""Gets the qps of this TopologyInfo.

        **参数解释**： 每秒查询率。 **取值范围**： 不涉及。 

        :return: The qps of this TopologyInfo.
        :rtype: str
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        r"""Sets the qps of this TopologyInfo.

        **参数解释**： 每秒查询率。 **取值范围**： 不涉及。 

        :param qps: The qps of this TopologyInfo.
        :type qps: str
        """
        self._qps = qps

    @property
    def bandwidth(self):
        r"""Gets the bandwidth of this TopologyInfo.

        :return: The bandwidth of this TopologyInfo.
        :rtype: :class:`huaweicloudsdkdcs.v2.BandWidth`
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        r"""Sets the bandwidth of this TopologyInfo.

        :param bandwidth: The bandwidth of this TopologyInfo.
        :type bandwidth: :class:`huaweicloudsdkdcs.v2.BandWidth`
        """
        self._bandwidth = bandwidth

    @property
    def db_num(self):
        r"""Gets the db_num of this TopologyInfo.

        **参数解释**： 该实例的DB数量。 **取值范围**： 不涉及。 

        :return: The db_num of this TopologyInfo.
        :rtype: str
        """
        return self._db_num

    @db_num.setter
    def db_num(self, db_num):
        r"""Sets the db_num of this TopologyInfo.

        **参数解释**： 该实例的DB数量。 **取值范围**： 不涉及。 

        :param db_num: The db_num of this TopologyInfo.
        :type db_num: str
        """
        self._db_num = db_num

    @property
    def dbs(self):
        r"""Gets the dbs of this TopologyInfo.

        :return: The dbs of this TopologyInfo.
        :rtype: :class:`huaweicloudsdkdcs.v2.KeySpace`
        """
        return self._dbs

    @dbs.setter
    def dbs(self, dbs):
        r"""Sets the dbs of this TopologyInfo.

        :param dbs: The dbs of this TopologyInfo.
        :type dbs: :class:`huaweicloudsdkdcs.v2.KeySpace`
        """
        self._dbs = dbs

    @property
    def relation_ip(self):
        r"""Gets the relation_ip of this TopologyInfo.

        **参数解释**： 关联IP。 **取值范围**： 不涉及。 

        :return: The relation_ip of this TopologyInfo.
        :rtype: str
        """
        return self._relation_ip

    @relation_ip.setter
    def relation_ip(self, relation_ip):
        r"""Sets the relation_ip of this TopologyInfo.

        **参数解释**： 关联IP。 **取值范围**： 不涉及。 

        :param relation_ip: The relation_ip of this TopologyInfo.
        :type relation_ip: str
        """
        self._relation_ip = relation_ip

    @property
    def relation_port(self):
        r"""Gets the relation_port of this TopologyInfo.

        **参数解释**： 关联端口。 **取值范围**： 不涉及。 

        :return: The relation_port of this TopologyInfo.
        :rtype: str
        """
        return self._relation_port

    @relation_port.setter
    def relation_port(self, relation_port):
        r"""Sets the relation_port of this TopologyInfo.

        **参数解释**： 关联端口。 **取值范围**： 不涉及。 

        :param relation_port: The relation_port of this TopologyInfo.
        :type relation_port: str
        """
        self._relation_port = relation_port

    @property
    def group_id(self):
        r"""Gets the group_id of this TopologyInfo.

        **参数解释**： 分片ID。 **取值范围**： 不涉及。 

        :return: The group_id of this TopologyInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this TopologyInfo.

        **参数解释**： 分片ID。 **取值范围**： 不涉及。 

        :param group_id: The group_id of this TopologyInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def status(self):
        r"""Gets the status of this TopologyInfo.

        **参数解释**： 节点状态。 **取值范围**： 不涉及。 

        :return: The status of this TopologyInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TopologyInfo.

        **参数解释**： 节点状态。 **取值范围**： 不涉及。 

        :param status: The status of this TopologyInfo.
        :type status: str
        """
        self._status = status

    @property
    def dims(self):
        r"""Gets the dims of this TopologyInfo.

        :return: The dims of this TopologyInfo.
        :rtype: :class:`huaweicloudsdkdcs.v2.DimsInfo`
        """
        return self._dims

    @dims.setter
    def dims(self, dims):
        r"""Sets the dims of this TopologyInfo.

        :param dims: The dims of this TopologyInfo.
        :type dims: :class:`huaweicloudsdkdcs.v2.DimsInfo`
        """
        self._dims = dims

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
        if not isinstance(other, TopologyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
