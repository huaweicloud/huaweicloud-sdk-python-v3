# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOperationalDataCurrentMonthUsingResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_success_rate': 'int',
        'running_tasks': 'int',
        'total_alerts': 'int',
        'total_days': 'int',
        'total_runs': 'int',
        'total_tasks': 'int',
        'work_item_count': 'int'
    }

    attribute_map = {
        'alert_success_rate': 'alert_success_rate',
        'running_tasks': 'running_tasks',
        'total_alerts': 'total_alerts',
        'total_days': 'total_days',
        'total_runs': 'total_runs',
        'total_tasks': 'total_tasks',
        'work_item_count': 'work_item_count'
    }

    def __init__(self, alert_success_rate=None, running_tasks=None, total_alerts=None, total_days=None, total_runs=None, total_tasks=None, work_item_count=None):
        r"""ShowOperationalDataCurrentMonthUsingResponse

        The model defined in huaweicloud sdk

        :param alert_success_rate: 告警成功比率，恒为1
        :type alert_success_rate: int
        :param running_tasks: 正在运行的任务个数
        :type running_tasks: int
        :param total_alerts: 总告警数
        :type total_alerts: int
        :param total_days: 总运行天数
        :type total_days: int
        :param total_runs: 总运行个数
        :type total_runs: int
        :param total_tasks: 总任务个数
        :type total_tasks: int
        :param work_item_count: 工作项个数
        :type work_item_count: int
        """
        
        super(ShowOperationalDataCurrentMonthUsingResponse, self).__init__()

        self._alert_success_rate = None
        self._running_tasks = None
        self._total_alerts = None
        self._total_days = None
        self._total_runs = None
        self._total_tasks = None
        self._work_item_count = None
        self.discriminator = None

        if alert_success_rate is not None:
            self.alert_success_rate = alert_success_rate
        if running_tasks is not None:
            self.running_tasks = running_tasks
        if total_alerts is not None:
            self.total_alerts = total_alerts
        if total_days is not None:
            self.total_days = total_days
        if total_runs is not None:
            self.total_runs = total_runs
        if total_tasks is not None:
            self.total_tasks = total_tasks
        if work_item_count is not None:
            self.work_item_count = work_item_count

    @property
    def alert_success_rate(self):
        r"""Gets the alert_success_rate of this ShowOperationalDataCurrentMonthUsingResponse.

        告警成功比率，恒为1

        :return: The alert_success_rate of this ShowOperationalDataCurrentMonthUsingResponse.
        :rtype: int
        """
        return self._alert_success_rate

    @alert_success_rate.setter
    def alert_success_rate(self, alert_success_rate):
        r"""Sets the alert_success_rate of this ShowOperationalDataCurrentMonthUsingResponse.

        告警成功比率，恒为1

        :param alert_success_rate: The alert_success_rate of this ShowOperationalDataCurrentMonthUsingResponse.
        :type alert_success_rate: int
        """
        self._alert_success_rate = alert_success_rate

    @property
    def running_tasks(self):
        r"""Gets the running_tasks of this ShowOperationalDataCurrentMonthUsingResponse.

        正在运行的任务个数

        :return: The running_tasks of this ShowOperationalDataCurrentMonthUsingResponse.
        :rtype: int
        """
        return self._running_tasks

    @running_tasks.setter
    def running_tasks(self, running_tasks):
        r"""Sets the running_tasks of this ShowOperationalDataCurrentMonthUsingResponse.

        正在运行的任务个数

        :param running_tasks: The running_tasks of this ShowOperationalDataCurrentMonthUsingResponse.
        :type running_tasks: int
        """
        self._running_tasks = running_tasks

    @property
    def total_alerts(self):
        r"""Gets the total_alerts of this ShowOperationalDataCurrentMonthUsingResponse.

        总告警数

        :return: The total_alerts of this ShowOperationalDataCurrentMonthUsingResponse.
        :rtype: int
        """
        return self._total_alerts

    @total_alerts.setter
    def total_alerts(self, total_alerts):
        r"""Sets the total_alerts of this ShowOperationalDataCurrentMonthUsingResponse.

        总告警数

        :param total_alerts: The total_alerts of this ShowOperationalDataCurrentMonthUsingResponse.
        :type total_alerts: int
        """
        self._total_alerts = total_alerts

    @property
    def total_days(self):
        r"""Gets the total_days of this ShowOperationalDataCurrentMonthUsingResponse.

        总运行天数

        :return: The total_days of this ShowOperationalDataCurrentMonthUsingResponse.
        :rtype: int
        """
        return self._total_days

    @total_days.setter
    def total_days(self, total_days):
        r"""Sets the total_days of this ShowOperationalDataCurrentMonthUsingResponse.

        总运行天数

        :param total_days: The total_days of this ShowOperationalDataCurrentMonthUsingResponse.
        :type total_days: int
        """
        self._total_days = total_days

    @property
    def total_runs(self):
        r"""Gets the total_runs of this ShowOperationalDataCurrentMonthUsingResponse.

        总运行个数

        :return: The total_runs of this ShowOperationalDataCurrentMonthUsingResponse.
        :rtype: int
        """
        return self._total_runs

    @total_runs.setter
    def total_runs(self, total_runs):
        r"""Sets the total_runs of this ShowOperationalDataCurrentMonthUsingResponse.

        总运行个数

        :param total_runs: The total_runs of this ShowOperationalDataCurrentMonthUsingResponse.
        :type total_runs: int
        """
        self._total_runs = total_runs

    @property
    def total_tasks(self):
        r"""Gets the total_tasks of this ShowOperationalDataCurrentMonthUsingResponse.

        总任务个数

        :return: The total_tasks of this ShowOperationalDataCurrentMonthUsingResponse.
        :rtype: int
        """
        return self._total_tasks

    @total_tasks.setter
    def total_tasks(self, total_tasks):
        r"""Sets the total_tasks of this ShowOperationalDataCurrentMonthUsingResponse.

        总任务个数

        :param total_tasks: The total_tasks of this ShowOperationalDataCurrentMonthUsingResponse.
        :type total_tasks: int
        """
        self._total_tasks = total_tasks

    @property
    def work_item_count(self):
        r"""Gets the work_item_count of this ShowOperationalDataCurrentMonthUsingResponse.

        工作项个数

        :return: The work_item_count of this ShowOperationalDataCurrentMonthUsingResponse.
        :rtype: int
        """
        return self._work_item_count

    @work_item_count.setter
    def work_item_count(self, work_item_count):
        r"""Sets the work_item_count of this ShowOperationalDataCurrentMonthUsingResponse.

        工作项个数

        :param work_item_count: The work_item_count of this ShowOperationalDataCurrentMonthUsingResponse.
        :type work_item_count: int
        """
        self._work_item_count = work_item_count

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
        if not isinstance(other, ShowOperationalDataCurrentMonthUsingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
