# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKeyUsageFlowResponseBodyEdges:

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
        'target': 'str'
    }

    attribute_map = {
        'source': 'source',
        'target': 'target'
    }

    def __init__(self, source=None, target=None):
        r"""ShowKeyUsageFlowResponseBodyEdges

        The model defined in huaweicloud sdk

        :param source: **参数解释：** 边起点节点ID **取值范围：** 不涉及
        :type source: str
        :param target: **参数解释：** 边终点节点ID **取值范围：** 不涉及
        :type target: str
        """
        
        

        self._source = None
        self._target = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if target is not None:
            self.target = target

    @property
    def source(self):
        r"""Gets the source of this ShowKeyUsageFlowResponseBodyEdges.

        **参数解释：** 边起点节点ID **取值范围：** 不涉及

        :return: The source of this ShowKeyUsageFlowResponseBodyEdges.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ShowKeyUsageFlowResponseBodyEdges.

        **参数解释：** 边起点节点ID **取值范围：** 不涉及

        :param source: The source of this ShowKeyUsageFlowResponseBodyEdges.
        :type source: str
        """
        self._source = source

    @property
    def target(self):
        r"""Gets the target of this ShowKeyUsageFlowResponseBodyEdges.

        **参数解释：** 边终点节点ID **取值范围：** 不涉及

        :return: The target of this ShowKeyUsageFlowResponseBodyEdges.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this ShowKeyUsageFlowResponseBodyEdges.

        **参数解释：** 边终点节点ID **取值范围：** 不涉及

        :param target: The target of this ShowKeyUsageFlowResponseBodyEdges.
        :type target: str
        """
        self._target = target

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
        if not isinstance(other, ShowKeyUsageFlowResponseBodyEdges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
