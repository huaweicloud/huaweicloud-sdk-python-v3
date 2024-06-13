# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkSqlParameter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_body': 'str',
        'dependency_jars': 'str'
    }

    attribute_map = {
        'sql_body': 'sql_body',
        'dependency_jars': 'dependency_jars'
    }

    def __init__(self, sql_body=None, dependency_jars=None):
        """FlinkSqlParameter

        The model defined in huaweicloud sdk

        :param sql_body: Flink SQL 语句。长度限制：1048576个字符。
        :type sql_body: str
        :param dependency_jars: Flink SQL 作业依赖的 Jar 包所在的 OBS 路径。
        :type dependency_jars: str
        """
        
        

        self._sql_body = None
        self._dependency_jars = None
        self.discriminator = None

        if sql_body is not None:
            self.sql_body = sql_body
        if dependency_jars is not None:
            self.dependency_jars = dependency_jars

    @property
    def sql_body(self):
        """Gets the sql_body of this FlinkSqlParameter.

        Flink SQL 语句。长度限制：1048576个字符。

        :return: The sql_body of this FlinkSqlParameter.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        """Sets the sql_body of this FlinkSqlParameter.

        Flink SQL 语句。长度限制：1048576个字符。

        :param sql_body: The sql_body of this FlinkSqlParameter.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def dependency_jars(self):
        """Gets the dependency_jars of this FlinkSqlParameter.

        Flink SQL 作业依赖的 Jar 包所在的 OBS 路径。

        :return: The dependency_jars of this FlinkSqlParameter.
        :rtype: str
        """
        return self._dependency_jars

    @dependency_jars.setter
    def dependency_jars(self, dependency_jars):
        """Sets the dependency_jars of this FlinkSqlParameter.

        Flink SQL 作业依赖的 Jar 包所在的 OBS 路径。

        :param dependency_jars: The dependency_jars of this FlinkSqlParameter.
        :type dependency_jars: str
        """
        self._dependency_jars = dependency_jars

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
        if not isinstance(other, FlinkSqlParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
