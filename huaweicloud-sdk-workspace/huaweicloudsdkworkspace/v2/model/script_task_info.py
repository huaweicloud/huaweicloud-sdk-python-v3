# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptTaskInfo:

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
        'task_scripts': 'list[ScriptTaskInfoTaskScripts]',
        'resource_type': 'str',
        'resource_ids': 'list[str]',
        'gray_resource_ids': 'list[str]',
        'success_num': 'int',
        'failed_num': 'int',
        'skip_num': 'int',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'task_scripts': 'task_scripts',
        'resource_type': 'resource_type',
        'resource_ids': 'resource_ids',
        'gray_resource_ids': 'gray_resource_ids',
        'success_num': 'success_num',
        'failed_num': 'failed_num',
        'skip_num': 'skip_num',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status'
    }

    def __init__(self, id=None, task_scripts=None, resource_type=None, resource_ids=None, gray_resource_ids=None, success_num=None, failed_num=None, skip_num=None, start_time=None, end_time=None, status=None):
        r"""ScriptTaskInfo

        The model defined in huaweicloud sdk

        :param id: 脚本任务ID。
        :type id: str
        :param task_scripts: 脚本列表。
        :type task_scripts: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfoTaskScripts`]
        :param resource_type: 资源类型，如DESKTOP。
        :type resource_type: str
        :param resource_ids: 执行脚本的资源ID列表。
        :type resource_ids: list[str]
        :param gray_resource_ids: 灰度批次执行资源ID列表。
        :type gray_resource_ids: list[str]
        :param success_num: task中成功的执行记录数量。
        :type success_num: int
        :param failed_num: task中失败的执行记录数量。
        :type failed_num: int
        :param skip_num: task中跳过的执行记录数量。
        :type skip_num: int
        :param start_time: 脚本执行开始时间。
        :type start_time: datetime
        :param end_time: 脚本执行结束时间。
        :type end_time: datetime
        :param status: 任务结果。
        :type status: str
        """
        
        

        self._id = None
        self._task_scripts = None
        self._resource_type = None
        self._resource_ids = None
        self._gray_resource_ids = None
        self._success_num = None
        self._failed_num = None
        self._skip_num = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if task_scripts is not None:
            self.task_scripts = task_scripts
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_ids is not None:
            self.resource_ids = resource_ids
        if gray_resource_ids is not None:
            self.gray_resource_ids = gray_resource_ids
        if success_num is not None:
            self.success_num = success_num
        if failed_num is not None:
            self.failed_num = failed_num
        if skip_num is not None:
            self.skip_num = skip_num
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this ScriptTaskInfo.

        脚本任务ID。

        :return: The id of this ScriptTaskInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScriptTaskInfo.

        脚本任务ID。

        :param id: The id of this ScriptTaskInfo.
        :type id: str
        """
        self._id = id

    @property
    def task_scripts(self):
        r"""Gets the task_scripts of this ScriptTaskInfo.

        脚本列表。

        :return: The task_scripts of this ScriptTaskInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfoTaskScripts`]
        """
        return self._task_scripts

    @task_scripts.setter
    def task_scripts(self, task_scripts):
        r"""Sets the task_scripts of this ScriptTaskInfo.

        脚本列表。

        :param task_scripts: The task_scripts of this ScriptTaskInfo.
        :type task_scripts: list[:class:`huaweicloudsdkworkspace.v2.ScriptTaskInfoTaskScripts`]
        """
        self._task_scripts = task_scripts

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ScriptTaskInfo.

        资源类型，如DESKTOP。

        :return: The resource_type of this ScriptTaskInfo.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ScriptTaskInfo.

        资源类型，如DESKTOP。

        :param resource_type: The resource_type of this ScriptTaskInfo.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_ids(self):
        r"""Gets the resource_ids of this ScriptTaskInfo.

        执行脚本的资源ID列表。

        :return: The resource_ids of this ScriptTaskInfo.
        :rtype: list[str]
        """
        return self._resource_ids

    @resource_ids.setter
    def resource_ids(self, resource_ids):
        r"""Sets the resource_ids of this ScriptTaskInfo.

        执行脚本的资源ID列表。

        :param resource_ids: The resource_ids of this ScriptTaskInfo.
        :type resource_ids: list[str]
        """
        self._resource_ids = resource_ids

    @property
    def gray_resource_ids(self):
        r"""Gets the gray_resource_ids of this ScriptTaskInfo.

        灰度批次执行资源ID列表。

        :return: The gray_resource_ids of this ScriptTaskInfo.
        :rtype: list[str]
        """
        return self._gray_resource_ids

    @gray_resource_ids.setter
    def gray_resource_ids(self, gray_resource_ids):
        r"""Sets the gray_resource_ids of this ScriptTaskInfo.

        灰度批次执行资源ID列表。

        :param gray_resource_ids: The gray_resource_ids of this ScriptTaskInfo.
        :type gray_resource_ids: list[str]
        """
        self._gray_resource_ids = gray_resource_ids

    @property
    def success_num(self):
        r"""Gets the success_num of this ScriptTaskInfo.

        task中成功的执行记录数量。

        :return: The success_num of this ScriptTaskInfo.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this ScriptTaskInfo.

        task中成功的执行记录数量。

        :param success_num: The success_num of this ScriptTaskInfo.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def failed_num(self):
        r"""Gets the failed_num of this ScriptTaskInfo.

        task中失败的执行记录数量。

        :return: The failed_num of this ScriptTaskInfo.
        :rtype: int
        """
        return self._failed_num

    @failed_num.setter
    def failed_num(self, failed_num):
        r"""Sets the failed_num of this ScriptTaskInfo.

        task中失败的执行记录数量。

        :param failed_num: The failed_num of this ScriptTaskInfo.
        :type failed_num: int
        """
        self._failed_num = failed_num

    @property
    def skip_num(self):
        r"""Gets the skip_num of this ScriptTaskInfo.

        task中跳过的执行记录数量。

        :return: The skip_num of this ScriptTaskInfo.
        :rtype: int
        """
        return self._skip_num

    @skip_num.setter
    def skip_num(self, skip_num):
        r"""Sets the skip_num of this ScriptTaskInfo.

        task中跳过的执行记录数量。

        :param skip_num: The skip_num of this ScriptTaskInfo.
        :type skip_num: int
        """
        self._skip_num = skip_num

    @property
    def start_time(self):
        r"""Gets the start_time of this ScriptTaskInfo.

        脚本执行开始时间。

        :return: The start_time of this ScriptTaskInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ScriptTaskInfo.

        脚本执行开始时间。

        :param start_time: The start_time of this ScriptTaskInfo.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ScriptTaskInfo.

        脚本执行结束时间。

        :return: The end_time of this ScriptTaskInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ScriptTaskInfo.

        脚本执行结束时间。

        :param end_time: The end_time of this ScriptTaskInfo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this ScriptTaskInfo.

        任务结果。

        :return: The status of this ScriptTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScriptTaskInfo.

        任务结果。

        :param status: The status of this ScriptTaskInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ScriptTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
