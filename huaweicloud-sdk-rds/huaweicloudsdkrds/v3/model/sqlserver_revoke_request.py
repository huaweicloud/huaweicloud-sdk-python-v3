# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlserverRevokeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'users': 'list[SqlserverUserWithPrivilege]'
    }

    attribute_map = {
        'db_name': 'db_name',
        'users': 'users'
    }

    def __init__(self, db_name=None, users=None):
        """SqlserverRevokeRequest

        The model defined in huaweicloud sdk

        :param db_name: 数据库名称。
        :type db_name: str
        :param users: 每个元素都是与数据库相关联的帐号。单次请求最多支持50个元素。
        :type users: list[:class:`huaweicloudsdkrds.v3.SqlserverUserWithPrivilege`]
        """
        
        

        self._db_name = None
        self._users = None
        self.discriminator = None

        self.db_name = db_name
        self.users = users

    @property
    def db_name(self):
        """Gets the db_name of this SqlserverRevokeRequest.

        数据库名称。

        :return: The db_name of this SqlserverRevokeRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this SqlserverRevokeRequest.

        数据库名称。

        :param db_name: The db_name of this SqlserverRevokeRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def users(self):
        """Gets the users of this SqlserverRevokeRequest.

        每个元素都是与数据库相关联的帐号。单次请求最多支持50个元素。

        :return: The users of this SqlserverRevokeRequest.
        :rtype: list[:class:`huaweicloudsdkrds.v3.SqlserverUserWithPrivilege`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this SqlserverRevokeRequest.

        每个元素都是与数据库相关联的帐号。单次请求最多支持50个元素。

        :param users: The users of this SqlserverRevokeRequest.
        :type users: list[:class:`huaweicloudsdkrds.v3.SqlserverUserWithPrivilege`]
        """
        self._users = users

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
        if not isinstance(other, SqlserverRevokeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
