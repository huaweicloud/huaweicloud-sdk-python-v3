# coding: utf-8

import pprint
import re

import six





class CreateLoadBalancerRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('x_auth_project_token')

    openapi_types = {
        'x_auth_project_token': 'str',
        'body': 'CreateLoadBalancerRequestBody'
    }

    attribute_map = {
        'x_auth_project_token': 'X-Auth-Project-Token',
        'body': 'body'
    }

    def __init__(self, x_auth_project_token=None, body=None):
        """CreateLoadBalancerRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_auth_project_token = None
        self._body = None
        self.discriminator = None

        if x_auth_project_token is not None:
            self.x_auth_project_token = x_auth_project_token
        if body is not None:
            self.body = body

    @property
    def x_auth_project_token(self):
        """Gets the x_auth_project_token of this CreateLoadBalancerRequest.


        :return: The x_auth_project_token of this CreateLoadBalancerRequest.
        :rtype: str
        """
        return self._x_auth_project_token

    @x_auth_project_token.setter
    def x_auth_project_token(self, x_auth_project_token):
        """Sets the x_auth_project_token of this CreateLoadBalancerRequest.


        :param x_auth_project_token: The x_auth_project_token of this CreateLoadBalancerRequest.
        :type: str
        """
        self._x_auth_project_token = x_auth_project_token

    @property
    def body(self):
        """Gets the body of this CreateLoadBalancerRequest.


        :return: The body of this CreateLoadBalancerRequest.
        :rtype: CreateLoadBalancerRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateLoadBalancerRequest.


        :param body: The body of this CreateLoadBalancerRequest.
        :type: CreateLoadBalancerRequestBody
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
        if not isinstance(other, CreateLoadBalancerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
