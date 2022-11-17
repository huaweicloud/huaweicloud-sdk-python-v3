# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlJobQueryDataset:

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
        'schema': 'list[object]',
        'rows': 'list[object]'
    }

    attribute_map = {
        'sql_type': 'sql_type',
        'schema': 'schema',
        'rows': 'rows'
    }

    def __init__(self, sql_type=None, schema=None, rows=None):
        """SqlJobQueryDataset

        The model defined in huaweicloud sdk

        :param sql_type: 作业类型。DDL, DCL, IMPORT, EXPORT, QUERY, INSERT.
        :type sql_type: str
        :param schema: 当语句类型为DDL时，返回其结果的列名称及类型。
        :type schema: list[object]
        :param rows: 当语句类型为DDL时，直接返回其执行结果。
        :type rows: list[object]
        """
        
        

        self._sql_type = None
        self._schema = None
        self._rows = None
        self.discriminator = None

        self.sql_type = sql_type
        if schema is not None:
            self.schema = schema
        if rows is not None:
            self.rows = rows

    @property
    def sql_type(self):
        """Gets the sql_type of this SqlJobQueryDataset.

        作业类型。DDL, DCL, IMPORT, EXPORT, QUERY, INSERT.

        :return: The sql_type of this SqlJobQueryDataset.
        :rtype: str
        """
        return self._sql_type

    @sql_type.setter
    def sql_type(self, sql_type):
        """Sets the sql_type of this SqlJobQueryDataset.

        作业类型。DDL, DCL, IMPORT, EXPORT, QUERY, INSERT.

        :param sql_type: The sql_type of this SqlJobQueryDataset.
        :type sql_type: str
        """
        self._sql_type = sql_type

    @property
    def schema(self):
        """Gets the schema of this SqlJobQueryDataset.

        当语句类型为DDL时，返回其结果的列名称及类型。

        :return: The schema of this SqlJobQueryDataset.
        :rtype: list[object]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this SqlJobQueryDataset.

        当语句类型为DDL时，返回其结果的列名称及类型。

        :param schema: The schema of this SqlJobQueryDataset.
        :type schema: list[object]
        """
        self._schema = schema

    @property
    def rows(self):
        """Gets the rows of this SqlJobQueryDataset.

        当语句类型为DDL时，直接返回其执行结果。

        :return: The rows of this SqlJobQueryDataset.
        :rtype: list[object]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this SqlJobQueryDataset.

        当语句类型为DDL时，直接返回其执行结果。

        :param rows: The rows of this SqlJobQueryDataset.
        :type rows: list[object]
        """
        self._rows = rows

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
        if not isinstance(other, SqlJobQueryDataset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
