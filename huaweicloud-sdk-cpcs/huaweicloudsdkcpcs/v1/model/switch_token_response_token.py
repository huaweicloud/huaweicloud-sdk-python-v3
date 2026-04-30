# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchTokenResponseToken:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app': 'SwitchTokenResponseTokenApp',
        'expires_at': 'str',
        'roles': 'list[SwitchTokenResponseTokenRoles]',
        'issued_at': 'str',
        'user': 'SwitchTokenResponseTokenUser'
    }

    attribute_map = {
        'app': 'app',
        'expires_at': 'expires_at',
        'roles': 'roles',
        'issued_at': 'issued_at',
        'user': 'user'
    }

    def __init__(self, app=None, expires_at=None, roles=None, issued_at=None, user=None):
        r"""SwitchTokenResponseToken

        The model defined in huaweicloud sdk

        :param app: 
        :type app: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenApp`
        :param expires_at: 过期时间
        :type expires_at: str
        :param roles: 角色列表
        :type roles: list[:class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenRoles`]
        :param issued_at: 签发时间
        :type issued_at: str
        :param user: 
        :type user: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenUser`
        """
        
        

        self._app = None
        self._expires_at = None
        self._roles = None
        self._issued_at = None
        self._user = None
        self.discriminator = None

        if app is not None:
            self.app = app
        if expires_at is not None:
            self.expires_at = expires_at
        if roles is not None:
            self.roles = roles
        if issued_at is not None:
            self.issued_at = issued_at
        if user is not None:
            self.user = user

    @property
    def app(self):
        r"""Gets the app of this SwitchTokenResponseToken.

        :return: The app of this SwitchTokenResponseToken.
        :rtype: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenApp`
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this SwitchTokenResponseToken.

        :param app: The app of this SwitchTokenResponseToken.
        :type app: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenApp`
        """
        self._app = app

    @property
    def expires_at(self):
        r"""Gets the expires_at of this SwitchTokenResponseToken.

        过期时间

        :return: The expires_at of this SwitchTokenResponseToken.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this SwitchTokenResponseToken.

        过期时间

        :param expires_at: The expires_at of this SwitchTokenResponseToken.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def roles(self):
        r"""Gets the roles of this SwitchTokenResponseToken.

        角色列表

        :return: The roles of this SwitchTokenResponseToken.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenRoles`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this SwitchTokenResponseToken.

        角色列表

        :param roles: The roles of this SwitchTokenResponseToken.
        :type roles: list[:class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenRoles`]
        """
        self._roles = roles

    @property
    def issued_at(self):
        r"""Gets the issued_at of this SwitchTokenResponseToken.

        签发时间

        :return: The issued_at of this SwitchTokenResponseToken.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        r"""Sets the issued_at of this SwitchTokenResponseToken.

        签发时间

        :param issued_at: The issued_at of this SwitchTokenResponseToken.
        :type issued_at: str
        """
        self._issued_at = issued_at

    @property
    def user(self):
        r"""Gets the user of this SwitchTokenResponseToken.

        :return: The user of this SwitchTokenResponseToken.
        :rtype: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this SwitchTokenResponseToken.

        :param user: The user of this SwitchTokenResponseToken.
        :type user: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseTokenUser`
        """
        self._user = user

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
        if not isinstance(other, SwitchTokenResponseToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
