# coding: utf-8

import pprint
import re

import six





class KeystoneCreateUserTokenByPasswordRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'nocatalog': 'str',
        'body': 'KeystoneCreateUserTokenByPasswordRequestBody'
    }

    attribute_map = {
        'nocatalog': 'nocatalog',
        'body': 'body'
    }

    def __init__(self, nocatalog=None, body=None):
        """KeystoneCreateUserTokenByPasswordRequest - a model defined in huaweicloud sdk"""
        
        

        self._nocatalog = None
        self._body = None
        self.discriminator = None

        if nocatalog is not None:
            self.nocatalog = nocatalog
        if body is not None:
            self.body = body

    @property
    def nocatalog(self):
        """Gets the nocatalog of this KeystoneCreateUserTokenByPasswordRequest.


        :return: The nocatalog of this KeystoneCreateUserTokenByPasswordRequest.
        :rtype: str
        """
        return self._nocatalog

    @nocatalog.setter
    def nocatalog(self, nocatalog):
        """Sets the nocatalog of this KeystoneCreateUserTokenByPasswordRequest.


        :param nocatalog: The nocatalog of this KeystoneCreateUserTokenByPasswordRequest.
        :type: str
        """
        self._nocatalog = nocatalog

    @property
    def body(self):
        """Gets the body of this KeystoneCreateUserTokenByPasswordRequest.


        :return: The body of this KeystoneCreateUserTokenByPasswordRequest.
        :rtype: KeystoneCreateUserTokenByPasswordRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this KeystoneCreateUserTokenByPasswordRequest.


        :param body: The body of this KeystoneCreateUserTokenByPasswordRequest.
        :type: KeystoneCreateUserTokenByPasswordRequestBody
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
        if not isinstance(other, KeystoneCreateUserTokenByPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
