# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MqttNodeChannelDetailDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_info': 'MqttNodeChannelConnectionInfoResp',
        'push_info': 'MqttNodeChannelPushInfoRsp'
    }

    attribute_map = {
        'connection_info': 'connection_info',
        'push_info': 'push_info'
    }

    def __init__(self, connection_info=None, push_info=None):
        r"""MqttNodeChannelDetailDTO

        The model defined in huaweicloud sdk

        :param connection_info: 
        :type connection_info: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelConnectionInfoResp`
        :param push_info: 
        :type push_info: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelPushInfoRsp`
        """
        
        

        self._connection_info = None
        self._push_info = None
        self.discriminator = None

        if connection_info is not None:
            self.connection_info = connection_info
        if push_info is not None:
            self.push_info = push_info

    @property
    def connection_info(self):
        r"""Gets the connection_info of this MqttNodeChannelDetailDTO.

        :return: The connection_info of this MqttNodeChannelDetailDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelConnectionInfoResp`
        """
        return self._connection_info

    @connection_info.setter
    def connection_info(self, connection_info):
        r"""Sets the connection_info of this MqttNodeChannelDetailDTO.

        :param connection_info: The connection_info of this MqttNodeChannelDetailDTO.
        :type connection_info: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelConnectionInfoResp`
        """
        self._connection_info = connection_info

    @property
    def push_info(self):
        r"""Gets the push_info of this MqttNodeChannelDetailDTO.

        :return: The push_info of this MqttNodeChannelDetailDTO.
        :rtype: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelPushInfoRsp`
        """
        return self._push_info

    @push_info.setter
    def push_info(self, push_info):
        r"""Sets the push_info of this MqttNodeChannelDetailDTO.

        :param push_info: The push_info of this MqttNodeChannelDetailDTO.
        :type push_info: :class:`huaweicloudsdkiotedge.v2.MqttNodeChannelPushInfoRsp`
        """
        self._push_info = push_info

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
        if not isinstance(other, MqttNodeChannelDetailDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
