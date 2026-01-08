# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopologyEdge:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'target': 'str',
        'source_type': 'str',
        'target_type': 'str',
        'label': 'str',
        'label_id': 'str'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target',
        'source_type': 'source_type',
        'target_type': 'target_type',
        'label': 'label',
        'label_id': 'label_id'
    }

    def __init__(self, source=None, target=None, source_type=None, target_type=None, label=None, label_id=None):
        r"""TopologyEdge

        The model defined in huaweicloud sdk

        :param source: **参数解释**：边起点id。  **取值范围**：不涉及
        :type source: str
        :param target: **参数解释**：边终点id。  **取值范围**：不涉及
        :type target: str
        :param source_type: **参数解释**：边起点类型。  **取值范围**：不涉及
        :type source_type: str
        :param target_type: **参数解释**：边终点类型。  **取值范围**：不涉及
        :type target_type: str
        :param label: **参数解释**：边label信息。  **取值范围**：不涉及
        :type label: str
        :param label_id: **参数解释**：label id。  **取值范围**：不涉及
        :type label_id: str
        """
        
        

        self._source = None
        self._target = None
        self._source_type = None
        self._target_type = None
        self._label = None
        self._label_id = None
        self.discriminator = None

        self.source = source
        self.target = target
        self.source_type = source_type
        self.target_type = target_type
        if label is not None:
            self.label = label
        if label_id is not None:
            self.label_id = label_id

    @property
    def source(self):
        r"""Gets the source of this TopologyEdge.

        **参数解释**：边起点id。  **取值范围**：不涉及

        :return: The source of this TopologyEdge.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this TopologyEdge.

        **参数解释**：边起点id。  **取值范围**：不涉及

        :param source: The source of this TopologyEdge.
        :type source: str
        """
        self._source = source

    @property
    def target(self):
        r"""Gets the target of this TopologyEdge.

        **参数解释**：边终点id。  **取值范围**：不涉及

        :return: The target of this TopologyEdge.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this TopologyEdge.

        **参数解释**：边终点id。  **取值范围**：不涉及

        :param target: The target of this TopologyEdge.
        :type target: str
        """
        self._target = target

    @property
    def source_type(self):
        r"""Gets the source_type of this TopologyEdge.

        **参数解释**：边起点类型。  **取值范围**：不涉及

        :return: The source_type of this TopologyEdge.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this TopologyEdge.

        **参数解释**：边起点类型。  **取值范围**：不涉及

        :param source_type: The source_type of this TopologyEdge.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def target_type(self):
        r"""Gets the target_type of this TopologyEdge.

        **参数解释**：边终点类型。  **取值范围**：不涉及

        :return: The target_type of this TopologyEdge.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this TopologyEdge.

        **参数解释**：边终点类型。  **取值范围**：不涉及

        :param target_type: The target_type of this TopologyEdge.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def label(self):
        r"""Gets the label of this TopologyEdge.

        **参数解释**：边label信息。  **取值范围**：不涉及

        :return: The label of this TopologyEdge.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this TopologyEdge.

        **参数解释**：边label信息。  **取值范围**：不涉及

        :param label: The label of this TopologyEdge.
        :type label: str
        """
        self._label = label

    @property
    def label_id(self):
        r"""Gets the label_id of this TopologyEdge.

        **参数解释**：label id。  **取值范围**：不涉及

        :return: The label_id of this TopologyEdge.
        :rtype: str
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        r"""Sets the label_id of this TopologyEdge.

        **参数解释**：label id。  **取值范围**：不涉及

        :param label_id: The label_id of this TopologyEdge.
        :type label_id: str
        """
        self._label_id = label_id

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
        if not isinstance(other, TopologyEdge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
