# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskTimeoutPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'same_ip_timeout_test_case_count': 'int',
        'same_test_case_timeout_ip_count': 'str',
        'test_case_timeout_count': 'int',
        'test_case_timeout_ratio': 'int',
        'timeout_times': 'int'
    }

    attribute_map = {
        'same_ip_timeout_test_case_count': 'sameIpTimeoutTestCaseCount',
        'same_test_case_timeout_ip_count': 'sameTestCaseTimeoutIpCount',
        'test_case_timeout_count': 'testCaseTimeoutCount',
        'test_case_timeout_ratio': 'testCaseTimeoutRatio',
        'timeout_times': 'timeoutTimes'
    }

    def __init__(self, same_ip_timeout_test_case_count=None, same_test_case_timeout_ip_count=None, test_case_timeout_count=None, test_case_timeout_ratio=None, timeout_times=None):
        r"""TaskTimeoutPolicy

        The model defined in huaweicloud sdk

        :param same_ip_timeout_test_case_count: 小网拨测：同一个ip超时的用例大于多少个告警
        :type same_ip_timeout_test_case_count: int
        :param same_test_case_timeout_ip_count: 小网拨测:同一用例在N个IP中超时，并且超时的用例个数达到M个告警
        :type same_test_case_timeout_ip_count: str
        :param test_case_timeout_count: 任务中多少个用例超时告警
        :type test_case_timeout_count: int
        :param test_case_timeout_ratio: 任务中多少百分比的用例超时告警
        :type test_case_timeout_ratio: int
        :param timeout_times: 任务连续超时告警
        :type timeout_times: int
        """
        
        

        self._same_ip_timeout_test_case_count = None
        self._same_test_case_timeout_ip_count = None
        self._test_case_timeout_count = None
        self._test_case_timeout_ratio = None
        self._timeout_times = None
        self.discriminator = None

        if same_ip_timeout_test_case_count is not None:
            self.same_ip_timeout_test_case_count = same_ip_timeout_test_case_count
        if same_test_case_timeout_ip_count is not None:
            self.same_test_case_timeout_ip_count = same_test_case_timeout_ip_count
        if test_case_timeout_count is not None:
            self.test_case_timeout_count = test_case_timeout_count
        if test_case_timeout_ratio is not None:
            self.test_case_timeout_ratio = test_case_timeout_ratio
        if timeout_times is not None:
            self.timeout_times = timeout_times

    @property
    def same_ip_timeout_test_case_count(self):
        r"""Gets the same_ip_timeout_test_case_count of this TaskTimeoutPolicy.

        小网拨测：同一个ip超时的用例大于多少个告警

        :return: The same_ip_timeout_test_case_count of this TaskTimeoutPolicy.
        :rtype: int
        """
        return self._same_ip_timeout_test_case_count

    @same_ip_timeout_test_case_count.setter
    def same_ip_timeout_test_case_count(self, same_ip_timeout_test_case_count):
        r"""Sets the same_ip_timeout_test_case_count of this TaskTimeoutPolicy.

        小网拨测：同一个ip超时的用例大于多少个告警

        :param same_ip_timeout_test_case_count: The same_ip_timeout_test_case_count of this TaskTimeoutPolicy.
        :type same_ip_timeout_test_case_count: int
        """
        self._same_ip_timeout_test_case_count = same_ip_timeout_test_case_count

    @property
    def same_test_case_timeout_ip_count(self):
        r"""Gets the same_test_case_timeout_ip_count of this TaskTimeoutPolicy.

        小网拨测:同一用例在N个IP中超时，并且超时的用例个数达到M个告警

        :return: The same_test_case_timeout_ip_count of this TaskTimeoutPolicy.
        :rtype: str
        """
        return self._same_test_case_timeout_ip_count

    @same_test_case_timeout_ip_count.setter
    def same_test_case_timeout_ip_count(self, same_test_case_timeout_ip_count):
        r"""Sets the same_test_case_timeout_ip_count of this TaskTimeoutPolicy.

        小网拨测:同一用例在N个IP中超时，并且超时的用例个数达到M个告警

        :param same_test_case_timeout_ip_count: The same_test_case_timeout_ip_count of this TaskTimeoutPolicy.
        :type same_test_case_timeout_ip_count: str
        """
        self._same_test_case_timeout_ip_count = same_test_case_timeout_ip_count

    @property
    def test_case_timeout_count(self):
        r"""Gets the test_case_timeout_count of this TaskTimeoutPolicy.

        任务中多少个用例超时告警

        :return: The test_case_timeout_count of this TaskTimeoutPolicy.
        :rtype: int
        """
        return self._test_case_timeout_count

    @test_case_timeout_count.setter
    def test_case_timeout_count(self, test_case_timeout_count):
        r"""Sets the test_case_timeout_count of this TaskTimeoutPolicy.

        任务中多少个用例超时告警

        :param test_case_timeout_count: The test_case_timeout_count of this TaskTimeoutPolicy.
        :type test_case_timeout_count: int
        """
        self._test_case_timeout_count = test_case_timeout_count

    @property
    def test_case_timeout_ratio(self):
        r"""Gets the test_case_timeout_ratio of this TaskTimeoutPolicy.

        任务中多少百分比的用例超时告警

        :return: The test_case_timeout_ratio of this TaskTimeoutPolicy.
        :rtype: int
        """
        return self._test_case_timeout_ratio

    @test_case_timeout_ratio.setter
    def test_case_timeout_ratio(self, test_case_timeout_ratio):
        r"""Sets the test_case_timeout_ratio of this TaskTimeoutPolicy.

        任务中多少百分比的用例超时告警

        :param test_case_timeout_ratio: The test_case_timeout_ratio of this TaskTimeoutPolicy.
        :type test_case_timeout_ratio: int
        """
        self._test_case_timeout_ratio = test_case_timeout_ratio

    @property
    def timeout_times(self):
        r"""Gets the timeout_times of this TaskTimeoutPolicy.

        任务连续超时告警

        :return: The timeout_times of this TaskTimeoutPolicy.
        :rtype: int
        """
        return self._timeout_times

    @timeout_times.setter
    def timeout_times(self, timeout_times):
        r"""Sets the timeout_times of this TaskTimeoutPolicy.

        任务连续超时告警

        :param timeout_times: The timeout_times of this TaskTimeoutPolicy.
        :type timeout_times: int
        """
        self._timeout_times = timeout_times

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
        if not isinstance(other, TaskTimeoutPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
