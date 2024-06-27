# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseEndpoint:

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
        'endpoint_name': 'str',
        'ip': 'str',
        'db_port': 'str',
        'db_user': 'str',
        'db_password': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'db_name': 'str',
        'source_sharding': 'list[BaseEndpoint]'
    }

    attribute_map = {
        'id': 'id',
        'endpoint_name': 'endpoint_name',
        'ip': 'ip',
        'db_port': 'db_port',
        'db_user': 'db_user',
        'db_password': 'db_password',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'db_name': 'db_name',
        'source_sharding': 'source_sharding'
    }

    def __init__(self, id=None, endpoint_name=None, ip=None, db_port=None, db_user=None, db_password=None, instance_id=None, instance_name=None, db_name=None, source_sharding=None):
        """BaseEndpoint

        The model defined in huaweicloud sdk

        :param id: 数据库信息ID。
        :type id: str
        :param endpoint_name: 数据库场景类型。取值： - oracle：云下自建Oracle数据库。 - ecs_oracle：华为云ECS自建Oracle数据库。 - cloud_gaussdbv5：华为云数据库GaussDB分布式。 - mysql：他云/本地自建MySQL数据库。 - ecs_mysql：华为云ECS自建MySQL数据库。 - cloud_mysql：华为云数据库RDS for MySQL。 - redis：云下自建Redis数据。 - ecs_redis：华为云ECS自建Redis数据。 - rediscluster：云下自建Redis集群数据库。 - ecs_rediscluster：华为云ECS自建Redis集群数据库。 - cloud_gaussdb_redis：华为云数据库GeminiDB Redis。 - postgresql: 云下自建PostgreSQL数据库。 - ecs_postgresql: 华为云ECS自建PostgreSQL数据库。 - cloud_postgresql: 华为云数据库RDS for PostgreSQL。 - mongodb: 云下自建MongoDB数据库。 - ecs_mongodb: 华为云ECS自建MongoDB数据库。 - cloud_mongodb: 华为云文档数据库服务DDS。
        :type endpoint_name: str
        :param ip: 数据库IP。 约束： - 数据库为自建MongoDB时，数据库IP与端口之间用“:”英文冒号拼接，多个值之间请用“,”英文逗号隔开，最多支持填写3个IP地址或域名。 - 数据库为DDS实例时，数据库IP与端口之间用“:”英文冒号拼接，多个IP端口之间请用“,”英文逗号分隔。 - 数据库为Redis集群时，请填写源端Redis集群所有分片的IP地址和对应端口，数据库IP与端口之间用“:”英文冒号拼接，多个IP端口之间请用“,”英文逗号分隔，并且推荐填写集群分片的Slave节点的IP地址。最多支持填写32个IP地址或域名，多个值之间请用英文逗号隔开。 示例： - MySQL：ip - MongoDB：ip:port,ip:port,ip:port - DDS：ip:port,ip:port  - Redis集群：ip:port,ip:port
        :type ip: str
        :param db_port: 数据库端口。  约束：输入范围为1-65535之间的整数。
        :type db_port: str
        :param db_user: 数据库用户名。
        :type db_user: str
        :param db_password: 数据库密码。
        :type db_password: str
        :param instance_id: 华为云数据库实例ID。
        :type instance_id: str
        :param instance_name: 华为云数据库实例名称。
        :type instance_name: str
        :param db_name: 指定数据库名称。例如： - oracle：serviceName.orcl。
        :type db_name: str
        :param source_sharding: 物理源库信息。
        :type source_sharding: list[:class:`huaweicloudsdkdrs.v5.BaseEndpoint`]
        """
        
        

        self._id = None
        self._endpoint_name = None
        self._ip = None
        self._db_port = None
        self._db_user = None
        self._db_password = None
        self._instance_id = None
        self._instance_name = None
        self._db_name = None
        self._source_sharding = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.endpoint_name = endpoint_name
        if ip is not None:
            self.ip = ip
        if db_port is not None:
            self.db_port = db_port
        self.db_user = db_user
        self.db_password = db_password
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if db_name is not None:
            self.db_name = db_name
        if source_sharding is not None:
            self.source_sharding = source_sharding

    @property
    def id(self):
        """Gets the id of this BaseEndpoint.

        数据库信息ID。

        :return: The id of this BaseEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BaseEndpoint.

        数据库信息ID。

        :param id: The id of this BaseEndpoint.
        :type id: str
        """
        self._id = id

    @property
    def endpoint_name(self):
        """Gets the endpoint_name of this BaseEndpoint.

        数据库场景类型。取值： - oracle：云下自建Oracle数据库。 - ecs_oracle：华为云ECS自建Oracle数据库。 - cloud_gaussdbv5：华为云数据库GaussDB分布式。 - mysql：他云/本地自建MySQL数据库。 - ecs_mysql：华为云ECS自建MySQL数据库。 - cloud_mysql：华为云数据库RDS for MySQL。 - redis：云下自建Redis数据。 - ecs_redis：华为云ECS自建Redis数据。 - rediscluster：云下自建Redis集群数据库。 - ecs_rediscluster：华为云ECS自建Redis集群数据库。 - cloud_gaussdb_redis：华为云数据库GeminiDB Redis。 - postgresql: 云下自建PostgreSQL数据库。 - ecs_postgresql: 华为云ECS自建PostgreSQL数据库。 - cloud_postgresql: 华为云数据库RDS for PostgreSQL。 - mongodb: 云下自建MongoDB数据库。 - ecs_mongodb: 华为云ECS自建MongoDB数据库。 - cloud_mongodb: 华为云文档数据库服务DDS。

        :return: The endpoint_name of this BaseEndpoint.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """Sets the endpoint_name of this BaseEndpoint.

        数据库场景类型。取值： - oracle：云下自建Oracle数据库。 - ecs_oracle：华为云ECS自建Oracle数据库。 - cloud_gaussdbv5：华为云数据库GaussDB分布式。 - mysql：他云/本地自建MySQL数据库。 - ecs_mysql：华为云ECS自建MySQL数据库。 - cloud_mysql：华为云数据库RDS for MySQL。 - redis：云下自建Redis数据。 - ecs_redis：华为云ECS自建Redis数据。 - rediscluster：云下自建Redis集群数据库。 - ecs_rediscluster：华为云ECS自建Redis集群数据库。 - cloud_gaussdb_redis：华为云数据库GeminiDB Redis。 - postgresql: 云下自建PostgreSQL数据库。 - ecs_postgresql: 华为云ECS自建PostgreSQL数据库。 - cloud_postgresql: 华为云数据库RDS for PostgreSQL。 - mongodb: 云下自建MongoDB数据库。 - ecs_mongodb: 华为云ECS自建MongoDB数据库。 - cloud_mongodb: 华为云文档数据库服务DDS。

        :param endpoint_name: The endpoint_name of this BaseEndpoint.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def ip(self):
        """Gets the ip of this BaseEndpoint.

        数据库IP。 约束： - 数据库为自建MongoDB时，数据库IP与端口之间用“:”英文冒号拼接，多个值之间请用“,”英文逗号隔开，最多支持填写3个IP地址或域名。 - 数据库为DDS实例时，数据库IP与端口之间用“:”英文冒号拼接，多个IP端口之间请用“,”英文逗号分隔。 - 数据库为Redis集群时，请填写源端Redis集群所有分片的IP地址和对应端口，数据库IP与端口之间用“:”英文冒号拼接，多个IP端口之间请用“,”英文逗号分隔，并且推荐填写集群分片的Slave节点的IP地址。最多支持填写32个IP地址或域名，多个值之间请用英文逗号隔开。 示例： - MySQL：ip - MongoDB：ip:port,ip:port,ip:port - DDS：ip:port,ip:port  - Redis集群：ip:port,ip:port

        :return: The ip of this BaseEndpoint.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this BaseEndpoint.

        数据库IP。 约束： - 数据库为自建MongoDB时，数据库IP与端口之间用“:”英文冒号拼接，多个值之间请用“,”英文逗号隔开，最多支持填写3个IP地址或域名。 - 数据库为DDS实例时，数据库IP与端口之间用“:”英文冒号拼接，多个IP端口之间请用“,”英文逗号分隔。 - 数据库为Redis集群时，请填写源端Redis集群所有分片的IP地址和对应端口，数据库IP与端口之间用“:”英文冒号拼接，多个IP端口之间请用“,”英文逗号分隔，并且推荐填写集群分片的Slave节点的IP地址。最多支持填写32个IP地址或域名，多个值之间请用英文逗号隔开。 示例： - MySQL：ip - MongoDB：ip:port,ip:port,ip:port - DDS：ip:port,ip:port  - Redis集群：ip:port,ip:port

        :param ip: The ip of this BaseEndpoint.
        :type ip: str
        """
        self._ip = ip

    @property
    def db_port(self):
        """Gets the db_port of this BaseEndpoint.

        数据库端口。  约束：输入范围为1-65535之间的整数。

        :return: The db_port of this BaseEndpoint.
        :rtype: str
        """
        return self._db_port

    @db_port.setter
    def db_port(self, db_port):
        """Sets the db_port of this BaseEndpoint.

        数据库端口。  约束：输入范围为1-65535之间的整数。

        :param db_port: The db_port of this BaseEndpoint.
        :type db_port: str
        """
        self._db_port = db_port

    @property
    def db_user(self):
        """Gets the db_user of this BaseEndpoint.

        数据库用户名。

        :return: The db_user of this BaseEndpoint.
        :rtype: str
        """
        return self._db_user

    @db_user.setter
    def db_user(self, db_user):
        """Sets the db_user of this BaseEndpoint.

        数据库用户名。

        :param db_user: The db_user of this BaseEndpoint.
        :type db_user: str
        """
        self._db_user = db_user

    @property
    def db_password(self):
        """Gets the db_password of this BaseEndpoint.

        数据库密码。

        :return: The db_password of this BaseEndpoint.
        :rtype: str
        """
        return self._db_password

    @db_password.setter
    def db_password(self, db_password):
        """Sets the db_password of this BaseEndpoint.

        数据库密码。

        :param db_password: The db_password of this BaseEndpoint.
        :type db_password: str
        """
        self._db_password = db_password

    @property
    def instance_id(self):
        """Gets the instance_id of this BaseEndpoint.

        华为云数据库实例ID。

        :return: The instance_id of this BaseEndpoint.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BaseEndpoint.

        华为云数据库实例ID。

        :param instance_id: The instance_id of this BaseEndpoint.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this BaseEndpoint.

        华为云数据库实例名称。

        :return: The instance_name of this BaseEndpoint.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this BaseEndpoint.

        华为云数据库实例名称。

        :param instance_name: The instance_name of this BaseEndpoint.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def db_name(self):
        """Gets the db_name of this BaseEndpoint.

        指定数据库名称。例如： - oracle：serviceName.orcl。

        :return: The db_name of this BaseEndpoint.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this BaseEndpoint.

        指定数据库名称。例如： - oracle：serviceName.orcl。

        :param db_name: The db_name of this BaseEndpoint.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def source_sharding(self):
        """Gets the source_sharding of this BaseEndpoint.

        物理源库信息。

        :return: The source_sharding of this BaseEndpoint.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.BaseEndpoint`]
        """
        return self._source_sharding

    @source_sharding.setter
    def source_sharding(self, source_sharding):
        """Sets the source_sharding of this BaseEndpoint.

        物理源库信息。

        :param source_sharding: The source_sharding of this BaseEndpoint.
        :type source_sharding: list[:class:`huaweicloudsdkdrs.v5.BaseEndpoint`]
        """
        self._source_sharding = source_sharding

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
        if not isinstance(other, BaseEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
