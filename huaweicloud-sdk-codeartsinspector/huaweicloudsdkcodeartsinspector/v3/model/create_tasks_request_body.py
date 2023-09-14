# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTasksRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_name': 'str',
        'url': 'str',
        'task_type': 'str',
        'timer': 'str',
        'trigger_time': 'str',
        'task_period': 'str',
        'task_config': 'TaskSettingsTaskConfig'
    }

    attribute_map = {
        'task_name': 'task_name',
        'url': 'url',
        'task_type': 'task_type',
        'timer': 'timer',
        'trigger_time': 'trigger_time',
        'task_period': 'task_period',
        'task_config': 'task_config'
    }

    def __init__(self, task_name=None, url=None, task_type=None, timer=None, trigger_time=None, task_period=None, task_config=None):
        """CreateTasksRequestBody

        The model defined in huaweicloud sdk

        :param task_name: 任务名称
        :type task_name: str
        :param url: 待扫描的目标网址
        :type url: str
        :param task_type: 扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 
        :type task_type: str
        :param timer: 普通任务的定时启动时间
        :type timer: str
        :param trigger_time: 监测任务的定时触发时间
        :type trigger_time: str
        :param task_period: 监测任务的定时触发周期:   * everyday - 每日   * threedays - 每三天   * everyweek - 每星期   * everymonth - 每月 
        :type task_period: str
        :param task_config: 
        :type task_config: :class:`huaweicloudsdkcodeartsinspector.v3.TaskSettingsTaskConfig`
        """
        
        

        self._task_name = None
        self._url = None
        self._task_type = None
        self._timer = None
        self._trigger_time = None
        self._task_period = None
        self._task_config = None
        self.discriminator = None

        self.task_name = task_name
        self.url = url
        if task_type is not None:
            self.task_type = task_type
        if timer is not None:
            self.timer = timer
        if trigger_time is not None:
            self.trigger_time = trigger_time
        if task_period is not None:
            self.task_period = task_period
        if task_config is not None:
            self.task_config = task_config

    @property
    def task_name(self):
        """Gets the task_name of this CreateTasksRequestBody.

        任务名称

        :return: The task_name of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateTasksRequestBody.

        任务名称

        :param task_name: The task_name of this CreateTasksRequestBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def url(self):
        """Gets the url of this CreateTasksRequestBody.

        待扫描的目标网址

        :return: The url of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateTasksRequestBody.

        待扫描的目标网址

        :param url: The url of this CreateTasksRequestBody.
        :type url: str
        """
        self._url = url

    @property
    def task_type(self):
        """Gets the task_type of this CreateTasksRequestBody.

        扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 

        :return: The task_type of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this CreateTasksRequestBody.

        扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 

        :param task_type: The task_type of this CreateTasksRequestBody.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def timer(self):
        """Gets the timer of this CreateTasksRequestBody.

        普通任务的定时启动时间

        :return: The timer of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._timer

    @timer.setter
    def timer(self, timer):
        """Sets the timer of this CreateTasksRequestBody.

        普通任务的定时启动时间

        :param timer: The timer of this CreateTasksRequestBody.
        :type timer: str
        """
        self._timer = timer

    @property
    def trigger_time(self):
        """Gets the trigger_time of this CreateTasksRequestBody.

        监测任务的定时触发时间

        :return: The trigger_time of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._trigger_time

    @trigger_time.setter
    def trigger_time(self, trigger_time):
        """Sets the trigger_time of this CreateTasksRequestBody.

        监测任务的定时触发时间

        :param trigger_time: The trigger_time of this CreateTasksRequestBody.
        :type trigger_time: str
        """
        self._trigger_time = trigger_time

    @property
    def task_period(self):
        """Gets the task_period of this CreateTasksRequestBody.

        监测任务的定时触发周期:   * everyday - 每日   * threedays - 每三天   * everyweek - 每星期   * everymonth - 每月 

        :return: The task_period of this CreateTasksRequestBody.
        :rtype: str
        """
        return self._task_period

    @task_period.setter
    def task_period(self, task_period):
        """Sets the task_period of this CreateTasksRequestBody.

        监测任务的定时触发周期:   * everyday - 每日   * threedays - 每三天   * everyweek - 每星期   * everymonth - 每月 

        :param task_period: The task_period of this CreateTasksRequestBody.
        :type task_period: str
        """
        self._task_period = task_period

    @property
    def task_config(self):
        """Gets the task_config of this CreateTasksRequestBody.

        :return: The task_config of this CreateTasksRequestBody.
        :rtype: :class:`huaweicloudsdkcodeartsinspector.v3.TaskSettingsTaskConfig`
        """
        return self._task_config

    @task_config.setter
    def task_config(self, task_config):
        """Sets the task_config of this CreateTasksRequestBody.

        :param task_config: The task_config of this CreateTasksRequestBody.
        :type task_config: :class:`huaweicloudsdkcodeartsinspector.v3.TaskSettingsTaskConfig`
        """
        self._task_config = task_config

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
        if not isinstance(other, CreateTasksRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
