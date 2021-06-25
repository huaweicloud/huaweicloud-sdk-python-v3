# coding: utf-8

import pprint
import re

import six





class CreateGeoipRulesRequest:


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
        'body': 'GeoIpBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'body': 'body'
    }

    def __init__(self, policy_id=None, body=None):
        """CreateGeoipRulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._policy_id = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        """Gets the policy_id of this CreateGeoipRulesRequest.

        policyid

        :return: The policy_id of this CreateGeoipRulesRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this CreateGeoipRulesRequest.

        policyid

        :param policy_id: The policy_id of this CreateGeoipRulesRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def body(self):
        """Gets the body of this CreateGeoipRulesRequest.


        :return: The body of this CreateGeoipRulesRequest.
        :rtype: GeoIpBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateGeoipRulesRequest.


        :param body: The body of this CreateGeoipRulesRequest.
        :type: GeoIpBody
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
        if not isinstance(other, CreateGeoipRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other