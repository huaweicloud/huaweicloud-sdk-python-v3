# coding: utf-8

import pprint
import re

import six





class ListMessageTemplatesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'message_template_name': 'str',
        'protocol': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'message_template_name': 'message_template_name',
        'protocol': 'protocol'
    }

    def __init__(self, offset=0, limit=100, message_template_name=None, protocol=None):
        """ListMessageTemplatesRequest - a model defined in huaweicloud sdk"""
        
        

        self._offset = None
        self._limit = None
        self._message_template_name = None
        self._protocol = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if message_template_name is not None:
            self.message_template_name = message_template_name
        self.protocol = protocol

    @property
    def offset(self):
        """Gets the offset of this ListMessageTemplatesRequest.


        :return: The offset of this ListMessageTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListMessageTemplatesRequest.


        :param offset: The offset of this ListMessageTemplatesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListMessageTemplatesRequest.


        :return: The limit of this ListMessageTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListMessageTemplatesRequest.


        :param limit: The limit of this ListMessageTemplatesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def message_template_name(self):
        """Gets the message_template_name of this ListMessageTemplatesRequest.


        :return: The message_template_name of this ListMessageTemplatesRequest.
        :rtype: str
        """
        return self._message_template_name

    @message_template_name.setter
    def message_template_name(self, message_template_name):
        """Sets the message_template_name of this ListMessageTemplatesRequest.


        :param message_template_name: The message_template_name of this ListMessageTemplatesRequest.
        :type: str
        """
        self._message_template_name = message_template_name

    @property
    def protocol(self):
        """Gets the protocol of this ListMessageTemplatesRequest.


        :return: The protocol of this ListMessageTemplatesRequest.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ListMessageTemplatesRequest.


        :param protocol: The protocol of this ListMessageTemplatesRequest.
        :type: str
        """
        self._protocol = protocol

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
        if not isinstance(other, ListMessageTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
