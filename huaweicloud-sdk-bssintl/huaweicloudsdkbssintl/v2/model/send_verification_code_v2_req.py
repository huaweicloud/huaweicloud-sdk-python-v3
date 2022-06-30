# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SendVerificationCodeV2Req:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'receiver_type': 'int',
        'timeout': 'int',
        'email': 'str',
        'lang': 'str'
    }

    attribute_map = {
        'receiver_type': 'receiver_type',
        'timeout': 'timeout',
        'email': 'email',
        'lang': 'lang'
    }

    def __init__(self, receiver_type=None, timeout=None, email=None, lang=None):
        """SendVerificationCodeV2Req

        The model defined in huaweicloud sdk

        :param receiver_type: 发送验证码的类型： 2：发送邮件验证码
        :type receiver_type: int
        :param timeout: 发送验证码的超时时间。 如果不填的话，采用系统默认超时时间5分钟。 单位：分钟
        :type timeout: int
        :param email: 指定发送验证码的邮箱地址。
        :type email: str
        :param lang: 根据该参数的取值选择发送邮件验证码的语言。 zh-cn：中文en-us：英文
        :type lang: str
        """
        
        

        self._receiver_type = None
        self._timeout = None
        self._email = None
        self._lang = None
        self.discriminator = None

        self.receiver_type = receiver_type
        if timeout is not None:
            self.timeout = timeout
        self.email = email
        if lang is not None:
            self.lang = lang

    @property
    def receiver_type(self):
        """Gets the receiver_type of this SendVerificationCodeV2Req.

        发送验证码的类型： 2：发送邮件验证码

        :return: The receiver_type of this SendVerificationCodeV2Req.
        :rtype: int
        """
        return self._receiver_type

    @receiver_type.setter
    def receiver_type(self, receiver_type):
        """Sets the receiver_type of this SendVerificationCodeV2Req.

        发送验证码的类型： 2：发送邮件验证码

        :param receiver_type: The receiver_type of this SendVerificationCodeV2Req.
        :type receiver_type: int
        """
        self._receiver_type = receiver_type

    @property
    def timeout(self):
        """Gets the timeout of this SendVerificationCodeV2Req.

        发送验证码的超时时间。 如果不填的话，采用系统默认超时时间5分钟。 单位：分钟

        :return: The timeout of this SendVerificationCodeV2Req.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this SendVerificationCodeV2Req.

        发送验证码的超时时间。 如果不填的话，采用系统默认超时时间5分钟。 单位：分钟

        :param timeout: The timeout of this SendVerificationCodeV2Req.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def email(self):
        """Gets the email of this SendVerificationCodeV2Req.

        指定发送验证码的邮箱地址。

        :return: The email of this SendVerificationCodeV2Req.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SendVerificationCodeV2Req.

        指定发送验证码的邮箱地址。

        :param email: The email of this SendVerificationCodeV2Req.
        :type email: str
        """
        self._email = email

    @property
    def lang(self):
        """Gets the lang of this SendVerificationCodeV2Req.

        根据该参数的取值选择发送邮件验证码的语言。 zh-cn：中文en-us：英文

        :return: The lang of this SendVerificationCodeV2Req.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this SendVerificationCodeV2Req.

        根据该参数的取值选择发送邮件验证码的语言。 zh-cn：中文en-us：英文

        :param lang: The lang of this SendVerificationCodeV2Req.
        :type lang: str
        """
        self._lang = lang

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
        if not isinstance(other, SendVerificationCodeV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
