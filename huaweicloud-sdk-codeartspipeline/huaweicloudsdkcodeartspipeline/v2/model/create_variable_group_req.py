# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateVariableGroupReq:

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
        'variables': 'list[CreateVariableGroupReqVariables]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'variables': 'variables'
    }

    def __init__(self, name=None, description=None, variables=None):
        r"""CreateVariableGroupReq

        The model defined in huaweicloud sdk

        :param name: **参数解释**： 参数组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type name: str
        :param description: **参数解释**： 描述详情。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type description: str
        :param variables: **参数解释**： 参数列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CreateVariableGroupReqVariables`]
        """
        
        

        self._name = None
        self._description = None
        self._variables = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if variables is not None:
            self.variables = variables

    @property
    def name(self):
        r"""Gets the name of this CreateVariableGroupReq.

        **参数解释**： 参数组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The name of this CreateVariableGroupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateVariableGroupReq.

        **参数解释**： 参数组名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param name: The name of this CreateVariableGroupReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateVariableGroupReq.

        **参数解释**： 描述详情。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The description of this CreateVariableGroupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateVariableGroupReq.

        **参数解释**： 描述详情。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param description: The description of this CreateVariableGroupReq.
        :type description: str
        """
        self._description = description

    @property
    def variables(self):
        r"""Gets the variables of this CreateVariableGroupReq.

        **参数解释**： 参数列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The variables of this CreateVariableGroupReq.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.CreateVariableGroupReqVariables`]
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        r"""Sets the variables of this CreateVariableGroupReq.

        **参数解释**： 参数列表。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param variables: The variables of this CreateVariableGroupReq.
        :type variables: list[:class:`huaweicloudsdkcodeartspipeline.v2.CreateVariableGroupReqVariables`]
        """
        self._variables = variables

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
        if not isinstance(other, CreateVariableGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
