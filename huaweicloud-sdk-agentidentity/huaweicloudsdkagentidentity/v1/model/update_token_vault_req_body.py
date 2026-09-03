# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTokenVaultReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_engine_configuration': 'PolicyEngineConfiguration'
    }

    attribute_map = {
        'policy_engine_configuration': 'policy_engine_configuration'
    }

    def __init__(self, policy_engine_configuration=None):
        r"""UpdateTokenVaultReqBody

        The model defined in huaweicloud sdk

        :param policy_engine_configuration: 
        :type policy_engine_configuration: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineConfiguration`
        """
        
        

        self._policy_engine_configuration = None
        self.discriminator = None

        self.policy_engine_configuration = policy_engine_configuration

    @property
    def policy_engine_configuration(self):
        r"""Gets the policy_engine_configuration of this UpdateTokenVaultReqBody.

        :return: The policy_engine_configuration of this UpdateTokenVaultReqBody.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineConfiguration`
        """
        return self._policy_engine_configuration

    @policy_engine_configuration.setter
    def policy_engine_configuration(self, policy_engine_configuration):
        r"""Sets the policy_engine_configuration of this UpdateTokenVaultReqBody.

        :param policy_engine_configuration: The policy_engine_configuration of this UpdateTokenVaultReqBody.
        :type policy_engine_configuration: :class:`huaweicloudsdkagentidentity.v1.PolicyEngineConfiguration`
        """
        self._policy_engine_configuration = policy_engine_configuration

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
        if not isinstance(other, UpdateTokenVaultReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
