# coding: utf-8

import pprint
import re

import six





class UpdateDeviceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'sn': 'str',
        'body': 'ModDeviceDTO'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'sn': 'sn',
        'body': 'body'
    }

    def __init__(self, x_request_id=None, accept_language=None, sn=None, body=None):
        """UpdateDeviceRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_request_id = None
        self._accept_language = None
        self._sn = None
        self._body = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        self.sn = sn
        if body is not None:
            self.body = body

    @property
    def x_request_id(self):
        """Gets the x_request_id of this UpdateDeviceRequest.


        :return: The x_request_id of this UpdateDeviceRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this UpdateDeviceRequest.


        :param x_request_id: The x_request_id of this UpdateDeviceRequest.
        :type: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this UpdateDeviceRequest.


        :return: The accept_language of this UpdateDeviceRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this UpdateDeviceRequest.


        :param accept_language: The accept_language of this UpdateDeviceRequest.
        :type: str
        """
        self._accept_language = accept_language

    @property
    def sn(self):
        """Gets the sn of this UpdateDeviceRequest.


        :return: The sn of this UpdateDeviceRequest.
        :rtype: str
        """
        return self._sn

    @sn.setter
    def sn(self, sn):
        """Sets the sn of this UpdateDeviceRequest.


        :param sn: The sn of this UpdateDeviceRequest.
        :type: str
        """
        self._sn = sn

    @property
    def body(self):
        """Gets the body of this UpdateDeviceRequest.


        :return: The body of this UpdateDeviceRequest.
        :rtype: ModDeviceDTO
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDeviceRequest.


        :param body: The body of this UpdateDeviceRequest.
        :type: ModDeviceDTO
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
        if not isinstance(other, UpdateDeviceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
