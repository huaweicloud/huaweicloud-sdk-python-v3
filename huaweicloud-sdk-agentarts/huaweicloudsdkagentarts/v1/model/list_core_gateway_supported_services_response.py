# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreGatewaySupportedServicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'supported_services': 'list[ListCoreGatewaySupportedServicesItem]'
    }

    attribute_map = {
        'supported_services': 'supported_services'
    }

    def __init__(self, supported_services=None):
        r"""ListCoreGatewaySupportedServicesResponse

        The model defined in huaweicloud sdk

        :param supported_services: **参数解释：** 网关支持的主力核心服务列表。 **取值范围：** 数组长度为1-100个。 
        :type supported_services: list[:class:`huaweicloudsdkagentarts.v1.ListCoreGatewaySupportedServicesItem`]
        """
        
        super().__init__()

        self._supported_services = None
        self.discriminator = None

        if supported_services is not None:
            self.supported_services = supported_services

    @property
    def supported_services(self):
        r"""Gets the supported_services of this ListCoreGatewaySupportedServicesResponse.

        **参数解释：** 网关支持的主力核心服务列表。 **取值范围：** 数组长度为1-100个。 

        :return: The supported_services of this ListCoreGatewaySupportedServicesResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.ListCoreGatewaySupportedServicesItem`]
        """
        return self._supported_services

    @supported_services.setter
    def supported_services(self, supported_services):
        r"""Sets the supported_services of this ListCoreGatewaySupportedServicesResponse.

        **参数解释：** 网关支持的主力核心服务列表。 **取值范围：** 数组长度为1-100个。 

        :param supported_services: The supported_services of this ListCoreGatewaySupportedServicesResponse.
        :type supported_services: list[:class:`huaweicloudsdkagentarts.v1.ListCoreGatewaySupportedServicesItem`]
        """
        self._supported_services = supported_services

    def to_dict(self):
        import warnings
        warnings.warn("ListCoreGatewaySupportedServicesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCoreGatewaySupportedServicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
