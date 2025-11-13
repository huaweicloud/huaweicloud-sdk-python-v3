# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelVendorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'model_vendors': 'list[ModelVendor]',
        'count': 'int'
    }

    attribute_map = {
        'model_vendors': 'model_vendors',
        'count': 'count'
    }

    def __init__(self, model_vendors=None, count=None):
        r"""ListModelVendorsResponse

        The model defined in huaweicloud sdk

        :param model_vendors: **参数解释**： 模型供应商列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type model_vendors: list[:class:`huaweicloudsdkeihealth.v2.ModelVendor`]
        :param count: **参数解释**： 模型供应商个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type count: int
        """
        
        super().__init__()

        self._model_vendors = None
        self._count = None
        self.discriminator = None

        if model_vendors is not None:
            self.model_vendors = model_vendors
        if count is not None:
            self.count = count

    @property
    def model_vendors(self):
        r"""Gets the model_vendors of this ListModelVendorsResponse.

        **参数解释**： 模型供应商列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The model_vendors of this ListModelVendorsResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v2.ModelVendor`]
        """
        return self._model_vendors

    @model_vendors.setter
    def model_vendors(self, model_vendors):
        r"""Sets the model_vendors of this ListModelVendorsResponse.

        **参数解释**： 模型供应商列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param model_vendors: The model_vendors of this ListModelVendorsResponse.
        :type model_vendors: list[:class:`huaweicloudsdkeihealth.v2.ModelVendor`]
        """
        self._model_vendors = model_vendors

    @property
    def count(self):
        r"""Gets the count of this ListModelVendorsResponse.

        **参数解释**： 模型供应商个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The count of this ListModelVendorsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListModelVendorsResponse.

        **参数解释**： 模型供应商个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param count: The count of this ListModelVendorsResponse.
        :type count: int
        """
        self._count = count

    def to_dict(self):
        import warnings
        warnings.warn("ListModelVendorsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListModelVendorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
