# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueuePlanEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'plan_name': 'str',
        'target_cu': 'int',
        'start_hour': 'int',
        'start_minute': 'int',
        'repeat_day': 'list[str]',
        'valid_date_begin': 'int',
        'valid_date_end': 'int',
        'activate': 'bool',
        'last_execute_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'plan_name': 'plan_name',
        'target_cu': 'target_cu',
        'start_hour': 'start_hour',
        'start_minute': 'start_minute',
        'repeat_day': 'repeat_day',
        'valid_date_begin': 'valid_date_begin',
        'valid_date_end': 'valid_date_end',
        'activate': 'activate',
        'last_execute_time': 'last_execute_time'
    }

    def __init__(self, id=None, plan_name=None, target_cu=None, start_hour=None, start_minute=None, repeat_day=None, valid_date_begin=None, valid_date_end=None, activate=None, last_execute_time=None):
        """QueuePlanEntity

        The model defined in huaweicloud sdk

        :param id: 扩缩容计划的ID编号。
        :type id: int
        :param plan_name: 扩缩容计划的名称。
        :type plan_name: str
        :param target_cu: 队列扩缩容计划的目标CU值。
        :type target_cu: int
        :param start_hour: 队列扩缩容计划的起始时（24小时制）。
        :type start_hour: int
        :param start_minute: 定时扩缩容计划的起始分。
        :type start_minute: int
        :param repeat_day: 定时扩缩容计划的重复周期规律
        :type repeat_day: list[str]
        :param valid_date_begin: 有效期开始时间（13位时间戳）
        :type valid_date_begin: int
        :param valid_date_end: 有效期结束时间（13位时间戳） 
        :type valid_date_end: int
        :param activate: 当前的扩缩容计划是否激活。
        :type activate: bool
        :param last_execute_time: 当前扩缩容计划最近一次执行的时间。
        :type last_execute_time: int
        """
        
        

        self._id = None
        self._plan_name = None
        self._target_cu = None
        self._start_hour = None
        self._start_minute = None
        self._repeat_day = None
        self._valid_date_begin = None
        self._valid_date_end = None
        self._activate = None
        self._last_execute_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if plan_name is not None:
            self.plan_name = plan_name
        if target_cu is not None:
            self.target_cu = target_cu
        if start_hour is not None:
            self.start_hour = start_hour
        if start_minute is not None:
            self.start_minute = start_minute
        self.repeat_day = repeat_day
        if valid_date_begin is not None:
            self.valid_date_begin = valid_date_begin
        if valid_date_end is not None:
            self.valid_date_end = valid_date_end
        if activate is not None:
            self.activate = activate
        if last_execute_time is not None:
            self.last_execute_time = last_execute_time

    @property
    def id(self):
        """Gets the id of this QueuePlanEntity.

        扩缩容计划的ID编号。

        :return: The id of this QueuePlanEntity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueuePlanEntity.

        扩缩容计划的ID编号。

        :param id: The id of this QueuePlanEntity.
        :type id: int
        """
        self._id = id

    @property
    def plan_name(self):
        """Gets the plan_name of this QueuePlanEntity.

        扩缩容计划的名称。

        :return: The plan_name of this QueuePlanEntity.
        :rtype: str
        """
        return self._plan_name

    @plan_name.setter
    def plan_name(self, plan_name):
        """Sets the plan_name of this QueuePlanEntity.

        扩缩容计划的名称。

        :param plan_name: The plan_name of this QueuePlanEntity.
        :type plan_name: str
        """
        self._plan_name = plan_name

    @property
    def target_cu(self):
        """Gets the target_cu of this QueuePlanEntity.

        队列扩缩容计划的目标CU值。

        :return: The target_cu of this QueuePlanEntity.
        :rtype: int
        """
        return self._target_cu

    @target_cu.setter
    def target_cu(self, target_cu):
        """Sets the target_cu of this QueuePlanEntity.

        队列扩缩容计划的目标CU值。

        :param target_cu: The target_cu of this QueuePlanEntity.
        :type target_cu: int
        """
        self._target_cu = target_cu

    @property
    def start_hour(self):
        """Gets the start_hour of this QueuePlanEntity.

        队列扩缩容计划的起始时（24小时制）。

        :return: The start_hour of this QueuePlanEntity.
        :rtype: int
        """
        return self._start_hour

    @start_hour.setter
    def start_hour(self, start_hour):
        """Sets the start_hour of this QueuePlanEntity.

        队列扩缩容计划的起始时（24小时制）。

        :param start_hour: The start_hour of this QueuePlanEntity.
        :type start_hour: int
        """
        self._start_hour = start_hour

    @property
    def start_minute(self):
        """Gets the start_minute of this QueuePlanEntity.

        定时扩缩容计划的起始分。

        :return: The start_minute of this QueuePlanEntity.
        :rtype: int
        """
        return self._start_minute

    @start_minute.setter
    def start_minute(self, start_minute):
        """Sets the start_minute of this QueuePlanEntity.

        定时扩缩容计划的起始分。

        :param start_minute: The start_minute of this QueuePlanEntity.
        :type start_minute: int
        """
        self._start_minute = start_minute

    @property
    def repeat_day(self):
        """Gets the repeat_day of this QueuePlanEntity.

        定时扩缩容计划的重复周期规律

        :return: The repeat_day of this QueuePlanEntity.
        :rtype: list[str]
        """
        return self._repeat_day

    @repeat_day.setter
    def repeat_day(self, repeat_day):
        """Sets the repeat_day of this QueuePlanEntity.

        定时扩缩容计划的重复周期规律

        :param repeat_day: The repeat_day of this QueuePlanEntity.
        :type repeat_day: list[str]
        """
        self._repeat_day = repeat_day

    @property
    def valid_date_begin(self):
        """Gets the valid_date_begin of this QueuePlanEntity.

        有效期开始时间（13位时间戳）

        :return: The valid_date_begin of this QueuePlanEntity.
        :rtype: int
        """
        return self._valid_date_begin

    @valid_date_begin.setter
    def valid_date_begin(self, valid_date_begin):
        """Sets the valid_date_begin of this QueuePlanEntity.

        有效期开始时间（13位时间戳）

        :param valid_date_begin: The valid_date_begin of this QueuePlanEntity.
        :type valid_date_begin: int
        """
        self._valid_date_begin = valid_date_begin

    @property
    def valid_date_end(self):
        """Gets the valid_date_end of this QueuePlanEntity.

        有效期结束时间（13位时间戳） 

        :return: The valid_date_end of this QueuePlanEntity.
        :rtype: int
        """
        return self._valid_date_end

    @valid_date_end.setter
    def valid_date_end(self, valid_date_end):
        """Sets the valid_date_end of this QueuePlanEntity.

        有效期结束时间（13位时间戳） 

        :param valid_date_end: The valid_date_end of this QueuePlanEntity.
        :type valid_date_end: int
        """
        self._valid_date_end = valid_date_end

    @property
    def activate(self):
        """Gets the activate of this QueuePlanEntity.

        当前的扩缩容计划是否激活。

        :return: The activate of this QueuePlanEntity.
        :rtype: bool
        """
        return self._activate

    @activate.setter
    def activate(self, activate):
        """Sets the activate of this QueuePlanEntity.

        当前的扩缩容计划是否激活。

        :param activate: The activate of this QueuePlanEntity.
        :type activate: bool
        """
        self._activate = activate

    @property
    def last_execute_time(self):
        """Gets the last_execute_time of this QueuePlanEntity.

        当前扩缩容计划最近一次执行的时间。

        :return: The last_execute_time of this QueuePlanEntity.
        :rtype: int
        """
        return self._last_execute_time

    @last_execute_time.setter
    def last_execute_time(self, last_execute_time):
        """Sets the last_execute_time of this QueuePlanEntity.

        当前扩缩容计划最近一次执行的时间。

        :param last_execute_time: The last_execute_time of this QueuePlanEntity.
        :type last_execute_time: int
        """
        self._last_execute_time = last_execute_time

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
        if not isinstance(other, QueuePlanEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
