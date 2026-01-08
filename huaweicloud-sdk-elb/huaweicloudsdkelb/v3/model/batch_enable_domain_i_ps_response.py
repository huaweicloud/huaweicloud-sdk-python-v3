# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchEnableDomainIPsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ips': 'list[ListDnsIpResponseBody]'
    }

    attribute_map = {
        'ips': 'ips'
    }

    def __init__(self, ips=None):
        r"""BatchEnableDomainIPsResponse

        The model defined in huaweicloud sdk

        :param ips: **参数解释**：返回的负载均衡器的dns ip信息。  **约束限制**：如果负载均衡器的公网域名和私网域名开关都没有打开，则列表为空。  **取值范围**：不涉及  **默认取值**：不涉及
        :type ips: list[:class:`huaweicloudsdkelb.v3.ListDnsIpResponseBody`]
        """
        
        super().__init__()

        self._ips = None
        self.discriminator = None

        if ips is not None:
            self.ips = ips

    @property
    def ips(self):
        r"""Gets the ips of this BatchEnableDomainIPsResponse.

        **参数解释**：返回的负载均衡器的dns ip信息。  **约束限制**：如果负载均衡器的公网域名和私网域名开关都没有打开，则列表为空。  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The ips of this BatchEnableDomainIPsResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.ListDnsIpResponseBody`]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this BatchEnableDomainIPsResponse.

        **参数解释**：返回的负载均衡器的dns ip信息。  **约束限制**：如果负载均衡器的公网域名和私网域名开关都没有打开，则列表为空。  **取值范围**：不涉及  **默认取值**：不涉及

        :param ips: The ips of this BatchEnableDomainIPsResponse.
        :type ips: list[:class:`huaweicloudsdkelb.v3.ListDnsIpResponseBody`]
        """
        self._ips = ips

    def to_dict(self):
        import warnings
        warnings.warn("BatchEnableDomainIPsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchEnableDomainIPsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
