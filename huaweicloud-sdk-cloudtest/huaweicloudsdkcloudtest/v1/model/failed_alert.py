# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedAlert:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cloud_alarm': 'CloudAlarmDto',
        'task_policy': 'TaskPolicy',
        'test_case_policy': 'TestCasePolicy',
        'wise_eye': 'WiseEye'
    }

    attribute_map = {
        'cloud_alarm': 'cloudAlarm',
        'task_policy': 'taskPolicy',
        'test_case_policy': 'testCasePolicy',
        'wise_eye': 'wiseEye'
    }

    def __init__(self, cloud_alarm=None, task_policy=None, test_case_policy=None, wise_eye=None):
        r"""FailedAlert

        The model defined in huaweicloud sdk

        :param cloud_alarm: 
        :type cloud_alarm: :class:`huaweicloudsdkcloudtest.v1.CloudAlarmDto`
        :param task_policy: 
        :type task_policy: :class:`huaweicloudsdkcloudtest.v1.TaskPolicy`
        :param test_case_policy: 
        :type test_case_policy: :class:`huaweicloudsdkcloudtest.v1.TestCasePolicy`
        :param wise_eye: 
        :type wise_eye: :class:`huaweicloudsdkcloudtest.v1.WiseEye`
        """
        
        

        self._cloud_alarm = None
        self._task_policy = None
        self._test_case_policy = None
        self._wise_eye = None
        self.discriminator = None

        if cloud_alarm is not None:
            self.cloud_alarm = cloud_alarm
        if task_policy is not None:
            self.task_policy = task_policy
        if test_case_policy is not None:
            self.test_case_policy = test_case_policy
        if wise_eye is not None:
            self.wise_eye = wise_eye

    @property
    def cloud_alarm(self):
        r"""Gets the cloud_alarm of this FailedAlert.

        :return: The cloud_alarm of this FailedAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.CloudAlarmDto`
        """
        return self._cloud_alarm

    @cloud_alarm.setter
    def cloud_alarm(self, cloud_alarm):
        r"""Sets the cloud_alarm of this FailedAlert.

        :param cloud_alarm: The cloud_alarm of this FailedAlert.
        :type cloud_alarm: :class:`huaweicloudsdkcloudtest.v1.CloudAlarmDto`
        """
        self._cloud_alarm = cloud_alarm

    @property
    def task_policy(self):
        r"""Gets the task_policy of this FailedAlert.

        :return: The task_policy of this FailedAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TaskPolicy`
        """
        return self._task_policy

    @task_policy.setter
    def task_policy(self, task_policy):
        r"""Sets the task_policy of this FailedAlert.

        :param task_policy: The task_policy of this FailedAlert.
        :type task_policy: :class:`huaweicloudsdkcloudtest.v1.TaskPolicy`
        """
        self._task_policy = task_policy

    @property
    def test_case_policy(self):
        r"""Gets the test_case_policy of this FailedAlert.

        :return: The test_case_policy of this FailedAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestCasePolicy`
        """
        return self._test_case_policy

    @test_case_policy.setter
    def test_case_policy(self, test_case_policy):
        r"""Sets the test_case_policy of this FailedAlert.

        :param test_case_policy: The test_case_policy of this FailedAlert.
        :type test_case_policy: :class:`huaweicloudsdkcloudtest.v1.TestCasePolicy`
        """
        self._test_case_policy = test_case_policy

    @property
    def wise_eye(self):
        r"""Gets the wise_eye of this FailedAlert.

        :return: The wise_eye of this FailedAlert.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.WiseEye`
        """
        return self._wise_eye

    @wise_eye.setter
    def wise_eye(self, wise_eye):
        r"""Sets the wise_eye of this FailedAlert.

        :param wise_eye: The wise_eye of this FailedAlert.
        :type wise_eye: :class:`huaweicloudsdkcloudtest.v1.WiseEye`
        """
        self._wise_eye = wise_eye

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
        if not isinstance(other, FailedAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
