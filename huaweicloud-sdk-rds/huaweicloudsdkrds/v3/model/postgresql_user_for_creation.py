# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgresqlUserForCreation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'password': 'str',
        'comment': 'str'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password',
        'comment': 'comment'
    }

    def __init__(self, name=None, password=None, comment=None):
        """PostgresqlUserForCreation

        The model defined in huaweicloud sdk

        :param name: 数据库用户名称。  数据库用户名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和系统用户名称相同。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”,“ rdsProxy”, “rdsDdm”。
        :type name: str
        :param password: 数据库用户密码。  取值范围：非空，密码长度在8到32个字符之间，至少包含大写字母、小写字母、数字、特殊字符~!@#%^*-_&#x3D;+?,三种字符的组合，不能和数据库帐号“name”或“name”的逆序相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        :param comment: 数据库用户备注。 取值范围：长度1~512个字符。
        :type comment: str
        """
        
        

        self._name = None
        self._password = None
        self._comment = None
        self.discriminator = None

        self.name = name
        self.password = password
        if comment is not None:
            self.comment = comment

    @property
    def name(self):
        """Gets the name of this PostgresqlUserForCreation.

        数据库用户名称。  数据库用户名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和系统用户名称相同。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”,“ rdsProxy”, “rdsDdm”。

        :return: The name of this PostgresqlUserForCreation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostgresqlUserForCreation.

        数据库用户名称。  数据库用户名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，不能和系统用户名称相同。  系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”,“ rdsProxy”, “rdsDdm”。

        :param name: The name of this PostgresqlUserForCreation.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this PostgresqlUserForCreation.

        数据库用户密码。  取值范围：非空，密码长度在8到32个字符之间，至少包含大写字母、小写字母、数字、特殊字符~!@#%^*-_=+?,三种字符的组合，不能和数据库帐号“name”或“name”的逆序相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this PostgresqlUserForCreation.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this PostgresqlUserForCreation.

        数据库用户密码。  取值范围：非空，密码长度在8到32个字符之间，至少包含大写字母、小写字母、数字、特殊字符~!@#%^*-_=+?,三种字符的组合，不能和数据库帐号“name”或“name”的逆序相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this PostgresqlUserForCreation.
        :type password: str
        """
        self._password = password

    @property
    def comment(self):
        """Gets the comment of this PostgresqlUserForCreation.

        数据库用户备注。 取值范围：长度1~512个字符。

        :return: The comment of this PostgresqlUserForCreation.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PostgresqlUserForCreation.

        数据库用户备注。 取值范围：长度1~512个字符。

        :param comment: The comment of this PostgresqlUserForCreation.
        :type comment: str
        """
        self._comment = comment

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
        if not isinstance(other, PostgresqlUserForCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
