# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateUserByDomainReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'password': 'str',
        'mobile': 'str',
        'areacode': 'str',
        'email': 'str'
    }

    attribute_map = {
        'password': 'password',
        'mobile': 'mobile',
        'areacode': 'areacode',
        'email': 'email'
    }

    def __init__(self, password=None, mobile=None, areacode=None, email=None):
        r"""UpdateUserByDomainReq

        The model defined in huaweicloud sdk

        :param password: 新密码，在8-32位之间支持用户自定义密码长度，至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。
        :type password: str
        :param mobile: 用户手机号，纯数字，长度小于等于32位，当且仅当重置手机号时传入空串。必须与国家码同时存在。
        :type mobile: str
        :param areacode: 国家码，当且仅当重置手机号时传入空串。中国大陆为“0086”
        :type areacode: str
        :param email: 用户邮箱，需符合邮箱格式
        :type email: str
        """
        
        

        self._password = None
        self._mobile = None
        self._areacode = None
        self._email = None
        self.discriminator = None

        if password is not None:
            self.password = password
        if mobile is not None:
            self.mobile = mobile
        if areacode is not None:
            self.areacode = areacode
        if email is not None:
            self.email = email

    @property
    def password(self):
        r"""Gets the password of this UpdateUserByDomainReq.

        新密码，在8-32位之间支持用户自定义密码长度，至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。

        :return: The password of this UpdateUserByDomainReq.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this UpdateUserByDomainReq.

        新密码，在8-32位之间支持用户自定义密码长度，至少包含以下四种字符中的两种： 大写字母、小写字母、数字和特殊字符。

        :param password: The password of this UpdateUserByDomainReq.
        :type password: str
        """
        self._password = password

    @property
    def mobile(self):
        r"""Gets the mobile of this UpdateUserByDomainReq.

        用户手机号，纯数字，长度小于等于32位，当且仅当重置手机号时传入空串。必须与国家码同时存在。

        :return: The mobile of this UpdateUserByDomainReq.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        r"""Sets the mobile of this UpdateUserByDomainReq.

        用户手机号，纯数字，长度小于等于32位，当且仅当重置手机号时传入空串。必须与国家码同时存在。

        :param mobile: The mobile of this UpdateUserByDomainReq.
        :type mobile: str
        """
        self._mobile = mobile

    @property
    def areacode(self):
        r"""Gets the areacode of this UpdateUserByDomainReq.

        国家码，当且仅当重置手机号时传入空串。中国大陆为“0086”

        :return: The areacode of this UpdateUserByDomainReq.
        :rtype: str
        """
        return self._areacode

    @areacode.setter
    def areacode(self, areacode):
        r"""Sets the areacode of this UpdateUserByDomainReq.

        国家码，当且仅当重置手机号时传入空串。中国大陆为“0086”

        :param areacode: The areacode of this UpdateUserByDomainReq.
        :type areacode: str
        """
        self._areacode = areacode

    @property
    def email(self):
        r"""Gets the email of this UpdateUserByDomainReq.

        用户邮箱，需符合邮箱格式

        :return: The email of this UpdateUserByDomainReq.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this UpdateUserByDomainReq.

        用户邮箱，需符合邮箱格式

        :param email: The email of this UpdateUserByDomainReq.
        :type email: str
        """
        self._email = email

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
        if not isinstance(other, UpdateUserByDomainReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
