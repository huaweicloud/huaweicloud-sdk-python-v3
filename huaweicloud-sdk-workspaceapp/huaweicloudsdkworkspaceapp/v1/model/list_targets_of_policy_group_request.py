# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTargetsOfPolicyGroupRequest:

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
        'target_type': 'str'
    }

    attribute_map = {
        'policy_group_id': 'policy_group_id',
        'target_type': 'target_type'
    }

    def __init__(self, policy_group_id=None, target_type=None):
        """ListTargetsOfPolicyGroupRequest

        The model defined in huaweicloud sdk

        :param policy_group_id: 策略组id。
        :type policy_group_id: str
        :param target_type: 应用对象的类型。 - USER：表示用户 - USERGROUP：表示用户组。 - APPGROUP：应用组。 - OU：组织单元。 - ALl：所有类型
        :type target_type: str
        """
        
        

        self._policy_group_id = None
        self._target_type = None
        self.discriminator = None

        self.policy_group_id = policy_group_id
        if target_type is not None:
            self.target_type = target_type

    @property
    def policy_group_id(self):
        """Gets the policy_group_id of this ListTargetsOfPolicyGroupRequest.

        策略组id。

        :return: The policy_group_id of this ListTargetsOfPolicyGroupRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        """Sets the policy_group_id of this ListTargetsOfPolicyGroupRequest.

        策略组id。

        :param policy_group_id: The policy_group_id of this ListTargetsOfPolicyGroupRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def target_type(self):
        """Gets the target_type of this ListTargetsOfPolicyGroupRequest.

        应用对象的类型。 - USER：表示用户 - USERGROUP：表示用户组。 - APPGROUP：应用组。 - OU：组织单元。 - ALl：所有类型

        :return: The target_type of this ListTargetsOfPolicyGroupRequest.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this ListTargetsOfPolicyGroupRequest.

        应用对象的类型。 - USER：表示用户 - USERGROUP：表示用户组。 - APPGROUP：应用组。 - OU：组织单元。 - ALl：所有类型

        :param target_type: The target_type of this ListTargetsOfPolicyGroupRequest.
        :type target_type: str
        """
        self._target_type = target_type

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
        if not isinstance(other, ListTargetsOfPolicyGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
