# coding: utf-8

import pprint
import re

import six





class ShowBuiltInPolicyDefinitionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'policy_definition_id': 'str',
        'x_language': 'str'
    }

    attribute_map = {
        'policy_definition_id': 'policy_definition_id',
        'x_language': 'X-Language'
    }

    def __init__(self, policy_definition_id=None, x_language='zh-cn'):
        """ShowBuiltInPolicyDefinitionRequest - a model defined in huaweicloud sdk"""
        
        

        self._policy_definition_id = None
        self._x_language = None
        self.discriminator = None

        self.policy_definition_id = policy_definition_id
        if x_language is not None:
            self.x_language = x_language

    @property
    def policy_definition_id(self):
        """Gets the policy_definition_id of this ShowBuiltInPolicyDefinitionRequest.


        :return: The policy_definition_id of this ShowBuiltInPolicyDefinitionRequest.
        :rtype: str
        """
        return self._policy_definition_id

    @policy_definition_id.setter
    def policy_definition_id(self, policy_definition_id):
        """Sets the policy_definition_id of this ShowBuiltInPolicyDefinitionRequest.


        :param policy_definition_id: The policy_definition_id of this ShowBuiltInPolicyDefinitionRequest.
        :type: str
        """
        self._policy_definition_id = policy_definition_id

    @property
    def x_language(self):
        """Gets the x_language of this ShowBuiltInPolicyDefinitionRequest.


        :return: The x_language of this ShowBuiltInPolicyDefinitionRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowBuiltInPolicyDefinitionRequest.


        :param x_language: The x_language of this ShowBuiltInPolicyDefinitionRequest.
        :type: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowBuiltInPolicyDefinitionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
