# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutUserResponse(SdkResponse):

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
        'external_id': 'str',
        'meta': 'MetaDto',
        'schemas': 'list[str]',
        'user_name': 'str',
        'name': 'NameDto',
        'display_name': 'str',
        'nick_name': 'str',
        'title': 'str',
        'user_type': 'str',
        'preferred_language': 'str',
        'locale': 'str',
        'timezone': 'str',
        'active': 'bool',
        'emails': 'list[EmailItemDto]',
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
        'nick_name': 'nickName',
        'title': 'title',
        'user_type': 'userType',
        'preferred_language': 'preferredLanguage',
        'locale': 'locale',
        'timezone': 'timezone',
        'active': 'active',
        'emails': 'emails',
        'addresses': 'addresses',
        'phone_numbers': 'phoneNumbers',
        'urnietfparamsscimschemasextensionenterprise2_0_user': 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User'
    }

    def __init__(self, id=None, external_id=None, meta=None, schemas=None, user_name=None, name=None, display_name=None, nick_name=None, title=None, user_type=None, preferred_language=None, locale=None, timezone=None, active=None, emails=None, addresses=None, phone_numbers=None, urnietfparamsscimschemasextensionenterprise2_0_user=None):
        r"""PutUserResponse

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
        :param nick_name: 包含用户昵称的字符串
        :type nick_name: str
        :param title: 包含用户头衔的字符串
        :type title: str
        :param user_type: 指示用户类型的字符串
        :type user_type: str
        :param preferred_language: 包含用户首选语言的字符串
        :type preferred_language: str
        :param locale: 包含用户地理区域或位置的字符串
        :type locale: str
        :param timezone: 包含用户时区的字符串
        :type timezone: str
        :param active: 表示用户是否启用
        :type active: bool
        :param emails: 包含用户的电子邮箱信息的对象列表
        :type emails: list[:class:`huaweicloudsdkidentitycenterscim.v1.EmailItemDto`]
        :param addresses: 包含用户地址信息的对象列表
        :type addresses: list[:class:`huaweicloudsdkidentitycenterscim.v1.AddressItemDto`]
        :param phone_numbers: 包含用户电话号码信息的对象列表
        :type phone_numbers: list[:class:`huaweicloudsdkidentitycenterscim.v1.PhoneNumberItemDto`]
        :param urnietfparamsscimschemasextensionenterprise2_0_user: 
        :type urnietfparamsscimschemasextensionenterprise2_0_user: :class:`huaweicloudsdkidentitycenterscim.v1.EnterpriseDto`
        """
        
        super(PutUserResponse, self).__init__()

        self._id = None
        self._external_id = None
        self._meta = None
        self._schemas = None
        self._user_name = None
        self._name = None
        self._display_name = None
        self._nick_name = None
        self._title = None
        self._user_type = None
        self._preferred_language = None
        self._locale = None
        self._timezone = None
        self._active = None
        self._emails = None
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
        if nick_name is not None:
            self.nick_name = nick_name
        if title is not None:
            self.title = title
        if user_type is not None:
            self.user_type = user_type
        if preferred_language is not None:
            self.preferred_language = preferred_language
        if locale is not None:
            self.locale = locale
        if timezone is not None:
            self.timezone = timezone
        if active is not None:
            self.active = active
        if emails is not None:
            self.emails = emails
        if addresses is not None:
            self.addresses = addresses
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if urnietfparamsscimschemasextensionenterprise2_0_user is not None:
            self.urnietfparamsscimschemasextensionenterprise2_0_user = urnietfparamsscimschemasextensionenterprise2_0_user

    @property
    def id(self):
        r"""Gets the id of this PutUserResponse.

        用户的全局唯一标识符（ID）

        :return: The id of this PutUserResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PutUserResponse.

        用户的全局唯一标识符（ID）

        :param id: The id of this PutUserResponse.
        :type id: str
        """
        self._id = id

    @property
    def external_id(self):
        r"""Gets the external_id of this PutUserResponse.

        外部标识符

        :return: The external_id of this PutUserResponse.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        r"""Sets the external_id of this PutUserResponse.

        外部标识符

        :param external_id: The external_id of this PutUserResponse.
        :type external_id: str
        """
        self._external_id = external_id

    @property
    def meta(self):
        r"""Gets the meta of this PutUserResponse.

        :return: The meta of this PutUserResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.MetaDto`
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        r"""Sets the meta of this PutUserResponse.

        :param meta: The meta of this PutUserResponse.
        :type meta: :class:`huaweicloudsdkidentitycenterscim.v1.MetaDto`
        """
        self._meta = meta

    @property
    def schemas(self):
        r"""Gets the schemas of this PutUserResponse.

        概要

        :return: The schemas of this PutUserResponse.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this PutUserResponse.

        概要

        :param schemas: The schemas of this PutUserResponse.
        :type schemas: list[str]
        """
        self._schemas = schemas

    @property
    def user_name(self):
        r"""Gets the user_name of this PutUserResponse.

        用户名，用于标识用户的唯一字符串

        :return: The user_name of this PutUserResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this PutUserResponse.

        用户名，用于标识用户的唯一字符串

        :param user_name: The user_name of this PutUserResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def name(self):
        r"""Gets the name of this PutUserResponse.

        :return: The name of this PutUserResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.NameDto`
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PutUserResponse.

        :param name: The name of this PutUserResponse.
        :type name: :class:`huaweicloudsdkidentitycenterscim.v1.NameDto`
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this PutUserResponse.

        包含用户显示名称的字符串

        :return: The display_name of this PutUserResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this PutUserResponse.

        包含用户显示名称的字符串

        :param display_name: The display_name of this PutUserResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def nick_name(self):
        r"""Gets the nick_name of this PutUserResponse.

        包含用户昵称的字符串

        :return: The nick_name of this PutUserResponse.
        :rtype: str
        """
        return self._nick_name

    @nick_name.setter
    def nick_name(self, nick_name):
        r"""Sets the nick_name of this PutUserResponse.

        包含用户昵称的字符串

        :param nick_name: The nick_name of this PutUserResponse.
        :type nick_name: str
        """
        self._nick_name = nick_name

    @property
    def title(self):
        r"""Gets the title of this PutUserResponse.

        包含用户头衔的字符串

        :return: The title of this PutUserResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this PutUserResponse.

        包含用户头衔的字符串

        :param title: The title of this PutUserResponse.
        :type title: str
        """
        self._title = title

    @property
    def user_type(self):
        r"""Gets the user_type of this PutUserResponse.

        指示用户类型的字符串

        :return: The user_type of this PutUserResponse.
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        r"""Sets the user_type of this PutUserResponse.

        指示用户类型的字符串

        :param user_type: The user_type of this PutUserResponse.
        :type user_type: str
        """
        self._user_type = user_type

    @property
    def preferred_language(self):
        r"""Gets the preferred_language of this PutUserResponse.

        包含用户首选语言的字符串

        :return: The preferred_language of this PutUserResponse.
        :rtype: str
        """
        return self._preferred_language

    @preferred_language.setter
    def preferred_language(self, preferred_language):
        r"""Sets the preferred_language of this PutUserResponse.

        包含用户首选语言的字符串

        :param preferred_language: The preferred_language of this PutUserResponse.
        :type preferred_language: str
        """
        self._preferred_language = preferred_language

    @property
    def locale(self):
        r"""Gets the locale of this PutUserResponse.

        包含用户地理区域或位置的字符串

        :return: The locale of this PutUserResponse.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this PutUserResponse.

        包含用户地理区域或位置的字符串

        :param locale: The locale of this PutUserResponse.
        :type locale: str
        """
        self._locale = locale

    @property
    def timezone(self):
        r"""Gets the timezone of this PutUserResponse.

        包含用户时区的字符串

        :return: The timezone of this PutUserResponse.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        r"""Sets the timezone of this PutUserResponse.

        包含用户时区的字符串

        :param timezone: The timezone of this PutUserResponse.
        :type timezone: str
        """
        self._timezone = timezone

    @property
    def active(self):
        r"""Gets the active of this PutUserResponse.

        表示用户是否启用

        :return: The active of this PutUserResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        r"""Sets the active of this PutUserResponse.

        表示用户是否启用

        :param active: The active of this PutUserResponse.
        :type active: bool
        """
        self._active = active

    @property
    def emails(self):
        r"""Gets the emails of this PutUserResponse.

        包含用户的电子邮箱信息的对象列表

        :return: The emails of this PutUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.EmailItemDto`]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        r"""Sets the emails of this PutUserResponse.

        包含用户的电子邮箱信息的对象列表

        :param emails: The emails of this PutUserResponse.
        :type emails: list[:class:`huaweicloudsdkidentitycenterscim.v1.EmailItemDto`]
        """
        self._emails = emails

    @property
    def addresses(self):
        r"""Gets the addresses of this PutUserResponse.

        包含用户地址信息的对象列表

        :return: The addresses of this PutUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.AddressItemDto`]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        r"""Sets the addresses of this PutUserResponse.

        包含用户地址信息的对象列表

        :param addresses: The addresses of this PutUserResponse.
        :type addresses: list[:class:`huaweicloudsdkidentitycenterscim.v1.AddressItemDto`]
        """
        self._addresses = addresses

    @property
    def phone_numbers(self):
        r"""Gets the phone_numbers of this PutUserResponse.

        包含用户电话号码信息的对象列表

        :return: The phone_numbers of this PutUserResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.PhoneNumberItemDto`]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        r"""Sets the phone_numbers of this PutUserResponse.

        包含用户电话号码信息的对象列表

        :param phone_numbers: The phone_numbers of this PutUserResponse.
        :type phone_numbers: list[:class:`huaweicloudsdkidentitycenterscim.v1.PhoneNumberItemDto`]
        """
        self._phone_numbers = phone_numbers

    @property
    def urnietfparamsscimschemasextensionenterprise2_0_user(self):
        r"""Gets the urnietfparamsscimschemasextensionenterprise2_0_user of this PutUserResponse.

        :return: The urnietfparamsscimschemasextensionenterprise2_0_user of this PutUserResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.EnterpriseDto`
        """
        return self._urnietfparamsscimschemasextensionenterprise2_0_user

    @urnietfparamsscimschemasextensionenterprise2_0_user.setter
    def urnietfparamsscimschemasextensionenterprise2_0_user(self, urnietfparamsscimschemasextensionenterprise2_0_user):
        r"""Sets the urnietfparamsscimschemasextensionenterprise2_0_user of this PutUserResponse.

        :param urnietfparamsscimschemasextensionenterprise2_0_user: The urnietfparamsscimschemasextensionenterprise2_0_user of this PutUserResponse.
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
        if not isinstance(other, PutUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
