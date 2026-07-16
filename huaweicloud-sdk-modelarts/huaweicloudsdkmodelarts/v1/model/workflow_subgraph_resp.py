# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkflowSubgraphResp:

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
        'steps': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'steps': 'steps'
    }

    def __init__(self, name=None, steps=None):
        r"""WorkflowSubgraphResp

        The model defined in huaweicloud sdk

        :param name: **参数解释**：子图名称。 **取值范围**：不涉及。
        :type name: str
        :param steps: **参数解释**：子图step成员。
        :type steps: list[str]
        """
        
        

        self._name = None
        self._steps = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if steps is not None:
            self.steps = steps

    @property
    def name(self):
        r"""Gets the name of this WorkflowSubgraphResp.

        **参数解释**：子图名称。 **取值范围**：不涉及。

        :return: The name of this WorkflowSubgraphResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkflowSubgraphResp.

        **参数解释**：子图名称。 **取值范围**：不涉及。

        :param name: The name of this WorkflowSubgraphResp.
        :type name: str
        """
        self._name = name

    @property
    def steps(self):
        r"""Gets the steps of this WorkflowSubgraphResp.

        **参数解释**：子图step成员。

        :return: The steps of this WorkflowSubgraphResp.
        :rtype: list[str]
        """
        return self._steps

    @steps.setter
    def steps(self, steps):
        r"""Sets the steps of this WorkflowSubgraphResp.

        **参数解释**：子图step成员。

        :param steps: The steps of this WorkflowSubgraphResp.
        :type steps: list[str]
        """
        self._steps = steps

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
        if not isinstance(other, WorkflowSubgraphResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
