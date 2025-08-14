# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeUserResponse(SdkResponse):

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
        'external_id': 'str',
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
        'email_verified': 'bool',
        'enabled': 'bool',
        'enterprise': 'EnterpriseDto'
    }

    attribute_map = {
        'addresses': 'addresses',
        'display_name': 'display_name',
        'emails': 'emails',
        'external_id': 'external_id',
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
        'email_verified': 'email_verified',
        'enabled': 'enabled',
        'enterprise': 'enterprise'
    }

    def __init__(self, addresses=None, display_name=None, emails=None, external_id=None, external_ids=None, identity_store_id=None, locale=None, name=None, nickname=None, phone_numbers=None, preferred_language=None, profile_url=None, timezone=None, title=None, user_id=None, user_name=None, user_type=None, created_at=None, created_by=None, updated_at=None, updated_by=None, email_verified=None, enabled=None, enterprise=None):
        r"""DescribeUserResponse

        The model defined in huaweicloud sdk

        :param addresses: 用户的地址信息列表
        :type addresses: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        :param display_name: 用户的显示名称
        :type display_name: str
        :param emails: 用户的电子邮箱信息列表
        :type emails: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        :param external_id: 外部身份源分配给此资源的标识符
        :type external_id: str
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
        :param email_verified: 一个布尔值，表示用户主的电子邮箱是否验证
        :type email_verified: bool
        :param enabled: 一个布尔值，表示用户是否启用
        :type enabled: bool
        :param enterprise: 
        :type enterprise: :class:`huaweicloudsdkidentitycenterstore.v1.EnterpriseDto`
        """
        
        super(DescribeUserResponse, self).__init__()

        self._addresses = None
        self._display_name = None
        self._emails = None
        self._external_id = None
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
        self._email_verified = None
        self._enabled = None
        self._enterprise = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if display_name is not None:
            self.display_name = display_name
        if emails is not None:
            self.emails = emails
        if external_id is not None:
            self.external_id = external_id
        if external_ids is not None:
            self.external_ids = external_ids
        if identity_store_id is not None:
            self.identity_store_id = identity_store_id
        if locale is not None:
            self.locale = locale
        if name is not None:
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
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if user_type is not None:
            self.user_type = user_type
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
        if email_verified is not None:
            self.email_verified = email_verified
        if enabled is not None:
            self.enabled = enabled
        if enterprise is not None:
            self.enterprise = enterprise

    @property
    def addresses(self):
        r"""Gets the addresses of this DescribeUserResponse.

        用户的地址信息列表

        :return: The addresses of this DescribeUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this DescribeUserResponse.

        用户的地址信息列表

        :param addresses: The addresses of this DescribeUserResponse.
        :type addresses: list[:class:`huaweicloudsdkidentitycenterstore.v1.AddressDto`]
        """
        self._addresses = addresses

    @property
    def display_name(self):
        r"""Gets the display_name of this DescribeUserResponse.

        用户的显示名称

        :return: The display_name of this DescribeUserResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this DescribeUserResponse.

        用户的显示名称

        :param display_name: The display_name of this DescribeUserResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def emails(self):
        r"""Gets the emails of this DescribeUserResponse.

        用户的电子邮箱信息列表

        :return: The emails of this DescribeUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        r"""Sets the emails of this DescribeUserResponse.

        用户的电子邮箱信息列表

        :param emails: The emails of this DescribeUserResponse.
        :type emails: list[:class:`huaweicloudsdkidentitycenterstore.v1.EmailDto`]
        """
        self._emails = emails

    @property
    def external_id(self):
        r"""Gets the external_id of this DescribeUserResponse.

        外部身份源分配给此资源的标识符

        :return: The external_id of this DescribeUserResponse.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        r"""Sets the external_id of this DescribeUserResponse.

        外部身份源分配给此资源的标识符

        :param external_id: The external_id of this DescribeUserResponse.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def external_ids(self):
        r"""Gets the external_ids of this DescribeUserResponse.

        用户的外部标识符信息列表

        :return: The external_ids of this DescribeUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`]
        """
        return self._external_ids

    @external_ids.setter
    def external_ids(self, external_ids):
        r"""Sets the external_ids of this DescribeUserResponse.

        用户的外部标识符信息列表

        :param external_ids: The external_ids of this DescribeUserResponse.
        :type external_ids: list[:class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`]
        """
        self._external_ids = external_ids

    @property
    def identity_store_id(self):
        r"""Gets the identity_store_id of this DescribeUserResponse.

        身份源的全局唯一标识符（ID）

        :return: The identity_store_id of this DescribeUserResponse.
        :rtype: str
        """
        return self._identity_store_id

    @identity_store_id.setter
    def identity_store_id(self, identity_store_id):
        r"""Sets the identity_store_id of this DescribeUserResponse.

        身份源的全局唯一标识符（ID）

        :param identity_store_id: The identity_store_id of this DescribeUserResponse.
        :type identity_store_id: str
        """
        self._identity_store_id = identity_store_id

    @property
    def locale(self):
        r"""Gets the locale of this DescribeUserResponse.

        用户的地理区域或位置信息

        :return: The locale of this DescribeUserResponse.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this DescribeUserResponse.

        用户的地理区域或位置信息

        :param locale: The locale of this DescribeUserResponse.
        :type locale: str
        """
        self._locale = locale

    @property
    def name(self):
        r"""Gets the name of this DescribeUserResponse.

        :return: The name of this DescribeUserResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.NameDto`
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this DescribeUserResponse.

        :param name: The name of this DescribeUserResponse.
        :type name: :class:`huaweicloudsdkidentitycenterstore.v1.NameDto`
        """
        self._name = name

    @property
    def nickname(self):
        r"""Gets the nickname of this DescribeUserResponse.

        用户昵称

        :return: The nickname of this DescribeUserResponse.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        r"""Sets the nickname of this DescribeUserResponse.

        用户昵称

        :param nickname: The nickname of this DescribeUserResponse.
        :type nickname: str
        """
        self._nickname = nickname

    @property
    def phone_numbers(self):
        r"""Gets the phone_numbers of this DescribeUserResponse.

        用户的电话号码信息列表

        :return: The phone_numbers of this DescribeUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterstore.v1.PhoneNumberDto`]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        r"""Sets the phone_numbers of this DescribeUserResponse.

        用户的电话号码信息列表

        :param phone_numbers: The phone_numbers of this DescribeUserResponse.
        :type phone_numbers: list[:class:`huaweicloudsdkidentitycenterstore.v1.PhoneNumberDto`]
        """
        self._phone_numbers = phone_numbers

    @property
    def preferred_language(self):
        r"""Gets the preferred_language of this DescribeUserResponse.

        用户语言首选项

        :return: The preferred_language of this DescribeUserResponse.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        r"""Sets the preferred_language of this DescribeUserResponse.

        用户语言首选项

        :param preferred_language: The preferred_language of this DescribeUserResponse.
        :type preferred_language: str
        """
        self._preferred_language = preferred_language

    @property
    def profile_url(self):
        r"""Gets the profile_url of this DescribeUserResponse.

        与用户关联的URL

        :return: The profile_url of this DescribeUserResponse.
        :rtype: str
        """
        return self._profile_url

    @profile_url.setter
    def profile_url(self, profile_url):
        r"""Sets the profile_url of this DescribeUserResponse.

        与用户关联的URL

        :param profile_url: The profile_url of this DescribeUserResponse.
        :type profile_url: str
        """
        self._profile_url = profile_url

    @property
    def timezone(self):
        r"""Gets the timezone of this DescribeUserResponse.

        用户时区

        :return: The timezone of this DescribeUserResponse.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this DescribeUserResponse.

        用户时区

        :param timezone: The timezone of this DescribeUserResponse.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def title(self):
        r"""Gets the title of this DescribeUserResponse.

        用户头衔

        :return: The title of this DescribeUserResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this DescribeUserResponse.

        用户头衔

        :param title: The title of this DescribeUserResponse.
        :type title: str
        """
        self._title = title

    @property
    def user_id(self):
        r"""Gets the user_id of this DescribeUserResponse.

        身份源中IdentityCenter用户的全局唯一标识符（ID）

        :return: The user_id of this DescribeUserResponse.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this DescribeUserResponse.

        身份源中IdentityCenter用户的全局唯一标识符（ID）

        :param user_id: The user_id of this DescribeUserResponse.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this DescribeUserResponse.

        用户名，用于标识用户的唯一字符串

        :return: The user_name of this DescribeUserResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DescribeUserResponse.

        用户名，用于标识用户的唯一字符串

        :param user_name: The user_name of this DescribeUserResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_type(self):
        r"""Gets the user_type of this DescribeUserResponse.

        用户类型

        :return: The user_type of this DescribeUserResponse.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this DescribeUserResponse.

        用户类型

        :param user_type: The user_type of this DescribeUserResponse.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def created_at(self):
        r"""Gets the created_at of this DescribeUserResponse.

        创建用户时的时间戳

        :return: The created_at of this DescribeUserResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this DescribeUserResponse.

        创建用户时的时间戳

        :param created_at: The created_at of this DescribeUserResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def created_by(self):
        r"""Gets the created_by of this DescribeUserResponse.

        创建者

        :return: The created_by of this DescribeUserResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this DescribeUserResponse.

        创建者

        :param created_by: The created_by of this DescribeUserResponse.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DescribeUserResponse.

        更新用户时的时间戳

        :return: The updated_at of this DescribeUserResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DescribeUserResponse.

        更新用户时的时间戳

        :param updated_at: The updated_at of this DescribeUserResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def updated_by(self):
        r"""Gets the updated_by of this DescribeUserResponse.

        更新者

        :return: The updated_by of this DescribeUserResponse.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this DescribeUserResponse.

        更新者

        :param updated_by: The updated_by of this DescribeUserResponse.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def email_verified(self):
        r"""Gets the email_verified of this DescribeUserResponse.

        一个布尔值，表示用户主的电子邮箱是否验证

        :return: The email_verified of this DescribeUserResponse.
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        r"""Sets the email_verified of this DescribeUserResponse.

        一个布尔值，表示用户主的电子邮箱是否验证

        :param email_verified: The email_verified of this DescribeUserResponse.
        :type email_verified: bool
        """
        self._email_verified = email_verified

    @property
    def enabled(self):
        r"""Gets the enabled of this DescribeUserResponse.

        一个布尔值，表示用户是否启用

        :return: The enabled of this DescribeUserResponse.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this DescribeUserResponse.

        一个布尔值，表示用户是否启用

        :param enabled: The enabled of this DescribeUserResponse.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def enterprise(self):
        r"""Gets the enterprise of this DescribeUserResponse.

        :return: The enterprise of this DescribeUserResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.EnterpriseDto`
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        r"""Sets the enterprise of this DescribeUserResponse.

        :param enterprise: The enterprise of this DescribeUserResponse.
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
        if not isinstance(other, DescribeUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
