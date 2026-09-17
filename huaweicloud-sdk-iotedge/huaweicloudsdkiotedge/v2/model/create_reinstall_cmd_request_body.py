# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReinstallCmdRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_secret': 'str',
        'verify_code': 'str'
    }

    attribute_map = {
        'device_secret': 'device_secret',
        'verify_code': 'verify_code'
    }

    def __init__(self, device_secret=None, verify_code=None):
        r"""CreateReinstallCmdRequestBody

        The model defined in huaweicloud sdk

        :param device_secret: 边缘节点设备密钥，如果不输入则平台随机生成
        :type device_secret: str
        :param verify_code: 边缘节点注册使用的验证码，如果不输入则平台随机生成。
        :type verify_code: str
        """
        
        

        self._device_secret = None
        self._verify_code = None
        self.discriminator = None

        if device_secret is not None:
            self.device_secret = device_secret
        if verify_code is not None:
            self.verify_code = verify_code

    @property
    def device_secret(self):
        r"""Gets the device_secret of this CreateReinstallCmdRequestBody.

        边缘节点设备密钥，如果不输入则平台随机生成

        :return: The device_secret of this CreateReinstallCmdRequestBody.
        :rtype: str
        """
        return self._device_secret

    @device_secret.setter
    def device_secret(self, device_secret):
        r"""Sets the device_secret of this CreateReinstallCmdRequestBody.

        边缘节点设备密钥，如果不输入则平台随机生成

        :param device_secret: The device_secret of this CreateReinstallCmdRequestBody.
        :type device_secret: str
        """
        self._device_secret = device_secret

    @property
    def verify_code(self):
        r"""Gets the verify_code of this CreateReinstallCmdRequestBody.

        边缘节点注册使用的验证码，如果不输入则平台随机生成。

        :return: The verify_code of this CreateReinstallCmdRequestBody.
        :rtype: str
        """
        return self._verify_code

    @verify_code.setter
    def verify_code(self, verify_code):
        r"""Sets the verify_code of this CreateReinstallCmdRequestBody.

        边缘节点注册使用的验证码，如果不输入则平台随机生成。

        :param verify_code: The verify_code of this CreateReinstallCmdRequestBody.
        :type verify_code: str
        """
        self._verify_code = verify_code

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
        if not isinstance(other, CreateReinstallCmdRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
