# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IamAccount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'iam_user': 'str',
        'iam_user_id': 'str',
        'user_account': 'str',
        'iam_token': 'str',
        'iam_domain': 'str',
        'iam_domain_id': 'str',
        'iam_x_domain_id': 'str',
        'iam_x_domain_type': 'str',
        'iam_project_id': 'str',
        'iam_project_name': 'str',
        'language': 'str',
        'instance_id': 'str',
        'assumed_by_domain_id': 'str',
        'assumed_by_user_id': 'str',
        'assumed_by_user_name': 'str',
        'roles': 'list[str]',
        'exclusive_project_id': 'str',
        'eps_enable': 'bool',
        'shared_project_name': 'str',
        'authorization': 'str',
        'context_attributes': 'str',
        'user_profile': 'str',
        'sts_token': 'str',
        'access_key_id': 'str',
        'secret_access_key': 'str',
        'source_account': 'str',
        'source_urn': 'str',
        'request_proof': 'str',
        'x_project_id': 'str',
        'fulfillment_agency': 'str',
        'operation_id': 'str'
    }

    attribute_map = {
        'iam_user': 'iam_user',
        'iam_user_id': 'iam_user_id',
        'user_account': 'user_account',
        'iam_token': 'iam_token',
        'iam_domain': 'iam_domain',
        'iam_domain_id': 'iam_domain_id',
        'iam_x_domain_id': 'iam_x_domain_id',
        'iam_x_domain_type': 'iam_x_domain_type',
        'iam_project_id': 'iam_project_id',
        'iam_project_name': 'iam_project_name',
        'language': 'language',
        'instance_id': 'instance_id',
        'assumed_by_domain_id': 'assumed_by_domain_id',
        'assumed_by_user_id': 'assumed_by_user_id',
        'assumed_by_user_name': 'assumed_by_user_name',
        'roles': 'roles',
        'exclusive_project_id': 'exclusive_project_id',
        'eps_enable': 'eps_enable',
        'shared_project_name': 'shared_project_name',
        'authorization': 'authorization',
        'context_attributes': 'context_attributes',
        'user_profile': 'user_profile',
        'sts_token': 'sts_token',
        'access_key_id': 'access_key_id',
        'secret_access_key': 'secret_access_key',
        'source_account': 'source_account',
        'source_urn': 'source_urn',
        'request_proof': 'request_proof',
        'x_project_id': 'x_project_id',
        'fulfillment_agency': 'fulfillment_agency',
        'operation_id': 'operation_id'
    }

    def __init__(self, iam_user=None, iam_user_id=None, user_account=None, iam_token=None, iam_domain=None, iam_domain_id=None, iam_x_domain_id=None, iam_x_domain_type=None, iam_project_id=None, iam_project_name=None, language=None, instance_id=None, assumed_by_domain_id=None, assumed_by_user_id=None, assumed_by_user_name=None, roles=None, exclusive_project_id=None, eps_enable=None, shared_project_name=None, authorization=None, context_attributes=None, user_profile=None, sts_token=None, access_key_id=None, secret_access_key=None, source_account=None, source_urn=None, request_proof=None, x_project_id=None, fulfillment_agency=None, operation_id=None):
        r"""IamAccount

        The model defined in huaweicloud sdk

        :param iam_user: iam账号。
        :type iam_user: str
        :param iam_user_id: iam账号id。
        :type iam_user_id: str
        :param user_account: iam账号权限。
        :type user_account: str
        :param iam_token: iam账号token。
        :type iam_token: str
        :param iam_domain: iamdomain账号。
        :type iam_domain: str
        :param iam_domain_id: iamdomain账号id。
        :type iam_domain_id: str
        :param iam_x_domain_id: iamxdomain账号id。
        :type iam_x_domain_id: str
        :param iam_x_domain_type: iamxdomain账号类型。
        :type iam_x_domain_type: str
        :param iam_project_id: iam项目id。
        :type iam_project_id: str
        :param iam_project_name: iam项目名称。
        :type iam_project_name: str
        :param language: 语言。
        :type language: str
        :param instance_id: 实例id。
        :type instance_id: str
        :param assumed_by_domain_id: assumed_by_domain_id。
        :type assumed_by_domain_id: str
        :param assumed_by_user_id: assumed_by_user_id。
        :type assumed_by_user_id: str
        :param assumed_by_user_name: assumed_by_user_name。
        :type assumed_by_user_name: str
        :param roles: 角色信息。
        :type roles: list[str]
        :param exclusive_project_id: exclusive_project_id。
        :type exclusive_project_id: str
        :param eps_enable: 是否支持eps。
        :type eps_enable: bool
        :param shared_project_name: shared_project_name。
        :type shared_project_name: str
        :param authorization: authorization。
        :type authorization: str
        :param context_attributes: 文本属性。
        :type context_attributes: str
        :param user_profile: 用户文件。
        :type user_profile: str
        :param sts_token: sts_token。
        :type sts_token: str
        :param access_key_id: access_key_id。
        :type access_key_id: str
        :param secret_access_key: secret_access_key。
        :type secret_access_key: str
        :param source_account: source_account。
        :type source_account: str
        :param source_urn: source_urn。
        :type source_urn: str
        :param request_proof: request_proof。
        :type request_proof: str
        :param x_project_id: x_project_id。
        :type x_project_id: str
        :param fulfillment_agency: fulfillment_agency。
        :type fulfillment_agency: str
        :param operation_id: operation_id。
        :type operation_id: str
        """
        
        

        self._iam_user = None
        self._iam_user_id = None
        self._user_account = None
        self._iam_token = None
        self._iam_domain = None
        self._iam_domain_id = None
        self._iam_x_domain_id = None
        self._iam_x_domain_type = None
        self._iam_project_id = None
        self._iam_project_name = None
        self._language = None
        self._instance_id = None
        self._assumed_by_domain_id = None
        self._assumed_by_user_id = None
        self._assumed_by_user_name = None
        self._roles = None
        self._exclusive_project_id = None
        self._eps_enable = None
        self._shared_project_name = None
        self._authorization = None
        self._context_attributes = None
        self._user_profile = None
        self._sts_token = None
        self._access_key_id = None
        self._secret_access_key = None
        self._source_account = None
        self._source_urn = None
        self._request_proof = None
        self._x_project_id = None
        self._fulfillment_agency = None
        self._operation_id = None
        self.discriminator = None

        if iam_user is not None:
            self.iam_user = iam_user
        if iam_user_id is not None:
            self.iam_user_id = iam_user_id
        if user_account is not None:
            self.user_account = user_account
        if iam_token is not None:
            self.iam_token = iam_token
        if iam_domain is not None:
            self.iam_domain = iam_domain
        if iam_domain_id is not None:
            self.iam_domain_id = iam_domain_id
        if iam_x_domain_id is not None:
            self.iam_x_domain_id = iam_x_domain_id
        if iam_x_domain_type is not None:
            self.iam_x_domain_type = iam_x_domain_type
        if iam_project_id is not None:
            self.iam_project_id = iam_project_id
        if iam_project_name is not None:
            self.iam_project_name = iam_project_name
        if language is not None:
            self.language = language
        if instance_id is not None:
            self.instance_id = instance_id
        if assumed_by_domain_id is not None:
            self.assumed_by_domain_id = assumed_by_domain_id
        if assumed_by_user_id is not None:
            self.assumed_by_user_id = assumed_by_user_id
        if assumed_by_user_name is not None:
            self.assumed_by_user_name = assumed_by_user_name
        if roles is not None:
            self.roles = roles
        if exclusive_project_id is not None:
            self.exclusive_project_id = exclusive_project_id
        if eps_enable is not None:
            self.eps_enable = eps_enable
        if shared_project_name is not None:
            self.shared_project_name = shared_project_name
        if authorization is not None:
            self.authorization = authorization
        if context_attributes is not None:
            self.context_attributes = context_attributes
        if user_profile is not None:
            self.user_profile = user_profile
        if sts_token is not None:
            self.sts_token = sts_token
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if source_account is not None:
            self.source_account = source_account
        if source_urn is not None:
            self.source_urn = source_urn
        if request_proof is not None:
            self.request_proof = request_proof
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if fulfillment_agency is not None:
            self.fulfillment_agency = fulfillment_agency
        if operation_id is not None:
            self.operation_id = operation_id

    @property
    def iam_user(self):
        r"""Gets the iam_user of this IamAccount.

        iam账号。

        :return: The iam_user of this IamAccount.
        :rtype: str
        """
        return self._iam_user

    @iam_user.setter
    def iam_user(self, iam_user):
        r"""Sets the iam_user of this IamAccount.

        iam账号。

        :param iam_user: The iam_user of this IamAccount.
        :type iam_user: str
        """
        self._iam_user = iam_user

    @property
    def iam_user_id(self):
        r"""Gets the iam_user_id of this IamAccount.

        iam账号id。

        :return: The iam_user_id of this IamAccount.
        :rtype: str
        """
        return self._iam_user_id

    @iam_user_id.setter
    def iam_user_id(self, iam_user_id):
        r"""Sets the iam_user_id of this IamAccount.

        iam账号id。

        :param iam_user_id: The iam_user_id of this IamAccount.
        :type iam_user_id: str
        """
        self._iam_user_id = iam_user_id

    @property
    def user_account(self):
        r"""Gets the user_account of this IamAccount.

        iam账号权限。

        :return: The user_account of this IamAccount.
        :rtype: str
        """
        return self._user_account

    @user_account.setter
    def user_account(self, user_account):
        r"""Sets the user_account of this IamAccount.

        iam账号权限。

        :param user_account: The user_account of this IamAccount.
        :type user_account: str
        """
        self._user_account = user_account

    @property
    def iam_token(self):
        r"""Gets the iam_token of this IamAccount.

        iam账号token。

        :return: The iam_token of this IamAccount.
        :rtype: str
        """
        return self._iam_token

    @iam_token.setter
    def iam_token(self, iam_token):
        r"""Sets the iam_token of this IamAccount.

        iam账号token。

        :param iam_token: The iam_token of this IamAccount.
        :type iam_token: str
        """
        self._iam_token = iam_token

    @property
    def iam_domain(self):
        r"""Gets the iam_domain of this IamAccount.

        iamdomain账号。

        :return: The iam_domain of this IamAccount.
        :rtype: str
        """
        return self._iam_domain

    @iam_domain.setter
    def iam_domain(self, iam_domain):
        r"""Sets the iam_domain of this IamAccount.

        iamdomain账号。

        :param iam_domain: The iam_domain of this IamAccount.
        :type iam_domain: str
        """
        self._iam_domain = iam_domain

    @property
    def iam_domain_id(self):
        r"""Gets the iam_domain_id of this IamAccount.

        iamdomain账号id。

        :return: The iam_domain_id of this IamAccount.
        :rtype: str
        """
        return self._iam_domain_id

    @iam_domain_id.setter
    def iam_domain_id(self, iam_domain_id):
        r"""Sets the iam_domain_id of this IamAccount.

        iamdomain账号id。

        :param iam_domain_id: The iam_domain_id of this IamAccount.
        :type iam_domain_id: str
        """
        self._iam_domain_id = iam_domain_id

    @property
    def iam_x_domain_id(self):
        r"""Gets the iam_x_domain_id of this IamAccount.

        iamxdomain账号id。

        :return: The iam_x_domain_id of this IamAccount.
        :rtype: str
        """
        return self._iam_x_domain_id

    @iam_x_domain_id.setter
    def iam_x_domain_id(self, iam_x_domain_id):
        r"""Sets the iam_x_domain_id of this IamAccount.

        iamxdomain账号id。

        :param iam_x_domain_id: The iam_x_domain_id of this IamAccount.
        :type iam_x_domain_id: str
        """
        self._iam_x_domain_id = iam_x_domain_id

    @property
    def iam_x_domain_type(self):
        r"""Gets the iam_x_domain_type of this IamAccount.

        iamxdomain账号类型。

        :return: The iam_x_domain_type of this IamAccount.
        :rtype: str
        """
        return self._iam_x_domain_type

    @iam_x_domain_type.setter
    def iam_x_domain_type(self, iam_x_domain_type):
        r"""Sets the iam_x_domain_type of this IamAccount.

        iamxdomain账号类型。

        :param iam_x_domain_type: The iam_x_domain_type of this IamAccount.
        :type iam_x_domain_type: str
        """
        self._iam_x_domain_type = iam_x_domain_type

    @property
    def iam_project_id(self):
        r"""Gets the iam_project_id of this IamAccount.

        iam项目id。

        :return: The iam_project_id of this IamAccount.
        :rtype: str
        """
        return self._iam_project_id

    @iam_project_id.setter
    def iam_project_id(self, iam_project_id):
        r"""Sets the iam_project_id of this IamAccount.

        iam项目id。

        :param iam_project_id: The iam_project_id of this IamAccount.
        :type iam_project_id: str
        """
        self._iam_project_id = iam_project_id

    @property
    def iam_project_name(self):
        r"""Gets the iam_project_name of this IamAccount.

        iam项目名称。

        :return: The iam_project_name of this IamAccount.
        :rtype: str
        """
        return self._iam_project_name

    @iam_project_name.setter
    def iam_project_name(self, iam_project_name):
        r"""Sets the iam_project_name of this IamAccount.

        iam项目名称。

        :param iam_project_name: The iam_project_name of this IamAccount.
        :type iam_project_name: str
        """
        self._iam_project_name = iam_project_name

    @property
    def language(self):
        r"""Gets the language of this IamAccount.

        语言。

        :return: The language of this IamAccount.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this IamAccount.

        语言。

        :param language: The language of this IamAccount.
        :type language: str
        """
        self._language = language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this IamAccount.

        实例id。

        :return: The instance_id of this IamAccount.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this IamAccount.

        实例id。

        :param instance_id: The instance_id of this IamAccount.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def assumed_by_domain_id(self):
        r"""Gets the assumed_by_domain_id of this IamAccount.

        assumed_by_domain_id。

        :return: The assumed_by_domain_id of this IamAccount.
        :rtype: str
        """
        return self._assumed_by_domain_id

    @assumed_by_domain_id.setter
    def assumed_by_domain_id(self, assumed_by_domain_id):
        r"""Sets the assumed_by_domain_id of this IamAccount.

        assumed_by_domain_id。

        :param assumed_by_domain_id: The assumed_by_domain_id of this IamAccount.
        :type assumed_by_domain_id: str
        """
        self._assumed_by_domain_id = assumed_by_domain_id

    @property
    def assumed_by_user_id(self):
        r"""Gets the assumed_by_user_id of this IamAccount.

        assumed_by_user_id。

        :return: The assumed_by_user_id of this IamAccount.
        :rtype: str
        """
        return self._assumed_by_user_id

    @assumed_by_user_id.setter
    def assumed_by_user_id(self, assumed_by_user_id):
        r"""Sets the assumed_by_user_id of this IamAccount.

        assumed_by_user_id。

        :param assumed_by_user_id: The assumed_by_user_id of this IamAccount.
        :type assumed_by_user_id: str
        """
        self._assumed_by_user_id = assumed_by_user_id

    @property
    def assumed_by_user_name(self):
        r"""Gets the assumed_by_user_name of this IamAccount.

        assumed_by_user_name。

        :return: The assumed_by_user_name of this IamAccount.
        :rtype: str
        """
        return self._assumed_by_user_name

    @assumed_by_user_name.setter
    def assumed_by_user_name(self, assumed_by_user_name):
        r"""Sets the assumed_by_user_name of this IamAccount.

        assumed_by_user_name。

        :param assumed_by_user_name: The assumed_by_user_name of this IamAccount.
        :type assumed_by_user_name: str
        """
        self._assumed_by_user_name = assumed_by_user_name

    @property
    def roles(self):
        r"""Gets the roles of this IamAccount.

        角色信息。

        :return: The roles of this IamAccount.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this IamAccount.

        角色信息。

        :param roles: The roles of this IamAccount.
        :type roles: list[str]
        """
        self._roles = roles

    @property
    def exclusive_project_id(self):
        r"""Gets the exclusive_project_id of this IamAccount.

        exclusive_project_id。

        :return: The exclusive_project_id of this IamAccount.
        :rtype: str
        """
        return self._exclusive_project_id

    @exclusive_project_id.setter
    def exclusive_project_id(self, exclusive_project_id):
        r"""Sets the exclusive_project_id of this IamAccount.

        exclusive_project_id。

        :param exclusive_project_id: The exclusive_project_id of this IamAccount.
        :type exclusive_project_id: str
        """
        self._exclusive_project_id = exclusive_project_id

    @property
    def eps_enable(self):
        r"""Gets the eps_enable of this IamAccount.

        是否支持eps。

        :return: The eps_enable of this IamAccount.
        :rtype: bool
        """
        return self._eps_enable

    @eps_enable.setter
    def eps_enable(self, eps_enable):
        r"""Sets the eps_enable of this IamAccount.

        是否支持eps。

        :param eps_enable: The eps_enable of this IamAccount.
        :type eps_enable: bool
        """
        self._eps_enable = eps_enable

    @property
    def shared_project_name(self):
        r"""Gets the shared_project_name of this IamAccount.

        shared_project_name。

        :return: The shared_project_name of this IamAccount.
        :rtype: str
        """
        return self._shared_project_name

    @shared_project_name.setter
    def shared_project_name(self, shared_project_name):
        r"""Sets the shared_project_name of this IamAccount.

        shared_project_name。

        :param shared_project_name: The shared_project_name of this IamAccount.
        :type shared_project_name: str
        """
        self._shared_project_name = shared_project_name

    @property
    def authorization(self):
        r"""Gets the authorization of this IamAccount.

        authorization。

        :return: The authorization of this IamAccount.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this IamAccount.

        authorization。

        :param authorization: The authorization of this IamAccount.
        :type authorization: str
        """
        self._authorization = authorization

    @property
    def context_attributes(self):
        r"""Gets the context_attributes of this IamAccount.

        文本属性。

        :return: The context_attributes of this IamAccount.
        :rtype: str
        """
        return self._context_attributes

    @context_attributes.setter
    def context_attributes(self, context_attributes):
        r"""Sets the context_attributes of this IamAccount.

        文本属性。

        :param context_attributes: The context_attributes of this IamAccount.
        :type context_attributes: str
        """
        self._context_attributes = context_attributes

    @property
    def user_profile(self):
        r"""Gets the user_profile of this IamAccount.

        用户文件。

        :return: The user_profile of this IamAccount.
        :rtype: str
        """
        return self._user_profile

    @user_profile.setter
    def user_profile(self, user_profile):
        r"""Sets the user_profile of this IamAccount.

        用户文件。

        :param user_profile: The user_profile of this IamAccount.
        :type user_profile: str
        """
        self._user_profile = user_profile

    @property
    def sts_token(self):
        r"""Gets the sts_token of this IamAccount.

        sts_token。

        :return: The sts_token of this IamAccount.
        :rtype: str
        """
        return self._sts_token

    @sts_token.setter
    def sts_token(self, sts_token):
        r"""Sets the sts_token of this IamAccount.

        sts_token。

        :param sts_token: The sts_token of this IamAccount.
        :type sts_token: str
        """
        self._sts_token = sts_token

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this IamAccount.

        access_key_id。

        :return: The access_key_id of this IamAccount.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this IamAccount.

        access_key_id。

        :param access_key_id: The access_key_id of this IamAccount.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        r"""Gets the secret_access_key of this IamAccount.

        secret_access_key。

        :return: The secret_access_key of this IamAccount.
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        r"""Sets the secret_access_key of this IamAccount.

        secret_access_key。

        :param secret_access_key: The secret_access_key of this IamAccount.
        :type secret_access_key: str
        """
        self._secret_access_key = secret_access_key

    @property
    def source_account(self):
        r"""Gets the source_account of this IamAccount.

        source_account。

        :return: The source_account of this IamAccount.
        :rtype: str
        """
        return self._source_account

    @source_account.setter
    def source_account(self, source_account):
        r"""Sets the source_account of this IamAccount.

        source_account。

        :param source_account: The source_account of this IamAccount.
        :type source_account: str
        """
        self._source_account = source_account

    @property
    def source_urn(self):
        r"""Gets the source_urn of this IamAccount.

        source_urn。

        :return: The source_urn of this IamAccount.
        :rtype: str
        """
        return self._source_urn

    @source_urn.setter
    def source_urn(self, source_urn):
        r"""Sets the source_urn of this IamAccount.

        source_urn。

        :param source_urn: The source_urn of this IamAccount.
        :type source_urn: str
        """
        self._source_urn = source_urn

    @property
    def request_proof(self):
        r"""Gets the request_proof of this IamAccount.

        request_proof。

        :return: The request_proof of this IamAccount.
        :rtype: str
        """
        return self._request_proof

    @request_proof.setter
    def request_proof(self, request_proof):
        r"""Sets the request_proof of this IamAccount.

        request_proof。

        :param request_proof: The request_proof of this IamAccount.
        :type request_proof: str
        """
        self._request_proof = request_proof

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this IamAccount.

        x_project_id。

        :return: The x_project_id of this IamAccount.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this IamAccount.

        x_project_id。

        :param x_project_id: The x_project_id of this IamAccount.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def fulfillment_agency(self):
        r"""Gets the fulfillment_agency of this IamAccount.

        fulfillment_agency。

        :return: The fulfillment_agency of this IamAccount.
        :rtype: str
        """
        return self._fulfillment_agency

    @fulfillment_agency.setter
    def fulfillment_agency(self, fulfillment_agency):
        r"""Sets the fulfillment_agency of this IamAccount.

        fulfillment_agency。

        :param fulfillment_agency: The fulfillment_agency of this IamAccount.
        :type fulfillment_agency: str
        """
        self._fulfillment_agency = fulfillment_agency

    @property
    def operation_id(self):
        r"""Gets the operation_id of this IamAccount.

        operation_id。

        :return: The operation_id of this IamAccount.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this IamAccount.

        operation_id。

        :param operation_id: The operation_id of this IamAccount.
        :type operation_id: str
        """
        self._operation_id = operation_id

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
        if not isinstance(other, IamAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
