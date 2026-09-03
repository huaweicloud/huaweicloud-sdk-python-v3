# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeletePolicyEngineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_engine_id': 'str'
    }

    attribute_map = {
        'policy_engine_id': 'policy_engine_id'
    }

    def __init__(self, policy_engine_id=None):
        r"""DeletePolicyEngineRequest

        The model defined in huaweicloud sdk

        :param policy_engine_id: System-generated unique identifier for the policy engine.
        :type policy_engine_id: str
        """
        
        

        self._policy_engine_id = None
        self.discriminator = None

        self.policy_engine_id = policy_engine_id

    @property
    def policy_engine_id(self):
        r"""Gets the policy_engine_id of this DeletePolicyEngineRequest.

        System-generated unique identifier for the policy engine.

        :return: The policy_engine_id of this DeletePolicyEngineRequest.
        :rtype: str
        """
        return self._policy_engine_id

    @policy_engine_id.setter
    def policy_engine_id(self, policy_engine_id):
        r"""Sets the policy_engine_id of this DeletePolicyEngineRequest.

        System-generated unique identifier for the policy engine.

        :param policy_engine_id: The policy_engine_id of this DeletePolicyEngineRequest.
        :type policy_engine_id: str
        """
        self._policy_engine_id = policy_engine_id

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
        if not isinstance(other, DeletePolicyEngineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
