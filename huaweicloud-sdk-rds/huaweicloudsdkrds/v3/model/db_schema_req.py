# coding: utf-8

import pprint
import re

import six





class DbSchemaReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'db_name': 'str',
        'schemas': 'list[SchemaReq]'
    }

    attribute_map = {
        'db_name': 'db_name',
        'schemas': 'schemas'
    }

    def __init__(self, db_name=None, schemas=None):
        """DbSchemaReq - a model defined in huaweicloud sdk"""
        
        

        self._db_name = None
        self._schemas = None
        self.discriminator = None

        self.db_name = db_name
        if schemas is not None:
            self.schemas = schemas

    @property
    def db_name(self):
        """Gets the db_name of this DbSchemaReq.

        数据库名称。 数据库名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和RDS for PostgreSQL模板库重名。 RDS for PostgreSQL模板库包括postgres， template0 ，template1。

        :return: The db_name of this DbSchemaReq.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DbSchemaReq.

        数据库名称。 数据库名称在1到63个字符之间，由字母、数字、或下划线组成，不能包含其他特殊字符，不能以“pg”和数字开头，且不能和RDS for PostgreSQL模板库重名。 RDS for PostgreSQL模板库包括postgres， template0 ，template1。

        :param db_name: The db_name of this DbSchemaReq.
        :type: str
        """
        self._db_name = db_name

    @property
    def schemas(self):
        """Gets the schemas of this DbSchemaReq.


        :return: The schemas of this DbSchemaReq.
        :rtype: list[SchemaReq]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """Sets the schemas of this DbSchemaReq.


        :param schemas: The schemas of this DbSchemaReq.
        :type: list[SchemaReq]
        """
        self._schemas = schemas

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DbSchemaReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
