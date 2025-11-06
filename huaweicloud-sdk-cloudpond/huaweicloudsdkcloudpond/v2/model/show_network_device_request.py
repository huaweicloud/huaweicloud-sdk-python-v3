# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNetworkDeviceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_device_id': 'str'
    }

    attribute_map = {
        'network_device_id': 'network_device_id'
    }

    def __init__(self, network_device_id=None):
        r"""ShowNetworkDeviceRequest

        The model defined in huaweicloud sdk

        :param network_device_id: 网络设备ID
        :type network_device_id: str
        """
        
        

        self._network_device_id = None
        self.discriminator = None

        self.network_device_id = network_device_id

    @property
    def network_device_id(self):
        r"""Gets the network_device_id of this ShowNetworkDeviceRequest.

        网络设备ID

        :return: The network_device_id of this ShowNetworkDeviceRequest.
        :rtype: str
        """
        return self._network_device_id

    @network_device_id.setter
    def network_device_id(self, network_device_id):
        r"""Sets the network_device_id of this ShowNetworkDeviceRequest.

        网络设备ID

        :param network_device_id: The network_device_id of this ShowNetworkDeviceRequest.
        :type network_device_id: str
        """
        self._network_device_id = network_device_id

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
        if not isinstance(other, ShowNetworkDeviceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
