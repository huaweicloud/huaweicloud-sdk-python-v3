# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDesktopPoolsScriptExecTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_pool_id': 'str',
        'script_id': 'str',
        'script_name': 'str',
        'status': 'str',
        'task_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'execute_time_start': 'str',
        'execute_time_end': 'str',
        'task_id': 'list[str]'
    }

    attribute_map = {
        'desktop_pool_id': 'desktop_pool_id',
        'script_id': 'script_id',
        'script_name': 'script_name',
        'status': 'status',
        'task_type': 'task_type',
        'offset': 'offset',
        'limit': 'limit',
        'execute_time_start': 'execute_time_start',
        'execute_time_end': 'execute_time_end',
        'task_id': 'task_id'
    }

    def __init__(self, desktop_pool_id=None, script_id=None, script_name=None, status=None, task_type=None, offset=None, limit=None, execute_time_start=None, execute_time_end=None, task_id=None):
        r"""ShowDesktopPoolsScriptExecTasksRequest

        The model defined in huaweicloud sdk

        :param desktop_pool_id: 桌面池id。
        :type desktop_pool_id: str
        :param script_id: 脚本id。
        :type script_id: str
        :param script_name: 脚本名称。
        :type script_name: str
        :param status: 执行情况。SUCCESS：成功，FAILED：失败，RUNNING：执行中，WAITING：等待。
        :type status: str
        :param task_type: 查询的任务类型。支持SCRIPT、COMMAND。
        :type task_type: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始。
        :type offset: int
        :param limit: 用于分页查询，返回桌面数量限制。取值范围0-100，默认值是10。
        :type limit: int
        :param execute_time_start: 按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。
        :type execute_time_start: str
        :param execute_time_end: 按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。
        :type execute_time_end: str
        :param task_id: 任务id。
        :type task_id: list[str]
        """
        
        

        self._desktop_pool_id = None
        self._script_id = None
        self._script_name = None
        self._status = None
        self._task_type = None
        self._offset = None
        self._limit = None
        self._execute_time_start = None
        self._execute_time_end = None
        self._task_id = None
        self.discriminator = None

        if desktop_pool_id is not None:
            self.desktop_pool_id = desktop_pool_id
        if script_id is not None:
            self.script_id = script_id
        if script_name is not None:
            self.script_name = script_name
        if status is not None:
            self.status = status
        if task_type is not None:
            self.task_type = task_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if execute_time_start is not None:
            self.execute_time_start = execute_time_start
        if execute_time_end is not None:
            self.execute_time_end = execute_time_end
        if task_id is not None:
            self.task_id = task_id

    @property
    def desktop_pool_id(self):
        r"""Gets the desktop_pool_id of this ShowDesktopPoolsScriptExecTasksRequest.

        桌面池id。

        :return: The desktop_pool_id of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: str
        """
        return self._desktop_pool_id

    @desktop_pool_id.setter
    def desktop_pool_id(self, desktop_pool_id):
        r"""Sets the desktop_pool_id of this ShowDesktopPoolsScriptExecTasksRequest.

        桌面池id。

        :param desktop_pool_id: The desktop_pool_id of this ShowDesktopPoolsScriptExecTasksRequest.
        :type desktop_pool_id: str
        """
        self._desktop_pool_id = desktop_pool_id

    @property
    def script_id(self):
        r"""Gets the script_id of this ShowDesktopPoolsScriptExecTasksRequest.

        脚本id。

        :return: The script_id of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: str
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id):
        r"""Sets the script_id of this ShowDesktopPoolsScriptExecTasksRequest.

        脚本id。

        :param script_id: The script_id of this ShowDesktopPoolsScriptExecTasksRequest.
        :type script_id: str
        """
        self._script_id = script_id

    @property
    def script_name(self):
        r"""Gets the script_name of this ShowDesktopPoolsScriptExecTasksRequest.

        脚本名称。

        :return: The script_name of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this ShowDesktopPoolsScriptExecTasksRequest.

        脚本名称。

        :param script_name: The script_name of this ShowDesktopPoolsScriptExecTasksRequest.
        :type script_name: str
        """
        self._script_name = script_name

    @property
    def status(self):
        r"""Gets the status of this ShowDesktopPoolsScriptExecTasksRequest.

        执行情况。SUCCESS：成功，FAILED：失败，RUNNING：执行中，WAITING：等待。

        :return: The status of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDesktopPoolsScriptExecTasksRequest.

        执行情况。SUCCESS：成功，FAILED：失败，RUNNING：执行中，WAITING：等待。

        :param status: The status of this ShowDesktopPoolsScriptExecTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def task_type(self):
        r"""Gets the task_type of this ShowDesktopPoolsScriptExecTasksRequest.

        查询的任务类型。支持SCRIPT、COMMAND。

        :return: The task_type of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this ShowDesktopPoolsScriptExecTasksRequest.

        查询的任务类型。支持SCRIPT、COMMAND。

        :param task_type: The task_type of this ShowDesktopPoolsScriptExecTasksRequest.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def offset(self):
        r"""Gets the offset of this ShowDesktopPoolsScriptExecTasksRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :return: The offset of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowDesktopPoolsScriptExecTasksRequest.

        用于分页查询，查询的起始记录序号，从0开始。

        :param offset: The offset of this ShowDesktopPoolsScriptExecTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowDesktopPoolsScriptExecTasksRequest.

        用于分页查询，返回桌面数量限制。取值范围0-100，默认值是10。

        :return: The limit of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowDesktopPoolsScriptExecTasksRequest.

        用于分页查询，返回桌面数量限制。取值范围0-100，默认值是10。

        :param limit: The limit of this ShowDesktopPoolsScriptExecTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def execute_time_start(self):
        r"""Gets the execute_time_start of this ShowDesktopPoolsScriptExecTasksRequest.

        按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。

        :return: The execute_time_start of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: str
        """
        return self._execute_time_start

    @execute_time_start.setter
    def execute_time_start(self, execute_time_start):
        r"""Sets the execute_time_start of this ShowDesktopPoolsScriptExecTasksRequest.

        按执行时间查询的起始时间。指定该参数后，返回的结果为此时间之后的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。

        :param execute_time_start: The execute_time_start of this ShowDesktopPoolsScriptExecTasksRequest.
        :type execute_time_start: str
        """
        self._execute_time_start = execute_time_start

    @property
    def execute_time_end(self):
        r"""Gets the execute_time_end of this ShowDesktopPoolsScriptExecTasksRequest.

        按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。

        :return: The execute_time_end of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: str
        """
        return self._execute_time_end

    @execute_time_end.setter
    def execute_time_end(self, execute_time_end):
        r"""Sets the execute_time_end of this ShowDesktopPoolsScriptExecTasksRequest.

        按执行时间查询的终止时间。指定该参数后，返回的结果为此时间之前的所有任务记录。时间格式如：“2021-10-01T12:00:00Z”。

        :param execute_time_end: The execute_time_end of this ShowDesktopPoolsScriptExecTasksRequest.
        :type execute_time_end: str
        """
        self._execute_time_end = execute_time_end

    @property
    def task_id(self):
        r"""Gets the task_id of this ShowDesktopPoolsScriptExecTasksRequest.

        任务id。

        :return: The task_id of this ShowDesktopPoolsScriptExecTasksRequest.
        :rtype: list[str]
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ShowDesktopPoolsScriptExecTasksRequest.

        任务id。

        :param task_id: The task_id of this ShowDesktopPoolsScriptExecTasksRequest.
        :type task_id: list[str]
        """
        self._task_id = task_id

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
        if not isinstance(other, ShowDesktopPoolsScriptExecTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
