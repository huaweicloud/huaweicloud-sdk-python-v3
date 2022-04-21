# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDbUserRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'db_username': 'str',
        'db_user_password': 'str'
    }

    attribute_map = {
        'db_username': 'db_username',
        'db_user_password': 'db_user_password'
    }

    def __init__(self, db_username=None, db_user_password=None):
        """UpdateDbUserRequestBody

        The model defined in huaweicloud sdk

        :param db_username: 数据库用户名称
        :type db_username: str
        :param db_user_password: 数据库用户密码
        :type db_user_password: str
        """
        
        

        self._db_username = None
        self._db_user_password = None
        self.discriminator = None

        self.db_username = db_username
        self.db_user_password = db_user_password

    @property
    def db_username(self):
        """Gets the db_username of this UpdateDbUserRequestBody.

        数据库用户名称

        :return: The db_username of this UpdateDbUserRequestBody.
        :rtype: str
        """
        return self._db_username

    @db_username.setter
    def db_username(self, db_username):
        """Sets the db_username of this UpdateDbUserRequestBody.

        数据库用户名称

        :param db_username: The db_username of this UpdateDbUserRequestBody.
        :type db_username: str
        """
        self._db_username = db_username

    @property
    def db_user_password(self):
        """Gets the db_user_password of this UpdateDbUserRequestBody.

        数据库用户密码

        :return: The db_user_password of this UpdateDbUserRequestBody.
        :rtype: str
        """
        return self._db_user_password

    @db_user_password.setter
    def db_user_password(self, db_user_password):
        """Sets the db_user_password of this UpdateDbUserRequestBody.

        数据库用户密码

        :param db_user_password: The db_user_password of this UpdateDbUserRequestBody.
        :type db_user_password: str
        """
        self._db_user_password = db_user_password

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
        if not isinstance(other, UpdateDbUserRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
