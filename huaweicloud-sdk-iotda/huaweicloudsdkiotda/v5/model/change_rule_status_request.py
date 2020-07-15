# coding: utf-8

import pprint
import re

import six





class ChangeRuleStatusRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'rule_id': 'str',
        'body': 'RuleStatus'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'rule_id': 'rule_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, rule_id=None, body=None):
        """ChangeRuleStatusRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._rule_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.rule_id = rule_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this ChangeRuleStatusRequest.


        :return: The instance_id of this ChangeRuleStatusRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ChangeRuleStatusRequest.


        :param instance_id: The instance_id of this ChangeRuleStatusRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def rule_id(self):
        """Gets the rule_id of this ChangeRuleStatusRequest.


        :return: The rule_id of this ChangeRuleStatusRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ChangeRuleStatusRequest.


        :param rule_id: The rule_id of this ChangeRuleStatusRequest.
        :type: str
        """
        self._rule_id = rule_id

    @property
    def body(self):
        """Gets the body of this ChangeRuleStatusRequest.


        :return: The body of this ChangeRuleStatusRequest.
        :rtype: RuleStatus
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ChangeRuleStatusRequest.


        :param body: The body of this ChangeRuleStatusRequest.
        :type: RuleStatus
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangeRuleStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
