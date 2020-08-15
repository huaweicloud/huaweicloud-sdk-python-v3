# coding: utf-8

import pprint
import re

import six





class InstanceAction:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action': 'InstanceActionType',
        'parameters': 'InstanceActionParameters'
    }

    attribute_map = {
        'action': 'action',
        'parameters': 'parameters'
    }

    def __init__(self, action=None, parameters=None):
        """InstanceAction - a model defined in huaweicloud sdk"""
        
        

        self._action = None
        self._parameters = None
        self.discriminator = None

        self.action = action
        if parameters is not None:
            self.parameters = parameters

    @property
    def action(self):
        """Gets the action of this InstanceAction.


        :return: The action of this InstanceAction.
        :rtype: InstanceActionType
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InstanceAction.


        :param action: The action of this InstanceAction.
        :type: InstanceActionType
        """
        self._action = action

    @property
    def parameters(self):
        """Gets the parameters of this InstanceAction.


        :return: The parameters of this InstanceAction.
        :rtype: InstanceActionParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InstanceAction.


        :param parameters: The parameters of this InstanceAction.
        :type: InstanceActionParameters
        """
        self._parameters = parameters

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
        if not isinstance(other, InstanceAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
