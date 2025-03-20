# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnscopedTokenUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'TokenDomainResult',
        'id': 'str',
        'name': 'str',
        'os_federation': 'TokenUserOsfederation'
    }

    attribute_map = {
        'domain': 'domain',
        'id': 'id',
        'name': 'name',
        'os_federation': 'OS-FEDERATION'
    }

    def __init__(self, domain=None, id=None, name=None, os_federation=None):
        """UnscopedTokenUser

        The model defined in huaweicloud sdk

        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.TokenDomainResult`
        :param id: 用户ID。
        :type id: str
        :param name: 用户名称。
        :type name: str
        :param os_federation: 
        :type os_federation: :class:`huaweicloudsdkiam.v3.TokenUserOsfederation`
        """
        
        

        self._domain = None
        self._id = None
        self._name = None
        self._os_federation = None
        self.discriminator = None

        self.domain = domain
        self.id = id
        self.name = name
        self.os_federation = os_federation

    @property
    def domain(self):
        """Gets the domain of this UnscopedTokenUser.

        :return: The domain of this UnscopedTokenUser.
        :rtype: :class:`huaweicloudsdkiam.v3.TokenDomainResult`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this UnscopedTokenUser.

        :param domain: The domain of this UnscopedTokenUser.
        :type domain: :class:`huaweicloudsdkiam.v3.TokenDomainResult`
        """
        self._domain = domain

    @property
    def id(self):
        """Gets the id of this UnscopedTokenUser.

        用户ID。

        :return: The id of this UnscopedTokenUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnscopedTokenUser.

        用户ID。

        :param id: The id of this UnscopedTokenUser.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UnscopedTokenUser.

        用户名称。

        :return: The name of this UnscopedTokenUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnscopedTokenUser.

        用户名称。

        :param name: The name of this UnscopedTokenUser.
        :type name: str
        """
        self._name = name

    @property
    def os_federation(self):
        """Gets the os_federation of this UnscopedTokenUser.

        :return: The os_federation of this UnscopedTokenUser.
        :rtype: :class:`huaweicloudsdkiam.v3.TokenUserOsfederation`
        """
        return self._os_federation

    @os_federation.setter
    def os_federation(self, os_federation):
        """Sets the os_federation of this UnscopedTokenUser.

        :param os_federation: The os_federation of this UnscopedTokenUser.
        :type os_federation: :class:`huaweicloudsdkiam.v3.TokenUserOsfederation`
        """
        self._os_federation = os_federation

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
        if not isinstance(other, UnscopedTokenUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
