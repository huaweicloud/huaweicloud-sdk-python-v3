# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityListUserTableListTableList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datasource_type': 'str',
        'cluster_id': 'str',
        'database_name': 'str',
        'schema_name': 'str',
        'table_name': 'str'
    }

    attribute_map = {
        'datasource_type': 'datasource_type',
        'cluster_id': 'cluster_id',
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'table_name': 'table_name'
    }

    def __init__(self, datasource_type=None, cluster_id=None, database_name=None, schema_name=None, table_name=None):
        r"""SecurityListUserTableListTableList

        The model defined in huaweicloud sdk

        :param datasource_type: 必填，数据源类型，枚举：HIVE[、DLI](tag:nohcs)、DWS
        :type datasource_type: str
        :param cluster_id: 数据源集群id ，Mrs和dws数据源必填[，dli数据源可不传](tag:nohcs)
        :type cluster_id: str
        :param database_name: 必填，数据库名称
        :type database_name: str
        :param schema_name: Mrs[、dli数据源](tag:nohcs)非必填，dws数据源必填，dws数据源Schema名称
        :type schema_name: str
        :param table_name: 必填，表名称
        :type table_name: str
        """
        
        

        self._datasource_type = None
        self._cluster_id = None
        self._database_name = None
        self._schema_name = None
        self._table_name = None
        self.discriminator = None

        self.datasource_type = datasource_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        self.table_name = table_name

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this SecurityListUserTableListTableList.

        必填，数据源类型，枚举：HIVE[、DLI](tag:nohcs)、DWS

        :return: The datasource_type of this SecurityListUserTableListTableList.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this SecurityListUserTableListTableList.

        必填，数据源类型，枚举：HIVE[、DLI](tag:nohcs)、DWS

        :param datasource_type: The datasource_type of this SecurityListUserTableListTableList.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this SecurityListUserTableListTableList.

        数据源集群id ，Mrs和dws数据源必填[，dli数据源可不传](tag:nohcs)

        :return: The cluster_id of this SecurityListUserTableListTableList.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this SecurityListUserTableListTableList.

        数据源集群id ，Mrs和dws数据源必填[，dli数据源可不传](tag:nohcs)

        :param cluster_id: The cluster_id of this SecurityListUserTableListTableList.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def database_name(self):
        r"""Gets the database_name of this SecurityListUserTableListTableList.

        必填，数据库名称

        :return: The database_name of this SecurityListUserTableListTableList.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this SecurityListUserTableListTableList.

        必填，数据库名称

        :param database_name: The database_name of this SecurityListUserTableListTableList.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        r"""Gets the schema_name of this SecurityListUserTableListTableList.

        Mrs[、dli数据源](tag:nohcs)非必填，dws数据源必填，dws数据源Schema名称

        :return: The schema_name of this SecurityListUserTableListTableList.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        r"""Sets the schema_name of this SecurityListUserTableListTableList.

        Mrs[、dli数据源](tag:nohcs)非必填，dws数据源必填，dws数据源Schema名称

        :param schema_name: The schema_name of this SecurityListUserTableListTableList.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def table_name(self):
        r"""Gets the table_name of this SecurityListUserTableListTableList.

        必填，表名称

        :return: The table_name of this SecurityListUserTableListTableList.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this SecurityListUserTableListTableList.

        必填，表名称

        :param table_name: The table_name of this SecurityListUserTableListTableList.
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
        if not isinstance(other, SecurityListUserTableListTableList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
