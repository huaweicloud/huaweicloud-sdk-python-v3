# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostgreSQLRestoreSchema:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema': 'str',
        'tables': 'list[PostgreSQLRestoreTable]'
    }

    attribute_map = {
        'schema': 'schema',
        'tables': 'tables'
    }

    def __init__(self, schema=None, tables=None):
        r"""PostgreSQLRestoreSchema

        The model defined in huaweicloud sdk

        :param schema: 模式信息
        :type schema: str
        :param tables: 表信息
        :type tables: list[:class:`huaweicloudsdkrds.v3.PostgreSQLRestoreTable`]
        """
        
        

        self._schema = None
        self._tables = None
        self.discriminator = None

        if schema is not None:
            self.schema = schema
        if tables is not None:
            self.tables = tables

    @property
    def schema(self):
        r"""Gets the schema of this PostgreSQLRestoreSchema.

        模式信息

        :return: The schema of this PostgreSQLRestoreSchema.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this PostgreSQLRestoreSchema.

        模式信息

        :param schema: The schema of this PostgreSQLRestoreSchema.
        :type schema: str
        """
        self._schema = schema

    @property
    def tables(self):
        r"""Gets the tables of this PostgreSQLRestoreSchema.

        表信息

        :return: The tables of this PostgreSQLRestoreSchema.
        :rtype: list[:class:`huaweicloudsdkrds.v3.PostgreSQLRestoreTable`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this PostgreSQLRestoreSchema.

        表信息

        :param tables: The tables of this PostgreSQLRestoreSchema.
        :type tables: list[:class:`huaweicloudsdkrds.v3.PostgreSQLRestoreTable`]
        """
        self._tables = tables

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
        if not isinstance(other, PostgreSQLRestoreSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
