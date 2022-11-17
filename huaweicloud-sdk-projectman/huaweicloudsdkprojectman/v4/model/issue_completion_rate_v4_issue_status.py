# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueCompletionRateV4IssueStatus:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'closed_num': 'int',
        'new_num': 'int',
        'process_num': 'int',
        'rejected_num': 'int',
        'solved_num': 'int',
        'test_num': 'int'
    }

    attribute_map = {
        'closed_num': 'closed_num',
        'new_num': 'new_num',
        'process_num': 'process_num',
        'rejected_num': 'rejected_num',
        'solved_num': 'solved_num',
        'test_num': 'test_num'
    }

    def __init__(self, closed_num=None, new_num=None, process_num=None, rejected_num=None, solved_num=None, test_num=None):
        """IssueCompletionRateV4IssueStatus

        The model defined in huaweicloud sdk

        :param closed_num: 已关闭的工作项
        :type closed_num: int
        :param new_num: 新建的工作项
        :type new_num: int
        :param process_num: 进行中的工作项数目
        :type process_num: int
        :param rejected_num: 已经拒绝的工作项
        :type rejected_num: int
        :param solved_num: 已经解决的工作项
        :type solved_num: int
        :param test_num: 测试中的工作项
        :type test_num: int
        """
        
        

        self._closed_num = None
        self._new_num = None
        self._process_num = None
        self._rejected_num = None
        self._solved_num = None
        self._test_num = None
        self.discriminator = None

        if closed_num is not None:
            self.closed_num = closed_num
        if new_num is not None:
            self.new_num = new_num
        if process_num is not None:
            self.process_num = process_num
        if rejected_num is not None:
            self.rejected_num = rejected_num
        if solved_num is not None:
            self.solved_num = solved_num
        if test_num is not None:
            self.test_num = test_num

    @property
    def closed_num(self):
        """Gets the closed_num of this IssueCompletionRateV4IssueStatus.

        已关闭的工作项

        :return: The closed_num of this IssueCompletionRateV4IssueStatus.
        :rtype: int
        """
        return self._closed_num

    @closed_num.setter
    def closed_num(self, closed_num):
        """Sets the closed_num of this IssueCompletionRateV4IssueStatus.

        已关闭的工作项

        :param closed_num: The closed_num of this IssueCompletionRateV4IssueStatus.
        :type closed_num: int
        """
        self._closed_num = closed_num

    @property
    def new_num(self):
        """Gets the new_num of this IssueCompletionRateV4IssueStatus.

        新建的工作项

        :return: The new_num of this IssueCompletionRateV4IssueStatus.
        :rtype: int
        """
        return self._new_num

    @new_num.setter
    def new_num(self, new_num):
        """Sets the new_num of this IssueCompletionRateV4IssueStatus.

        新建的工作项

        :param new_num: The new_num of this IssueCompletionRateV4IssueStatus.
        :type new_num: int
        """
        self._new_num = new_num

    @property
    def process_num(self):
        """Gets the process_num of this IssueCompletionRateV4IssueStatus.

        进行中的工作项数目

        :return: The process_num of this IssueCompletionRateV4IssueStatus.
        :rtype: int
        """
        return self._process_num

    @process_num.setter
    def process_num(self, process_num):
        """Sets the process_num of this IssueCompletionRateV4IssueStatus.

        进行中的工作项数目

        :param process_num: The process_num of this IssueCompletionRateV4IssueStatus.
        :type process_num: int
        """
        self._process_num = process_num

    @property
    def rejected_num(self):
        """Gets the rejected_num of this IssueCompletionRateV4IssueStatus.

        已经拒绝的工作项

        :return: The rejected_num of this IssueCompletionRateV4IssueStatus.
        :rtype: int
        """
        return self._rejected_num

    @rejected_num.setter
    def rejected_num(self, rejected_num):
        """Sets the rejected_num of this IssueCompletionRateV4IssueStatus.

        已经拒绝的工作项

        :param rejected_num: The rejected_num of this IssueCompletionRateV4IssueStatus.
        :type rejected_num: int
        """
        self._rejected_num = rejected_num

    @property
    def solved_num(self):
        """Gets the solved_num of this IssueCompletionRateV4IssueStatus.

        已经解决的工作项

        :return: The solved_num of this IssueCompletionRateV4IssueStatus.
        :rtype: int
        """
        return self._solved_num

    @solved_num.setter
    def solved_num(self, solved_num):
        """Sets the solved_num of this IssueCompletionRateV4IssueStatus.

        已经解决的工作项

        :param solved_num: The solved_num of this IssueCompletionRateV4IssueStatus.
        :type solved_num: int
        """
        self._solved_num = solved_num

    @property
    def test_num(self):
        """Gets the test_num of this IssueCompletionRateV4IssueStatus.

        测试中的工作项

        :return: The test_num of this IssueCompletionRateV4IssueStatus.
        :rtype: int
        """
        return self._test_num

    @test_num.setter
    def test_num(self, test_num):
        """Sets the test_num of this IssueCompletionRateV4IssueStatus.

        测试中的工作项

        :param test_num: The test_num of this IssueCompletionRateV4IssueStatus.
        :type test_num: int
        """
        self._test_num = test_num

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
        if not isinstance(other, IssueCompletionRateV4IssueStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
