# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssueBySnapIdsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'message': 'str',
        'code': 'str',
        'issues': 'list[IssueVO]'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code',
        'issues': 'issues'
    }

    def __init__(self, message=None, code=None, issues=None):
        r"""ListIssueBySnapIdsResponse

        The model defined in huaweicloud sdk

        :param message: 请求返回的结果信息。
        :type message: str
        :param code: 请求状态码。
        :type code: str
        :param issues: 快照对应的工作项信息。
        :type issues: list[:class:`huaweicloudsdkprojectman.v4.IssueVO`]
        """
        
        super().__init__()

        self._message = None
        self._code = None
        self._issues = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if issues is not None:
            self.issues = issues

    @property
    def message(self):
        r"""Gets the message of this ListIssueBySnapIdsResponse.

        请求返回的结果信息。

        :return: The message of this ListIssueBySnapIdsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListIssueBySnapIdsResponse.

        请求返回的结果信息。

        :param message: The message of this ListIssueBySnapIdsResponse.
        :type message: str
        """
        self._message = message

    @property
    def code(self):
        r"""Gets the code of this ListIssueBySnapIdsResponse.

        请求状态码。

        :return: The code of this ListIssueBySnapIdsResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ListIssueBySnapIdsResponse.

        请求状态码。

        :param code: The code of this ListIssueBySnapIdsResponse.
        :type code: str
        """
        self._code = code

    @property
    def issues(self):
        r"""Gets the issues of this ListIssueBySnapIdsResponse.

        快照对应的工作项信息。

        :return: The issues of this ListIssueBySnapIdsResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueVO`]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        r"""Sets the issues of this ListIssueBySnapIdsResponse.

        快照对应的工作项信息。

        :param issues: The issues of this ListIssueBySnapIdsResponse.
        :type issues: list[:class:`huaweicloudsdkprojectman.v4.IssueVO`]
        """
        self._issues = issues

    def to_dict(self):
        import warnings
        warnings.warn("ListIssueBySnapIdsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListIssueBySnapIdsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
