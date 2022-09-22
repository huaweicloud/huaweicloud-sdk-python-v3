# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActiveDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sms_number': 'str',
        'country': 'str',
        'email_addr': 'str'
    }

    attribute_map = {
        'sms_number': 'smsNumber',
        'country': 'country',
        'email_addr': 'emailAddr'
    }

    def __init__(self, sms_number=None, country=None, email_addr=None):
        """ActiveDTO

        The model defined in huaweicloud sdk

        :param sms_number: 手机号。 例如中国大陆手机+86xxxxxxxxxxx。当填写手机号时 “country”参数必填。 &gt; 号码和邮箱必须填一个，若企业未开启短信功能，则邮箱必填。 
        :type sms_number: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param email_addr: 邮件地址。 &gt; 号码和邮箱必须填一个，若企业未开启短信功能，则邮箱必填。 
        :type email_addr: str
        """
        
        

        self._sms_number = None
        self._country = None
        self._email_addr = None
        self.discriminator = None

        if sms_number is not None:
            self.sms_number = sms_number
        if country is not None:
            self.country = country
        if email_addr is not None:
            self.email_addr = email_addr

    @property
    def sms_number(self):
        """Gets the sms_number of this ActiveDTO.

        手机号。 例如中国大陆手机+86xxxxxxxxxxx。当填写手机号时 “country”参数必填。 > 号码和邮箱必须填一个，若企业未开启短信功能，则邮箱必填。 

        :return: The sms_number of this ActiveDTO.
        :rtype: str
        """
        return self._sms_number

    @sms_number.setter
    def sms_number(self, sms_number):
        """Sets the sms_number of this ActiveDTO.

        手机号。 例如中国大陆手机+86xxxxxxxxxxx。当填写手机号时 “country”参数必填。 > 号码和邮箱必须填一个，若企业未开启短信功能，则邮箱必填。 

        :param sms_number: The sms_number of this ActiveDTO.
        :type sms_number: str
        """
        self._sms_number = sms_number

    @property
    def country(self):
        """Gets the country of this ActiveDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this ActiveDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ActiveDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this ActiveDTO.
        :type country: str
        """
        self._country = country

    @property
    def email_addr(self):
        """Gets the email_addr of this ActiveDTO.

        邮件地址。 > 号码和邮箱必须填一个，若企业未开启短信功能，则邮箱必填。 

        :return: The email_addr of this ActiveDTO.
        :rtype: str
        """
        return self._email_addr

    @email_addr.setter
    def email_addr(self, email_addr):
        """Sets the email_addr of this ActiveDTO.

        邮件地址。 > 号码和邮箱必须填一个，若企业未开启短信功能，则邮箱必填。 

        :param email_addr: The email_addr of this ActiveDTO.
        :type email_addr: str
        """
        self._email_addr = email_addr

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
        if not isinstance(other, ActiveDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
