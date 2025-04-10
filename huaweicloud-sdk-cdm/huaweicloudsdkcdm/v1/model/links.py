# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Links:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'link_config_values': 'LinksLinkconfigvalues',
        'creation_user': 'str',
        'name': 'str',
        'id': 'int',
        'creation_date': 'int',
        'connector_name': 'str',
        'update_date': 'int',
        'enabled': 'bool',
        'update_user': 'str'
    }

    attribute_map = {
        'link_config_values': 'link-config-values',
        'creation_user': 'creation-user',
        'name': 'name',
        'id': 'id',
        'creation_date': 'creation-date',
        'connector_name': 'connector-name',
        'update_date': 'update-date',
        'enabled': 'enabled',
        'update_user': 'update-user'
    }

    def __init__(self, link_config_values=None, creation_user=None, name=None, id=None, creation_date=None, connector_name=None, update_date=None, enabled=None, update_user=None):
        r"""Links

        The model defined in huaweicloud sdk

        :param link_config_values: 
        :type link_config_values: :class:`huaweicloudsdkcdm.v1.LinksLinkconfigvalues`
        :param creation_user: 创建连接的用户
        :type creation_user: str
        :param name: 连接名称
        :type name: str
        :param id: 连接ID
        :type id: int
        :param creation_date: 创建连接的时间
        :type creation_date: int
        :param connector_name: 连接器名称，对应的连接参数如下：generic-jdbc-connector：关系数据库连接。obs-connector：OBS连接、阿里云OSS连接。hdfs-connector：HDFS连接。hbase-connector：HBase连接、CloudTable连接。hive-connector：Hive连接。ftp-connector/sftp-connector：FTP/SFTP连接。mongodb-connector：MongoDB连接。redis-connector：Redis/DCS连接。nas-connector：NAS/SFS连接。kafka-connector：Kafka连接。dis-connector：DIS连接。elasticsearch-connector：Elasticsearch/云搜索服务连接。dli-connector：DLI连接。opentsdb-connector：CloudTable OpenTSDB连接。http-connector：HTTP/HTTPS连接，该连接暂无连接参数。thirdparty-obs-connector：七牛云KODO/腾讯云COS连接、亚马逊对象存储连接。dms-kafka-connector：DMS Kafka连接
        :type connector_name: str
        :param update_date: 更新连接的时间
        :type update_date: int
        :param enabled: 是否激活连接，默认为“true”
        :type enabled: bool
        :param update_user: 更新连接的用户
        :type update_user: str
        """
        
        

        self._link_config_values = None
        self._creation_user = None
        self._name = None
        self._id = None
        self._creation_date = None
        self._connector_name = None
        self._update_date = None
        self._enabled = None
        self._update_user = None
        self.discriminator = None

        self.link_config_values = link_config_values
        if creation_user is not None:
            self.creation_user = creation_user
        self.name = name
        if id is not None:
            self.id = id
        if creation_date is not None:
            self.creation_date = creation_date
        self.connector_name = connector_name
        if update_date is not None:
            self.update_date = update_date
        if enabled is not None:
            self.enabled = enabled
        if update_user is not None:
            self.update_user = update_user

    @property
    def link_config_values(self):
        r"""Gets the link_config_values of this Links.

        :return: The link_config_values of this Links.
        :rtype: :class:`huaweicloudsdkcdm.v1.LinksLinkconfigvalues`
        """
        return self._link_config_values

    @link_config_values.setter
    def link_config_values(self, link_config_values):
        r"""Sets the link_config_values of this Links.

        :param link_config_values: The link_config_values of this Links.
        :type link_config_values: :class:`huaweicloudsdkcdm.v1.LinksLinkconfigvalues`
        """
        self._link_config_values = link_config_values

    @property
    def creation_user(self):
        r"""Gets the creation_user of this Links.

        创建连接的用户

        :return: The creation_user of this Links.
        :rtype: str
        """
        return self._creation_user

    @creation_user.setter
    def creation_user(self, creation_user):
        r"""Sets the creation_user of this Links.

        创建连接的用户

        :param creation_user: The creation_user of this Links.
        :type creation_user: str
        """
        self._creation_user = creation_user

    @property
    def name(self):
        r"""Gets the name of this Links.

        连接名称

        :return: The name of this Links.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Links.

        连接名称

        :param name: The name of this Links.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this Links.

        连接ID

        :return: The id of this Links.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Links.

        连接ID

        :param id: The id of this Links.
        :type id: int
        """
        self._id = id

    @property
    def creation_date(self):
        r"""Gets the creation_date of this Links.

        创建连接的时间

        :return: The creation_date of this Links.
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        r"""Sets the creation_date of this Links.

        创建连接的时间

        :param creation_date: The creation_date of this Links.
        :type creation_date: int
        """
        self._creation_date = creation_date

    @property
    def connector_name(self):
        r"""Gets the connector_name of this Links.

        连接器名称，对应的连接参数如下：generic-jdbc-connector：关系数据库连接。obs-connector：OBS连接、阿里云OSS连接。hdfs-connector：HDFS连接。hbase-connector：HBase连接、CloudTable连接。hive-connector：Hive连接。ftp-connector/sftp-connector：FTP/SFTP连接。mongodb-connector：MongoDB连接。redis-connector：Redis/DCS连接。nas-connector：NAS/SFS连接。kafka-connector：Kafka连接。dis-connector：DIS连接。elasticsearch-connector：Elasticsearch/云搜索服务连接。dli-connector：DLI连接。opentsdb-connector：CloudTable OpenTSDB连接。http-connector：HTTP/HTTPS连接，该连接暂无连接参数。thirdparty-obs-connector：七牛云KODO/腾讯云COS连接、亚马逊对象存储连接。dms-kafka-connector：DMS Kafka连接

        :return: The connector_name of this Links.
        :rtype: str
        """
        return self._connector_name

    @connector_name.setter
    def connector_name(self, connector_name):
        r"""Sets the connector_name of this Links.

        连接器名称，对应的连接参数如下：generic-jdbc-connector：关系数据库连接。obs-connector：OBS连接、阿里云OSS连接。hdfs-connector：HDFS连接。hbase-connector：HBase连接、CloudTable连接。hive-connector：Hive连接。ftp-connector/sftp-connector：FTP/SFTP连接。mongodb-connector：MongoDB连接。redis-connector：Redis/DCS连接。nas-connector：NAS/SFS连接。kafka-connector：Kafka连接。dis-connector：DIS连接。elasticsearch-connector：Elasticsearch/云搜索服务连接。dli-connector：DLI连接。opentsdb-connector：CloudTable OpenTSDB连接。http-connector：HTTP/HTTPS连接，该连接暂无连接参数。thirdparty-obs-connector：七牛云KODO/腾讯云COS连接、亚马逊对象存储连接。dms-kafka-connector：DMS Kafka连接

        :param connector_name: The connector_name of this Links.
        :type connector_name: str
        """
        self._connector_name = connector_name

    @property
    def update_date(self):
        r"""Gets the update_date of this Links.

        更新连接的时间

        :return: The update_date of this Links.
        :rtype: int
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        r"""Sets the update_date of this Links.

        更新连接的时间

        :param update_date: The update_date of this Links.
        :type update_date: int
        """
        self._update_date = update_date

    @property
    def enabled(self):
        r"""Gets the enabled of this Links.

        是否激活连接，默认为“true”

        :return: The enabled of this Links.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this Links.

        是否激活连接，默认为“true”

        :param enabled: The enabled of this Links.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def update_user(self):
        r"""Gets the update_user of this Links.

        更新连接的用户

        :return: The update_user of this Links.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        r"""Sets the update_user of this Links.

        更新连接的用户

        :param update_user: The update_user of this Links.
        :type update_user: str
        """
        self._update_user = update_user

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
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
