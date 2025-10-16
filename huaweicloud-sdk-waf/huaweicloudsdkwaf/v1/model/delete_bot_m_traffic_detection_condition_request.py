# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBotMTrafficDetectionConditionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'condition_id': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'condition_id': 'condition_id'
    }

    def __init__(self, policy_id=None, condition_id=None):
        r"""DeleteBotMTrafficDetectionConditionRequest

        The model defined in huaweicloud sdk

        :param policy_id: policyId
        :type policy_id: str
        :param condition_id: 流量检测条件Id
        :type condition_id: str
        """
        
        

        self._policy_id = None
        self._condition_id = None
        self.discriminator = None

        self.policy_id = policy_id
        self.condition_id = condition_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this DeleteBotMTrafficDetectionConditionRequest.

        policyId

        :return: The policy_id of this DeleteBotMTrafficDetectionConditionRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this DeleteBotMTrafficDetectionConditionRequest.

        policyId

        :param policy_id: The policy_id of this DeleteBotMTrafficDetectionConditionRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def condition_id(self):
        r"""Gets the condition_id of this DeleteBotMTrafficDetectionConditionRequest.

        流量检测条件Id

        :return: The condition_id of this DeleteBotMTrafficDetectionConditionRequest.
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        r"""Sets the condition_id of this DeleteBotMTrafficDetectionConditionRequest.

        流量检测条件Id

        :param condition_id: The condition_id of this DeleteBotMTrafficDetectionConditionRequest.
        :type condition_id: str
        """
        self._condition_id = condition_id

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
        if not isinstance(other, DeleteBotMTrafficDetectionConditionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
