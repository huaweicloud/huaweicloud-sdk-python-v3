# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLimitTaskRequest:

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
        'task_scope': 'str',
        'limit_type': 'str',
        'limit_type_value': 'str',
        'task_name': 'str',
        'sql_model': 'str',
        'rule_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'task_scope': 'task_scope',
        'limit_type': 'limit_type',
        'limit_type_value': 'limit_type_value',
        'task_name': 'task_name',
        'sql_model': 'sql_model',
        'rule_name': 'rule_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, task_scope=None, limit_type=None, limit_type_value=None, task_name=None, sql_model=None, rule_name=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ListLimitTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param task_scope: 限流任务范围，目前支持SQL,SESSION。
        :type task_scope: str
        :param limit_type: 限流类型，支持SQL_ID、SQL_TYPE、SESSION_ACTIVE_MAX_COUNT类型。
        :type limit_type: str
        :param limit_type_value: 限流类型值，支持模糊匹配。
        :type limit_type_value: str
        :param task_name: 限流任务名，支持模糊匹配。
        :type task_name: str
        :param sql_model: sql模板，支持模糊匹配。
        :type sql_model: str
        :param rule_name: 规则名。
        :type rule_name: str
        :param start_time: 限流任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ,当前时间指UTC时间。
        :type start_time: str
        :param end_time: 限流任务结束时间，格式为yyyy-mm-ddThh:mm:ssZ,当前时间指UTC时间。
        :type end_time: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  取值范围：0 - 10000
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._task_scope = None
        self._limit_type = None
        self._limit_type_value = None
        self._task_name = None
        self._sql_model = None
        self._rule_name = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if task_scope is not None:
            self.task_scope = task_scope
        if limit_type is not None:
            self.limit_type = limit_type
        if limit_type_value is not None:
            self.limit_type_value = limit_type_value
        if task_name is not None:
            self.task_name = task_name
        if sql_model is not None:
            self.sql_model = sql_model
        if rule_name is not None:
            self.rule_name = rule_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListLimitTaskRequest.

        实例ID。

        :return: The instance_id of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListLimitTaskRequest.

        实例ID。

        :param instance_id: The instance_id of this ListLimitTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_scope(self):
        r"""Gets the task_scope of this ListLimitTaskRequest.

        限流任务范围，目前支持SQL,SESSION。

        :return: The task_scope of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._task_scope

    @task_scope.setter
    def task_scope(self, task_scope):
        r"""Sets the task_scope of this ListLimitTaskRequest.

        限流任务范围，目前支持SQL,SESSION。

        :param task_scope: The task_scope of this ListLimitTaskRequest.
        :type task_scope: str
        """
        self._task_scope = task_scope

    @property
    def limit_type(self):
        r"""Gets the limit_type of this ListLimitTaskRequest.

        限流类型，支持SQL_ID、SQL_TYPE、SESSION_ACTIVE_MAX_COUNT类型。

        :return: The limit_type of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._limit_type

    @limit_type.setter
    def limit_type(self, limit_type):
        r"""Sets the limit_type of this ListLimitTaskRequest.

        限流类型，支持SQL_ID、SQL_TYPE、SESSION_ACTIVE_MAX_COUNT类型。

        :param limit_type: The limit_type of this ListLimitTaskRequest.
        :type limit_type: str
        """
        self._limit_type = limit_type

    @property
    def limit_type_value(self):
        r"""Gets the limit_type_value of this ListLimitTaskRequest.

        限流类型值，支持模糊匹配。

        :return: The limit_type_value of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._limit_type_value

    @limit_type_value.setter
    def limit_type_value(self, limit_type_value):
        r"""Sets the limit_type_value of this ListLimitTaskRequest.

        限流类型值，支持模糊匹配。

        :param limit_type_value: The limit_type_value of this ListLimitTaskRequest.
        :type limit_type_value: str
        """
        self._limit_type_value = limit_type_value

    @property
    def task_name(self):
        r"""Gets the task_name of this ListLimitTaskRequest.

        限流任务名，支持模糊匹配。

        :return: The task_name of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ListLimitTaskRequest.

        限流任务名，支持模糊匹配。

        :param task_name: The task_name of this ListLimitTaskRequest.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def sql_model(self):
        r"""Gets the sql_model of this ListLimitTaskRequest.

        sql模板，支持模糊匹配。

        :return: The sql_model of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._sql_model

    @sql_model.setter
    def sql_model(self, sql_model):
        r"""Sets the sql_model of this ListLimitTaskRequest.

        sql模板，支持模糊匹配。

        :param sql_model: The sql_model of this ListLimitTaskRequest.
        :type sql_model: str
        """
        self._sql_model = sql_model

    @property
    def rule_name(self):
        r"""Gets the rule_name of this ListLimitTaskRequest.

        规则名。

        :return: The rule_name of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this ListLimitTaskRequest.

        规则名。

        :param rule_name: The rule_name of this ListLimitTaskRequest.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ListLimitTaskRequest.

        限流任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ,当前时间指UTC时间。

        :return: The start_time of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListLimitTaskRequest.

        限流任务开始时间，格式为yyyy-mm-ddThh:mm:ssZ,当前时间指UTC时间。

        :param start_time: The start_time of this ListLimitTaskRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListLimitTaskRequest.

        限流任务结束时间，格式为yyyy-mm-ddThh:mm:ssZ,当前时间指UTC时间。

        :return: The end_time of this ListLimitTaskRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListLimitTaskRequest.

        限流任务结束时间，格式为yyyy-mm-ddThh:mm:ssZ,当前时间指UTC时间。

        :param end_time: The end_time of this ListLimitTaskRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListLimitTaskRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  取值范围：0 - 10000

        :return: The offset of this ListLimitTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLimitTaskRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  取值范围：0 - 10000

        :param offset: The offset of this ListLimitTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLimitTaskRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListLimitTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLimitTaskRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListLimitTaskRequest.
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
        if not isinstance(other, ListLimitTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
