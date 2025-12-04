# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadHttpSignCertResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str'
    }

    attribute_map = {
        'content_type': 'content-type'
    }

    def __init__(self, content_type=None):
        r"""DownloadHttpSignCertResponse

        The model defined in huaweicloud sdk

        :param content_type: 
        :type content_type: str
        """
        
        super().__init__()

        self._content_type = None
        self.discriminator = None

        if content_type is not None:
            self.content_type = content_type

    @property
    def content_type(self):
        r"""Gets the content_type of this DownloadHttpSignCertResponse.

        :return: The content_type of this DownloadHttpSignCertResponse.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this DownloadHttpSignCertResponse.

        :param content_type: The content_type of this DownloadHttpSignCertResponse.
        :type content_type: str
        """
        self._content_type = content_type

    def to_dict(self):
        import warnings
        warnings.warn("DownloadHttpSignCertResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, DownloadHttpSignCertResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
