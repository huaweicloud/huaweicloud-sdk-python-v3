# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class User:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'user_source': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_source': 'user_source',
        'user_id': 'user_id'
    }

    def __init__(self, user_name=None, user_source=None, user_id=None):
        r"""User

        The model defined in huaweicloud sdk

        :param user_name: 用户名
        :type user_name: str
        :param user_source: 用户类型 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 AGENTTENANT 委托 OTHER 其它
        :type user_source: str
        :param user_id: 用户ID
        :type user_id: str
        """
        
        

        self._user_name = None
        self._user_source = None
        self._user_id = None
        self.discriminator = None

        self.user_name = user_name
        self.user_source = user_source
        self.user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this User.

        用户名

        :return: The user_name of this User.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this User.

        用户名

        :param user_name: The user_name of this User.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_source(self):
        r"""Gets the user_source of this User.

        用户类型 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 AGENTTENANT 委托 OTHER 其它

        :return: The user_source of this User.
        :rtype: str
        """
        return self._user_source

    @user_source.setter
    def user_source(self, user_source):
        r"""Sets the user_source of this User.

        用户类型 IAM云用户 SAML联邦 LDAP ld用户 LOCAL 本地用户 AGENTTENANT 委托 OTHER 其它

        :param user_source: The user_source of this User.
        :type user_source: str
        """
        self._user_source = user_source

    @property
    def user_id(self):
        r"""Gets the user_id of this User.

        用户ID

        :return: The user_id of this User.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this User.

        用户ID

        :param user_id: The user_id of this User.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
