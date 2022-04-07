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
        """SendVerificationCodeV2Req - a model defined in huaweicloud sdk"""
        
        

        self._receiver_type = None
        self._timeout = None
        self._email = None
        self._lang = None
        self.discriminator = None

        self.receiver_type = receiver_type
        if timeout is not None:
            self.timeout = timeout
        if email is not None:
            self.email = email
        if lang is not None:
            self.lang = lang

    @property
    def receiver_type(self):
        """Gets the receiver_type of this SendVerificationCodeV2Req.

        |参数名称：发送类型：1：发送短信验证码。2：发送邮件验证码。| |参数的约束及描述：发送类型：1：发送短信验证码。2：发送邮件验证码。|

        :return: The receiver_type of this SendVerificationCodeV2Req.
        :rtype: int
        """
        return self._receiver_type

    @receiver_type.setter
    def receiver_type(self, receiver_type):
        """Sets the receiver_type of this SendVerificationCodeV2Req.

        |参数名称：发送类型：1：发送短信验证码。2：发送邮件验证码。| |参数的约束及描述：发送类型：1：发送短信验证码。2：发送邮件验证码。|

        :param receiver_type: The receiver_type of this SendVerificationCodeV2Req.
        :type: int
        """
        self._receiver_type = receiver_type

    @property
    def timeout(self):
        """Gets the timeout of this SendVerificationCodeV2Req.

        |参数名称：验证码超时时间。如果不填的话，采用系统默认超时时间5分钟。单位：分钟| |参数的约束及描述：验证码超时时间。如果不填的话，采用系统默认超时时间5分钟。单位：分钟|

        :return: The timeout of this SendVerificationCodeV2Req.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this SendVerificationCodeV2Req.

        |参数名称：验证码超时时间。如果不填的话，采用系统默认超时时间5分钟。单位：分钟| |参数的约束及描述：验证码超时时间。如果不填的话，采用系统默认超时时间5分钟。单位：分钟|

        :param timeout: The timeout of this SendVerificationCodeV2Req.
        :type: int
        """
        self._timeout = timeout

    @property
    def email(self):
        """Gets the email of this SendVerificationCodeV2Req.

        |参数名称：指定发送邮箱地址。| |参数约束及描述：指定发送邮箱地址。|

        :return: The email of this SendVerificationCodeV2Req.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SendVerificationCodeV2Req.

        |参数名称：指定发送邮箱地址。| |参数约束及描述：指定发送邮箱地址。|

        :param email: The email of this SendVerificationCodeV2Req.
        :type: str
        """
        self._email = email

    @property
    def lang(self):
        """Gets the lang of this SendVerificationCodeV2Req.

        |参数名称：根据语言如果查询不到对应模板信息，就取系统默认语言对应的模板信息。zh-cn：中文；en-us：英文。| |参数约束及描述：根据语言如果查询不到对应模板信息，就取系统默认语言对应的模板信息。zh-cn：中文；en-us：英文。|

        :return: The lang of this SendVerificationCodeV2Req.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this SendVerificationCodeV2Req.

        |参数名称：根据语言如果查询不到对应模板信息，就取系统默认语言对应的模板信息。zh-cn：中文；en-us：英文。| |参数约束及描述：根据语言如果查询不到对应模板信息，就取系统默认语言对应的模板信息。zh-cn：中文；en-us：英文。|

        :param lang: The lang of this SendVerificationCodeV2Req.
        :type: str
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
