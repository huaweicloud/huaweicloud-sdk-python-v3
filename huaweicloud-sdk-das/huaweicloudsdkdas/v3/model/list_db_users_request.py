# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbUsersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'db_user_id': 'str',
        'db_username': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'db_user_id': 'db_user_id',
        'db_username': 'db_username',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, db_user_id=None, db_username=None, x_language=None):
        """ListDbUsersRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param db_user_id: 数据库用户ID
        :type db_user_id: str
        :param db_username: 数据库用户名称
        :type db_username: str
        :param x_language: 语言
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._db_user_id = None
        self._db_username = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if db_user_id is not None:
            self.db_user_id = db_user_id
        if db_username is not None:
            self.db_username = db_username
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDbUsersRequest.

        实例ID

        :return: The instance_id of this ListDbUsersRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDbUsersRequest.

        实例ID

        :param instance_id: The instance_id of this ListDbUsersRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListDbUsersRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListDbUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDbUsersRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListDbUsersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDbUsersRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ListDbUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDbUsersRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ListDbUsersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def db_user_id(self):
        """Gets the db_user_id of this ListDbUsersRequest.

        数据库用户ID

        :return: The db_user_id of this ListDbUsersRequest.
        :rtype: str
        """
        return self._db_user_id

    @db_user_id.setter
    def db_user_id(self, db_user_id):
        """Sets the db_user_id of this ListDbUsersRequest.

        数据库用户ID

        :param db_user_id: The db_user_id of this ListDbUsersRequest.
        :type db_user_id: str
        """
        self._db_user_id = db_user_id

    @property
    def db_username(self):
        """Gets the db_username of this ListDbUsersRequest.

        数据库用户名称

        :return: The db_username of this ListDbUsersRequest.
        :rtype: str
        """
        return self._db_username

    @db_username.setter
    def db_username(self, db_username):
        """Sets the db_username of this ListDbUsersRequest.

        数据库用户名称

        :param db_username: The db_username of this ListDbUsersRequest.
        :type db_username: str
        """
        self._db_username = db_username

    @property
    def x_language(self):
        """Gets the x_language of this ListDbUsersRequest.

        语言

        :return: The x_language of this ListDbUsersRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListDbUsersRequest.

        语言

        :param x_language: The x_language of this ListDbUsersRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListDbUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
