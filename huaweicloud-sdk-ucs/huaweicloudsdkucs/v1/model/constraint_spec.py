# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConstraintSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enforcement_action': 'str',
        'match': 'Match',
        'parameters': 'object'
    }

    attribute_map = {
        'enforcement_action': 'enforcementAction',
        'match': 'match',
        'parameters': 'parameters'
    }

    def __init__(self, enforcement_action=None, match=None, parameters=None):
        r"""ConstraintSpec

        The model defined in huaweicloud sdk

        :param enforcement_action: 策略执行行为，当前支持warn和deny
        :type enforcement_action: str
        :param match: 
        :type match: :class:`huaweicloudsdkucs.v1.Match`
        :param parameters: 可变参数
        :type parameters: object
        """
        
        

        self._enforcement_action = None
        self._match = None
        self._parameters = None
        self.discriminator = None

        if enforcement_action is not None:
            self.enforcement_action = enforcement_action
        if match is not None:
            self.match = match
        if parameters is not None:
            self.parameters = parameters

    @property
    def enforcement_action(self):
        r"""Gets the enforcement_action of this ConstraintSpec.

        策略执行行为，当前支持warn和deny

        :return: The enforcement_action of this ConstraintSpec.
        :rtype: str
        """
        return self._enforcement_action

    @enforcement_action.setter
    def enforcement_action(self, enforcement_action):
        r"""Sets the enforcement_action of this ConstraintSpec.

        策略执行行为，当前支持warn和deny

        :param enforcement_action: The enforcement_action of this ConstraintSpec.
        :type enforcement_action: str
        """
        self._enforcement_action = enforcement_action

    @property
    def match(self):
        r"""Gets the match of this ConstraintSpec.

        :return: The match of this ConstraintSpec.
        :rtype: :class:`huaweicloudsdkucs.v1.Match`
        """
        return self._match

    @match.setter
    def match(self, match):
        r"""Sets the match of this ConstraintSpec.

        :param match: The match of this ConstraintSpec.
        :type match: :class:`huaweicloudsdkucs.v1.Match`
        """
        self._match = match

    @property
    def parameters(self):
        r"""Gets the parameters of this ConstraintSpec.

        可变参数

        :return: The parameters of this ConstraintSpec.
        :rtype: object
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this ConstraintSpec.

        可变参数

        :param parameters: The parameters of this ConstraintSpec.
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
        if not isinstance(other, ConstraintSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
