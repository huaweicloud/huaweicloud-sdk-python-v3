# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CorpBasicDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'domain': 'str',
        'phone': 'str',
        'country': 'str',
        'fax': 'str',
        'email': 'str',
        'address': 'str',
        'description': 'str',
        'sp_id': 'str',
        'language': 'str',
        'time_zone_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'domain': 'domain',
        'phone': 'phone',
        'country': 'country',
        'fax': 'fax',
        'email': 'email',
        'address': 'address',
        'description': 'description',
        'sp_id': 'spId',
        'language': 'language',
        'time_zone_id': 'timeZoneId'
    }

    def __init__(self, name=None, domain=None, phone=None, country=None, fax=None, email=None, address=None, description=None, sp_id=None, language=None, time_zone_id=None):
        """CorpBasicDTO

        The model defined in huaweicloud sdk

        :param name: 企业名称，格式必须满足^[^#%&amp;&#39;+;&lt;&gt;&#x3D;\\\&quot;&#39;？?\\\\\\\\……/]*$。
        :type name: str
        :param domain: 企业域名。
        :type domain: str
        :param phone: 手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时， “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)。
        :type phone: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param fax: 传真号码,格式必须满足(^$|^[+]?[0-9]+$)。
        :type fax: str
        :param email: 邮箱地址,格式必须满足(^$|^[\\\\w-+]+(\\\\.[\\\\w-+]+)*@[\\\\w-]+(\\\\.[\\\\w-]+)*(\\\\.[\\\\w-]{1,})$)。
        :type email: str
        :param address: 地址。
        :type address: str
        :param description: 备注。
        :type description: str
        :param sp_id: 企业归属的SP ID。仅在查询时返回。
        :type sp_id: str
        :param language: 企业提示音语言设置,zh-CN或en-US。
        :type language: str
        :param time_zone_id: 时区Id设置,例如北京东8区timeZoneId值为56,时区Id和时区的对应关系请参考: [[时区表](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html)](tag:hws)[[时区表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html)](tag:hk) 。 
        :type time_zone_id: str
        """
        
        

        self._name = None
        self._domain = None
        self._phone = None
        self._country = None
        self._fax = None
        self._email = None
        self._address = None
        self._description = None
        self._sp_id = None
        self._language = None
        self._time_zone_id = None
        self.discriminator = None

        self.name = name
        if domain is not None:
            self.domain = domain
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if fax is not None:
            self.fax = fax
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address
        if description is not None:
            self.description = description
        if sp_id is not None:
            self.sp_id = sp_id
        if language is not None:
            self.language = language
        if time_zone_id is not None:
            self.time_zone_id = time_zone_id

    @property
    def name(self):
        """Gets the name of this CorpBasicDTO.

        企业名称，格式必须满足^[^#%&'+;<>=\\\"'？?\\\\\\\\……/]*$。

        :return: The name of this CorpBasicDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CorpBasicDTO.

        企业名称，格式必须满足^[^#%&'+;<>=\\\"'？?\\\\\\\\……/]*$。

        :param name: The name of this CorpBasicDTO.
        :type name: str
        """
        self._name = name

    @property
    def domain(self):
        """Gets the domain of this CorpBasicDTO.

        企业域名。

        :return: The domain of this CorpBasicDTO.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CorpBasicDTO.

        企业域名。

        :param domain: The domain of this CorpBasicDTO.
        :type domain: str
        """
        self._domain = domain

    @property
    def phone(self):
        """Gets the phone of this CorpBasicDTO.

        手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时， “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)。

        :return: The phone of this CorpBasicDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CorpBasicDTO.

        手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时， “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)。

        :param phone: The phone of this CorpBasicDTO.
        :type phone: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this CorpBasicDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this CorpBasicDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CorpBasicDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this CorpBasicDTO.
        :type country: str
        """
        self._country = country

    @property
    def fax(self):
        """Gets the fax of this CorpBasicDTO.

        传真号码,格式必须满足(^$|^[+]?[0-9]+$)。

        :return: The fax of this CorpBasicDTO.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this CorpBasicDTO.

        传真号码,格式必须满足(^$|^[+]?[0-9]+$)。

        :param fax: The fax of this CorpBasicDTO.
        :type fax: str
        """
        self._fax = fax

    @property
    def email(self):
        """Gets the email of this CorpBasicDTO.

        邮箱地址,格式必须满足(^$|^[\\\\w-+]+(\\\\.[\\\\w-+]+)*@[\\\\w-]+(\\\\.[\\\\w-]+)*(\\\\.[\\\\w-]{1,})$)。

        :return: The email of this CorpBasicDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CorpBasicDTO.

        邮箱地址,格式必须满足(^$|^[\\\\w-+]+(\\\\.[\\\\w-+]+)*@[\\\\w-]+(\\\\.[\\\\w-]+)*(\\\\.[\\\\w-]{1,})$)。

        :param email: The email of this CorpBasicDTO.
        :type email: str
        """
        self._email = email

    @property
    def address(self):
        """Gets the address of this CorpBasicDTO.

        地址。

        :return: The address of this CorpBasicDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CorpBasicDTO.

        地址。

        :param address: The address of this CorpBasicDTO.
        :type address: str
        """
        self._address = address

    @property
    def description(self):
        """Gets the description of this CorpBasicDTO.

        备注。

        :return: The description of this CorpBasicDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CorpBasicDTO.

        备注。

        :param description: The description of this CorpBasicDTO.
        :type description: str
        """
        self._description = description

    @property
    def sp_id(self):
        """Gets the sp_id of this CorpBasicDTO.

        企业归属的SP ID。仅在查询时返回。

        :return: The sp_id of this CorpBasicDTO.
        :rtype: str
        """
        return self._sp_id

    @sp_id.setter
    def sp_id(self, sp_id):
        """Sets the sp_id of this CorpBasicDTO.

        企业归属的SP ID。仅在查询时返回。

        :param sp_id: The sp_id of this CorpBasicDTO.
        :type sp_id: str
        """
        self._sp_id = sp_id

    @property
    def language(self):
        """Gets the language of this CorpBasicDTO.

        企业提示音语言设置,zh-CN或en-US。

        :return: The language of this CorpBasicDTO.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CorpBasicDTO.

        企业提示音语言设置,zh-CN或en-US。

        :param language: The language of this CorpBasicDTO.
        :type language: str
        """
        self._language = language

    @property
    def time_zone_id(self):
        """Gets the time_zone_id of this CorpBasicDTO.

        时区Id设置,例如北京东8区timeZoneId值为56,时区Id和时区的对应关系请参考: [[时区表](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html)](tag:hws)[[时区表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html)](tag:hk) 。 

        :return: The time_zone_id of this CorpBasicDTO.
        :rtype: str
        """
        return self._time_zone_id

    @time_zone_id.setter
    def time_zone_id(self, time_zone_id):
        """Sets the time_zone_id of this CorpBasicDTO.

        时区Id设置,例如北京东8区timeZoneId值为56,时区Id和时区的对应关系请参考: [[时区表](https://support.huaweicloud.com/api-meeting/meeting_21_0110.html)](tag:hws)[[时区表](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0110.html)](tag:hk) 。 

        :param time_zone_id: The time_zone_id of this CorpBasicDTO.
        :type time_zone_id: str
        """
        self._time_zone_id = time_zone_id

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
        if not isinstance(other, CorpBasicDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
