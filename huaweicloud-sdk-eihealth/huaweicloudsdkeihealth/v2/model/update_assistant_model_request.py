# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAssistantModelRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vendor_id': 'str',
        'model_id': 'str',
        'body': 'UpdateAssistantModelReq'
    }

    attribute_map = {
        'vendor_id': 'vendor_id',
        'model_id': 'model_id',
        'body': 'body'
    }

    def __init__(self, vendor_id=None, model_id=None, body=None):
        r"""UpdateAssistantModelRequest

        The model defined in huaweicloud sdk

        :param vendor_id: **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type vendor_id: str
        :param model_id: **参数解释**： 模型ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 
        :type model_id: str
        :param body: Body of the UpdateAssistantModelRequest
        :type body: :class:`huaweicloudsdkeihealth.v2.UpdateAssistantModelReq`
        """
        
        

        self._vendor_id = None
        self._model_id = None
        self._body = None
        self.discriminator = None

        self.vendor_id = vendor_id
        self.model_id = model_id
        if body is not None:
            self.body = body

    @property
    def vendor_id(self):
        r"""Gets the vendor_id of this UpdateAssistantModelRequest.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The vendor_id of this UpdateAssistantModelRequest.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        r"""Sets the vendor_id of this UpdateAssistantModelRequest.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param vendor_id: The vendor_id of this UpdateAssistantModelRequest.
        :type vendor_id: str
        """
        self._vendor_id = vendor_id

    @property
    def model_id(self):
        r"""Gets the model_id of this UpdateAssistantModelRequest.

        **参数解释**： 模型ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :return: The model_id of this UpdateAssistantModelRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this UpdateAssistantModelRequest.

        **参数解释**： 模型ID。 **约束限制**： 不涉及 **取值范围**： 仅支持字母、数字、中划线和下划线，长度为[1-128]个字符。 **默认取值**： 不涉及 

        :param model_id: The model_id of this UpdateAssistantModelRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def body(self):
        r"""Gets the body of this UpdateAssistantModelRequest.

        :return: The body of this UpdateAssistantModelRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v2.UpdateAssistantModelReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateAssistantModelRequest.

        :param body: The body of this UpdateAssistantModelRequest.
        :type body: :class:`huaweicloudsdkeihealth.v2.UpdateAssistantModelReq`
        """
        self._body = body

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
        if not isinstance(other, UpdateAssistantModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
