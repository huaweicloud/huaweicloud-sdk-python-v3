# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginCaptchaConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enabled': 'bool',
        'trigger_threshold': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'trigger_threshold': 'trigger_threshold'
    }

    def __init__(self, enabled=None, trigger_threshold=None):
        r"""LoginCaptchaConfig

        The model defined in huaweicloud sdk

        :param enabled: 是否开启滑块验证码。
        :type enabled: bool
        :param trigger_threshold: 用户登录失败 trigger_threshold 次后开始要求验证码认证。验证码不启用时无意义，启用时若不传默认为 3。
        :type trigger_threshold: int
        """
        
        

        self._enabled = None
        self._trigger_threshold = None
        self.discriminator = None

        if enabled is not None:
            self.enabled = enabled
        if trigger_threshold is not None:
            self.trigger_threshold = trigger_threshold

    @property
    def enabled(self):
        r"""Gets the enabled of this LoginCaptchaConfig.

        是否开启滑块验证码。

        :return: The enabled of this LoginCaptchaConfig.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this LoginCaptchaConfig.

        是否开启滑块验证码。

        :param enabled: The enabled of this LoginCaptchaConfig.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def trigger_threshold(self):
        r"""Gets the trigger_threshold of this LoginCaptchaConfig.

        用户登录失败 trigger_threshold 次后开始要求验证码认证。验证码不启用时无意义，启用时若不传默认为 3。

        :return: The trigger_threshold of this LoginCaptchaConfig.
        :rtype: int
        """
        return self._trigger_threshold

    @trigger_threshold.setter
    def trigger_threshold(self, trigger_threshold):
        r"""Sets the trigger_threshold of this LoginCaptchaConfig.

        用户登录失败 trigger_threshold 次后开始要求验证码认证。验证码不启用时无意义，启用时若不传默认为 3。

        :param trigger_threshold: The trigger_threshold of this LoginCaptchaConfig.
        :type trigger_threshold: int
        """
        self._trigger_threshold = trigger_threshold

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
        if not isinstance(other, LoginCaptchaConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
