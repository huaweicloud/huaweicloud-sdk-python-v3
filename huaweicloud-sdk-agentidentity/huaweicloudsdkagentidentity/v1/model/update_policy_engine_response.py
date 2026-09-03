# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyEngineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_engine': 'PolicyEngine'
    }

    attribute_map = {
        'policy_engine': 'policy_engine'
    }

    def __init__(self, policy_engine=None):
        r"""UpdatePolicyEngineResponse

        The model defined in huaweicloud sdk

        :param policy_engine: 
        :type policy_engine: :class:`huaweicloudsdkagentidentity.v1.PolicyEngine`
        """
        
        super().__init__()

        self._policy_engine = None
        self.discriminator = None

        if policy_engine is not None:
            self.policy_engine = policy_engine

    @property
    def policy_engine(self):
        r"""Gets the policy_engine of this UpdatePolicyEngineResponse.

        :return: The policy_engine of this UpdatePolicyEngineResponse.
        :rtype: :class:`huaweicloudsdkagentidentity.v1.PolicyEngine`
        """
        return self._policy_engine

    @policy_engine.setter
    def policy_engine(self, policy_engine):
        r"""Sets the policy_engine of this UpdatePolicyEngineResponse.

        :param policy_engine: The policy_engine of this UpdatePolicyEngineResponse.
        :type policy_engine: :class:`huaweicloudsdkagentidentity.v1.PolicyEngine`
        """
        self._policy_engine = policy_engine

    def to_dict(self):
        import warnings
        warnings.warn("UpdatePolicyEngineResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UpdatePolicyEngineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
