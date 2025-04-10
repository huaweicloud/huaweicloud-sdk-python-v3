# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScopedTokenInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expires_at': 'str',
        'methods': 'list[str]',
        'issued_at': 'str',
        'user': 'FederationUserBody',
        'domain': 'DomainInfo',
        'project': 'ProjectInfo',
        'roles': 'list[ScopedTokenInfoRoles]',
        'catalog': 'list[UnscopedTokenInfoEndpoints]'
    }

    attribute_map = {
        'expires_at': 'expires_at',
        'methods': 'methods',
        'issued_at': 'issued_at',
        'user': 'user',
        'domain': 'domain',
        'project': 'project',
        'roles': 'roles',
        'catalog': 'catalog'
    }

    def __init__(self, expires_at=None, methods=None, issued_at=None, user=None, domain=None, project=None, roles=None, catalog=None):
        r"""ScopedTokenInfo

        The model defined in huaweicloud sdk

        :param expires_at: 过期时间。
        :type expires_at: str
        :param methods: 获取token的方式，联邦用户默认为mapped。
        :type methods: list[str]
        :param issued_at: 生成时间。
        :type issued_at: str
        :param user: 
        :type user: :class:`huaweicloudsdkiam.v3.FederationUserBody`
        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.DomainInfo`
        :param project: 
        :type project: :class:`huaweicloudsdkiam.v3.ProjectInfo`
        :param roles: roles信息。
        :type roles: list[:class:`huaweicloudsdkiam.v3.ScopedTokenInfoRoles`]
        :param catalog: catalog信息
        :type catalog: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoEndpoints`]
        """
        
        

        self._expires_at = None
        self._methods = None
        self._issued_at = None
        self._user = None
        self._domain = None
        self._project = None
        self._roles = None
        self._catalog = None
        self.discriminator = None

        self.expires_at = expires_at
        self.methods = methods
        self.issued_at = issued_at
        self.user = user
        if domain is not None:
            self.domain = domain
        if project is not None:
            self.project = project
        self.roles = roles
        self.catalog = catalog

    @property
    def expires_at(self):
        r"""Gets the expires_at of this ScopedTokenInfo.

        过期时间。

        :return: The expires_at of this ScopedTokenInfo.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        r"""Sets the expires_at of this ScopedTokenInfo.

        过期时间。

        :param expires_at: The expires_at of this ScopedTokenInfo.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def methods(self):
        r"""Gets the methods of this ScopedTokenInfo.

        获取token的方式，联邦用户默认为mapped。

        :return: The methods of this ScopedTokenInfo.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        r"""Sets the methods of this ScopedTokenInfo.

        获取token的方式，联邦用户默认为mapped。

        :param methods: The methods of this ScopedTokenInfo.
        :type methods: list[str]
        """
        self._methods = methods

    @property
    def issued_at(self):
        r"""Gets the issued_at of this ScopedTokenInfo.

        生成时间。

        :return: The issued_at of this ScopedTokenInfo.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        r"""Sets the issued_at of this ScopedTokenInfo.

        生成时间。

        :param issued_at: The issued_at of this ScopedTokenInfo.
        :type issued_at: str
        """
        self._issued_at = issued_at

    @property
    def user(self):
        r"""Gets the user of this ScopedTokenInfo.

        :return: The user of this ScopedTokenInfo.
        :rtype: :class:`huaweicloudsdkiam.v3.FederationUserBody`
        """
        return self._user

    @user.setter
    def user(self, user):
        r"""Sets the user of this ScopedTokenInfo.

        :param user: The user of this ScopedTokenInfo.
        :type user: :class:`huaweicloudsdkiam.v3.FederationUserBody`
        """
        self._user = user

    @property
    def domain(self):
        r"""Gets the domain of this ScopedTokenInfo.

        :return: The domain of this ScopedTokenInfo.
        :rtype: :class:`huaweicloudsdkiam.v3.DomainInfo`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ScopedTokenInfo.

        :param domain: The domain of this ScopedTokenInfo.
        :type domain: :class:`huaweicloudsdkiam.v3.DomainInfo`
        """
        self._domain = domain

    @property
    def project(self):
        r"""Gets the project of this ScopedTokenInfo.

        :return: The project of this ScopedTokenInfo.
        :rtype: :class:`huaweicloudsdkiam.v3.ProjectInfo`
        """
        return self._project

    @project.setter
    def project(self, project):
        r"""Sets the project of this ScopedTokenInfo.

        :param project: The project of this ScopedTokenInfo.
        :type project: :class:`huaweicloudsdkiam.v3.ProjectInfo`
        """
        self._project = project

    @property
    def roles(self):
        r"""Gets the roles of this ScopedTokenInfo.

        roles信息。

        :return: The roles of this ScopedTokenInfo.
        :rtype: list[:class:`huaweicloudsdkiam.v3.ScopedTokenInfoRoles`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this ScopedTokenInfo.

        roles信息。

        :param roles: The roles of this ScopedTokenInfo.
        :type roles: list[:class:`huaweicloudsdkiam.v3.ScopedTokenInfoRoles`]
        """
        self._roles = roles

    @property
    def catalog(self):
        r"""Gets the catalog of this ScopedTokenInfo.

        catalog信息

        :return: The catalog of this ScopedTokenInfo.
        :rtype: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoEndpoints`]
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        r"""Sets the catalog of this ScopedTokenInfo.

        catalog信息

        :param catalog: The catalog of this ScopedTokenInfo.
        :type catalog: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoEndpoints`]
        """
        self._catalog = catalog

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
        if not isinstance(other, ScopedTokenInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
