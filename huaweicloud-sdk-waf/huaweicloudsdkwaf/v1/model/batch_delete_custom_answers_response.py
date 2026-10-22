# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteCustomAnswersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deleted': 'list[str]',
        'failed': 'list[FailedCustomAnswers]'
    }

    attribute_map = {
        'deleted': 'deleted',
        'failed': 'failed'
    }

    def __init__(self, deleted=None, failed=None):
        r"""BatchDeleteCustomAnswersResponse

        The model defined in huaweicloud sdk

        :param deleted: 已删除的代答库ID列表
        :type deleted: list[str]
        :param failed: 删除失败的代答库列表
        :type failed: list[:class:`huaweicloudsdkwaf.v1.FailedCustomAnswers`]
        """
        
        super().__init__()

        self._deleted = None
        self._failed = None
        self.discriminator = None

        if deleted is not None:
            self.deleted = deleted
        if failed is not None:
            self.failed = failed

    @property
    def deleted(self):
        r"""Gets the deleted of this BatchDeleteCustomAnswersResponse.

        已删除的代答库ID列表

        :return: The deleted of this BatchDeleteCustomAnswersResponse.
        :rtype: list[str]
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        r"""Sets the deleted of this BatchDeleteCustomAnswersResponse.

        已删除的代答库ID列表

        :param deleted: The deleted of this BatchDeleteCustomAnswersResponse.
        :type deleted: list[str]
        """
        self._deleted = deleted

    @property
    def failed(self):
        r"""Gets the failed of this BatchDeleteCustomAnswersResponse.

        删除失败的代答库列表

        :return: The failed of this BatchDeleteCustomAnswersResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.FailedCustomAnswers`]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this BatchDeleteCustomAnswersResponse.

        删除失败的代答库列表

        :param failed: The failed of this BatchDeleteCustomAnswersResponse.
        :type failed: list[:class:`huaweicloudsdkwaf.v1.FailedCustomAnswers`]
        """
        self._failed = failed

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteCustomAnswersResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteCustomAnswersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
