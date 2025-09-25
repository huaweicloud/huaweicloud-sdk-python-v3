# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLimitTaskResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_scope': 'str',
        'limit_type': 'str',
        'limit_type_value': 'str',
        'task_name': 'str',
        'databases': 'str',
        'sql_model': 'str',
        'key_words': 'str',
        'status': 'str',
        'instance_id': 'str',
        'rule_name': 'str',
        'parallel_size': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'cpu_utilization': 'int',
        'memory_utilization': 'int',
        'created': 'str',
        'updated': 'str',
        'creator': 'str',
        'modifier': 'str',
        'node_infos': 'list[ShowLimitTaskNodeOption]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_scope': 'task_scope',
        'limit_type': 'limit_type',
        'limit_type_value': 'limit_type_value',
        'task_name': 'task_name',
        'databases': 'databases',
        'sql_model': 'sql_model',
        'key_words': 'key_words',
        'status': 'status',
        'instance_id': 'instance_id',
        'rule_name': 'rule_name',
        'parallel_size': 'parallel_size',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'cpu_utilization': 'cpu_utilization',
        'memory_utilization': 'memory_utilization',
        'created': 'created',
        'updated': 'updated',
        'creator': 'creator',
        'modifier': 'modifier',
        'node_infos': 'node_infos'
    }

    def __init__(self, task_id=None, task_scope=None, limit_type=None, limit_type_value=None, task_name=None, databases=None, sql_model=None, key_words=None, status=None, instance_id=None, rule_name=None, parallel_size=None, start_time=None, end_time=None, cpu_utilization=None, memory_utilization=None, created=None, updated=None, creator=None, modifier=None, node_infos=None):
        r"""ListLimitTaskResponseResult

        The model defined in huaweicloud sdk

        :param task_id: **参数解释**: 限流任务ID。 **取值范围**: 不涉及。
        :type task_id: str
        :param task_scope: **参数解释**: 任务限流范围。 **取值范围**: 目前支持SQL，SESSION两种级别范围。
        :type task_scope: str
        :param limit_type: **参数解释**: 任务限流类型。 **取值范围**: - 当“task_scope”为SQL时，可选SQL_ID、SQL_TYPE类型。 - 当“task_scope”为SESSION时，可选SESSION_ACTIVE_MAX_COUNT类型。
        :type limit_type: str
        :param limit_type_value: **参数解释**: 任务限流类型值。 **取值范围**: - 当“limit_type”为SQL_ID类型时，该值为选中模板的sql_id。 - 当“limit_type”为SQL_TYPE类型时，值为SQL类型，为select，update，insert，delete，merge的一种。 - 当“limit_type”为SESSION_ACTIVE_MAX_COUNT类型时，该值为CPU_OR_MEMORY。
        :type limit_type_value: str
        :param task_name: **参数解释**: 限流任务名。 **取值范围**: 不涉及。
        :type task_name: str
        :param databases: **参数解释**: 实例的数据库列表，每个数据库以英文逗号形式隔开。 **取值范围**: 不涉及。
        :type databases: str
        :param sql_model: **参数解释**: SQL模板，仅当任务类型为SQL_ID时，返回该值。 **取值范围**: 不涉及。
        :type sql_model: str
        :param key_words: **参数解释**: 关键词，仅当任务类型为SQL_TYPE时，返回该值。 **取值范围**: 不涉及。
        :type key_words: str
        :param status: **参数解释**: 限流任务状态。 **取值范围**: 当前支持：CREATING，UPDATING，DELETING，WAIT_EXECUTE，EXCUTING，TIME_OVER，DELETED，CREATE_FAILED，UPDATE_FAILED，DELETE_FAILED，EXCEPTION，NODE_SHUT_DOWN。
        :type status: str
        :param instance_id: **参数解释**: 实例ID。 **取值范围**: 不涉及。
        :type instance_id: str
        :param rule_name: **参数解释**: 规则名。 **取值范围**: 不涉及。
        :type rule_name: str
        :param parallel_size: **参数解释**: 并发数。 **取值范围**: [0, 2147483647]
        :type parallel_size: int
        :param start_time: **参数解释**: 限流任务开始时间。 **取值范围**: 不涉及。
        :type start_time: str
        :param end_time: **参数解释**: 限流任务结束时间。 **取值范围**: 不涉及。
        :type end_time: str
        :param cpu_utilization: **参数解释**: CPU利用率阈值，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留整数部分。 **取值范围**: [0, 100)
        :type cpu_utilization: int
        :param memory_utilization: **参数解释**: 内存利用率阈值，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留整数部分。 **取值范围**: [0, 100)
        :type memory_utilization: int
        :param created: **参数解释**: 限流任务创建时间。 **取值范围**: 不涉及。
        :type created: str
        :param updated: **参数解释**: 限流任务更新时间。 **取值范围**: 不涉及。
        :type updated: str
        :param creator: **参数解释**: 创建者。 **取值范围**: 不涉及。
        :type creator: str
        :param modifier: **参数解释**: 更新者。 **取值范围**: 不涉及。
        :type modifier: str
        :param node_infos: **参数解释**: CN节点信息列表。
        :type node_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ShowLimitTaskNodeOption`]
        """
        
        

        self._task_id = None
        self._task_scope = None
        self._limit_type = None
        self._limit_type_value = None
        self._task_name = None
        self._databases = None
        self._sql_model = None
        self._key_words = None
        self._status = None
        self._instance_id = None
        self._rule_name = None
        self._parallel_size = None
        self._start_time = None
        self._end_time = None
        self._cpu_utilization = None
        self._memory_utilization = None
        self._created = None
        self._updated = None
        self._creator = None
        self._modifier = None
        self._node_infos = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_scope is not None:
            self.task_scope = task_scope
        if limit_type is not None:
            self.limit_type = limit_type
        if limit_type_value is not None:
            self.limit_type_value = limit_type_value
        if task_name is not None:
            self.task_name = task_name
        if databases is not None:
            self.databases = databases
        if sql_model is not None:
            self.sql_model = sql_model
        if key_words is not None:
            self.key_words = key_words
        if status is not None:
            self.status = status
        if instance_id is not None:
            self.instance_id = instance_id
        if rule_name is not None:
            self.rule_name = rule_name
        if parallel_size is not None:
            self.parallel_size = parallel_size
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if cpu_utilization is not None:
            self.cpu_utilization = cpu_utilization
        if memory_utilization is not None:
            self.memory_utilization = memory_utilization
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if creator is not None:
            self.creator = creator
        if modifier is not None:
            self.modifier = modifier
        if node_infos is not None:
            self.node_infos = node_infos

    @property
    def task_id(self):
        r"""Gets the task_id of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务ID。 **取值范围**: 不涉及。

        :return: The task_id of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务ID。 **取值范围**: 不涉及。

        :param task_id: The task_id of this ListLimitTaskResponseResult.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_scope(self):
        r"""Gets the task_scope of this ListLimitTaskResponseResult.

        **参数解释**: 任务限流范围。 **取值范围**: 目前支持SQL，SESSION两种级别范围。

        :return: The task_scope of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._task_scope

    @task_scope.setter
    def task_scope(self, task_scope):
        r"""Sets the task_scope of this ListLimitTaskResponseResult.

        **参数解释**: 任务限流范围。 **取值范围**: 目前支持SQL，SESSION两种级别范围。

        :param task_scope: The task_scope of this ListLimitTaskResponseResult.
        :type task_scope: str
        """
        self._task_scope = task_scope

    @property
    def limit_type(self):
        r"""Gets the limit_type of this ListLimitTaskResponseResult.

        **参数解释**: 任务限流类型。 **取值范围**: - 当“task_scope”为SQL时，可选SQL_ID、SQL_TYPE类型。 - 当“task_scope”为SESSION时，可选SESSION_ACTIVE_MAX_COUNT类型。

        :return: The limit_type of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        r"""Sets the limit_type of this ListLimitTaskResponseResult.

        **参数解释**: 任务限流类型。 **取值范围**: - 当“task_scope”为SQL时，可选SQL_ID、SQL_TYPE类型。 - 当“task_scope”为SESSION时，可选SESSION_ACTIVE_MAX_COUNT类型。

        :param limit_type: The limit_type of this ListLimitTaskResponseResult.
        :type limit_type: str
        """
        self._limit_type = limit_type

    @property
    def limit_type_value(self):
        r"""Gets the limit_type_value of this ListLimitTaskResponseResult.

        **参数解释**: 任务限流类型值。 **取值范围**: - 当“limit_type”为SQL_ID类型时，该值为选中模板的sql_id。 - 当“limit_type”为SQL_TYPE类型时，值为SQL类型，为select，update，insert，delete，merge的一种。 - 当“limit_type”为SESSION_ACTIVE_MAX_COUNT类型时，该值为CPU_OR_MEMORY。

        :return: The limit_type_value of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._limit_type_value

    @limit_type_value.setter
    def limit_type_value(self, limit_type_value):
        r"""Sets the limit_type_value of this ListLimitTaskResponseResult.

        **参数解释**: 任务限流类型值。 **取值范围**: - 当“limit_type”为SQL_ID类型时，该值为选中模板的sql_id。 - 当“limit_type”为SQL_TYPE类型时，值为SQL类型，为select，update，insert，delete，merge的一种。 - 当“limit_type”为SESSION_ACTIVE_MAX_COUNT类型时，该值为CPU_OR_MEMORY。

        :param limit_type_value: The limit_type_value of this ListLimitTaskResponseResult.
        :type limit_type_value: str
        """
        self._limit_type_value = limit_type_value

    @property
    def task_name(self):
        r"""Gets the task_name of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务名。 **取值范围**: 不涉及。

        :return: The task_name of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务名。 **取值范围**: 不涉及。

        :param task_name: The task_name of this ListLimitTaskResponseResult.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def databases(self):
        r"""Gets the databases of this ListLimitTaskResponseResult.

        **参数解释**: 实例的数据库列表，每个数据库以英文逗号形式隔开。 **取值范围**: 不涉及。

        :return: The databases of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this ListLimitTaskResponseResult.

        **参数解释**: 实例的数据库列表，每个数据库以英文逗号形式隔开。 **取值范围**: 不涉及。

        :param databases: The databases of this ListLimitTaskResponseResult.
        :type databases: str
        """
        self._databases = databases

    @property
    def sql_model(self):
        r"""Gets the sql_model of this ListLimitTaskResponseResult.

        **参数解释**: SQL模板，仅当任务类型为SQL_ID时，返回该值。 **取值范围**: 不涉及。

        :return: The sql_model of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._sql_model

    @sql_model.setter
    def sql_model(self, sql_model):
        r"""Sets the sql_model of this ListLimitTaskResponseResult.

        **参数解释**: SQL模板，仅当任务类型为SQL_ID时，返回该值。 **取值范围**: 不涉及。

        :param sql_model: The sql_model of this ListLimitTaskResponseResult.
        :type sql_model: str
        """
        self._sql_model = sql_model

    @property
    def key_words(self):
        r"""Gets the key_words of this ListLimitTaskResponseResult.

        **参数解释**: 关键词，仅当任务类型为SQL_TYPE时，返回该值。 **取值范围**: 不涉及。

        :return: The key_words of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._key_words

    @key_words.setter
    def key_words(self, key_words):
        r"""Sets the key_words of this ListLimitTaskResponseResult.

        **参数解释**: 关键词，仅当任务类型为SQL_TYPE时，返回该值。 **取值范围**: 不涉及。

        :param key_words: The key_words of this ListLimitTaskResponseResult.
        :type key_words: str
        """
        self._key_words = key_words

    @property
    def status(self):
        r"""Gets the status of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务状态。 **取值范围**: 当前支持：CREATING，UPDATING，DELETING，WAIT_EXECUTE，EXCUTING，TIME_OVER，DELETED，CREATE_FAILED，UPDATE_FAILED，DELETE_FAILED，EXCEPTION，NODE_SHUT_DOWN。

        :return: The status of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务状态。 **取值范围**: 当前支持：CREATING，UPDATING，DELETING，WAIT_EXECUTE，EXCUTING，TIME_OVER，DELETED，CREATE_FAILED，UPDATE_FAILED，DELETE_FAILED，EXCEPTION，NODE_SHUT_DOWN。

        :param status: The status of this ListLimitTaskResponseResult.
        :type status: str
        """
        self._status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListLimitTaskResponseResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。

        :return: The instance_id of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListLimitTaskResponseResult.

        **参数解释**: 实例ID。 **取值范围**: 不涉及。

        :param instance_id: The instance_id of this ListLimitTaskResponseResult.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ListLimitTaskResponseResult.

        **参数解释**: 规则名。 **取值范围**: 不涉及。

        :return: The rule_name of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ListLimitTaskResponseResult.

        **参数解释**: 规则名。 **取值范围**: 不涉及。

        :param rule_name: The rule_name of this ListLimitTaskResponseResult.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def parallel_size(self):
        r"""Gets the parallel_size of this ListLimitTaskResponseResult.

        **参数解释**: 并发数。 **取值范围**: [0, 2147483647]

        :return: The parallel_size of this ListLimitTaskResponseResult.
        :rtype: int
        """
        return self._parallel_size

    @parallel_size.setter
    def parallel_size(self, parallel_size):
        r"""Sets the parallel_size of this ListLimitTaskResponseResult.

        **参数解释**: 并发数。 **取值范围**: [0, 2147483647]

        :param parallel_size: The parallel_size of this ListLimitTaskResponseResult.
        :type parallel_size: int
        """
        self._parallel_size = parallel_size

    @property
    def start_time(self):
        r"""Gets the start_time of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务开始时间。 **取值范围**: 不涉及。

        :return: The start_time of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务开始时间。 **取值范围**: 不涉及。

        :param start_time: The start_time of this ListLimitTaskResponseResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务结束时间。 **取值范围**: 不涉及。

        :return: The end_time of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务结束时间。 **取值范围**: 不涉及。

        :param end_time: The end_time of this ListLimitTaskResponseResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def cpu_utilization(self):
        r"""Gets the cpu_utilization of this ListLimitTaskResponseResult.

        **参数解释**: CPU利用率阈值，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留整数部分。 **取值范围**: [0, 100)

        :return: The cpu_utilization of this ListLimitTaskResponseResult.
        :rtype: int
        """
        return self._cpu_utilization

    @cpu_utilization.setter
    def cpu_utilization(self, cpu_utilization):
        r"""Sets the cpu_utilization of this ListLimitTaskResponseResult.

        **参数解释**: CPU利用率阈值，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留整数部分。 **取值范围**: [0, 100)

        :param cpu_utilization: The cpu_utilization of this ListLimitTaskResponseResult.
        :type cpu_utilization: int
        """
        self._cpu_utilization = cpu_utilization

    @property
    def memory_utilization(self):
        r"""Gets the memory_utilization of this ListLimitTaskResponseResult.

        **参数解释**: 内存利用率阈值，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留整数部分。 **取值范围**: [0, 100)

        :return: The memory_utilization of this ListLimitTaskResponseResult.
        :rtype: int
        """
        return self._memory_utilization

    @memory_utilization.setter
    def memory_utilization(self, memory_utilization):
        r"""Sets the memory_utilization of this ListLimitTaskResponseResult.

        **参数解释**: 内存利用率阈值，仅当任务类型为SESSION_ACTIVE_MAX_COUNT时，返回该值且只保留整数部分。 **取值范围**: [0, 100)

        :param memory_utilization: The memory_utilization of this ListLimitTaskResponseResult.
        :type memory_utilization: int
        """
        self._memory_utilization = memory_utilization

    @property
    def created(self):
        r"""Gets the created of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务创建时间。 **取值范围**: 不涉及。

        :return: The created of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务创建时间。 **取值范围**: 不涉及。

        :param created: The created of this ListLimitTaskResponseResult.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务更新时间。 **取值范围**: 不涉及。

        :return: The updated of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ListLimitTaskResponseResult.

        **参数解释**: 限流任务更新时间。 **取值范围**: 不涉及。

        :param updated: The updated of this ListLimitTaskResponseResult.
        :type updated: str
        """
        self._updated = updated

    @property
    def creator(self):
        r"""Gets the creator of this ListLimitTaskResponseResult.

        **参数解释**: 创建者。 **取值范围**: 不涉及。

        :return: The creator of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ListLimitTaskResponseResult.

        **参数解释**: 创建者。 **取值范围**: 不涉及。

        :param creator: The creator of this ListLimitTaskResponseResult.
        :type creator: str
        """
        self._creator = creator

    @property
    def modifier(self):
        r"""Gets the modifier of this ListLimitTaskResponseResult.

        **参数解释**: 更新者。 **取值范围**: 不涉及。

        :return: The modifier of this ListLimitTaskResponseResult.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this ListLimitTaskResponseResult.

        **参数解释**: 更新者。 **取值范围**: 不涉及。

        :param modifier: The modifier of this ListLimitTaskResponseResult.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def node_infos(self):
        r"""Gets the node_infos of this ListLimitTaskResponseResult.

        **参数解释**: CN节点信息列表。

        :return: The node_infos of this ListLimitTaskResponseResult.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ShowLimitTaskNodeOption`]
        """
        return self._node_infos

    @node_infos.setter
    def node_infos(self, node_infos):
        r"""Sets the node_infos of this ListLimitTaskResponseResult.

        **参数解释**: CN节点信息列表。

        :param node_infos: The node_infos of this ListLimitTaskResponseResult.
        :type node_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ShowLimitTaskNodeOption`]
        """
        self._node_infos = node_infos

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
        if not isinstance(other, ListLimitTaskResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
