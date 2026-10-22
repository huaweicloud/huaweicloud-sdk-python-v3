# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListV2EndpointsResponse(SdkResponse):

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
        'endpoints': 'list[V2EndpointBriefInfo]'
    }

    attribute_map = {
        'total': 'total',
        'endpoints': 'endpoints'
    }

    def __init__(self, total=None, endpoints=None):
        r"""ListV2EndpointsResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释**：总记录数。 **取值范围**：不涉及。 
        :type total: int
        :param endpoints: **参数解释**：端点列表。 
        :type endpoints: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointBriefInfo`]
        """
        
        super().__init__()

        self._total = None
        self._endpoints = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if endpoints is not None:
            self.endpoints = endpoints

    @property
    def total(self):
        r"""Gets the total of this ListV2EndpointsResponse.

        **参数解释**：总记录数。 **取值范围**：不涉及。 

        :return: The total of this ListV2EndpointsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListV2EndpointsResponse.

        **参数解释**：总记录数。 **取值范围**：不涉及。 

        :param total: The total of this ListV2EndpointsResponse.
        :type total: int
        """
        self._total = total

    @property
    def endpoints(self):
        r"""Gets the endpoints of this ListV2EndpointsResponse.

        **参数解释**：端点列表。 

        :return: The endpoints of this ListV2EndpointsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointBriefInfo`]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this ListV2EndpointsResponse.

        **参数解释**：端点列表。 

        :param endpoints: The endpoints of this ListV2EndpointsResponse.
        :type endpoints: list[:class:`huaweicloudsdkaidatalake.v2.V2EndpointBriefInfo`]
        """
        self._endpoints = endpoints

    def to_dict(self):
        import warnings
        warnings.warn("ListV2EndpointsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListV2EndpointsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
