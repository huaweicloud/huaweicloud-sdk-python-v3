# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKillOpRuleRuleListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'operation_types': 'str',
        'namespaces': 'str',
        'status': 'str',
        'plan_summary': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'operation_types': 'operation_types',
        'namespaces': 'namespaces',
        'status': 'status',
        'plan_summary': 'plan_summary',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, operation_types=None, namespaces=None, status=None, plan_summary=None, offset=None, limit=None):
        r"""ShowKillOpRuleRuleListRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“[查询实例列表和详情](x-wc://file&#x3D;zh-cn_topic_0000001369935045.xml)”接口获取。如果未申请实例，可以调用“[创建实例](x-wc://file&#x3D;zh-cn_topic_0000001369734929.xml)”接口创建。
        :type instance_id: str
        :param operation_types: Sql语句操作类型。  - insert，表示插入语句。  - update，表示更新语句。  - query，表示查询语句。  - command，表示命令语句。  - remove，表示删除语句。  - getmore，表示获取更多数据语句。
        :type operation_types: str
        :param namespaces: 表命名空间。取值格式：库名.表名。 - 可为空，表示不做限制。 - 单独库名，表示对某个库下的所有集合生效。 - 库名.表名，表示对具体库下的具体的集合生效。
        :type namespaces: str
        :param status: killOp规则状态。  - ENABLED，规则生效中。 - DISABLED，规则禁用中。
        :type status: str
        :param plan_summary: 执行计划。 默认值空，表示不做限制。  - COLLSCAN。 - SORT_KEY_GENERATOR。 - SKIP。 - LIMIT。 - GEO_NEAR_2DSPHERE。 - GEO_NEAR_2D。 - AGGREGATE。 - OR。
        :type plan_summary: str
        :param offset: 索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._operation_types = None
        self._namespaces = None
        self._status = None
        self._plan_summary = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if operation_types is not None:
            self.operation_types = operation_types
        if namespaces is not None:
            self.namespaces = namespaces
        if status is not None:
            self.status = status
        if plan_summary is not None:
            self.plan_summary = plan_summary
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKillOpRuleRuleListRequest.

        实例ID，可以调用“[查询实例列表和详情](x-wc://file=zh-cn_topic_0000001369935045.xml)”接口获取。如果未申请实例，可以调用“[创建实例](x-wc://file=zh-cn_topic_0000001369734929.xml)”接口创建。

        :return: The instance_id of this ShowKillOpRuleRuleListRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKillOpRuleRuleListRequest.

        实例ID，可以调用“[查询实例列表和详情](x-wc://file=zh-cn_topic_0000001369935045.xml)”接口获取。如果未申请实例，可以调用“[创建实例](x-wc://file=zh-cn_topic_0000001369734929.xml)”接口创建。

        :param instance_id: The instance_id of this ShowKillOpRuleRuleListRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def operation_types(self):
        r"""Gets the operation_types of this ShowKillOpRuleRuleListRequest.

        Sql语句操作类型。  - insert，表示插入语句。  - update，表示更新语句。  - query，表示查询语句。  - command，表示命令语句。  - remove，表示删除语句。  - getmore，表示获取更多数据语句。

        :return: The operation_types of this ShowKillOpRuleRuleListRequest.
        :rtype: str
        """
        return self._operation_types

    @operation_types.setter
    def operation_types(self, operation_types):
        r"""Sets the operation_types of this ShowKillOpRuleRuleListRequest.

        Sql语句操作类型。  - insert，表示插入语句。  - update，表示更新语句。  - query，表示查询语句。  - command，表示命令语句。  - remove，表示删除语句。  - getmore，表示获取更多数据语句。

        :param operation_types: The operation_types of this ShowKillOpRuleRuleListRequest.
        :type operation_types: str
        """
        self._operation_types = operation_types

    @property
    def namespaces(self):
        r"""Gets the namespaces of this ShowKillOpRuleRuleListRequest.

        表命名空间。取值格式：库名.表名。 - 可为空，表示不做限制。 - 单独库名，表示对某个库下的所有集合生效。 - 库名.表名，表示对具体库下的具体的集合生效。

        :return: The namespaces of this ShowKillOpRuleRuleListRequest.
        :rtype: str
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this ShowKillOpRuleRuleListRequest.

        表命名空间。取值格式：库名.表名。 - 可为空，表示不做限制。 - 单独库名，表示对某个库下的所有集合生效。 - 库名.表名，表示对具体库下的具体的集合生效。

        :param namespaces: The namespaces of this ShowKillOpRuleRuleListRequest.
        :type namespaces: str
        """
        self._namespaces = namespaces

    @property
    def status(self):
        r"""Gets the status of this ShowKillOpRuleRuleListRequest.

        killOp规则状态。  - ENABLED，规则生效中。 - DISABLED，规则禁用中。

        :return: The status of this ShowKillOpRuleRuleListRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowKillOpRuleRuleListRequest.

        killOp规则状态。  - ENABLED，规则生效中。 - DISABLED，规则禁用中。

        :param status: The status of this ShowKillOpRuleRuleListRequest.
        :type status: str
        """
        self._status = status

    @property
    def plan_summary(self):
        r"""Gets the plan_summary of this ShowKillOpRuleRuleListRequest.

        执行计划。 默认值空，表示不做限制。  - COLLSCAN。 - SORT_KEY_GENERATOR。 - SKIP。 - LIMIT。 - GEO_NEAR_2DSPHERE。 - GEO_NEAR_2D。 - AGGREGATE。 - OR。

        :return: The plan_summary of this ShowKillOpRuleRuleListRequest.
        :rtype: str
        """
        return self._plan_summary

    @plan_summary.setter
    def plan_summary(self, plan_summary):
        r"""Sets the plan_summary of this ShowKillOpRuleRuleListRequest.

        执行计划。 默认值空，表示不做限制。  - COLLSCAN。 - SORT_KEY_GENERATOR。 - SKIP。 - LIMIT。 - GEO_NEAR_2DSPHERE。 - GEO_NEAR_2D。 - AGGREGATE。 - OR。

        :param plan_summary: The plan_summary of this ShowKillOpRuleRuleListRequest.
        :type plan_summary: str
        """
        self._plan_summary = plan_summary

    @property
    def offset(self):
        r"""Gets the offset of this ShowKillOpRuleRuleListRequest.

        索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。

        :return: The offset of this ShowKillOpRuleRuleListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowKillOpRuleRuleListRequest.

        索引位置，偏移量。  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）。 取值必须为数字，不能为负数。

        :param offset: The offset of this ShowKillOpRuleRuleListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowKillOpRuleRuleListRequest.

        查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。

        :return: The limit of this ShowKillOpRuleRuleListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowKillOpRuleRuleListRequest.

        查询个数上限值。 - 取值范围: 1~100。 - 不传该参数时，默认查询前100条信息。

        :param limit: The limit of this ShowKillOpRuleRuleListRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowKillOpRuleRuleListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
