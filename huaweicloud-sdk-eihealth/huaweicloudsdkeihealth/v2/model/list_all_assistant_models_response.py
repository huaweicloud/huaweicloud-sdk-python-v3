# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllAssistantModelsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendors': 'list[AssistantModelVendorInfo]',
        'count': 'int'
    }

    attribute_map = {
        'vendors': 'vendors',
        'count': 'count'
    }

    def __init__(self, vendors=None, count=None):
        r"""ListAllAssistantModelsResponse

        The model defined in huaweicloud sdk

        :param vendors: **参数解释**： 供应商列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type vendors: list[:class:`huaweicloudsdkeihealth.v2.AssistantModelVendorInfo`]
        :param count: **参数解释**： 供应商个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type count: int
        """
        
        super().__init__()

        self._vendors = None
        self._count = None
        self.discriminator = None

        if vendors is not None:
            self.vendors = vendors
        if count is not None:
            self.count = count

    @property
    def vendors(self):
        r"""Gets the vendors of this ListAllAssistantModelsResponse.

        **参数解释**： 供应商列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The vendors of this ListAllAssistantModelsResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v2.AssistantModelVendorInfo`]
        """
        return self._vendors

    @vendors.setter
    def vendors(self, vendors):
        r"""Sets the vendors of this ListAllAssistantModelsResponse.

        **参数解释**： 供应商列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param vendors: The vendors of this ListAllAssistantModelsResponse.
        :type vendors: list[:class:`huaweicloudsdkeihealth.v2.AssistantModelVendorInfo`]
        """
        self._vendors = vendors

    @property
    def count(self):
        r"""Gets the count of this ListAllAssistantModelsResponse.

        **参数解释**： 供应商个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The count of this ListAllAssistantModelsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAllAssistantModelsResponse.

        **参数解释**： 供应商个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param count: The count of this ListAllAssistantModelsResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListAllAssistantModelsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAllAssistantModelsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
