# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterConfigResponseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'protect_node_num': 'int',
        'protect_interrupt_node_num': 'int',
        'unprotect_node_num': 'int',
        'node_total_num': 'int',
        'cluster_name': 'str',
        'charging_mode': 'str',
        'auto_upgrade': 'bool',
        'prefer_packet_cycle': 'int',
        'vpc_id': 'str',
        'protect_type': 'str',
        'protect_status': 'str',
        'cluster_type': 'str',
        'fail_reason': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'protect_node_num': 'protect_node_num',
        'protect_interrupt_node_num': 'protect_interrupt_node_num',
        'unprotect_node_num': 'unprotect_node_num',
        'node_total_num': 'node_total_num',
        'cluster_name': 'cluster_name',
        'charging_mode': 'charging_mode',
        'auto_upgrade': 'auto_upgrade',
        'prefer_packet_cycle': 'prefer_packet_cycle',
        'vpc_id': 'vpc_id',
        'protect_type': 'protect_type',
        'protect_status': 'protect_status',
        'cluster_type': 'cluster_type',
        'fail_reason': 'fail_reason'
    }

    def __init__(self, cluster_id=None, protect_node_num=None, protect_interrupt_node_num=None, unprotect_node_num=None, node_total_num=None, cluster_name=None, charging_mode=None, auto_upgrade=None, prefer_packet_cycle=None, vpc_id=None, protect_type=None, protect_status=None, cluster_type=None, fail_reason=None):
        """ClusterConfigResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param protect_node_num: 集群开启防护节点数量
        :type protect_node_num: int
        :param protect_interrupt_node_num: 集群防护中断节点数量
        :type protect_interrupt_node_num: int
        :param unprotect_node_num: 集群防护中断节点数量
        :type unprotect_node_num: int
        :param node_total_num: 集群节点总数
        :type node_total_num: int
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param charging_mode: 付费模式 | on_demand 按需 free 免费
        :type charging_mode: str
        :param auto_upgrade: 开启agent自动升级
        :type auto_upgrade: bool
        :param prefer_packet_cycle: 优先使用包周期配额；默认0
        :type prefer_packet_cycle: int
        :param vpc_id: vpc id
        :type vpc_id: str
        :param protect_type: cce protection type
        :type protect_type: str
        :param protect_status: protection status
        :type protect_status: str
        :param cluster_type: cluster type
        :type cluster_type: str
        :param fail_reason: fail reason
        :type fail_reason: str
        """
        
        

        self._cluster_id = None
        self._protect_node_num = None
        self._protect_interrupt_node_num = None
        self._unprotect_node_num = None
        self._node_total_num = None
        self._cluster_name = None
        self._charging_mode = None
        self._auto_upgrade = None
        self._prefer_packet_cycle = None
        self._vpc_id = None
        self._protect_type = None
        self._protect_status = None
        self._cluster_type = None
        self._fail_reason = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if protect_node_num is not None:
            self.protect_node_num = protect_node_num
        if protect_interrupt_node_num is not None:
            self.protect_interrupt_node_num = protect_interrupt_node_num
        if unprotect_node_num is not None:
            self.unprotect_node_num = unprotect_node_num
        if node_total_num is not None:
            self.node_total_num = node_total_num
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if auto_upgrade is not None:
            self.auto_upgrade = auto_upgrade
        if prefer_packet_cycle is not None:
            self.prefer_packet_cycle = prefer_packet_cycle
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if protect_type is not None:
            self.protect_type = protect_type
        if protect_status is not None:
            self.protect_status = protect_status
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if fail_reason is not None:
            self.fail_reason = fail_reason

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusterConfigResponseInfo.

        集群id

        :return: The cluster_id of this ClusterConfigResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusterConfigResponseInfo.

        集群id

        :param cluster_id: The cluster_id of this ClusterConfigResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def protect_node_num(self):
        """Gets the protect_node_num of this ClusterConfigResponseInfo.

        集群开启防护节点数量

        :return: The protect_node_num of this ClusterConfigResponseInfo.
        :rtype: int
        """
        return self._protect_node_num

    @protect_node_num.setter
    def protect_node_num(self, protect_node_num):
        """Sets the protect_node_num of this ClusterConfigResponseInfo.

        集群开启防护节点数量

        :param protect_node_num: The protect_node_num of this ClusterConfigResponseInfo.
        :type protect_node_num: int
        """
        self._protect_node_num = protect_node_num

    @property
    def protect_interrupt_node_num(self):
        """Gets the protect_interrupt_node_num of this ClusterConfigResponseInfo.

        集群防护中断节点数量

        :return: The protect_interrupt_node_num of this ClusterConfigResponseInfo.
        :rtype: int
        """
        return self._protect_interrupt_node_num

    @protect_interrupt_node_num.setter
    def protect_interrupt_node_num(self, protect_interrupt_node_num):
        """Sets the protect_interrupt_node_num of this ClusterConfigResponseInfo.

        集群防护中断节点数量

        :param protect_interrupt_node_num: The protect_interrupt_node_num of this ClusterConfigResponseInfo.
        :type protect_interrupt_node_num: int
        """
        self._protect_interrupt_node_num = protect_interrupt_node_num

    @property
    def unprotect_node_num(self):
        """Gets the unprotect_node_num of this ClusterConfigResponseInfo.

        集群防护中断节点数量

        :return: The unprotect_node_num of this ClusterConfigResponseInfo.
        :rtype: int
        """
        return self._unprotect_node_num

    @unprotect_node_num.setter
    def unprotect_node_num(self, unprotect_node_num):
        """Sets the unprotect_node_num of this ClusterConfigResponseInfo.

        集群防护中断节点数量

        :param unprotect_node_num: The unprotect_node_num of this ClusterConfigResponseInfo.
        :type unprotect_node_num: int
        """
        self._unprotect_node_num = unprotect_node_num

    @property
    def node_total_num(self):
        """Gets the node_total_num of this ClusterConfigResponseInfo.

        集群节点总数

        :return: The node_total_num of this ClusterConfigResponseInfo.
        :rtype: int
        """
        return self._node_total_num

    @node_total_num.setter
    def node_total_num(self, node_total_num):
        """Sets the node_total_num of this ClusterConfigResponseInfo.

        集群节点总数

        :param node_total_num: The node_total_num of this ClusterConfigResponseInfo.
        :type node_total_num: int
        """
        self._node_total_num = node_total_num

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ClusterConfigResponseInfo.

        集群名称

        :return: The cluster_name of this ClusterConfigResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ClusterConfigResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClusterConfigResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ClusterConfigResponseInfo.

        付费模式 | on_demand 按需 free 免费

        :return: The charging_mode of this ClusterConfigResponseInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ClusterConfigResponseInfo.

        付费模式 | on_demand 按需 free 免费

        :param charging_mode: The charging_mode of this ClusterConfigResponseInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def auto_upgrade(self):
        """Gets the auto_upgrade of this ClusterConfigResponseInfo.

        开启agent自动升级

        :return: The auto_upgrade of this ClusterConfigResponseInfo.
        :rtype: bool
        """
        return self._auto_upgrade

    @auto_upgrade.setter
    def auto_upgrade(self, auto_upgrade):
        """Sets the auto_upgrade of this ClusterConfigResponseInfo.

        开启agent自动升级

        :param auto_upgrade: The auto_upgrade of this ClusterConfigResponseInfo.
        :type auto_upgrade: bool
        """
        self._auto_upgrade = auto_upgrade

    @property
    def prefer_packet_cycle(self):
        """Gets the prefer_packet_cycle of this ClusterConfigResponseInfo.

        优先使用包周期配额；默认0

        :return: The prefer_packet_cycle of this ClusterConfigResponseInfo.
        :rtype: int
        """
        return self._prefer_packet_cycle

    @prefer_packet_cycle.setter
    def prefer_packet_cycle(self, prefer_packet_cycle):
        """Sets the prefer_packet_cycle of this ClusterConfigResponseInfo.

        优先使用包周期配额；默认0

        :param prefer_packet_cycle: The prefer_packet_cycle of this ClusterConfigResponseInfo.
        :type prefer_packet_cycle: int
        """
        self._prefer_packet_cycle = prefer_packet_cycle

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ClusterConfigResponseInfo.

        vpc id

        :return: The vpc_id of this ClusterConfigResponseInfo.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ClusterConfigResponseInfo.

        vpc id

        :param vpc_id: The vpc_id of this ClusterConfigResponseInfo.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def protect_type(self):
        """Gets the protect_type of this ClusterConfigResponseInfo.

        cce protection type

        :return: The protect_type of this ClusterConfigResponseInfo.
        :rtype: str
        """
        return self._protect_type

    @protect_type.setter
    def protect_type(self, protect_type):
        """Sets the protect_type of this ClusterConfigResponseInfo.

        cce protection type

        :param protect_type: The protect_type of this ClusterConfigResponseInfo.
        :type protect_type: str
        """
        self._protect_type = protect_type

    @property
    def protect_status(self):
        """Gets the protect_status of this ClusterConfigResponseInfo.

        protection status

        :return: The protect_status of this ClusterConfigResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        """Sets the protect_status of this ClusterConfigResponseInfo.

        protection status

        :param protect_status: The protect_status of this ClusterConfigResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

    @property
    def cluster_type(self):
        """Gets the cluster_type of this ClusterConfigResponseInfo.

        cluster type

        :return: The cluster_type of this ClusterConfigResponseInfo.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this ClusterConfigResponseInfo.

        cluster type

        :param cluster_type: The cluster_type of this ClusterConfigResponseInfo.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ClusterConfigResponseInfo.

        fail reason

        :return: The fail_reason of this ClusterConfigResponseInfo.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ClusterConfigResponseInfo.

        fail reason

        :param fail_reason: The fail_reason of this ClusterConfigResponseInfo.
        :type fail_reason: str
        """
        self._fail_reason = fail_reason

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
        if not isinstance(other, ClusterConfigResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
