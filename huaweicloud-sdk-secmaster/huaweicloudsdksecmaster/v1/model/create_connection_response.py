# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'message': 'str',
        'asset': 'AssetInfoResponseBody'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'asset': 'asset'
    }

    def __init__(self, code=None, message=None, asset=None):
        r"""CreateConnectionResponse

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: str
        :param message: 错误信息
        :type message: str
        :param asset: 
        :type asset: :class:`huaweicloudsdksecmaster.v1.AssetInfoResponseBody`
        """
        
        super().__init__()

        self._code = None
        self._message = None
        self._asset = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if asset is not None:
            self.asset = asset

    @property
    def code(self):
        r"""Gets the code of this CreateConnectionResponse.

        错误码

        :return: The code of this CreateConnectionResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this CreateConnectionResponse.

        错误码

        :param code: The code of this CreateConnectionResponse.
        :type code: str
        """
        self._code = code

    @property
    def message(self):
        r"""Gets the message of this CreateConnectionResponse.

        错误信息

        :return: The message of this CreateConnectionResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this CreateConnectionResponse.

        错误信息

        :param message: The message of this CreateConnectionResponse.
        :type message: str
        """
        self._message = message

    @property
    def asset(self):
        r"""Gets the asset of this CreateConnectionResponse.

        :return: The asset of this CreateConnectionResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v1.AssetInfoResponseBody`
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        r"""Sets the asset of this CreateConnectionResponse.

        :param asset: The asset of this CreateConnectionResponse.
        :type asset: :class:`huaweicloudsdksecmaster.v1.AssetInfoResponseBody`
        """
        self._asset = asset

    def to_dict(self):
        import warnings
        warnings.warn("CreateConnectionResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
