# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchColdTableStorageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'failed_items': 'list[FailedItem]'
    }

    attribute_map = {
        'result': 'result',
        'failed_items': 'failed_items'
    }

    def __init__(self, result=None, failed_items=None):
        r"""SwitchColdTableStorageResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释**：  操作结果。  **取值范围**：  - SUCCESS：成功。 - FAILED：失败。
        :type result: str
        :param failed_items: **参数解释**：  校验失败的表信息。  当result取值为FAILED时，返回此参数。
        :type failed_items: list[:class:`huaweicloudsdkgaussdb.v3.FailedItem`]
        """
        
        super().__init__()

        self._result = None
        self._failed_items = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if failed_items is not None:
            self.failed_items = failed_items

    @property
    def result(self):
        r"""Gets the result of this SwitchColdTableStorageResponse.

        **参数解释**：  操作结果。  **取值范围**：  - SUCCESS：成功。 - FAILED：失败。

        :return: The result of this SwitchColdTableStorageResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this SwitchColdTableStorageResponse.

        **参数解释**：  操作结果。  **取值范围**：  - SUCCESS：成功。 - FAILED：失败。

        :param result: The result of this SwitchColdTableStorageResponse.
        :type result: str
        """
        self._result = result

    @property
    def failed_items(self):
        r"""Gets the failed_items of this SwitchColdTableStorageResponse.

        **参数解释**：  校验失败的表信息。  当result取值为FAILED时，返回此参数。

        :return: The failed_items of this SwitchColdTableStorageResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.FailedItem`]
        """
        return self._failed_items

    @failed_items.setter
    def failed_items(self, failed_items):
        r"""Sets the failed_items of this SwitchColdTableStorageResponse.

        **参数解释**：  校验失败的表信息。  当result取值为FAILED时，返回此参数。

        :param failed_items: The failed_items of this SwitchColdTableStorageResponse.
        :type failed_items: list[:class:`huaweicloudsdkgaussdb.v3.FailedItem`]
        """
        self._failed_items = failed_items

    def to_dict(self):
        import warnings
        warnings.warn("SwitchColdTableStorageResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SwitchColdTableStorageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
