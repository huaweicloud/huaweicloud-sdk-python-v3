# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstancesMetricResult:

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
        'mode': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'solution': 'str',
        'disk_used_size': 'str',
        'disk_total_size': 'str',
        'disk_usage': 'str',
        'p80': 'str',
        'p95': 'str',
        'deadlocks': 'str',
        'buffer_hit_ratio': 'str',
        'nodes': 'list[InstancesNodesResult]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'mode': 'mode',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'solution': 'solution',
        'disk_used_size': 'disk_used_size',
        'disk_total_size': 'disk_total_size',
        'disk_usage': 'disk_usage',
        'p80': 'p80',
        'p95': 'p95',
        'deadlocks': 'deadlocks',
        'buffer_hit_ratio': 'buffer_hit_ratio',
        'nodes': 'nodes'
    }

    def __init__(self, id=None, name=None, status=None, mode=None, engine_name=None, engine_version=None, solution=None, disk_used_size=None, disk_total_size=None, disk_usage=None, p80=None, p95=None, deadlocks=None, buffer_hit_ratio=None, nodes=None):
        r"""InstancesMetricResult

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 实例ID。 **取值范围**： 不涉及。
        :type id: str
        :param name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type name: str
        :param status: **参数解释**： 实例状态。 **取值范围**： - creating，表示实例正在创建。 - normal，表示实例正常。 - abnormal，表示实例异常。 - createfail，表示实例创建失败。
        :type status: str
        :param mode: **参数解释**： 实例类型。 **取值范围**： 不涉及。
        :type mode: str
        :param engine_name: **参数解释**： 引擎名称。 **取值范围**： 不涉及。
        :type engine_name: str
        :param engine_version: **参数解释**： 引擎版本。 **取值范围**： 不涉及。
        :type engine_version: str
        :param solution: **参数解释**： 部署形态。 **取值范围**： 不涉及。
        :type solution: str
        :param disk_used_size: **参数解释**： 实例数据磁盘已使用大小。 **取值范围**： 不涉及。
        :type disk_used_size: str
        :param disk_total_size: **参数解释**： 实例数据磁盘总大小。 **取值范围**： 不涉及。
        :type disk_total_size: str
        :param disk_usage: **参数解释**： 实例数据磁盘已使用百分比。 **取值范围**： 不涉及。
        :type disk_usage: str
        :param p80: **参数解释**： 80% SQL的响应时间。 **取值范围**： 不涉及。
        :type p80: str
        :param p95: **参数解释**： 95% SQL的响应时间。 **取值范围**： 不涉及。
        :type p95: str
        :param deadlocks: **参数解释**： 死锁次数。 **取值范围**： 不涉及。
        :type deadlocks: str
        :param buffer_hit_ratio: **参数解释**： buffer 命中率。 **取值范围**： 不涉及。
        :type buffer_hit_ratio: str
        :param nodes: **参数解释**： 实例节点信息列表。
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstancesNodesResult`]
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._mode = None
        self._engine_name = None
        self._engine_version = None
        self._solution = None
        self._disk_used_size = None
        self._disk_total_size = None
        self._disk_usage = None
        self._p80 = None
        self._p95 = None
        self._deadlocks = None
        self._buffer_hit_ratio = None
        self._nodes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if mode is not None:
            self.mode = mode
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if solution is not None:
            self.solution = solution
        if disk_used_size is not None:
            self.disk_used_size = disk_used_size
        if disk_total_size is not None:
            self.disk_total_size = disk_total_size
        if disk_usage is not None:
            self.disk_usage = disk_usage
        if p80 is not None:
            self.p80 = p80
        if p95 is not None:
            self.p95 = p95
        if deadlocks is not None:
            self.deadlocks = deadlocks
        if buffer_hit_ratio is not None:
            self.buffer_hit_ratio = buffer_hit_ratio
        if nodes is not None:
            self.nodes = nodes

    @property
    def id(self):
        r"""Gets the id of this InstancesMetricResult.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :return: The id of this InstancesMetricResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstancesMetricResult.

        **参数解释**： 实例ID。 **取值范围**： 不涉及。

        :param id: The id of this InstancesMetricResult.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this InstancesMetricResult.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The name of this InstancesMetricResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstancesMetricResult.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param name: The name of this InstancesMetricResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this InstancesMetricResult.

        **参数解释**： 实例状态。 **取值范围**： - creating，表示实例正在创建。 - normal，表示实例正常。 - abnormal，表示实例异常。 - createfail，表示实例创建失败。

        :return: The status of this InstancesMetricResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstancesMetricResult.

        **参数解释**： 实例状态。 **取值范围**： - creating，表示实例正在创建。 - normal，表示实例正常。 - abnormal，表示实例异常。 - createfail，表示实例创建失败。

        :param status: The status of this InstancesMetricResult.
        :type status: str
        """
        self._status = status

    @property
    def mode(self):
        r"""Gets the mode of this InstancesMetricResult.

        **参数解释**： 实例类型。 **取值范围**： 不涉及。

        :return: The mode of this InstancesMetricResult.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this InstancesMetricResult.

        **参数解释**： 实例类型。 **取值范围**： 不涉及。

        :param mode: The mode of this InstancesMetricResult.
        :type mode: str
        """
        self._mode = mode

    @property
    def engine_name(self):
        r"""Gets the engine_name of this InstancesMetricResult.

        **参数解释**： 引擎名称。 **取值范围**： 不涉及。

        :return: The engine_name of this InstancesMetricResult.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this InstancesMetricResult.

        **参数解释**： 引擎名称。 **取值范围**： 不涉及。

        :param engine_name: The engine_name of this InstancesMetricResult.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this InstancesMetricResult.

        **参数解释**： 引擎版本。 **取值范围**： 不涉及。

        :return: The engine_version of this InstancesMetricResult.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this InstancesMetricResult.

        **参数解释**： 引擎版本。 **取值范围**： 不涉及。

        :param engine_version: The engine_version of this InstancesMetricResult.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def solution(self):
        r"""Gets the solution of this InstancesMetricResult.

        **参数解释**： 部署形态。 **取值范围**： 不涉及。

        :return: The solution of this InstancesMetricResult.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this InstancesMetricResult.

        **参数解释**： 部署形态。 **取值范围**： 不涉及。

        :param solution: The solution of this InstancesMetricResult.
        :type solution: str
        """
        self._solution = solution

    @property
    def disk_used_size(self):
        r"""Gets the disk_used_size of this InstancesMetricResult.

        **参数解释**： 实例数据磁盘已使用大小。 **取值范围**： 不涉及。

        :return: The disk_used_size of this InstancesMetricResult.
        :rtype: str
        """
        return self._disk_used_size

    @disk_used_size.setter
    def disk_used_size(self, disk_used_size):
        r"""Sets the disk_used_size of this InstancesMetricResult.

        **参数解释**： 实例数据磁盘已使用大小。 **取值范围**： 不涉及。

        :param disk_used_size: The disk_used_size of this InstancesMetricResult.
        :type disk_used_size: str
        """
        self._disk_used_size = disk_used_size

    @property
    def disk_total_size(self):
        r"""Gets the disk_total_size of this InstancesMetricResult.

        **参数解释**： 实例数据磁盘总大小。 **取值范围**： 不涉及。

        :return: The disk_total_size of this InstancesMetricResult.
        :rtype: str
        """
        return self._disk_total_size

    @disk_total_size.setter
    def disk_total_size(self, disk_total_size):
        r"""Sets the disk_total_size of this InstancesMetricResult.

        **参数解释**： 实例数据磁盘总大小。 **取值范围**： 不涉及。

        :param disk_total_size: The disk_total_size of this InstancesMetricResult.
        :type disk_total_size: str
        """
        self._disk_total_size = disk_total_size

    @property
    def disk_usage(self):
        r"""Gets the disk_usage of this InstancesMetricResult.

        **参数解释**： 实例数据磁盘已使用百分比。 **取值范围**： 不涉及。

        :return: The disk_usage of this InstancesMetricResult.
        :rtype: str
        """
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, disk_usage):
        r"""Sets the disk_usage of this InstancesMetricResult.

        **参数解释**： 实例数据磁盘已使用百分比。 **取值范围**： 不涉及。

        :param disk_usage: The disk_usage of this InstancesMetricResult.
        :type disk_usage: str
        """
        self._disk_usage = disk_usage

    @property
    def p80(self):
        r"""Gets the p80 of this InstancesMetricResult.

        **参数解释**： 80% SQL的响应时间。 **取值范围**： 不涉及。

        :return: The p80 of this InstancesMetricResult.
        :rtype: str
        """
        return self._p80

    @p80.setter
    def p80(self, p80):
        r"""Sets the p80 of this InstancesMetricResult.

        **参数解释**： 80% SQL的响应时间。 **取值范围**： 不涉及。

        :param p80: The p80 of this InstancesMetricResult.
        :type p80: str
        """
        self._p80 = p80

    @property
    def p95(self):
        r"""Gets the p95 of this InstancesMetricResult.

        **参数解释**： 95% SQL的响应时间。 **取值范围**： 不涉及。

        :return: The p95 of this InstancesMetricResult.
        :rtype: str
        """
        return self._p95

    @p95.setter
    def p95(self, p95):
        r"""Sets the p95 of this InstancesMetricResult.

        **参数解释**： 95% SQL的响应时间。 **取值范围**： 不涉及。

        :param p95: The p95 of this InstancesMetricResult.
        :type p95: str
        """
        self._p95 = p95

    @property
    def deadlocks(self):
        r"""Gets the deadlocks of this InstancesMetricResult.

        **参数解释**： 死锁次数。 **取值范围**： 不涉及。

        :return: The deadlocks of this InstancesMetricResult.
        :rtype: str
        """
        return self._deadlocks

    @deadlocks.setter
    def deadlocks(self, deadlocks):
        r"""Sets the deadlocks of this InstancesMetricResult.

        **参数解释**： 死锁次数。 **取值范围**： 不涉及。

        :param deadlocks: The deadlocks of this InstancesMetricResult.
        :type deadlocks: str
        """
        self._deadlocks = deadlocks

    @property
    def buffer_hit_ratio(self):
        r"""Gets the buffer_hit_ratio of this InstancesMetricResult.

        **参数解释**： buffer 命中率。 **取值范围**： 不涉及。

        :return: The buffer_hit_ratio of this InstancesMetricResult.
        :rtype: str
        """
        return self._buffer_hit_ratio

    @buffer_hit_ratio.setter
    def buffer_hit_ratio(self, buffer_hit_ratio):
        r"""Sets the buffer_hit_ratio of this InstancesMetricResult.

        **参数解释**： buffer 命中率。 **取值范围**： 不涉及。

        :param buffer_hit_ratio: The buffer_hit_ratio of this InstancesMetricResult.
        :type buffer_hit_ratio: str
        """
        self._buffer_hit_ratio = buffer_hit_ratio

    @property
    def nodes(self):
        r"""Gets the nodes of this InstancesMetricResult.

        **参数解释**： 实例节点信息列表。

        :return: The nodes of this InstancesMetricResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstancesNodesResult`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this InstancesMetricResult.

        **参数解释**： 实例节点信息列表。

        :param nodes: The nodes of this InstancesMetricResult.
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.InstancesNodesResult`]
        """
        self._nodes = nodes

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
        if not isinstance(other, InstancesMetricResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
