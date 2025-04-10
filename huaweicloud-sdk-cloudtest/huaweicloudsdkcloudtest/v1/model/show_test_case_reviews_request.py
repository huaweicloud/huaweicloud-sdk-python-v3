# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTestCaseReviewsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'version_uri': 'str',
        'page_no': 'int',
        'page_size': 'int',
        'testcase_uri': 'str'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'version_uri': 'version_uri',
        'page_no': 'page_no',
        'page_size': 'page_size',
        'testcase_uri': 'testcase_uri'
    }

    def __init__(self, project_uuid=None, version_uri=None, page_no=None, page_size=None, testcase_uri=None):
        r"""ShowTestCaseReviewsRequest

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param version_uri: 版本URI
        :type version_uri: str
        :param page_no: 当前页数
        :type page_no: int
        :param page_size: 每页条数
        :type page_size: int
        :param testcase_uri: 分支用例URI
        :type testcase_uri: str
        """
        
        

        self._project_uuid = None
        self._version_uri = None
        self._page_no = None
        self._page_size = None
        self._testcase_uri = None
        self.discriminator = None

        self.project_uuid = project_uuid
        self.version_uri = version_uri
        self.page_no = page_no
        self.page_size = page_size
        self.testcase_uri = testcase_uri

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ShowTestCaseReviewsRequest.

        项目id

        :return: The project_uuid of this ShowTestCaseReviewsRequest.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ShowTestCaseReviewsRequest.

        项目id

        :param project_uuid: The project_uuid of this ShowTestCaseReviewsRequest.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def version_uri(self):
        r"""Gets the version_uri of this ShowTestCaseReviewsRequest.

        版本URI

        :return: The version_uri of this ShowTestCaseReviewsRequest.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this ShowTestCaseReviewsRequest.

        版本URI

        :param version_uri: The version_uri of this ShowTestCaseReviewsRequest.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def page_no(self):
        r"""Gets the page_no of this ShowTestCaseReviewsRequest.

        当前页数

        :return: The page_no of this ShowTestCaseReviewsRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ShowTestCaseReviewsRequest.

        当前页数

        :param page_no: The page_no of this ShowTestCaseReviewsRequest.
        :type page_no: int
        """
        self._page_no = page_no

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowTestCaseReviewsRequest.

        每页条数

        :return: The page_size of this ShowTestCaseReviewsRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowTestCaseReviewsRequest.

        每页条数

        :param page_size: The page_size of this ShowTestCaseReviewsRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def testcase_uri(self):
        r"""Gets the testcase_uri of this ShowTestCaseReviewsRequest.

        分支用例URI

        :return: The testcase_uri of this ShowTestCaseReviewsRequest.
        :rtype: str
        """
        return self._testcase_uri

    @testcase_uri.setter
    def testcase_uri(self, testcase_uri):
        r"""Sets the testcase_uri of this ShowTestCaseReviewsRequest.

        分支用例URI

        :param testcase_uri: The testcase_uri of this ShowTestCaseReviewsRequest.
        :type testcase_uri: str
        """
        self._testcase_uri = testcase_uri

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
        if not isinstance(other, ShowTestCaseReviewsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
