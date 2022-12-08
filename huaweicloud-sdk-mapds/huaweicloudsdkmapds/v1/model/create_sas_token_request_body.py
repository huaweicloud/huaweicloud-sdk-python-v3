# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSasTokenRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'keytype': 'str',
        'expiry': 'str'
    }

    attribute_map = {
        'keytype': 'keytype',
        'expiry': 'expiry'
    }

    def __init__(self, keytype=None, expiry=None):
        """CreateSasTokenRequestBody

        The model defined in huaweicloud sdk

        :param keytype: 用于为用户生成令牌的密钥  取值为primary或者secondary  每个用户只有2个apikey，primary的原则就是对比apiKey时间最早的那个。  如果只有一个apikey，primary和secondary都指同一个apiKey
        :type keytype: str
        :param expiry: 令牌到期UTC时间，格式如：2019-04-21T00:44:24Z   日期符合以下格式： yyyy-MM-ddTHH:mm:ssZ 由 ISO 8601 标准指定。  最小值不小于15min，最大值不超过24h
        :type expiry: str
        """
        
        

        self._keytype = None
        self._expiry = None
        self.discriminator = None

        self.keytype = keytype
        self.expiry = expiry

    @property
    def keytype(self):
        """Gets the keytype of this CreateSasTokenRequestBody.

        用于为用户生成令牌的密钥  取值为primary或者secondary  每个用户只有2个apikey，primary的原则就是对比apiKey时间最早的那个。  如果只有一个apikey，primary和secondary都指同一个apiKey

        :return: The keytype of this CreateSasTokenRequestBody.
        :rtype: str
        """
        return self._keytype

    @keytype.setter
    def keytype(self, keytype):
        """Sets the keytype of this CreateSasTokenRequestBody.

        用于为用户生成令牌的密钥  取值为primary或者secondary  每个用户只有2个apikey，primary的原则就是对比apiKey时间最早的那个。  如果只有一个apikey，primary和secondary都指同一个apiKey

        :param keytype: The keytype of this CreateSasTokenRequestBody.
        :type keytype: str
        """
        self._keytype = keytype

    @property
    def expiry(self):
        """Gets the expiry of this CreateSasTokenRequestBody.

        令牌到期UTC时间，格式如：2019-04-21T00:44:24Z   日期符合以下格式： yyyy-MM-ddTHH:mm:ssZ 由 ISO 8601 标准指定。  最小值不小于15min，最大值不超过24h

        :return: The expiry of this CreateSasTokenRequestBody.
        :rtype: str
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this CreateSasTokenRequestBody.

        令牌到期UTC时间，格式如：2019-04-21T00:44:24Z   日期符合以下格式： yyyy-MM-ddTHH:mm:ssZ 由 ISO 8601 标准指定。  最小值不小于15min，最大值不超过24h

        :param expiry: The expiry of this CreateSasTokenRequestBody.
        :type expiry: str
        """
        self._expiry = expiry

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
        if not isinstance(other, CreateSasTokenRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
