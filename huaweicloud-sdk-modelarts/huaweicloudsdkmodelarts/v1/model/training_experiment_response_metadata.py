# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrainingExperimentResponseMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'workspace_id': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'workspace_id': 'workspace_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'id': 'id'
    }

    def __init__(self, name=None, description=None, workspace_id=None, create_time=None, update_time=None, id=None):
        r"""TrainingExperimentResponseMetadata

        The model defined in huaweicloud sdk

        :param name: **参数解释**：实验名称。 **取值范围**：不涉及。
        :type name: str
        :param description: **参数解释**：描述信息。 **取值范围**：不涉及。
        :type description: str
        :param workspace_id: **参数解释**：工作空间ID。 **取值范围**：不涉及。
        :type workspace_id: str
        :param create_time: **参数解释**：创建时间。 **取值范围**：不涉及。
        :type create_time: int
        :param update_time: **参数解释**：更新时间。 **取值范围**：不涉及。
        :type update_time: int
        :param id: **参数解释**：实验ID。 **取值范围**：不涉及。
        :type id: str
        """
        
        

        self._name = None
        self._description = None
        self._workspace_id = None
        self._create_time = None
        self._update_time = None
        self._id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if id is not None:
            self.id = id

    @property
    def name(self):
        r"""Gets the name of this TrainingExperimentResponseMetadata.

        **参数解释**：实验名称。 **取值范围**：不涉及。

        :return: The name of this TrainingExperimentResponseMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TrainingExperimentResponseMetadata.

        **参数解释**：实验名称。 **取值范围**：不涉及。

        :param name: The name of this TrainingExperimentResponseMetadata.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TrainingExperimentResponseMetadata.

        **参数解释**：描述信息。 **取值范围**：不涉及。

        :return: The description of this TrainingExperimentResponseMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TrainingExperimentResponseMetadata.

        **参数解释**：描述信息。 **取值范围**：不涉及。

        :param description: The description of this TrainingExperimentResponseMetadata.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this TrainingExperimentResponseMetadata.

        **参数解释**：工作空间ID。 **取值范围**：不涉及。

        :return: The workspace_id of this TrainingExperimentResponseMetadata.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this TrainingExperimentResponseMetadata.

        **参数解释**：工作空间ID。 **取值范围**：不涉及。

        :param workspace_id: The workspace_id of this TrainingExperimentResponseMetadata.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def create_time(self):
        r"""Gets the create_time of this TrainingExperimentResponseMetadata.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :return: The create_time of this TrainingExperimentResponseMetadata.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this TrainingExperimentResponseMetadata.

        **参数解释**：创建时间。 **取值范围**：不涉及。

        :param create_time: The create_time of this TrainingExperimentResponseMetadata.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this TrainingExperimentResponseMetadata.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :return: The update_time of this TrainingExperimentResponseMetadata.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this TrainingExperimentResponseMetadata.

        **参数解释**：更新时间。 **取值范围**：不涉及。

        :param update_time: The update_time of this TrainingExperimentResponseMetadata.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this TrainingExperimentResponseMetadata.

        **参数解释**：实验ID。 **取值范围**：不涉及。

        :return: The id of this TrainingExperimentResponseMetadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TrainingExperimentResponseMetadata.

        **参数解释**：实验ID。 **取值范围**：不涉及。

        :param id: The id of this TrainingExperimentResponseMetadata.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, TrainingExperimentResponseMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
