# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSessionsRequest:

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
        'offset': 'int',
        'limit': 'int',
        'plan_summary': 'str',
        'type': 'str',
        'namespace': 'str',
        'cost_time': 'int'
    }

    attribute_map = {
        'node_id': 'node_id',
        'offset': 'offset',
        'limit': 'limit',
        'plan_summary': 'plan_summary',
        'type': 'type',
        'namespace': 'namespace',
        'cost_time': 'cost_time'
    }

    def __init__(self, node_id=None, offset=None, limit=None, plan_summary=None, type=None, namespace=None, cost_time=None):
        """ListSessionsRequest

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。允许查询的节点如下： 集群下面的 mongos节点以及 副本集、单节点实例下面的所有节点。
        :type node_id: str
        :param offset: 索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。取值范围[1, 20]，默认10 （表示返回10条数据）。
        :type limit: int
        :param plan_summary: 执行计划描述。取空值表示查询所有语句类型，也可指定执行计划，例如： COLLSCAN IXSCAN FETCH SORT LIMIT SKIP COUNT COUNT_SCAN TEXT PROJECTION 等
        :type plan_summary: str
        :param type: 操作类型。取空值表示查询所有操作类型。也可指定操作类型，例如： none update insert query command getmore remove killcursors等
        :type type: str
        :param namespace: 命名空间。取空值表示查询所有命名空间。也可根据当前业务进行指定。
        :type namespace: str
        :param cost_time: 运行时间，单位为 ms。取空值表示查询所有的运行时间。也可根据当前业务需要进行配置，表示查询超出 cost_time 的会话。
        :type cost_time: int
        """
        
        

        self._node_id = None
        self._offset = None
        self._limit = None
        self._plan_summary = None
        self._type = None
        self._namespace = None
        self._cost_time = None
        self.discriminator = None

        self.node_id = node_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if plan_summary is not None:
            self.plan_summary = plan_summary
        if type is not None:
            self.type = type
        if namespace is not None:
            self.namespace = namespace
        if cost_time is not None:
            self.cost_time = cost_time

    @property
    def node_id(self):
        """Gets the node_id of this ListSessionsRequest.

        节点ID。允许查询的节点如下： 集群下面的 mongos节点以及 副本集、单节点实例下面的所有节点。

        :return: The node_id of this ListSessionsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListSessionsRequest.

        节点ID。允许查询的节点如下： 集群下面的 mongos节点以及 副本集、单节点实例下面的所有节点。

        :param node_id: The node_id of this ListSessionsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def offset(self):
        """Gets the offset of this ListSessionsRequest.

        索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListSessionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSessionsRequest.

        索引位置，偏移量。 从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListSessionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSessionsRequest.

        查询记录数。取值范围[1, 20]，默认10 （表示返回10条数据）。

        :return: The limit of this ListSessionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSessionsRequest.

        查询记录数。取值范围[1, 20]，默认10 （表示返回10条数据）。

        :param limit: The limit of this ListSessionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def plan_summary(self):
        """Gets the plan_summary of this ListSessionsRequest.

        执行计划描述。取空值表示查询所有语句类型，也可指定执行计划，例如： COLLSCAN IXSCAN FETCH SORT LIMIT SKIP COUNT COUNT_SCAN TEXT PROJECTION 等

        :return: The plan_summary of this ListSessionsRequest.
        :rtype: str
        """
        return self._plan_summary

    @plan_summary.setter
    def plan_summary(self, plan_summary):
        """Sets the plan_summary of this ListSessionsRequest.

        执行计划描述。取空值表示查询所有语句类型，也可指定执行计划，例如： COLLSCAN IXSCAN FETCH SORT LIMIT SKIP COUNT COUNT_SCAN TEXT PROJECTION 等

        :param plan_summary: The plan_summary of this ListSessionsRequest.
        :type plan_summary: str
        """
        self._plan_summary = plan_summary

    @property
    def type(self):
        """Gets the type of this ListSessionsRequest.

        操作类型。取空值表示查询所有操作类型。也可指定操作类型，例如： none update insert query command getmore remove killcursors等

        :return: The type of this ListSessionsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListSessionsRequest.

        操作类型。取空值表示查询所有操作类型。也可指定操作类型，例如： none update insert query command getmore remove killcursors等

        :param type: The type of this ListSessionsRequest.
        :type type: str
        """
        self._type = type

    @property
    def namespace(self):
        """Gets the namespace of this ListSessionsRequest.

        命名空间。取空值表示查询所有命名空间。也可根据当前业务进行指定。

        :return: The namespace of this ListSessionsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListSessionsRequest.

        命名空间。取空值表示查询所有命名空间。也可根据当前业务进行指定。

        :param namespace: The namespace of this ListSessionsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def cost_time(self):
        """Gets the cost_time of this ListSessionsRequest.

        运行时间，单位为 ms。取空值表示查询所有的运行时间。也可根据当前业务需要进行配置，表示查询超出 cost_time 的会话。

        :return: The cost_time of this ListSessionsRequest.
        :rtype: int
        """
        return self._cost_time

    @cost_time.setter
    def cost_time(self, cost_time):
        """Sets the cost_time of this ListSessionsRequest.

        运行时间，单位为 ms。取空值表示查询所有的运行时间。也可根据当前业务需要进行配置，表示查询超出 cost_time 的会话。

        :param cost_time: The cost_time of this ListSessionsRequest.
        :type cost_time: int
        """
        self._cost_time = cost_time

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
        if not isinstance(other, ListSessionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
