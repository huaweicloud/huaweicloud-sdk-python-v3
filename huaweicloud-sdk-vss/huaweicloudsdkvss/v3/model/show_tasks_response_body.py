# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTasksResponseBody:

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
        'task_id': 'str',
        'domain_name': 'str',
        'task_settings': 'TaskSettings',
        'create_time': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'task_status': 'str',
        'schedule_status': 'str',
        'progress': 'int',
        'reason': 'str',
        'pack_num': 'int',
        'score': 'int',
        'safe_level': 'str',
        'statistics': 'VulnsLevel'
    }

    attribute_map = {
        'task_name': 'task_name',
        'url': 'url',
        'task_type': 'task_type',
        'task_id': 'task_id',
        'domain_name': 'domain_name',
        'task_settings': 'task_settings',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'task_status': 'task_status',
        'schedule_status': 'schedule_status',
        'progress': 'progress',
        'reason': 'reason',
        'pack_num': 'pack_num',
        'score': 'score',
        'safe_level': 'safe_level',
        'statistics': 'statistics'
    }

    def __init__(self, task_name=None, url=None, task_type=None, task_id=None, domain_name=None, task_settings=None, create_time=None, start_time=None, end_time=None, task_status=None, schedule_status=None, progress=None, reason=None, pack_num=None, score=None, safe_level=None, statistics=None):
        """ShowTasksResponseBody

        The model defined in huaweicloud sdk

        :param task_name: 任务名称
        :type task_name: str
        :param url: 待扫描的目标网址
        :type url: str
        :param task_type: 扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 
        :type task_type: str
        :param task_id: 任务ID
        :type task_id: str
        :param domain_name: 域名
        :type domain_name: str
        :param task_settings: 
        :type task_settings: :class:`huaweicloudsdkvss.v3.TaskSettings`
        :param create_time: 创建任务的时间
        :type create_time: str
        :param start_time: 任务启动的时间
        :type start_time: str
        :param end_time: 任务结束的时间
        :type end_time: str
        :param task_status: 任务状态:   * running - 正在运行   * success - 成功   * canceled - 已取消   * waiting - 正在等待   * failure - 失败 
        :type task_status: str
        :param schedule_status: 监测任务状态:   * running - 正在运行   * waiting - 正在等待   * finished - 已完成 
        :type schedule_status: str
        :param progress: 任务进度
        :type progress: int
        :param reason: 任务状态描述
        :type reason: str
        :param pack_num: 包总数
        :type pack_num: int
        :param score: 安全分数
        :type score: int
        :param safe_level: 安全等级:   * safety - 安全   * average - 中风险   * highrisk - 高风险 
        :type safe_level: str
        :param statistics: 
        :type statistics: :class:`huaweicloudsdkvss.v3.VulnsLevel`
        """
        
        

        self._task_name = None
        self._url = None
        self._task_type = None
        self._task_id = None
        self._domain_name = None
        self._task_settings = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._task_status = None
        self._schedule_status = None
        self._progress = None
        self._reason = None
        self._pack_num = None
        self._score = None
        self._safe_level = None
        self._statistics = None
        self.discriminator = None

        self.task_name = task_name
        self.url = url
        if task_type is not None:
            self.task_type = task_type
        if task_id is not None:
            self.task_id = task_id
        if domain_name is not None:
            self.domain_name = domain_name
        if task_settings is not None:
            self.task_settings = task_settings
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if task_status is not None:
            self.task_status = task_status
        if schedule_status is not None:
            self.schedule_status = schedule_status
        if progress is not None:
            self.progress = progress
        if reason is not None:
            self.reason = reason
        if pack_num is not None:
            self.pack_num = pack_num
        if score is not None:
            self.score = score
        if safe_level is not None:
            self.safe_level = safe_level
        if statistics is not None:
            self.statistics = statistics

    @property
    def task_name(self):
        """Gets the task_name of this ShowTasksResponseBody.

        任务名称

        :return: The task_name of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this ShowTasksResponseBody.

        任务名称

        :param task_name: The task_name of this ShowTasksResponseBody.
        :type task_name: str
        """
        self._task_name = task_name

    @property
    def url(self):
        """Gets the url of this ShowTasksResponseBody.

        待扫描的目标网址

        :return: The url of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ShowTasksResponseBody.

        待扫描的目标网址

        :param url: The url of this ShowTasksResponseBody.
        :type url: str
        """
        self._url = url

    @property
    def task_type(self):
        """Gets the task_type of this ShowTasksResponseBody.

        扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 

        :return: The task_type of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this ShowTasksResponseBody.

        扫描任务类型:   * normal - 普通任务   * monitor - 监测任务 

        :param task_type: The task_type of this ShowTasksResponseBody.
        :type task_type: str
        """
        self._task_type = task_type

    @property
    def task_id(self):
        """Gets the task_id of this ShowTasksResponseBody.

        任务ID

        :return: The task_id of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowTasksResponseBody.

        任务ID

        :param task_id: The task_id of this ShowTasksResponseBody.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def domain_name(self):
        """Gets the domain_name of this ShowTasksResponseBody.

        域名

        :return: The domain_name of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this ShowTasksResponseBody.

        域名

        :param domain_name: The domain_name of this ShowTasksResponseBody.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def task_settings(self):
        """Gets the task_settings of this ShowTasksResponseBody.

        :return: The task_settings of this ShowTasksResponseBody.
        :rtype: :class:`huaweicloudsdkvss.v3.TaskSettings`
        """
        return self._task_settings

    @task_settings.setter
    def task_settings(self, task_settings):
        """Sets the task_settings of this ShowTasksResponseBody.

        :param task_settings: The task_settings of this ShowTasksResponseBody.
        :type task_settings: :class:`huaweicloudsdkvss.v3.TaskSettings`
        """
        self._task_settings = task_settings

    @property
    def create_time(self):
        """Gets the create_time of this ShowTasksResponseBody.

        创建任务的时间

        :return: The create_time of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowTasksResponseBody.

        创建任务的时间

        :param create_time: The create_time of this ShowTasksResponseBody.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def start_time(self):
        """Gets the start_time of this ShowTasksResponseBody.

        任务启动的时间

        :return: The start_time of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ShowTasksResponseBody.

        任务启动的时间

        :param start_time: The start_time of this ShowTasksResponseBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowTasksResponseBody.

        任务结束的时间

        :return: The end_time of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowTasksResponseBody.

        任务结束的时间

        :param end_time: The end_time of this ShowTasksResponseBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def task_status(self):
        """Gets the task_status of this ShowTasksResponseBody.

        任务状态:   * running - 正在运行   * success - 成功   * canceled - 已取消   * waiting - 正在等待   * failure - 失败 

        :return: The task_status of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._task_status

    @task_status.setter
    def task_status(self, task_status):
        """Sets the task_status of this ShowTasksResponseBody.

        任务状态:   * running - 正在运行   * success - 成功   * canceled - 已取消   * waiting - 正在等待   * failure - 失败 

        :param task_status: The task_status of this ShowTasksResponseBody.
        :type task_status: str
        """
        self._task_status = task_status

    @property
    def schedule_status(self):
        """Gets the schedule_status of this ShowTasksResponseBody.

        监测任务状态:   * running - 正在运行   * waiting - 正在等待   * finished - 已完成 

        :return: The schedule_status of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._schedule_status

    @schedule_status.setter
    def schedule_status(self, schedule_status):
        """Sets the schedule_status of this ShowTasksResponseBody.

        监测任务状态:   * running - 正在运行   * waiting - 正在等待   * finished - 已完成 

        :param schedule_status: The schedule_status of this ShowTasksResponseBody.
        :type schedule_status: str
        """
        self._schedule_status = schedule_status

    @property
    def progress(self):
        """Gets the progress of this ShowTasksResponseBody.

        任务进度

        :return: The progress of this ShowTasksResponseBody.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ShowTasksResponseBody.

        任务进度

        :param progress: The progress of this ShowTasksResponseBody.
        :type progress: int
        """
        self._progress = progress

    @property
    def reason(self):
        """Gets the reason of this ShowTasksResponseBody.

        任务状态描述

        :return: The reason of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ShowTasksResponseBody.

        任务状态描述

        :param reason: The reason of this ShowTasksResponseBody.
        :type reason: str
        """
        self._reason = reason

    @property
    def pack_num(self):
        """Gets the pack_num of this ShowTasksResponseBody.

        包总数

        :return: The pack_num of this ShowTasksResponseBody.
        :rtype: int
        """
        return self._pack_num

    @pack_num.setter
    def pack_num(self, pack_num):
        """Sets the pack_num of this ShowTasksResponseBody.

        包总数

        :param pack_num: The pack_num of this ShowTasksResponseBody.
        :type pack_num: int
        """
        self._pack_num = pack_num

    @property
    def score(self):
        """Gets the score of this ShowTasksResponseBody.

        安全分数

        :return: The score of this ShowTasksResponseBody.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ShowTasksResponseBody.

        安全分数

        :param score: The score of this ShowTasksResponseBody.
        :type score: int
        """
        self._score = score

    @property
    def safe_level(self):
        """Gets the safe_level of this ShowTasksResponseBody.

        安全等级:   * safety - 安全   * average - 中风险   * highrisk - 高风险 

        :return: The safe_level of this ShowTasksResponseBody.
        :rtype: str
        """
        return self._safe_level

    @safe_level.setter
    def safe_level(self, safe_level):
        """Sets the safe_level of this ShowTasksResponseBody.

        安全等级:   * safety - 安全   * average - 中风险   * highrisk - 高风险 

        :param safe_level: The safe_level of this ShowTasksResponseBody.
        :type safe_level: str
        """
        self._safe_level = safe_level

    @property
    def statistics(self):
        """Gets the statistics of this ShowTasksResponseBody.

        :return: The statistics of this ShowTasksResponseBody.
        :rtype: :class:`huaweicloudsdkvss.v3.VulnsLevel`
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this ShowTasksResponseBody.

        :param statistics: The statistics of this ShowTasksResponseBody.
        :type statistics: :class:`huaweicloudsdkvss.v3.VulnsLevel`
        """
        self._statistics = statistics

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
        if not isinstance(other, ShowTasksResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
