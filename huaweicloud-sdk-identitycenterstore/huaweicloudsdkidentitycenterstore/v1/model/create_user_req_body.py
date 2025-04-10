# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('display_name')
    sensitive_list.append('locale')
    sensitive_list.append('nickname')
    sensitive_list.append('preferred_language')
    sensitive_list.append('profile_url')
    sensitive_list.append('timezone')
    sensitive_list.append('title')
    sensitive_list.append('user_type')

    openapi_types = {
        'addresses': 'list[AddressDto]',
        'display_name': 'str',
        'emails': 'list[EmailDto]',
        'locale': 'str',
        'name': 'NameDto',
        'nickname': 'str',
        'phone_numbers': 'list[PhoneNumberDto]',
        'preferred_language': 'str',
        'profile_url': 'str',
        'timezone': 'str',
        'title': 'str',
        'user_name': 'str',
        'user_type': 'str',
        'password_mode': 'str',
        'enterprise': 'EnterpriseDto'
    }

    attribute_map = {
        'addresses': 'addresses',
        'display_name': 'display_name',
        'emails': 'emails',
        'locale': 'locale',
        'name': 'name',
        'nickname': 'nickname',
        'phone_numbers': 'phone_numbers',
        'preferred_language': 'preferred_language',
        'profile_url': 'profile_url',
        'timezone': 'timezone',
        'title': 'title',
        'user_name': 'user_name',
        'user_type': 'user_type',
        'password_mode': 'password_mode',
        'enterprise': 'enterprise'
    }

    def __init__(self, addresses=None, display_name=None, emails=None, locale=None, name=None, nickname=None, phone_numbers=None, preferred_language=None, profile_url=None, timezone=None, title=None, user_name=None, user_type=None, password_mode=None, enterprise=None):
        r"""CreateUserReqBody

        The model defined in huaweicloud sdk

        :param addresses: 用户的地址信息列表
        :type addresses: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        :param display_name: 用户的显示名称
        :type display_name: str
        :param emails: 用户的电子邮箱信息列表
        :type emails: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        :param locale: 用户的地理区域或位置信息
        :type locale: str
        :param name: 
        :type name: :class:`huaweicloudsdkidentitycenterstore.v1.NameDto`
        :param nickname: 用户昵称
        :type nickname: str
        :param phone_numbers: 用户的电话号码信息列表
        :type phone_numbers: list[:class:`huaweicloudsdkidentitycenterstore.v1.PhoneNumberDto`]
        :param preferred_language: 用户语言首选项
        :type preferred_language: str
        :param profile_url: 与用户关联的URL
        :type profile_url: str
        :param timezone: 用户时区
        :type timezone: str
        :param title: 用户头衔
        :type title: str
        :param user_name: 用户名，用于标识用户的唯一字符串
        :type user_name: str
        :param user_type: 用户类型
        :type user_type: str
        :param password_mode: 初始化密码方式，一次性密码/邮箱
        :type password_mode: str
        :param enterprise: 
        :type enterprise: :class:`huaweicloudsdkidentitycenterstore.v1.EnterpriseDto`
        """
        
        

        self._addresses = None
        self._display_name = None
        self._emails = None
        self._locale = None
        self._name = None
        self._nickname = None
        self._phone_numbers = None
        self._preferred_language = None
        self._profile_url = None
        self._timezone = None
        self._title = None
        self._user_name = None
        self._user_type = None
        self._password_mode = None
        self._enterprise = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        self.display_name = display_name
        self.emails = emails
        if locale is not None:
            self.locale = locale
        self.name = name
        if nickname is not None:
            self.nickname = nickname
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if preferred_language is not None:
            self.preferred_language = preferred_language
        if profile_url is not None:
            self.profile_url = profile_url
        if timezone is not None:
            self.timezone = timezone
        if title is not None:
            self.title = title
        self.user_name = user_name
        if user_type is not None:
            self.user_type = user_type
        self.password_mode = password_mode
        if enterprise is not None:
            self.enterprise = enterprise

    @property
    def addresses(self):
        r"""Gets the addresses of this CreateUserReqBody.

        用户的地址信息列表

        :return: The addresses of this CreateUserReqBody.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this CreateUserReqBody.

        用户的地址信息列表

        :param addresses: The addresses of this CreateUserReqBody.
        :type addresses: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        """
        self._addresses = addresses

    @property
    def display_name(self):
        r"""Gets the display_name of this CreateUserReqBody.

        用户的显示名称

        :return: The display_name of this CreateUserReqBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this CreateUserReqBody.

        用户的显示名称

        :param display_name: The display_name of this CreateUserReqBody.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def emails(self):
        r"""Gets the emails of this CreateUserReqBody.

        用户的电子邮箱信息列表

        :return: The emails of this CreateUserReqBody.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        r"""Sets the emails of this CreateUserReqBody.

        用户的电子邮箱信息列表

        :param emails: The emails of this CreateUserReqBody.
        :type emails: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        """
        self._emails = emails

    @property
    def locale(self):
        r"""Gets the locale of this CreateUserReqBody.

        用户的地理区域或位置信息

        :return: The locale of this CreateUserReqBody.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this CreateUserReqBody.

        用户的地理区域或位置信息

        :param locale: The locale of this CreateUserReqBody.
        :type locale: str
        """
        self._locale = locale

    @property
    def name(self):
        r"""Gets the name of this CreateUserReqBody.

        :return: The name of this CreateUserReqBody.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.NameDto`
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateUserReqBody.

        :param name: The name of this CreateUserReqBody.
        :type name: :class:`huaweicloudsdkidentitycenterstore.v1.NameDto`
        """
        self._name = name

    @property
    def nickname(self):
        r"""Gets the nickname of this CreateUserReqBody.

        用户昵称

        :return: The nickname of this CreateUserReqBody.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        r"""Sets the nickname of this CreateUserReqBody.

        用户昵称

        :param nickname: The nickname of this CreateUserReqBody.
        :type nickname: str
        """
        self._nickname = nickname

    @property
    def phone_numbers(self):
        r"""Gets the phone_numbers of this CreateUserReqBody.

        用户的电话号码信息列表

        :return: The phone_numbers of this CreateUserReqBody.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.PhoneNumberDto`]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        r"""Sets the phone_numbers of this CreateUserReqBody.

        用户的电话号码信息列表

        :param phone_numbers: The phone_numbers of this CreateUserReqBody.
        :type phone_numbers: list[:class:`huaweicloudsdkidentitycenterstore.v1.PhoneNumberDto`]
        """
        self._phone_numbers = phone_numbers

    @property
    def preferred_language(self):
        r"""Gets the preferred_language of this CreateUserReqBody.

        用户语言首选项

        :return: The preferred_language of this CreateUserReqBody.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        r"""Sets the preferred_language of this CreateUserReqBody.

        用户语言首选项

        :param preferred_language: The preferred_language of this CreateUserReqBody.
        :type preferred_language: str
        """
        self._preferred_language = preferred_language

    @property
    def profile_url(self):
        r"""Gets the profile_url of this CreateUserReqBody.

        与用户关联的URL

        :return: The profile_url of this CreateUserReqBody.
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        r"""Sets the profile_url of this CreateUserReqBody.

        与用户关联的URL

        :param profile_url: The profile_url of this CreateUserReqBody.
        :type profile_url: str
        """
        self._profile_url = profile_url

    @property
    def timezone(self):
        r"""Gets the timezone of this CreateUserReqBody.

        用户时区

        :return: The timezone of this CreateUserReqBody.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this CreateUserReqBody.

        用户时区

        :param timezone: The timezone of this CreateUserReqBody.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def title(self):
        r"""Gets the title of this CreateUserReqBody.

        用户头衔

        :return: The title of this CreateUserReqBody.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this CreateUserReqBody.

        用户头衔

        :param title: The title of this CreateUserReqBody.
        :type title: str
        """
        self._title = title

    @property
    def user_name(self):
        r"""Gets the user_name of this CreateUserReqBody.

        用户名，用于标识用户的唯一字符串

        :return: The user_name of this CreateUserReqBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this CreateUserReqBody.

        用户名，用于标识用户的唯一字符串

        :param user_name: The user_name of this CreateUserReqBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_type(self):
        r"""Gets the user_type of this CreateUserReqBody.

        用户类型

        :return: The user_type of this CreateUserReqBody.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this CreateUserReqBody.

        用户类型

        :param user_type: The user_type of this CreateUserReqBody.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def password_mode(self):
        r"""Gets the password_mode of this CreateUserReqBody.

        初始化密码方式，一次性密码/邮箱

        :return: The password_mode of this CreateUserReqBody.
        :rtype: str
        """
        return self._password_mode

    @password_mode.setter
    def password_mode(self, password_mode):
        r"""Sets the password_mode of this CreateUserReqBody.

        初始化密码方式，一次性密码/邮箱

        :param password_mode: The password_mode of this CreateUserReqBody.
        :type password_mode: str
        """
        self._password_mode = password_mode

    @property
    def enterprise(self):
        r"""Gets the enterprise of this CreateUserReqBody.

        :return: The enterprise of this CreateUserReqBody.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.EnterpriseDto`
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        r"""Sets the enterprise of this CreateUserReqBody.

        :param enterprise: The enterprise of this CreateUserReqBody.
        :type enterprise: :class:`huaweicloudsdkidentitycenterstore.v1.EnterpriseDto`
        """
        self._enterprise = enterprise

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
        if not isinstance(other, CreateUserReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
