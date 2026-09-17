# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociateScrumIssueResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[AssociateIssueDetail]',
        'status': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status'
    }

    def __init__(self, result=None, status=None):
        r"""AssociateScrumIssueResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释**： 本次新增的关联关系记录列表,每个元素对应一条关联关系。
        :type result: list[:class:`huaweicloudsdkprojectman.v4.AssociateIssueDetail`]
        :param status: **参数解释**： 接口整体响应状态。 **取值范围**： - success：关联工作项成功。 - error：关联工作项失败,详见错误码说明。
        :type status: str
        """
        
        super().__init__()

        self._result = None
        self._status = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if status is not None:
            self.status = status

    @property
    def result(self):
        r"""Gets the result of this AssociateScrumIssueResponse.

        **参数解释**： 本次新增的关联关系记录列表,每个元素对应一条关联关系。

        :return: The result of this AssociateScrumIssueResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.AssociateIssueDetail`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this AssociateScrumIssueResponse.

        **参数解释**： 本次新增的关联关系记录列表,每个元素对应一条关联关系。

        :param result: The result of this AssociateScrumIssueResponse.
        :type result: list[:class:`huaweicloudsdkprojectman.v4.AssociateIssueDetail`]
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this AssociateScrumIssueResponse.

        **参数解释**： 接口整体响应状态。 **取值范围**： - success：关联工作项成功。 - error：关联工作项失败,详见错误码说明。

        :return: The status of this AssociateScrumIssueResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AssociateScrumIssueResponse.

        **参数解释**： 接口整体响应状态。 **取值范围**： - success：关联工作项成功。 - error：关联工作项失败,详见错误码说明。

        :param status: The status of this AssociateScrumIssueResponse.
        :type status: str
        """
        self._status = status

    def to_dict(self):
        import warnings
        warnings.warn("AssociateScrumIssueResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, AssociateScrumIssueResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
