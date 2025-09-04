# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTestReportCustomDetailByUriRequest:

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
        'version_uri': 'str',
        'report_uri': 'str',
        'custom_info_uri': 'str',
        'body': 'TestReportCustomDetailInfo'
    }

    attribute_map = {
        'project_id': 'project_id',
        'version_uri': 'version_uri',
        'report_uri': 'report_uri',
        'custom_info_uri': 'custom_info_uri',
        'body': 'body'
    }

    def __init__(self, project_id=None, version_uri=None, report_uri=None, custom_info_uri=None, body=None):
        r"""UpdateTestReportCustomDetailByUriRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param version_uri: 计划uri
        :type version_uri: str
        :param report_uri: 测试报告Uri
        :type report_uri: str
        :param custom_info_uri: 测试报告自定义模块Uri
        :type custom_info_uri: str
        :param body: Body of the UpdateTestReportCustomDetailByUriRequest
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestReportCustomDetailInfo`
        """
        
        

        self._project_id = None
        self._version_uri = None
        self._report_uri = None
        self._custom_info_uri = None
        self._body = None
        self.discriminator = None

        self.project_id = project_id
        self.version_uri = version_uri
        self.report_uri = report_uri
        self.custom_info_uri = custom_info_uri
        if body is not None:
            self.body = body

    @property
    def project_id(self):
        r"""Gets the project_id of this UpdateTestReportCustomDetailByUriRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this UpdateTestReportCustomDetailByUriRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this UpdateTestReportCustomDetailByUriRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this UpdateTestReportCustomDetailByUriRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def version_uri(self):
        r"""Gets the version_uri of this UpdateTestReportCustomDetailByUriRequest.

        计划uri

        :return: The version_uri of this UpdateTestReportCustomDetailByUriRequest.
        :rtype: str
        """
        return self._version_uri

    @version_uri.setter
    def version_uri(self, version_uri):
        r"""Sets the version_uri of this UpdateTestReportCustomDetailByUriRequest.

        计划uri

        :param version_uri: The version_uri of this UpdateTestReportCustomDetailByUriRequest.
        :type version_uri: str
        """
        self._version_uri = version_uri

    @property
    def report_uri(self):
        r"""Gets the report_uri of this UpdateTestReportCustomDetailByUriRequest.

        测试报告Uri

        :return: The report_uri of this UpdateTestReportCustomDetailByUriRequest.
        :rtype: str
        """
        return self._report_uri

    @report_uri.setter
    def report_uri(self, report_uri):
        r"""Sets the report_uri of this UpdateTestReportCustomDetailByUriRequest.

        测试报告Uri

        :param report_uri: The report_uri of this UpdateTestReportCustomDetailByUriRequest.
        :type report_uri: str
        """
        self._report_uri = report_uri

    @property
    def custom_info_uri(self):
        r"""Gets the custom_info_uri of this UpdateTestReportCustomDetailByUriRequest.

        测试报告自定义模块Uri

        :return: The custom_info_uri of this UpdateTestReportCustomDetailByUriRequest.
        :rtype: str
        """
        return self._custom_info_uri

    @custom_info_uri.setter
    def custom_info_uri(self, custom_info_uri):
        r"""Sets the custom_info_uri of this UpdateTestReportCustomDetailByUriRequest.

        测试报告自定义模块Uri

        :param custom_info_uri: The custom_info_uri of this UpdateTestReportCustomDetailByUriRequest.
        :type custom_info_uri: str
        """
        self._custom_info_uri = custom_info_uri

    @property
    def body(self):
        r"""Gets the body of this UpdateTestReportCustomDetailByUriRequest.

        :return: The body of this UpdateTestReportCustomDetailByUriRequest.
        :rtype: :class:`huaweicloudsdkcloudtest.v1.TestReportCustomDetailInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTestReportCustomDetailByUriRequest.

        :param body: The body of this UpdateTestReportCustomDetailByUriRequest.
        :type body: :class:`huaweicloudsdkcloudtest.v1.TestReportCustomDetailInfo`
        """
        self._body = body

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
        if not isinstance(other, UpdateTestReportCustomDetailByUriRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
