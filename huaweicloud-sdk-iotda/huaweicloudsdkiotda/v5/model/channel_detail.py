# coding: utf-8

import pprint
import re

import six





class ChannelDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'http_forwarding': 'HttpForwarding',
        'amqp_forwarding': 'AmqpForwarding'
    }

    attribute_map = {
        'http_forwarding': 'http_forwarding',
        'amqp_forwarding': 'amqp_forwarding'
    }

    def __init__(self, http_forwarding=None, amqp_forwarding=None):
        """ChannelDetail - a model defined in huaweicloud sdk"""
        
        

        self._http_forwarding = None
        self._amqp_forwarding = None
        self.discriminator = None

        if http_forwarding is not None:
            self.http_forwarding = http_forwarding
        if amqp_forwarding is not None:
            self.amqp_forwarding = amqp_forwarding

    @property
    def http_forwarding(self):
        """Gets the http_forwarding of this ChannelDetail.


        :return: The http_forwarding of this ChannelDetail.
        :rtype: HttpForwarding
        """
        return self._http_forwarding

    @http_forwarding.setter
    def http_forwarding(self, http_forwarding):
        """Sets the http_forwarding of this ChannelDetail.


        :param http_forwarding: The http_forwarding of this ChannelDetail.
        :type: HttpForwarding
        """
        self._http_forwarding = http_forwarding

    @property
    def amqp_forwarding(self):
        """Gets the amqp_forwarding of this ChannelDetail.


        :return: The amqp_forwarding of this ChannelDetail.
        :rtype: AmqpForwarding
        """
        return self._amqp_forwarding

    @amqp_forwarding.setter
    def amqp_forwarding(self, amqp_forwarding):
        """Sets the amqp_forwarding of this ChannelDetail.


        :param amqp_forwarding: The amqp_forwarding of this ChannelDetail.
        :type: AmqpForwarding
        """
        self._amqp_forwarding = amqp_forwarding

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
        if not isinstance(other, ChannelDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
