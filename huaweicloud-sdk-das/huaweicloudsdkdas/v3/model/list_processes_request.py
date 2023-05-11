# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProcessesRequest:

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
        'db_user_id': 'str',
        'user': 'str',
        'database': 'str',
        'offset': 'int',
        'limit': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'db_user_id': 'db_user_id',
        'user': 'user',
        'database': 'database',
        'offset': 'offset',
        'limit': 'limit',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, db_user_id=None, user=None, database=None, offset=None, limit=None, x_language=None):
        """ListProcessesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param db_user_id: 数据库用户ID
        :type db_user_id: str
        :param user: 用户
        :type user: str
        :param database: 数据库
        :type database: str
        :param offset: 偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 每页记录数，默认为20，最大取值100。
        :type limit: int
        :param x_language: 语言
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._db_user_id = None
        self._user = None
        self._database = None
        self._offset = None
        self._limit = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.db_user_id = db_user_id
        if user is not None:
            self.user = user
        if database is not None:
            self.database = database
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListProcessesRequest.

        实例ID

        :return: The instance_id of this ListProcessesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListProcessesRequest.

        实例ID

        :param instance_id: The instance_id of this ListProcessesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def db_user_id(self):
        """Gets the db_user_id of this ListProcessesRequest.

        数据库用户ID

        :return: The db_user_id of this ListProcessesRequest.
        :rtype: str
        """
        return self._db_user_id

    @db_user_id.setter
    def db_user_id(self, db_user_id):
        """Sets the db_user_id of this ListProcessesRequest.

        数据库用户ID

        :param db_user_id: The db_user_id of this ListProcessesRequest.
        :type db_user_id: str
        """
        self._db_user_id = db_user_id

    @property
    def user(self):
        """Gets the user of this ListProcessesRequest.

        用户

        :return: The user of this ListProcessesRequest.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ListProcessesRequest.

        用户

        :param user: The user of this ListProcessesRequest.
        :type user: str
        """
        self._user = user

    @property
    def database(self):
        """Gets the database of this ListProcessesRequest.

        数据库

        :return: The database of this ListProcessesRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ListProcessesRequest.

        数据库

        :param database: The database of this ListProcessesRequest.
        :type database: str
        """
        self._database = database

    @property
    def offset(self):
        """Gets the offset of this ListProcessesRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ListProcessesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProcessesRequest.

        偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ListProcessesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProcessesRequest.

        每页记录数，默认为20，最大取值100。

        :return: The limit of this ListProcessesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProcessesRequest.

        每页记录数，默认为20，最大取值100。

        :param limit: The limit of this ListProcessesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListProcessesRequest.

        语言

        :return: The x_language of this ListProcessesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListProcessesRequest.

        语言

        :param x_language: The x_language of this ListProcessesRequest.
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
        if not isinstance(other, ListProcessesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
