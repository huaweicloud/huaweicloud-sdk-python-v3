# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDispatchesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dispatch_id': 'str',
        'task_id': 'str',
        'start_datetime': 'int',
        'period': 'str',
        'dispatch_interval': 'int',
        'created_date': 'int',
        'last_modified_date': 'int',
        'remark': 'str',
        'use_quartz_cron': 'bool',
        'cron': 'str'
    }

    attribute_map = {
        'dispatch_id': 'dispatch_id',
        'task_id': 'task_id',
        'start_datetime': 'start_datetime',
        'period': 'period',
        'dispatch_interval': 'dispatch_interval',
        'created_date': 'created_date',
        'last_modified_date': 'last_modified_date',
        'remark': 'remark',
        'use_quartz_cron': 'use_quartz_cron',
        'cron': 'cron'
    }

    def __init__(self, dispatch_id=None, task_id=None, start_datetime=None, period=None, dispatch_interval=None, created_date=None, last_modified_date=None, remark=None, use_quartz_cron=None, cron=None):
        """CreateDispatchesResponse

        The model defined in huaweicloud sdk

        :param dispatch_id: 调度计划ID
        :type dispatch_id: str
        :param task_id: 调度计划关联的任务ID
        :type task_id: str
        :param start_datetime: 调度计划的执行开始时间
        :type start_datetime: int
        :param period: 调度计划执行周期的时间单位，当使用cron表达式时，为空 - MIN (分钟) - HOUR (小时) - DAY (日) - WEEK (周) - MON (月)
        :type period: str
        :param dispatch_interval: 调度计划的执行间隔时间周期
        :type dispatch_interval: int
        :param created_date: 调度计划的创建时间
        :type created_date: int
        :param last_modified_date: 调度计划最近一次的修改时间
        :type last_modified_date: int
        :param remark: 调度计划的备注信息
        :type remark: str
        :param use_quartz_cron: 调度计划是否使用cron表达式，允许如下值： - true (使用cron表达式) - false (不使用cron表达式)
        :type use_quartz_cron: bool
        :param cron: 调度计划的cron表达式
        :type cron: str
        """
        
        super(CreateDispatchesResponse, self).__init__()

        self._dispatch_id = None
        self._task_id = None
        self._start_datetime = None
        self._period = None
        self._dispatch_interval = None
        self._created_date = None
        self._last_modified_date = None
        self._remark = None
        self._use_quartz_cron = None
        self._cron = None
        self.discriminator = None

        if dispatch_id is not None:
            self.dispatch_id = dispatch_id
        if task_id is not None:
            self.task_id = task_id
        if start_datetime is not None:
            self.start_datetime = start_datetime
        if period is not None:
            self.period = period
        if dispatch_interval is not None:
            self.dispatch_interval = dispatch_interval
        if created_date is not None:
            self.created_date = created_date
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if remark is not None:
            self.remark = remark
        if use_quartz_cron is not None:
            self.use_quartz_cron = use_quartz_cron
        if cron is not None:
            self.cron = cron

    @property
    def dispatch_id(self):
        """Gets the dispatch_id of this CreateDispatchesResponse.

        调度计划ID

        :return: The dispatch_id of this CreateDispatchesResponse.
        :rtype: str
        """
        return self._dispatch_id

    @dispatch_id.setter
    def dispatch_id(self, dispatch_id):
        """Sets the dispatch_id of this CreateDispatchesResponse.

        调度计划ID

        :param dispatch_id: The dispatch_id of this CreateDispatchesResponse.
        :type dispatch_id: str
        """
        self._dispatch_id = dispatch_id

    @property
    def task_id(self):
        """Gets the task_id of this CreateDispatchesResponse.

        调度计划关联的任务ID

        :return: The task_id of this CreateDispatchesResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CreateDispatchesResponse.

        调度计划关联的任务ID

        :param task_id: The task_id of this CreateDispatchesResponse.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def start_datetime(self):
        """Gets the start_datetime of this CreateDispatchesResponse.

        调度计划的执行开始时间

        :return: The start_datetime of this CreateDispatchesResponse.
        :rtype: int
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        """Sets the start_datetime of this CreateDispatchesResponse.

        调度计划的执行开始时间

        :param start_datetime: The start_datetime of this CreateDispatchesResponse.
        :type start_datetime: int
        """
        self._start_datetime = start_datetime

    @property
    def period(self):
        """Gets the period of this CreateDispatchesResponse.

        调度计划执行周期的时间单位，当使用cron表达式时，为空 - MIN (分钟) - HOUR (小时) - DAY (日) - WEEK (周) - MON (月)

        :return: The period of this CreateDispatchesResponse.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this CreateDispatchesResponse.

        调度计划执行周期的时间单位，当使用cron表达式时，为空 - MIN (分钟) - HOUR (小时) - DAY (日) - WEEK (周) - MON (月)

        :param period: The period of this CreateDispatchesResponse.
        :type period: str
        """
        self._period = period

    @property
    def dispatch_interval(self):
        """Gets the dispatch_interval of this CreateDispatchesResponse.

        调度计划的执行间隔时间周期

        :return: The dispatch_interval of this CreateDispatchesResponse.
        :rtype: int
        """
        return self._dispatch_interval

    @dispatch_interval.setter
    def dispatch_interval(self, dispatch_interval):
        """Sets the dispatch_interval of this CreateDispatchesResponse.

        调度计划的执行间隔时间周期

        :param dispatch_interval: The dispatch_interval of this CreateDispatchesResponse.
        :type dispatch_interval: int
        """
        self._dispatch_interval = dispatch_interval

    @property
    def created_date(self):
        """Gets the created_date of this CreateDispatchesResponse.

        调度计划的创建时间

        :return: The created_date of this CreateDispatchesResponse.
        :rtype: int
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this CreateDispatchesResponse.

        调度计划的创建时间

        :param created_date: The created_date of this CreateDispatchesResponse.
        :type created_date: int
        """
        self._created_date = created_date

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this CreateDispatchesResponse.

        调度计划最近一次的修改时间

        :return: The last_modified_date of this CreateDispatchesResponse.
        :rtype: int
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this CreateDispatchesResponse.

        调度计划最近一次的修改时间

        :param last_modified_date: The last_modified_date of this CreateDispatchesResponse.
        :type last_modified_date: int
        """
        self._last_modified_date = last_modified_date

    @property
    def remark(self):
        """Gets the remark of this CreateDispatchesResponse.

        调度计划的备注信息

        :return: The remark of this CreateDispatchesResponse.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateDispatchesResponse.

        调度计划的备注信息

        :param remark: The remark of this CreateDispatchesResponse.
        :type remark: str
        """
        self._remark = remark

    @property
    def use_quartz_cron(self):
        """Gets the use_quartz_cron of this CreateDispatchesResponse.

        调度计划是否使用cron表达式，允许如下值： - true (使用cron表达式) - false (不使用cron表达式)

        :return: The use_quartz_cron of this CreateDispatchesResponse.
        :rtype: bool
        """
        return self._use_quartz_cron

    @use_quartz_cron.setter
    def use_quartz_cron(self, use_quartz_cron):
        """Sets the use_quartz_cron of this CreateDispatchesResponse.

        调度计划是否使用cron表达式，允许如下值： - true (使用cron表达式) - false (不使用cron表达式)

        :param use_quartz_cron: The use_quartz_cron of this CreateDispatchesResponse.
        :type use_quartz_cron: bool
        """
        self._use_quartz_cron = use_quartz_cron

    @property
    def cron(self):
        """Gets the cron of this CreateDispatchesResponse.

        调度计划的cron表达式

        :return: The cron of this CreateDispatchesResponse.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this CreateDispatchesResponse.

        调度计划的cron表达式

        :param cron: The cron of this CreateDispatchesResponse.
        :type cron: str
        """
        self._cron = cron

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
        if not isinstance(other, CreateDispatchesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
