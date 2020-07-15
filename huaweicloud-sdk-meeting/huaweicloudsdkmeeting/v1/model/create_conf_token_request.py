# coding: utf-8

import pprint
import re

import six





class CreateConfTokenRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('x_password')

    openapi_types = {
        'conference_id': 'str',
        'x_conference_authorization': 'str',
        'x_password': 'str',
        'x_login_type': 'int',
        'x_nonce': 'str'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'x_conference_authorization': 'X-Conference-Authorization',
        'x_password': 'X-Password',
        'x_login_type': 'X-Login-Type',
        'x_nonce': 'X-Nonce'
    }

    def __init__(self, conference_id=None, x_conference_authorization=None, x_password=None, x_login_type=None, x_nonce=None):
        """CreateConfTokenRequest - a model defined in huaweicloud sdk"""
        
        

        self._conference_id = None
        self._x_conference_authorization = None
        self._x_password = None
        self._x_login_type = None
        self._x_nonce = None
        self.discriminator = None

        self.conference_id = conference_id
        if x_conference_authorization is not None:
            self.x_conference_authorization = x_conference_authorization
        self.x_password = x_password
        self.x_login_type = x_login_type
        if x_nonce is not None:
            self.x_nonce = x_nonce

    @property
    def conference_id(self):
        """Gets the conference_id of this CreateConfTokenRequest.


        :return: The conference_id of this CreateConfTokenRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this CreateConfTokenRequest.


        :param conference_id: The conference_id of this CreateConfTokenRequest.
        :type: str
        """
        self._conference_id = conference_id

    @property
    def x_conference_authorization(self):
        """Gets the x_conference_authorization of this CreateConfTokenRequest.


        :return: The x_conference_authorization of this CreateConfTokenRequest.
        :rtype: str
        """
        return self._x_conference_authorization

    @x_conference_authorization.setter
    def x_conference_authorization(self, x_conference_authorization):
        """Sets the x_conference_authorization of this CreateConfTokenRequest.


        :param x_conference_authorization: The x_conference_authorization of this CreateConfTokenRequest.
        :type: str
        """
        self._x_conference_authorization = x_conference_authorization

    @property
    def x_password(self):
        """Gets the x_password of this CreateConfTokenRequest.


        :return: The x_password of this CreateConfTokenRequest.
        :rtype: str
        """
        return self._x_password

    @x_password.setter
    def x_password(self, x_password):
        """Sets the x_password of this CreateConfTokenRequest.


        :param x_password: The x_password of this CreateConfTokenRequest.
        :type: str
        """
        self._x_password = x_password

    @property
    def x_login_type(self):
        """Gets the x_login_type of this CreateConfTokenRequest.


        :return: The x_login_type of this CreateConfTokenRequest.
        :rtype: int
        """
        return self._x_login_type

    @x_login_type.setter
    def x_login_type(self, x_login_type):
        """Sets the x_login_type of this CreateConfTokenRequest.


        :param x_login_type: The x_login_type of this CreateConfTokenRequest.
        :type: int
        """
        self._x_login_type = x_login_type

    @property
    def x_nonce(self):
        """Gets the x_nonce of this CreateConfTokenRequest.


        :return: The x_nonce of this CreateConfTokenRequest.
        :rtype: str
        """
        return self._x_nonce

    @x_nonce.setter
    def x_nonce(self, x_nonce):
        """Sets the x_nonce of this CreateConfTokenRequest.


        :param x_nonce: The x_nonce of this CreateConfTokenRequest.
        :type: str
        """
        self._x_nonce = x_nonce

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
        if not isinstance(other, CreateConfTokenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
