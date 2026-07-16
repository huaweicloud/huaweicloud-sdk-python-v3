# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckTrainingExperimentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'experiment_name': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'experiment_name': 'experiment_name'
    }

    def __init__(self, workspace_id=None, experiment_name=None):
        r"""CheckTrainingExperimentRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID。获取方法请参见[查询工作空间列表](ListWorkspace.xml)。 **约束限制**：存在并使用的工作空间。 **取值范围**：不涉及。 **默认取值**：“0”。
        :type workspace_id: str
        :param experiment_name: **参数解释**：实验名称。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type experiment_name: str
        """
        
        

        self._workspace_id = None
        self._experiment_name = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        self.experiment_name = experiment_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CheckTrainingExperimentRequest.

        **参数解释**：工作空间ID。获取方法请参见[查询工作空间列表](ListWorkspace.xml)。 **约束限制**：存在并使用的工作空间。 **取值范围**：不涉及。 **默认取值**：“0”。

        :return: The workspace_id of this CheckTrainingExperimentRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CheckTrainingExperimentRequest.

        **参数解释**：工作空间ID。获取方法请参见[查询工作空间列表](ListWorkspace.xml)。 **约束限制**：存在并使用的工作空间。 **取值范围**：不涉及。 **默认取值**：“0”。

        :param workspace_id: The workspace_id of this CheckTrainingExperimentRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def experiment_name(self):
        r"""Gets the experiment_name of this CheckTrainingExperimentRequest.

        **参数解释**：实验名称。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The experiment_name of this CheckTrainingExperimentRequest.
        :rtype: str
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        r"""Sets the experiment_name of this CheckTrainingExperimentRequest.

        **参数解释**：实验名称。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param experiment_name: The experiment_name of this CheckTrainingExperimentRequest.
        :type experiment_name: str
        """
        self._experiment_name = experiment_name

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
        if not isinstance(other, CheckTrainingExperimentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
