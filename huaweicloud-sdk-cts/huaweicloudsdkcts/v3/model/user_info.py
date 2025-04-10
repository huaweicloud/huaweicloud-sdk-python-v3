# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserInfo:

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
        'name': 'str',
        'user_name': 'str',
        'domain': 'BaseUser',
        'account_id': 'str',
        'access_key_id': 'str',
        'principal_urn': 'str',
        'principal_id': 'str',
        'principal_is_root_user': 'str',
        'type': 'str',
        'invoked_by': 'list[str]',
        'session_context': 'SessionContext'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_name': 'user_name',
        'domain': 'domain',
        'account_id': 'account_id',
        'access_key_id': 'access_key_id',
        'principal_urn': 'principal_urn',
        'principal_id': 'principal_id',
        'principal_is_root_user': 'principal_is_root_user',
        'type': 'type',
        'invoked_by': 'invoked_by',
        'session_context': 'session_context'
    }

    def __init__(self, id=None, name=None, user_name=None, domain=None, account_id=None, access_key_id=None, principal_urn=None, principal_id=None, principal_is_root_user=None, type=None, invoked_by=None, session_context=None):
        r"""UserInfo

        The model defined in huaweicloud sdk

        :param id: 用户ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。
        :type id: str
        :param name: 用户名称。
        :type name: str
        :param user_name: 用户名称。
        :type user_name: str
        :param domain: 
        :type domain: :class:`huaweicloudsdkcts.v3.BaseUser`
        :param account_id: 账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。
        :type account_id: str
        :param access_key_id: 访问密钥ID。
        :type access_key_id: str
        :param principal_urn: 操作用户身份的 URN。 如果是 IAM 用户身份，格式如 iam::&lt;account-id&gt;:user:&lt;user-name&gt;。 如果是 IAM 委托会话 身份，格式如 sts::&lt;account-id&gt;:assumed-agency:&lt;agency-name&gt;/&lt;agency-session-name&gt;。 如果是 IAM 联邦身份，格式如 sts::&lt;account-id&gt;:external-user:&lt;idp_id&gt;/&lt;user-session-name&gt;。
        :type principal_urn: str
        :param principal_id: 操作用户身份Id。 - 如果是 IAM 用户身份，格式为 &lt;user-id&gt;。 - 如果是 IAM 委托会话身份，格式为 &lt;agency-id&gt;:&lt;agency-session-name&gt;。 - 如果是 IAM 联邦身份，格式为 &lt;idp_id&gt;:&lt;user-session-name&gt;
        :type principal_id: str
        :param principal_is_root_user: 是否是根用户。 - 值为“true”时，表示操作者是根用户。 - 值为“false”时，表示操作者是委托会话身份、联邦身份或非根用户的 IAM 用户。
        :type principal_is_root_user: str
        :param type: 操作者身份类型。
        :type type: str
        :param invoked_by: 发出请求的服务的名称。控制台操作时为[\&quot;service.console\&quot; ]
        :type invoked_by: list[str]
        :param session_context: 
        :type session_context: :class:`huaweicloudsdkcts.v3.SessionContext`
        """
        
        

        self._id = None
        self._name = None
        self._user_name = None
        self._domain = None
        self._account_id = None
        self._access_key_id = None
        self._principal_urn = None
        self._principal_id = None
        self._principal_is_root_user = None
        self._type = None
        self._invoked_by = None
        self._session_context = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_name is not None:
            self.user_name = user_name
        if domain is not None:
            self.domain = domain
        if account_id is not None:
            self.account_id = account_id
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if principal_urn is not None:
            self.principal_urn = principal_urn
        if principal_id is not None:
            self.principal_id = principal_id
        if principal_is_root_user is not None:
            self.principal_is_root_user = principal_is_root_user
        if type is not None:
            self.type = type
        if invoked_by is not None:
            self.invoked_by = invoked_by
        if session_context is not None:
            self.session_context = session_context

    @property
    def id(self):
        r"""Gets the id of this UserInfo.

        用户ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :return: The id of this UserInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UserInfo.

        用户ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :param id: The id of this UserInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UserInfo.

        用户名称。

        :return: The name of this UserInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UserInfo.

        用户名称。

        :param name: The name of this UserInfo.
        :type name: str
        """
        self._name = name

    @property
    def user_name(self):
        r"""Gets the user_name of this UserInfo.

        用户名称。

        :return: The user_name of this UserInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this UserInfo.

        用户名称。

        :param user_name: The user_name of this UserInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain(self):
        r"""Gets the domain of this UserInfo.

        :return: The domain of this UserInfo.
        :rtype: :class:`huaweicloudsdkcts.v3.BaseUser`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this UserInfo.

        :param domain: The domain of this UserInfo.
        :type domain: :class:`huaweicloudsdkcts.v3.BaseUser`
        """
        self._domain = domain

    @property
    def account_id(self):
        r"""Gets the account_id of this UserInfo.

        账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :return: The account_id of this UserInfo.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this UserInfo.

        账号ID，参见《云审计服务API参考》“获取账号ID和项目ID”章节。

        :param account_id: The account_id of this UserInfo.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this UserInfo.

        访问密钥ID。

        :return: The access_key_id of this UserInfo.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this UserInfo.

        访问密钥ID。

        :param access_key_id: The access_key_id of this UserInfo.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def principal_urn(self):
        r"""Gets the principal_urn of this UserInfo.

        操作用户身份的 URN。 如果是 IAM 用户身份，格式如 iam::<account-id>:user:<user-name>。 如果是 IAM 委托会话 身份，格式如 sts::<account-id>:assumed-agency:<agency-name>/<agency-session-name>。 如果是 IAM 联邦身份，格式如 sts::<account-id>:external-user:<idp_id>/<user-session-name>。

        :return: The principal_urn of this UserInfo.
        :rtype: str
        """
        return self._principal_urn

    @principal_urn.setter
    def principal_urn(self, principal_urn):
        r"""Sets the principal_urn of this UserInfo.

        操作用户身份的 URN。 如果是 IAM 用户身份，格式如 iam::<account-id>:user:<user-name>。 如果是 IAM 委托会话 身份，格式如 sts::<account-id>:assumed-agency:<agency-name>/<agency-session-name>。 如果是 IAM 联邦身份，格式如 sts::<account-id>:external-user:<idp_id>/<user-session-name>。

        :param principal_urn: The principal_urn of this UserInfo.
        :type principal_urn: str
        """
        self._principal_urn = principal_urn

    @property
    def principal_id(self):
        r"""Gets the principal_id of this UserInfo.

        操作用户身份Id。 - 如果是 IAM 用户身份，格式为 <user-id>。 - 如果是 IAM 委托会话身份，格式为 <agency-id>:<agency-session-name>。 - 如果是 IAM 联邦身份，格式为 <idp_id>:<user-session-name>

        :return: The principal_id of this UserInfo.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        r"""Sets the principal_id of this UserInfo.

        操作用户身份Id。 - 如果是 IAM 用户身份，格式为 <user-id>。 - 如果是 IAM 委托会话身份，格式为 <agency-id>:<agency-session-name>。 - 如果是 IAM 联邦身份，格式为 <idp_id>:<user-session-name>

        :param principal_id: The principal_id of this UserInfo.
        :type principal_id: str
        """
        self._principal_id = principal_id

    @property
    def principal_is_root_user(self):
        r"""Gets the principal_is_root_user of this UserInfo.

        是否是根用户。 - 值为“true”时，表示操作者是根用户。 - 值为“false”时，表示操作者是委托会话身份、联邦身份或非根用户的 IAM 用户。

        :return: The principal_is_root_user of this UserInfo.
        :rtype: str
        """
        return self._principal_is_root_user

    @principal_is_root_user.setter
    def principal_is_root_user(self, principal_is_root_user):
        r"""Sets the principal_is_root_user of this UserInfo.

        是否是根用户。 - 值为“true”时，表示操作者是根用户。 - 值为“false”时，表示操作者是委托会话身份、联邦身份或非根用户的 IAM 用户。

        :param principal_is_root_user: The principal_is_root_user of this UserInfo.
        :type principal_is_root_user: str
        """
        self._principal_is_root_user = principal_is_root_user

    @property
    def type(self):
        r"""Gets the type of this UserInfo.

        操作者身份类型。

        :return: The type of this UserInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UserInfo.

        操作者身份类型。

        :param type: The type of this UserInfo.
        :type type: str
        """
        self._type = type

    @property
    def invoked_by(self):
        r"""Gets the invoked_by of this UserInfo.

        发出请求的服务的名称。控制台操作时为[\"service.console\" ]

        :return: The invoked_by of this UserInfo.
        :rtype: list[str]
        """
        return self._invoked_by

    @invoked_by.setter
    def invoked_by(self, invoked_by):
        r"""Sets the invoked_by of this UserInfo.

        发出请求的服务的名称。控制台操作时为[\"service.console\" ]

        :param invoked_by: The invoked_by of this UserInfo.
        :type invoked_by: list[str]
        """
        self._invoked_by = invoked_by

    @property
    def session_context(self):
        r"""Gets the session_context of this UserInfo.

        :return: The session_context of this UserInfo.
        :rtype: :class:`huaweicloudsdkcts.v3.SessionContext`
        """
        return self._session_context

    @session_context.setter
    def session_context(self, session_context):
        r"""Sets the session_context of this UserInfo.

        :param session_context: The session_context of this UserInfo.
        :type session_context: :class:`huaweicloudsdkcts.v3.SessionContext`
        """
        self._session_context = session_context

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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
