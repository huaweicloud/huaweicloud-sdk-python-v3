# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataConnectorDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connector_name': 'str',
        'source_type': 'str',
        'source_info': 'str',
        'connector_id': 'str',
        'create_time': 'int',
        'last_update_time': 'int',
        'create_by': 'str',
        'create_user': 'str',
        'tenant_id': 'str',
        'last_update_by': 'str',
        'status': 'int',
        'used_clusters': 'str',
        'encrypt_type': 'int'
    }

    attribute_map = {
        'connector_name': 'connector_name',
        'source_type': 'source_type',
        'source_info': 'source_info',
        'connector_id': 'connector_id',
        'create_time': 'create_time',
        'last_update_time': 'last_update_time',
        'create_by': 'create_by',
        'create_user': 'create_user',
        'tenant_id': 'tenant_id',
        'last_update_by': 'last_update_by',
        'status': 'status',
        'used_clusters': 'used_clusters',
        'encrypt_type': 'encrypt_type'
    }

    def __init__(self, connector_name=None, source_type=None, source_info=None, connector_id=None, create_time=None, last_update_time=None, create_by=None, create_user=None, tenant_id=None, last_update_by=None, status=None, used_clusters=None, encrypt_type=None):
        """DataConnectorDetail

        The model defined in huaweicloud sdk

        :param connector_name: 数据连接名称。
        :type connector_name: str
        :param source_type: 数据连接类型。 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)
        :type source_type: str
        :param source_info: 数据源信息，为json格式，不同数据连接有不同的信息，各数据源的source_info请求内容可参见示例。
        :type source_info: str
        :param connector_id: 数据连接ID
        :type connector_id: str
        :param create_time: 创建时间
        :type create_time: int
        :param last_update_time: 最后更新时间
        :type last_update_time: int
        :param create_by: 创建时间
        :type create_by: str
        :param create_user: 创建用户
        :type create_user: str
        :param tenant_id: 租户ID
        :type tenant_id: str
        :param last_update_by: 最后更新时间
        :type last_update_by: str
        :param status: 数据连接状态
        :type status: int
        :param used_clusters: 使用集群
        :type used_clusters: str
        :param encrypt_type: 加密类型
        :type encrypt_type: int
        """
        
        

        self._connector_name = None
        self._source_type = None
        self._source_info = None
        self._connector_id = None
        self._create_time = None
        self._last_update_time = None
        self._create_by = None
        self._create_user = None
        self._tenant_id = None
        self._last_update_by = None
        self._status = None
        self._used_clusters = None
        self._encrypt_type = None
        self.discriminator = None

        self.connector_name = connector_name
        self.source_type = source_type
        self.source_info = source_info
        if connector_id is not None:
            self.connector_id = connector_id
        if create_time is not None:
            self.create_time = create_time
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if create_by is not None:
            self.create_by = create_by
        if create_user is not None:
            self.create_user = create_user
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if last_update_by is not None:
            self.last_update_by = last_update_by
        if status is not None:
            self.status = status
        if used_clusters is not None:
            self.used_clusters = used_clusters
        if encrypt_type is not None:
            self.encrypt_type = encrypt_type

    @property
    def connector_name(self):
        """Gets the connector_name of this DataConnectorDetail.

        数据连接名称。

        :return: The connector_name of this DataConnectorDetail.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        """Sets the connector_name of this DataConnectorDetail.

        数据连接名称。

        :param connector_name: The connector_name of this DataConnectorDetail.
        :type connector_name: str
        """
        self._connector_name = connector_name

    @property
    def source_type(self):
        """Gets the source_type of this DataConnectorDetail.

        数据连接类型。 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)

        :return: The source_type of this DataConnectorDetail.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DataConnectorDetail.

        数据连接类型。 - RDS_POSTGRES：RDS服务PostgreSQL数据库 - RDS_MYSQL：RDS服务MySQL数据库 - gaussdb-mysql：云数据库GaussDB(for MySQL)

        :param source_type: The source_type of this DataConnectorDetail.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_info(self):
        """Gets the source_info of this DataConnectorDetail.

        数据源信息，为json格式，不同数据连接有不同的信息，各数据源的source_info请求内容可参见示例。

        :return: The source_info of this DataConnectorDetail.
        :rtype: str
        """
        return self._source_info

    @source_info.setter
    def source_info(self, source_info):
        """Sets the source_info of this DataConnectorDetail.

        数据源信息，为json格式，不同数据连接有不同的信息，各数据源的source_info请求内容可参见示例。

        :param source_info: The source_info of this DataConnectorDetail.
        :type source_info: str
        """
        self._source_info = source_info

    @property
    def connector_id(self):
        """Gets the connector_id of this DataConnectorDetail.

        数据连接ID

        :return: The connector_id of this DataConnectorDetail.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this DataConnectorDetail.

        数据连接ID

        :param connector_id: The connector_id of this DataConnectorDetail.
        :type connector_id: str
        """
        self._connector_id = connector_id

    @property
    def create_time(self):
        """Gets the create_time of this DataConnectorDetail.

        创建时间

        :return: The create_time of this DataConnectorDetail.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataConnectorDetail.

        创建时间

        :param create_time: The create_time of this DataConnectorDetail.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def last_update_time(self):
        """Gets the last_update_time of this DataConnectorDetail.

        最后更新时间

        :return: The last_update_time of this DataConnectorDetail.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this DataConnectorDetail.

        最后更新时间

        :param last_update_time: The last_update_time of this DataConnectorDetail.
        :type last_update_time: int
        """
        self._last_update_time = last_update_time

    @property
    def create_by(self):
        """Gets the create_by of this DataConnectorDetail.

        创建时间

        :return: The create_by of this DataConnectorDetail.
        :rtype: str
        """
        return self._create_by

    @create_by.setter
    def create_by(self, create_by):
        """Sets the create_by of this DataConnectorDetail.

        创建时间

        :param create_by: The create_by of this DataConnectorDetail.
        :type create_by: str
        """
        self._create_by = create_by

    @property
    def create_user(self):
        """Gets the create_user of this DataConnectorDetail.

        创建用户

        :return: The create_user of this DataConnectorDetail.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this DataConnectorDetail.

        创建用户

        :param create_user: The create_user of this DataConnectorDetail.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def tenant_id(self):
        """Gets the tenant_id of this DataConnectorDetail.

        租户ID

        :return: The tenant_id of this DataConnectorDetail.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this DataConnectorDetail.

        租户ID

        :param tenant_id: The tenant_id of this DataConnectorDetail.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def last_update_by(self):
        """Gets the last_update_by of this DataConnectorDetail.

        最后更新时间

        :return: The last_update_by of this DataConnectorDetail.
        :rtype: str
        """
        return self._last_update_by

    @last_update_by.setter
    def last_update_by(self, last_update_by):
        """Sets the last_update_by of this DataConnectorDetail.

        最后更新时间

        :param last_update_by: The last_update_by of this DataConnectorDetail.
        :type last_update_by: str
        """
        self._last_update_by = last_update_by

    @property
    def status(self):
        """Gets the status of this DataConnectorDetail.

        数据连接状态

        :return: The status of this DataConnectorDetail.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DataConnectorDetail.

        数据连接状态

        :param status: The status of this DataConnectorDetail.
        :type status: int
        """
        self._status = status

    @property
    def used_clusters(self):
        """Gets the used_clusters of this DataConnectorDetail.

        使用集群

        :return: The used_clusters of this DataConnectorDetail.
        :rtype: str
        """
        return self._used_clusters

    @used_clusters.setter
    def used_clusters(self, used_clusters):
        """Sets the used_clusters of this DataConnectorDetail.

        使用集群

        :param used_clusters: The used_clusters of this DataConnectorDetail.
        :type used_clusters: str
        """
        self._used_clusters = used_clusters

    @property
    def encrypt_type(self):
        """Gets the encrypt_type of this DataConnectorDetail.

        加密类型

        :return: The encrypt_type of this DataConnectorDetail.
        :rtype: int
        """
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, encrypt_type):
        """Sets the encrypt_type of this DataConnectorDetail.

        加密类型

        :param encrypt_type: The encrypt_type of this DataConnectorDetail.
        :type encrypt_type: int
        """
        self._encrypt_type = encrypt_type

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
        if not isinstance(other, DataConnectorDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
