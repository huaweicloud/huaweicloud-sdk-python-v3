# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuertHistorySQLResultsBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'last_use_time': 'int',
        'sql_statement': 'str'
    }

    attribute_map = {
        'last_use_time': 'last_use_time',
        'sql_statement': 'sql_statement'
    }

    def __init__(self, last_use_time=None, sql_statement=None):
        """QuertHistorySQLResultsBody

        The model defined in huaweicloud sdk

        :param last_use_time: 上次修改时间，时间戳，毫秒数
        :type last_use_time: int
        :param sql_statement: 历史sql语句
        :type sql_statement: str
        """
        
        

        self._last_use_time = None
        self._sql_statement = None
        self.discriminator = None

        if last_use_time is not None:
            self.last_use_time = last_use_time
        if sql_statement is not None:
            self.sql_statement = sql_statement

    @property
    def last_use_time(self):
        """Gets the last_use_time of this QuertHistorySQLResultsBody.

        上次修改时间，时间戳，毫秒数

        :return: The last_use_time of this QuertHistorySQLResultsBody.
        :rtype: int
        """
        return self._last_use_time

    @last_use_time.setter
    def last_use_time(self, last_use_time):
        """Sets the last_use_time of this QuertHistorySQLResultsBody.

        上次修改时间，时间戳，毫秒数

        :param last_use_time: The last_use_time of this QuertHistorySQLResultsBody.
        :type last_use_time: int
        """
        self._last_use_time = last_use_time

    @property
    def sql_statement(self):
        """Gets the sql_statement of this QuertHistorySQLResultsBody.

        历史sql语句

        :return: The sql_statement of this QuertHistorySQLResultsBody.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        """Sets the sql_statement of this QuertHistorySQLResultsBody.

        历史sql语句

        :param sql_statement: The sql_statement of this QuertHistorySQLResultsBody.
        :type sql_statement: str
        """
        self._sql_statement = sql_statement

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
        if not isinstance(other, QuertHistorySQLResultsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
