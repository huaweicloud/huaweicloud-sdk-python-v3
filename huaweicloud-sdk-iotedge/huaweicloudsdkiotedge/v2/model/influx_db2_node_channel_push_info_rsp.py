# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InfluxDB2NodeChannelPushInfoRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_data': 'DeviceInfluxDB2NodeChannelPushInfoDetail'
    }

    attribute_map = {
        'device_data': 'device_data'
    }

    def __init__(self, device_data=None):
        r"""InfluxDB2NodeChannelPushInfoRsp

        The model defined in huaweicloud sdk

        :param device_data: 
        :type device_data: :class:`huaweicloudsdkiotedge.v2.DeviceInfluxDB2NodeChannelPushInfoDetail`
        """
        
        

        self._device_data = None
        self.discriminator = None

        if device_data is not None:
            self.device_data = device_data

    @property
    def device_data(self):
        r"""Gets the device_data of this InfluxDB2NodeChannelPushInfoRsp.

        :return: The device_data of this InfluxDB2NodeChannelPushInfoRsp.
        :rtype: :class:`huaweicloudsdkiotedge.v2.DeviceInfluxDB2NodeChannelPushInfoDetail`
        """
        return self._device_data

    @device_data.setter
    def device_data(self, device_data):
        r"""Sets the device_data of this InfluxDB2NodeChannelPushInfoRsp.

        :param device_data: The device_data of this InfluxDB2NodeChannelPushInfoRsp.
        :type device_data: :class:`huaweicloudsdkiotedge.v2.DeviceInfluxDB2NodeChannelPushInfoDetail`
        """
        self._device_data = device_data

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
        if not isinstance(other, InfluxDB2NodeChannelPushInfoRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
