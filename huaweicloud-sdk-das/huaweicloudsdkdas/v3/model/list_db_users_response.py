# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'db_users': 'list[DbUser]'
    }

    attribute_map = {
        'total': 'total',
        'db_users': 'db_users'
    }

    def __init__(self, total=None, db_users=None):
        """ListDbUsersResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param db_users: 数据库用户列表
        :type db_users: list[:class:`huaweicloudsdkdas.v3.DbUser`]
        """
        
        super(ListDbUsersResponse, self).__init__()

        self._total = None
        self._db_users = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if db_users is not None:
            self.db_users = db_users

    @property
    def total(self):
        """Gets the total of this ListDbUsersResponse.

        总数

        :return: The total of this ListDbUsersResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListDbUsersResponse.

        总数

        :param total: The total of this ListDbUsersResponse.
        :type total: int
        """
        self._total = total

    @property
    def db_users(self):
        """Gets the db_users of this ListDbUsersResponse.

        数据库用户列表

        :return: The db_users of this ListDbUsersResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.DbUser`]
        """
        return self._db_users

    @db_users.setter
    def db_users(self, db_users):
        """Sets the db_users of this ListDbUsersResponse.

        数据库用户列表

        :param db_users: The db_users of this ListDbUsersResponse.
        :type db_users: list[:class:`huaweicloudsdkdas.v3.DbUser`]
        """
        self._db_users = db_users

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
        if not isinstance(other, ListDbUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
