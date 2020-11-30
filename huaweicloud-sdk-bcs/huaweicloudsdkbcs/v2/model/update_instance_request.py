# coding: utf-8

import pprint
import re

import six





class UpdateInstanceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'body': 'UpdateInstanceRequestBody'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'body': 'body'
    }

    def __init__(self, blockchain_id=None, body=None):
        """UpdateInstanceRequest - a model defined in huaweicloud sdk"""
        
        

        self._blockchain_id = None
        self._body = None
        self.discriminator = None

        self.blockchain_id = blockchain_id
        if body is not None:
            self.body = body

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this UpdateInstanceRequest.


        :return: The blockchain_id of this UpdateInstanceRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this UpdateInstanceRequest.


        :param blockchain_id: The blockchain_id of this UpdateInstanceRequest.
        :type: str
        """
        self._blockchain_id = blockchain_id

    @property
    def body(self):
        """Gets the body of this UpdateInstanceRequest.


        :return: The body of this UpdateInstanceRequest.
        :rtype: UpdateInstanceRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateInstanceRequest.


        :param body: The body of this UpdateInstanceRequest.
        :type: UpdateInstanceRequestBody
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
        if not isinstance(other, UpdateInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
