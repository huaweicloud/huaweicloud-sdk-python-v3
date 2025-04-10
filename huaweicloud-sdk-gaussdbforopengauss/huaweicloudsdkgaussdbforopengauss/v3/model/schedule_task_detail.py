# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScheduleTaskDetail:

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
        'task_name': 'str',
        'status': 'str',
        'create_time': 'str',
        'start_time': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'task_content': 'object'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'status': 'status',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'task_content': 'task_content'
    }

    def __init__(self, task_id=None, task_name=None, status=None, create_time=None, start_time=None, instance_id=None, instance_name=None, task_content=None):
        r"""ScheduleTaskDetail

        The model defined in huaweicloud sdk

        :param task_id: 任务ID。
        :type task_id: str
        :param task_name: 任务名称。
        :type task_name: str
        :param status: 任务状态。
        :type status: str
        :param create_time: 任务创建时间,格式为yyyy-mm-ddThh:mm:ssZ。
        :type create_time: str
        :param start_time: 任务开始时间,格式为yyyy-mm-ddThh:mm:ssZ。
        :type start_time: str
        :param instance_id: 实例ID。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param task_content: 任务信息。
        :type task_content: object
        """
        
        

        self._task_id = None
        self._task_name = None
        self._status = None
        self._create_time = None
        self._start_time = None
        self._instance_id = None
        self._instance_name = None
        self._task_content = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if status is not None:
            self.status = status
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if task_content is not None:
            self.task_content = task_content

    @property
    def task_id(self):
        r"""Gets the task_id of this ScheduleTaskDetail.

        任务ID。

        :return: The task_id of this ScheduleTaskDetail.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ScheduleTaskDetail.

        任务ID。

        :param task_id: The task_id of this ScheduleTaskDetail.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        r"""Gets the task_name of this ScheduleTaskDetail.

        任务名称。

        :return: The task_name of this ScheduleTaskDetail.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        r"""Sets the task_name of this ScheduleTaskDetail.

        任务名称。

        :param task_name: The task_name of this ScheduleTaskDetail.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def status(self):
        r"""Gets the status of this ScheduleTaskDetail.

        任务状态。

        :return: The status of this ScheduleTaskDetail.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ScheduleTaskDetail.

        任务状态。

        :param status: The status of this ScheduleTaskDetail.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this ScheduleTaskDetail.

        任务创建时间,格式为yyyy-mm-ddThh:mm:ssZ。

        :return: The create_time of this ScheduleTaskDetail.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ScheduleTaskDetail.

        任务创建时间,格式为yyyy-mm-ddThh:mm:ssZ。

        :param create_time: The create_time of this ScheduleTaskDetail.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ScheduleTaskDetail.

        任务开始时间,格式为yyyy-mm-ddThh:mm:ssZ。

        :return: The start_time of this ScheduleTaskDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ScheduleTaskDetail.

        任务开始时间,格式为yyyy-mm-ddThh:mm:ssZ。

        :param start_time: The start_time of this ScheduleTaskDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ScheduleTaskDetail.

        实例ID。

        :return: The instance_id of this ScheduleTaskDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ScheduleTaskDetail.

        实例ID。

        :param instance_id: The instance_id of this ScheduleTaskDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this ScheduleTaskDetail.

        实例名称。

        :return: The instance_name of this ScheduleTaskDetail.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this ScheduleTaskDetail.

        实例名称。

        :param instance_name: The instance_name of this ScheduleTaskDetail.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def task_content(self):
        r"""Gets the task_content of this ScheduleTaskDetail.

        任务信息。

        :return: The task_content of this ScheduleTaskDetail.
        :rtype: object
        """
        return self._task_content

    @task_content.setter
    def task_content(self, task_content):
        r"""Sets the task_content of this ScheduleTaskDetail.

        任务信息。

        :param task_content: The task_content of this ScheduleTaskDetail.
        :type task_content: object
        """
        self._task_content = task_content

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
        if not isinstance(other, ScheduleTaskDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
