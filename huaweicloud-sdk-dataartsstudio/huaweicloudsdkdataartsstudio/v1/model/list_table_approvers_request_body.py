# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTableApproversRequestBody:

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
        'datasource_type': 'str',
        'cluster_id': 'str',
        'schema_name': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'expire_time': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'datasource_type': 'datasource_type',
        'cluster_id': 'cluster_id',
        'schema_name': 'schema_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'expire_time': 'expire_time'
    }

    def __init__(self, instance_id=None, datasource_type=None, cluster_id=None, schema_name=None, database_name=None, table_name=None, expire_time=None):
        r"""ListTableApproversRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: 实例id
        :type instance_id: str
        :param datasource_type: 数据源类型,hive,dws,dli
        :type datasource_type: str
        :param cluster_id: 集群id,dli传DLI，dws和mrs-hive传对应的集群id
        :type cluster_id: str
        :param schema_name: schema名称，dws需要传这个字段
        :type schema_name: str
        :param database_name: 数据库名称
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param expire_time: 权限到期时间时间戳，毫秒。
        :type expire_time: int
        """
        
        

        self._instance_id = None
        self._datasource_type = None
        self._cluster_id = None
        self._schema_name = None
        self._database_name = None
        self._table_name = None
        self._expire_time = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if schema_name is not None:
            self.schema_name = schema_name
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListTableApproversRequestBody.

        实例id

        :return: The instance_id of this ListTableApproversRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListTableApproversRequestBody.

        实例id

        :param instance_id: The instance_id of this ListTableApproversRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this ListTableApproversRequestBody.

        数据源类型,hive,dws,dli

        :return: The datasource_type of this ListTableApproversRequestBody.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this ListTableApproversRequestBody.

        数据源类型,hive,dws,dli

        :param datasource_type: The datasource_type of this ListTableApproversRequestBody.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListTableApproversRequestBody.

        集群id,dli传DLI，dws和mrs-hive传对应的集群id

        :return: The cluster_id of this ListTableApproversRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListTableApproversRequestBody.

        集群id,dli传DLI，dws和mrs-hive传对应的集群id

        :param cluster_id: The cluster_id of this ListTableApproversRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def schema_name(self):
        r"""Gets the schema_name of this ListTableApproversRequestBody.

        schema名称，dws需要传这个字段

        :return: The schema_name of this ListTableApproversRequestBody.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this ListTableApproversRequestBody.

        schema名称，dws需要传这个字段

        :param schema_name: The schema_name of this ListTableApproversRequestBody.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListTableApproversRequestBody.

        数据库名称

        :return: The database_name of this ListTableApproversRequestBody.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListTableApproversRequestBody.

        数据库名称

        :param database_name: The database_name of this ListTableApproversRequestBody.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListTableApproversRequestBody.

        表名称

        :return: The table_name of this ListTableApproversRequestBody.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListTableApproversRequestBody.

        表名称

        :param table_name: The table_name of this ListTableApproversRequestBody.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def expire_time(self):
        r"""Gets the expire_time of this ListTableApproversRequestBody.

        权限到期时间时间戳，毫秒。

        :return: The expire_time of this ListTableApproversRequestBody.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this ListTableApproversRequestBody.

        权限到期时间时间戳，毫秒。

        :param expire_time: The expire_time of this ListTableApproversRequestBody.
        :type expire_time: int
        """
        self._expire_time = expire_time

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
        if not isinstance(other, ListTableApproversRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
