# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachCustomerManagedPolicyToPermissionSetReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'policy_content': 'str',
        'description': 'str'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'policy_content': 'policy_content',
        'description': 'description'
    }

    def __init__(self, policy_name=None, policy_content=None, description=None):
        """AttachCustomerManagedPolicyToPermissionSetReqBody

        The model defined in huaweicloud sdk

        :param policy_name: 策略名称
        :type policy_name: str
        :param policy_content: 策略内容
        :type policy_content: str
        :param description: 策略描述
        :type description: str
        """
        
        

        self._policy_name = None
        self._policy_content = None
        self._description = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if policy_content is not None:
            self.policy_content = policy_content
        if description is not None:
            self.description = description

    @property
    def policy_name(self):
        """Gets the policy_name of this AttachCustomerManagedPolicyToPermissionSetReqBody.

        策略名称

        :return: The policy_name of this AttachCustomerManagedPolicyToPermissionSetReqBody.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this AttachCustomerManagedPolicyToPermissionSetReqBody.

        策略名称

        :param policy_name: The policy_name of this AttachCustomerManagedPolicyToPermissionSetReqBody.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def policy_content(self):
        """Gets the policy_content of this AttachCustomerManagedPolicyToPermissionSetReqBody.

        策略内容

        :return: The policy_content of this AttachCustomerManagedPolicyToPermissionSetReqBody.
        :rtype: str
        """
        return self._policy_content

    @policy_content.setter
    def policy_content(self, policy_content):
        """Sets the policy_content of this AttachCustomerManagedPolicyToPermissionSetReqBody.

        策略内容

        :param policy_content: The policy_content of this AttachCustomerManagedPolicyToPermissionSetReqBody.
        :type policy_content: str
        """
        self._policy_content = policy_content

    @property
    def description(self):
        """Gets the description of this AttachCustomerManagedPolicyToPermissionSetReqBody.

        策略描述

        :return: The description of this AttachCustomerManagedPolicyToPermissionSetReqBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttachCustomerManagedPolicyToPermissionSetReqBody.

        策略描述

        :param description: The description of this AttachCustomerManagedPolicyToPermissionSetReqBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AttachCustomerManagedPolicyToPermissionSetReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
