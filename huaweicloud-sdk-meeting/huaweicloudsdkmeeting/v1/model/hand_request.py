# coding: utf-8

import pprint
import re

import six





class HandRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conference_id': 'str',
        'participant_id': 'str',
        'x_conference_authorization': 'str',
        'body': 'RestHandsUpReqBody'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'participant_id': 'participantID',
        'x_conference_authorization': 'X-Conference-Authorization',
        'body': 'body'
    }

    def __init__(self, conference_id=None, participant_id=None, x_conference_authorization=None, body=None):
        """HandRequest - a model defined in huaweicloud sdk"""
        
        

        self._conference_id = None
        self._participant_id = None
        self._x_conference_authorization = None
        self._body = None
        self.discriminator = None

        self.conference_id = conference_id
        self.participant_id = participant_id
        self.x_conference_authorization = x_conference_authorization
        if body is not None:
            self.body = body

    @property
    def conference_id(self):
        """Gets the conference_id of this HandRequest.


        :return: The conference_id of this HandRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this HandRequest.


        :param conference_id: The conference_id of this HandRequest.
        :type: str
        """
        self._conference_id = conference_id

    @property
    def participant_id(self):
        """Gets the participant_id of this HandRequest.


        :return: The participant_id of this HandRequest.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        """Sets the participant_id of this HandRequest.


        :param participant_id: The participant_id of this HandRequest.
        :type: str
        """
        self._participant_id = participant_id

    @property
    def x_conference_authorization(self):
        """Gets the x_conference_authorization of this HandRequest.


        :return: The x_conference_authorization of this HandRequest.
        :rtype: str
        """
        return self._x_conference_authorization

    @x_conference_authorization.setter
    def x_conference_authorization(self, x_conference_authorization):
        """Sets the x_conference_authorization of this HandRequest.


        :param x_conference_authorization: The x_conference_authorization of this HandRequest.
        :type: str
        """
        self._x_conference_authorization = x_conference_authorization

    @property
    def body(self):
        """Gets the body of this HandRequest.


        :return: The body of this HandRequest.
        :rtype: RestHandsUpReqBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this HandRequest.


        :param body: The body of this HandRequest.
        :type: RestHandsUpReqBody
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
        if not isinstance(other, HandRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
