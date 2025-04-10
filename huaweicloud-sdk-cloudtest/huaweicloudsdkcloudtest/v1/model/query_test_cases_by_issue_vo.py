# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryTestCasesByIssueVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'case_status_map': 'dict(str, int)',
        'new_create': 'int',
        'designing': 'int',
        'finished': 'int',
        'testing': 'int',
        'test_case_num': 'int',
        'testcases': 'list[TestCaseVo]',
        'total_count': 'int'
    }

    attribute_map = {
        'case_status_map': 'case_status_map',
        'new_create': 'new_create',
        'designing': 'designing',
        'finished': 'finished',
        'testing': 'testing',
        'test_case_num': 'test_case_num',
        'testcases': 'testcases',
        'total_count': 'total_count'
    }

    def __init__(self, case_status_map=None, new_create=None, designing=None, finished=None, testing=None, test_case_num=None, testcases=None, total_count=None):
        r"""QueryTestCasesByIssueVo

        The model defined in huaweicloud sdk

        :param case_status_map: 用例状态
        :type case_status_map: dict(str, int)
        :param new_create: 新建态
        :type new_create: int
        :param designing: 设计态
        :type designing: int
        :param finished: 完成态
        :type finished: int
        :param testing: 测试态
        :type testing: int
        :param test_case_num: 需求关联的用例数量
        :type test_case_num: int
        :param testcases: 用例详情
        :type testcases: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseVo`]
        :param total_count: 用例总数
        :type total_count: int
        """
        
        

        self._case_status_map = None
        self._new_create = None
        self._designing = None
        self._finished = None
        self._testing = None
        self._test_case_num = None
        self._testcases = None
        self._total_count = None
        self.discriminator = None

        if case_status_map is not None:
            self.case_status_map = case_status_map
        if new_create is not None:
            self.new_create = new_create
        if designing is not None:
            self.designing = designing
        if finished is not None:
            self.finished = finished
        if testing is not None:
            self.testing = testing
        if test_case_num is not None:
            self.test_case_num = test_case_num
        if testcases is not None:
            self.testcases = testcases
        if total_count is not None:
            self.total_count = total_count

    @property
    def case_status_map(self):
        r"""Gets the case_status_map of this QueryTestCasesByIssueVo.

        用例状态

        :return: The case_status_map of this QueryTestCasesByIssueVo.
        :rtype: dict(str, int)
        """
        return self._case_status_map

    @case_status_map.setter
    def case_status_map(self, case_status_map):
        r"""Sets the case_status_map of this QueryTestCasesByIssueVo.

        用例状态

        :param case_status_map: The case_status_map of this QueryTestCasesByIssueVo.
        :type case_status_map: dict(str, int)
        """
        self._case_status_map = case_status_map

    @property
    def new_create(self):
        r"""Gets the new_create of this QueryTestCasesByIssueVo.

        新建态

        :return: The new_create of this QueryTestCasesByIssueVo.
        :rtype: int
        """
        return self._new_create

    @new_create.setter
    def new_create(self, new_create):
        r"""Sets the new_create of this QueryTestCasesByIssueVo.

        新建态

        :param new_create: The new_create of this QueryTestCasesByIssueVo.
        :type new_create: int
        """
        self._new_create = new_create

    @property
    def designing(self):
        r"""Gets the designing of this QueryTestCasesByIssueVo.

        设计态

        :return: The designing of this QueryTestCasesByIssueVo.
        :rtype: int
        """
        return self._designing

    @designing.setter
    def designing(self, designing):
        r"""Sets the designing of this QueryTestCasesByIssueVo.

        设计态

        :param designing: The designing of this QueryTestCasesByIssueVo.
        :type designing: int
        """
        self._designing = designing

    @property
    def finished(self):
        r"""Gets the finished of this QueryTestCasesByIssueVo.

        完成态

        :return: The finished of this QueryTestCasesByIssueVo.
        :rtype: int
        """
        return self._finished

    @finished.setter
    def finished(self, finished):
        r"""Sets the finished of this QueryTestCasesByIssueVo.

        完成态

        :param finished: The finished of this QueryTestCasesByIssueVo.
        :type finished: int
        """
        self._finished = finished

    @property
    def testing(self):
        r"""Gets the testing of this QueryTestCasesByIssueVo.

        测试态

        :return: The testing of this QueryTestCasesByIssueVo.
        :rtype: int
        """
        return self._testing

    @testing.setter
    def testing(self, testing):
        r"""Sets the testing of this QueryTestCasesByIssueVo.

        测试态

        :param testing: The testing of this QueryTestCasesByIssueVo.
        :type testing: int
        """
        self._testing = testing

    @property
    def test_case_num(self):
        r"""Gets the test_case_num of this QueryTestCasesByIssueVo.

        需求关联的用例数量

        :return: The test_case_num of this QueryTestCasesByIssueVo.
        :rtype: int
        """
        return self._test_case_num

    @test_case_num.setter
    def test_case_num(self, test_case_num):
        r"""Sets the test_case_num of this QueryTestCasesByIssueVo.

        需求关联的用例数量

        :param test_case_num: The test_case_num of this QueryTestCasesByIssueVo.
        :type test_case_num: int
        """
        self._test_case_num = test_case_num

    @property
    def testcases(self):
        r"""Gets the testcases of this QueryTestCasesByIssueVo.

        用例详情

        :return: The testcases of this QueryTestCasesByIssueVo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseVo`]
        """
        return self._testcases

    @testcases.setter
    def testcases(self, testcases):
        r"""Sets the testcases of this QueryTestCasesByIssueVo.

        用例详情

        :param testcases: The testcases of this QueryTestCasesByIssueVo.
        :type testcases: list[:class:`huaweicloudsdkcloudtest.v1.TestCaseVo`]
        """
        self._testcases = testcases

    @property
    def total_count(self):
        r"""Gets the total_count of this QueryTestCasesByIssueVo.

        用例总数

        :return: The total_count of this QueryTestCasesByIssueVo.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this QueryTestCasesByIssueVo.

        用例总数

        :param total_count: The total_count of this QueryTestCasesByIssueVo.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, QueryTestCasesByIssueVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
