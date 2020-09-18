# coding: utf-8

import pprint
import re

import six





class SendSmVerificationCodeReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mobile_phone': 'str',
        'timeout': 'int',
        'language': 'str',
        'sm_template_args': 'list[TemplateArgs]'
    }

    attribute_map = {
        'mobile_phone': 'mobile_phone',
        'timeout': 'timeout',
        'language': 'language',
        'sm_template_args': 'sm_template_args'
    }

    def __init__(self, mobile_phone=None, timeout=10, language=None, sm_template_args=None):
        """SendSmVerificationCodeReq - a model defined in huaweicloud sdk"""
        
        

        self._mobile_phone = None
        self._timeout = None
        self._language = None
        self._sm_template_args = None
        self.discriminator = None

        self.mobile_phone = mobile_phone
        if timeout is not None:
            self.timeout = timeout
        if language is not None:
            self.language = language
        if sm_template_args is not None:
            self.sm_template_args = sm_template_args

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this SendSmVerificationCodeReq.

        |参数名称：手机号| |参数约束及描述：手机号|

        :return: The mobile_phone of this SendSmVerificationCodeReq.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this SendSmVerificationCodeReq.

        |参数名称：手机号| |参数约束及描述：手机号|

        :param mobile_phone: The mobile_phone of this SendSmVerificationCodeReq.
        :type: str
        """
        self._mobile_phone = mobile_phone

    @property
    def timeout(self):
        """Gets the timeout of this SendSmVerificationCodeReq.

        |参数名称：超时时间，单位是分钟| |参数的约束及描述：超时时间，单位是分钟，短信传递10，邮箱传递60|

        :return: The timeout of this SendSmVerificationCodeReq.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this SendSmVerificationCodeReq.

        |参数名称：超时时间，单位是分钟| |参数的约束及描述：超时时间，单位是分钟，短信传递10，邮箱传递60|

        :param timeout: The timeout of this SendSmVerificationCodeReq.
        :type: int
        """
        self._timeout = timeout

    @property
    def language(self):
        """Gets the language of this SendSmVerificationCodeReq.

        |参数名称：发送的短信的语言zh-cn: 中文en-us: 英语| |参数约束及描述：发送的短信的语言zh-cn: 中文en-us: 英语|

        :return: The language of this SendSmVerificationCodeReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SendSmVerificationCodeReq.

        |参数名称：发送的短信的语言zh-cn: 中文en-us: 英语| |参数约束及描述：发送的短信的语言zh-cn: 中文en-us: 英语|

        :param language: The language of this SendSmVerificationCodeReq.
        :type: str
        """
        self._language = language

    @property
    def sm_template_args(self):
        """Gets the sm_template_args of this SendSmVerificationCodeReq.

        |参数名称：短信模板参数| |参数约束以及描述：短信模板参数|

        :return: The sm_template_args of this SendSmVerificationCodeReq.
        :rtype: list[TemplateArgs]
        """
        return self._sm_template_args

    @sm_template_args.setter
    def sm_template_args(self, sm_template_args):
        """Sets the sm_template_args of this SendSmVerificationCodeReq.

        |参数名称：短信模板参数| |参数约束以及描述：短信模板参数|

        :param sm_template_args: The sm_template_args of this SendSmVerificationCodeReq.
        :type: list[TemplateArgs]
        """
        self._sm_template_args = sm_template_args

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendSmVerificationCodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
