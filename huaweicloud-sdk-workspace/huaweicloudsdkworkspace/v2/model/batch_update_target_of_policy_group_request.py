# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateTargetOfPolicyGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_id': 'str',
        'body': 'ModifyPolicyTargetReq'
    }

    attribute_map = {
        'policy_group_id': 'policy_group_id',
        'body': 'body'
    }

    def __init__(self, policy_group_id=None, body=None):
        """BatchUpdateTargetOfPolicyGroupRequest

        The model defined in huaweicloud sdk

        :param policy_group_id: 策略组id。
        :type policy_group_id: str
        :param body: Body of the BatchUpdateTargetOfPolicyGroupRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.ModifyPolicyTargetReq`
        """
        
        

        self._policy_group_id = None
        self._body = None
        self.discriminator = None

        self.policy_group_id = policy_group_id
        if body is not None:
            self.body = body

    @property
    def policy_group_id(self):
        """Gets the policy_group_id of this BatchUpdateTargetOfPolicyGroupRequest.

        策略组id。

        :return: The policy_group_id of this BatchUpdateTargetOfPolicyGroupRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        """Sets the policy_group_id of this BatchUpdateTargetOfPolicyGroupRequest.

        策略组id。

        :param policy_group_id: The policy_group_id of this BatchUpdateTargetOfPolicyGroupRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def body(self):
        """Gets the body of this BatchUpdateTargetOfPolicyGroupRequest.

        :return: The body of this BatchUpdateTargetOfPolicyGroupRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ModifyPolicyTargetReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchUpdateTargetOfPolicyGroupRequest.

        :param body: The body of this BatchUpdateTargetOfPolicyGroupRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.ModifyPolicyTargetReq`
        """
        self._body = body

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
        if not isinstance(other, BatchUpdateTargetOfPolicyGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
