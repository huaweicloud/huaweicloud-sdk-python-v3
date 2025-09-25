# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ToolCall:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'name': 'str',
        'operation': 'str',
        'parameters': 'dict(str, object)'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'operation': 'operation',
        'parameters': 'parameters'
    }

    def __init__(self, type=None, name=None, operation=None, parameters=None):
        r"""ToolCall

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 工具类型。 **约束限制**： 不涉及 **取值范围**： * drug_job：药物作业 * workflow：流程作业 **默认取值**： 不涉及 
        :type type: str
        :param name: **参数解释**： 工具名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type name: str
        :param operation: **参数解释**： 工具操作。 **约束限制**： 不涉及 **取值范围**： * create：新增 * delete：删除 * update：修改 * query：查询 **默认取值**： 不涉及 
        :type operation: str
        :param parameters: **参数解释**： 工具调用所需参数列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type parameters: dict(str, object)
        """
        
        

        self._type = None
        self._name = None
        self._operation = None
        self._parameters = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if operation is not None:
            self.operation = operation
        if parameters is not None:
            self.parameters = parameters

    @property
    def type(self):
        r"""Gets the type of this ToolCall.

        **参数解释**： 工具类型。 **约束限制**： 不涉及 **取值范围**： * drug_job：药物作业 * workflow：流程作业 **默认取值**： 不涉及 

        :return: The type of this ToolCall.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ToolCall.

        **参数解释**： 工具类型。 **约束限制**： 不涉及 **取值范围**： * drug_job：药物作业 * workflow：流程作业 **默认取值**： 不涉及 

        :param type: The type of this ToolCall.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ToolCall.

        **参数解释**： 工具名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The name of this ToolCall.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ToolCall.

        **参数解释**： 工具名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param name: The name of this ToolCall.
        :type name: str
        """
        self._name = name

    @property
    def operation(self):
        r"""Gets the operation of this ToolCall.

        **参数解释**： 工具操作。 **约束限制**： 不涉及 **取值范围**： * create：新增 * delete：删除 * update：修改 * query：查询 **默认取值**： 不涉及 

        :return: The operation of this ToolCall.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ToolCall.

        **参数解释**： 工具操作。 **约束限制**： 不涉及 **取值范围**： * create：新增 * delete：删除 * update：修改 * query：查询 **默认取值**： 不涉及 

        :param operation: The operation of this ToolCall.
        :type operation: str
        """
        self._operation = operation

    @property
    def parameters(self):
        r"""Gets the parameters of this ToolCall.

        **参数解释**： 工具调用所需参数列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The parameters of this ToolCall.
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ToolCall.

        **参数解释**： 工具调用所需参数列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param parameters: The parameters of this ToolCall.
        :type parameters: dict(str, object)
        """
        self._parameters = parameters

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
        if not isinstance(other, ToolCall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
