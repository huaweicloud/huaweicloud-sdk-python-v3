# coding: utf-8

import pprint
import re

import six





class ShowRuleActionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('stage_auth_token')

    openapi_types = {
        'stage_auth_token': 'str',
        'instance_id': 'str',
        'action_id': 'str'
    }

    attribute_map = {
        'stage_auth_token': 'Stage-Auth-Token',
        'instance_id': 'Instance-Id',
        'action_id': 'action_id'
    }

    def __init__(self, stage_auth_token=None, instance_id=None, action_id=None):
        """ShowRuleActionRequest - a model defined in huaweicloud sdk"""
        
        

        self._stage_auth_token = None
        self._instance_id = None
        self._action_id = None
        self.discriminator = None

        if stage_auth_token is not None:
            self.stage_auth_token = stage_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        self.action_id = action_id

    @property
    def stage_auth_token(self):
        """Gets the stage_auth_token of this ShowRuleActionRequest.


        :return: The stage_auth_token of this ShowRuleActionRequest.
        :rtype: str
        """
        return self._stage_auth_token

    @stage_auth_token.setter
    def stage_auth_token(self, stage_auth_token):
        """Sets the stage_auth_token of this ShowRuleActionRequest.


        :param stage_auth_token: The stage_auth_token of this ShowRuleActionRequest.
        :type: str
        """
        self._stage_auth_token = stage_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowRuleActionRequest.


        :return: The instance_id of this ShowRuleActionRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowRuleActionRequest.


        :param instance_id: The instance_id of this ShowRuleActionRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def action_id(self):
        """Gets the action_id of this ShowRuleActionRequest.


        :return: The action_id of this ShowRuleActionRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ShowRuleActionRequest.


        :param action_id: The action_id of this ShowRuleActionRequest.
        :type: str
        """
        self._action_id = action_id

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
        if not isinstance(other, ShowRuleActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
