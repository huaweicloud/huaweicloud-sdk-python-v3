# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNetworkDeviceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_device': 'NetworkDevice'
    }

    attribute_map = {
        'network_device': 'network_device'
    }

    def __init__(self, network_device=None):
        r"""ShowNetworkDeviceResponse

        The model defined in huaweicloud sdk

        :param network_device: 
        :type network_device: :class:`huaweicloudsdkcloudpond.v2.NetworkDevice`
        """
        
        super().__init__()

        self._network_device = None
        self.discriminator = None

        if network_device is not None:
            self.network_device = network_device

    @property
    def network_device(self):
        r"""Gets the network_device of this ShowNetworkDeviceResponse.

        :return: The network_device of this ShowNetworkDeviceResponse.
        :rtype: :class:`huaweicloudsdkcloudpond.v2.NetworkDevice`
        """
        return self._network_device

    @network_device.setter
    def network_device(self, network_device):
        r"""Sets the network_device of this ShowNetworkDeviceResponse.

        :param network_device: The network_device of this ShowNetworkDeviceResponse.
        :type network_device: :class:`huaweicloudsdkcloudpond.v2.NetworkDevice`
        """
        self._network_device = network_device

    def to_dict(self):
        import warnings
        warnings.warn("ShowNetworkDeviceResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowNetworkDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
