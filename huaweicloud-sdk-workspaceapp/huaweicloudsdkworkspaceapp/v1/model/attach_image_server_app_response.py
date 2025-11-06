# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachImageServerAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uri': 'str'
    }

    attribute_map = {
        'uri': 'uri'
    }

    def __init__(self, uri=None):
        r"""AttachImageServerAppResponse

        The model defined in huaweicloud sdk

        :param uri: 分发软件信息的URI。
        :type uri: str
        """
        
        super().__init__()

        self._uri = None
        self.discriminator = None

        if uri is not None:
            self.uri = uri

    @property
    def uri(self):
        r"""Gets the uri of this AttachImageServerAppResponse.

        分发软件信息的URI。

        :return: The uri of this AttachImageServerAppResponse.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this AttachImageServerAppResponse.

        分发软件信息的URI。

        :param uri: The uri of this AttachImageServerAppResponse.
        :type uri: str
        """
        self._uri = uri

    def to_dict(self):
        import warnings
        warnings.warn("AttachImageServerAppResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, AttachImageServerAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
