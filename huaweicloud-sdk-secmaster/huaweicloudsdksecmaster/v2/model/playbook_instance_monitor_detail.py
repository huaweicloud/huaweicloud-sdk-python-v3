# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlaybookInstanceMonitorDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_instance_run_num': 'int',
        'schedule_instance_run_num': 'int',
        'event_instance_run_num': 'int',
        'average_run_time': 'float',
        'min_run_time_instance': 'PlaybookInstanceRunStatistics',
        'max_run_time_instance': 'PlaybookInstanceRunStatistics',
        'total_instance_num': 'int',
        'success_instance_num': 'int',
        'fail_instance_num': 'int',
        'terminate_instance_num': 'int',
        'running_instance_num': 'int'
    }

    attribute_map = {
        'total_instance_run_num': 'total_instance_run_num',
        'schedule_instance_run_num': 'schedule_instance_run_num',
        'event_instance_run_num': 'event_instance_run_num',
        'average_run_time': 'average_run_time',
        'min_run_time_instance': 'min_run_time_instance',
        'max_run_time_instance': 'max_run_time_instance',
        'total_instance_num': 'total_instance_num',
        'success_instance_num': 'success_instance_num',
        'fail_instance_num': 'fail_instance_num',
        'terminate_instance_num': 'terminate_instance_num',
        'running_instance_num': 'running_instance_num'
    }

    def __init__(self, total_instance_run_num=None, schedule_instance_run_num=None, event_instance_run_num=None, average_run_time=None, min_run_time_instance=None, max_run_time_instance=None, total_instance_num=None, success_instance_num=None, fail_instance_num=None, terminate_instance_num=None, running_instance_num=None):
        r"""PlaybookInstanceMonitorDetail

        The model defined in huaweicloud sdk

        :param total_instance_run_num: 运行总次数
        :type total_instance_run_num: int
        :param schedule_instance_run_num: 定时触发执行次数
        :type schedule_instance_run_num: int
        :param event_instance_run_num: 时间触发执行次数
        :type event_instance_run_num: int
        :param average_run_time: 平均运行时间
        :type average_run_time: float
        :param min_run_time_instance: 
        :type min_run_time_instance: :class:`huaweicloudsdksecmaster.v2.PlaybookInstanceRunStatistics`
        :param max_run_time_instance: 
        :type max_run_time_instance: :class:`huaweicloudsdksecmaster.v2.PlaybookInstanceRunStatistics`
        :param total_instance_num: 剧本实例总数
        :type total_instance_num: int
        :param success_instance_num: 运行成功实例数量
        :type success_instance_num: int
        :param fail_instance_num: 运行失败实例数量
        :type fail_instance_num: int
        :param terminate_instance_num: 运行终止实例数量
        :type terminate_instance_num: int
        :param running_instance_num: 运行中实例数量
        :type running_instance_num: int
        """
        
        

        self._total_instance_run_num = None
        self._schedule_instance_run_num = None
        self._event_instance_run_num = None
        self._average_run_time = None
        self._min_run_time_instance = None
        self._max_run_time_instance = None
        self._total_instance_num = None
        self._success_instance_num = None
        self._fail_instance_num = None
        self._terminate_instance_num = None
        self._running_instance_num = None
        self.discriminator = None

        if total_instance_run_num is not None:
            self.total_instance_run_num = total_instance_run_num
        if schedule_instance_run_num is not None:
            self.schedule_instance_run_num = schedule_instance_run_num
        if event_instance_run_num is not None:
            self.event_instance_run_num = event_instance_run_num
        if average_run_time is not None:
            self.average_run_time = average_run_time
        if min_run_time_instance is not None:
            self.min_run_time_instance = min_run_time_instance
        if max_run_time_instance is not None:
            self.max_run_time_instance = max_run_time_instance
        if total_instance_num is not None:
            self.total_instance_num = total_instance_num
        if success_instance_num is not None:
            self.success_instance_num = success_instance_num
        if fail_instance_num is not None:
            self.fail_instance_num = fail_instance_num
        if terminate_instance_num is not None:
            self.terminate_instance_num = terminate_instance_num
        if running_instance_num is not None:
            self.running_instance_num = running_instance_num

    @property
    def total_instance_run_num(self):
        r"""Gets the total_instance_run_num of this PlaybookInstanceMonitorDetail.

        运行总次数

        :return: The total_instance_run_num of this PlaybookInstanceMonitorDetail.
        :rtype: int
        """
        return self._total_instance_run_num

    @total_instance_run_num.setter
    def total_instance_run_num(self, total_instance_run_num):
        r"""Sets the total_instance_run_num of this PlaybookInstanceMonitorDetail.

        运行总次数

        :param total_instance_run_num: The total_instance_run_num of this PlaybookInstanceMonitorDetail.
        :type total_instance_run_num: int
        """
        self._total_instance_run_num = total_instance_run_num

    @property
    def schedule_instance_run_num(self):
        r"""Gets the schedule_instance_run_num of this PlaybookInstanceMonitorDetail.

        定时触发执行次数

        :return: The schedule_instance_run_num of this PlaybookInstanceMonitorDetail.
        :rtype: int
        """
        return self._schedule_instance_run_num

    @schedule_instance_run_num.setter
    def schedule_instance_run_num(self, schedule_instance_run_num):
        r"""Sets the schedule_instance_run_num of this PlaybookInstanceMonitorDetail.

        定时触发执行次数

        :param schedule_instance_run_num: The schedule_instance_run_num of this PlaybookInstanceMonitorDetail.
        :type schedule_instance_run_num: int
        """
        self._schedule_instance_run_num = schedule_instance_run_num

    @property
    def event_instance_run_num(self):
        r"""Gets the event_instance_run_num of this PlaybookInstanceMonitorDetail.

        时间触发执行次数

        :return: The event_instance_run_num of this PlaybookInstanceMonitorDetail.
        :rtype: int
        """
        return self._event_instance_run_num

    @event_instance_run_num.setter
    def event_instance_run_num(self, event_instance_run_num):
        r"""Sets the event_instance_run_num of this PlaybookInstanceMonitorDetail.

        时间触发执行次数

        :param event_instance_run_num: The event_instance_run_num of this PlaybookInstanceMonitorDetail.
        :type event_instance_run_num: int
        """
        self._event_instance_run_num = event_instance_run_num

    @property
    def average_run_time(self):
        r"""Gets the average_run_time of this PlaybookInstanceMonitorDetail.

        平均运行时间

        :return: The average_run_time of this PlaybookInstanceMonitorDetail.
        :rtype: float
        """
        return self._average_run_time

    @average_run_time.setter
    def average_run_time(self, average_run_time):
        r"""Sets the average_run_time of this PlaybookInstanceMonitorDetail.

        平均运行时间

        :param average_run_time: The average_run_time of this PlaybookInstanceMonitorDetail.
        :type average_run_time: float
        """
        self._average_run_time = average_run_time

    @property
    def min_run_time_instance(self):
        r"""Gets the min_run_time_instance of this PlaybookInstanceMonitorDetail.

        :return: The min_run_time_instance of this PlaybookInstanceMonitorDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.PlaybookInstanceRunStatistics`
        """
        return self._min_run_time_instance

    @min_run_time_instance.setter
    def min_run_time_instance(self, min_run_time_instance):
        r"""Sets the min_run_time_instance of this PlaybookInstanceMonitorDetail.

        :param min_run_time_instance: The min_run_time_instance of this PlaybookInstanceMonitorDetail.
        :type min_run_time_instance: :class:`huaweicloudsdksecmaster.v2.PlaybookInstanceRunStatistics`
        """
        self._min_run_time_instance = min_run_time_instance

    @property
    def max_run_time_instance(self):
        r"""Gets the max_run_time_instance of this PlaybookInstanceMonitorDetail.

        :return: The max_run_time_instance of this PlaybookInstanceMonitorDetail.
        :rtype: :class:`huaweicloudsdksecmaster.v2.PlaybookInstanceRunStatistics`
        """
        return self._max_run_time_instance

    @max_run_time_instance.setter
    def max_run_time_instance(self, max_run_time_instance):
        r"""Sets the max_run_time_instance of this PlaybookInstanceMonitorDetail.

        :param max_run_time_instance: The max_run_time_instance of this PlaybookInstanceMonitorDetail.
        :type max_run_time_instance: :class:`huaweicloudsdksecmaster.v2.PlaybookInstanceRunStatistics`
        """
        self._max_run_time_instance = max_run_time_instance

    @property
    def total_instance_num(self):
        r"""Gets the total_instance_num of this PlaybookInstanceMonitorDetail.

        剧本实例总数

        :return: The total_instance_num of this PlaybookInstanceMonitorDetail.
        :rtype: int
        """
        return self._total_instance_num

    @total_instance_num.setter
    def total_instance_num(self, total_instance_num):
        r"""Sets the total_instance_num of this PlaybookInstanceMonitorDetail.

        剧本实例总数

        :param total_instance_num: The total_instance_num of this PlaybookInstanceMonitorDetail.
        :type total_instance_num: int
        """
        self._total_instance_num = total_instance_num

    @property
    def success_instance_num(self):
        r"""Gets the success_instance_num of this PlaybookInstanceMonitorDetail.

        运行成功实例数量

        :return: The success_instance_num of this PlaybookInstanceMonitorDetail.
        :rtype: int
        """
        return self._success_instance_num

    @success_instance_num.setter
    def success_instance_num(self, success_instance_num):
        r"""Sets the success_instance_num of this PlaybookInstanceMonitorDetail.

        运行成功实例数量

        :param success_instance_num: The success_instance_num of this PlaybookInstanceMonitorDetail.
        :type success_instance_num: int
        """
        self._success_instance_num = success_instance_num

    @property
    def fail_instance_num(self):
        r"""Gets the fail_instance_num of this PlaybookInstanceMonitorDetail.

        运行失败实例数量

        :return: The fail_instance_num of this PlaybookInstanceMonitorDetail.
        :rtype: int
        """
        return self._fail_instance_num

    @fail_instance_num.setter
    def fail_instance_num(self, fail_instance_num):
        r"""Sets the fail_instance_num of this PlaybookInstanceMonitorDetail.

        运行失败实例数量

        :param fail_instance_num: The fail_instance_num of this PlaybookInstanceMonitorDetail.
        :type fail_instance_num: int
        """
        self._fail_instance_num = fail_instance_num

    @property
    def terminate_instance_num(self):
        r"""Gets the terminate_instance_num of this PlaybookInstanceMonitorDetail.

        运行终止实例数量

        :return: The terminate_instance_num of this PlaybookInstanceMonitorDetail.
        :rtype: int
        """
        return self._terminate_instance_num

    @terminate_instance_num.setter
    def terminate_instance_num(self, terminate_instance_num):
        r"""Sets the terminate_instance_num of this PlaybookInstanceMonitorDetail.

        运行终止实例数量

        :param terminate_instance_num: The terminate_instance_num of this PlaybookInstanceMonitorDetail.
        :type terminate_instance_num: int
        """
        self._terminate_instance_num = terminate_instance_num

    @property
    def running_instance_num(self):
        r"""Gets the running_instance_num of this PlaybookInstanceMonitorDetail.

        运行中实例数量

        :return: The running_instance_num of this PlaybookInstanceMonitorDetail.
        :rtype: int
        """
        return self._running_instance_num

    @running_instance_num.setter
    def running_instance_num(self, running_instance_num):
        r"""Sets the running_instance_num of this PlaybookInstanceMonitorDetail.

        运行中实例数量

        :param running_instance_num: The running_instance_num of this PlaybookInstanceMonitorDetail.
        :type running_instance_num: int
        """
        self._running_instance_num = running_instance_num

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
        if not isinstance(other, PlaybookInstanceMonitorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
