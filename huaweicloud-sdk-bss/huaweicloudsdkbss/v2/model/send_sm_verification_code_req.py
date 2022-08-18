# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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

    def __init__(self, mobile_phone=None, timeout=None, language=None, sm_template_args=None):
        """SendSmVerificationCodeReq

        The model defined in huaweicloud sdk

        :param mobile_phone: 接受短信验证码的手机号码。
        :type mobile_phone: str
        :param timeout: 超时时间，默认值为10分钟。 单位：分钟
        :type timeout: int
        :param language: 发送的短信的语言。 zh-cn: 中文en-us: 英语 默认为偏好设置的默认语言。
        :type language: str
        :param sm_template_args: 短信发送模板中的变量，具体参见表1。
        :type sm_template_args: list[:class:`huaweicloudsdkbss.v2.TemplateArgs`]
        """
        
        

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

        接受短信验证码的手机号码。

        :return: The mobile_phone of this SendSmVerificationCodeReq.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this SendSmVerificationCodeReq.

        接受短信验证码的手机号码。

        :param mobile_phone: The mobile_phone of this SendSmVerificationCodeReq.
        :type mobile_phone: str
        """
        self._mobile_phone = mobile_phone

    @property
    def timeout(self):
        """Gets the timeout of this SendSmVerificationCodeReq.

        超时时间，默认值为10分钟。 单位：分钟

        :return: The timeout of this SendSmVerificationCodeReq.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this SendSmVerificationCodeReq.

        超时时间，默认值为10分钟。 单位：分钟

        :param timeout: The timeout of this SendSmVerificationCodeReq.
        :type timeout: int
        """
        self._timeout = timeout

    @property
    def language(self):
        """Gets the language of this SendSmVerificationCodeReq.

        发送的短信的语言。 zh-cn: 中文en-us: 英语 默认为偏好设置的默认语言。

        :return: The language of this SendSmVerificationCodeReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SendSmVerificationCodeReq.

        发送的短信的语言。 zh-cn: 中文en-us: 英语 默认为偏好设置的默认语言。

        :param language: The language of this SendSmVerificationCodeReq.
        :type language: str
        """
        self._language = language

    @property
    def sm_template_args(self):
        """Gets the sm_template_args of this SendSmVerificationCodeReq.

        短信发送模板中的变量，具体参见表1。

        :return: The sm_template_args of this SendSmVerificationCodeReq.
        :rtype: list[:class:`huaweicloudsdkbss.v2.TemplateArgs`]
        """
        return self._sm_template_args

    @sm_template_args.setter
    def sm_template_args(self, sm_template_args):
        """Sets the sm_template_args of this SendSmVerificationCodeReq.

        短信发送模板中的变量，具体参见表1。

        :param sm_template_args: The sm_template_args of this SendSmVerificationCodeReq.
        :type sm_template_args: list[:class:`huaweicloudsdkbss.v2.TemplateArgs`]
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
        if not isinstance(other, SendSmVerificationCodeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
