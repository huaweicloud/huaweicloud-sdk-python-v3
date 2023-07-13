# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataTransformationObjectVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'data_transformation_type': 'str',
        'db_name': 'str',
        'schema_name': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'data_transformation_type': 'data_transformation_type',
        'db_name': 'db_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name'
    }

    def __init__(self, id=None, data_transformation_type=None, db_name=None, schema_name=None, table_name=None):
        """DataTransformationObjectVO

        The model defined in huaweicloud sdk

        :param id: 数据库对象、数据库表名称和过滤类型名称，例如格式为db1-*-*-tb1-*-*---conditionFilter--。
        :type id: str
        :param data_transformation_type: contentConditionalFilter：普通行过滤配置； configConditionalFilter：高级行过滤配置。
        :type data_transformation_type: str
        :param db_name: 库名称。
        :type db_name: str
        :param schema_name: schema名称。
        :type schema_name: str
        :param table_name: 表名称。
        :type table_name: str
        """
        
        

        self._id = None
        self._data_transformation_type = None
        self._db_name = None
        self._schema_name = None
        self._table_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if data_transformation_type is not None:
            self.data_transformation_type = data_transformation_type
        if db_name is not None:
            self.db_name = db_name
        if schema_name is not None:
            self.schema_name = schema_name
        if table_name is not None:
            self.table_name = table_name

    @property
    def id(self):
        """Gets the id of this DataTransformationObjectVO.

        数据库对象、数据库表名称和过滤类型名称，例如格式为db1-*-*-tb1-*-*---conditionFilter--。

        :return: The id of this DataTransformationObjectVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataTransformationObjectVO.

        数据库对象、数据库表名称和过滤类型名称，例如格式为db1-*-*-tb1-*-*---conditionFilter--。

        :param id: The id of this DataTransformationObjectVO.
        :type id: str
        """
        self._id = id

    @property
    def data_transformation_type(self):
        """Gets the data_transformation_type of this DataTransformationObjectVO.

        contentConditionalFilter：普通行过滤配置； configConditionalFilter：高级行过滤配置。

        :return: The data_transformation_type of this DataTransformationObjectVO.
        :rtype: str
        """
        return self._data_transformation_type

    @data_transformation_type.setter
    def data_transformation_type(self, data_transformation_type):
        """Sets the data_transformation_type of this DataTransformationObjectVO.

        contentConditionalFilter：普通行过滤配置； configConditionalFilter：高级行过滤配置。

        :param data_transformation_type: The data_transformation_type of this DataTransformationObjectVO.
        :type data_transformation_type: str
        """
        self._data_transformation_type = data_transformation_type

    @property
    def db_name(self):
        """Gets the db_name of this DataTransformationObjectVO.

        库名称。

        :return: The db_name of this DataTransformationObjectVO.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this DataTransformationObjectVO.

        库名称。

        :param db_name: The db_name of this DataTransformationObjectVO.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def schema_name(self):
        """Gets the schema_name of this DataTransformationObjectVO.

        schema名称。

        :return: The schema_name of this DataTransformationObjectVO.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this DataTransformationObjectVO.

        schema名称。

        :param schema_name: The schema_name of this DataTransformationObjectVO.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        """Gets the table_name of this DataTransformationObjectVO.

        表名称。

        :return: The table_name of this DataTransformationObjectVO.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this DataTransformationObjectVO.

        表名称。

        :param table_name: The table_name of this DataTransformationObjectVO.
        :type table_name: str
        """
        self._table_name = table_name

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
        if not isinstance(other, DataTransformationObjectVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
