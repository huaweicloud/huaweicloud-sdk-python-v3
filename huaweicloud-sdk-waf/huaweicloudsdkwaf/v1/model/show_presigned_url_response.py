# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPresignedUrlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'presigned_url': 'str',
        'expire': 'int'
    }

    attribute_map = {
        'presigned_url': 'presigned_url',
        'expire': 'expire'
    }

    def __init__(self, presigned_url=None, expire=None):
        r"""ShowPresignedUrlResponse

        The model defined in huaweicloud sdk

        :param presigned_url: 预签名URL
        :type presigned_url: str
        :param expire: 过期时间（秒）
        :type expire: int
        """
        
        super().__init__()

        self._presigned_url = None
        self._expire = None
        self.discriminator = None

        if presigned_url is not None:
            self.presigned_url = presigned_url
        if expire is not None:
            self.expire = expire

    @property
    def presigned_url(self):
        r"""Gets the presigned_url of this ShowPresignedUrlResponse.

        预签名URL

        :return: The presigned_url of this ShowPresignedUrlResponse.
        :rtype: str
        """
        return self._presigned_url

    @presigned_url.setter
    def presigned_url(self, presigned_url):
        r"""Sets the presigned_url of this ShowPresignedUrlResponse.

        预签名URL

        :param presigned_url: The presigned_url of this ShowPresignedUrlResponse.
        :type presigned_url: str
        """
        self._presigned_url = presigned_url

    @property
    def expire(self):
        r"""Gets the expire of this ShowPresignedUrlResponse.

        过期时间（秒）

        :return: The expire of this ShowPresignedUrlResponse.
        :rtype: int
        """
        return self._expire

    @expire.setter
    def expire(self, expire):
        r"""Sets the expire of this ShowPresignedUrlResponse.

        过期时间（秒）

        :param expire: The expire of this ShowPresignedUrlResponse.
        :type expire: int
        """
        self._expire = expire

    def to_dict(self):
        import warnings
        warnings.warn("ShowPresignedUrlResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowPresignedUrlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
