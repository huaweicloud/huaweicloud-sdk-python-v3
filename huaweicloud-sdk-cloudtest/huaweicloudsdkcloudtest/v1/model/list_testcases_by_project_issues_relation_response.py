# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTestcasesByProjectIssuesRelationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'testcases': 'list[IssuesRelationTestCaseVo]',
        'total_count': 'int',
        'page_no': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'testcases': 'testcases',
        'total_count': 'total_count',
        'page_no': 'page_no',
        'page_size': 'page_size'
    }

    def __init__(self, testcases=None, total_count=None, page_no=None, page_size=None):
        r"""ListTestcasesByProjectIssuesRelationResponse

        The model defined in huaweicloud sdk

        :param testcases: 用例详情
        :type testcases: list[:class:`huaweicloudsdkcloudtest.v1.IssuesRelationTestCaseVo`]
        :param total_count: 用例总数
        :type total_count: int
        :param page_no: 页码
        :type page_no: int
        :param page_size: 每页数量
        :type page_size: int
        """
        
        super(ListTestcasesByProjectIssuesRelationResponse, self).__init__()

        self._testcases = None
        self._total_count = None
        self._page_no = None
        self._page_size = None
        self.discriminator = None

        if testcases is not None:
            self.testcases = testcases
        if total_count is not None:
            self.total_count = total_count
        if page_no is not None:
            self.page_no = page_no
        if page_size is not None:
            self.page_size = page_size

    @property
    def testcases(self):
        r"""Gets the testcases of this ListTestcasesByProjectIssuesRelationResponse.

        用例详情

        :return: The testcases of this ListTestcasesByProjectIssuesRelationResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.IssuesRelationTestCaseVo`]
        """
        return self._testcases

    @testcases.setter
    def testcases(self, testcases):
        r"""Sets the testcases of this ListTestcasesByProjectIssuesRelationResponse.

        用例详情

        :param testcases: The testcases of this ListTestcasesByProjectIssuesRelationResponse.
        :type testcases: list[:class:`huaweicloudsdkcloudtest.v1.IssuesRelationTestCaseVo`]
        """
        self._testcases = testcases

    @property
    def total_count(self):
        r"""Gets the total_count of this ListTestcasesByProjectIssuesRelationResponse.

        用例总数

        :return: The total_count of this ListTestcasesByProjectIssuesRelationResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListTestcasesByProjectIssuesRelationResponse.

        用例总数

        :param total_count: The total_count of this ListTestcasesByProjectIssuesRelationResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def page_no(self):
        r"""Gets the page_no of this ListTestcasesByProjectIssuesRelationResponse.

        页码

        :return: The page_no of this ListTestcasesByProjectIssuesRelationResponse.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListTestcasesByProjectIssuesRelationResponse.

        页码

        :param page_no: The page_no of this ListTestcasesByProjectIssuesRelationResponse.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ListTestcasesByProjectIssuesRelationResponse.

        每页数量

        :return: The page_size of this ListTestcasesByProjectIssuesRelationResponse.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListTestcasesByProjectIssuesRelationResponse.

        每页数量

        :param page_size: The page_size of this ListTestcasesByProjectIssuesRelationResponse.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ListTestcasesByProjectIssuesRelationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
