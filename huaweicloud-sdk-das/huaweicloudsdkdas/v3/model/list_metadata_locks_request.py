# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetadataLocksRequest:

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
        'thread_id': 'str',
        'database': 'str',
        'table': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'db_user_id': 'db_user_id',
        'thread_id': 'thread_id',
        'database': 'database',
        'table': 'table',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, db_user_id=None, thread_id=None, database=None, table=None, x_language=None):
        """ListMetadataLocksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param db_user_id: 数据库用户ID
        :type db_user_id: str
        :param thread_id: 会话ID
        :type thread_id: str
        :param database: 数据库名称
        :type database: str
        :param table: 表名
        :type table: str
        :param x_language: 语言
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._db_user_id = None
        self._thread_id = None
        self._database = None
        self._table = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.db_user_id = db_user_id
        if thread_id is not None:
            self.thread_id = thread_id
        if database is not None:
            self.database = database
        if table is not None:
            self.table = table
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ListMetadataLocksRequest.

        实例ID

        :return: The instance_id of this ListMetadataLocksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListMetadataLocksRequest.

        实例ID

        :param instance_id: The instance_id of this ListMetadataLocksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def db_user_id(self):
        """Gets the db_user_id of this ListMetadataLocksRequest.

        数据库用户ID

        :return: The db_user_id of this ListMetadataLocksRequest.
        :rtype: str
        """
        return self._db_user_id

    @db_user_id.setter
    def db_user_id(self, db_user_id):
        """Sets the db_user_id of this ListMetadataLocksRequest.

        数据库用户ID

        :param db_user_id: The db_user_id of this ListMetadataLocksRequest.
        :type db_user_id: str
        """
        self._db_user_id = db_user_id

    @property
    def thread_id(self):
        """Gets the thread_id of this ListMetadataLocksRequest.

        会话ID

        :return: The thread_id of this ListMetadataLocksRequest.
        :rtype: str
        """
        return self._thread_id

    @thread_id.setter
    def thread_id(self, thread_id):
        """Sets the thread_id of this ListMetadataLocksRequest.

        会话ID

        :param thread_id: The thread_id of this ListMetadataLocksRequest.
        :type thread_id: str
        """
        self._thread_id = thread_id

    @property
    def database(self):
        """Gets the database of this ListMetadataLocksRequest.

        数据库名称

        :return: The database of this ListMetadataLocksRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ListMetadataLocksRequest.

        数据库名称

        :param database: The database of this ListMetadataLocksRequest.
        :type database: str
        """
        self._database = database

    @property
    def table(self):
        """Gets the table of this ListMetadataLocksRequest.

        表名

        :return: The table of this ListMetadataLocksRequest.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this ListMetadataLocksRequest.

        表名

        :param table: The table of this ListMetadataLocksRequest.
        :type table: str
        """
        self._table = table

    @property
    def x_language(self):
        """Gets the x_language of this ListMetadataLocksRequest.

        语言

        :return: The x_language of this ListMetadataLocksRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListMetadataLocksRequest.

        语言

        :param x_language: The x_language of this ListMetadataLocksRequest.
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
        if not isinstance(other, ListMetadataLocksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
