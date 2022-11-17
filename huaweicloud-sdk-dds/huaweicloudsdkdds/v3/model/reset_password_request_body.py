# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResetPasswordRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_pwd': 'str',
        'user_name': 'str',
        'db_name': 'str'
    }

    attribute_map = {
        'user_pwd': 'user_pwd',
        'user_name': 'user_name',
        'db_name': 'db_name'
    }

    def __init__(self, user_pwd=None, user_name=None, db_name=None):
        """ResetPasswordRequestBody

        The model defined in huaweicloud sdk

        :param user_pwd: 数据库密码。取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_&#x3D;+?的组合。建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。
        :type user_pwd: str
        :param user_name: 数据库用户名称，默认为“rwuser”。取值范围：长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。
        :type user_name: str
        :param db_name: 用户所在的数据库，默认为“admin”。取值范围：长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。
        :type db_name: str
        """
        
        

        self._user_pwd = None
        self._user_name = None
        self._db_name = None
        self.discriminator = None

        self.user_pwd = user_pwd
        if user_name is not None:
            self.user_name = user_name
        if db_name is not None:
            self.db_name = db_name

    @property
    def user_pwd(self):
        """Gets the user_pwd of this ResetPasswordRequestBody.

        数据库密码。取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :return: The user_pwd of this ResetPasswordRequestBody.
        :rtype: str
        """
        return self._user_pwd

    @user_pwd.setter
    def user_pwd(self, user_pwd):
        """Sets the user_pwd of this ResetPasswordRequestBody.

        数据库密码。取值范围：长度为8~32位，必须是大写字母（A~Z）、小写字母（a~z）、数字（0~9）、特殊字符~!@#%^*-_=+?的组合。建议您输入高强度密码，以提高安全性，防止出现密码被暴力破解等安全风险。

        :param user_pwd: The user_pwd of this ResetPasswordRequestBody.
        :type user_pwd: str
        """
        self._user_pwd = user_pwd

    @property
    def user_name(self):
        """Gets the user_name of this ResetPasswordRequestBody.

        数据库用户名称，默认为“rwuser”。取值范围：长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :return: The user_name of this ResetPasswordRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ResetPasswordRequestBody.

        数据库用户名称，默认为“rwuser”。取值范围：长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :param user_name: The user_name of this ResetPasswordRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def db_name(self):
        """Gets the db_name of this ResetPasswordRequestBody.

        用户所在的数据库，默认为“admin”。取值范围：长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :return: The db_name of this ResetPasswordRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this ResetPasswordRequestBody.

        用户所在的数据库，默认为“admin”。取值范围：长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :param db_name: The db_name of this ResetPasswordRequestBody.
        :type db_name: str
        """
        self._db_name = db_name

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
        if not isinstance(other, ResetPasswordRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
