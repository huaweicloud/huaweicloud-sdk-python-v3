# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FederationUserBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_federation': 'OsFederationInfo',
        'domain': 'DomainInfo',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'os_federation': 'OS-FEDERATION',
        'domain': 'domain',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, os_federation=None, domain=None, id=None, name=None):
        """FederationUserBody

        The model defined in huaweicloud sdk

        :param os_federation: 
        :type os_federation: :class:`huaweicloudsdkiam.v3.OsFederationInfo`
        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.DomainInfo`
        :param id: user id。
        :type id: str
        :param name: user name。
        :type name: str
        """
        
        

        self._os_federation = None
        self._domain = None
        self._id = None
        self._name = None
        self.discriminator = None

        self.os_federation = os_federation
        self.domain = domain
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def os_federation(self):
        """Gets the os_federation of this FederationUserBody.

        :return: The os_federation of this FederationUserBody.
        :rtype: :class:`huaweicloudsdkiam.v3.OsFederationInfo`
        """
        return self._os_federation

    @os_federation.setter
    def os_federation(self, os_federation):
        """Sets the os_federation of this FederationUserBody.

        :param os_federation: The os_federation of this FederationUserBody.
        :type os_federation: :class:`huaweicloudsdkiam.v3.OsFederationInfo`
        """
        self._os_federation = os_federation

    @property
    def domain(self):
        """Gets the domain of this FederationUserBody.

        :return: The domain of this FederationUserBody.
        :rtype: :class:`huaweicloudsdkiam.v3.DomainInfo`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this FederationUserBody.

        :param domain: The domain of this FederationUserBody.
        :type domain: :class:`huaweicloudsdkiam.v3.DomainInfo`
        """
        self._domain = domain

    @property
    def id(self):
        """Gets the id of this FederationUserBody.

        user id。

        :return: The id of this FederationUserBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FederationUserBody.

        user id。

        :param id: The id of this FederationUserBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this FederationUserBody.

        user name。

        :return: The name of this FederationUserBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FederationUserBody.

        user name。

        :param name: The name of this FederationUserBody.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, FederationUserBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
