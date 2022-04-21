# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDatabaseUserRequestBody:

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
        'db_name': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'db_name': 'db_name'
    }

    def __init__(self, user_name=None, db_name=None):
        """DeleteDatabaseUserRequestBody

        The model defined in huaweicloud sdk

        :param user_name: 数据库用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。
        :type user_name: str
        :param db_name: 用户所在的数据库。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。
        :type db_name: str
        """
        
        

        self._user_name = None
        self._db_name = None
        self.discriminator = None

        self.user_name = user_name
        self.db_name = db_name

    @property
    def user_name(self):
        """Gets the user_name of this DeleteDatabaseUserRequestBody.

        数据库用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :return: The user_name of this DeleteDatabaseUserRequestBody.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this DeleteDatabaseUserRequestBody.

        数据库用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :param user_name: The user_name of this DeleteDatabaseUserRequestBody.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def db_name(self):
        """Gets the db_name of this DeleteDatabaseUserRequestBody.

        用户所在的数据库。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :return: The db_name of this DeleteDatabaseUserRequestBody.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DeleteDatabaseUserRequestBody.

        用户所在的数据库。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :param db_name: The db_name of this DeleteDatabaseUserRequestBody.
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
        if not isinstance(other, DeleteDatabaseUserRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
