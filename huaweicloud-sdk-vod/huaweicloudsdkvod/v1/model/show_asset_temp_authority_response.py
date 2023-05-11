# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAssetTempAuthorityResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sign_str': 'str'
    }

    attribute_map = {
        'sign_str': 'sign_str'
    }

    def __init__(self, sign_str=None):
        """ShowAssetTempAuthorityResponse

        The model defined in huaweicloud sdk

        :param sign_str: 带授权签名字符串的URL。具体调用示例请参见[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。  示例：https://{obs_domain}/{bucket}?AWSAccessKeyId&#x3D;{AccessKeyID}&amp;Expires&#x3D;{ExpiresValue}&amp;Signature&#x3D;{Signature}
        :type sign_str: str
        """
        
        super(ShowAssetTempAuthorityResponse, self).__init__()

        self._sign_str = None
        self.discriminator = None

        if sign_str is not None:
            self.sign_str = sign_str

    @property
    def sign_str(self):
        """Gets the sign_str of this ShowAssetTempAuthorityResponse.

        带授权签名字符串的URL。具体调用示例请参见[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。  示例：https://{obs_domain}/{bucket}?AWSAccessKeyId={AccessKeyID}&Expires={ExpiresValue}&Signature={Signature}

        :return: The sign_str of this ShowAssetTempAuthorityResponse.
        :rtype: str
        """
        return self._sign_str

    @sign_str.setter
    def sign_str(self, sign_str):
        """Sets the sign_str of this ShowAssetTempAuthorityResponse.

        带授权签名字符串的URL。具体调用示例请参见[示例2：媒资分段上传（20M以上）](https://support.huaweicloud.com/api-vod/vod_04_0216.html)。  示例：https://{obs_domain}/{bucket}?AWSAccessKeyId={AccessKeyID}&Expires={ExpiresValue}&Signature={Signature}

        :param sign_str: The sign_str of this ShowAssetTempAuthorityResponse.
        :type sign_str: str
        """
        self._sign_str = sign_str

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
        if not isinstance(other, ShowAssetTempAuthorityResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
