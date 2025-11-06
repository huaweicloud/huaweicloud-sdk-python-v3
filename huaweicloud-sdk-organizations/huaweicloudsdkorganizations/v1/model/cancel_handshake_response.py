# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelHandshakeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'handshake': 'HandshakeDto'
    }

    attribute_map = {
        'handshake': 'handshake'
    }

    def __init__(self, handshake=None):
        r"""CancelHandshakeResponse

        The model defined in huaweicloud sdk

        :param handshake: 
        :type handshake: :class:`huaweicloudsdkorganizations.v1.HandshakeDto`
        """
        
        super().__init__()

        self._handshake = None
        self.discriminator = None

        if handshake is not None:
            self.handshake = handshake

    @property
    def handshake(self):
        r"""Gets the handshake of this CancelHandshakeResponse.

        :return: The handshake of this CancelHandshakeResponse.
        :rtype: :class:`huaweicloudsdkorganizations.v1.HandshakeDto`
        """
        return self._handshake

    @handshake.setter
    def handshake(self, handshake):
        r"""Sets the handshake of this CancelHandshakeResponse.

        :param handshake: The handshake of this CancelHandshakeResponse.
        :type handshake: :class:`huaweicloudsdkorganizations.v1.HandshakeDto`
        """
        self._handshake = handshake

    def to_dict(self):
        import warnings
        warnings.warn("CancelHandshakeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CancelHandshakeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
