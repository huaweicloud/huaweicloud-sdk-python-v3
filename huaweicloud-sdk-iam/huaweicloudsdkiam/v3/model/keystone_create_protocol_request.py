# coding: utf-8

import pprint
import re

import six





class KeystoneCreateProtocolRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'idp_id': 'str',
        'protocol_id': 'str',
        'body': 'KeystoneCreateProtocolRequestBody'
    }

    attribute_map = {
        'idp_id': 'idp_id',
        'protocol_id': 'protocol_id',
        'body': 'body'
    }

    def __init__(self, idp_id=None, protocol_id=None, body=None):
        """KeystoneCreateProtocolRequest - a model defined in huaweicloud sdk"""
        
        

        self._idp_id = None
        self._protocol_id = None
        self._body = None
        self.discriminator = None

        self.idp_id = idp_id
        self.protocol_id = protocol_id
        if body is not None:
            self.body = body

    @property
    def idp_id(self):
        """Gets the idp_id of this KeystoneCreateProtocolRequest.


        :return: The idp_id of this KeystoneCreateProtocolRequest.
        :rtype: str
        """
        return self._idp_id

    @idp_id.setter
    def idp_id(self, idp_id):
        """Sets the idp_id of this KeystoneCreateProtocolRequest.


        :param idp_id: The idp_id of this KeystoneCreateProtocolRequest.
        :type: str
        """
        self._idp_id = idp_id

    @property
    def protocol_id(self):
        """Gets the protocol_id of this KeystoneCreateProtocolRequest.


        :return: The protocol_id of this KeystoneCreateProtocolRequest.
        :rtype: str
        """
        return self._protocol_id

    @protocol_id.setter
    def protocol_id(self, protocol_id):
        """Sets the protocol_id of this KeystoneCreateProtocolRequest.


        :param protocol_id: The protocol_id of this KeystoneCreateProtocolRequest.
        :type: str
        """
        self._protocol_id = protocol_id

    @property
    def body(self):
        """Gets the body of this KeystoneCreateProtocolRequest.


        :return: The body of this KeystoneCreateProtocolRequest.
        :rtype: KeystoneCreateProtocolRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this KeystoneCreateProtocolRequest.


        :param body: The body of this KeystoneCreateProtocolRequest.
        :type: KeystoneCreateProtocolRequestBody
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
        if not isinstance(other, KeystoneCreateProtocolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
