# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnscopedTokenInfo:

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
        'roles': 'list[UnscopedTokenInfoRoles]',
        'catalog': 'list[UnscopedTokenInfoCatalog]'
    }

    attribute_map = {
        'expires_at': 'expires_at',
        'methods': 'methods',
        'issued_at': 'issued_at',
        'user': 'user',
        'roles': 'roles',
        'catalog': 'catalog'
    }

    def __init__(self, expires_at=None, methods=None, issued_at=None, user=None, roles=None, catalog=None):
        """UnscopedTokenInfo

        The model defined in huaweicloud sdk

        :param expires_at: 过期时间。
        :type expires_at: str
        :param methods: token获取方式，联邦认证默认为mapped。
        :type methods: list[str]
        :param issued_at: 生成时间。
        :type issued_at: str
        :param user: 
        :type user: :class:`huaweicloudsdkiam.v3.FederationUserBody`
        :param roles: roles信息。
        :type roles: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoRoles`]
        :param catalog: catalog信息。
        :type catalog: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoCatalog`]
        """
        
        

        self._expires_at = None
        self._methods = None
        self._issued_at = None
        self._user = None
        self._roles = None
        self._catalog = None
        self.discriminator = None

        self.expires_at = expires_at
        self.methods = methods
        self.issued_at = issued_at
        self.user = user
        if roles is not None:
            self.roles = roles
        if catalog is not None:
            self.catalog = catalog

    @property
    def expires_at(self):
        """Gets the expires_at of this UnscopedTokenInfo.

        过期时间。

        :return: The expires_at of this UnscopedTokenInfo.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this UnscopedTokenInfo.

        过期时间。

        :param expires_at: The expires_at of this UnscopedTokenInfo.
        :type expires_at: str
        """
        self._expires_at = expires_at

    @property
    def methods(self):
        """Gets the methods of this UnscopedTokenInfo.

        token获取方式，联邦认证默认为mapped。

        :return: The methods of this UnscopedTokenInfo.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """Sets the methods of this UnscopedTokenInfo.

        token获取方式，联邦认证默认为mapped。

        :param methods: The methods of this UnscopedTokenInfo.
        :type methods: list[str]
        """
        self._methods = methods

    @property
    def issued_at(self):
        """Gets the issued_at of this UnscopedTokenInfo.

        生成时间。

        :return: The issued_at of this UnscopedTokenInfo.
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this UnscopedTokenInfo.

        生成时间。

        :param issued_at: The issued_at of this UnscopedTokenInfo.
        :type issued_at: str
        """
        self._issued_at = issued_at

    @property
    def user(self):
        """Gets the user of this UnscopedTokenInfo.


        :return: The user of this UnscopedTokenInfo.
        :rtype: :class:`huaweicloudsdkiam.v3.FederationUserBody`
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UnscopedTokenInfo.


        :param user: The user of this UnscopedTokenInfo.
        :type user: :class:`huaweicloudsdkiam.v3.FederationUserBody`
        """
        self._user = user

    @property
    def roles(self):
        """Gets the roles of this UnscopedTokenInfo.

        roles信息。

        :return: The roles of this UnscopedTokenInfo.
        :rtype: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoRoles`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UnscopedTokenInfo.

        roles信息。

        :param roles: The roles of this UnscopedTokenInfo.
        :type roles: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoRoles`]
        """
        self._roles = roles

    @property
    def catalog(self):
        """Gets the catalog of this UnscopedTokenInfo.

        catalog信息。

        :return: The catalog of this UnscopedTokenInfo.
        :rtype: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoCatalog`]
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        """Sets the catalog of this UnscopedTokenInfo.

        catalog信息。

        :param catalog: The catalog of this UnscopedTokenInfo.
        :type catalog: list[:class:`huaweicloudsdkiam.v3.UnscopedTokenInfoCatalog`]
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
        if not isinstance(other, UnscopedTokenInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
