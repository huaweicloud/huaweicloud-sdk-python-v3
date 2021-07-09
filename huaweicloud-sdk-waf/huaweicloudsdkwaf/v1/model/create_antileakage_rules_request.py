# coding: utf-8

import re
import six





class CreateAntileakageRulesRequest:


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
        'body': 'CreateAntiLeakageRequestBody'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'body': 'body'
    }

    def __init__(self, policy_id=None, body=None):
        """CreateAntileakageRulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._policy_id = None
        self._body = None
        self.discriminator = None

        self.policy_id = policy_id
        if body is not None:
            self.body = body

    @property
    def policy_id(self):
        """Gets the policy_id of this CreateAntileakageRulesRequest.

        policyid

        :return: The policy_id of this CreateAntileakageRulesRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this CreateAntileakageRulesRequest.

        policyid

        :param policy_id: The policy_id of this CreateAntileakageRulesRequest.
        :type: str
        """
        self._policy_id = policy_id

    @property
    def body(self):
        """Gets the body of this CreateAntileakageRulesRequest.


        :return: The body of this CreateAntileakageRulesRequest.
        :rtype: CreateAntiLeakageRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateAntileakageRulesRequest.


        :param body: The body of this CreateAntileakageRulesRequest.
        :type: CreateAntiLeakageRequestBody
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateAntileakageRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
