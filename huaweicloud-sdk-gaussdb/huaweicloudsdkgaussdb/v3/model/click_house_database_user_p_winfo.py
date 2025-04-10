# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClickHouseDatabaseUserPWinfo:

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
        'password': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'password': 'password'
    }

    def __init__(self, user_name=None, password=None):
        r"""ClickHouseDatabaseUserPWinfo

        The model defined in huaweicloud sdk

        :param user_name: 数据库账号名。
        :type user_name: str
        :param password: 数据库账号密码。 - 8-32个字符 - 至少包含以下字符中的三种：大写字母、小写字母、数字和特殊字符~！@#%^*-_&#x3D;+?, - 不能与用户名或倒序的用户名相同
        :type password: str
        """
        
        

        self._user_name = None
        self._password = None
        self.discriminator = None

        self.user_name = user_name
        self.password = password

    @property
    def user_name(self):
        r"""Gets the user_name of this ClickHouseDatabaseUserPWinfo.

        数据库账号名。

        :return: The user_name of this ClickHouseDatabaseUserPWinfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ClickHouseDatabaseUserPWinfo.

        数据库账号名。

        :param user_name: The user_name of this ClickHouseDatabaseUserPWinfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def password(self):
        r"""Gets the password of this ClickHouseDatabaseUserPWinfo.

        数据库账号密码。 - 8-32个字符 - 至少包含以下字符中的三种：大写字母、小写字母、数字和特殊字符~！@#%^*-_=+?, - 不能与用户名或倒序的用户名相同

        :return: The password of this ClickHouseDatabaseUserPWinfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this ClickHouseDatabaseUserPWinfo.

        数据库账号密码。 - 8-32个字符 - 至少包含以下字符中的三种：大写字母、小写字母、数字和特殊字符~！@#%^*-_=+?, - 不能与用户名或倒序的用户名相同

        :param password: The password of this ClickHouseDatabaseUserPWinfo.
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
        if not isinstance(other, ClickHouseDatabaseUserPWinfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
