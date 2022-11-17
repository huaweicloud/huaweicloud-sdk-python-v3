# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatasourceTablesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'datasource_id': 'str',
        'position': 'str',
        'db_name': 'str',
        'db_schema': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'datasource_id': 'datasource_id',
        'position': 'position',
        'db_name': 'db_name',
        'db_schema': 'db_schema',
        'filter': 'filter'
    }

    def __init__(self, instance_id=None, datasource_id=None, position=None, db_name=None, db_schema=None, filter=None):
        """ListDatasourceTablesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param datasource_id: 数据源ID
        :type datasource_id: str
        :param position: 数据源所在任务位置 - SOURCE 数据源处于任务源端 - TARGET 数据源处于任务目标端
        :type position: str
        :param db_name: 数据库名称，只支持MRSHIVE，FIHIVE类型的数据源
        :type db_name: str
        :param db_schema: 数据库模式,GAUSS100数据库使用
        :type db_schema: str
        :param filter: 表名模糊匹配过滤器
        :type filter: str
        """
        
        

        self._instance_id = None
        self._datasource_id = None
        self._position = None
        self._db_name = None
        self._db_schema = None
        self._filter = None
        self.discriminator = None

        self.instance_id = instance_id
        self.datasource_id = datasource_id
        self.position = position
        if db_name is not None:
            self.db_name = db_name
        if db_schema is not None:
            self.db_schema = db_schema
        if filter is not None:
            self.filter = filter

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDatasourceTablesRequest.

        实例ID

        :return: The instance_id of this ListDatasourceTablesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDatasourceTablesRequest.

        实例ID

        :param instance_id: The instance_id of this ListDatasourceTablesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def datasource_id(self):
        """Gets the datasource_id of this ListDatasourceTablesRequest.

        数据源ID

        :return: The datasource_id of this ListDatasourceTablesRequest.
        :rtype: str
        """
        return self._datasource_id

    @datasource_id.setter
    def datasource_id(self, datasource_id):
        """Sets the datasource_id of this ListDatasourceTablesRequest.

        数据源ID

        :param datasource_id: The datasource_id of this ListDatasourceTablesRequest.
        :type datasource_id: str
        """
        self._datasource_id = datasource_id

    @property
    def position(self):
        """Gets the position of this ListDatasourceTablesRequest.

        数据源所在任务位置 - SOURCE 数据源处于任务源端 - TARGET 数据源处于任务目标端

        :return: The position of this ListDatasourceTablesRequest.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this ListDatasourceTablesRequest.

        数据源所在任务位置 - SOURCE 数据源处于任务源端 - TARGET 数据源处于任务目标端

        :param position: The position of this ListDatasourceTablesRequest.
        :type position: str
        """
        self._position = position

    @property
    def db_name(self):
        """Gets the db_name of this ListDatasourceTablesRequest.

        数据库名称，只支持MRSHIVE，FIHIVE类型的数据源

        :return: The db_name of this ListDatasourceTablesRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this ListDatasourceTablesRequest.

        数据库名称，只支持MRSHIVE，FIHIVE类型的数据源

        :param db_name: The db_name of this ListDatasourceTablesRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def db_schema(self):
        """Gets the db_schema of this ListDatasourceTablesRequest.

        数据库模式,GAUSS100数据库使用

        :return: The db_schema of this ListDatasourceTablesRequest.
        :rtype: str
        """
        return self._db_schema

    @db_schema.setter
    def db_schema(self, db_schema):
        """Sets the db_schema of this ListDatasourceTablesRequest.

        数据库模式,GAUSS100数据库使用

        :param db_schema: The db_schema of this ListDatasourceTablesRequest.
        :type db_schema: str
        """
        self._db_schema = db_schema

    @property
    def filter(self):
        """Gets the filter of this ListDatasourceTablesRequest.

        表名模糊匹配过滤器

        :return: The filter of this ListDatasourceTablesRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this ListDatasourceTablesRequest.

        表名模糊匹配过滤器

        :param filter: The filter of this ListDatasourceTablesRequest.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, ListDatasourceTablesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
