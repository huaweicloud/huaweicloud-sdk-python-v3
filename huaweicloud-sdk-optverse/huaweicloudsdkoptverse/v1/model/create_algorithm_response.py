# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlgorithmResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'meta_info': 'MetaInfo',
        'payload': 'PayloadObject'
    }

    attribute_map = {
        'meta_info': 'meta_info',
        'payload': 'payload'
    }

    def __init__(self, meta_info=None, payload=None):
        r"""CreateAlgorithmResponse

        The model defined in huaweicloud sdk

        :param meta_info: 
        :type meta_info: :class:`huaweicloudsdkoptverse.v1.MetaInfo`
        :param payload: 
        :type payload: :class:`huaweicloudsdkoptverse.v1.PayloadObject`
        """
        
        super().__init__()

        self._meta_info = None
        self._payload = None
        self.discriminator = None

        if meta_info is not None:
            self.meta_info = meta_info
        if payload is not None:
            self.payload = payload

    @property
    def meta_info(self):
        r"""Gets the meta_info of this CreateAlgorithmResponse.

        :return: The meta_info of this CreateAlgorithmResponse.
        :rtype: :class:`huaweicloudsdkoptverse.v1.MetaInfo`
        """
        return self._meta_info

    @meta_info.setter
    def meta_info(self, meta_info):
        r"""Sets the meta_info of this CreateAlgorithmResponse.

        :param meta_info: The meta_info of this CreateAlgorithmResponse.
        :type meta_info: :class:`huaweicloudsdkoptverse.v1.MetaInfo`
        """
        self._meta_info = meta_info

    @property
    def payload(self):
        r"""Gets the payload of this CreateAlgorithmResponse.

        :return: The payload of this CreateAlgorithmResponse.
        :rtype: :class:`huaweicloudsdkoptverse.v1.PayloadObject`
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        r"""Sets the payload of this CreateAlgorithmResponse.

        :param payload: The payload of this CreateAlgorithmResponse.
        :type payload: :class:`huaweicloudsdkoptverse.v1.PayloadObject`
        """
        self._payload = payload

    def to_dict(self):
        import warnings
        warnings.warn("CreateAlgorithmResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateAlgorithmResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
