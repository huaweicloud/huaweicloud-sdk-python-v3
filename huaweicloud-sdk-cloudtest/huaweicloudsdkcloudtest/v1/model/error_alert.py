# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorAlert:

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
        'task_error_policy': 'TaskErrorPolicy'
    }

    attribute_map = {
        'alert_template': 'alert_template',
        'enable': 'enable',
        'task_error_policy': 'taskErrorPolicy'
    }

    def __init__(self, alert_template=None, enable=None, task_error_policy=None):
        r"""ErrorAlert

        The model defined in huaweicloud sdk

        :param alert_template: 
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        :param enable: 异常告警是否开启：0关闭，1开启，默认关闭
        :type enable: str
        :param task_error_policy: 
        :type task_error_policy: :class:`huaweicloudsdkcloudtest.v1.TaskErrorPolicy`
        """
        
        

        self._alert_template = None
        self._enable = None
        self._task_error_policy = None
        self.discriminator = None

        if alert_template is not None:
            self.alert_template = alert_template
        if enable is not None:
            self.enable = enable
        if task_error_policy is not None:
            self.task_error_policy = task_error_policy

    @property
    def alert_template(self):
        r"""Gets the alert_template of this ErrorAlert.

        :return: The alert_template of this ErrorAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        return self._alert_template

    @alert_template.setter
    def alert_template(self, alert_template):
        r"""Sets the alert_template of this ErrorAlert.

        :param alert_template: The alert_template of this ErrorAlert.
        :type alert_template: :class:`huaweicloudsdkcloudtest.v1.AlertTemplate`
        """
        self._alert_template = alert_template

    @property
    def enable(self):
        r"""Gets the enable of this ErrorAlert.

        异常告警是否开启：0关闭，1开启，默认关闭

        :return: The enable of this ErrorAlert.
        :rtype: str
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this ErrorAlert.

        异常告警是否开启：0关闭，1开启，默认关闭

        :param enable: The enable of this ErrorAlert.
        :type enable: str
        """
        self._enable = enable

    @property
    def task_error_policy(self):
        r"""Gets the task_error_policy of this ErrorAlert.

        :return: The task_error_policy of this ErrorAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TaskErrorPolicy`
        """
        return self._task_error_policy

    @task_error_policy.setter
    def task_error_policy(self, task_error_policy):
        r"""Sets the task_error_policy of this ErrorAlert.

        :param task_error_policy: The task_error_policy of this ErrorAlert.
        :type task_error_policy: :class:`huaweicloudsdkcloudtest.v1.TaskErrorPolicy`
        """
        self._task_error_policy = task_error_policy

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
        if not isinstance(other, ErrorAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
