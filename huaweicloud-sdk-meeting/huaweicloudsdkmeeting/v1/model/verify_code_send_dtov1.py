# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyCodeSendDTOV1:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'send_method': 'str',
        'token': 'str'
    }

    attribute_map = {
        'user': 'user',
        'send_method': 'sendMethod',
        'token': 'token'
    }

    def __init__(self, user=None, send_method=None, token=None):
        """VerifyCodeSendDTOV1

        The model defined in huaweicloud sdk

        :param user: 用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 &gt; 必须和发送滑块验证码时带的用户身份信息相同。 
        :type user: str
        :param send_method: 验证码发送方式。 user类型是用户真实帐号时必选；如果没有选择的话，优先短信方式。 * sms：短信方式 * email：邮件方式 
        :type send_method: str
        :param token: 访问Token字符串。通过[[校验滑块验证码](https://support.huaweicloud.com/api-meeting/meeting_21_0101.html)](tag:hws)[[校验滑块验证码](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0101.html)](tag:hk) 接口获取。
        :type token: str
        """
        
        

        self._user = None
        self._send_method = None
        self._token = None
        self.discriminator = None

        self.user = user
        if send_method is not None:
            self.send_method = send_method
        if token is not None:
            self.token = token

    @property
    def user(self):
        """Gets the user of this VerifyCodeSendDTOV1.

        用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 > 必须和发送滑块验证码时带的用户身份信息相同。 

        :return: The user of this VerifyCodeSendDTOV1.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this VerifyCodeSendDTOV1.

        用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 > 必须和发送滑块验证码时带的用户身份信息相同。 

        :param user: The user of this VerifyCodeSendDTOV1.
        :type user: str
        """
        self._user = user

    @property
    def send_method(self):
        """Gets the send_method of this VerifyCodeSendDTOV1.

        验证码发送方式。 user类型是用户真实帐号时必选；如果没有选择的话，优先短信方式。 * sms：短信方式 * email：邮件方式 

        :return: The send_method of this VerifyCodeSendDTOV1.
        :rtype: str
        """
        return self._send_method

    @send_method.setter
    def send_method(self, send_method):
        """Sets the send_method of this VerifyCodeSendDTOV1.

        验证码发送方式。 user类型是用户真实帐号时必选；如果没有选择的话，优先短信方式。 * sms：短信方式 * email：邮件方式 

        :param send_method: The send_method of this VerifyCodeSendDTOV1.
        :type send_method: str
        """
        self._send_method = send_method

    @property
    def token(self):
        """Gets the token of this VerifyCodeSendDTOV1.

        访问Token字符串。通过[[校验滑块验证码](https://support.huaweicloud.com/api-meeting/meeting_21_0101.html)](tag:hws)[[校验滑块验证码](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0101.html)](tag:hk) 接口获取。

        :return: The token of this VerifyCodeSendDTOV1.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this VerifyCodeSendDTOV1.

        访问Token字符串。通过[[校验滑块验证码](https://support.huaweicloud.com/api-meeting/meeting_21_0101.html)](tag:hws)[[校验滑块验证码](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0101.html)](tag:hk) 接口获取。

        :param token: The token of this VerifyCodeSendDTOV1.
        :type token: str
        """
        self._token = token

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
        if not isinstance(other, VerifyCodeSendDTOV1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
