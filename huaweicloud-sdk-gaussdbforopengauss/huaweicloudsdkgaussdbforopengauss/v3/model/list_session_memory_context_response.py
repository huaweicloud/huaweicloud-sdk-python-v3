# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSessionMemoryContextResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'memory_context_info': 'list[SessionMemoryContextInfoResult]'
    }

    attribute_map = {
        'total': 'total',
        'memory_context_info': 'memory_context_info'
    }

    def __init__(self, total=None, memory_context_info=None):
        r"""ListSessionMemoryContextResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**: 总数。 **取值范围**: 不涉及。
        :type total: int
        :param memory_context_info: **参数解释**: 会话内存上下文列表。
        :type memory_context_info: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SessionMemoryContextInfoResult`]
        """
        
        super().__init__()

        self._total = None
        self._memory_context_info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if memory_context_info is not None:
            self.memory_context_info = memory_context_info

    @property
    def total(self):
        r"""Gets the total of this ListSessionMemoryContextResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。

        :return: The total of this ListSessionMemoryContextResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSessionMemoryContextResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。

        :param total: The total of this ListSessionMemoryContextResponse.
        :type total: int
        """
        self._total = total

    @property
    def memory_context_info(self):
        r"""Gets the memory_context_info of this ListSessionMemoryContextResponse.

        **参数解释**: 会话内存上下文列表。

        :return: The memory_context_info of this ListSessionMemoryContextResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SessionMemoryContextInfoResult`]
        """
        return self._memory_context_info

    @memory_context_info.setter
    def memory_context_info(self, memory_context_info):
        r"""Sets the memory_context_info of this ListSessionMemoryContextResponse.

        **参数解释**: 会话内存上下文列表。

        :param memory_context_info: The memory_context_info of this ListSessionMemoryContextResponse.
        :type memory_context_info: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SessionMemoryContextInfoResult`]
        """
        self._memory_context_info = memory_context_info

    def to_dict(self):
        import warnings
        warnings.warn("ListSessionMemoryContextResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSessionMemoryContextResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
