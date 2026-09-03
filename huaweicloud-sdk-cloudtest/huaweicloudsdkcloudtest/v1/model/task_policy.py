# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_times': 'int',
        'same_ip_failed_test_case_count': 'int',
        'same_test_case_failed_ip_count': 'str',
        'test_case_failed_count': 'int',
        'test_case_failed_ratio': 'int'
    }

    attribute_map = {
        'failed_times': 'failed_times',
        'same_ip_failed_test_case_count': 'sameIpFailedTestCaseCount',
        'same_test_case_failed_ip_count': 'sameTestCaseFailedIpCount',
        'test_case_failed_count': 'testCaseFailedCount',
        'test_case_failed_ratio': 'testCaseFailedRatio'
    }

    def __init__(self, failed_times=None, same_ip_failed_test_case_count=None, same_test_case_failed_ip_count=None, test_case_failed_count=None, test_case_failed_ratio=None):
        r"""TaskPolicy

        The model defined in huaweicloud sdk

        :param failed_times: 任务连续失败N次告警
        :type failed_times: int
        :param same_ip_failed_test_case_count: 小网拨测：同一个ip失败的用例大于多少个告警
        :type same_ip_failed_test_case_count: int
        :param same_test_case_failed_ip_count: 小网拨测:同一用例在N个IP中失败，并且失败的用例个数达到M个
        :type same_test_case_failed_ip_count: str
        :param test_case_failed_count: 任务中多少个用例失败告警
        :type test_case_failed_count: int
        :param test_case_failed_ratio: 任务中多少百分比的用例失败告警
        :type test_case_failed_ratio: int
        """
        
        

        self._failed_times = None
        self._same_ip_failed_test_case_count = None
        self._same_test_case_failed_ip_count = None
        self._test_case_failed_count = None
        self._test_case_failed_ratio = None
        self.discriminator = None

        if failed_times is not None:
            self.failed_times = failed_times
        if same_ip_failed_test_case_count is not None:
            self.same_ip_failed_test_case_count = same_ip_failed_test_case_count
        if same_test_case_failed_ip_count is not None:
            self.same_test_case_failed_ip_count = same_test_case_failed_ip_count
        if test_case_failed_count is not None:
            self.test_case_failed_count = test_case_failed_count
        if test_case_failed_ratio is not None:
            self.test_case_failed_ratio = test_case_failed_ratio

    @property
    def failed_times(self):
        r"""Gets the failed_times of this TaskPolicy.

        任务连续失败N次告警

        :return: The failed_times of this TaskPolicy.
        :rtype: int
        """
        return self._failed_times

    @failed_times.setter
    def failed_times(self, failed_times):
        r"""Sets the failed_times of this TaskPolicy.

        任务连续失败N次告警

        :param failed_times: The failed_times of this TaskPolicy.
        :type failed_times: int
        """
        self._failed_times = failed_times

    @property
    def same_ip_failed_test_case_count(self):
        r"""Gets the same_ip_failed_test_case_count of this TaskPolicy.

        小网拨测：同一个ip失败的用例大于多少个告警

        :return: The same_ip_failed_test_case_count of this TaskPolicy.
        :rtype: int
        """
        return self._same_ip_failed_test_case_count

    @same_ip_failed_test_case_count.setter
    def same_ip_failed_test_case_count(self, same_ip_failed_test_case_count):
        r"""Sets the same_ip_failed_test_case_count of this TaskPolicy.

        小网拨测：同一个ip失败的用例大于多少个告警

        :param same_ip_failed_test_case_count: The same_ip_failed_test_case_count of this TaskPolicy.
        :type same_ip_failed_test_case_count: int
        """
        self._same_ip_failed_test_case_count = same_ip_failed_test_case_count

    @property
    def same_test_case_failed_ip_count(self):
        r"""Gets the same_test_case_failed_ip_count of this TaskPolicy.

        小网拨测:同一用例在N个IP中失败，并且失败的用例个数达到M个

        :return: The same_test_case_failed_ip_count of this TaskPolicy.
        :rtype: str
        """
        return self._same_test_case_failed_ip_count

    @same_test_case_failed_ip_count.setter
    def same_test_case_failed_ip_count(self, same_test_case_failed_ip_count):
        r"""Sets the same_test_case_failed_ip_count of this TaskPolicy.

        小网拨测:同一用例在N个IP中失败，并且失败的用例个数达到M个

        :param same_test_case_failed_ip_count: The same_test_case_failed_ip_count of this TaskPolicy.
        :type same_test_case_failed_ip_count: str
        """
        self._same_test_case_failed_ip_count = same_test_case_failed_ip_count

    @property
    def test_case_failed_count(self):
        r"""Gets the test_case_failed_count of this TaskPolicy.

        任务中多少个用例失败告警

        :return: The test_case_failed_count of this TaskPolicy.
        :rtype: int
        """
        return self._test_case_failed_count

    @test_case_failed_count.setter
    def test_case_failed_count(self, test_case_failed_count):
        r"""Sets the test_case_failed_count of this TaskPolicy.

        任务中多少个用例失败告警

        :param test_case_failed_count: The test_case_failed_count of this TaskPolicy.
        :type test_case_failed_count: int
        """
        self._test_case_failed_count = test_case_failed_count

    @property
    def test_case_failed_ratio(self):
        r"""Gets the test_case_failed_ratio of this TaskPolicy.

        任务中多少百分比的用例失败告警

        :return: The test_case_failed_ratio of this TaskPolicy.
        :rtype: int
        """
        return self._test_case_failed_ratio

    @test_case_failed_ratio.setter
    def test_case_failed_ratio(self, test_case_failed_ratio):
        r"""Sets the test_case_failed_ratio of this TaskPolicy.

        任务中多少百分比的用例失败告警

        :param test_case_failed_ratio: The test_case_failed_ratio of this TaskPolicy.
        :type test_case_failed_ratio: int
        """
        self._test_case_failed_ratio = test_case_failed_ratio

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
        if not isinstance(other, TaskPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
