# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Authorization:

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
        'account_id': 'str',
        'account': 'str',
        'app_id': 'str',
        'app_name': 'str',
        'app_group_id': 'str',
        'app_group_name': 'str',
        'authorization_type': 'str',
        'account_type': 'str',
        'platform_type': 'str',
        'domain': 'str',
        'create_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'account': 'account',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'app_group_id': 'app_group_id',
        'app_group_name': 'app_group_name',
        'authorization_type': 'authorization_type',
        'account_type': 'account_type',
        'platform_type': 'platform_type',
        'domain': 'domain',
        'create_at': 'create_at'
    }

    def __init__(self, id=None, account_id=None, account=None, app_id=None, app_name=None, app_group_id=None, app_group_name=None, authorization_type=None, account_type=None, platform_type=None, domain=None, create_at=None):
        r"""Authorization

        The model defined in huaweicloud sdk

        :param id: 授权ID。
        :type id: str
        :param account_id: 用户ID(或用户组ID)。
        :type account_id: str
        :param account: 用户名(或用户组名)。
        :type account: str
        :param app_id: 应用ID (按照组授权时,该字段为空)。
        :type app_id: str
        :param app_name: 应用名称 (按照组授权时,该字段为空)。
        :type app_name: str
        :param app_group_id: 应用组ID。
        :type app_group_id: str
        :param app_group_name: 应用组名称。
        :type app_group_name: str
        :param authorization_type: 授权类型，基于应用(组)授权，默认为APP_GROUP授权。 * &#x60;APP&#x60; - 按照应用授权（***尚未支持***）。 * &#x60;APP_GROUP&#x60; - 按照应用组授权。
        :type authorization_type: str
        :param account_type: 用户类型： * &#x60;USER&#x60; - 用户 * &#x60;USER_GROUP&#x60; - 用户组
        :type account_type: str
        :param platform_type: 平台类型： * &#x60;AD&#x60; - AD域 * &#x60;LOCAL&#x60; - LiteAs * &#x60;SYSTEM&#x60; - 系统内置
        :type platform_type: str
        :param domain: 域名城。
        :type domain: str
        :param create_at: 发布时间。
        :type create_at: datetime
        """
        
        

        self._id = None
        self._account_id = None
        self._account = None
        self._app_id = None
        self._app_name = None
        self._app_group_id = None
        self._app_group_name = None
        self._authorization_type = None
        self._account_type = None
        self._platform_type = None
        self._domain = None
        self._create_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if account is not None:
            self.account = account
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if app_group_id is not None:
            self.app_group_id = app_group_id
        if app_group_name is not None:
            self.app_group_name = app_group_name
        if authorization_type is not None:
            self.authorization_type = authorization_type
        if account_type is not None:
            self.account_type = account_type
        if platform_type is not None:
            self.platform_type = platform_type
        if domain is not None:
            self.domain = domain
        if create_at is not None:
            self.create_at = create_at

    @property
    def id(self):
        r"""Gets the id of this Authorization.

        授权ID。

        :return: The id of this Authorization.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Authorization.

        授权ID。

        :param id: The id of this Authorization.
        :type id: str
        """
        self._id = id

    @property
    def account_id(self):
        r"""Gets the account_id of this Authorization.

        用户ID(或用户组ID)。

        :return: The account_id of this Authorization.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this Authorization.

        用户ID(或用户组ID)。

        :param account_id: The account_id of this Authorization.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account(self):
        r"""Gets the account of this Authorization.

        用户名(或用户组名)。

        :return: The account of this Authorization.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this Authorization.

        用户名(或用户组名)。

        :param account: The account of this Authorization.
        :type account: str
        """
        self._account = account

    @property
    def app_id(self):
        r"""Gets the app_id of this Authorization.

        应用ID (按照组授权时,该字段为空)。

        :return: The app_id of this Authorization.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this Authorization.

        应用ID (按照组授权时,该字段为空)。

        :param app_id: The app_id of this Authorization.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        r"""Gets the app_name of this Authorization.

        应用名称 (按照组授权时,该字段为空)。

        :return: The app_name of this Authorization.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this Authorization.

        应用名称 (按照组授权时,该字段为空)。

        :param app_name: The app_name of this Authorization.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_group_id(self):
        r"""Gets the app_group_id of this Authorization.

        应用组ID。

        :return: The app_group_id of this Authorization.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        r"""Sets the app_group_id of this Authorization.

        应用组ID。

        :param app_group_id: The app_group_id of this Authorization.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def app_group_name(self):
        r"""Gets the app_group_name of this Authorization.

        应用组名称。

        :return: The app_group_name of this Authorization.
        :rtype: str
        """
        return self._app_group_name

    @app_group_name.setter
    def app_group_name(self, app_group_name):
        r"""Sets the app_group_name of this Authorization.

        应用组名称。

        :param app_group_name: The app_group_name of this Authorization.
        :type app_group_name: str
        """
        self._app_group_name = app_group_name

    @property
    def authorization_type(self):
        r"""Gets the authorization_type of this Authorization.

        授权类型，基于应用(组)授权，默认为APP_GROUP授权。 * `APP` - 按照应用授权（***尚未支持***）。 * `APP_GROUP` - 按照应用组授权。

        :return: The authorization_type of this Authorization.
        :rtype: str
        """
        return self._authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        r"""Sets the authorization_type of this Authorization.

        授权类型，基于应用(组)授权，默认为APP_GROUP授权。 * `APP` - 按照应用授权（***尚未支持***）。 * `APP_GROUP` - 按照应用组授权。

        :param authorization_type: The authorization_type of this Authorization.
        :type authorization_type: str
        """
        self._authorization_type = authorization_type

    @property
    def account_type(self):
        r"""Gets the account_type of this Authorization.

        用户类型： * `USER` - 用户 * `USER_GROUP` - 用户组

        :return: The account_type of this Authorization.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        r"""Sets the account_type of this Authorization.

        用户类型： * `USER` - 用户 * `USER_GROUP` - 用户组

        :param account_type: The account_type of this Authorization.
        :type account_type: str
        """
        self._account_type = account_type

    @property
    def platform_type(self):
        r"""Gets the platform_type of this Authorization.

        平台类型： * `AD` - AD域 * `LOCAL` - LiteAs * `SYSTEM` - 系统内置

        :return: The platform_type of this Authorization.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        r"""Sets the platform_type of this Authorization.

        平台类型： * `AD` - AD域 * `LOCAL` - LiteAs * `SYSTEM` - 系统内置

        :param platform_type: The platform_type of this Authorization.
        :type platform_type: str
        """
        self._platform_type = platform_type

    @property
    def domain(self):
        r"""Gets the domain of this Authorization.

        域名城。

        :return: The domain of this Authorization.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this Authorization.

        域名城。

        :param domain: The domain of this Authorization.
        :type domain: str
        """
        self._domain = domain

    @property
    def create_at(self):
        r"""Gets the create_at of this Authorization.

        发布时间。

        :return: The create_at of this Authorization.
        :rtype: datetime
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this Authorization.

        发布时间。

        :param create_at: The create_at of this Authorization.
        :type create_at: datetime
        """
        self._create_at = create_at

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Authorization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
