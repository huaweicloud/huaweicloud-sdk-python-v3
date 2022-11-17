# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerificationCodeDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'contact': 'str',
        'verification_code': 'str',
        'country': 'str'
    }

    attribute_map = {
        'contact': 'contact',
        'verification_code': 'verificationCode',
        'country': 'country'
    }

    def __init__(self, contact=None, verification_code=None, country=None):
        """VerificationCodeDTO

        The model defined in huaweicloud sdk

        :param contact: 后台自动识别是手机号还是邮箱。 如果为手机号，必须加上国家码，例如中国大陆手机为“+86xxxxxxxxxxx”，当填写手机号时 “country”参数必填。 
        :type contact: str
        :param verification_code: 验证码，在校验的场景时需要携带。
        :type verification_code: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        """
        
        

        self._contact = None
        self._verification_code = None
        self._country = None
        self.discriminator = None

        self.contact = contact
        if verification_code is not None:
            self.verification_code = verification_code
        if country is not None:
            self.country = country

    @property
    def contact(self):
        """Gets the contact of this VerificationCodeDTO.

        后台自动识别是手机号还是邮箱。 如果为手机号，必须加上国家码，例如中国大陆手机为“+86xxxxxxxxxxx”，当填写手机号时 “country”参数必填。 

        :return: The contact of this VerificationCodeDTO.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this VerificationCodeDTO.

        后台自动识别是手机号还是邮箱。 如果为手机号，必须加上国家码，例如中国大陆手机为“+86xxxxxxxxxxx”，当填写手机号时 “country”参数必填。 

        :param contact: The contact of this VerificationCodeDTO.
        :type contact: str
        """
        self._contact = contact

    @property
    def verification_code(self):
        """Gets the verification_code of this VerificationCodeDTO.

        验证码，在校验的场景时需要携带。

        :return: The verification_code of this VerificationCodeDTO.
        :rtype: str
        """
        return self._verification_code

    @verification_code.setter
    def verification_code(self, verification_code):
        """Sets the verification_code of this VerificationCodeDTO.

        验证码，在校验的场景时需要携带。

        :param verification_code: The verification_code of this VerificationCodeDTO.
        :type verification_code: str
        """
        self._verification_code = verification_code

    @property
    def country(self):
        """Gets the country of this VerificationCodeDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this VerificationCodeDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this VerificationCodeDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this VerificationCodeDTO.
        :type country: str
        """
        self._country = country

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
        if not isinstance(other, VerificationCodeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
