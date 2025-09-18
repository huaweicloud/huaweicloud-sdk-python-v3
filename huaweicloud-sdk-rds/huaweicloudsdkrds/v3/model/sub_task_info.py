# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubTaskInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_task_name': 'str',
        'percent': 'str',
        'executed_time': 'str',
        'status': 'str',
        'remaining_time': 'str',
        'show_detail': 'bool'
    }

    attribute_map = {
        'sub_task_name': 'sub_task_name',
        'percent': 'percent',
        'executed_time': 'executed_time',
        'status': 'status',
        'remaining_time': 'remaining_time',
        'show_detail': 'show_detail'
    }

    def __init__(self, sub_task_name=None, percent=None, executed_time=None, status=None, remaining_time=None, show_detail=None):
        r"""SubTaskInfo

        The model defined in huaweicloud sdk

        :param sub_task_name: 子任务名
        :type sub_task_name: str
        :param percent: 子任务进度
        :type percent: str
        :param executed_time: 子任务执行时间
        :type executed_time: str
        :param status: 子任务状态
        :type status: str
        :param remaining_time: 子任务剩余预估时长
        :type remaining_time: str
        :param show_detail: 是否展示已恢复库表
        :type show_detail: bool
        """
        
        

        self._sub_task_name = None
        self._percent = None
        self._executed_time = None
        self._status = None
        self._remaining_time = None
        self._show_detail = None
        self.discriminator = None

        if sub_task_name is not None:
            self.sub_task_name = sub_task_name
        if percent is not None:
            self.percent = percent
        if executed_time is not None:
            self.executed_time = executed_time
        if status is not None:
            self.status = status
        if remaining_time is not None:
            self.remaining_time = remaining_time
        if show_detail is not None:
            self.show_detail = show_detail

    @property
    def sub_task_name(self):
        r"""Gets the sub_task_name of this SubTaskInfo.

        子任务名

        :return: The sub_task_name of this SubTaskInfo.
        :rtype: str
        """
        return self._sub_task_name

    @sub_task_name.setter
    def sub_task_name(self, sub_task_name):
        r"""Sets the sub_task_name of this SubTaskInfo.

        子任务名

        :param sub_task_name: The sub_task_name of this SubTaskInfo.
        :type sub_task_name: str
        """
        self._sub_task_name = sub_task_name

    @property
    def percent(self):
        r"""Gets the percent of this SubTaskInfo.

        子任务进度

        :return: The percent of this SubTaskInfo.
        :rtype: str
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        r"""Sets the percent of this SubTaskInfo.

        子任务进度

        :param percent: The percent of this SubTaskInfo.
        :type percent: str
        """
        self._percent = percent

    @property
    def executed_time(self):
        r"""Gets the executed_time of this SubTaskInfo.

        子任务执行时间

        :return: The executed_time of this SubTaskInfo.
        :rtype: str
        """
        return self._executed_time

    @executed_time.setter
    def executed_time(self, executed_time):
        r"""Sets the executed_time of this SubTaskInfo.

        子任务执行时间

        :param executed_time: The executed_time of this SubTaskInfo.
        :type executed_time: str
        """
        self._executed_time = executed_time

    @property
    def status(self):
        r"""Gets the status of this SubTaskInfo.

        子任务状态

        :return: The status of this SubTaskInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SubTaskInfo.

        子任务状态

        :param status: The status of this SubTaskInfo.
        :type status: str
        """
        self._status = status

    @property
    def remaining_time(self):
        r"""Gets the remaining_time of this SubTaskInfo.

        子任务剩余预估时长

        :return: The remaining_time of this SubTaskInfo.
        :rtype: str
        """
        return self._remaining_time

    @remaining_time.setter
    def remaining_time(self, remaining_time):
        r"""Sets the remaining_time of this SubTaskInfo.

        子任务剩余预估时长

        :param remaining_time: The remaining_time of this SubTaskInfo.
        :type remaining_time: str
        """
        self._remaining_time = remaining_time

    @property
    def show_detail(self):
        r"""Gets the show_detail of this SubTaskInfo.

        是否展示已恢复库表

        :return: The show_detail of this SubTaskInfo.
        :rtype: bool
        """
        return self._show_detail

    @show_detail.setter
    def show_detail(self, show_detail):
        r"""Sets the show_detail of this SubTaskInfo.

        是否展示已恢复库表

        :param show_detail: The show_detail of this SubTaskInfo.
        :type show_detail: bool
        """
        self._show_detail = show_detail

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
        if not isinstance(other, SubTaskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
