# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptRecordsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'resource_id': 'list[str]',
        'resource_group_id': 'list[str]',
        'script_id': 'list[str]',
        'script_name': 'list[str]',
        'status': 'str',
        'is_first_order': 'bool',
        'script_task_id': 'str',
        'task_type': 'str',
        'show_history': 'bool',
        'execute_time_start': 'str',
        'execute_time_end': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'resource_id': 'resource_id',
        'resource_group_id': 'resource_group_id',
        'script_id': 'script_id',
        'script_name': 'script_name',
        'status': 'status',
        'is_first_order': 'is_first_order',
        'script_task_id': 'script_task_id',
        'task_type': 'task_type',
        'show_history': 'show_history',
        'execute_time_start': 'execute_time_start',
        'execute_time_end': 'execute_time_end'
    }

    def __init__(self, offset=None, limit=None, resource_id=None, resource_group_id=None, script_id=None, script_name=None, status=None, is_first_order=None, script_task_id=None, task_type=None, show_history=None, execute_time_start=None, execute_time_end=None):
        r"""ListScriptRecordsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 单次查询的大小[1-100]，默认值10。
        :type limit: int
        :param resource_id: 执行脚本的资源ID列表。
        :type resource_id: list[str]
        :param resource_group_id: 执行脚本的资源组ID。
        :type resource_group_id: list[str]
        :param script_id: 执行的脚本ID。
        :type script_id: list[str]
        :param script_name: 执行的脚本名称。
        :type script_name: list[str]
        :param status: 执行脚本的执行情况。
        :type status: str
        :param is_first_order: 是否首批执行。
        :type is_first_order: bool
        :param script_task_id: 执行脚本的任务ID。
        :type script_task_id: str
        :param task_type: 执行记录的任务类型(SCRIPT/COMMAND)。
        :type task_type: str
        :param show_history: 是否查询历史记录，默认为false，为true时需要同时传入resource_id与script_id。
        :type show_history: bool
        :param execute_time_start: 按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有执行记录。时间格式如：“2021-10-01T12:00:00Z”。
        :type execute_time_start: str
        :param execute_time_end: 按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有执行记录。时间格式如：“2021-10-01T12:00:00Z”。
        :type execute_time_end: str
        """
        
        

        self._offset = None
        self._limit = None
        self._resource_id = None
        self._resource_group_id = None
        self._script_id = None
        self._script_name = None
        self._status = None
        self._is_first_order = None
        self._script_task_id = None
        self._task_type = None
        self._show_history = None
        self._execute_time_start = None
        self._execute_time_end = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if script_id is not None:
            self.script_id = script_id
        if script_name is not None:
            self.script_name = script_name
        if status is not None:
            self.status = status
        if is_first_order is not None:
            self.is_first_order = is_first_order
        if script_task_id is not None:
            self.script_task_id = script_task_id
        if task_type is not None:
            self.task_type = task_type
        if show_history is not None:
            self.show_history = show_history
        if execute_time_start is not None:
            self.execute_time_start = execute_time_start
        if execute_time_end is not None:
            self.execute_time_end = execute_time_end

    @property
    def offset(self):
        r"""Gets the offset of this ListScriptRecordsRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListScriptRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScriptRecordsRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListScriptRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScriptRecordsRequest.

        单次查询的大小[1-100]，默认值10。

        :return: The limit of this ListScriptRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScriptRecordsRequest.

        单次查询的大小[1-100]，默认值10。

        :param limit: The limit of this ListScriptRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListScriptRecordsRequest.

        执行脚本的资源ID列表。

        :return: The resource_id of this ListScriptRecordsRequest.
        :rtype: list[str]
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListScriptRecordsRequest.

        执行脚本的资源ID列表。

        :param resource_id: The resource_id of this ListScriptRecordsRequest.
        :type resource_id: list[str]
        """
        self._resource_id = resource_id

    @property
    def resource_group_id(self):
        r"""Gets the resource_group_id of this ListScriptRecordsRequest.

        执行脚本的资源组ID。

        :return: The resource_group_id of this ListScriptRecordsRequest.
        :rtype: list[str]
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        r"""Sets the resource_group_id of this ListScriptRecordsRequest.

        执行脚本的资源组ID。

        :param resource_group_id: The resource_group_id of this ListScriptRecordsRequest.
        :type resource_group_id: list[str]
        """
        self._resource_group_id = resource_group_id

    @property
    def script_id(self):
        r"""Gets the script_id of this ListScriptRecordsRequest.

        执行的脚本ID。

        :return: The script_id of this ListScriptRecordsRequest.
        :rtype: list[str]
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this ListScriptRecordsRequest.

        执行的脚本ID。

        :param script_id: The script_id of this ListScriptRecordsRequest.
        :type script_id: list[str]
        """
        self._script_id = script_id

    @property
    def script_name(self):
        r"""Gets the script_name of this ListScriptRecordsRequest.

        执行的脚本名称。

        :return: The script_name of this ListScriptRecordsRequest.
        :rtype: list[str]
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this ListScriptRecordsRequest.

        执行的脚本名称。

        :param script_name: The script_name of this ListScriptRecordsRequest.
        :type script_name: list[str]
        """
        self._script_name = script_name

    @property
    def status(self):
        r"""Gets the status of this ListScriptRecordsRequest.

        执行脚本的执行情况。

        :return: The status of this ListScriptRecordsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListScriptRecordsRequest.

        执行脚本的执行情况。

        :param status: The status of this ListScriptRecordsRequest.
        :type status: str
        """
        self._status = status

    @property
    def is_first_order(self):
        r"""Gets the is_first_order of this ListScriptRecordsRequest.

        是否首批执行。

        :return: The is_first_order of this ListScriptRecordsRequest.
        :rtype: bool
        """
        return self._is_first_order

    @is_first_order.setter
    def is_first_order(self, is_first_order):
        r"""Sets the is_first_order of this ListScriptRecordsRequest.

        是否首批执行。

        :param is_first_order: The is_first_order of this ListScriptRecordsRequest.
        :type is_first_order: bool
        """
        self._is_first_order = is_first_order

    @property
    def script_task_id(self):
        r"""Gets the script_task_id of this ListScriptRecordsRequest.

        执行脚本的任务ID。

        :return: The script_task_id of this ListScriptRecordsRequest.
        :rtype: str
        """
        return self._script_task_id

    @script_task_id.setter
    def script_task_id(self, script_task_id):
        r"""Sets the script_task_id of this ListScriptRecordsRequest.

        执行脚本的任务ID。

        :param script_task_id: The script_task_id of this ListScriptRecordsRequest.
        :type script_task_id: str
        """
        self._script_task_id = script_task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this ListScriptRecordsRequest.

        执行记录的任务类型(SCRIPT/COMMAND)。

        :return: The task_type of this ListScriptRecordsRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListScriptRecordsRequest.

        执行记录的任务类型(SCRIPT/COMMAND)。

        :param task_type: The task_type of this ListScriptRecordsRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def show_history(self):
        r"""Gets the show_history of this ListScriptRecordsRequest.

        是否查询历史记录，默认为false，为true时需要同时传入resource_id与script_id。

        :return: The show_history of this ListScriptRecordsRequest.
        :rtype: bool
        """
        return self._show_history

    @show_history.setter
    def show_history(self, show_history):
        r"""Sets the show_history of this ListScriptRecordsRequest.

        是否查询历史记录，默认为false，为true时需要同时传入resource_id与script_id。

        :param show_history: The show_history of this ListScriptRecordsRequest.
        :type show_history: bool
        """
        self._show_history = show_history

    @property
    def execute_time_start(self):
        r"""Gets the execute_time_start of this ListScriptRecordsRequest.

        按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有执行记录。时间格式如：“2021-10-01T12:00:00Z”。

        :return: The execute_time_start of this ListScriptRecordsRequest.
        :rtype: str
        """
        return self._execute_time_start

    @execute_time_start.setter
    def execute_time_start(self, execute_time_start):
        r"""Sets the execute_time_start of this ListScriptRecordsRequest.

        按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有执行记录。时间格式如：“2021-10-01T12:00:00Z”。

        :param execute_time_start: The execute_time_start of this ListScriptRecordsRequest.
        :type execute_time_start: str
        """
        self._execute_time_start = execute_time_start

    @property
    def execute_time_end(self):
        r"""Gets the execute_time_end of this ListScriptRecordsRequest.

        按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有执行记录。时间格式如：“2021-10-01T12:00:00Z”。

        :return: The execute_time_end of this ListScriptRecordsRequest.
        :rtype: str
        """
        return self._execute_time_end

    @execute_time_end.setter
    def execute_time_end(self, execute_time_end):
        r"""Sets the execute_time_end of this ListScriptRecordsRequest.

        按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有执行记录。时间格式如：“2021-10-01T12:00:00Z”。

        :param execute_time_end: The execute_time_end of this ListScriptRecordsRequest.
        :type execute_time_end: str
        """
        self._execute_time_end = execute_time_end

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
        if not isinstance(other, ListScriptRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
