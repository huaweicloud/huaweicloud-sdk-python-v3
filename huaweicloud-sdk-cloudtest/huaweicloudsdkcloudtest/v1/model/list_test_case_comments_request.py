# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTestCaseCommentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'testcase_id': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'version_uri': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'testcase_id': 'testcase_id',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'version_uri': 'version_uri'
    }

    def __init__(self, project_id=None, testcase_id=None, page_no=None, page_size=None, version_uri=None):
        """ListTestCaseCommentsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param testcase_id: 用例uri
        :type testcase_id: str
        :param page_no: 页数
        :type page_no: int
        :param page_size: 页数大小
        :type page_size: int
        :param version_uri: 分支或者测试计划uri
        :type version_uri: str
        """
        
        

        self._project_id = None
        self._testcase_id = None
        self._page_no = None
        self._page_size = None
        self._version_uri = None
        self.discriminator = None

        self.project_id = project_id
        self.testcase_id = testcase_id
        self.page_no = page_no
        self.page_size = page_size
        if version_uri is not None:
            self.version_uri = version_uri

    @property
    def project_id(self):
        """Gets the project_id of this ListTestCaseCommentsRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this ListTestCaseCommentsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListTestCaseCommentsRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this ListTestCaseCommentsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def testcase_id(self):
        """Gets the testcase_id of this ListTestCaseCommentsRequest.

        用例uri

        :return: The testcase_id of this ListTestCaseCommentsRequest.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        """Sets the testcase_id of this ListTestCaseCommentsRequest.

        用例uri

        :param testcase_id: The testcase_id of this ListTestCaseCommentsRequest.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def page_no(self):
        """Gets the page_no of this ListTestCaseCommentsRequest.

        页数

        :return: The page_no of this ListTestCaseCommentsRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ListTestCaseCommentsRequest.

        页数

        :param page_no: The page_no of this ListTestCaseCommentsRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        """Gets the page_size of this ListTestCaseCommentsRequest.

        页数大小

        :return: The page_size of this ListTestCaseCommentsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListTestCaseCommentsRequest.

        页数大小

        :param page_size: The page_size of this ListTestCaseCommentsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def version_uri(self):
        """Gets the version_uri of this ListTestCaseCommentsRequest.

        分支或者测试计划uri

        :return: The version_uri of this ListTestCaseCommentsRequest.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        """Sets the version_uri of this ListTestCaseCommentsRequest.

        分支或者测试计划uri

        :param version_uri: The version_uri of this ListTestCaseCommentsRequest.
        :type version_uri: str
        """
        self._version_uri = version_uri

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
        if not isinstance(other, ListTestCaseCommentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
