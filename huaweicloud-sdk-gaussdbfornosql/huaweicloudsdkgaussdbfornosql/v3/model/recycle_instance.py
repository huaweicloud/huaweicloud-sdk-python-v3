# coding: utf-8

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
        'data_store': 'RecycleDatastore',
        'charge_type': 'str',
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
        'data_store': 'data_store',
        'charge_type': 'charge_type',
        'enterprise_project_id': 'enterprise_project_id',
        'backup_id': 'backup_id',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'retained_until': 'retained_until'
    }

    def __init__(self, id=None, name=None, mode=None, product_type=None, data_store=None, charge_type=None, enterprise_project_id=None, backup_id=None, created_at=None, deleted_at=None, retained_until=None):
        r"""RecycleInstance

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 实例ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 实例名称。 **取值范围：** 不涉及。
        :type name: str
        :param mode: **参数解释：** 实例类型。 **取值范围：** - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。 - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。 - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。 - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。 - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。 - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。
        :type mode: str
        :param product_type: **参数解释：** 产品类型。 **取值范围：** GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型
        :type product_type: str
        :param data_store: 
        :type data_store: :class:`huaweicloudsdkgaussdbfornosql.v3.RecycleDatastore`
        :param charge_type: **参数解释：** 计费方式。 **取值范围：** - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。
        :type charge_type: str
        :param enterprise_project_id: **参数解释：** 企业项目ID，取值为“0”，表示为default企业项目 **取值范围：** 不涉及。
        :type enterprise_project_id: str
        :param backup_id: **参数解释：** 备份ID。 **取值范围：** 不涉及。
        :type backup_id: str
        :param created_at: **参数解释：** 实例创建时间。 **取值范围：** 不涉及。
        :type created_at: str
        :param deleted_at: **参数解释：** 实例删除时间。 **取值范围：** 不涉及。
        :type deleted_at: str
        :param retained_until: **参数解释：** 回收备份保留截止时间。 **取值范围：** 不涉及。
        :type retained_until: str
        """
        
        

        self._id = None
        self._name = None
        self._mode = None
        self._product_type = None
        self._data_store = None
        self._charge_type = None
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
        if data_store is not None:
            self.data_store = data_store
        if charge_type is not None:
            self.charge_type = charge_type
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

        **参数解释：** 实例ID。 **取值范围：** 不涉及。

        :return: The id of this RecycleInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecycleInstance.

        **参数解释：** 实例ID。 **取值范围：** 不涉及。

        :param id: The id of this RecycleInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RecycleInstance.

        **参数解释：** 实例名称。 **取值范围：** 不涉及。

        :return: The name of this RecycleInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecycleInstance.

        **参数解释：** 实例名称。 **取值范围：** 不涉及。

        :param name: The name of this RecycleInstance.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        r"""Gets the mode of this RecycleInstance.

        **参数解释：** 实例类型。 **取值范围：** - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。 - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。 - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。 - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。 - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。 - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。

        :return: The mode of this RecycleInstance.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this RecycleInstance.

        **参数解释：** 实例类型。 **取值范围：** - 取值为“Cluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis Proxy经典部署模式集群实例类型。 - 取值为“CloudNativeCluster”，表示GeminiDB Cassandra、GeminiDB Influx、GeminiDB Redis云原生部署模式集群实例类型。 - 取值为“RedisCluster”，表示GeminiDB Redis Cluster经典部署模式集群实例类型。 - 取值为“Replication”，表示GeminiDB Redis经典部署模式主备实例类型。 - 取值为“InfluxdbSingle”，表示GeminiDB Influx经典部署模式单节点实例类型。 - 取值为“ReplicaSet”，表示GeminiDB Mongo副本集实例类型。

        :param mode: The mode of this RecycleInstance.
        :type mode: str
        """
        self._mode = mode

    @property
    def product_type(self):
        r"""Gets the product_type of this RecycleInstance.

        **参数解释：** 产品类型。 **取值范围：** GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型

        :return: The product_type of this RecycleInstance.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        r"""Sets the product_type of this RecycleInstance.

        **参数解释：** 产品类型。 **取值范围：** GeminiDB Redis云原生部署模式集群涉及此字段，取值：   -  Standard 标准型   -  Capacity 容量型

        :param product_type: The product_type of this RecycleInstance.
        :type product_type: str
        """
        self._product_type = product_type

    @property
    def data_store(self):
        r"""Gets the data_store of this RecycleInstance.

        :return: The data_store of this RecycleInstance.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RecycleDatastore`
        """
        return self._data_store

    @data_store.setter
    def data_store(self, data_store):
        r"""Sets the data_store of this RecycleInstance.

        :param data_store: The data_store of this RecycleInstance.
        :type data_store: :class:`huaweicloudsdkgaussdbfornosql.v3.RecycleDatastore`
        """
        self._data_store = data_store

    @property
    def charge_type(self):
        r"""Gets the charge_type of this RecycleInstance.

        **参数解释：** 计费方式。 **取值范围：** - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。

        :return: The charge_type of this RecycleInstance.
        :rtype: str
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        r"""Sets the charge_type of this RecycleInstance.

        **参数解释：** 计费方式。 **取值范围：** - prePaid：预付费，即包年/包月。 - postPaid：后付费，即按需付费。

        :param charge_type: The charge_type of this RecycleInstance.
        :type charge_type: str
        """
        self._charge_type = charge_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this RecycleInstance.

        **参数解释：** 企业项目ID，取值为“0”，表示为default企业项目 **取值范围：** 不涉及。

        :return: The enterprise_project_id of this RecycleInstance.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this RecycleInstance.

        **参数解释：** 企业项目ID，取值为“0”，表示为default企业项目 **取值范围：** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this RecycleInstance.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def backup_id(self):
        r"""Gets the backup_id of this RecycleInstance.

        **参数解释：** 备份ID。 **取值范围：** 不涉及。

        :return: The backup_id of this RecycleInstance.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RecycleInstance.

        **参数解释：** 备份ID。 **取值范围：** 不涉及。

        :param backup_id: The backup_id of this RecycleInstance.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def created_at(self):
        r"""Gets the created_at of this RecycleInstance.

        **参数解释：** 实例创建时间。 **取值范围：** 不涉及。

        :return: The created_at of this RecycleInstance.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecycleInstance.

        **参数解释：** 实例创建时间。 **取值范围：** 不涉及。

        :param created_at: The created_at of this RecycleInstance.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def deleted_at(self):
        r"""Gets the deleted_at of this RecycleInstance.

        **参数解释：** 实例删除时间。 **取值范围：** 不涉及。

        :return: The deleted_at of this RecycleInstance.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        r"""Sets the deleted_at of this RecycleInstance.

        **参数解释：** 实例删除时间。 **取值范围：** 不涉及。

        :param deleted_at: The deleted_at of this RecycleInstance.
        :type deleted_at: str
        """
        self._deleted_at = deleted_at

    @property
    def retained_until(self):
        r"""Gets the retained_until of this RecycleInstance.

        **参数解释：** 回收备份保留截止时间。 **取值范围：** 不涉及。

        :return: The retained_until of this RecycleInstance.
        :rtype: str
        """
        return self._retained_until

    @retained_until.setter
    def retained_until(self, retained_until):
        r"""Sets the retained_until of this RecycleInstance.

        **参数解释：** 回收备份保留截止时间。 **取值范围：** 不涉及。

        :param retained_until: The retained_until of this RecycleInstance.
        :type retained_until: str
        """
        self._retained_until = retained_until

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
