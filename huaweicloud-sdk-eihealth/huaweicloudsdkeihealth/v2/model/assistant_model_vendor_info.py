# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssistantModelVendorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor_name': 'str',
        'vendor_type': 'str',
        'models': 'list[ModelInfo]'
    }

    attribute_map = {
        'vendor_name': 'vendor_name',
        'vendor_type': 'vendor_type',
        'models': 'models'
    }

    def __init__(self, vendor_name=None, vendor_type=None, models=None):
        r"""AssistantModelVendorInfo

        The model defined in huaweicloud sdk

        :param vendor_name: **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type vendor_name: str
        :param vendor_type: **参数解释**： 模型供应商类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM：预置供应商 * CUSTOM：自定义供应商 **默认取值**： 不涉及 
        :type vendor_type: str
        :param models: **参数解释**： 供应商模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type models: list[:class:`huaweicloudsdkeihealth.v2.ModelInfo`]
        """
        
        

        self._vendor_name = None
        self._vendor_type = None
        self._models = None
        self.discriminator = None

        if vendor_name is not None:
            self.vendor_name = vendor_name
        if vendor_type is not None:
            self.vendor_type = vendor_type
        if models is not None:
            self.models = models

    @property
    def vendor_name(self):
        r"""Gets the vendor_name of this AssistantModelVendorInfo.

        **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The vendor_name of this AssistantModelVendorInfo.
        :rtype: str
        """
        return self._vendor_name

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        r"""Sets the vendor_name of this AssistantModelVendorInfo.

        **参数解释**： 模型供应商名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param vendor_name: The vendor_name of this AssistantModelVendorInfo.
        :type vendor_name: str
        """
        self._vendor_name = vendor_name

    @property
    def vendor_type(self):
        r"""Gets the vendor_type of this AssistantModelVendorInfo.

        **参数解释**： 模型供应商类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM：预置供应商 * CUSTOM：自定义供应商 **默认取值**： 不涉及 

        :return: The vendor_type of this AssistantModelVendorInfo.
        :rtype: str
        """
        return self._vendor_type

    @vendor_type.setter
    def vendor_type(self, vendor_type):
        r"""Sets the vendor_type of this AssistantModelVendorInfo.

        **参数解释**： 模型供应商类型。 **约束限制**： 不涉及 **取值范围**： * SYSTEM：预置供应商 * CUSTOM：自定义供应商 **默认取值**： 不涉及 

        :param vendor_type: The vendor_type of this AssistantModelVendorInfo.
        :type vendor_type: str
        """
        self._vendor_type = vendor_type

    @property
    def models(self):
        r"""Gets the models of this AssistantModelVendorInfo.

        **参数解释**： 供应商模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The models of this AssistantModelVendorInfo.
        :rtype: list[:class:`huaweicloudsdkeihealth.v2.ModelInfo`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this AssistantModelVendorInfo.

        **参数解释**： 供应商模型列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param models: The models of this AssistantModelVendorInfo.
        :type models: list[:class:`huaweicloudsdkeihealth.v2.ModelInfo`]
        """
        self._models = models

    def to_dict(self):
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
        if not isinstance(other, AssistantModelVendorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
