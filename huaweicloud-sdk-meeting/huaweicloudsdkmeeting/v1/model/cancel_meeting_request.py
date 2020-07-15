# coding: utf-8

import pprint
import re

import six





class CancelMeetingRequest:


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
        'user_uuid': 'str',
        'type': 'int',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'user_uuid': 'userUUID',
        'type': 'type',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, conference_id=None, user_uuid=None, type=None, x_authorization_type=None, x_site_id=None):
        """CancelMeetingRequest - a model defined in huaweicloud sdk"""
        
        

        self._conference_id = None
        self._user_uuid = None
        self._type = None
        self._x_authorization_type = None
        self._x_site_id = None
        self.discriminator = None

        self.conference_id = conference_id
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if type is not None:
            self.type = type
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def conference_id(self):
        """Gets the conference_id of this CancelMeetingRequest.


        :return: The conference_id of this CancelMeetingRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this CancelMeetingRequest.


        :param conference_id: The conference_id of this CancelMeetingRequest.
        :type: str
        """
        self._conference_id = conference_id

    @property
    def user_uuid(self):
        """Gets the user_uuid of this CancelMeetingRequest.


        :return: The user_uuid of this CancelMeetingRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this CancelMeetingRequest.


        :param user_uuid: The user_uuid of this CancelMeetingRequest.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def type(self):
        """Gets the type of this CancelMeetingRequest.


        :return: The type of this CancelMeetingRequest.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CancelMeetingRequest.


        :param type: The type of this CancelMeetingRequest.
        :type: int
        """
        self._type = type

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this CancelMeetingRequest.


        :return: The x_authorization_type of this CancelMeetingRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this CancelMeetingRequest.


        :param x_authorization_type: The x_authorization_type of this CancelMeetingRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this CancelMeetingRequest.


        :return: The x_site_id of this CancelMeetingRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this CancelMeetingRequest.


        :param x_site_id: The x_site_id of this CancelMeetingRequest.
        :type: str
        """
        self._x_site_id = x_site_id

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
        if not isinstance(other, CancelMeetingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
