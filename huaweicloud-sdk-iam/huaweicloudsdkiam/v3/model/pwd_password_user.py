# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PwdPasswordUser:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'PwdPasswordUserDomain',
        'name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'name': 'name',
        'password': 'password'
    }

    def __init__(self, domain=None, name=None, password=None):
        """PwdPasswordUser

        The model defined in huaweicloud sdk

        :param domain: 
        :type domain: :class:`huaweicloudsdkiam.v3.PwdPasswordUserDomain`
        :param name: IAM用户名，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。
        :type name: str
        :param password: IAM用户的登录密码。
        :type password: str
        """
        
        

        self._domain = None
        self._name = None
        self._password = None
        self.discriminator = None

        self.domain = domain
        self.name = name
        self.password = password

    @property
    def domain(self):
        """Gets the domain of this PwdPasswordUser.

        :return: The domain of this PwdPasswordUser.
        :rtype: :class:`huaweicloudsdkiam.v3.PwdPasswordUserDomain`
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this PwdPasswordUser.

        :param domain: The domain of this PwdPasswordUser.
        :type domain: :class:`huaweicloudsdkiam.v3.PwdPasswordUserDomain`
        """
        self._domain = domain

    @property
    def name(self):
        """Gets the name of this PwdPasswordUser.

        IAM用户名，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The name of this PwdPasswordUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PwdPasswordUser.

        IAM用户名，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param name: The name of this PwdPasswordUser.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this PwdPasswordUser.

        IAM用户的登录密码。

        :return: The password of this PwdPasswordUser.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PwdPasswordUser.

        IAM用户的登录密码。

        :param password: The password of this PwdPasswordUser.
        :type password: str
        """
        self._password = password

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
        if not isinstance(other, PwdPasswordUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
