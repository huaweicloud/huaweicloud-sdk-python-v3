# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCorpAdminResultDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'account': 'str',
        'name': 'str',
        'admin_type': 'int',
        'email': 'str',
        'phone': 'str',
        'country': 'str',
        'dept': 'DeptBasicDTO'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'name': 'name',
        'admin_type': 'adminType',
        'email': 'email',
        'phone': 'phone',
        'country': 'country',
        'dept': 'dept'
    }

    def __init__(self, id=None, account=None, name=None, admin_type=None, email=None, phone=None, country=None, dept=None):
        r"""QueryCorpAdminResultDTO

        The model defined in huaweicloud sdk

        :param id: 用户UUID。
        :type id: str
        :param account: 用户帐号（华为云会议帐号）。
        :type account: str
        :param name: 用户名称。
        :type name: str
        :param admin_type: 管理员类型。 * 0：默认管理员 * 1：普通管理员 
        :type admin_type: int
        :param email: 邮箱地址。
        :type email: str
        :param phone: 手机号。
        :type phone: str
        :param country: [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 
        :type country: str
        :param dept: 
        :type dept: :class:`huaweicloudsdkmeeting.v1.DeptBasicDTO`
        """
        
        

        self._id = None
        self._account = None
        self._name = None
        self._admin_type = None
        self._email = None
        self._phone = None
        self._country = None
        self._dept = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account is not None:
            self.account = account
        if name is not None:
            self.name = name
        if admin_type is not None:
            self.admin_type = admin_type
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if country is not None:
            self.country = country
        if dept is not None:
            self.dept = dept

    @property
    def id(self):
        r"""Gets the id of this QueryCorpAdminResultDTO.

        用户UUID。

        :return: The id of this QueryCorpAdminResultDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryCorpAdminResultDTO.

        用户UUID。

        :param id: The id of this QueryCorpAdminResultDTO.
        :type id: str
        """
        self._id = id

    @property
    def account(self):
        r"""Gets the account of this QueryCorpAdminResultDTO.

        用户帐号（华为云会议帐号）。

        :return: The account of this QueryCorpAdminResultDTO.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this QueryCorpAdminResultDTO.

        用户帐号（华为云会议帐号）。

        :param account: The account of this QueryCorpAdminResultDTO.
        :type account: str
        """
        self._account = account

    @property
    def name(self):
        r"""Gets the name of this QueryCorpAdminResultDTO.

        用户名称。

        :return: The name of this QueryCorpAdminResultDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryCorpAdminResultDTO.

        用户名称。

        :param name: The name of this QueryCorpAdminResultDTO.
        :type name: str
        """
        self._name = name

    @property
    def admin_type(self):
        r"""Gets the admin_type of this QueryCorpAdminResultDTO.

        管理员类型。 * 0：默认管理员 * 1：普通管理员 

        :return: The admin_type of this QueryCorpAdminResultDTO.
        :rtype: int
        """
        return self._admin_type

    @admin_type.setter
    def admin_type(self, admin_type):
        r"""Sets the admin_type of this QueryCorpAdminResultDTO.

        管理员类型。 * 0：默认管理员 * 1：普通管理员 

        :param admin_type: The admin_type of this QueryCorpAdminResultDTO.
        :type admin_type: int
        """
        self._admin_type = admin_type

    @property
    def email(self):
        r"""Gets the email of this QueryCorpAdminResultDTO.

        邮箱地址。

        :return: The email of this QueryCorpAdminResultDTO.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this QueryCorpAdminResultDTO.

        邮箱地址。

        :param email: The email of this QueryCorpAdminResultDTO.
        :type email: str
        """
        self._email = email

    @property
    def phone(self):
        r"""Gets the phone of this QueryCorpAdminResultDTO.

        手机号。

        :return: The phone of this QueryCorpAdminResultDTO.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        r"""Sets the phone of this QueryCorpAdminResultDTO.

        手机号。

        :param phone: The phone of this QueryCorpAdminResultDTO.
        :type phone: str
        """
        self._phone = phone

    @property
    def country(self):
        r"""Gets the country of this QueryCorpAdminResultDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :return: The country of this QueryCorpAdminResultDTO.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        r"""Sets the country of this QueryCorpAdminResultDTO.

        [[手机号所属的国家](https://support.huaweicloud.com/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hws)[[手机号所属的国家](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0109.html#ZH-CN_TOPIC_0212714591__table19371178135314)](tag:hk) 。 

        :param country: The country of this QueryCorpAdminResultDTO.
        :type country: str
        """
        self._country = country

    @property
    def dept(self):
        r"""Gets the dept of this QueryCorpAdminResultDTO.

        :return: The dept of this QueryCorpAdminResultDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.DeptBasicDTO`
        """
        return self._dept

    @dept.setter
    def dept(self, dept):
        r"""Sets the dept of this QueryCorpAdminResultDTO.

        :param dept: The dept of this QueryCorpAdminResultDTO.
        :type dept: :class:`huaweicloudsdkmeeting.v1.DeptBasicDTO`
        """
        self._dept = dept

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
        if not isinstance(other, QueryCorpAdminResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
