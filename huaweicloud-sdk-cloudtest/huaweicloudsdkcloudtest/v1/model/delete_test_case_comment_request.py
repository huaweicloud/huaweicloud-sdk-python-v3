# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTestCaseCommentRequest:

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
        'comment_id': 'str',
        'version_uri': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'testcase_id': 'testcase_id',
        'comment_id': 'comment_id',
        'version_uri': 'version_uri'
    }

    def __init__(self, project_id=None, testcase_id=None, comment_id=None, version_uri=None):
        r"""DeleteTestCaseCommentRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param testcase_id: 用例uri
        :type testcase_id: str
        :param comment_id: 评论uri
        :type comment_id: str
        :param version_uri: 分支或者测试计划uri
        :type version_uri: str
        """
        
        

        self._project_id = None
        self._testcase_id = None
        self._comment_id = None
        self._version_uri = None
        self.discriminator = None

        self.project_id = project_id
        self.testcase_id = testcase_id
        self.comment_id = comment_id
        if version_uri is not None:
            self.version_uri = version_uri

    @property
    def project_id(self):
        r"""Gets the project_id of this DeleteTestCaseCommentRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this DeleteTestCaseCommentRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DeleteTestCaseCommentRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this DeleteTestCaseCommentRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def testcase_id(self):
        r"""Gets the testcase_id of this DeleteTestCaseCommentRequest.

        用例uri

        :return: The testcase_id of this DeleteTestCaseCommentRequest.
        :rtype: str
        """
        return self._testcase_id

    @testcase_id.setter
    def testcase_id(self, testcase_id):
        r"""Sets the testcase_id of this DeleteTestCaseCommentRequest.

        用例uri

        :param testcase_id: The testcase_id of this DeleteTestCaseCommentRequest.
        :type testcase_id: str
        """
        self._testcase_id = testcase_id

    @property
    def comment_id(self):
        r"""Gets the comment_id of this DeleteTestCaseCommentRequest.

        评论uri

        :return: The comment_id of this DeleteTestCaseCommentRequest.
        :rtype: str
        """
        return self._comment_id

    @comment_id.setter
    def comment_id(self, comment_id):
        r"""Sets the comment_id of this DeleteTestCaseCommentRequest.

        评论uri

        :param comment_id: The comment_id of this DeleteTestCaseCommentRequest.
        :type comment_id: str
        """
        self._comment_id = comment_id

    @property
    def version_uri(self):
        r"""Gets the version_uri of this DeleteTestCaseCommentRequest.

        分支或者测试计划uri

        :return: The version_uri of this DeleteTestCaseCommentRequest.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this DeleteTestCaseCommentRequest.

        分支或者测试计划uri

        :param version_uri: The version_uri of this DeleteTestCaseCommentRequest.
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
        if not isinstance(other, DeleteTestCaseCommentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
