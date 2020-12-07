# coding: utf-8

import pprint
import re

import six





class UpdateTopicAttributeRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'name': 'str',
        'body': 'UpdateTopicAttributeRequestBody'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'name': 'name',
        'body': 'body'
    }

    def __init__(self, topic_urn=None, name=None, body=None):
        """UpdateTopicAttributeRequest - a model defined in huaweicloud sdk"""
        
        

        self._topic_urn = None
        self._name = None
        self._body = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.name = name
        if body is not None:
            self.body = body

    @property
    def topic_urn(self):
        """Gets the topic_urn of this UpdateTopicAttributeRequest.


        :return: The topic_urn of this UpdateTopicAttributeRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this UpdateTopicAttributeRequest.


        :param topic_urn: The topic_urn of this UpdateTopicAttributeRequest.
        :type: str
        """
        self._topic_urn = topic_urn

    @property
    def name(self):
        """Gets the name of this UpdateTopicAttributeRequest.


        :return: The name of this UpdateTopicAttributeRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTopicAttributeRequest.


        :param name: The name of this UpdateTopicAttributeRequest.
        :type: str
        """
        self._name = name

    @property
    def body(self):
        """Gets the body of this UpdateTopicAttributeRequest.


        :return: The body of this UpdateTopicAttributeRequest.
        :rtype: UpdateTopicAttributeRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateTopicAttributeRequest.


        :param body: The body of this UpdateTopicAttributeRequest.
        :type: UpdateTopicAttributeRequestBody
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
        if not isinstance(other, UpdateTopicAttributeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
