# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckSQLGramarReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sql': 'str',
        'currentdb': 'str'
    }

    attribute_map = {
        'sql': 'sql',
        'currentdb': 'currentdb'
    }

    def __init__(self, sql=None, currentdb=None):
        """CheckSQLGramarReq

        The model defined in huaweicloud sdk

        :param sql: 待执行的SQL语句。
        :type sql: str
        :param currentdb: SQL语句执行所在的数据库。
        :type currentdb: str
        """
        
        

        self._sql = None
        self._currentdb = None
        self.discriminator = None

        self.sql = sql
        if currentdb is not None:
            self.currentdb = currentdb

    @property
    def sql(self):
        """Gets the sql of this CheckSQLGramarReq.

        待执行的SQL语句。

        :return: The sql of this CheckSQLGramarReq.
        :rtype: str
        """
        return self._sql

    @sql.setter
    def sql(self, sql):
        """Sets the sql of this CheckSQLGramarReq.

        待执行的SQL语句。

        :param sql: The sql of this CheckSQLGramarReq.
        :type sql: str
        """
        self._sql = sql

    @property
    def currentdb(self):
        """Gets the currentdb of this CheckSQLGramarReq.

        SQL语句执行所在的数据库。

        :return: The currentdb of this CheckSQLGramarReq.
        :rtype: str
        """
        return self._currentdb

    @currentdb.setter
    def currentdb(self, currentdb):
        """Sets the currentdb of this CheckSQLGramarReq.

        SQL语句执行所在的数据库。

        :param currentdb: The currentdb of this CheckSQLGramarReq.
        :type currentdb: str
        """
        self._currentdb = currentdb

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
        if not isinstance(other, CheckSQLGramarReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other