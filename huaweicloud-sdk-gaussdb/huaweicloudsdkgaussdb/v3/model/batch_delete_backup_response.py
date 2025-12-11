# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteBackupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_results': 'list[DeleteBackupResult]',
        'success_count': 'int',
        'failed_count': 'int'
    }

    attribute_map = {
        'failed_results': 'failed_results',
        'success_count': 'success_count',
        'failed_count': 'failed_count'
    }

    def __init__(self, failed_results=None, success_count=None, failed_count=None):
        r"""BatchDeleteBackupResponse

        The model defined in huaweicloud sdk

        :param failed_results: **参数解释**：  备份删除异常信息。  **取值范围**：  当所有备份删除成功，该值是空。
        :type failed_results: list[:class:`huaweicloudsdkgaussdb.v3.DeleteBackupResult`]
        :param success_count: **参数解释**：  删除成功的数量。  **取值范围**：  0-50。
        :type success_count: int
        :param failed_count: **参数解释**：  删除失败的数量。  **取值范围**：  0-50。
        :type failed_count: int
        """
        
        super().__init__()

        self._failed_results = None
        self._success_count = None
        self._failed_count = None
        self.discriminator = None

        if failed_results is not None:
            self.failed_results = failed_results
        if success_count is not None:
            self.success_count = success_count
        if failed_count is not None:
            self.failed_count = failed_count

    @property
    def failed_results(self):
        r"""Gets the failed_results of this BatchDeleteBackupResponse.

        **参数解释**：  备份删除异常信息。  **取值范围**：  当所有备份删除成功，该值是空。

        :return: The failed_results of this BatchDeleteBackupResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DeleteBackupResult`]
        """
        return self._failed_results

    @failed_results.setter
    def failed_results(self, failed_results):
        r"""Sets the failed_results of this BatchDeleteBackupResponse.

        **参数解释**：  备份删除异常信息。  **取值范围**：  当所有备份删除成功，该值是空。

        :param failed_results: The failed_results of this BatchDeleteBackupResponse.
        :type failed_results: list[:class:`huaweicloudsdkgaussdb.v3.DeleteBackupResult`]
        """
        self._failed_results = failed_results

    @property
    def success_count(self):
        r"""Gets the success_count of this BatchDeleteBackupResponse.

        **参数解释**：  删除成功的数量。  **取值范围**：  0-50。

        :return: The success_count of this BatchDeleteBackupResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this BatchDeleteBackupResponse.

        **参数解释**：  删除成功的数量。  **取值范围**：  0-50。

        :param success_count: The success_count of this BatchDeleteBackupResponse.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failed_count(self):
        r"""Gets the failed_count of this BatchDeleteBackupResponse.

        **参数解释**：  删除失败的数量。  **取值范围**：  0-50。

        :return: The failed_count of this BatchDeleteBackupResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        r"""Sets the failed_count of this BatchDeleteBackupResponse.

        **参数解释**：  删除失败的数量。  **取值范围**：  0-50。

        :param failed_count: The failed_count of this BatchDeleteBackupResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteBackupResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteBackupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
