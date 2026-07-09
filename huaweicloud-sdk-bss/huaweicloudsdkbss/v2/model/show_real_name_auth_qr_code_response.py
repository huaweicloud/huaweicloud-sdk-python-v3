# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRealNameAuthQrCodeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'qr_code_url': 'str'
    }

    attribute_map = {
        'qr_code_url': 'qr_code_url'
    }

    def __init__(self, qr_code_url=None):
        r"""ShowRealNameAuthQrCodeResponse

        The model defined in huaweicloud sdk

        :param qr_code_url: 人脸实名认证二维码地址。该二维码仅限单次使用，扫描后将自动失效。若未在10分钟内完成扫描，系统将自动作废。
        :type qr_code_url: str
        """
        
        super().__init__()

        self._qr_code_url = None
        self.discriminator = None

        if qr_code_url is not None:
            self.qr_code_url = qr_code_url

    @property
    def qr_code_url(self):
        r"""Gets the qr_code_url of this ShowRealNameAuthQrCodeResponse.

        人脸实名认证二维码地址。该二维码仅限单次使用，扫描后将自动失效。若未在10分钟内完成扫描，系统将自动作废。

        :return: The qr_code_url of this ShowRealNameAuthQrCodeResponse.
        :rtype: str
        """
        return self._qr_code_url

    @qr_code_url.setter
    def qr_code_url(self, qr_code_url):
        r"""Sets the qr_code_url of this ShowRealNameAuthQrCodeResponse.

        人脸实名认证二维码地址。该二维码仅限单次使用，扫描后将自动失效。若未在10分钟内完成扫描，系统将自动作废。

        :param qr_code_url: The qr_code_url of this ShowRealNameAuthQrCodeResponse.
        :type qr_code_url: str
        """
        self._qr_code_url = qr_code_url

    def to_dict(self):
        import warnings
        warnings.warn("ShowRealNameAuthQrCodeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowRealNameAuthQrCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
