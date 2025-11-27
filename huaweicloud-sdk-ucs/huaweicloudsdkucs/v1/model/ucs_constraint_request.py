# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UCSConstraintRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'constraint_template_id': 'str',
        'enforcement_action': 'str',
        'namespaces': 'list[str]',
        'parameters': 'object'
    }

    attribute_map = {
        'constraint_template_id': 'constraintTemplateID',
        'enforcement_action': 'enforcementAction',
        'namespaces': 'namespaces',
        'parameters': 'parameters'
    }

    def __init__(self, constraint_template_id=None, enforcement_action=None, namespaces=None, parameters=None):
        r"""UCSConstraintRequest

        The model defined in huaweicloud sdk

        :param constraint_template_id: 策略模板的ID
        :type constraint_template_id: str
        :param enforcement_action: 策略执行方式，当前支持warn和deny
        :type enforcement_action: str
        :param namespaces: 生效的命名空间
        :type namespaces: list[str]
        :param parameters: 策略实例的参数
        :type parameters: object
        """
        
        

        self._constraint_template_id = None
        self._enforcement_action = None
        self._namespaces = None
        self._parameters = None
        self.discriminator = None

        if constraint_template_id is not None:
            self.constraint_template_id = constraint_template_id
        if enforcement_action is not None:
            self.enforcement_action = enforcement_action
        if namespaces is not None:
            self.namespaces = namespaces
        if parameters is not None:
            self.parameters = parameters

    @property
    def constraint_template_id(self):
        r"""Gets the constraint_template_id of this UCSConstraintRequest.

        策略模板的ID

        :return: The constraint_template_id of this UCSConstraintRequest.
        :rtype: str
        """
        return self._constraint_template_id

    @constraint_template_id.setter
    def constraint_template_id(self, constraint_template_id):
        r"""Sets the constraint_template_id of this UCSConstraintRequest.

        策略模板的ID

        :param constraint_template_id: The constraint_template_id of this UCSConstraintRequest.
        :type constraint_template_id: str
        """
        self._constraint_template_id = constraint_template_id

    @property
    def enforcement_action(self):
        r"""Gets the enforcement_action of this UCSConstraintRequest.

        策略执行方式，当前支持warn和deny

        :return: The enforcement_action of this UCSConstraintRequest.
        :rtype: str
        """
        return self._enforcement_action

    @enforcement_action.setter
    def enforcement_action(self, enforcement_action):
        r"""Sets the enforcement_action of this UCSConstraintRequest.

        策略执行方式，当前支持warn和deny

        :param enforcement_action: The enforcement_action of this UCSConstraintRequest.
        :type enforcement_action: str
        """
        self._enforcement_action = enforcement_action

    @property
    def namespaces(self):
        r"""Gets the namespaces of this UCSConstraintRequest.

        生效的命名空间

        :return: The namespaces of this UCSConstraintRequest.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this UCSConstraintRequest.

        生效的命名空间

        :param namespaces: The namespaces of this UCSConstraintRequest.
        :type namespaces: list[str]
        """
        self._namespaces = namespaces

    @property
    def parameters(self):
        r"""Gets the parameters of this UCSConstraintRequest.

        策略实例的参数

        :return: The parameters of this UCSConstraintRequest.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this UCSConstraintRequest.

        策略实例的参数

        :param parameters: The parameters of this UCSConstraintRequest.
        :type parameters: object
        """
        self._parameters = parameters

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
        if not isinstance(other, UCSConstraintRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
