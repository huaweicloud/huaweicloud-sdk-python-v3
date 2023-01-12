# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisablePolicyAssignmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_auth_token')

    openapi_types = {
        'x_auth_token': 'str',
        'policy_assignment_id': 'str'
    }

    attribute_map = {
        'x_auth_token': 'X-Auth-Token',
        'policy_assignment_id': 'policy_assignment_id'
    }

    def __init__(self, x_auth_token=None, policy_assignment_id=None):
        """DisablePolicyAssignmentRequest

        The model defined in huaweicloud sdk

        :param x_auth_token: 用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。
        :type x_auth_token: str
        :param policy_assignment_id: 规则ID
        :type policy_assignment_id: str
        """
        
        

        self._x_auth_token = None
        self._policy_assignment_id = None
        self.discriminator = None

        self.x_auth_token = x_auth_token
        self.policy_assignment_id = policy_assignment_id

    @property
    def x_auth_token(self):
        """Gets the x_auth_token of this DisablePolicyAssignmentRequest.

        用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。

        :return: The x_auth_token of this DisablePolicyAssignmentRequest.
        :rtype: str
        """
        return self._x_auth_token

    @x_auth_token.setter
    def x_auth_token(self, x_auth_token):
        """Sets the x_auth_token of this DisablePolicyAssignmentRequest.

        用户Token。 获取Token，请参考《统一身份认证服务API参考》的“获取用户Token”章节。请求响应成功后在响应消息头中包含的“X-Subject-Token”的值即为Token值。

        :param x_auth_token: The x_auth_token of this DisablePolicyAssignmentRequest.
        :type x_auth_token: str
        """
        self._x_auth_token = x_auth_token

    @property
    def policy_assignment_id(self):
        """Gets the policy_assignment_id of this DisablePolicyAssignmentRequest.

        规则ID

        :return: The policy_assignment_id of this DisablePolicyAssignmentRequest.
        :rtype: str
        """
        return self._policy_assignment_id

    @policy_assignment_id.setter
    def policy_assignment_id(self, policy_assignment_id):
        """Sets the policy_assignment_id of this DisablePolicyAssignmentRequest.

        规则ID

        :param policy_assignment_id: The policy_assignment_id of this DisablePolicyAssignmentRequest.
        :type policy_assignment_id: str
        """
        self._policy_assignment_id = policy_assignment_id

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
        if not isinstance(other, DisablePolicyAssignmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
