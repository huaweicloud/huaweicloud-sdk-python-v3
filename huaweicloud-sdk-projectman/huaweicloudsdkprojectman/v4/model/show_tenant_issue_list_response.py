# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTenantIssueListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'message': 'str',
        'result': 'list[IssueDetailsResponse]'
    }

    attribute_map = {
        'status': 'status',
        'message': 'message',
        'result': 'result'
    }

    def __init__(self, status=None, message=None, result=None):
        r"""ShowTenantIssueListResponse

        The model defined in huaweicloud sdk

        :param status: **参数解释**： 返回状态。 **取值范围**： success：响应成功。 error：响应失败
        :type status: str
        :param message: **参数解释**： 信息。 **取值范围**： 不涉及
        :type message: str
        :param result: **参数解释**： 查询结果。
        :type result: list[:class:`huaweicloudsdkprojectman.v4.IssueDetailsResponse`]
        """
        
        super().__init__()

        self._status = None
        self._message = None
        self._result = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if message is not None:
            self.message = message
        if result is not None:
            self.result = result

    @property
    def status(self):
        r"""Gets the status of this ShowTenantIssueListResponse.

        **参数解释**： 返回状态。 **取值范围**： success：响应成功。 error：响应失败

        :return: The status of this ShowTenantIssueListResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTenantIssueListResponse.

        **参数解释**： 返回状态。 **取值范围**： success：响应成功。 error：响应失败

        :param status: The status of this ShowTenantIssueListResponse.
        :type status: str
        """
        self._status = status

    @property
    def message(self):
        r"""Gets the message of this ShowTenantIssueListResponse.

        **参数解释**： 信息。 **取值范围**： 不涉及

        :return: The message of this ShowTenantIssueListResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ShowTenantIssueListResponse.

        **参数解释**： 信息。 **取值范围**： 不涉及

        :param message: The message of this ShowTenantIssueListResponse.
        :type message: str
        """
        self._message = message

    @property
    def result(self):
        r"""Gets the result of this ShowTenantIssueListResponse.

        **参数解释**： 查询结果。

        :return: The result of this ShowTenantIssueListResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueDetailsResponse`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ShowTenantIssueListResponse.

        **参数解释**： 查询结果。

        :param result: The result of this ShowTenantIssueListResponse.
        :type result: list[:class:`huaweicloudsdkprojectman.v4.IssueDetailsResponse`]
        """
        self._result = result

    def to_dict(self):
        import warnings
        warnings.warn("ShowTenantIssueListResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTenantIssueListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
