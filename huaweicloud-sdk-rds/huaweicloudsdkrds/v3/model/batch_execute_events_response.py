# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchExecuteEventsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'list[EventJobResult]'
    }

    attribute_map = {
        'results': 'results'
    }

    def __init__(self, results=None):
        r"""BatchExecuteEventsResponse

        The model defined in huaweicloud sdk

        :param results: **参数解释**：  事件操作响应结果  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type results: list[:class:`huaweicloudsdkrds.v3.EventJobResult`]
        """
        
        super().__init__()

        self._results = None
        self.discriminator = None

        if results is not None:
            self.results = results

    @property
    def results(self):
        r"""Gets the results of this BatchExecuteEventsResponse.

        **参数解释**：  事件操作响应结果  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The results of this BatchExecuteEventsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.EventJobResult`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this BatchExecuteEventsResponse.

        **参数解释**：  事件操作响应结果  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param results: The results of this BatchExecuteEventsResponse.
        :type results: list[:class:`huaweicloudsdkrds.v3.EventJobResult`]
        """
        self._results = results

    def to_dict(self):
        import warnings
        warnings.warn("BatchExecuteEventsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchExecuteEventsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
