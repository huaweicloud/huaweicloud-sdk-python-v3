# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DbUserPwdRequest:

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
        'password': 'str'
    }

    attribute_map = {
        'name': 'name',
        'password': 'password'
    }

    def __init__(self, name=None, password=None):
        """DbUserPwdRequest

        The model defined in huaweicloud sdk

        :param name: 数据库帐号名称，不能为系统账号用户。系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。
        :type name: str
        :param password: 数据库帐号密码。  取值范围：  非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#%^*-_&#x3D;+?,组成，长度8~32个字符，不能和数据库帐号“name”或“name”的逆序相同，或不能和当前密码相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type password: str
        """
        
        

        self._name = None
        self._password = None
        self.discriminator = None

        self.name = name
        self.password = password

    @property
    def name(self):
        """Gets the name of this DbUserPwdRequest.

        数据库帐号名称，不能为系统账号用户。系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。

        :return: The name of this DbUserPwdRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DbUserPwdRequest.

        数据库帐号名称，不能为系统账号用户。系统用户包括“rdsAdmin”,“ rdsMetric”, “rdsBackup”, “rdsRepl”。

        :param name: The name of this DbUserPwdRequest.
        :type name: str
        """
        self._name = name

    @property
    def password(self):
        """Gets the password of this DbUserPwdRequest.

        数据库帐号密码。  取值范围：  非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#%^*-_=+?,组成，长度8~32个字符，不能和数据库帐号“name”或“name”的逆序相同，或不能和当前密码相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The password of this DbUserPwdRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this DbUserPwdRequest.

        数据库帐号密码。  取值范围：  非空，至少包含以下字符中的三种：大写字母、小写字母、数字和特殊符号~!@#%^*-_=+?,组成，长度8~32个字符，不能和数据库帐号“name”或“name”的逆序相同，或不能和当前密码相同。  建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param password: The password of this DbUserPwdRequest.
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
        if not isinstance(other, DbUserPwdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
