# coding: utf-8

import pprint
import re

import six





class AgencyTokenResult:


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
        'issued_at': 'str',
        'assumed_by': 'AgencyAssumedby',
        'catalog': 'list[TokenCatalog]',
        'domain': 'AgencyTokenDomain',
        'project': 'AgencyTokenProject',
        'roles': 'list[TokenRole]',
        'user': 'AgencyTokenUser'
    }

    attribute_map = {
        'methods': 'methods',
        'expires_at': 'expires_at',
        'issued_at': 'issued_at',
        'assumed_by': 'assumed_by',
        'catalog': 'catalog',
        'domain': 'domain',
        'project': 'project',
        'roles': 'roles',
        'user': 'user'
    }

    def __init__(self, methods=None, expires_at=None, issued_at=None, assumed_by=None, catalog=None, domain=None, project=None, roles=None, user=None):
        """AgencyTokenResult - a model defined in huaweicloud sdk"""
        
        

        self._methods = None
        self._expires_at = None
        self._issued_at = None
        self._assumed_by = None
        self._catalog = None
        self._domain = None
        self._project = None
        self._roles = None
        self._user = None
        self.discriminator = None

        self.methods = methods
        self.expires_at = expires_at
        self.issued_at = issued_at
        self.assumed_by = assumed_by
        if catalog is not None:
            self.catalog = catalog
        if domain is not None:
            self.domain = domain
        if project is not None:
            self.project = project
        self.roles = roles
        self.user = user

    @property
    def methods(self):
        """Gets the methods of this AgencyTokenResult.

        获取token的方式。

        :return: The methods of this AgencyTokenResult.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this AgencyTokenResult.

        获取token的方式。

        :param methods: The methods of this AgencyTokenResult.
        :type: list[str]
        """
        self._methods = methods

    @property
    def expires_at(self):
        """Gets the expires_at of this AgencyTokenResult.

        token到期时间。

        :return: The expires_at of this AgencyTokenResult.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this AgencyTokenResult.

        token到期时间。

        :param expires_at: The expires_at of this AgencyTokenResult.
        :type: str
        """
        self._expires_at = expires_at

    @property
    def issued_at(self):
        """Gets the issued_at of this AgencyTokenResult.

        token下发时间。

        :return: The issued_at of this AgencyTokenResult.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this AgencyTokenResult.

        token下发时间。

        :param issued_at: The issued_at of this AgencyTokenResult.
        :type: str
        """
        self._issued_at = issued_at

    @property
    def assumed_by(self):
        """Gets the assumed_by of this AgencyTokenResult.


        :return: The assumed_by of this AgencyTokenResult.
        :rtype: AgencyAssumedby
        """
        return self._assumed_by

    @assumed_by.setter
    def assumed_by(self, assumed_by):
        """Sets the assumed_by of this AgencyTokenResult.


        :param assumed_by: The assumed_by of this AgencyTokenResult.
        :type: AgencyAssumedby
        """
        self._assumed_by = assumed_by

    @property
    def catalog(self):
        """Gets the catalog of this AgencyTokenResult.

        服务目录信息。

        :return: The catalog of this AgencyTokenResult.
        :rtype: list[TokenCatalog]
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this AgencyTokenResult.

        服务目录信息。

        :param catalog: The catalog of this AgencyTokenResult.
        :type: list[TokenCatalog]
        """
        self._catalog = catalog

    @property
    def domain(self):
        """Gets the domain of this AgencyTokenResult.


        :return: The domain of this AgencyTokenResult.
        :rtype: AgencyTokenDomain
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AgencyTokenResult.


        :param domain: The domain of this AgencyTokenResult.
        :type: AgencyTokenDomain
        """
        self._domain = domain

    @property
    def project(self):
        """Gets the project of this AgencyTokenResult.


        :return: The project of this AgencyTokenResult.
        :rtype: AgencyTokenProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this AgencyTokenResult.


        :param project: The project of this AgencyTokenResult.
        :type: AgencyTokenProject
        """
        self._project = project

    @property
    def roles(self):
        """Gets the roles of this AgencyTokenResult.

        委托token的权限信息。

        :return: The roles of this AgencyTokenResult.
        :rtype: list[TokenRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this AgencyTokenResult.

        委托token的权限信息。

        :param roles: The roles of this AgencyTokenResult.
        :type: list[TokenRole]
        """
        self._roles = roles

    @property
    def user(self):
        """Gets the user of this AgencyTokenResult.


        :return: The user of this AgencyTokenResult.
        :rtype: AgencyTokenUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AgencyTokenResult.


        :param user: The user of this AgencyTokenResult.
        :type: AgencyTokenUser
        """
        self._user = user

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
        if not isinstance(other, AgencyTokenResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
