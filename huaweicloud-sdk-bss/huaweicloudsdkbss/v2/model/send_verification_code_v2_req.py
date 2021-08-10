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
        'mobile_phone': 'str',
        'lang': 'str',
        'scene': 'int',
        'customer_id': 'str'
    }

    attribute_map = {
        'receiver_type': 'receiver_type',
        'timeout': 'timeout',
        'mobile_phone': 'mobile_phone',
        'lang': 'lang',
        'scene': 'scene',
        'customer_id': 'customer_id'
    }

    def __init__(self, receiver_type=None, timeout=None, mobile_phone=None, lang=None, scene=None, customer_id=None):
        """SendVerificationCodeV2Req - a model defined in huaweicloud sdk"""
        
        

        self._receiver_type = None
        self._timeout = None
        self._mobile_phone = None
        self._lang = None
        self._scene = None
        self._customer_id = None
        self.discriminator = None

        self.receiver_type = receiver_type
        if timeout is not None:
            self.timeout = timeout
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if lang is not None:
            self.lang = lang
        if scene is not None:
            self.scene = scene
        if customer_id is not None:
            self.customer_id = customer_id

    @property
    def receiver_type(self):
        """Gets the receiver_type of this SendVerificationCodeV2Req.

        发送验证码的类型： 1：发送短信验证码

        :return: The receiver_type of this SendVerificationCodeV2Req.
        :rtype: int
        """
        return self._receiver_type

    @receiver_type.setter
    def receiver_type(self, receiver_type):
        """Sets the receiver_type of this SendVerificationCodeV2Req.

        发送验证码的类型： 1：发送短信验证码

        :param receiver_type: The receiver_type of this SendVerificationCodeV2Req.
        :type: int
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
        :type: int
        """
        self._timeout = timeout

    @property
    def mobile_phone(self):
        """Gets the mobile_phone of this SendVerificationCodeV2Req.

        指定发送验证码的手机号。 目前系统只支持中国手机号。 示例：13XXXXXXXXX

        :return: The mobile_phone of this SendVerificationCodeV2Req.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        """Sets the mobile_phone of this SendVerificationCodeV2Req.

        指定发送验证码的手机号。 目前系统只支持中国手机号。 示例：13XXXXXXXXX

        :param mobile_phone: The mobile_phone of this SendVerificationCodeV2Req.
        :type: str
        """
        self._mobile_phone = mobile_phone

    @property
    def lang(self):
        """Gets the lang of this SendVerificationCodeV2Req.

        根据该参数的取值选择发送短信验证码的语言。 zh-cn：中文en-us：英文

        :return: The lang of this SendVerificationCodeV2Req.
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this SendVerificationCodeV2Req.

        根据该参数的取值选择发送短信验证码的语言。 zh-cn：中文en-us：英文

        :param lang: The lang of this SendVerificationCodeV2Req.
        :type: str
        """
        self._lang = lang

    @property
    def scene(self):
        """Gets the scene of this SendVerificationCodeV2Req.

        验证码使用的场景，目前支持如下场景： 29：注册场景18：个人银行卡实名认证场景 不填写默认为29。

        :return: The scene of this SendVerificationCodeV2Req.
        :rtype: int
        """
        return self._scene

    @scene.setter
    def scene(self, scene):
        """Sets the scene of this SendVerificationCodeV2Req.

        验证码使用的场景，目前支持如下场景： 29：注册场景18：个人银行卡实名认证场景 不填写默认为29。

        :param scene: The scene of this SendVerificationCodeV2Req.
        :type: int
        """
        self._scene = scene

    @property
    def customer_id(self):
        """Gets the customer_id of this SendVerificationCodeV2Req.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。 如果scene=18的时候必填。

        :return: The customer_id of this SendVerificationCodeV2Req.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SendVerificationCodeV2Req.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。 如果scene=18的时候必填。

        :param customer_id: The customer_id of this SendVerificationCodeV2Req.
        :type: str
        """
        self._customer_id = customer_id

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
