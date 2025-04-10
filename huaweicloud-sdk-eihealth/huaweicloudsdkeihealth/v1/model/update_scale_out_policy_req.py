# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScaleOutPolicyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'max_nodes': 'int',
        'min_nodes': 'int',
        'cpu_rule_enable': 'bool',
        'cpu_percent': 'int',
        'add_nodes_for_cpu_rule': 'int',
        'mem_rule_enable': 'bool',
        'mem_percent': 'int',
        'add_nodes_for_mem_rule': 'int'
    }

    attribute_map = {
        'name': 'name',
        'max_nodes': 'max_nodes',
        'min_nodes': 'min_nodes',
        'cpu_rule_enable': 'cpu_rule_enable',
        'cpu_percent': 'cpu_percent',
        'add_nodes_for_cpu_rule': 'add_nodes_for_cpu_rule',
        'mem_rule_enable': 'mem_rule_enable',
        'mem_percent': 'mem_percent',
        'add_nodes_for_mem_rule': 'add_nodes_for_mem_rule'
    }

    def __init__(self, name=None, max_nodes=None, min_nodes=None, cpu_rule_enable=None, cpu_percent=None, add_nodes_for_cpu_rule=None, mem_rule_enable=None, mem_percent=None, add_nodes_for_mem_rule=None):
        r"""UpdateScaleOutPolicyReq

        The model defined in huaweicloud sdk

        :param name: 策略名称
        :type name: str
        :param max_nodes: 扩容节点数上限
        :type max_nodes: int
        :param min_nodes: 扩容节点数下限
        :type min_nodes: int
        :param cpu_rule_enable: 是否启用cpu规则
        :type cpu_rule_enable: bool
        :param cpu_percent: cpu分配率百分比
        :type cpu_percent: int
        :param add_nodes_for_cpu_rule: 满足扩容策略中cpu分配率时增加的节点数
        :type add_nodes_for_cpu_rule: int
        :param mem_rule_enable: 是否启用mem规则
        :type mem_rule_enable: bool
        :param mem_percent: mem分配率百分比
        :type mem_percent: int
        :param add_nodes_for_mem_rule: 满足扩容策略中mem分配率时增加的节点数
        :type add_nodes_for_mem_rule: int
        """
        
        

        self._name = None
        self._max_nodes = None
        self._min_nodes = None
        self._cpu_rule_enable = None
        self._cpu_percent = None
        self._add_nodes_for_cpu_rule = None
        self._mem_rule_enable = None
        self._mem_percent = None
        self._add_nodes_for_mem_rule = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if max_nodes is not None:
            self.max_nodes = max_nodes
        if min_nodes is not None:
            self.min_nodes = min_nodes
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
    def name(self):
        r"""Gets the name of this UpdateScaleOutPolicyReq.

        策略名称

        :return: The name of this UpdateScaleOutPolicyReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateScaleOutPolicyReq.

        策略名称

        :param name: The name of this UpdateScaleOutPolicyReq.
        :type name: str
        """
        self._name = name

    @property
    def max_nodes(self):
        r"""Gets the max_nodes of this UpdateScaleOutPolicyReq.

        扩容节点数上限

        :return: The max_nodes of this UpdateScaleOutPolicyReq.
        :rtype: int
        """
        return self._max_nodes

    @max_nodes.setter
    def max_nodes(self, max_nodes):
        r"""Sets the max_nodes of this UpdateScaleOutPolicyReq.

        扩容节点数上限

        :param max_nodes: The max_nodes of this UpdateScaleOutPolicyReq.
        :type max_nodes: int
        """
        self._max_nodes = max_nodes

    @property
    def min_nodes(self):
        r"""Gets the min_nodes of this UpdateScaleOutPolicyReq.

        扩容节点数下限

        :return: The min_nodes of this UpdateScaleOutPolicyReq.
        :rtype: int
        """
        return self._min_nodes

    @min_nodes.setter
    def min_nodes(self, min_nodes):
        r"""Sets the min_nodes of this UpdateScaleOutPolicyReq.

        扩容节点数下限

        :param min_nodes: The min_nodes of this UpdateScaleOutPolicyReq.
        :type min_nodes: int
        """
        self._min_nodes = min_nodes

    @property
    def cpu_rule_enable(self):
        r"""Gets the cpu_rule_enable of this UpdateScaleOutPolicyReq.

        是否启用cpu规则

        :return: The cpu_rule_enable of this UpdateScaleOutPolicyReq.
        :rtype: bool
        """
        return self._cpu_rule_enable

    @cpu_rule_enable.setter
    def cpu_rule_enable(self, cpu_rule_enable):
        r"""Sets the cpu_rule_enable of this UpdateScaleOutPolicyReq.

        是否启用cpu规则

        :param cpu_rule_enable: The cpu_rule_enable of this UpdateScaleOutPolicyReq.
        :type cpu_rule_enable: bool
        """
        self._cpu_rule_enable = cpu_rule_enable

    @property
    def cpu_percent(self):
        r"""Gets the cpu_percent of this UpdateScaleOutPolicyReq.

        cpu分配率百分比

        :return: The cpu_percent of this UpdateScaleOutPolicyReq.
        :rtype: int
        """
        return self._cpu_percent

    @cpu_percent.setter
    def cpu_percent(self, cpu_percent):
        r"""Sets the cpu_percent of this UpdateScaleOutPolicyReq.

        cpu分配率百分比

        :param cpu_percent: The cpu_percent of this UpdateScaleOutPolicyReq.
        :type cpu_percent: int
        """
        self._cpu_percent = cpu_percent

    @property
    def add_nodes_for_cpu_rule(self):
        r"""Gets the add_nodes_for_cpu_rule of this UpdateScaleOutPolicyReq.

        满足扩容策略中cpu分配率时增加的节点数

        :return: The add_nodes_for_cpu_rule of this UpdateScaleOutPolicyReq.
        :rtype: int
        """
        return self._add_nodes_for_cpu_rule

    @add_nodes_for_cpu_rule.setter
    def add_nodes_for_cpu_rule(self, add_nodes_for_cpu_rule):
        r"""Sets the add_nodes_for_cpu_rule of this UpdateScaleOutPolicyReq.

        满足扩容策略中cpu分配率时增加的节点数

        :param add_nodes_for_cpu_rule: The add_nodes_for_cpu_rule of this UpdateScaleOutPolicyReq.
        :type add_nodes_for_cpu_rule: int
        """
        self._add_nodes_for_cpu_rule = add_nodes_for_cpu_rule

    @property
    def mem_rule_enable(self):
        r"""Gets the mem_rule_enable of this UpdateScaleOutPolicyReq.

        是否启用mem规则

        :return: The mem_rule_enable of this UpdateScaleOutPolicyReq.
        :rtype: bool
        """
        return self._mem_rule_enable

    @mem_rule_enable.setter
    def mem_rule_enable(self, mem_rule_enable):
        r"""Sets the mem_rule_enable of this UpdateScaleOutPolicyReq.

        是否启用mem规则

        :param mem_rule_enable: The mem_rule_enable of this UpdateScaleOutPolicyReq.
        :type mem_rule_enable: bool
        """
        self._mem_rule_enable = mem_rule_enable

    @property
    def mem_percent(self):
        r"""Gets the mem_percent of this UpdateScaleOutPolicyReq.

        mem分配率百分比

        :return: The mem_percent of this UpdateScaleOutPolicyReq.
        :rtype: int
        """
        return self._mem_percent

    @mem_percent.setter
    def mem_percent(self, mem_percent):
        r"""Sets the mem_percent of this UpdateScaleOutPolicyReq.

        mem分配率百分比

        :param mem_percent: The mem_percent of this UpdateScaleOutPolicyReq.
        :type mem_percent: int
        """
        self._mem_percent = mem_percent

    @property
    def add_nodes_for_mem_rule(self):
        r"""Gets the add_nodes_for_mem_rule of this UpdateScaleOutPolicyReq.

        满足扩容策略中mem分配率时增加的节点数

        :return: The add_nodes_for_mem_rule of this UpdateScaleOutPolicyReq.
        :rtype: int
        """
        return self._add_nodes_for_mem_rule

    @add_nodes_for_mem_rule.setter
    def add_nodes_for_mem_rule(self, add_nodes_for_mem_rule):
        r"""Sets the add_nodes_for_mem_rule of this UpdateScaleOutPolicyReq.

        满足扩容策略中mem分配率时增加的节点数

        :param add_nodes_for_mem_rule: The add_nodes_for_mem_rule of this UpdateScaleOutPolicyReq.
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
        if not isinstance(other, UpdateScaleOutPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
