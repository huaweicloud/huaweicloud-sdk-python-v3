# coding: utf-8

import pprint
import re

import six





class CreateUnscopeTokenByIdpInitiatedRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_idp_id': 'str',
        'body': 'object'
    }

    attribute_map = {
        'x_idp_id': 'X-Idp-Id',
        'body': 'body'
    }

    def __init__(self, x_idp_id=None, body=None):
        """CreateUnscopeTokenByIdpInitiatedRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_idp_id = None
        self._body = None
        self.discriminator = None

        self.x_idp_id = x_idp_id
        if body is not None:
            self.body = body

    @property
    def x_idp_id(self):
        """Gets the x_idp_id of this CreateUnscopeTokenByIdpInitiatedRequest.


        :return: The x_idp_id of this CreateUnscopeTokenByIdpInitiatedRequest.
        :rtype: str
        """
        return self._x_idp_id

    @x_idp_id.setter
    def x_idp_id(self, x_idp_id):
        """Sets the x_idp_id of this CreateUnscopeTokenByIdpInitiatedRequest.


        :param x_idp_id: The x_idp_id of this CreateUnscopeTokenByIdpInitiatedRequest.
        :type: str
        """
        self._x_idp_id = x_idp_id

    @property
    def body(self):
        """Gets the body of this CreateUnscopeTokenByIdpInitiatedRequest.


        :return: The body of this CreateUnscopeTokenByIdpInitiatedRequest.
        :rtype: object
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateUnscopeTokenByIdpInitiatedRequest.


        :param body: The body of this CreateUnscopeTokenByIdpInitiatedRequest.
        :type: object
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
        if not isinstance(other, CreateUnscopeTokenByIdpInitiatedRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
