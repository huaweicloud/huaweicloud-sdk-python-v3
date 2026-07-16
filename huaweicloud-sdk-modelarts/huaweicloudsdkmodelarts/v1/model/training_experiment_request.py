# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrainingExperimentRequest:

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
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, description=None):
        r"""TrainingExperimentRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释**：实验ID，填写实验ID时，此训练作业将会纳入该已有实验分组，填写前请确保该实验ID真实存在。 **取值范围**：不涉及。
        :type id: str
        :param name: **参数解释**：实验名称，只填写实验名称时，将会创建该实验分组，并将此训练作业纳入该分组。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param description: **参数解释**：描述信息。 **约束限制**：最大长度256，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this TrainingExperimentRequest.

        **参数解释**：实验ID，填写实验ID时，此训练作业将会纳入该已有实验分组，填写前请确保该实验ID真实存在。 **取值范围**：不涉及。

        :return: The id of this TrainingExperimentRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TrainingExperimentRequest.

        **参数解释**：实验ID，填写实验ID时，此训练作业将会纳入该已有实验分组，填写前请确保该实验ID真实存在。 **取值范围**：不涉及。

        :param id: The id of this TrainingExperimentRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this TrainingExperimentRequest.

        **参数解释**：实验名称，只填写实验名称时，将会创建该实验分组，并将此训练作业纳入该分组。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this TrainingExperimentRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TrainingExperimentRequest.

        **参数解释**：实验名称，只填写实验名称时，将会创建该实验分组，并将此训练作业纳入该分组。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this TrainingExperimentRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TrainingExperimentRequest.

        **参数解释**：描述信息。 **约束限制**：最大长度256，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The description of this TrainingExperimentRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TrainingExperimentRequest.

        **参数解释**：描述信息。 **约束限制**：最大长度256，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param description: The description of this TrainingExperimentRequest.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, TrainingExperimentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
