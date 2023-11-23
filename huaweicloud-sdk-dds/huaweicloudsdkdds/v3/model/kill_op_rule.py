# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KillOpRule:

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
        'operation_types': 'str',
        'status': 'str',
        'namespaces': 'str',
        'client_ips': 'str',
        'plan_summary': 'str',
        'max_concurrency': 'int',
        'secs_running': 'int',
        'node_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'operation_types': 'operation_types',
        'status': 'status',
        'namespaces': 'namespaces',
        'client_ips': 'client_ips',
        'plan_summary': 'plan_summary',
        'max_concurrency': 'max_concurrency',
        'secs_running': 'secs_running',
        'node_type': 'node_type'
    }

    def __init__(self, id=None, operation_types=None, status=None, namespaces=None, client_ips=None, plan_summary=None, max_concurrency=None, secs_running=None, node_type=None):
        """KillOpRule

        The model defined in huaweicloud sdk

        :param id: killOp规则ID。
        :type id: str
        :param operation_types: Sql语句操作类型。 最多支持同时选择6种语句类型。同时选择多种类型时，匹配任意一种类型时规则生效。 - insert，表示插入语句。  - update，表示更新语句。  - query，表示查询语句。  - command，表示命令语句。  - remove，表示删除语句。  - getmore，表示获取更多数据语句。
        :type operation_types: str
        :param status: killOp规则状态。  - ENABLED，规则生效中。 - DISABLED，规则禁用中。
        :type status: str
        :param namespaces: 表命名空间。取值格式：库名.表名。同时配置多组信息时，匹配任意一组信息时规则生效 - 目前仅支持配置一组信息 - 可为空，表示不做限制。 - 单独库名，表示对某个库下的所有集合生效。 - 库名.表名，表示对具体库下的具体的集合生效。
        :type namespaces: str
        :param client_ips: 客户端连接IP。只支持IPV4。可为空，表示不做限制。最多支持配置5个IP。同时配置多个IP时，匹配任意一个IP时规则生效。
        :type client_ips: str
        :param plan_summary: 执行计划。 默认值空，表示不做限制。  - COLLSCAN。 - SORT_KEY_GENERATOR。 - SKIP。 - LIMIT。 - GEO_NEAR_2DSPHERE。 - GEO_NEAR_2D。 - AGGREGATE。 - OR。
        :type plan_summary: str
        :param max_concurrency: 最大并发数。 取值： 不能为负数，可为空，默认为0，表示不做限制， 最小值为1， 最大值为100000。secs_running和max_concurrency不可同时为0。
        :type max_concurrency: int
        :param secs_running: 单条操作最大运行时长。取值： 不能为负数，可为空，默认为0，表示不做限制。单位：s。最小值为2， 最大值为86400。secs_running和max_concurrency不可同时为0。
        :type secs_running: int
        :param node_type: 节点类型。  - mongos_shard，表示同时在mongos和shard节点生效。 - mongos，表示只在集群mongos节点生效。 - shard，表示只在集群shard节点生效。 - replica，表示只在副本集节点生效。
        :type node_type: str
        """
        
        

        self._id = None
        self._operation_types = None
        self._status = None
        self._namespaces = None
        self._client_ips = None
        self._plan_summary = None
        self._max_concurrency = None
        self._secs_running = None
        self._node_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if operation_types is not None:
            self.operation_types = operation_types
        if status is not None:
            self.status = status
        if namespaces is not None:
            self.namespaces = namespaces
        if client_ips is not None:
            self.client_ips = client_ips
        if plan_summary is not None:
            self.plan_summary = plan_summary
        if max_concurrency is not None:
            self.max_concurrency = max_concurrency
        if secs_running is not None:
            self.secs_running = secs_running
        if node_type is not None:
            self.node_type = node_type

    @property
    def id(self):
        """Gets the id of this KillOpRule.

        killOp规则ID。

        :return: The id of this KillOpRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KillOpRule.

        killOp规则ID。

        :param id: The id of this KillOpRule.
        :type id: str
        """
        self._id = id

    @property
    def operation_types(self):
        """Gets the operation_types of this KillOpRule.

        Sql语句操作类型。 最多支持同时选择6种语句类型。同时选择多种类型时，匹配任意一种类型时规则生效。 - insert，表示插入语句。  - update，表示更新语句。  - query，表示查询语句。  - command，表示命令语句。  - remove，表示删除语句。  - getmore，表示获取更多数据语句。

        :return: The operation_types of this KillOpRule.
        :rtype: str
        """
        return self._operation_types

    @operation_types.setter
    def operation_types(self, operation_types):
        """Sets the operation_types of this KillOpRule.

        Sql语句操作类型。 最多支持同时选择6种语句类型。同时选择多种类型时，匹配任意一种类型时规则生效。 - insert，表示插入语句。  - update，表示更新语句。  - query，表示查询语句。  - command，表示命令语句。  - remove，表示删除语句。  - getmore，表示获取更多数据语句。

        :param operation_types: The operation_types of this KillOpRule.
        :type operation_types: str
        """
        self._operation_types = operation_types

    @property
    def status(self):
        """Gets the status of this KillOpRule.

        killOp规则状态。  - ENABLED，规则生效中。 - DISABLED，规则禁用中。

        :return: The status of this KillOpRule.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this KillOpRule.

        killOp规则状态。  - ENABLED，规则生效中。 - DISABLED，规则禁用中。

        :param status: The status of this KillOpRule.
        :type status: str
        """
        self._status = status

    @property
    def namespaces(self):
        """Gets the namespaces of this KillOpRule.

        表命名空间。取值格式：库名.表名。同时配置多组信息时，匹配任意一组信息时规则生效 - 目前仅支持配置一组信息 - 可为空，表示不做限制。 - 单独库名，表示对某个库下的所有集合生效。 - 库名.表名，表示对具体库下的具体的集合生效。

        :return: The namespaces of this KillOpRule.
        :rtype: str
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this KillOpRule.

        表命名空间。取值格式：库名.表名。同时配置多组信息时，匹配任意一组信息时规则生效 - 目前仅支持配置一组信息 - 可为空，表示不做限制。 - 单独库名，表示对某个库下的所有集合生效。 - 库名.表名，表示对具体库下的具体的集合生效。

        :param namespaces: The namespaces of this KillOpRule.
        :type namespaces: str
        """
        self._namespaces = namespaces

    @property
    def client_ips(self):
        """Gets the client_ips of this KillOpRule.

        客户端连接IP。只支持IPV4。可为空，表示不做限制。最多支持配置5个IP。同时配置多个IP时，匹配任意一个IP时规则生效。

        :return: The client_ips of this KillOpRule.
        :rtype: str
        """
        return self._client_ips

    @client_ips.setter
    def client_ips(self, client_ips):
        """Sets the client_ips of this KillOpRule.

        客户端连接IP。只支持IPV4。可为空，表示不做限制。最多支持配置5个IP。同时配置多个IP时，匹配任意一个IP时规则生效。

        :param client_ips: The client_ips of this KillOpRule.
        :type client_ips: str
        """
        self._client_ips = client_ips

    @property
    def plan_summary(self):
        """Gets the plan_summary of this KillOpRule.

        执行计划。 默认值空，表示不做限制。  - COLLSCAN。 - SORT_KEY_GENERATOR。 - SKIP。 - LIMIT。 - GEO_NEAR_2DSPHERE。 - GEO_NEAR_2D。 - AGGREGATE。 - OR。

        :return: The plan_summary of this KillOpRule.
        :rtype: str
        """
        return self._plan_summary

    @plan_summary.setter
    def plan_summary(self, plan_summary):
        """Sets the plan_summary of this KillOpRule.

        执行计划。 默认值空，表示不做限制。  - COLLSCAN。 - SORT_KEY_GENERATOR。 - SKIP。 - LIMIT。 - GEO_NEAR_2DSPHERE。 - GEO_NEAR_2D。 - AGGREGATE。 - OR。

        :param plan_summary: The plan_summary of this KillOpRule.
        :type plan_summary: str
        """
        self._plan_summary = plan_summary

    @property
    def max_concurrency(self):
        """Gets the max_concurrency of this KillOpRule.

        最大并发数。 取值： 不能为负数，可为空，默认为0，表示不做限制， 最小值为1， 最大值为100000。secs_running和max_concurrency不可同时为0。

        :return: The max_concurrency of this KillOpRule.
        :rtype: int
        """
        return self._max_concurrency

    @max_concurrency.setter
    def max_concurrency(self, max_concurrency):
        """Sets the max_concurrency of this KillOpRule.

        最大并发数。 取值： 不能为负数，可为空，默认为0，表示不做限制， 最小值为1， 最大值为100000。secs_running和max_concurrency不可同时为0。

        :param max_concurrency: The max_concurrency of this KillOpRule.
        :type max_concurrency: int
        """
        self._max_concurrency = max_concurrency

    @property
    def secs_running(self):
        """Gets the secs_running of this KillOpRule.

        单条操作最大运行时长。取值： 不能为负数，可为空，默认为0，表示不做限制。单位：s。最小值为2， 最大值为86400。secs_running和max_concurrency不可同时为0。

        :return: The secs_running of this KillOpRule.
        :rtype: int
        """
        return self._secs_running

    @secs_running.setter
    def secs_running(self, secs_running):
        """Sets the secs_running of this KillOpRule.

        单条操作最大运行时长。取值： 不能为负数，可为空，默认为0，表示不做限制。单位：s。最小值为2， 最大值为86400。secs_running和max_concurrency不可同时为0。

        :param secs_running: The secs_running of this KillOpRule.
        :type secs_running: int
        """
        self._secs_running = secs_running

    @property
    def node_type(self):
        """Gets the node_type of this KillOpRule.

        节点类型。  - mongos_shard，表示同时在mongos和shard节点生效。 - mongos，表示只在集群mongos节点生效。 - shard，表示只在集群shard节点生效。 - replica，表示只在副本集节点生效。

        :return: The node_type of this KillOpRule.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this KillOpRule.

        节点类型。  - mongos_shard，表示同时在mongos和shard节点生效。 - mongos，表示只在集群mongos节点生效。 - shard，表示只在集群shard节点生效。 - replica，表示只在副本集节点生效。

        :param node_type: The node_type of this KillOpRule.
        :type node_type: str
        """
        self._node_type = node_type

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
        if not isinstance(other, KillOpRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
