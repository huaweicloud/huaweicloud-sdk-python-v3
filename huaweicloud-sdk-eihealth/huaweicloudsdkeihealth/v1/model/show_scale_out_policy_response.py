# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScaleOutPolicyResponse(SdkResponse):

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
        'status': 'str',
        'create_time': 'str',
        'node_spec': 'NodeSpecDto',
        'availability_zone': 'str',
        'nodes': 'int',
        'max_nodes': 'int',
        'min_nodes': 'int',
        'scaling_times': 'int',
        'scaling_enable': 'bool',
        'cpu_rule_enable': 'bool',
        'cpu_percent': 'int',
        'add_nodes_for_cpu_rule': 'int',
        'mem_rule_enable': 'bool',
        'mem_percent': 'int',
        'add_nodes_for_mem_rule': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'create_time': 'create_time',
        'node_spec': 'node_spec',
        'availability_zone': 'availability_zone',
        'nodes': 'nodes',
        'max_nodes': 'max_nodes',
        'min_nodes': 'min_nodes',
        'scaling_times': 'scaling_times',
        'scaling_enable': 'scaling_enable',
        'cpu_rule_enable': 'cpu_rule_enable',
        'cpu_percent': 'cpu_percent',
        'add_nodes_for_cpu_rule': 'add_nodes_for_cpu_rule',
        'mem_rule_enable': 'mem_rule_enable',
        'mem_percent': 'mem_percent',
        'add_nodes_for_mem_rule': 'add_nodes_for_mem_rule'
    }

    def __init__(self, id=None, name=None, status=None, create_time=None, node_spec=None, availability_zone=None, nodes=None, max_nodes=None, min_nodes=None, scaling_times=None, scaling_enable=None, cpu_rule_enable=None, cpu_percent=None, add_nodes_for_cpu_rule=None, mem_rule_enable=None, mem_percent=None, add_nodes_for_mem_rule=None):
        """ShowScaleOutPolicyResponse

        The model defined in huaweicloud sdk

        :param id: 策略ID
        :type id: str
        :param name: 策略名称
        :type name: str
        :param status: 状态
        :type status: str
        :param create_time: 创建时间
        :type create_time: str
        :param node_spec: 
        :type node_spec: :class:`huaweicloudsdkeihealth.v1.NodeSpecDto`
        :param availability_zone: 可用区
        :type availability_zone: str
        :param nodes: 节点数量
        :type nodes: int
        :param max_nodes: 扩容节点数上限
        :type max_nodes: int
        :param min_nodes: 扩容节点数下限
        :type min_nodes: int
        :param scaling_times: 伸缩次数
        :type scaling_times: int
        :param scaling_enable: 是否开启自动扩容
        :type scaling_enable: bool
        :param cpu_rule_enable: 是否开启cpu执行策略
        :type cpu_rule_enable: bool
        :param cpu_percent: cpu分配率百分比
        :type cpu_percent: int
        :param add_nodes_for_cpu_rule: 满足扩容策略中cpu分配率时增加的节点数
        :type add_nodes_for_cpu_rule: int
        :param mem_rule_enable: 是否开启mem执行策略
        :type mem_rule_enable: bool
        :param mem_percent: mem分配率百分比
        :type mem_percent: int
        :param add_nodes_for_mem_rule: 满足扩容策略中mem分配率时增加的节点数
        :type add_nodes_for_mem_rule: int
        """
        
        super(ShowScaleOutPolicyResponse, self).__init__()

        self._id = None
        self._name = None
        self._status = None
        self._create_time = None
        self._node_spec = None
        self._availability_zone = None
        self._nodes = None
        self._max_nodes = None
        self._min_nodes = None
        self._scaling_times = None
        self._scaling_enable = None
        self._cpu_rule_enable = None
        self._cpu_percent = None
        self._add_nodes_for_cpu_rule = None
        self._mem_rule_enable = None
        self._mem_percent = None
        self._add_nodes_for_mem_rule = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if node_spec is not None:
            self.node_spec = node_spec
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if nodes is not None:
            self.nodes = nodes
        if max_nodes is not None:
            self.max_nodes = max_nodes
        if min_nodes is not None:
            self.min_nodes = min_nodes
        if scaling_times is not None:
            self.scaling_times = scaling_times
        if scaling_enable is not None:
            self.scaling_enable = scaling_enable
        if cpu_rule_enable is not None:
            self.cpu_rule_enable = cpu_rule_enable
        if cpu_percent is not None:
            self.cpu_percent = cpu_percent
        if add_nodes_for_cpu_rule is not None:
            self.add_nodes_for_cpu_rule = add_nodes_for_cpu_rule
        if mem_rule_enable is not None:
            self.mem_rule_enable = mem_rule_enable
        if mem_percent is not None:
            self.mem_percent = mem_percent
        if add_nodes_for_mem_rule is not None:
            self.add_nodes_for_mem_rule = add_nodes_for_mem_rule

    @property
    def id(self):
        """Gets the id of this ShowScaleOutPolicyResponse.

        策略ID

        :return: The id of this ShowScaleOutPolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowScaleOutPolicyResponse.

        策略ID

        :param id: The id of this ShowScaleOutPolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowScaleOutPolicyResponse.

        策略名称

        :return: The name of this ShowScaleOutPolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowScaleOutPolicyResponse.

        策略名称

        :param name: The name of this ShowScaleOutPolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ShowScaleOutPolicyResponse.

        状态

        :return: The status of this ShowScaleOutPolicyResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowScaleOutPolicyResponse.

        状态

        :param status: The status of this ShowScaleOutPolicyResponse.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        """Gets the create_time of this ShowScaleOutPolicyResponse.

        创建时间

        :return: The create_time of this ShowScaleOutPolicyResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowScaleOutPolicyResponse.

        创建时间

        :param create_time: The create_time of this ShowScaleOutPolicyResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def node_spec(self):
        """Gets the node_spec of this ShowScaleOutPolicyResponse.

        :return: The node_spec of this ShowScaleOutPolicyResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NodeSpecDto`
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        """Sets the node_spec of this ShowScaleOutPolicyResponse.

        :param node_spec: The node_spec of this ShowScaleOutPolicyResponse.
        :type node_spec: :class:`huaweicloudsdkeihealth.v1.NodeSpecDto`
        """
        self._node_spec = node_spec

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ShowScaleOutPolicyResponse.

        可用区

        :return: The availability_zone of this ShowScaleOutPolicyResponse.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ShowScaleOutPolicyResponse.

        可用区

        :param availability_zone: The availability_zone of this ShowScaleOutPolicyResponse.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def nodes(self):
        """Gets the nodes of this ShowScaleOutPolicyResponse.

        节点数量

        :return: The nodes of this ShowScaleOutPolicyResponse.
        :rtype: int
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ShowScaleOutPolicyResponse.

        节点数量

        :param nodes: The nodes of this ShowScaleOutPolicyResponse.
        :type nodes: int
        """
        self._nodes = nodes

    @property
    def max_nodes(self):
        """Gets the max_nodes of this ShowScaleOutPolicyResponse.

        扩容节点数上限

        :return: The max_nodes of this ShowScaleOutPolicyResponse.
        :rtype: int
        """
        return self._max_nodes

    @max_nodes.setter
    def max_nodes(self, max_nodes):
        """Sets the max_nodes of this ShowScaleOutPolicyResponse.

        扩容节点数上限

        :param max_nodes: The max_nodes of this ShowScaleOutPolicyResponse.
        :type max_nodes: int
        """
        self._max_nodes = max_nodes

    @property
    def min_nodes(self):
        """Gets the min_nodes of this ShowScaleOutPolicyResponse.

        扩容节点数下限

        :return: The min_nodes of this ShowScaleOutPolicyResponse.
        :rtype: int
        """
        return self._min_nodes

    @min_nodes.setter
    def min_nodes(self, min_nodes):
        """Sets the min_nodes of this ShowScaleOutPolicyResponse.

        扩容节点数下限

        :param min_nodes: The min_nodes of this ShowScaleOutPolicyResponse.
        :type min_nodes: int
        """
        self._min_nodes = min_nodes

    @property
    def scaling_times(self):
        """Gets the scaling_times of this ShowScaleOutPolicyResponse.

        伸缩次数

        :return: The scaling_times of this ShowScaleOutPolicyResponse.
        :rtype: int
        """
        return self._scaling_times

    @scaling_times.setter
    def scaling_times(self, scaling_times):
        """Sets the scaling_times of this ShowScaleOutPolicyResponse.

        伸缩次数

        :param scaling_times: The scaling_times of this ShowScaleOutPolicyResponse.
        :type scaling_times: int
        """
        self._scaling_times = scaling_times

    @property
    def scaling_enable(self):
        """Gets the scaling_enable of this ShowScaleOutPolicyResponse.

        是否开启自动扩容

        :return: The scaling_enable of this ShowScaleOutPolicyResponse.
        :rtype: bool
        """
        return self._scaling_enable

    @scaling_enable.setter
    def scaling_enable(self, scaling_enable):
        """Sets the scaling_enable of this ShowScaleOutPolicyResponse.

        是否开启自动扩容

        :param scaling_enable: The scaling_enable of this ShowScaleOutPolicyResponse.
        :type scaling_enable: bool
        """
        self._scaling_enable = scaling_enable

    @property
    def cpu_rule_enable(self):
        """Gets the cpu_rule_enable of this ShowScaleOutPolicyResponse.

        是否开启cpu执行策略

        :return: The cpu_rule_enable of this ShowScaleOutPolicyResponse.
        :rtype: bool
        """
        return self._cpu_rule_enable

    @cpu_rule_enable.setter
    def cpu_rule_enable(self, cpu_rule_enable):
        """Sets the cpu_rule_enable of this ShowScaleOutPolicyResponse.

        是否开启cpu执行策略

        :param cpu_rule_enable: The cpu_rule_enable of this ShowScaleOutPolicyResponse.
        :type cpu_rule_enable: bool
        """
        self._cpu_rule_enable = cpu_rule_enable

    @property
    def cpu_percent(self):
        """Gets the cpu_percent of this ShowScaleOutPolicyResponse.

        cpu分配率百分比

        :return: The cpu_percent of this ShowScaleOutPolicyResponse.
        :rtype: int
        """
        return self._cpu_percent

    @cpu_percent.setter
    def cpu_percent(self, cpu_percent):
        """Sets the cpu_percent of this ShowScaleOutPolicyResponse.

        cpu分配率百分比

        :param cpu_percent: The cpu_percent of this ShowScaleOutPolicyResponse.
        :type cpu_percent: int
        """
        self._cpu_percent = cpu_percent

    @property
    def add_nodes_for_cpu_rule(self):
        """Gets the add_nodes_for_cpu_rule of this ShowScaleOutPolicyResponse.

        满足扩容策略中cpu分配率时增加的节点数

        :return: The add_nodes_for_cpu_rule of this ShowScaleOutPolicyResponse.
        :rtype: int
        """
        return self._add_nodes_for_cpu_rule

    @add_nodes_for_cpu_rule.setter
    def add_nodes_for_cpu_rule(self, add_nodes_for_cpu_rule):
        """Sets the add_nodes_for_cpu_rule of this ShowScaleOutPolicyResponse.

        满足扩容策略中cpu分配率时增加的节点数

        :param add_nodes_for_cpu_rule: The add_nodes_for_cpu_rule of this ShowScaleOutPolicyResponse.
        :type add_nodes_for_cpu_rule: int
        """
        self._add_nodes_for_cpu_rule = add_nodes_for_cpu_rule

    @property
    def mem_rule_enable(self):
        """Gets the mem_rule_enable of this ShowScaleOutPolicyResponse.

        是否开启mem执行策略

        :return: The mem_rule_enable of this ShowScaleOutPolicyResponse.
        :rtype: bool
        """
        return self._mem_rule_enable

    @mem_rule_enable.setter
    def mem_rule_enable(self, mem_rule_enable):
        """Sets the mem_rule_enable of this ShowScaleOutPolicyResponse.

        是否开启mem执行策略

        :param mem_rule_enable: The mem_rule_enable of this ShowScaleOutPolicyResponse.
        :type mem_rule_enable: bool
        """
        self._mem_rule_enable = mem_rule_enable

    @property
    def mem_percent(self):
        """Gets the mem_percent of this ShowScaleOutPolicyResponse.

        mem分配率百分比

        :return: The mem_percent of this ShowScaleOutPolicyResponse.
        :rtype: int
        """
        return self._mem_percent

    @mem_percent.setter
    def mem_percent(self, mem_percent):
        """Sets the mem_percent of this ShowScaleOutPolicyResponse.

        mem分配率百分比

        :param mem_percent: The mem_percent of this ShowScaleOutPolicyResponse.
        :type mem_percent: int
        """
        self._mem_percent = mem_percent

    @property
    def add_nodes_for_mem_rule(self):
        """Gets the add_nodes_for_mem_rule of this ShowScaleOutPolicyResponse.

        满足扩容策略中mem分配率时增加的节点数

        :return: The add_nodes_for_mem_rule of this ShowScaleOutPolicyResponse.
        :rtype: int
        """
        return self._add_nodes_for_mem_rule

    @add_nodes_for_mem_rule.setter
    def add_nodes_for_mem_rule(self, add_nodes_for_mem_rule):
        """Sets the add_nodes_for_mem_rule of this ShowScaleOutPolicyResponse.

        满足扩容策略中mem分配率时增加的节点数

        :param add_nodes_for_mem_rule: The add_nodes_for_mem_rule of this ShowScaleOutPolicyResponse.
        :type add_nodes_for_mem_rule: int
        """
        self._add_nodes_for_mem_rule = add_nodes_for_mem_rule

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
        if not isinstance(other, ShowScaleOutPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
