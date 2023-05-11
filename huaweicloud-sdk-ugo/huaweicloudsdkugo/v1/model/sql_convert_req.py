# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlConvertReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_db_type': 'str',
        'target_db_type': 'str',
        'target_db_version': 'str',
        'sql_statement': 'str'
    }

    attribute_map = {
        'source_db_type': 'source_db_type',
        'target_db_type': 'target_db_type',
        'target_db_version': 'target_db_version',
        'sql_statement': 'sql_statement'
    }

    def __init__(self, source_db_type=None, target_db_type=None, target_db_version=None, sql_statement=None):
        """SqlConvertReq

        The model defined in huaweicloud sdk

        :param source_db_type: 源数据库类型。
        :type source_db_type: str
        :param target_db_type: 目标数据库类型。其中GaussDB Centralized已弃用。
        :type target_db_type: str
        :param target_db_version: 目标数据库版本。 （注意：该字段需要与 target_db_type 字段组合成有效的目标数据库类型与版本，当前支持以下组合： GaussDB Centralized-2.0（已弃用）； GaussDB Primary/Standby-2.0； RDS for PostgreSQL-11； RDS for PostgreSQL-Enhanced Edition； RDS for MySQL-5.7; GaussDB(for MySQL) 8.0。)
        :type target_db_version: str
        :param sql_statement: 需要转换的SQL语句。
        :type sql_statement: str
        """
        
        

        self._source_db_type = None
        self._target_db_type = None
        self._target_db_version = None
        self._sql_statement = None
        self.discriminator = None

        self.source_db_type = source_db_type
        self.target_db_type = target_db_type
        self.target_db_version = target_db_version
        self.sql_statement = sql_statement

    @property
    def source_db_type(self):
        """Gets the source_db_type of this SqlConvertReq.

        源数据库类型。

        :return: The source_db_type of this SqlConvertReq.
        :rtype: str
        """
        return self._source_db_type

    @source_db_type.setter
    def source_db_type(self, source_db_type):
        """Sets the source_db_type of this SqlConvertReq.

        源数据库类型。

        :param source_db_type: The source_db_type of this SqlConvertReq.
        :type source_db_type: str
        """
        self._source_db_type = source_db_type

    @property
    def target_db_type(self):
        """Gets the target_db_type of this SqlConvertReq.

        目标数据库类型。其中GaussDB Centralized已弃用。

        :return: The target_db_type of this SqlConvertReq.
        :rtype: str
        """
        return self._target_db_type

    @target_db_type.setter
    def target_db_type(self, target_db_type):
        """Sets the target_db_type of this SqlConvertReq.

        目标数据库类型。其中GaussDB Centralized已弃用。

        :param target_db_type: The target_db_type of this SqlConvertReq.
        :type target_db_type: str
        """
        self._target_db_type = target_db_type

    @property
    def target_db_version(self):
        """Gets the target_db_version of this SqlConvertReq.

        目标数据库版本。 （注意：该字段需要与 target_db_type 字段组合成有效的目标数据库类型与版本，当前支持以下组合： GaussDB Centralized-2.0（已弃用）； GaussDB Primary/Standby-2.0； RDS for PostgreSQL-11； RDS for PostgreSQL-Enhanced Edition； RDS for MySQL-5.7; GaussDB(for MySQL) 8.0。)

        :return: The target_db_version of this SqlConvertReq.
        :rtype: str
        """
        return self._target_db_version

    @target_db_version.setter
    def target_db_version(self, target_db_version):
        """Sets the target_db_version of this SqlConvertReq.

        目标数据库版本。 （注意：该字段需要与 target_db_type 字段组合成有效的目标数据库类型与版本，当前支持以下组合： GaussDB Centralized-2.0（已弃用）； GaussDB Primary/Standby-2.0； RDS for PostgreSQL-11； RDS for PostgreSQL-Enhanced Edition； RDS for MySQL-5.7; GaussDB(for MySQL) 8.0。)

        :param target_db_version: The target_db_version of this SqlConvertReq.
        :type target_db_version: str
        """
        self._target_db_version = target_db_version

    @property
    def sql_statement(self):
        """Gets the sql_statement of this SqlConvertReq.

        需要转换的SQL语句。

        :return: The sql_statement of this SqlConvertReq.
        :rtype: str
        """
        return self._sql_statement

    @sql_statement.setter
    def sql_statement(self, sql_statement):
        """Sets the sql_statement of this SqlConvertReq.

        需要转换的SQL语句。

        :param sql_statement: The sql_statement of this SqlConvertReq.
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
        if not isinstance(other, SqlConvertReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
