# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'DomainDto',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, domain=None, id=None, name=None):
        r"""UserDto

        The model defined in huaweicloud sdk

        :param domain: 
        :type domain: :class:`huaweicloudsdkeihealth.v1.DomainDto`
        :param id: 用户id
        :type id: str
        :param name: 用户名
        :type name: str
        """
        
        

        self._domain = None
        self._id = None
        self._name = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def domain(self):
        r"""Gets the domain of this UserDto.

        :return: The domain of this UserDto.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DomainDto`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this UserDto.

        :param domain: The domain of this UserDto.
        :type domain: :class:`huaweicloudsdkeihealth.v1.DomainDto`
        """
        self._domain = domain

    @property
    def id(self):
        r"""Gets the id of this UserDto.

        用户id

        :return: The id of this UserDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UserDto.

        用户id

        :param id: The id of this UserDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this UserDto.

        用户名

        :return: The name of this UserDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UserDto.

        用户名

        :param name: The name of this UserDto.
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
        if not isinstance(other, UserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
