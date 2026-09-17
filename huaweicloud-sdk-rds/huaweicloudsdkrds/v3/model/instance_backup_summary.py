# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceBackupSummary:

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
        'name': 'str',
        'backup_used_space': 'float',
        'datastore': 'InstanceBackupDatastore',
        'space': 'Space'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name',
        'backup_used_space': 'backup_used_space',
        'datastore': 'datastore',
        'space': 'space'
    }

    def __init__(self, instance_id=None, name=None, backup_used_space=None, datastore=None, space=None):
        r"""InstanceBackupSummary

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instance_id: str
        :param name: **参数解释**：  实例名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type name: str
        :param backup_used_space: **参数解释**：  备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type backup_used_space: float
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkrds.v3.InstanceBackupDatastore`
        :param space: 
        :type space: :class:`huaweicloudsdkrds.v3.Space`
        """
        
        

        self._instance_id = None
        self._name = None
        self._backup_used_space = None
        self._datastore = None
        self._space = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if backup_used_space is not None:
            self.backup_used_space = backup_used_space
        if datastore is not None:
            self.datastore = datastore
        if space is not None:
            self.space = space

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceBackupSummary.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instance_id of this InstanceBackupSummary.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceBackupSummary.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this InstanceBackupSummary.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this InstanceBackupSummary.

        **参数解释**：  实例名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The name of this InstanceBackupSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceBackupSummary.

        **参数解释**：  实例名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param name: The name of this InstanceBackupSummary.
        :type name: str
        """
        self._name = name

    @property
    def backup_used_space(self):
        r"""Gets the backup_used_space of this InstanceBackupSummary.

        **参数解释**：  备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The backup_used_space of this InstanceBackupSummary.
        :rtype: float
        """
        return self._backup_used_space

    @backup_used_space.setter
    def backup_used_space(self, backup_used_space):
        r"""Sets the backup_used_space of this InstanceBackupSummary.

        **参数解释**：  备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param backup_used_space: The backup_used_space of this InstanceBackupSummary.
        :type backup_used_space: float
        """
        self._backup_used_space = backup_used_space

    @property
    def datastore(self):
        r"""Gets the datastore of this InstanceBackupSummary.

        :return: The datastore of this InstanceBackupSummary.
        :rtype: :class:`huaweicloudsdkrds.v3.InstanceBackupDatastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        r"""Sets the datastore of this InstanceBackupSummary.

        :param datastore: The datastore of this InstanceBackupSummary.
        :type datastore: :class:`huaweicloudsdkrds.v3.InstanceBackupDatastore`
        """
        self._datastore = datastore

    @property
    def space(self):
        r"""Gets the space of this InstanceBackupSummary.

        :return: The space of this InstanceBackupSummary.
        :rtype: :class:`huaweicloudsdkrds.v3.Space`
        """
        return self._space

    @space.setter
    def space(self, space):
        r"""Sets the space of this InstanceBackupSummary.

        :param space: The space of this InstanceBackupSummary.
        :type space: :class:`huaweicloudsdkrds.v3.Space`
        """
        self._space = space

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
        if not isinstance(other, InstanceBackupSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
