# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTaskResultDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'task_name': 'str',
        'begin_time': 'str',
        'end_time': 'str',
        'task_type': 'str',
        'operator': 'str',
        'total_count': 'int',
        'success_count': 'int',
        'failure_count': 'int',
        'task_status': 'str',
        'task_id': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'task_name': 'task_name',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'task_type': 'task_type',
        'operator': 'operator',
        'total_count': 'total_count',
        'success_count': 'success_count',
        'failure_count': 'failure_count',
        'task_status': 'task_status',
        'task_id': 'task_id',
        'user_id': 'user_id'
    }

    def __init__(self, resource=None, task_name=None, begin_time=None, end_time=None, task_type=None, operator=None, total_count=None, success_count=None, failure_count=None, task_status=None, task_id=None, user_id=None):
        r"""QueryTaskResultDTO

        The model defined in huaweicloud sdk

        :param resource: 资源
        :type resource: str
        :param task_name: 任务名称
        :type task_name: str
        :param begin_time: 任务开始时间
        :type begin_time: str
        :param end_time: 任务结束时间
        :type end_time: str
        :param task_type: 任务类型
        :type task_type: str
        :param operator: 操作人
        :type operator: str
        :param total_count: 导入总数
        :type total_count: int
        :param success_count: 成功数
        :type success_count: int
        :param failure_count: 失败数
        :type failure_count: int
        :param task_status: 任务状态
        :type task_status: str
        :param task_id: 任务ID
        :type task_id: str
        :param user_id: 操作用户ID
        :type user_id: str
        """
        
        

        self._resource = None
        self._task_name = None
        self._begin_time = None
        self._end_time = None
        self._task_type = None
        self._operator = None
        self._total_count = None
        self._success_count = None
        self._failure_count = None
        self._task_status = None
        self._task_id = None
        self._user_id = None
        self.discriminator = None

        if resource is not None:
            self.resource = resource
        if task_name is not None:
            self.task_name = task_name
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if task_type is not None:
            self.task_type = task_type
        if operator is not None:
            self.operator = operator
        if total_count is not None:
            self.total_count = total_count
        if success_count is not None:
            self.success_count = success_count
        if failure_count is not None:
            self.failure_count = failure_count
        if task_status is not None:
            self.task_status = task_status
        if task_id is not None:
            self.task_id = task_id
        if user_id is not None:
            self.user_id = user_id

    @property
    def resource(self):
        r"""Gets the resource of this QueryTaskResultDTO.

        资源

        :return: The resource of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this QueryTaskResultDTO.

        资源

        :param resource: The resource of this QueryTaskResultDTO.
        :type resource: str
        """
        self._resource = resource

    @property
    def task_name(self):
        r"""Gets the task_name of this QueryTaskResultDTO.

        任务名称

        :return: The task_name of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this QueryTaskResultDTO.

        任务名称

        :param task_name: The task_name of this QueryTaskResultDTO.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def begin_time(self):
        r"""Gets the begin_time of this QueryTaskResultDTO.

        任务开始时间

        :return: The begin_time of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this QueryTaskResultDTO.

        任务开始时间

        :param begin_time: The begin_time of this QueryTaskResultDTO.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this QueryTaskResultDTO.

        任务结束时间

        :return: The end_time of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this QueryTaskResultDTO.

        任务结束时间

        :param end_time: The end_time of this QueryTaskResultDTO.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def task_type(self):
        r"""Gets the task_type of this QueryTaskResultDTO.

        任务类型

        :return: The task_type of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        r"""Sets the task_type of this QueryTaskResultDTO.

        任务类型

        :param task_type: The task_type of this QueryTaskResultDTO.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def operator(self):
        r"""Gets the operator of this QueryTaskResultDTO.

        操作人

        :return: The operator of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this QueryTaskResultDTO.

        操作人

        :param operator: The operator of this QueryTaskResultDTO.
        :type operator: str
        """
        self._operator = operator

    @property
    def total_count(self):
        r"""Gets the total_count of this QueryTaskResultDTO.

        导入总数

        :return: The total_count of this QueryTaskResultDTO.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this QueryTaskResultDTO.

        导入总数

        :param total_count: The total_count of this QueryTaskResultDTO.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def success_count(self):
        r"""Gets the success_count of this QueryTaskResultDTO.

        成功数

        :return: The success_count of this QueryTaskResultDTO.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this QueryTaskResultDTO.

        成功数

        :param success_count: The success_count of this QueryTaskResultDTO.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failure_count(self):
        r"""Gets the failure_count of this QueryTaskResultDTO.

        失败数

        :return: The failure_count of this QueryTaskResultDTO.
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        r"""Sets the failure_count of this QueryTaskResultDTO.

        失败数

        :param failure_count: The failure_count of this QueryTaskResultDTO.
        :type failure_count: int
        """
        self._failure_count = failure_count

    @property
    def task_status(self):
        r"""Gets the task_status of this QueryTaskResultDTO.

        任务状态

        :return: The task_status of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        r"""Sets the task_status of this QueryTaskResultDTO.

        任务状态

        :param task_status: The task_status of this QueryTaskResultDTO.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def task_id(self):
        r"""Gets the task_id of this QueryTaskResultDTO.

        任务ID

        :return: The task_id of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this QueryTaskResultDTO.

        任务ID

        :param task_id: The task_id of this QueryTaskResultDTO.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def user_id(self):
        r"""Gets the user_id of this QueryTaskResultDTO.

        操作用户ID

        :return: The user_id of this QueryTaskResultDTO.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this QueryTaskResultDTO.

        操作用户ID

        :param user_id: The user_id of this QueryTaskResultDTO.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, QueryTaskResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
