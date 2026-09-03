# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskErrorPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'same_ip_error_test_case_count': 'int',
        'same_test_case_error_ip_count': 'str',
        'test_case_error_count': 'int',
        'test_case_error_ratio': 'int'
    }

    attribute_map = {
        'same_ip_error_test_case_count': 'sameIpErrorTestCaseCount',
        'same_test_case_error_ip_count': 'sameTestCaseErrorIpCount',
        'test_case_error_count': 'testCaseErrorCount',
        'test_case_error_ratio': 'testCaseErrorRatio'
    }

    def __init__(self, same_ip_error_test_case_count=None, same_test_case_error_ip_count=None, test_case_error_count=None, test_case_error_ratio=None):
        r"""TaskErrorPolicy

        The model defined in huaweicloud sdk

        :param same_ip_error_test_case_count: 小网拨测：同一个ip异常的用例大于多少个告警
        :type same_ip_error_test_case_count: int
        :param same_test_case_error_ip_count: 小网拨测:同一用例在N个IP中异常，并且异常的用例个数达到M个告警
        :type same_test_case_error_ip_count: str
        :param test_case_error_count: 任务中多少个用例异常告警
        :type test_case_error_count: int
        :param test_case_error_ratio: 任务中多少百分比的用例异常告警
        :type test_case_error_ratio: int
        """
        
        

        self._same_ip_error_test_case_count = None
        self._same_test_case_error_ip_count = None
        self._test_case_error_count = None
        self._test_case_error_ratio = None
        self.discriminator = None

        if same_ip_error_test_case_count is not None:
            self.same_ip_error_test_case_count = same_ip_error_test_case_count
        if same_test_case_error_ip_count is not None:
            self.same_test_case_error_ip_count = same_test_case_error_ip_count
        if test_case_error_count is not None:
            self.test_case_error_count = test_case_error_count
        if test_case_error_ratio is not None:
            self.test_case_error_ratio = test_case_error_ratio

    @property
    def same_ip_error_test_case_count(self):
        r"""Gets the same_ip_error_test_case_count of this TaskErrorPolicy.

        小网拨测：同一个ip异常的用例大于多少个告警

        :return: The same_ip_error_test_case_count of this TaskErrorPolicy.
        :rtype: int
        """
        return self._same_ip_error_test_case_count

    @same_ip_error_test_case_count.setter
    def same_ip_error_test_case_count(self, same_ip_error_test_case_count):
        r"""Sets the same_ip_error_test_case_count of this TaskErrorPolicy.

        小网拨测：同一个ip异常的用例大于多少个告警

        :param same_ip_error_test_case_count: The same_ip_error_test_case_count of this TaskErrorPolicy.
        :type same_ip_error_test_case_count: int
        """
        self._same_ip_error_test_case_count = same_ip_error_test_case_count

    @property
    def same_test_case_error_ip_count(self):
        r"""Gets the same_test_case_error_ip_count of this TaskErrorPolicy.

        小网拨测:同一用例在N个IP中异常，并且异常的用例个数达到M个告警

        :return: The same_test_case_error_ip_count of this TaskErrorPolicy.
        :rtype: str
        """
        return self._same_test_case_error_ip_count

    @same_test_case_error_ip_count.setter
    def same_test_case_error_ip_count(self, same_test_case_error_ip_count):
        r"""Sets the same_test_case_error_ip_count of this TaskErrorPolicy.

        小网拨测:同一用例在N个IP中异常，并且异常的用例个数达到M个告警

        :param same_test_case_error_ip_count: The same_test_case_error_ip_count of this TaskErrorPolicy.
        :type same_test_case_error_ip_count: str
        """
        self._same_test_case_error_ip_count = same_test_case_error_ip_count

    @property
    def test_case_error_count(self):
        r"""Gets the test_case_error_count of this TaskErrorPolicy.

        任务中多少个用例异常告警

        :return: The test_case_error_count of this TaskErrorPolicy.
        :rtype: int
        """
        return self._test_case_error_count

    @test_case_error_count.setter
    def test_case_error_count(self, test_case_error_count):
        r"""Sets the test_case_error_count of this TaskErrorPolicy.

        任务中多少个用例异常告警

        :param test_case_error_count: The test_case_error_count of this TaskErrorPolicy.
        :type test_case_error_count: int
        """
        self._test_case_error_count = test_case_error_count

    @property
    def test_case_error_ratio(self):
        r"""Gets the test_case_error_ratio of this TaskErrorPolicy.

        任务中多少百分比的用例异常告警

        :return: The test_case_error_ratio of this TaskErrorPolicy.
        :rtype: int
        """
        return self._test_case_error_ratio

    @test_case_error_ratio.setter
    def test_case_error_ratio(self, test_case_error_ratio):
        r"""Sets the test_case_error_ratio of this TaskErrorPolicy.

        任务中多少百分比的用例异常告警

        :param test_case_error_ratio: The test_case_error_ratio of this TaskErrorPolicy.
        :type test_case_error_ratio: int
        """
        self._test_case_error_ratio = test_case_error_ratio

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
        if not isinstance(other, TaskErrorPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
