# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchCpcsTokenResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'roles': 'list[str]',
        'ak': 'SwitchTokenResponseAk',
        'expired_at': 'str',
        'issued_at': 'str',
        'user': 'SwitchTokenResponseUser',
        'x_cpcs_token': 'str'
    }

    attribute_map = {
        'roles': 'roles',
        'ak': 'ak',
        'expired_at': 'expired_at',
        'issued_at': 'issued_at',
        'user': 'user',
        'x_cpcs_token': 'X-CPCS-Token'
    }

    def __init__(self, roles=None, ak=None, expired_at=None, issued_at=None, user=None, x_cpcs_token=None):
        r"""SwitchCpcsTokenResponse

        The model defined in huaweicloud sdk

        :param roles: 角色列表
        :type roles: list[str]
        :param ak: 
        :type ak: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseAk`
        :param expired_at: 过期时间
        :type expired_at: str
        :param issued_at: 签发时间
        :type issued_at: str
        :param user: 
        :type user: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseUser`
        :param x_cpcs_token: 
        :type x_cpcs_token: str
        """
        
        super().__init__()

        self._roles = None
        self._ak = None
        self._expired_at = None
        self._issued_at = None
        self._user = None
        self._x_cpcs_token = None
        self.discriminator = None

        if roles is not None:
            self.roles = roles
        if ak is not None:
            self.ak = ak
        if expired_at is not None:
            self.expired_at = expired_at
        if issued_at is not None:
            self.issued_at = issued_at
        if user is not None:
            self.user = user
        if x_cpcs_token is not None:
            self.x_cpcs_token = x_cpcs_token

    @property
    def roles(self):
        r"""Gets the roles of this SwitchCpcsTokenResponse.

        角色列表

        :return: The roles of this SwitchCpcsTokenResponse.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this SwitchCpcsTokenResponse.

        角色列表

        :param roles: The roles of this SwitchCpcsTokenResponse.
        :type roles: list[str]
        """
        self._roles = roles

    @property
    def ak(self):
        r"""Gets the ak of this SwitchCpcsTokenResponse.

        :return: The ak of this SwitchCpcsTokenResponse.
        :rtype: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseAk`
        """
        return self._ak

    @ak.setter
    def ak(self, ak):
        r"""Sets the ak of this SwitchCpcsTokenResponse.

        :param ak: The ak of this SwitchCpcsTokenResponse.
        :type ak: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseAk`
        """
        self._ak = ak

    @property
    def expired_at(self):
        r"""Gets the expired_at of this SwitchCpcsTokenResponse.

        过期时间

        :return: The expired_at of this SwitchCpcsTokenResponse.
        :rtype: str
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        r"""Sets the expired_at of this SwitchCpcsTokenResponse.

        过期时间

        :param expired_at: The expired_at of this SwitchCpcsTokenResponse.
        :type expired_at: str
        """
        self._expired_at = expired_at

    @property
    def issued_at(self):
        r"""Gets the issued_at of this SwitchCpcsTokenResponse.

        签发时间

        :return: The issued_at of this SwitchCpcsTokenResponse.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        r"""Sets the issued_at of this SwitchCpcsTokenResponse.

        签发时间

        :param issued_at: The issued_at of this SwitchCpcsTokenResponse.
        :type issued_at: str
        """
        self._issued_at = issued_at

    @property
    def user(self):
        r"""Gets the user of this SwitchCpcsTokenResponse.

        :return: The user of this SwitchCpcsTokenResponse.
        :rtype: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this SwitchCpcsTokenResponse.

        :param user: The user of this SwitchCpcsTokenResponse.
        :type user: :class:`huaweicloudsdkcpcs.v1.SwitchTokenResponseUser`
        """
        self._user = user

    @property
    def x_cpcs_token(self):
        r"""Gets the x_cpcs_token of this SwitchCpcsTokenResponse.

        :return: The x_cpcs_token of this SwitchCpcsTokenResponse.
        :rtype: str
        """
        return self._x_cpcs_token

    @x_cpcs_token.setter
    def x_cpcs_token(self, x_cpcs_token):
        r"""Sets the x_cpcs_token of this SwitchCpcsTokenResponse.

        :param x_cpcs_token: The x_cpcs_token of this SwitchCpcsTokenResponse.
        :type x_cpcs_token: str
        """
        self._x_cpcs_token = x_cpcs_token

    def to_dict(self):
        import warnings
        warnings.warn("SwitchCpcsTokenResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, SwitchCpcsTokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
