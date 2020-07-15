# coding: utf-8

import pprint
import re

import six





class CreateMeetingRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_uuid': 'str',
        'x_authorization_type': 'str',
        'x_site_id': 'str',
        'body': 'RestScheduleConfDTO'
    }

    attribute_map = {
        'user_uuid': 'userUUID',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id',
        'body': 'body'
    }

    def __init__(self, user_uuid=None, x_authorization_type=None, x_site_id=None, body=None):
        """CreateMeetingRequest - a model defined in huaweicloud sdk"""
        
        

        self._user_uuid = None
        self._x_authorization_type = None
        self._x_site_id = None
        self._body = None
        self.discriminator = None

        if user_uuid is not None:
            self.user_uuid = user_uuid
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id
        if body is not None:
            self.body = body

    @property
    def user_uuid(self):
        """Gets the user_uuid of this CreateMeetingRequest.


        :return: The user_uuid of this CreateMeetingRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this CreateMeetingRequest.


        :param user_uuid: The user_uuid of this CreateMeetingRequest.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this CreateMeetingRequest.


        :return: The x_authorization_type of this CreateMeetingRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this CreateMeetingRequest.


        :param x_authorization_type: The x_authorization_type of this CreateMeetingRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this CreateMeetingRequest.


        :return: The x_site_id of this CreateMeetingRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this CreateMeetingRequest.


        :param x_site_id: The x_site_id of this CreateMeetingRequest.
        :type: str
        """
        self._x_site_id = x_site_id

    @property
    def body(self):
        """Gets the body of this CreateMeetingRequest.


        :return: The body of this CreateMeetingRequest.
        :rtype: RestScheduleConfDTO
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateMeetingRequest.


        :param body: The body of this CreateMeetingRequest.
        :type: RestScheduleConfDTO
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
        if not isinstance(other, CreateMeetingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
