# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('nick_name')
    sensitive_list.append('title')
    sensitive_list.append('preferred_language')
    sensitive_list.append('locale')
    sensitive_list.append('timezone')

    openapi_types = {
        'id': 'str',
        'external_id': 'str',
        'meta': 'MetaDto',
        'schemas': 'list[str]',
        'user_name': 'str',
        'name': 'NameDto',
        'display_name': 'str',
        'active': 'bool',
        'emails': 'list[EmailItemDto]',
        'user_type': 'str',
        'nick_name': 'str',
        'title': 'str',
        'preferred_language': 'str',
        'locale': 'str',
        'timezone': 'str',
        'addresses': 'list[AddressItemDto]',
        'phone_numbers': 'list[PhoneNumberItemDto]',
        'urnietfparamsscimschemasextensionenterprise2_0_user': 'EnterpriseDto'
    }

    attribute_map = {
        'id': 'id',
        'external_id': 'externalId',
        'meta': 'meta',
        'schemas': 'schemas',
        'user_name': 'userName',
        'name': 'name',
        'display_name': 'displayName',
        'active': 'active',
        'emails': 'emails',
        'user_type': 'userType',
        'nick_name': 'nickName',
        'title': 'title',
        'preferred_language': 'preferredLanguage',
        'locale': 'locale',
        'timezone': 'timezone',
        'addresses': 'addresses',
        'phone_numbers': 'phoneNumbers',
        'urnietfparamsscimschemasextensionenterprise2_0_user': 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User'
    }

    def __init__(self, id=None, external_id=None, meta=None, schemas=None, user_name=None, name=None, display_name=None, active=None, emails=None, user_type=None, nick_name=None, title=None, preferred_language=None, locale=None, timezone=None, addresses=None, phone_numbers=None, urnietfparamsscimschemasextensionenterprise2_0_user=None):
        """GetUserResponse

        The model defined in huaweicloud sdk

        :param id: 用户的全局唯一标识符（ID）
        :type id: str
        :param external_id: 外部标识符
        :type external_id: str
        :param meta: 
        :type meta: :class:`huaweicloudsdkidentitycenterscim.v1.MetaDto`
        :param schemas: 概要
        :type schemas: list[str]
        :param user_name: 用户名，用于标识用户的唯一字符串
        :type user_name: str
        :param name: 
        :type name: :class:`huaweicloudsdkidentitycenterscim.v1.NameDto`
        :param display_name: 包含用户显示名称的字符串
        :type display_name: str
        :param active: 表示用户是否启用
        :type active: bool
        :param emails: 包含用户的电子邮箱信息的对象列表
        :type emails: list[:class:`huaweicloudsdkidentitycenterscim.v1.EmailItemDto`]
        :param user_type: 指示用户类型的字符串
        :type user_type: str
        :param nick_name: 用户昵称
        :type nick_name: str
        :param title: 用户头衔
        :type title: str
        :param preferred_language: 用户语言首选项
        :type preferred_language: str
        :param locale: 用户的地理区域或位置信息
        :type locale: str
        :param timezone: 用户时区
        :type timezone: str
        :param addresses: 用户的地址信息列表
        :type addresses: list[:class:`huaweicloudsdkidentitycenterscim.v1.AddressItemDto`]
        :param phone_numbers: 用户的电话号码信息列表
        :type phone_numbers: list[:class:`huaweicloudsdkidentitycenterscim.v1.PhoneNumberItemDto`]
        :param urnietfparamsscimschemasextensionenterprise2_0_user: 
        :type urnietfparamsscimschemasextensionenterprise2_0_user: :class:`huaweicloudsdkidentitycenterscim.v1.EnterpriseDto`
        """
        
        super(GetUserResponse, self).__init__()

        self._id = None
        self._external_id = None
        self._meta = None
        self._schemas = None
        self._user_name = None
        self._name = None
        self._display_name = None
        self._active = None
        self._emails = None
        self._user_type = None
        self._nick_name = None
        self._title = None
        self._preferred_language = None
        self._locale = None
        self._timezone = None
        self._addresses = None
        self._phone_numbers = None
        self._urnietfparamsscimschemasextensionenterprise2_0_user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if external_id is not None:
            self.external_id = external_id
        if meta is not None:
            self.meta = meta
        if schemas is not None:
            self.schemas = schemas
        if user_name is not None:
            self.user_name = user_name
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if active is not None:
            self.active = active
        if emails is not None:
            self.emails = emails
        if user_type is not None:
            self.user_type = user_type
        if nick_name is not None:
            self.nick_name = nick_name
        if title is not None:
            self.title = title
        if preferred_language is not None:
            self.preferred_language = preferred_language
        if locale is not None:
            self.locale = locale
        if timezone is not None:
            self.timezone = timezone
        if addresses is not None:
            self.addresses = addresses
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if urnietfparamsscimschemasextensionenterprise2_0_user is not None:
            self.urnietfparamsscimschemasextensionenterprise2_0_user = urnietfparamsscimschemasextensionenterprise2_0_user

    @property
    def id(self):
        """Gets the id of this GetUserResponse.

        用户的全局唯一标识符（ID）

        :return: The id of this GetUserResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetUserResponse.

        用户的全局唯一标识符（ID）

        :param id: The id of this GetUserResponse.
        :type id: str
        """
        self._id = id

    @property
    def external_id(self):
        """Gets the external_id of this GetUserResponse.

        外部标识符

        :return: The external_id of this GetUserResponse.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this GetUserResponse.

        外部标识符

        :param external_id: The external_id of this GetUserResponse.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def meta(self):
        """Gets the meta of this GetUserResponse.

        :return: The meta of this GetUserResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.MetaDto`
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this GetUserResponse.

        :param meta: The meta of this GetUserResponse.
        :type meta: :class:`huaweicloudsdkidentitycenterscim.v1.MetaDto`
        """
        self._meta = meta

    @property
    def schemas(self):
        """Gets the schemas of this GetUserResponse.

        概要

        :return: The schemas of this GetUserResponse.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this GetUserResponse.

        概要

        :param schemas: The schemas of this GetUserResponse.
        :type schemas: list[str]
        """
        self._schemas = schemas

    @property
    def user_name(self):
        """Gets the user_name of this GetUserResponse.

        用户名，用于标识用户的唯一字符串

        :return: The user_name of this GetUserResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this GetUserResponse.

        用户名，用于标识用户的唯一字符串

        :param user_name: The user_name of this GetUserResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def name(self):
        """Gets the name of this GetUserResponse.

        :return: The name of this GetUserResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.NameDto`
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUserResponse.

        :param name: The name of this GetUserResponse.
        :type name: :class:`huaweicloudsdkidentitycenterscim.v1.NameDto`
        """
        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this GetUserResponse.

        包含用户显示名称的字符串

        :return: The display_name of this GetUserResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetUserResponse.

        包含用户显示名称的字符串

        :param display_name: The display_name of this GetUserResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def active(self):
        """Gets the active of this GetUserResponse.

        表示用户是否启用

        :return: The active of this GetUserResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this GetUserResponse.

        表示用户是否启用

        :param active: The active of this GetUserResponse.
        :type active: bool
        """
        self._active = active

    @property
    def emails(self):
        """Gets the emails of this GetUserResponse.

        包含用户的电子邮箱信息的对象列表

        :return: The emails of this GetUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.EmailItemDto`]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this GetUserResponse.

        包含用户的电子邮箱信息的对象列表

        :param emails: The emails of this GetUserResponse.
        :type emails: list[:class:`huaweicloudsdkidentitycenterscim.v1.EmailItemDto`]
        """
        self._emails = emails

    @property
    def user_type(self):
        """Gets the user_type of this GetUserResponse.

        指示用户类型的字符串

        :return: The user_type of this GetUserResponse.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this GetUserResponse.

        指示用户类型的字符串

        :param user_type: The user_type of this GetUserResponse.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def nick_name(self):
        """Gets the nick_name of this GetUserResponse.

        用户昵称

        :return: The nick_name of this GetUserResponse.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        """Sets the nick_name of this GetUserResponse.

        用户昵称

        :param nick_name: The nick_name of this GetUserResponse.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def title(self):
        """Gets the title of this GetUserResponse.

        用户头衔

        :return: The title of this GetUserResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GetUserResponse.

        用户头衔

        :param title: The title of this GetUserResponse.
        :type title: str
        """
        self._title = title

    @property
    def preferred_language(self):
        """Gets the preferred_language of this GetUserResponse.

        用户语言首选项

        :return: The preferred_language of this GetUserResponse.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        """Sets the preferred_language of this GetUserResponse.

        用户语言首选项

        :param preferred_language: The preferred_language of this GetUserResponse.
        :type preferred_language: str
        """
        self._preferred_language = preferred_language

    @property
    def locale(self):
        """Gets the locale of this GetUserResponse.

        用户的地理区域或位置信息

        :return: The locale of this GetUserResponse.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this GetUserResponse.

        用户的地理区域或位置信息

        :param locale: The locale of this GetUserResponse.
        :type locale: str
        """
        self._locale = locale

    @property
    def timezone(self):
        """Gets the timezone of this GetUserResponse.

        用户时区

        :return: The timezone of this GetUserResponse.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this GetUserResponse.

        用户时区

        :param timezone: The timezone of this GetUserResponse.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def addresses(self):
        """Gets the addresses of this GetUserResponse.

        用户的地址信息列表

        :return: The addresses of this GetUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.AddressItemDto`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this GetUserResponse.

        用户的地址信息列表

        :param addresses: The addresses of this GetUserResponse.
        :type addresses: list[:class:`huaweicloudsdkidentitycenterscim.v1.AddressItemDto`]
        """
        self._addresses = addresses

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this GetUserResponse.

        用户的电话号码信息列表

        :return: The phone_numbers of this GetUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.PhoneNumberItemDto`]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this GetUserResponse.

        用户的电话号码信息列表

        :param phone_numbers: The phone_numbers of this GetUserResponse.
        :type phone_numbers: list[:class:`huaweicloudsdkidentitycenterscim.v1.PhoneNumberItemDto`]
        """
        self._phone_numbers = phone_numbers

    @property
    def urnietfparamsscimschemasextensionenterprise2_0_user(self):
        """Gets the urnietfparamsscimschemasextensionenterprise2_0_user of this GetUserResponse.

        :return: The urnietfparamsscimschemasextensionenterprise2_0_user of this GetUserResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.EnterpriseDto`
        """
        return self._urnietfparamsscimschemasextensionenterprise2_0_user

    @urnietfparamsscimschemasextensionenterprise2_0_user.setter
    def urnietfparamsscimschemasextensionenterprise2_0_user(self, urnietfparamsscimschemasextensionenterprise2_0_user):
        """Sets the urnietfparamsscimschemasextensionenterprise2_0_user of this GetUserResponse.

        :param urnietfparamsscimschemasextensionenterprise2_0_user: The urnietfparamsscimschemasextensionenterprise2_0_user of this GetUserResponse.
        :type urnietfparamsscimschemasextensionenterprise2_0_user: :class:`huaweicloudsdkidentitycenterscim.v1.EnterpriseDto`
        """
        self._urnietfparamsscimschemasextensionenterprise2_0_user = urnietfparamsscimschemasextensionenterprise2_0_user

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
        if not isinstance(other, GetUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
