# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdminDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account': 'str',
        'name': 'str',
        'pwd': 'str',
        'email': 'str',
        'phone': 'str',
        'country': 'str'
    }

    attribute_map = {
        'account': 'account',
        'name': 'name',
        'pwd': 'pwd',
        'email': 'email',
        'phone': 'phone',
        'country': 'country'
    }

    def __init__(self, account=None, name=None, pwd=None, email=None, phone=None, country=None):
        """AdminDTO

        The model defined in huaweicloud sdk

        :param account: 用户帐号，帐号只能包含大小写字母、数字、_、-、.、@符号，不能为纯数字和@后面带.号。
        :type account: str
        :param name: 名称。
        :type name: str
        :param pwd: 若携带则以前台携带为准，否则后台默认生成,密码必须满足: * 6-32位 * 不能和帐号的正序和倒序一致 * 至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（&#x60; ~ ! @ # $ % ^ &amp; * ( ) - _ &#x3D; + \\ | [ { } ] ; : \\\&quot; ,&#39; &lt; . &gt; / ?
        :type pwd: str
        :param email: 邮箱，管理员手机和邮箱必填其一，否则无法重置密码。如果企业短信开关关闭，则邮箱必填。格式必须满足(^$|^[\\\\w-+]+(\\\\.[\\\\w-+]+)*@[\\\\w-]+(\\\\.[\\\\w-]+)*(\\\\.[\\\\w-]{1,})$)。
        :type email: str
        :param phone: 手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时 “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)。
        :type phone: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        """
        
        

        self._account = None
        self._name = None
        self._pwd = None
        self._email = None
        self._phone = None
        self._country = None
        self.discriminator = None

        self.account = account
        self.name = name
        self.pwd = pwd
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country

    @property
    def account(self):
        """Gets the account of this AdminDTO.

        用户帐号，帐号只能包含大小写字母、数字、_、-、.、@符号，不能为纯数字和@后面带.号。

        :return: The account of this AdminDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AdminDTO.

        用户帐号，帐号只能包含大小写字母、数字、_、-、.、@符号，不能为纯数字和@后面带.号。

        :param account: The account of this AdminDTO.
        :type account: str
        """
        self._account = account

    @property
    def name(self):
        """Gets the name of this AdminDTO.

        名称。

        :return: The name of this AdminDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AdminDTO.

        名称。

        :param name: The name of this AdminDTO.
        :type name: str
        """
        self._name = name

    @property
    def pwd(self):
        """Gets the pwd of this AdminDTO.

        若携带则以前台携带为准，否则后台默认生成,密码必须满足: * 6-32位 * 不能和帐号的正序和倒序一致 * 至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（` ~ ! @ # $ % ^ & * ( ) - _ = + \\ | [ { } ] ; : \\\" ,' < . > / ?

        :return: The pwd of this AdminDTO.
        :rtype: str
        """
        return self._pwd

    @pwd.setter
    def pwd(self, pwd):
        """Sets the pwd of this AdminDTO.

        若携带则以前台携带为准，否则后台默认生成,密码必须满足: * 6-32位 * 不能和帐号的正序和倒序一致 * 至少包含两种字符类型：小写字母、大写字母、数字、特殊字符（` ~ ! @ # $ % ^ & * ( ) - _ = + \\ | [ { } ] ; : \\\" ,' < . > / ?

        :param pwd: The pwd of this AdminDTO.
        :type pwd: str
        """
        self._pwd = pwd

    @property
    def email(self):
        """Gets the email of this AdminDTO.

        邮箱，管理员手机和邮箱必填其一，否则无法重置密码。如果企业短信开关关闭，则邮箱必填。格式必须满足(^$|^[\\\\w-+]+(\\\\.[\\\\w-+]+)*@[\\\\w-]+(\\\\.[\\\\w-]+)*(\\\\.[\\\\w-]{1,})$)。

        :return: The email of this AdminDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AdminDTO.

        邮箱，管理员手机和邮箱必填其一，否则无法重置密码。如果企业短信开关关闭，则邮箱必填。格式必须满足(^$|^[\\\\w-+]+(\\\\.[\\\\w-+]+)*@[\\\\w-]+(\\\\.[\\\\w-]+)*(\\\\.[\\\\w-]{1,})$)。

        :param email: The email of this AdminDTO.
        :type email: str
        """
        self._email = email

    @property
    def phone(self):
        """Gets the phone of this AdminDTO.

        手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时 “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)。

        :return: The phone of this AdminDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this AdminDTO.

        手机号，必须加上国家码，例如中国大陆手机+86xxxxxxx，当填写手机号时 “country”参数必填,手机格式必须满足(^$|^[+]?[0-9]+$)。

        :param phone: The phone of this AdminDTO.
        :type phone: str
        """
        self._phone = phone

    @property
    def country(self):
        """Gets the country of this AdminDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this AdminDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this AdminDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this AdminDTO.
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
        if not isinstance(other, AdminDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
