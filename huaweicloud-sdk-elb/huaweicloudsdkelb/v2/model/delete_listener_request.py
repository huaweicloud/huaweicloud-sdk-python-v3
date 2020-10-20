# coding: utf-8

import pprint
import re

import six





class DeleteListenerRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cascade': 'bool',
        'listener_id': 'str'
    }

    attribute_map = {
        'cascade': 'cascade',
        'listener_id': 'listener_id'
    }

    def __init__(self, cascade=None, listener_id=None):
        """DeleteListenerRequest - a model defined in huaweicloud sdk"""
        
        

        self._cascade = None
        self._listener_id = None
        self.discriminator = None

        if cascade is not None:
            self.cascade = cascade
        self.listener_id = listener_id

    @property
    def cascade(self):
        """Gets the cascade of this DeleteListenerRequest.


        :return: The cascade of this DeleteListenerRequest.
        :rtype: bool
        """
        return self._cascade

    @cascade.setter
    def cascade(self, cascade):
        """Sets the cascade of this DeleteListenerRequest.


        :param cascade: The cascade of this DeleteListenerRequest.
        :type: bool
        """
        self._cascade = cascade

    @property
    def listener_id(self):
        """Gets the listener_id of this DeleteListenerRequest.


        :return: The listener_id of this DeleteListenerRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this DeleteListenerRequest.


        :param listener_id: The listener_id of this DeleteListenerRequest.
        :type: str
        """
        self._listener_id = listener_id

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
        if not isinstance(other, DeleteListenerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
