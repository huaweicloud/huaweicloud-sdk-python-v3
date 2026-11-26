# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAssetFileDownLoadPathResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'signedurl': 'str'
    }

    attribute_map = {
        'signedurl': 'signedurl'
    }

    def __init__(self, signedurl=None):
        r"""CreateAssetFileDownLoadPathResponse

        The model defined in huaweicloud sdk

        :param signedurl: **参数解释**：资产文件下载临时路径。
        :type signedurl: str
        """
        
        super().__init__()

        self._signedurl = None
        self.discriminator = None

        if signedurl is not None:
            self.signedurl = signedurl

    @property
    def signedurl(self):
        r"""Gets the signedurl of this CreateAssetFileDownLoadPathResponse.

        **参数解释**：资产文件下载临时路径。

        :return: The signedurl of this CreateAssetFileDownLoadPathResponse.
        :rtype: str
        """
        return self._signedurl

    @signedurl.setter
    def signedurl(self, signedurl):
        r"""Sets the signedurl of this CreateAssetFileDownLoadPathResponse.

        **参数解释**：资产文件下载临时路径。

        :param signedurl: The signedurl of this CreateAssetFileDownLoadPathResponse.
        :type signedurl: str
        """
        self._signedurl = signedurl

    def to_dict(self):
        import warnings
        warnings.warn("CreateAssetFileDownLoadPathResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateAssetFileDownLoadPathResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
