# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterRedistributionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'db_name': 'str',
        'table_name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'limit': 'limit',
        'offset': 'offset',
        'db_name': 'db_name',
        'table_name': 'table_name',
        'type': 'type'
    }

    def __init__(self, cluster_id=None, limit=None, offset=None, db_name=None, table_name=None, type=None):
        """ShowClusterRedistributionRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param limit: 分页查询，每页大小
        :type limit: int
        :param offset: 分页查询，偏移
        :type offset: int
        :param db_name: 数据库名称
        :type db_name: str
        :param table_name: 表名称
        :type table_name: str
        :param type: 类型
        :type type: str
        """
        
        

        self._cluster_id = None
        self._limit = None
        self._offset = None
        self._db_name = None
        self._table_name = None
        self._type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if db_name is not None:
            self.db_name = db_name
        if table_name is not None:
            self.table_name = table_name
        if type is not None:
            self.type = type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowClusterRedistributionRequest.

        集群ID

        :return: The cluster_id of this ShowClusterRedistributionRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowClusterRedistributionRequest.

        集群ID

        :param cluster_id: The cluster_id of this ShowClusterRedistributionRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def limit(self):
        """Gets the limit of this ShowClusterRedistributionRequest.

        分页查询，每页大小

        :return: The limit of this ShowClusterRedistributionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowClusterRedistributionRequest.

        分页查询，每页大小

        :param limit: The limit of this ShowClusterRedistributionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowClusterRedistributionRequest.

        分页查询，偏移

        :return: The offset of this ShowClusterRedistributionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowClusterRedistributionRequest.

        分页查询，偏移

        :param offset: The offset of this ShowClusterRedistributionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def db_name(self):
        """Gets the db_name of this ShowClusterRedistributionRequest.

        数据库名称

        :return: The db_name of this ShowClusterRedistributionRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this ShowClusterRedistributionRequest.

        数据库名称

        :param db_name: The db_name of this ShowClusterRedistributionRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def table_name(self):
        """Gets the table_name of this ShowClusterRedistributionRequest.

        表名称

        :return: The table_name of this ShowClusterRedistributionRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ShowClusterRedistributionRequest.

        表名称

        :param table_name: The table_name of this ShowClusterRedistributionRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def type(self):
        """Gets the type of this ShowClusterRedistributionRequest.

        类型

        :return: The type of this ShowClusterRedistributionRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowClusterRedistributionRequest.

        类型

        :param type: The type of this ShowClusterRedistributionRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ShowClusterRedistributionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
