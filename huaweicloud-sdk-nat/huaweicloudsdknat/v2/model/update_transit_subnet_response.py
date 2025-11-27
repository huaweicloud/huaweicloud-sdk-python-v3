# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTransitSubnetResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'transit_subnet': 'TransitSubnet',
        'request_id': 'str'
    }

    attribute_map = {
        'transit_subnet': 'transit_subnet',
        'request_id': 'request_id'
    }

    def __init__(self, transit_subnet=None, request_id=None):
        r"""UpdateTransitSubnetResponse

        The model defined in huaweicloud sdk

        :param transit_subnet: 
        :type transit_subnet: :class:`huaweicloudsdknat.v2.TransitSubnet`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super().__init__()

        self._transit_subnet = None
        self._request_id = None
        self.discriminator = None

        if transit_subnet is not None:
            self.transit_subnet = transit_subnet
        if request_id is not None:
            self.request_id = request_id

    @property
    def transit_subnet(self):
        r"""Gets the transit_subnet of this UpdateTransitSubnetResponse.

        :return: The transit_subnet of this UpdateTransitSubnetResponse.
        :rtype: :class:`huaweicloudsdknat.v2.TransitSubnet`
        """
        return self._transit_subnet

    @transit_subnet.setter
    def transit_subnet(self, transit_subnet):
        r"""Sets the transit_subnet of this UpdateTransitSubnetResponse.

        :param transit_subnet: The transit_subnet of this UpdateTransitSubnetResponse.
        :type transit_subnet: :class:`huaweicloudsdknat.v2.TransitSubnet`
        """
        self._transit_subnet = transit_subnet

    @property
    def request_id(self):
        r"""Gets the request_id of this UpdateTransitSubnetResponse.

        请求ID

        :return: The request_id of this UpdateTransitSubnetResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this UpdateTransitSubnetResponse.

        请求ID

        :param request_id: The request_id of this UpdateTransitSubnetResponse.
        :type request_id: str
        """
        self._request_id = request_id

    def to_dict(self):
        import warnings
        warnings.warn("UpdateTransitSubnetResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateTransitSubnetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
