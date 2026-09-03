# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimeoutAlert:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_template': 'AlertTemplate',
        'enable': 'str',
        'task_timeout_policy': 'TaskTimeoutPolicy',
        'test_case_timeout_policy': 'TestCaseTimeoutPolicy',
        'timeout_retry_times': 'int'
    }

    attribute_map = {
        'alert_template': 'alert_template',
        'enable': 'enable',
        'task_timeout_policy': 'task_timeout_policy',
        'test_case_timeout_policy': 'testCaseTimeoutPolicy',
        'timeout_retry_times': 'timeoutRetryTimes'
    }

    def __init__(self, alert_template=None, enable=None, task_timeout_policy=None, test_case_timeout_policy=None, timeout_retry_times=None):
        r"""TimeoutAlert

        The model defined in huaweicloud sdk

        :param alert_template: 
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        :param enable: 超时告警开启 0关闭 1开启
        :type enable: str
        :param task_timeout_policy: 
        :type task_timeout_policy: :class:`huaweicloudsdkcloudtest.v1.TaskTimeoutPolicy`
        :param test_case_timeout_policy: 
        :type test_case_timeout_policy: :class:`huaweicloudsdkcloudtest.v1.TestCaseTimeoutPolicy`
        :param timeout_retry_times: 超时重试次数
        :type timeout_retry_times: int
        """
        
        

        self._alert_template = None
        self._enable = None
        self._task_timeout_policy = None
        self._test_case_timeout_policy = None
        self._timeout_retry_times = None
        self.discriminator = None

        if alert_template is not None:
            self.alert_template = alert_template
        if enable is not None:
            self.enable = enable
        if task_timeout_policy is not None:
            self.task_timeout_policy = task_timeout_policy
        if test_case_timeout_policy is not None:
            self.test_case_timeout_policy = test_case_timeout_policy
        if timeout_retry_times is not None:
            self.timeout_retry_times = timeout_retry_times

    @property
    def alert_template(self):
        r"""Gets the alert_template of this TimeoutAlert.

        :return: The alert_template of this TimeoutAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        return self._alert_template

    @alert_template.setter
    def alert_template(self, alert_template):
        r"""Sets the alert_template of this TimeoutAlert.

        :param alert_template: The alert_template of this TimeoutAlert.
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        self._alert_template = alert_template

    @property
    def enable(self):
        r"""Gets the enable of this TimeoutAlert.

        超时告警开启 0关闭 1开启

        :return: The enable of this TimeoutAlert.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this TimeoutAlert.

        超时告警开启 0关闭 1开启

        :param enable: The enable of this TimeoutAlert.
        :type enable: str
        """
        self._enable = enable

    @property
    def task_timeout_policy(self):
        r"""Gets the task_timeout_policy of this TimeoutAlert.

        :return: The task_timeout_policy of this TimeoutAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TaskTimeoutPolicy`
        """
        return self._task_timeout_policy

    @task_timeout_policy.setter
    def task_timeout_policy(self, task_timeout_policy):
        r"""Sets the task_timeout_policy of this TimeoutAlert.

        :param task_timeout_policy: The task_timeout_policy of this TimeoutAlert.
        :type task_timeout_policy: :class:`huaweicloudsdkcloudtest.v1.TaskTimeoutPolicy`
        """
        self._task_timeout_policy = task_timeout_policy

    @property
    def test_case_timeout_policy(self):
        r"""Gets the test_case_timeout_policy of this TimeoutAlert.

        :return: The test_case_timeout_policy of this TimeoutAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestCaseTimeoutPolicy`
        """
        return self._test_case_timeout_policy

    @test_case_timeout_policy.setter
    def test_case_timeout_policy(self, test_case_timeout_policy):
        r"""Sets the test_case_timeout_policy of this TimeoutAlert.

        :param test_case_timeout_policy: The test_case_timeout_policy of this TimeoutAlert.
        :type test_case_timeout_policy: :class:`huaweicloudsdkcloudtest.v1.TestCaseTimeoutPolicy`
        """
        self._test_case_timeout_policy = test_case_timeout_policy

    @property
    def timeout_retry_times(self):
        r"""Gets the timeout_retry_times of this TimeoutAlert.

        超时重试次数

        :return: The timeout_retry_times of this TimeoutAlert.
        :rtype: int
        """
        return self._timeout_retry_times

    @timeout_retry_times.setter
    def timeout_retry_times(self, timeout_retry_times):
        r"""Sets the timeout_retry_times of this TimeoutAlert.

        超时重试次数

        :param timeout_retry_times: The timeout_retry_times of this TimeoutAlert.
        :type timeout_retry_times: int
        """
        self._timeout_retry_times = timeout_retry_times

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimeoutAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
