# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_name': 'str',
        'description': 'str',
        'policies': 'Policies'
    }

    attribute_map = {
        'policy_group_name': 'policy_group_name',
        'description': 'description',
        'policies': 'policies'
    }

    def __init__(self, policy_group_name=None, description=None, policies=None):
        """PolicyTemplate

        The model defined in huaweicloud sdk

        :param policy_group_name: 策略组名称，名称需要满足如下规则 1. 不能有空格和.开头，可以由中文、数字、英文大小写组成 2. 字符长度范围1-55
        :type policy_group_name: str
        :param description: 描述
        :type description: str
        :param policies: 
        :type policies: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        """
        
        

        self._policy_group_name = None
        self._description = None
        self._policies = None
        self.discriminator = None

        self.policy_group_name = policy_group_name
        if description is not None:
            self.description = description
        self.policies = policies

    @property
    def policy_group_name(self):
        """Gets the policy_group_name of this PolicyTemplate.

        策略组名称，名称需要满足如下规则 1. 不能有空格和.开头，可以由中文、数字、英文大小写组成 2. 字符长度范围1-55

        :return: The policy_group_name of this PolicyTemplate.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        """Sets the policy_group_name of this PolicyTemplate.

        策略组名称，名称需要满足如下规则 1. 不能有空格和.开头，可以由中文、数字、英文大小写组成 2. 字符长度范围1-55

        :param policy_group_name: The policy_group_name of this PolicyTemplate.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def description(self):
        """Gets the description of this PolicyTemplate.

        描述

        :return: The description of this PolicyTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyTemplate.

        描述

        :param description: The description of this PolicyTemplate.
        :type description: str
        """
        self._description = description

    @property
    def policies(self):
        """Gets the policies of this PolicyTemplate.

        :return: The policies of this PolicyTemplate.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PolicyTemplate.

        :param policies: The policies of this PolicyTemplate.
        :type policies: :class:`huaweicloudsdkworkspaceapp.v1.Policies`
        """
        self._policies = policies

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
        if not isinstance(other, PolicyTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
