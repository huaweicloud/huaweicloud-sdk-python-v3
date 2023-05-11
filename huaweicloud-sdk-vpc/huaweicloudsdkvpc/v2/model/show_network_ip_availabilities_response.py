# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNetworkIpAvailabilitiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_ip_availability': 'NetworkIpAvailability'
    }

    attribute_map = {
        'network_ip_availability': 'network_ip_availability'
    }

    def __init__(self, network_ip_availability=None):
        """ShowNetworkIpAvailabilitiesResponse

        The model defined in huaweicloud sdk

        :param network_ip_availability: 
        :type network_ip_availability: :class:`huaweicloudsdkvpc.v2.NetworkIpAvailability`
        """
        
        super(ShowNetworkIpAvailabilitiesResponse, self).__init__()

        self._network_ip_availability = None
        self.discriminator = None

        if network_ip_availability is not None:
            self.network_ip_availability = network_ip_availability

    @property
    def network_ip_availability(self):
        """Gets the network_ip_availability of this ShowNetworkIpAvailabilitiesResponse.

        :return: The network_ip_availability of this ShowNetworkIpAvailabilitiesResponse.
        :rtype: :class:`huaweicloudsdkvpc.v2.NetworkIpAvailability`
        """
        return self._network_ip_availability

    @network_ip_availability.setter
    def network_ip_availability(self, network_ip_availability):
        """Sets the network_ip_availability of this ShowNetworkIpAvailabilitiesResponse.

        :param network_ip_availability: The network_ip_availability of this ShowNetworkIpAvailabilitiesResponse.
        :type network_ip_availability: :class:`huaweicloudsdkvpc.v2.NetworkIpAvailability`
        """
        self._network_ip_availability = network_ip_availability

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowNetworkIpAvailabilitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
