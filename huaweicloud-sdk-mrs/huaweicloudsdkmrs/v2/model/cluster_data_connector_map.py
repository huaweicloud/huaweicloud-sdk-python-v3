# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterDataConnectorMap:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'map_id': 'int',
        'connector_id': 'str',
        'component_name': 'str',
        'role_type': 'str',
        'source_type': 'str',
        'cluster_id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'map_id': 'map_id',
        'connector_id': 'connector_id',
        'component_name': 'component_name',
        'role_type': 'role_type',
        'source_type': 'source_type',
        'cluster_id': 'cluster_id',
        'status': 'status'
    }

    def __init__(self, map_id=None, connector_id=None, component_name=None, role_type=None, source_type=None, cluster_id=None, status=None):
        """ClusterDataConnectorMap

        The model defined in huaweicloud sdk

        :param map_id: 数据连接关联ID值
        :type map_id: int
        :param connector_id: 数据连接ID值
        :type connector_id: str
        :param component_name: 组件名
        :type component_name: str
        :param role_type: 组件角色类型。 - hive_metastore：Hive Metastore角色 - hive_data：Hive角色 - hbase_data：Hbase角色 - ranger_data：Ranger角色
        :type role_type: str
        :param source_type: 数据连接类型。 - LOCAL_DB：本地元数据 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)
        :type source_type: str
        :param cluster_id: 关联集群id
        :type cluster_id: str
        :param status: 数据连接状态。 - 0：代表正常状态 - 1：代表使用中
        :type status: int
        """
        
        

        self._map_id = None
        self._connector_id = None
        self._component_name = None
        self._role_type = None
        self._source_type = None
        self._cluster_id = None
        self._status = None
        self.discriminator = None

        if map_id is not None:
            self.map_id = map_id
        if connector_id is not None:
            self.connector_id = connector_id
        if component_name is not None:
            self.component_name = component_name
        if role_type is not None:
            self.role_type = role_type
        if source_type is not None:
            self.source_type = source_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if status is not None:
            self.status = status

    @property
    def map_id(self):
        """Gets the map_id of this ClusterDataConnectorMap.

        数据连接关联ID值

        :return: The map_id of this ClusterDataConnectorMap.
        :rtype: int
        """
        return self._map_id

    @map_id.setter
    def map_id(self, map_id):
        """Sets the map_id of this ClusterDataConnectorMap.

        数据连接关联ID值

        :param map_id: The map_id of this ClusterDataConnectorMap.
        :type map_id: int
        """
        self._map_id = map_id

    @property
    def connector_id(self):
        """Gets the connector_id of this ClusterDataConnectorMap.

        数据连接ID值

        :return: The connector_id of this ClusterDataConnectorMap.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this ClusterDataConnectorMap.

        数据连接ID值

        :param connector_id: The connector_id of this ClusterDataConnectorMap.
        :type connector_id: str
        """
        self._connector_id = connector_id

    @property
    def component_name(self):
        """Gets the component_name of this ClusterDataConnectorMap.

        组件名

        :return: The component_name of this ClusterDataConnectorMap.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this ClusterDataConnectorMap.

        组件名

        :param component_name: The component_name of this ClusterDataConnectorMap.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def role_type(self):
        """Gets the role_type of this ClusterDataConnectorMap.

        组件角色类型。 - hive_metastore：Hive Metastore角色 - hive_data：Hive角色 - hbase_data：Hbase角色 - ranger_data：Ranger角色

        :return: The role_type of this ClusterDataConnectorMap.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        """Sets the role_type of this ClusterDataConnectorMap.

        组件角色类型。 - hive_metastore：Hive Metastore角色 - hive_data：Hive角色 - hbase_data：Hbase角色 - ranger_data：Ranger角色

        :param role_type: The role_type of this ClusterDataConnectorMap.
        :type role_type: str
        """
        self._role_type = role_type

    @property
    def source_type(self):
        """Gets the source_type of this ClusterDataConnectorMap.

        数据连接类型。 - LOCAL_DB：本地元数据 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)

        :return: The source_type of this ClusterDataConnectorMap.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ClusterDataConnectorMap.

        数据连接类型。 - LOCAL_DB：本地元数据 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)

        :param source_type: The source_type of this ClusterDataConnectorMap.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ClusterDataConnectorMap.

        关联集群id

        :return: The cluster_id of this ClusterDataConnectorMap.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ClusterDataConnectorMap.

        关联集群id

        :param cluster_id: The cluster_id of this ClusterDataConnectorMap.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def status(self):
        """Gets the status of this ClusterDataConnectorMap.

        数据连接状态。 - 0：代表正常状态 - 1：代表使用中

        :return: The status of this ClusterDataConnectorMap.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterDataConnectorMap.

        数据连接状态。 - 0：代表正常状态 - 1：代表使用中

        :param status: The status of this ClusterDataConnectorMap.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, ClusterDataConnectorMap):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
