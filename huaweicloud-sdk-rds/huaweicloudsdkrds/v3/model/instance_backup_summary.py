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
        'id': 'str',
        'name': 'str',
        'backup_use_space': 'float',
        'datastore': 'InstanceBackupDatastore',
        'spaces': 'Spaces'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'backup_use_space': 'backup_use_space',
        'datastore': 'datastore',
        'spaces': 'spaces'
    }

    def __init__(self, id=None, name=None, backup_use_space=None, datastore=None, spaces=None):
        r"""InstanceBackupSummary

        The model defined in huaweicloud sdk

        :param id: **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type id: str
        :param name: **参数解释**：  实例名称。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type name: str
        :param backup_use_space: **参数解释**：  备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type backup_use_space: float
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkrds.v3.InstanceBackupDatastore`
        :param spaces: 
        :type spaces: :class:`huaweicloudsdkrds.v3.Spaces`
        """
        
        

        self._id = None
        self._name = None
        self._backup_use_space = None
        self._datastore = None
        self._spaces = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if backup_use_space is not None:
            self.backup_use_space = backup_use_space
        if datastore is not None:
            self.datastore = datastore
        if spaces is not None:
            self.spaces = spaces

    @property
    def id(self):
        r"""Gets the id of this InstanceBackupSummary.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The id of this InstanceBackupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceBackupSummary.

        **参数解释**：  实例ID。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param id: The id of this InstanceBackupSummary.
        :type id: str
        """
        self._id = id

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
    def backup_use_space(self):
        r"""Gets the backup_use_space of this InstanceBackupSummary.

        **参数解释**：  备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The backup_use_space of this InstanceBackupSummary.
        :rtype: float
        """
        return self._backup_use_space

    @backup_use_space.setter
    def backup_use_space(self, backup_use_space):
        r"""Sets the backup_use_space of this InstanceBackupSummary.

        **参数解释**：  备份用量，单位MB。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param backup_use_space: The backup_use_space of this InstanceBackupSummary.
        :type backup_use_space: float
        """
        self._backup_use_space = backup_use_space

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
    def spaces(self):
        r"""Gets the spaces of this InstanceBackupSummary.

        :return: The spaces of this InstanceBackupSummary.
        :rtype: :class:`huaweicloudsdkrds.v3.Spaces`
        """
        return self._spaces

    @spaces.setter
    def spaces(self, spaces):
        r"""Sets the spaces of this InstanceBackupSummary.

        :param spaces: The spaces of this InstanceBackupSummary.
        :type spaces: :class:`huaweicloudsdkrds.v3.Spaces`
        """
        self._spaces = spaces

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
