# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigIamUserDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'user_name': 'str',
        'domain_id': 'str',
        'domain_name': 'str',
        'is_domain_owner': 'bool'
    }

    attribute_map = {
        'user_id': 'user_id',
        'user_name': 'user_name',
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'is_domain_owner': 'is_domain_owner'
    }

    def __init__(self, user_id=None, user_name=None, domain_id=None, domain_name=None, is_domain_owner=None):
        r"""ApigIamUserDto

        The model defined in huaweicloud sdk

        :param user_id: 用户id
        :type user_id: str
        :param user_name: 用户名
        :type user_name: str
        :param domain_id: 租户id
        :type domain_id: str
        :param domain_name: 租户名
        :type domain_name: str
        :param is_domain_owner: 是否是空间拥有者
        :type is_domain_owner: bool
        """
        
        

        self._user_id = None
        self._user_name = None
        self._domain_id = None
        self._domain_name = None
        self._is_domain_owner = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        if is_domain_owner is not None:
            self.is_domain_owner = is_domain_owner

    @property
    def user_id(self):
        r"""Gets the user_id of this ApigIamUserDto.

        用户id

        :return: The user_id of this ApigIamUserDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ApigIamUserDto.

        用户id

        :param user_id: The user_id of this ApigIamUserDto.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this ApigIamUserDto.

        用户名

        :return: The user_name of this ApigIamUserDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ApigIamUserDto.

        用户名

        :param user_name: The user_name of this ApigIamUserDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ApigIamUserDto.

        租户id

        :return: The domain_id of this ApigIamUserDto.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ApigIamUserDto.

        租户id

        :param domain_id: The domain_id of this ApigIamUserDto.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ApigIamUserDto.

        租户名

        :return: The domain_name of this ApigIamUserDto.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ApigIamUserDto.

        租户名

        :param domain_name: The domain_name of this ApigIamUserDto.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def is_domain_owner(self):
        r"""Gets the is_domain_owner of this ApigIamUserDto.

        是否是空间拥有者

        :return: The is_domain_owner of this ApigIamUserDto.
        :rtype: bool
        """
        return self._is_domain_owner

    @is_domain_owner.setter
    def is_domain_owner(self, is_domain_owner):
        r"""Sets the is_domain_owner of this ApigIamUserDto.

        是否是空间拥有者

        :param is_domain_owner: The is_domain_owner of this ApigIamUserDto.
        :type is_domain_owner: bool
        """
        self._is_domain_owner = is_domain_owner

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
        if not isinstance(other, ApigIamUserDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
