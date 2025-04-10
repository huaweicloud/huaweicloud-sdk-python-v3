# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecycleInstance:

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
        'name': 'str',
        'mode': 'str',
        'product_type': 'str',
        'datastore': 'RecycleDatastore',
        'charge_mode': 'str',
        'enterprise_project_id': 'str',
        'backup_id': 'str',
        'created_at': 'str',
        'deleted_at': 'str',
        'retained_until': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mode': 'mode',
        'product_type': 'product_type',
        'datastore': 'datastore',
        'charge_mode': 'charge_mode',
        'enterprise_project_id': 'enterprise_project_id',
        'backup_id': 'backup_id',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'retained_until': 'retained_until'
    }

    def __init__(self, id=None, name=None, mode=None, product_type=None, datastore=None, charge_mode=None, enterprise_project_id=None, backup_id=None, created_at=None, deleted_at=None, retained_until=None):
        r"""RecycleInstance

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param name: 实例名称。
        :type name: str
        :param mode: 实例类型。   - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。
        :type mode: str
        :param product_type: 产品类型。 GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型
        :type product_type: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.RecycleDatastore`
        :param charge_mode: 计费方式。 计费方式。   - prePaid：预付费，即包年/包月。   - postPaid：后付费，即按需付费。
        :type charge_mode: str
        :param enterprise_project_id: 企业项目ID，取值为“0”，表示为default企业项目
        :type enterprise_project_id: str
        :param backup_id: 备份ID。
        :type backup_id: str
        :param created_at: 实例创建时间。
        :type created_at: str
        :param deleted_at: 实例删除时间。
        :type deleted_at: str
        :param retained_until: 回收备份保留截止时间。
        :type retained_until: str
        """
        
        

        self._id = None
        self._name = None
        self._mode = None
        self._product_type = None
        self._datastore = None
        self._charge_mode = None
        self._enterprise_project_id = None
        self._backup_id = None
        self._created_at = None
        self._deleted_at = None
        self._retained_until = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if product_type is not None:
            self.product_type = product_type
        if datastore is not None:
            self.datastore = datastore
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if backup_id is not None:
            self.backup_id = backup_id
        if created_at is not None:
            self.created_at = created_at
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if retained_until is not None:
            self.retained_until = retained_until

    @property
    def id(self):
        r"""Gets the id of this RecycleInstance.

        实例ID。

        :return: The id of this RecycleInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecycleInstance.

        实例ID。

        :param id: The id of this RecycleInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RecycleInstance.

        实例名称。

        :return: The name of this RecycleInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecycleInstance.

        实例名称。

        :param name: The name of this RecycleInstance.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        r"""Gets the mode of this RecycleInstance.

        实例类型。   - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。

        :return: The mode of this RecycleInstance.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this RecycleInstance.

        实例类型。   - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。   - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。   - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。   - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。   - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。   - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。

        :param mode: The mode of this RecycleInstance.
        :type mode: str
        """
        self._mode = mode

    @property
    def product_type(self):
        r"""Gets the product_type of this RecycleInstance.

        产品类型。 GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型

        :return: The product_type of this RecycleInstance.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this RecycleInstance.

        产品类型。 GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型

        :param product_type: The product_type of this RecycleInstance.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def datastore(self):
        r"""Gets the datastore of this RecycleInstance.

        :return: The datastore of this RecycleInstance.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RecycleDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this RecycleInstance.

        :param datastore: The datastore of this RecycleInstance.
        :type datastore: :class:`huaweicloudsdkgaussdbfornosql.v3.RecycleDatastore`
        """
        self._datastore = datastore

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this RecycleInstance.

        计费方式。 计费方式。   - prePaid：预付费，即包年/包月。   - postPaid：后付费，即按需付费。

        :return: The charge_mode of this RecycleInstance.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this RecycleInstance.

        计费方式。 计费方式。   - prePaid：预付费，即包年/包月。   - postPaid：后付费，即按需付费。

        :param charge_mode: The charge_mode of this RecycleInstance.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this RecycleInstance.

        企业项目ID，取值为“0”，表示为default企业项目

        :return: The enterprise_project_id of this RecycleInstance.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this RecycleInstance.

        企业项目ID，取值为“0”，表示为default企业项目

        :param enterprise_project_id: The enterprise_project_id of this RecycleInstance.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this RecycleInstance.

        备份ID。

        :return: The backup_id of this RecycleInstance.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RecycleInstance.

        备份ID。

        :param backup_id: The backup_id of this RecycleInstance.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def created_at(self):
        r"""Gets the created_at of this RecycleInstance.

        实例创建时间。

        :return: The created_at of this RecycleInstance.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecycleInstance.

        实例创建时间。

        :param created_at: The created_at of this RecycleInstance.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def deleted_at(self):
        r"""Gets the deleted_at of this RecycleInstance.

        实例删除时间。

        :return: The deleted_at of this RecycleInstance.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        r"""Sets the deleted_at of this RecycleInstance.

        实例删除时间。

        :param deleted_at: The deleted_at of this RecycleInstance.
        :type deleted_at: str
        """
        self._deleted_at = deleted_at

    @property
    def retained_until(self):
        r"""Gets the retained_until of this RecycleInstance.

        回收备份保留截止时间。

        :return: The retained_until of this RecycleInstance.
        :rtype: str
        """
        return self._retained_until

    @retained_until.setter
    def retained_until(self, retained_until):
        r"""Sets the retained_until of this RecycleInstance.

        回收备份保留截止时间。

        :param retained_until: The retained_until of this RecycleInstance.
        :type retained_until: str
        """
        self._retained_until = retained_until

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
        if not isinstance(other, RecycleInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
