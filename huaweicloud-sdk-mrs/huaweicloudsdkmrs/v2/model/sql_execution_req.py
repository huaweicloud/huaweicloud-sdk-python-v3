# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlExecutionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_type': 'str',
        'sql_content': 'str',
        'database': 'str',
        'archive_path': 'str'
    }

    attribute_map = {
        'sql_type': 'sql_type',
        'sql_content': 'sql_content',
        'database': 'database',
        'archive_path': 'archive_path'
    }

    def __init__(self, sql_type=None, sql_content=None, database=None, archive_path=None):
        """SqlExecutionReq

        The model defined in huaweicloud sdk

        :param sql_type: SQL类型。目前仅支持“presto”类型的SQL。 说明： - 只有包含Presto组件的集群才能提交执行presto类型的SQL。 - 当前仅MRS 2.0.6版本的MRS 2.0.6.1补丁、MRS 2.1.0版本的MRS 2.1.0.7补丁、MRS 3.1.2及之后版本集群支持。
        :type sql_type: str
        :param sql_content: 待执行的SQL语句。 说明： 目前仅支持执行单条语句，语句中不包含“;”。
        :type sql_content: str
        :param database: 执行SQL所在的数据库，默认为default。
        :type database: str
        :param archive_path: SQL执行结果的转储文件夹。 说明： 只有select语句才会转储查询的结果。当前仅支持转储到OBS中。
        :type archive_path: str
        """
        
        

        self._sql_type = None
        self._sql_content = None
        self._database = None
        self._archive_path = None
        self.discriminator = None

        self.sql_type = sql_type
        self.sql_content = sql_content
        if database is not None:
            self.database = database
        if archive_path is not None:
            self.archive_path = archive_path

    @property
    def sql_type(self):
        """Gets the sql_type of this SqlExecutionReq.

        SQL类型。目前仅支持“presto”类型的SQL。 说明： - 只有包含Presto组件的集群才能提交执行presto类型的SQL。 - 当前仅MRS 2.0.6版本的MRS 2.0.6.1补丁、MRS 2.1.0版本的MRS 2.1.0.7补丁、MRS 3.1.2及之后版本集群支持。

        :return: The sql_type of this SqlExecutionReq.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        """Sets the sql_type of this SqlExecutionReq.

        SQL类型。目前仅支持“presto”类型的SQL。 说明： - 只有包含Presto组件的集群才能提交执行presto类型的SQL。 - 当前仅MRS 2.0.6版本的MRS 2.0.6.1补丁、MRS 2.1.0版本的MRS 2.1.0.7补丁、MRS 3.1.2及之后版本集群支持。

        :param sql_type: The sql_type of this SqlExecutionReq.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def sql_content(self):
        """Gets the sql_content of this SqlExecutionReq.

        待执行的SQL语句。 说明： 目前仅支持执行单条语句，语句中不包含“;”。

        :return: The sql_content of this SqlExecutionReq.
        :rtype: str
        """
        return self._sql_content

    @sql_content.setter
    def sql_content(self, sql_content):
        """Sets the sql_content of this SqlExecutionReq.

        待执行的SQL语句。 说明： 目前仅支持执行单条语句，语句中不包含“;”。

        :param sql_content: The sql_content of this SqlExecutionReq.
        :type sql_content: str
        """
        self._sql_content = sql_content

    @property
    def database(self):
        """Gets the database of this SqlExecutionReq.

        执行SQL所在的数据库，默认为default。

        :return: The database of this SqlExecutionReq.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this SqlExecutionReq.

        执行SQL所在的数据库，默认为default。

        :param database: The database of this SqlExecutionReq.
        :type database: str
        """
        self._database = database

    @property
    def archive_path(self):
        """Gets the archive_path of this SqlExecutionReq.

        SQL执行结果的转储文件夹。 说明： 只有select语句才会转储查询的结果。当前仅支持转储到OBS中。

        :return: The archive_path of this SqlExecutionReq.
        :rtype: str
        """
        return self._archive_path

    @archive_path.setter
    def archive_path(self, archive_path):
        """Sets the archive_path of this SqlExecutionReq.

        SQL执行结果的转储文件夹。 说明： 只有select语句才会转储查询的结果。当前仅支持转储到OBS中。

        :param archive_path: The archive_path of this SqlExecutionReq.
        :type archive_path: str
        """
        self._archive_path = archive_path

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
        if not isinstance(other, SqlExecutionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
