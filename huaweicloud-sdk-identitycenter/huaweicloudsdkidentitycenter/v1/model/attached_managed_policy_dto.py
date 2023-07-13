# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachedManagedPolicyDto:

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
        'policy_name': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name'
    }

    def __init__(self, policy_id=None, policy_name=None):
        """AttachedManagedPolicyDto

        The model defined in huaweicloud sdk

        :param policy_id: 系统策略唯一标识
        :type policy_id: str
        :param policy_name: 系统策略名称
        :type policy_name: str
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name

    @property
    def policy_id(self):
        """Gets the policy_id of this AttachedManagedPolicyDto.

        系统策略唯一标识

        :return: The policy_id of this AttachedManagedPolicyDto.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this AttachedManagedPolicyDto.

        系统策略唯一标识

        :param policy_id: The policy_id of this AttachedManagedPolicyDto.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        """Gets the policy_name of this AttachedManagedPolicyDto.

        系统策略名称

        :return: The policy_name of this AttachedManagedPolicyDto.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this AttachedManagedPolicyDto.

        系统策略名称

        :param policy_name: The policy_name of this AttachedManagedPolicyDto.
        :type policy_name: str
        """
        self._policy_name = policy_name

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
        if not isinstance(other, AttachedManagedPolicyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
