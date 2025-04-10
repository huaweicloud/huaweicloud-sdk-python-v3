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
        'datastore': 'RecycleDatastore',
        'pay_mode': 'str',
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
        'datastore': 'datastore',
        'pay_mode': 'pay_mode',
        'enterprise_project_id': 'enterprise_project_id',
        'backup_id': 'backup_id',
        'created_at': 'created_at',
        'deleted_at': 'deleted_at',
        'retained_until': 'retained_until'
    }

    def __init__(self, id=None, name=None, mode=None, datastore=None, pay_mode=None, enterprise_project_id=None, backup_id=None, created_at=None, deleted_at=None, retained_until=None):
        r"""RecycleInstance

        The model defined in huaweicloud sdk

        :param id: 实例ID
        :type id: str
        :param name: 实例名称
        :type name: str
        :param mode: 实例类型。支持集群、副本集、以及单节点。 取值   - Sharding   - ReplicaSet   - Single
        :type mode: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkdds.v3.RecycleDatastore`
        :param pay_mode: 计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。
        :type pay_mode: str
        :param enterprise_project_id: 企业项目ID，取值为“0”，表示为default企业项目
        :type enterprise_project_id: str
        :param backup_id: 备份ID
        :type backup_id: str
        :param created_at: 创建时间
        :type created_at: str
        :param deleted_at: 删除时间
        :type deleted_at: str
        :param retained_until: 保留截止时间
        :type retained_until: str
        """
        
        

        self._id = None
        self._name = None
        self._mode = None
        self._datastore = None
        self._pay_mode = None
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
        if datastore is not None:
            self.datastore = datastore
        if pay_mode is not None:
            self.pay_mode = pay_mode
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

        实例ID

        :return: The id of this RecycleInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RecycleInstance.

        实例ID

        :param id: The id of this RecycleInstance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this RecycleInstance.

        实例名称

        :return: The name of this RecycleInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RecycleInstance.

        实例名称

        :param name: The name of this RecycleInstance.
        :type name: str
        """
        self._name = name

    @property
    def mode(self):
        r"""Gets the mode of this RecycleInstance.

        实例类型。支持集群、副本集、以及单节点。 取值   - Sharding   - ReplicaSet   - Single

        :return: The mode of this RecycleInstance.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this RecycleInstance.

        实例类型。支持集群、副本集、以及单节点。 取值   - Sharding   - ReplicaSet   - Single

        :param mode: The mode of this RecycleInstance.
        :type mode: str
        """
        self._mode = mode

    @property
    def datastore(self):
        r"""Gets the datastore of this RecycleInstance.

        :return: The datastore of this RecycleInstance.
        :rtype: :class:`huaweicloudsdkdds.v3.RecycleDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this RecycleInstance.

        :param datastore: The datastore of this RecycleInstance.
        :type datastore: :class:`huaweicloudsdkdds.v3.RecycleDatastore`
        """
        self._datastore = datastore

    @property
    def pay_mode(self):
        r"""Gets the pay_mode of this RecycleInstance.

        计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :return: The pay_mode of this RecycleInstance.
        :rtype: str
        """
        return self._pay_mode

    @pay_mode.setter
    def pay_mode(self, pay_mode):
        r"""Sets the pay_mode of this RecycleInstance.

        计费方式。 - 取值为“0”，表示按需计费。 - 取值为“1”，表示包年/包月计费。

        :param pay_mode: The pay_mode of this RecycleInstance.
        :type pay_mode: str
        """
        self._pay_mode = pay_mode

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

        备份ID

        :return: The backup_id of this RecycleInstance.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RecycleInstance.

        备份ID

        :param backup_id: The backup_id of this RecycleInstance.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def created_at(self):
        r"""Gets the created_at of this RecycleInstance.

        创建时间

        :return: The created_at of this RecycleInstance.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this RecycleInstance.

        创建时间

        :param created_at: The created_at of this RecycleInstance.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def deleted_at(self):
        r"""Gets the deleted_at of this RecycleInstance.

        删除时间

        :return: The deleted_at of this RecycleInstance.
        :rtype: str
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        r"""Sets the deleted_at of this RecycleInstance.

        删除时间

        :param deleted_at: The deleted_at of this RecycleInstance.
        :type deleted_at: str
        """
        self._deleted_at = deleted_at

    @property
    def retained_until(self):
        r"""Gets the retained_until of this RecycleInstance.

        保留截止时间

        :return: The retained_until of this RecycleInstance.
        :rtype: str
        """
        return self._retained_until

    @retained_until.setter
    def retained_until(self, retained_until):
        r"""Sets the retained_until of this RecycleInstance.

        保留截止时间

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
