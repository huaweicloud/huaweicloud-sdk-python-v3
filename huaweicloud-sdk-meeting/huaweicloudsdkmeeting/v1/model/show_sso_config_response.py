# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSsoConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_sso': 'bool',
        'domain': 'str',
        'authorize_url': 'str',
        'get_token_url': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'scope': 'str',
        'acc_field_name': 'str',
        'get_user_info_url': 'str',
        'oauth2_server_type': 'int',
        'pc_schema_url': 'str',
        'android_schema_url': 'str',
        'ios_schema_url': 'str',
        'third_name': 'str',
        'third_email': 'str',
        'third_mobile': 'str',
        'third_access_token': 'str',
        'third_head_img_url': 'str'
    }

    attribute_map = {
        'enable_sso': 'enableSSO',
        'domain': 'domain',
        'authorize_url': 'authorizeUrl',
        'get_token_url': 'getTokenUrl',
        'client_id': 'clientId',
        'client_secret': 'clientSecret',
        'scope': 'scope',
        'acc_field_name': 'accFieldName',
        'get_user_info_url': 'getUserInfoUrl',
        'oauth2_server_type': 'oauth2ServerType',
        'pc_schema_url': 'pcSchemaUrl',
        'android_schema_url': 'androidSchemaUrl',
        'ios_schema_url': 'iosSchemaUrl',
        'third_name': 'thirdName',
        'third_email': 'thirdEmail',
        'third_mobile': 'thirdMobile',
        'third_access_token': 'thirdAccessToken',
        'third_head_img_url': 'thirdHeadImgUrl'
    }

    def __init__(self, enable_sso=None, domain=None, authorize_url=None, get_token_url=None, client_id=None, client_secret=None, scope=None, acc_field_name=None, get_user_info_url=None, oauth2_server_type=None, pc_schema_url=None, android_schema_url=None, ios_schema_url=None, third_name=None, third_email=None, third_mobile=None, third_access_token=None, third_head_img_url=None):
        r"""ShowSsoConfigResponse

        The model defined in huaweicloud sdk

        :param enable_sso: 是否开启SSO登录。
        :type enable_sso: bool
        :param domain: 企业域名。
        :type domain: str
        :param authorize_url: 鉴权中心URL。
        :type authorize_url: str
        :param get_token_url: 获取Token URL。
        :type get_token_url: str
        :param client_id: APP ID。
        :type client_id: str
        :param client_secret: APP秘钥。
        :type client_secret: str
        :param scope: 授权范围。 * openid：OAuth2.0的OIDC 
        :type scope: str
        :param acc_field_name: 第三方帐号的字段名称。
        :type acc_field_name: str
        :param get_user_info_url: 用户信息查询URL。
        :type get_user_info_url: str
        :param oauth2_server_type: 鉴权类型。OAuth2.0鉴权时取0。 * 0：OAuth2.0鉴权 
        :type oauth2_server_type: int
        :param pc_schema_url: 拉起PC端终端的schema。
        :type pc_schema_url: str
        :param android_schema_url: 拉起安卓端终端的schema。
        :type android_schema_url: str
        :param ios_schema_url: 拉起ios端终端的schema。
        :type ios_schema_url: str
        :param third_name: 第三方名称的字段名称。
        :type third_name: str
        :param third_email: 第三方邮箱的字段名称。
        :type third_email: str
        :param third_mobile: 第三方手机号的字段名称。
        :type third_mobile: str
        :param third_access_token: 第三方accessToken的字段名称。
        :type third_access_token: str
        :param third_head_img_url: 第三方头像链接的字段名称。
        :type third_head_img_url: str
        """
        
        super(ShowSsoConfigResponse, self).__init__()

        self._enable_sso = None
        self._domain = None
        self._authorize_url = None
        self._get_token_url = None
        self._client_id = None
        self._client_secret = None
        self._scope = None
        self._acc_field_name = None
        self._get_user_info_url = None
        self._oauth2_server_type = None
        self._pc_schema_url = None
        self._android_schema_url = None
        self._ios_schema_url = None
        self._third_name = None
        self._third_email = None
        self._third_mobile = None
        self._third_access_token = None
        self._third_head_img_url = None
        self.discriminator = None

        if enable_sso is not None:
            self.enable_sso = enable_sso
        if domain is not None:
            self.domain = domain
        if authorize_url is not None:
            self.authorize_url = authorize_url
        if get_token_url is not None:
            self.get_token_url = get_token_url
        if client_id is not None:
            self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if scope is not None:
            self.scope = scope
        if acc_field_name is not None:
            self.acc_field_name = acc_field_name
        if get_user_info_url is not None:
            self.get_user_info_url = get_user_info_url
        if oauth2_server_type is not None:
            self.oauth2_server_type = oauth2_server_type
        if pc_schema_url is not None:
            self.pc_schema_url = pc_schema_url
        if android_schema_url is not None:
            self.android_schema_url = android_schema_url
        if ios_schema_url is not None:
            self.ios_schema_url = ios_schema_url
        if third_name is not None:
            self.third_name = third_name
        if third_email is not None:
            self.third_email = third_email
        if third_mobile is not None:
            self.third_mobile = third_mobile
        if third_access_token is not None:
            self.third_access_token = third_access_token
        if third_head_img_url is not None:
            self.third_head_img_url = third_head_img_url

    @property
    def enable_sso(self):
        r"""Gets the enable_sso of this ShowSsoConfigResponse.

        是否开启SSO登录。

        :return: The enable_sso of this ShowSsoConfigResponse.
        :rtype: bool
        """
        return self._enable_sso

    @enable_sso.setter
    def enable_sso(self, enable_sso):
        r"""Sets the enable_sso of this ShowSsoConfigResponse.

        是否开启SSO登录。

        :param enable_sso: The enable_sso of this ShowSsoConfigResponse.
        :type enable_sso: bool
        """
        self._enable_sso = enable_sso

    @property
    def domain(self):
        r"""Gets the domain of this ShowSsoConfigResponse.

        企业域名。

        :return: The domain of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ShowSsoConfigResponse.

        企业域名。

        :param domain: The domain of this ShowSsoConfigResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def authorize_url(self):
        r"""Gets the authorize_url of this ShowSsoConfigResponse.

        鉴权中心URL。

        :return: The authorize_url of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._authorize_url

    @authorize_url.setter
    def authorize_url(self, authorize_url):
        r"""Sets the authorize_url of this ShowSsoConfigResponse.

        鉴权中心URL。

        :param authorize_url: The authorize_url of this ShowSsoConfigResponse.
        :type authorize_url: str
        """
        self._authorize_url = authorize_url

    @property
    def get_token_url(self):
        r"""Gets the get_token_url of this ShowSsoConfigResponse.

        获取Token URL。

        :return: The get_token_url of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._get_token_url

    @get_token_url.setter
    def get_token_url(self, get_token_url):
        r"""Sets the get_token_url of this ShowSsoConfigResponse.

        获取Token URL。

        :param get_token_url: The get_token_url of this ShowSsoConfigResponse.
        :type get_token_url: str
        """
        self._get_token_url = get_token_url

    @property
    def client_id(self):
        r"""Gets the client_id of this ShowSsoConfigResponse.

        APP ID。

        :return: The client_id of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ShowSsoConfigResponse.

        APP ID。

        :param client_id: The client_id of this ShowSsoConfigResponse.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        r"""Gets the client_secret of this ShowSsoConfigResponse.

        APP秘钥。

        :return: The client_secret of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        r"""Sets the client_secret of this ShowSsoConfigResponse.

        APP秘钥。

        :param client_secret: The client_secret of this ShowSsoConfigResponse.
        :type client_secret: str
        """
        self._client_secret = client_secret

    @property
    def scope(self):
        r"""Gets the scope of this ShowSsoConfigResponse.

        授权范围。 * openid：OAuth2.0的OIDC 

        :return: The scope of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        r"""Sets the scope of this ShowSsoConfigResponse.

        授权范围。 * openid：OAuth2.0的OIDC 

        :param scope: The scope of this ShowSsoConfigResponse.
        :type scope: str
        """
        self._scope = scope

    @property
    def acc_field_name(self):
        r"""Gets the acc_field_name of this ShowSsoConfigResponse.

        第三方帐号的字段名称。

        :return: The acc_field_name of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._acc_field_name

    @acc_field_name.setter
    def acc_field_name(self, acc_field_name):
        r"""Sets the acc_field_name of this ShowSsoConfigResponse.

        第三方帐号的字段名称。

        :param acc_field_name: The acc_field_name of this ShowSsoConfigResponse.
        :type acc_field_name: str
        """
        self._acc_field_name = acc_field_name

    @property
    def get_user_info_url(self):
        r"""Gets the get_user_info_url of this ShowSsoConfigResponse.

        用户信息查询URL。

        :return: The get_user_info_url of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._get_user_info_url

    @get_user_info_url.setter
    def get_user_info_url(self, get_user_info_url):
        r"""Sets the get_user_info_url of this ShowSsoConfigResponse.

        用户信息查询URL。

        :param get_user_info_url: The get_user_info_url of this ShowSsoConfigResponse.
        :type get_user_info_url: str
        """
        self._get_user_info_url = get_user_info_url

    @property
    def oauth2_server_type(self):
        r"""Gets the oauth2_server_type of this ShowSsoConfigResponse.

        鉴权类型。OAuth2.0鉴权时取0。 * 0：OAuth2.0鉴权 

        :return: The oauth2_server_type of this ShowSsoConfigResponse.
        :rtype: int
        """
        return self._oauth2_server_type

    @oauth2_server_type.setter
    def oauth2_server_type(self, oauth2_server_type):
        r"""Sets the oauth2_server_type of this ShowSsoConfigResponse.

        鉴权类型。OAuth2.0鉴权时取0。 * 0：OAuth2.0鉴权 

        :param oauth2_server_type: The oauth2_server_type of this ShowSsoConfigResponse.
        :type oauth2_server_type: int
        """
        self._oauth2_server_type = oauth2_server_type

    @property
    def pc_schema_url(self):
        r"""Gets the pc_schema_url of this ShowSsoConfigResponse.

        拉起PC端终端的schema。

        :return: The pc_schema_url of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._pc_schema_url

    @pc_schema_url.setter
    def pc_schema_url(self, pc_schema_url):
        r"""Sets the pc_schema_url of this ShowSsoConfigResponse.

        拉起PC端终端的schema。

        :param pc_schema_url: The pc_schema_url of this ShowSsoConfigResponse.
        :type pc_schema_url: str
        """
        self._pc_schema_url = pc_schema_url

    @property
    def android_schema_url(self):
        r"""Gets the android_schema_url of this ShowSsoConfigResponse.

        拉起安卓端终端的schema。

        :return: The android_schema_url of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._android_schema_url

    @android_schema_url.setter
    def android_schema_url(self, android_schema_url):
        r"""Sets the android_schema_url of this ShowSsoConfigResponse.

        拉起安卓端终端的schema。

        :param android_schema_url: The android_schema_url of this ShowSsoConfigResponse.
        :type android_schema_url: str
        """
        self._android_schema_url = android_schema_url

    @property
    def ios_schema_url(self):
        r"""Gets the ios_schema_url of this ShowSsoConfigResponse.

        拉起ios端终端的schema。

        :return: The ios_schema_url of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._ios_schema_url

    @ios_schema_url.setter
    def ios_schema_url(self, ios_schema_url):
        r"""Sets the ios_schema_url of this ShowSsoConfigResponse.

        拉起ios端终端的schema。

        :param ios_schema_url: The ios_schema_url of this ShowSsoConfigResponse.
        :type ios_schema_url: str
        """
        self._ios_schema_url = ios_schema_url

    @property
    def third_name(self):
        r"""Gets the third_name of this ShowSsoConfigResponse.

        第三方名称的字段名称。

        :return: The third_name of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._third_name

    @third_name.setter
    def third_name(self, third_name):
        r"""Sets the third_name of this ShowSsoConfigResponse.

        第三方名称的字段名称。

        :param third_name: The third_name of this ShowSsoConfigResponse.
        :type third_name: str
        """
        self._third_name = third_name

    @property
    def third_email(self):
        r"""Gets the third_email of this ShowSsoConfigResponse.

        第三方邮箱的字段名称。

        :return: The third_email of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._third_email

    @third_email.setter
    def third_email(self, third_email):
        r"""Sets the third_email of this ShowSsoConfigResponse.

        第三方邮箱的字段名称。

        :param third_email: The third_email of this ShowSsoConfigResponse.
        :type third_email: str
        """
        self._third_email = third_email

    @property
    def third_mobile(self):
        r"""Gets the third_mobile of this ShowSsoConfigResponse.

        第三方手机号的字段名称。

        :return: The third_mobile of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._third_mobile

    @third_mobile.setter
    def third_mobile(self, third_mobile):
        r"""Sets the third_mobile of this ShowSsoConfigResponse.

        第三方手机号的字段名称。

        :param third_mobile: The third_mobile of this ShowSsoConfigResponse.
        :type third_mobile: str
        """
        self._third_mobile = third_mobile

    @property
    def third_access_token(self):
        r"""Gets the third_access_token of this ShowSsoConfigResponse.

        第三方accessToken的字段名称。

        :return: The third_access_token of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._third_access_token

    @third_access_token.setter
    def third_access_token(self, third_access_token):
        r"""Sets the third_access_token of this ShowSsoConfigResponse.

        第三方accessToken的字段名称。

        :param third_access_token: The third_access_token of this ShowSsoConfigResponse.
        :type third_access_token: str
        """
        self._third_access_token = third_access_token

    @property
    def third_head_img_url(self):
        r"""Gets the third_head_img_url of this ShowSsoConfigResponse.

        第三方头像链接的字段名称。

        :return: The third_head_img_url of this ShowSsoConfigResponse.
        :rtype: str
        """
        return self._third_head_img_url

    @third_head_img_url.setter
    def third_head_img_url(self, third_head_img_url):
        r"""Sets the third_head_img_url of this ShowSsoConfigResponse.

        第三方头像链接的字段名称。

        :param third_head_img_url: The third_head_img_url of this ShowSsoConfigResponse.
        :type third_head_img_url: str
        """
        self._third_head_img_url = third_head_img_url

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
        if not isinstance(other, ShowSsoConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
