# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateScaleOutPolicyReq:

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
        'availability_zone': 'str',
        'spec_code': 'str',
        'max_nodes': 'int',
        'min_nodes': 'int',
        'data_disk_spec_code': 'str',
        'data_disk_size': 'int',
        'cpu_rule_enable': 'bool',
        'cpu_percent': 'int',
        'add_nodes_for_cpu_rule': 'int',
        'mem_rule_enable': 'bool',
        'mem_percent': 'int',
        'add_nodes_for_mem_rule': 'int'
    }

    attribute_map = {
        'name': 'name',
        'availability_zone': 'availability_zone',
        'spec_code': 'spec_code',
        'max_nodes': 'max_nodes',
        'min_nodes': 'min_nodes',
        'data_disk_spec_code': 'data_disk_spec_code',
        'data_disk_size': 'data_disk_size',
        'cpu_rule_enable': 'cpu_rule_enable',
        'cpu_percent': 'cpu_percent',
        'add_nodes_for_cpu_rule': 'add_nodes_for_cpu_rule',
        'mem_rule_enable': 'mem_rule_enable',
        'mem_percent': 'mem_percent',
        'add_nodes_for_mem_rule': 'add_nodes_for_mem_rule'
    }

    def __init__(self, name=None, availability_zone=None, spec_code=None, max_nodes=None, min_nodes=None, data_disk_spec_code=None, data_disk_size=None, cpu_rule_enable=None, cpu_percent=None, add_nodes_for_cpu_rule=None, mem_rule_enable=None, mem_percent=None, add_nodes_for_mem_rule=None):
        r"""CreateScaleOutPolicyReq

        The model defined in huaweicloud sdk

        :param name: 策略名称
        :type name: str
        :param availability_zone: 可用区
        :type availability_zone: str
        :param spec_code: 规格编码
        :type spec_code: str
        :param max_nodes: 扩容节点数上限
        :type max_nodes: int
        :param min_nodes: 扩容节点数下限
        :type min_nodes: int
        :param data_disk_spec_code: 额外数据盘规格编码
        :type data_disk_spec_code: str
        :param data_disk_size: 额外数据盘大小
        :type data_disk_size: int
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
        self._availability_zone = None
        self._spec_code = None
        self._max_nodes = None
        self._min_nodes = None
        self._data_disk_spec_code = None
        self._data_disk_size = None
        self._cpu_rule_enable = None
        self._cpu_percent = None
        self._add_nodes_for_cpu_rule = None
        self._mem_rule_enable = None
        self._mem_percent = None
        self._add_nodes_for_mem_rule = None
        self.discriminator = None

        self.name = name
        self.availability_zone = availability_zone
        self.spec_code = spec_code
        self.max_nodes = max_nodes
        self.min_nodes = min_nodes
        if data_disk_spec_code is not None:
            self.data_disk_spec_code = data_disk_spec_code
        if data_disk_size is not None:
            self.data_disk_size = data_disk_size
        self.cpu_rule_enable = cpu_rule_enable
        self.cpu_percent = cpu_percent
        self.add_nodes_for_cpu_rule = add_nodes_for_cpu_rule
        self.mem_rule_enable = mem_rule_enable
        self.mem_percent = mem_percent
        self.add_nodes_for_mem_rule = add_nodes_for_mem_rule

    @property
    def name(self):
        r"""Gets the name of this CreateScaleOutPolicyReq.

        策略名称

        :return: The name of this CreateScaleOutPolicyReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateScaleOutPolicyReq.

        策略名称

        :param name: The name of this CreateScaleOutPolicyReq.
        :type name: str
        """
        self._name = name

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this CreateScaleOutPolicyReq.

        可用区

        :return: The availability_zone of this CreateScaleOutPolicyReq.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this CreateScaleOutPolicyReq.

        可用区

        :param availability_zone: The availability_zone of this CreateScaleOutPolicyReq.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def spec_code(self):
        r"""Gets the spec_code of this CreateScaleOutPolicyReq.

        规格编码

        :return: The spec_code of this CreateScaleOutPolicyReq.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this CreateScaleOutPolicyReq.

        规格编码

        :param spec_code: The spec_code of this CreateScaleOutPolicyReq.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def max_nodes(self):
        r"""Gets the max_nodes of this CreateScaleOutPolicyReq.

        扩容节点数上限

        :return: The max_nodes of this CreateScaleOutPolicyReq.
        :rtype: int
        """
        return self._max_nodes

    @max_nodes.setter
    def max_nodes(self, max_nodes):
        r"""Sets the max_nodes of this CreateScaleOutPolicyReq.

        扩容节点数上限

        :param max_nodes: The max_nodes of this CreateScaleOutPolicyReq.
        :type max_nodes: int
        """
        self._max_nodes = max_nodes

    @property
    def min_nodes(self):
        r"""Gets the min_nodes of this CreateScaleOutPolicyReq.

        扩容节点数下限

        :return: The min_nodes of this CreateScaleOutPolicyReq.
        :rtype: int
        """
        return self._min_nodes

    @min_nodes.setter
    def min_nodes(self, min_nodes):
        r"""Sets the min_nodes of this CreateScaleOutPolicyReq.

        扩容节点数下限

        :param min_nodes: The min_nodes of this CreateScaleOutPolicyReq.
        :type min_nodes: int
        """
        self._min_nodes = min_nodes

    @property
    def data_disk_spec_code(self):
        r"""Gets the data_disk_spec_code of this CreateScaleOutPolicyReq.

        额外数据盘规格编码

        :return: The data_disk_spec_code of this CreateScaleOutPolicyReq.
        :rtype: str
        """
        return self._data_disk_spec_code

    @data_disk_spec_code.setter
    def data_disk_spec_code(self, data_disk_spec_code):
        r"""Sets the data_disk_spec_code of this CreateScaleOutPolicyReq.

        额外数据盘规格编码

        :param data_disk_spec_code: The data_disk_spec_code of this CreateScaleOutPolicyReq.
        :type data_disk_spec_code: str
        """
        self._data_disk_spec_code = data_disk_spec_code

    @property
    def data_disk_size(self):
        r"""Gets the data_disk_size of this CreateScaleOutPolicyReq.

        额外数据盘大小

        :return: The data_disk_size of this CreateScaleOutPolicyReq.
        :rtype: int
        """
        return self._data_disk_size

    @data_disk_size.setter
    def data_disk_size(self, data_disk_size):
        r"""Sets the data_disk_size of this CreateScaleOutPolicyReq.

        额外数据盘大小

        :param data_disk_size: The data_disk_size of this CreateScaleOutPolicyReq.
        :type data_disk_size: int
        """
        self._data_disk_size = data_disk_size

    @property
    def cpu_rule_enable(self):
        r"""Gets the cpu_rule_enable of this CreateScaleOutPolicyReq.

        是否启用cpu规则

        :return: The cpu_rule_enable of this CreateScaleOutPolicyReq.
        :rtype: bool
        """
        return self._cpu_rule_enable

    @cpu_rule_enable.setter
    def cpu_rule_enable(self, cpu_rule_enable):
        r"""Sets the cpu_rule_enable of this CreateScaleOutPolicyReq.

        是否启用cpu规则

        :param cpu_rule_enable: The cpu_rule_enable of this CreateScaleOutPolicyReq.
        :type cpu_rule_enable: bool
        """
        self._cpu_rule_enable = cpu_rule_enable

    @property
    def cpu_percent(self):
        r"""Gets the cpu_percent of this CreateScaleOutPolicyReq.

        cpu分配率百分比

        :return: The cpu_percent of this CreateScaleOutPolicyReq.
        :rtype: int
        """
        return self._cpu_percent

    @cpu_percent.setter
    def cpu_percent(self, cpu_percent):
        r"""Sets the cpu_percent of this CreateScaleOutPolicyReq.

        cpu分配率百分比

        :param cpu_percent: The cpu_percent of this CreateScaleOutPolicyReq.
        :type cpu_percent: int
        """
        self._cpu_percent = cpu_percent

    @property
    def add_nodes_for_cpu_rule(self):
        r"""Gets the add_nodes_for_cpu_rule of this CreateScaleOutPolicyReq.

        满足扩容策略中cpu分配率时增加的节点数

        :return: The add_nodes_for_cpu_rule of this CreateScaleOutPolicyReq.
        :rtype: int
        """
        return self._add_nodes_for_cpu_rule

    @add_nodes_for_cpu_rule.setter
    def add_nodes_for_cpu_rule(self, add_nodes_for_cpu_rule):
        r"""Sets the add_nodes_for_cpu_rule of this CreateScaleOutPolicyReq.

        满足扩容策略中cpu分配率时增加的节点数

        :param add_nodes_for_cpu_rule: The add_nodes_for_cpu_rule of this CreateScaleOutPolicyReq.
        :type add_nodes_for_cpu_rule: int
        """
        self._add_nodes_for_cpu_rule = add_nodes_for_cpu_rule

    @property
    def mem_rule_enable(self):
        r"""Gets the mem_rule_enable of this CreateScaleOutPolicyReq.

        是否启用mem规则

        :return: The mem_rule_enable of this CreateScaleOutPolicyReq.
        :rtype: bool
        """
        return self._mem_rule_enable

    @mem_rule_enable.setter
    def mem_rule_enable(self, mem_rule_enable):
        r"""Sets the mem_rule_enable of this CreateScaleOutPolicyReq.

        是否启用mem规则

        :param mem_rule_enable: The mem_rule_enable of this CreateScaleOutPolicyReq.
        :type mem_rule_enable: bool
        """
        self._mem_rule_enable = mem_rule_enable

    @property
    def mem_percent(self):
        r"""Gets the mem_percent of this CreateScaleOutPolicyReq.

        mem分配率百分比

        :return: The mem_percent of this CreateScaleOutPolicyReq.
        :rtype: int
        """
        return self._mem_percent

    @mem_percent.setter
    def mem_percent(self, mem_percent):
        r"""Sets the mem_percent of this CreateScaleOutPolicyReq.

        mem分配率百分比

        :param mem_percent: The mem_percent of this CreateScaleOutPolicyReq.
        :type mem_percent: int
        """
        self._mem_percent = mem_percent

    @property
    def add_nodes_for_mem_rule(self):
        r"""Gets the add_nodes_for_mem_rule of this CreateScaleOutPolicyReq.

        满足扩容策略中mem分配率时增加的节点数

        :return: The add_nodes_for_mem_rule of this CreateScaleOutPolicyReq.
        :rtype: int
        """
        return self._add_nodes_for_mem_rule

    @add_nodes_for_mem_rule.setter
    def add_nodes_for_mem_rule(self, add_nodes_for_mem_rule):
        r"""Sets the add_nodes_for_mem_rule of this CreateScaleOutPolicyReq.

        满足扩容策略中mem分配率时增加的节点数

        :param add_nodes_for_mem_rule: The add_nodes_for_mem_rule of this CreateScaleOutPolicyReq.
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
        if not isinstance(other, CreateScaleOutPolicyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
