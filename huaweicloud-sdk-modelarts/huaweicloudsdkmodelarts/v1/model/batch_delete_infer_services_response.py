# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteInferServicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_responses': 'list[ServiceResponse]'
    }

    attribute_map = {
        'service_responses': 'service_responses'
    }

    def __init__(self, service_responses=None):
        r"""BatchDeleteInferServicesResponse

        The model defined in huaweicloud sdk

        :param service_responses: **参数解释：** 服务响应返回体。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type service_responses: list[:class:`huaweicloudsdkmodelarts.v1.ServiceResponse`]
        """
        
        super().__init__()

        self._service_responses = None
        self.discriminator = None

        if service_responses is not None:
            self.service_responses = service_responses

    @property
    def service_responses(self):
        r"""Gets the service_responses of this BatchDeleteInferServicesResponse.

        **参数解释：** 服务响应返回体。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The service_responses of this BatchDeleteInferServicesResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.ServiceResponse`]
        """
        return self._service_responses

    @service_responses.setter
    def service_responses(self, service_responses):
        r"""Sets the service_responses of this BatchDeleteInferServicesResponse.

        **参数解释：** 服务响应返回体。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param service_responses: The service_responses of this BatchDeleteInferServicesResponse.
        :type service_responses: list[:class:`huaweicloudsdkmodelarts.v1.ServiceResponse`]
        """
        self._service_responses = service_responses

    def to_dict(self):
        import warnings
        warnings.warn("BatchDeleteInferServicesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchDeleteInferServicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
