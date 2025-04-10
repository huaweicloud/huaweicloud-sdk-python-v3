# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScaleOutPolicyRsp:

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
        'scaling_enable': 'bool'
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
        'scaling_enable': 'scaling_enable'
    }

    def __init__(self, id=None, name=None, status=None, create_time=None, node_spec=None, availability_zone=None, nodes=None, max_nodes=None, min_nodes=None, scaling_times=None, scaling_enable=None):
        r"""ScaleOutPolicyRsp

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
        """
        
        

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

    @property
    def id(self):
        r"""Gets the id of this ScaleOutPolicyRsp.

        策略ID

        :return: The id of this ScaleOutPolicyRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScaleOutPolicyRsp.

        策略ID

        :param id: The id of this ScaleOutPolicyRsp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ScaleOutPolicyRsp.

        策略名称

        :return: The name of this ScaleOutPolicyRsp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScaleOutPolicyRsp.

        策略名称

        :param name: The name of this ScaleOutPolicyRsp.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ScaleOutPolicyRsp.

        状态

        :return: The status of this ScaleOutPolicyRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScaleOutPolicyRsp.

        状态

        :param status: The status of this ScaleOutPolicyRsp.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ScaleOutPolicyRsp.

        创建时间

        :return: The create_time of this ScaleOutPolicyRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ScaleOutPolicyRsp.

        创建时间

        :param create_time: The create_time of this ScaleOutPolicyRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def node_spec(self):
        r"""Gets the node_spec of this ScaleOutPolicyRsp.

        :return: The node_spec of this ScaleOutPolicyRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NodeSpecDto`
        """
        return self._node_spec

    @node_spec.setter
    def node_spec(self, node_spec):
        r"""Sets the node_spec of this ScaleOutPolicyRsp.

        :param node_spec: The node_spec of this ScaleOutPolicyRsp.
        :type node_spec: :class:`huaweicloudsdkeihealth.v1.NodeSpecDto`
        """
        self._node_spec = node_spec

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ScaleOutPolicyRsp.

        可用区

        :return: The availability_zone of this ScaleOutPolicyRsp.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ScaleOutPolicyRsp.

        可用区

        :param availability_zone: The availability_zone of this ScaleOutPolicyRsp.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def nodes(self):
        r"""Gets the nodes of this ScaleOutPolicyRsp.

        节点数量

        :return: The nodes of this ScaleOutPolicyRsp.
        :rtype: int
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this ScaleOutPolicyRsp.

        节点数量

        :param nodes: The nodes of this ScaleOutPolicyRsp.
        :type nodes: int
        """
        self._nodes = nodes

    @property
    def max_nodes(self):
        r"""Gets the max_nodes of this ScaleOutPolicyRsp.

        扩容节点数上限

        :return: The max_nodes of this ScaleOutPolicyRsp.
        :rtype: int
        """
        return self._max_nodes

    @max_nodes.setter
    def max_nodes(self, max_nodes):
        r"""Sets the max_nodes of this ScaleOutPolicyRsp.

        扩容节点数上限

        :param max_nodes: The max_nodes of this ScaleOutPolicyRsp.
        :type max_nodes: int
        """
        self._max_nodes = max_nodes

    @property
    def min_nodes(self):
        r"""Gets the min_nodes of this ScaleOutPolicyRsp.

        扩容节点数下限

        :return: The min_nodes of this ScaleOutPolicyRsp.
        :rtype: int
        """
        return self._min_nodes

    @min_nodes.setter
    def min_nodes(self, min_nodes):
        r"""Sets the min_nodes of this ScaleOutPolicyRsp.

        扩容节点数下限

        :param min_nodes: The min_nodes of this ScaleOutPolicyRsp.
        :type min_nodes: int
        """
        self._min_nodes = min_nodes

    @property
    def scaling_times(self):
        r"""Gets the scaling_times of this ScaleOutPolicyRsp.

        伸缩次数

        :return: The scaling_times of this ScaleOutPolicyRsp.
        :rtype: int
        """
        return self._scaling_times

    @scaling_times.setter
    def scaling_times(self, scaling_times):
        r"""Sets the scaling_times of this ScaleOutPolicyRsp.

        伸缩次数

        :param scaling_times: The scaling_times of this ScaleOutPolicyRsp.
        :type scaling_times: int
        """
        self._scaling_times = scaling_times

    @property
    def scaling_enable(self):
        r"""Gets the scaling_enable of this ScaleOutPolicyRsp.

        是否开启自动扩容

        :return: The scaling_enable of this ScaleOutPolicyRsp.
        :rtype: bool
        """
        return self._scaling_enable

    @scaling_enable.setter
    def scaling_enable(self, scaling_enable):
        r"""Sets the scaling_enable of this ScaleOutPolicyRsp.

        是否开启自动扩容

        :param scaling_enable: The scaling_enable of this ScaleOutPolicyRsp.
        :type scaling_enable: bool
        """
        self._scaling_enable = scaling_enable

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
        if not isinstance(other, ScaleOutPolicyRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
