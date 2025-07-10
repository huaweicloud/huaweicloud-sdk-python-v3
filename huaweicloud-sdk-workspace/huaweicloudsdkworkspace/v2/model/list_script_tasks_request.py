# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptTasksRequest:

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
        'resource_group_id': 'list[str]',
        'script_id': 'str',
        'script_name': 'str',
        'status': 'str',
        'resource_group_type': 'str',
        'task_id': 'list[str]',
        'task_type': 'str',
        'execute_time_start': 'str',
        'execute_time_end': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'resource_group_id': 'resource_group_id',
        'script_id': 'script_id',
        'script_name': 'script_name',
        'status': 'status',
        'resource_group_type': 'resource_group_type',
        'task_id': 'task_id',
        'task_type': 'task_type',
        'execute_time_start': 'execute_time_start',
        'execute_time_end': 'execute_time_end'
    }

    def __init__(self, offset=None, limit=None, resource_group_id=None, script_id=None, script_name=None, status=None, resource_group_type=None, task_id=None, task_type=None, execute_time_start=None, execute_time_end=None):
        r"""ListScriptTasksRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 单次查询的大小[1-100]，默认值10。
        :type limit: int
        :param resource_group_id: 执行脚本的资源组ID。
        :type resource_group_id: list[str]
        :param script_id: 脚本ID。
        :type script_id: str
        :param script_name: 脚本名。
        :type script_name: str
        :param status: 执行情况。
        :type status: str
        :param resource_group_type: 资源组类型。
        :type resource_group_type: str
        :param task_id: 执行脚本的任务ID。
        :type task_id: list[str]
        :param task_type: 任务类型(SCRIPT/COMMAND)。
        :type task_type: str
        :param execute_time_start: 按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。
        :type execute_time_start: str
        :param execute_time_end: 按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。
        :type execute_time_end: str
        """
        
        

        self._offset = None
        self._limit = None
        self._resource_group_id = None
        self._script_id = None
        self._script_name = None
        self._status = None
        self._resource_group_type = None
        self._task_id = None
        self._task_type = None
        self._execute_time_start = None
        self._execute_time_end = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        if script_id is not None:
            self.script_id = script_id
        if script_name is not None:
            self.script_name = script_name
        if status is not None:
            self.status = status
        if resource_group_type is not None:
            self.resource_group_type = resource_group_type
        if task_id is not None:
            self.task_id = task_id
        if task_type is not None:
            self.task_type = task_type
        if execute_time_start is not None:
            self.execute_time_start = execute_time_start
        if execute_time_end is not None:
            self.execute_time_end = execute_time_end

    @property
    def offset(self):
        r"""Gets the offset of this ListScriptTasksRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListScriptTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScriptTasksRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListScriptTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScriptTasksRequest.

        单次查询的大小[1-100]，默认值10。

        :return: The limit of this ListScriptTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScriptTasksRequest.

        单次查询的大小[1-100]，默认值10。

        :param limit: The limit of this ListScriptTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def resource_group_id(self):
        r"""Gets the resource_group_id of this ListScriptTasksRequest.

        执行脚本的资源组ID。

        :return: The resource_group_id of this ListScriptTasksRequest.
        :rtype: list[str]
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        r"""Sets the resource_group_id of this ListScriptTasksRequest.

        执行脚本的资源组ID。

        :param resource_group_id: The resource_group_id of this ListScriptTasksRequest.
        :type resource_group_id: list[str]
        """
        self._resource_group_id = resource_group_id

    @property
    def script_id(self):
        r"""Gets the script_id of this ListScriptTasksRequest.

        脚本ID。

        :return: The script_id of this ListScriptTasksRequest.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this ListScriptTasksRequest.

        脚本ID。

        :param script_id: The script_id of this ListScriptTasksRequest.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def script_name(self):
        r"""Gets the script_name of this ListScriptTasksRequest.

        脚本名。

        :return: The script_name of this ListScriptTasksRequest.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this ListScriptTasksRequest.

        脚本名。

        :param script_name: The script_name of this ListScriptTasksRequest.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def status(self):
        r"""Gets the status of this ListScriptTasksRequest.

        执行情况。

        :return: The status of this ListScriptTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListScriptTasksRequest.

        执行情况。

        :param status: The status of this ListScriptTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def resource_group_type(self):
        r"""Gets the resource_group_type of this ListScriptTasksRequest.

        资源组类型。

        :return: The resource_group_type of this ListScriptTasksRequest.
        :rtype: str
        """
        return self._resource_group_type

    @resource_group_type.setter
    def resource_group_type(self, resource_group_type):
        r"""Sets the resource_group_type of this ListScriptTasksRequest.

        资源组类型。

        :param resource_group_type: The resource_group_type of this ListScriptTasksRequest.
        :type resource_group_type: str
        """
        self._resource_group_type = resource_group_type

    @property
    def task_id(self):
        r"""Gets the task_id of this ListScriptTasksRequest.

        执行脚本的任务ID。

        :return: The task_id of this ListScriptTasksRequest.
        :rtype: list[str]
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListScriptTasksRequest.

        执行脚本的任务ID。

        :param task_id: The task_id of this ListScriptTasksRequest.
        :type task_id: list[str]
        """
        self._task_id = task_id

    @property
    def task_type(self):
        r"""Gets the task_type of this ListScriptTasksRequest.

        任务类型(SCRIPT/COMMAND)。

        :return: The task_type of this ListScriptTasksRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ListScriptTasksRequest.

        任务类型(SCRIPT/COMMAND)。

        :param task_type: The task_type of this ListScriptTasksRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def execute_time_start(self):
        r"""Gets the execute_time_start of this ListScriptTasksRequest.

        按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。

        :return: The execute_time_start of this ListScriptTasksRequest.
        :rtype: str
        """
        return self._execute_time_start

    @execute_time_start.setter
    def execute_time_start(self, execute_time_start):
        r"""Sets the execute_time_start of this ListScriptTasksRequest.

        按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。

        :param execute_time_start: The execute_time_start of this ListScriptTasksRequest.
        :type execute_time_start: str
        """
        self._execute_time_start = execute_time_start

    @property
    def execute_time_end(self):
        r"""Gets the execute_time_end of this ListScriptTasksRequest.

        按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。

        :return: The execute_time_end of this ListScriptTasksRequest.
        :rtype: str
        """
        return self._execute_time_end

    @execute_time_end.setter
    def execute_time_end(self, execute_time_end):
        r"""Sets the execute_time_end of this ListScriptTasksRequest.

        按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。

        :param execute_time_end: The execute_time_end of this ListScriptTasksRequest.
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
        if not isinstance(other, ListScriptTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
