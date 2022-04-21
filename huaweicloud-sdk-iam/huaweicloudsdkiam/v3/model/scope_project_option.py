# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScopeProjectOption:

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
        'domain': 'ScopeDomainOption'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'domain': 'domain'
    }

    def __init__(self, id=None, name=None, domain=None):
        """ScopeProjectOption

        The model defined in huaweicloud sdk

        :param id: 项目ID，id与name二选一即可。
        :type id: str
        :param name: 项目名，id与name二选一即可。
        :type name: str
        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.ScopeDomainOption`
        """
        
        

        self._id = None
        self._name = None
        self._domain = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if domain is not None:
            self.domain = domain

    @property
    def id(self):
        """Gets the id of this ScopeProjectOption.

        项目ID，id与name二选一即可。

        :return: The id of this ScopeProjectOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScopeProjectOption.

        项目ID，id与name二选一即可。

        :param id: The id of this ScopeProjectOption.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ScopeProjectOption.

        项目名，id与name二选一即可。

        :return: The name of this ScopeProjectOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScopeProjectOption.

        项目名，id与name二选一即可。

        :param name: The name of this ScopeProjectOption.
        :type name: str
        """
        self._name = name

    @property
    def domain(self):
        """Gets the domain of this ScopeProjectOption.


        :return: The domain of this ScopeProjectOption.
        :rtype: :class:`huaweicloudsdkiam.v3.ScopeDomainOption`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ScopeProjectOption.


        :param domain: The domain of this ScopeProjectOption.
        :type domain: :class:`huaweicloudsdkiam.v3.ScopeDomainOption`
        """
        self._domain = domain

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
        if not isinstance(other, ScopeProjectOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
