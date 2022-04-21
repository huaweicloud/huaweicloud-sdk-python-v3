# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteProcessReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'db_user_id': 'str',
        'process_ids': 'list[str]',
        'user': 'str',
        'database': 'str'
    }

    attribute_map = {
        'db_user_id': 'db_user_id',
        'process_ids': 'process_ids',
        'user': 'user',
        'database': 'database'
    }

    def __init__(self, db_user_id=None, process_ids=None, user=None, database=None):
        """DeleteProcessReqBody

        The model defined in huaweicloud sdk

        :param db_user_id: 数据库用户ID
        :type db_user_id: str
        :param process_ids: 会话ID列表。process_ids、user、database至少指定一个参数。
        :type process_ids: list[str]
        :param user: 用户
        :type user: str
        :param database: 数据库名称
        :type database: str
        """
        
        

        self._db_user_id = None
        self._process_ids = None
        self._user = None
        self._database = None
        self.discriminator = None

        self.db_user_id = db_user_id
        if process_ids is not None:
            self.process_ids = process_ids
        if user is not None:
            self.user = user
        if database is not None:
            self.database = database

    @property
    def db_user_id(self):
        """Gets the db_user_id of this DeleteProcessReqBody.

        数据库用户ID

        :return: The db_user_id of this DeleteProcessReqBody.
        :rtype: str
        """
        return self._db_user_id

    @db_user_id.setter
    def db_user_id(self, db_user_id):
        """Sets the db_user_id of this DeleteProcessReqBody.

        数据库用户ID

        :param db_user_id: The db_user_id of this DeleteProcessReqBody.
        :type db_user_id: str
        """
        self._db_user_id = db_user_id

    @property
    def process_ids(self):
        """Gets the process_ids of this DeleteProcessReqBody.

        会话ID列表。process_ids、user、database至少指定一个参数。

        :return: The process_ids of this DeleteProcessReqBody.
        :rtype: list[str]
        """
        return self._process_ids

    @process_ids.setter
    def process_ids(self, process_ids):
        """Sets the process_ids of this DeleteProcessReqBody.

        会话ID列表。process_ids、user、database至少指定一个参数。

        :param process_ids: The process_ids of this DeleteProcessReqBody.
        :type process_ids: list[str]
        """
        self._process_ids = process_ids

    @property
    def user(self):
        """Gets the user of this DeleteProcessReqBody.

        用户

        :return: The user of this DeleteProcessReqBody.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DeleteProcessReqBody.

        用户

        :param user: The user of this DeleteProcessReqBody.
        :type user: str
        """
        self._user = user

    @property
    def database(self):
        """Gets the database of this DeleteProcessReqBody.

        数据库名称

        :return: The database of this DeleteProcessReqBody.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this DeleteProcessReqBody.

        数据库名称

        :param database: The database of this DeleteProcessReqBody.
        :type database: str
        """
        self._database = database

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
        if not isinstance(other, DeleteProcessReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
