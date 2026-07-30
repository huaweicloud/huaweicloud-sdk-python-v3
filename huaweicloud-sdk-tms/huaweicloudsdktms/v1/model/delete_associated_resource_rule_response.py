# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAssociatedResourceRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'errors': 'list[ErrorInfo]'
    }

    attribute_map = {
        'errors': 'errors'
    }

    def __init__(self, errors=None):
        r"""DeleteAssociatedResourceRuleResponse

        The model defined in huaweicloud sdk

        :param errors: 操作失败的错误信息
        :type errors: list[:class:`huaweicloudsdktms.v1.ErrorInfo`]
        """
        
        super().__init__()

        self._errors = None
        self.discriminator = None

        if errors is not None:
            self.errors = errors

    @property
    def errors(self):
        r"""Gets the errors of this DeleteAssociatedResourceRuleResponse.

        操作失败的错误信息

        :return: The errors of this DeleteAssociatedResourceRuleResponse.
        :rtype: list[:class:`huaweicloudsdktms.v1.ErrorInfo`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this DeleteAssociatedResourceRuleResponse.

        操作失败的错误信息

        :param errors: The errors of this DeleteAssociatedResourceRuleResponse.
        :type errors: list[:class:`huaweicloudsdktms.v1.ErrorInfo`]
        """
        self._errors = errors

    def to_dict(self):
        import warnings
        warnings.warn("DeleteAssociatedResourceRuleResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DeleteAssociatedResourceRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
