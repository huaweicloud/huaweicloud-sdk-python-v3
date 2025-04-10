# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApiTestcaseHistoriesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'project_id': 'str',
        'testcase_id': 'str',
        'testcase_name': 'str',
        'testcase_results': 'list[TestcaseResult]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'project_id': 'project_id',
        'testcase_id': 'testcase_id',
        'testcase_name': 'testcase_name',
        'testcase_results': 'testcase_results'
    }

    def __init__(self, total_count=None, project_id=None, testcase_id=None, testcase_name=None, testcase_results=None):
        r"""ShowApiTestcaseHistoriesResponse

        The model defined in huaweicloud sdk

        :param total_count: 测试用例总数
        :type total_count: int
        :param project_id: 测试服务id
        :type project_id: str
        :param testcase_id: 测试用例id
        :type testcase_id: str
        :param testcase_name: 测试用例名称
        :type testcase_name: str
        :param testcase_results: 测试用例结果集
        :type testcase_results: list[:class:`huaweicloudsdkcloudtest.v1.TestcaseResult`]
        """
        
        super(ShowApiTestcaseHistoriesResponse, self).__init__()

        self._total_count = None
        self._project_id = None
        self._testcase_id = None
        self._testcase_name = None
        self._testcase_results = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if project_id is not None:
            self.project_id = project_id
        if testcase_id is not None:
            self.testcase_id = testcase_id
        if testcase_name is not None:
            self.testcase_name = testcase_name
        if testcase_results is not None:
            self.testcase_results = testcase_results

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowApiTestcaseHistoriesResponse.

        测试用例总数

        :return: The total_count of this ShowApiTestcaseHistoriesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowApiTestcaseHistoriesResponse.

        测试用例总数

        :param total_count: The total_count of this ShowApiTestcaseHistoriesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowApiTestcaseHistoriesResponse.

        测试服务id

        :return: The project_id of this ShowApiTestcaseHistoriesResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowApiTestcaseHistoriesResponse.

        测试服务id

        :param project_id: The project_id of this ShowApiTestcaseHistoriesResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def testcase_id(self):
        r"""Gets the testcase_id of this ShowApiTestcaseHistoriesResponse.

        测试用例id

        :return: The testcase_id of this ShowApiTestcaseHistoriesResponse.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        r"""Sets the testcase_id of this ShowApiTestcaseHistoriesResponse.

        测试用例id

        :param testcase_id: The testcase_id of this ShowApiTestcaseHistoriesResponse.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def testcase_name(self):
        r"""Gets the testcase_name of this ShowApiTestcaseHistoriesResponse.

        测试用例名称

        :return: The testcase_name of this ShowApiTestcaseHistoriesResponse.
        :rtype: str
        """
        return self._testcase_name

    @testcase_name.setter
    def testcase_name(self, testcase_name):
        r"""Sets the testcase_name of this ShowApiTestcaseHistoriesResponse.

        测试用例名称

        :param testcase_name: The testcase_name of this ShowApiTestcaseHistoriesResponse.
        :type testcase_name: str
        """
        self._testcase_name = testcase_name

    @property
    def testcase_results(self):
        r"""Gets the testcase_results of this ShowApiTestcaseHistoriesResponse.

        测试用例结果集

        :return: The testcase_results of this ShowApiTestcaseHistoriesResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestcaseResult`]
        """
        return self._testcase_results

    @testcase_results.setter
    def testcase_results(self, testcase_results):
        r"""Sets the testcase_results of this ShowApiTestcaseHistoriesResponse.

        测试用例结果集

        :param testcase_results: The testcase_results of this ShowApiTestcaseHistoriesResponse.
        :type testcase_results: list[:class:`huaweicloudsdkcloudtest.v1.TestcaseResult`]
        """
        self._testcase_results = testcase_results

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
        if not isinstance(other, ShowApiTestcaseHistoriesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
