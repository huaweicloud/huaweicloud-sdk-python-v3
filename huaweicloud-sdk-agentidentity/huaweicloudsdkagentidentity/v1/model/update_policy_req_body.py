# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'definition': 'PolicyDefinition',
        'validation_mode': 'ValidationMode'
    }

    attribute_map = {
        'description': 'description',
        'definition': 'definition',
        'validation_mode': 'validation_mode'
    }

    def __init__(self, description=None, definition=None, validation_mode=None):
        r"""UpdatePolicyReqBody

        The model defined in huaweicloud sdk

        :param description: 策略的更新描述。
        :type description: str
        :param definition: 
        :type definition: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        :param validation_mode: 
        :type validation_mode: :class:`huaweicloudsdkagentidentity.v1.ValidationMode`
        """
        
        

        self._description = None
        self._definition = None
        self._validation_mode = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if definition is not None:
            self.definition = definition
        if validation_mode is not None:
            self.validation_mode = validation_mode

    @property
    def description(self):
        r"""Gets the description of this UpdatePolicyReqBody.

        策略的更新描述。

        :return: The description of this UpdatePolicyReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdatePolicyReqBody.

        策略的更新描述。

        :param description: The description of this UpdatePolicyReqBody.
        :type description: str
        """
        self._description = description

    @property
    def definition(self):
        r"""Gets the definition of this UpdatePolicyReqBody.

        :return: The definition of this UpdatePolicyReqBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        """
        return self._definition

    @definition.setter
    def definition(self, definition):
        r"""Sets the definition of this UpdatePolicyReqBody.

        :param definition: The definition of this UpdatePolicyReqBody.
        :type definition: :class:`huaweicloudsdkagentidentity.v1.PolicyDefinition`
        """
        self._definition = definition

    @property
    def validation_mode(self):
        r"""Gets the validation_mode of this UpdatePolicyReqBody.

        :return: The validation_mode of this UpdatePolicyReqBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.ValidationMode`
        """
        return self._validation_mode

    @validation_mode.setter
    def validation_mode(self, validation_mode):
        r"""Sets the validation_mode of this UpdatePolicyReqBody.

        :param validation_mode: The validation_mode of this UpdatePolicyReqBody.
        :type validation_mode: :class:`huaweicloudsdkagentidentity.v1.ValidationMode`
        """
        self._validation_mode = validation_mode

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
        if not isinstance(other, UpdatePolicyReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
