# coding: utf-8

import pprint
import re

import six





class AgencyPolicyStatement:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action': 'list[str]',
        'effect': 'str',
        'resource': 'AgencyPolicyResource'
    }

    attribute_map = {
        'action': 'Action',
        'effect': 'Effect',
        'resource': 'Resource'
    }

    def __init__(self, action=None, effect=None, resource=None):
        """AgencyPolicyStatement - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._effect = None
        self._resource = None
        self.discriminator = None

        self.action = action
        self.effect = effect
        self.resource = resource

    @property
    def action(self):
        """Gets the action of this AgencyPolicyStatement.

        授权项，指对资源的具体操作权限。   > - 当自定义策略为委托自定义策略时，该字段值为：``` \"Action\": [\"iam:agencies:assume\"]```。

        :return: The action of this AgencyPolicyStatement.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AgencyPolicyStatement.

        授权项，指对资源的具体操作权限。   > - 当自定义策略为委托自定义策略时，该字段值为：``` \"Action\": [\"iam:agencies:assume\"]```。

        :param action: The action of this AgencyPolicyStatement.
        :type: list[str]
        """
        self._action = action

    @property
    def effect(self):
        """Gets the effect of this AgencyPolicyStatement.

        作用。包含两种：允许（Allow）和拒绝（Deny），既有Allow又有Deny的授权语句时，遵循Deny优先的原则。

        :return: The effect of this AgencyPolicyStatement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this AgencyPolicyStatement.

        作用。包含两种：允许（Allow）和拒绝（Deny），既有Allow又有Deny的授权语句时，遵循Deny优先的原则。

        :param effect: The effect of this AgencyPolicyStatement.
        :type: str
        """
        self._effect = effect

    @property
    def resource(self):
        """Gets the resource of this AgencyPolicyStatement.


        :return: The resource of this AgencyPolicyStatement.
        :rtype: AgencyPolicyResource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this AgencyPolicyStatement.


        :param resource: The resource of this AgencyPolicyStatement.
        :type: AgencyPolicyResource
        """
        self._resource = resource

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AgencyPolicyStatement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
