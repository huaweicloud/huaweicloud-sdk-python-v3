# coding: utf-8

import pprint
import re

import six





class ScopeTokenResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'methods': 'list[str]',
        'expires_at': 'str',
        'catalog': 'list[TokenCatalog]',
        'domain': 'TokenDomainResult',
        'project': 'TokenProjectResult',
        'roles': 'list[TokenRole]',
        'user': 'ScopedTokenUser',
        'issued_at': 'str'
    }

    attribute_map = {
        'methods': 'methods',
        'expires_at': 'expires_at',
        'catalog': 'catalog',
        'domain': 'domain',
        'project': 'project',
        'roles': 'roles',
        'user': 'user',
        'issued_at': 'issued_at'
    }

    def __init__(self, methods=None, expires_at=None, catalog=None, domain=None, project=None, roles=None, user=None, issued_at=None):
        """ScopeTokenResult - a model defined in huaweicloud sdk"""
        
        

        self._methods = None
        self._expires_at = None
        self._catalog = None
        self._domain = None
        self._project = None
        self._roles = None
        self._user = None
        self._issued_at = None
        self.discriminator = None

        self.methods = methods
        self.expires_at = expires_at
        if catalog is not None:
            self.catalog = catalog
        self.domain = domain
        self.project = project
        self.roles = roles
        self.user = user
        self.issued_at = issued_at

    @property
    def methods(self):
        """Gets the methods of this ScopeTokenResult.

        获取token的方式。

        :return: The methods of this ScopeTokenResult.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this ScopeTokenResult.

        获取token的方式。

        :param methods: The methods of this ScopeTokenResult.
        :type: list[str]
        """
        self._methods = methods

    @property
    def expires_at(self):
        """Gets the expires_at of this ScopeTokenResult.

        token过期时间。

        :return: The expires_at of this ScopeTokenResult.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this ScopeTokenResult.

        token过期时间。

        :param expires_at: The expires_at of this ScopeTokenResult.
        :type: str
        """
        self._expires_at = expires_at

    @property
    def catalog(self):
        """Gets the catalog of this ScopeTokenResult.

        服务目录信息。

        :return: The catalog of this ScopeTokenResult.
        :rtype: list[TokenCatalog]
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this ScopeTokenResult.

        服务目录信息。

        :param catalog: The catalog of this ScopeTokenResult.
        :type: list[TokenCatalog]
        """
        self._catalog = catalog

    @property
    def domain(self):
        """Gets the domain of this ScopeTokenResult.


        :return: The domain of this ScopeTokenResult.
        :rtype: TokenDomainResult
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ScopeTokenResult.


        :param domain: The domain of this ScopeTokenResult.
        :type: TokenDomainResult
        """
        self._domain = domain

    @property
    def project(self):
        """Gets the project of this ScopeTokenResult.


        :return: The project of this ScopeTokenResult.
        :rtype: TokenProjectResult
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ScopeTokenResult.


        :param project: The project of this ScopeTokenResult.
        :type: TokenProjectResult
        """
        self._project = project

    @property
    def roles(self):
        """Gets the roles of this ScopeTokenResult.

        token的权限信息。

        :return: The roles of this ScopeTokenResult.
        :rtype: list[TokenRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ScopeTokenResult.

        token的权限信息。

        :param roles: The roles of this ScopeTokenResult.
        :type: list[TokenRole]
        """
        self._roles = roles

    @property
    def user(self):
        """Gets the user of this ScopeTokenResult.


        :return: The user of this ScopeTokenResult.
        :rtype: ScopedTokenUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ScopeTokenResult.


        :param user: The user of this ScopeTokenResult.
        :type: ScopedTokenUser
        """
        self._user = user

    @property
    def issued_at(self):
        """Gets the issued_at of this ScopeTokenResult.

        token下发时间。

        :return: The issued_at of this ScopeTokenResult.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this ScopeTokenResult.

        token下发时间。

        :param issued_at: The issued_at of this ScopeTokenResult.
        :type: str
        """
        self._issued_at = issued_at

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScopeTokenResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
