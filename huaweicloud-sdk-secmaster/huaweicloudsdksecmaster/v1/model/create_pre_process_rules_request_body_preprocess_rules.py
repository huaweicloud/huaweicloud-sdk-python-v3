# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePreProcessRulesRequestBodyPreprocessRules:

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
        'mapper_id': 'str',
        'mapper_type_id': 'str',
        'action': 'str',
        'expression': 'str'
    }

    attribute_map = {
        'name': 'name',
        'mapper_id': 'mapper_id',
        'mapper_type_id': 'mapper_type_id',
        'action': 'action',
        'expression': 'expression'
    }

    def __init__(self, name=None, mapper_id=None, mapper_type_id=None, action=None, expression=None):
        r"""CreatePreProcessRulesRequestBodyPreprocessRules

        The model defined in huaweicloud sdk

        :param name: 名称
        :type name: str
        :param mapper_id: 映射id
        :type mapper_id: str
        :param mapper_type_id: 映射id
        :type mapper_type_id: str
        :param action: 预处理选项: drop-丢弃
        :type action: str
        :param expression: 表达式
        :type expression: str
        """
        
        

        self._name = None
        self._mapper_id = None
        self._mapper_type_id = None
        self._action = None
        self._expression = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if mapper_id is not None:
            self.mapper_id = mapper_id
        if mapper_type_id is not None:
            self.mapper_type_id = mapper_type_id
        if action is not None:
            self.action = action
        if expression is not None:
            self.expression = expression

    @property
    def name(self):
        r"""Gets the name of this CreatePreProcessRulesRequestBodyPreprocessRules.

        名称

        :return: The name of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePreProcessRulesRequestBodyPreprocessRules.

        名称

        :param name: The name of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :type name: str
        """
        self._name = name

    @property
    def mapper_id(self):
        r"""Gets the mapper_id of this CreatePreProcessRulesRequestBodyPreprocessRules.

        映射id

        :return: The mapper_id of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :rtype: str
        """
        return self._mapper_id

    @mapper_id.setter
    def mapper_id(self, mapper_id):
        r"""Sets the mapper_id of this CreatePreProcessRulesRequestBodyPreprocessRules.

        映射id

        :param mapper_id: The mapper_id of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :type mapper_id: str
        """
        self._mapper_id = mapper_id

    @property
    def mapper_type_id(self):
        r"""Gets the mapper_type_id of this CreatePreProcessRulesRequestBodyPreprocessRules.

        映射id

        :return: The mapper_type_id of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :rtype: str
        """
        return self._mapper_type_id

    @mapper_type_id.setter
    def mapper_type_id(self, mapper_type_id):
        r"""Sets the mapper_type_id of this CreatePreProcessRulesRequestBodyPreprocessRules.

        映射id

        :param mapper_type_id: The mapper_type_id of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :type mapper_type_id: str
        """
        self._mapper_type_id = mapper_type_id

    @property
    def action(self):
        r"""Gets the action of this CreatePreProcessRulesRequestBodyPreprocessRules.

        预处理选项: drop-丢弃

        :return: The action of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreatePreProcessRulesRequestBodyPreprocessRules.

        预处理选项: drop-丢弃

        :param action: The action of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :type action: str
        """
        self._action = action

    @property
    def expression(self):
        r"""Gets the expression of this CreatePreProcessRulesRequestBodyPreprocessRules.

        表达式

        :return: The expression of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        r"""Sets the expression of this CreatePreProcessRulesRequestBodyPreprocessRules.

        表达式

        :param expression: The expression of this CreatePreProcessRulesRequestBodyPreprocessRules.
        :type expression: str
        """
        self._expression = expression

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
        if not isinstance(other, CreatePreProcessRulesRequestBodyPreprocessRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
