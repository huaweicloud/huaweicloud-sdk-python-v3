# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'addresses': 'list[AddressDto]',
        'display_name': 'str',
        'emails': 'list[EmailDto]',
        'external_ids': 'list[ExternalIdDto]',
        'identity_store_id': 'str',
        'locale': 'str',
        'name': 'NameDto',
        'nickname': 'str',
        'phone_numbers': 'list[PhoneNumberDto]',
        'preferred_language': 'str',
        'profile_url': 'str',
        'timezone': 'str',
        'title': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'user_type': 'str',
        'created_at': 'int',
        'created_by': 'str',
        'updated_at': 'int',
        'updated_by': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'addresses': 'addresses',
        'display_name': 'display_name',
        'emails': 'emails',
        'external_ids': 'external_ids',
        'identity_store_id': 'identity_store_id',
        'locale': 'locale',
        'name': 'name',
        'nickname': 'nickname',
        'phone_numbers': 'phone_numbers',
        'preferred_language': 'preferred_language',
        'profile_url': 'profile_url',
        'timezone': 'timezone',
        'title': 'title',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'user_type': 'user_type',
        'created_at': 'created_at',
        'created_by': 'created_by',
        'updated_at': 'updated_at',
        'updated_by': 'updated_by',
        'enabled': 'enabled'
    }

    def __init__(self, addresses=None, display_name=None, emails=None, external_ids=None, identity_store_id=None, locale=None, name=None, nickname=None, phone_numbers=None, preferred_language=None, profile_url=None, timezone=None, title=None, user_id=None, user_name=None, user_type=None, created_at=None, created_by=None, updated_at=None, updated_by=None, enabled=None):
        """UserDto

        The model defined in huaweicloud sdk

        :param addresses: 用户的地址信息列表
        :type addresses: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        :param display_name: 用户的显示名称
        :type display_name: str
        :param emails: 用户的电子邮箱信息列表
        :type emails: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        :param external_ids: 用户的外部标识符信息列表
        :type external_ids: list[:class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`]
        :param identity_store_id: 身份源的全局唯一标识符（ID）
        :type identity_store_id: str
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
        :param user_id: 身份源中IdentityCenter用户的全局唯一标识符（ID）
        :type user_id: str
        :param user_name: 用户名，用于标识用户的唯一字符串
        :type user_name: str
        :param user_type: 用户类型
        :type user_type: str
        :param created_at: 创建用户时的时间戳
        :type created_at: int
        :param created_by: 创建者
        :type created_by: str
        :param updated_at: 更新用户时的时间戳
        :type updated_at: int
        :param updated_by: 更新者
        :type updated_by: str
        :param enabled: 一个布尔值，表示用户是否启用
        :type enabled: bool
        """
        
        

        self._addresses = None
        self._display_name = None
        self._emails = None
        self._external_ids = None
        self._identity_store_id = None
        self._locale = None
        self._name = None
        self._nickname = None
        self._phone_numbers = None
        self._preferred_language = None
        self._profile_url = None
        self._timezone = None
        self._title = None
        self._user_id = None
        self._user_name = None
        self._user_type = None
        self._created_at = None
        self._created_by = None
        self._updated_at = None
        self._updated_by = None
        self._enabled = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        self.display_name = display_name
        self.emails = emails
        if external_ids is not None:
            self.external_ids = external_ids
        self.identity_store_id = identity_store_id
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
        self.user_id = user_id
        self.user_name = user_name
        if user_type is not None:
            self.user_type = user_type
        self.created_at = created_at
        self.created_by = created_by
        self.updated_at = updated_at
        self.updated_by = updated_by
        self.enabled = enabled

    @property
    def addresses(self):
        """Gets the addresses of this UserDto.

        用户的地址信息列表

        :return: The addresses of this UserDto.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this UserDto.

        用户的地址信息列表

        :param addresses: The addresses of this UserDto.
        :type addresses: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        """
        self._addresses = addresses

    @property
    def display_name(self):
        """Gets the display_name of this UserDto.

        用户的显示名称

        :return: The display_name of this UserDto.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UserDto.

        用户的显示名称

        :param display_name: The display_name of this UserDto.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def emails(self):
        """Gets the emails of this UserDto.

        用户的电子邮箱信息列表

        :return: The emails of this UserDto.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this UserDto.

        用户的电子邮箱信息列表

        :param emails: The emails of this UserDto.
        :type emails: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        """
        self._emails = emails

    @property
    def external_ids(self):
        """Gets the external_ids of this UserDto.

        用户的外部标识符信息列表

        :return: The external_ids of this UserDto.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`]
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        """Sets the external_ids of this UserDto.

        用户的外部标识符信息列表

        :param external_ids: The external_ids of this UserDto.
        :type external_ids: list[:class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`]
        """
        self._external_ids = external_ids

    @property
    def identity_store_id(self):
        """Gets the identity_store_id of this UserDto.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this UserDto.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        """Sets the identity_store_id of this UserDto.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this UserDto.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def locale(self):
        """Gets the locale of this UserDto.

        用户的地理区域或位置信息

        :return: The locale of this UserDto.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this UserDto.

        用户的地理区域或位置信息

        :param locale: The locale of this UserDto.
        :type locale: str
        """
        self._locale = locale

    @property
    def name(self):
        """Gets the name of this UserDto.

        :return: The name of this UserDto.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.NameDto`
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserDto.

        :param name: The name of this UserDto.
        :type name: :class:`huaweicloudsdkidentitycenterstore.v1.NameDto`
        """
        self._name = name

    @property
    def nickname(self):
        """Gets the nickname of this UserDto.

        用户昵称

        :return: The nickname of this UserDto.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this UserDto.

        用户昵称

        :param nickname: The nickname of this UserDto.
        :type nickname: str
        """
        self._nickname = nickname

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this UserDto.

        用户的电话号码信息列表

        :return: The phone_numbers of this UserDto.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.PhoneNumberDto`]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this UserDto.

        用户的电话号码信息列表

        :param phone_numbers: The phone_numbers of this UserDto.
        :type phone_numbers: list[:class:`huaweicloudsdkidentitycenterstore.v1.PhoneNumberDto`]
        """
        self._phone_numbers = phone_numbers

    @property
    def preferred_language(self):
        """Gets the preferred_language of this UserDto.

        用户语言首选项

        :return: The preferred_language of this UserDto.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """Sets the preferred_language of this UserDto.

        用户语言首选项

        :param preferred_language: The preferred_language of this UserDto.
        :type preferred_language: str
        """
        self._preferred_language = preferred_language

    @property
    def profile_url(self):
        """Gets the profile_url of this UserDto.

        与用户关联的URL

        :return: The profile_url of this UserDto.
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        """Sets the profile_url of this UserDto.

        与用户关联的URL

        :param profile_url: The profile_url of this UserDto.
        :type profile_url: str
        """
        self._profile_url = profile_url

    @property
    def timezone(self):
        """Gets the timezone of this UserDto.

        用户时区

        :return: The timezone of this UserDto.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this UserDto.

        用户时区

        :param timezone: The timezone of this UserDto.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def title(self):
        """Gets the title of this UserDto.

        用户头衔

        :return: The title of this UserDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UserDto.

        用户头衔

        :param title: The title of this UserDto.
        :type title: str
        """
        self._title = title

    @property
    def user_id(self):
        """Gets the user_id of this UserDto.

        身份源中IdentityCenter用户的全局唯一标识符（ID）

        :return: The user_id of this UserDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserDto.

        身份源中IdentityCenter用户的全局唯一标识符（ID）

        :param user_id: The user_id of this UserDto.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        """Gets the user_name of this UserDto.

        用户名，用于标识用户的唯一字符串

        :return: The user_name of this UserDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this UserDto.

        用户名，用于标识用户的唯一字符串

        :param user_name: The user_name of this UserDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_type(self):
        """Gets the user_type of this UserDto.

        用户类型

        :return: The user_type of this UserDto.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this UserDto.

        用户类型

        :param user_type: The user_type of this UserDto.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def created_at(self):
        """Gets the created_at of this UserDto.

        创建用户时的时间戳

        :return: The created_at of this UserDto.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserDto.

        创建用户时的时间戳

        :param created_at: The created_at of this UserDto.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this UserDto.

        创建者

        :return: The created_by of this UserDto.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UserDto.

        创建者

        :param created_by: The created_by of this UserDto.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def updated_at(self):
        """Gets the updated_at of this UserDto.

        更新用户时的时间戳

        :return: The updated_at of this UserDto.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserDto.

        更新用户时的时间戳

        :param updated_at: The updated_at of this UserDto.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def updated_by(self):
        """Gets the updated_by of this UserDto.

        更新者

        :return: The updated_by of this UserDto.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this UserDto.

        更新者

        :param updated_by: The updated_by of this UserDto.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def enabled(self):
        """Gets the enabled of this UserDto.

        一个布尔值，表示用户是否启用

        :return: The enabled of this UserDto.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserDto.

        一个布尔值，表示用户是否启用

        :param enabled: The enabled of this UserDto.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, UserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
