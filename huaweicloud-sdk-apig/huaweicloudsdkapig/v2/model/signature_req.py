# coding: utf-8

import pprint
import re

import six





class SignatureReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sign_secret': 'str',
        'name': 'str',
        'sign_key': 'str',
        'sign_type': 'str'
    }

    attribute_map = {
        'sign_secret': 'sign_secret',
        'name': 'name',
        'sign_key': 'sign_key',
        'sign_type': 'sign_type'
    }

    def __init__(self, sign_secret=None, name=None, sign_key=None, sign_type=None):
        """SignatureReq - a model defined in huaweicloud sdk"""
        
        

        self._sign_secret = None
        self._name = None
        self._sign_key = None
        self._sign_type = None
        self.discriminator = None

        if sign_secret is not None:
            self.sign_secret = sign_secret
        self.name = name
        if sign_key is not None:
            self.sign_key = sign_key
        if sign_type is not None:
            self.sign_type = sign_type

    @property
    def sign_secret(self):
        """Gets the sign_secret of this SignatureReq.

        签名密钥的密钥。支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母开头，16 ~ 64字符。未填写时后台自动生成。

        :return: The sign_secret of this SignatureReq.
        :rtype: str
        """
        return self._sign_secret

    @sign_secret.setter
    def sign_secret(self, sign_secret):
        """Sets the sign_secret of this SignatureReq.

        签名密钥的密钥。支持英文，数字，下划线，中划线，!，@，#，$，%，且只能以英文字母开头，16 ~ 64字符。未填写时后台自动生成。

        :param sign_secret: The sign_secret of this SignatureReq.
        :type: str
        """
        self._sign_secret = sign_secret

    @property
    def name(self):
        """Gets the name of this SignatureReq.

        签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this SignatureReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SignatureReq.

        签名密钥的名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this SignatureReq.
        :type: str
        """
        self._name = name

    @property
    def sign_key(self):
        """Gets the sign_key of this SignatureReq.

        签名密钥的key。支持英文，数字，下划线，中划线，且只能以英文字母开头，8 ~ 32字符。未填写时后台自动生成。

        :return: The sign_key of this SignatureReq.
        :rtype: str
        """
        return self._sign_key

    @sign_key.setter
    def sign_key(self, sign_key):
        """Sets the sign_key of this SignatureReq.

        签名密钥的key。支持英文，数字，下划线，中划线，且只能以英文字母开头，8 ~ 32字符。未填写时后台自动生成。

        :param sign_key: The sign_key of this SignatureReq.
        :type: str
        """
        self._sign_key = sign_key

    @property
    def sign_type(self):
        """Gets the sign_type of this SignatureReq.

        签名密钥类型。

        :return: The sign_type of this SignatureReq.
        :rtype: str
        """
        return self._sign_type

    @sign_type.setter
    def sign_type(self, sign_type):
        """Sets the sign_type of this SignatureReq.

        签名密钥类型。

        :param sign_type: The sign_type of this SignatureReq.
        :type: str
        """
        self._sign_type = sign_type

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
        if not isinstance(other, SignatureReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
