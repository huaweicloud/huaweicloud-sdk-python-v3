# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrainingExperimentResp:

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
        'id': 'str',
        'serial_number': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'serial_number': 'serial_number'
    }

    def __init__(self, name=None, id=None, serial_number=None):
        r"""TrainingExperimentResp

        The model defined in huaweicloud sdk

        :param name: **参数解释**：实验名称。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param id: **参数解释**：实验ID。 **取值范围**：不涉及。
        :type id: str
        :param serial_number: **参数解释**：当前训练作业在所属的训练实验中的序号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：默认为0。
        :type serial_number: str
        """
        
        

        self._name = None
        self._id = None
        self._serial_number = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if serial_number is not None:
            self.serial_number = serial_number

    @property
    def name(self):
        r"""Gets the name of this TrainingExperimentResp.

        **参数解释**：实验名称。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this TrainingExperimentResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TrainingExperimentResp.

        **参数解释**：实验名称。 **约束限制**：最大长度64，不支持特殊字符。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this TrainingExperimentResp.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this TrainingExperimentResp.

        **参数解释**：实验ID。 **取值范围**：不涉及。

        :return: The id of this TrainingExperimentResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TrainingExperimentResp.

        **参数解释**：实验ID。 **取值范围**：不涉及。

        :param id: The id of this TrainingExperimentResp.
        :type id: str
        """
        self._id = id

    @property
    def serial_number(self):
        r"""Gets the serial_number of this TrainingExperimentResp.

        **参数解释**：当前训练作业在所属的训练实验中的序号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：默认为0。

        :return: The serial_number of this TrainingExperimentResp.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this TrainingExperimentResp.

        **参数解释**：当前训练作业在所属的训练实验中的序号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：默认为0。

        :param serial_number: The serial_number of this TrainingExperimentResp.
        :type serial_number: str
        """
        self._serial_number = serial_number

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
        if not isinstance(other, TrainingExperimentResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
