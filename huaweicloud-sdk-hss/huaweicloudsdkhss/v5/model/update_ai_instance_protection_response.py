# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAiInstanceProtectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'list[UpdateAiInstanceProtectionResultItem]'
    }

    attribute_map = {
        'results': 'results'
    }

    def __init__(self, results=None):
        r"""UpdateAiInstanceProtectionResponse

        The model defined in huaweicloud sdk

        :param results: **参数解释**： 每个智能体的处理结果列表 **取值范围**： 不涉及 
        :type results: list[:class:`huaweicloudsdkhss.v5.UpdateAiInstanceProtectionResultItem`]
        """
        
        super().__init__()

        self._results = None
        self.discriminator = None

        if results is not None:
            self.results = results

    @property
    def results(self):
        r"""Gets the results of this UpdateAiInstanceProtectionResponse.

        **参数解释**： 每个智能体的处理结果列表 **取值范围**： 不涉及 

        :return: The results of this UpdateAiInstanceProtectionResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.UpdateAiInstanceProtectionResultItem`]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this UpdateAiInstanceProtectionResponse.

        **参数解释**： 每个智能体的处理结果列表 **取值范围**： 不涉及 

        :param results: The results of this UpdateAiInstanceProtectionResponse.
        :type results: list[:class:`huaweicloudsdkhss.v5.UpdateAiInstanceProtectionResultItem`]
        """
        self._results = results

    def to_dict(self):
        import warnings
        warnings.warn("UpdateAiInstanceProtectionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateAiInstanceProtectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
