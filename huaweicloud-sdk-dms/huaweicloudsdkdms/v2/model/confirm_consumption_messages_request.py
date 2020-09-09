# coding: utf-8

import pprint
import re

import six





class ConfirmConsumptionMessagesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'queue_id': 'str',
        'consumer_group_id': 'str',
        'body': 'ConfirmConsumptionMessagesReq'
    }

    attribute_map = {
        'queue_id': 'queue_id',
        'consumer_group_id': 'consumer_group_id',
        'body': 'body'
    }

    def __init__(self, queue_id=None, consumer_group_id=None, body=None):
        """ConfirmConsumptionMessagesRequest - a model defined in huaweicloud sdk"""
        
        

        self._queue_id = None
        self._consumer_group_id = None
        self._body = None
        self.discriminator = None

        self.queue_id = queue_id
        self.consumer_group_id = consumer_group_id
        if body is not None:
            self.body = body

    @property
    def queue_id(self):
        """Gets the queue_id of this ConfirmConsumptionMessagesRequest.


        :return: The queue_id of this ConfirmConsumptionMessagesRequest.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this ConfirmConsumptionMessagesRequest.


        :param queue_id: The queue_id of this ConfirmConsumptionMessagesRequest.
        :type: str
        """
        self._queue_id = queue_id

    @property
    def consumer_group_id(self):
        """Gets the consumer_group_id of this ConfirmConsumptionMessagesRequest.


        :return: The consumer_group_id of this ConfirmConsumptionMessagesRequest.
        :rtype: str
        """
        return self._consumer_group_id

    @consumer_group_id.setter
    def consumer_group_id(self, consumer_group_id):
        """Sets the consumer_group_id of this ConfirmConsumptionMessagesRequest.


        :param consumer_group_id: The consumer_group_id of this ConfirmConsumptionMessagesRequest.
        :type: str
        """
        self._consumer_group_id = consumer_group_id

    @property
    def body(self):
        """Gets the body of this ConfirmConsumptionMessagesRequest.


        :return: The body of this ConfirmConsumptionMessagesRequest.
        :rtype: ConfirmConsumptionMessagesReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ConfirmConsumptionMessagesRequest.


        :param body: The body of this ConfirmConsumptionMessagesRequest.
        :type: ConfirmConsumptionMessagesReq
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
        if not isinstance(other, ConfirmConsumptionMessagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
