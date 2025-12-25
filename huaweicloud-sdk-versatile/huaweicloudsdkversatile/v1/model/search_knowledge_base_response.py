# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchKnowledgeBaseResponse(SdkResponse):

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
        'retrieve_result_list': 'list[RetrievalResultInfo]'
    }

    attribute_map = {
        'total': 'total',
        'retrieve_result_list': 'retrieve_result_list'
    }

    def __init__(self, total=None, retrieve_result_list=None):
        r"""SearchKnowledgeBaseResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**： 检索结果总数。  **取值范围**： 不涉及。
        :type total: int
        :param retrieve_result_list: **参数解释**： 检索结果列表。  **取值范围**： 不涉及。
        :type retrieve_result_list: list[:class:`huaweicloudsdkversatile.v1.RetrievalResultInfo`]
        """
        
        super().__init__()

        self._total = None
        self._retrieve_result_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if retrieve_result_list is not None:
            self.retrieve_result_list = retrieve_result_list

    @property
    def total(self):
        r"""Gets the total of this SearchKnowledgeBaseResponse.

        **参数解释**： 检索结果总数。  **取值范围**： 不涉及。

        :return: The total of this SearchKnowledgeBaseResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SearchKnowledgeBaseResponse.

        **参数解释**： 检索结果总数。  **取值范围**： 不涉及。

        :param total: The total of this SearchKnowledgeBaseResponse.
        :type total: int
        """
        self._total = total

    @property
    def retrieve_result_list(self):
        r"""Gets the retrieve_result_list of this SearchKnowledgeBaseResponse.

        **参数解释**： 检索结果列表。  **取值范围**： 不涉及。

        :return: The retrieve_result_list of this SearchKnowledgeBaseResponse.
        :rtype: list[:class:`huaweicloudsdkversatile.v1.RetrievalResultInfo`]
        """
        return self._retrieve_result_list

    @retrieve_result_list.setter
    def retrieve_result_list(self, retrieve_result_list):
        r"""Sets the retrieve_result_list of this SearchKnowledgeBaseResponse.

        **参数解释**： 检索结果列表。  **取值范围**： 不涉及。

        :param retrieve_result_list: The retrieve_result_list of this SearchKnowledgeBaseResponse.
        :type retrieve_result_list: list[:class:`huaweicloudsdkversatile.v1.RetrievalResultInfo`]
        """
        self._retrieve_result_list = retrieve_result_list

    def to_dict(self):
        import warnings
        warnings.warn("SearchKnowledgeBaseResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SearchKnowledgeBaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
