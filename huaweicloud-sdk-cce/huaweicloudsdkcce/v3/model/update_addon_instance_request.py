# coding: utf-8

import pprint
import re

import six





class UpdateAddonInstanceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'content_type': 'str',
        'body': 'InstanceRequest'
    }

    attribute_map = {
        'id': 'id',
        'content_type': 'Content-Type',
        'body': 'body'
    }

    def __init__(self, id=None, content_type='application/json', body=None):
        """UpdateAddonInstanceRequest - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._content_type = None
        self._body = None
        self.discriminator = None

        self.id = id
        self.content_type = content_type
        if body is not None:
            self.body = body

    @property
    def id(self):
        """Gets the id of this UpdateAddonInstanceRequest.


        :return: The id of this UpdateAddonInstanceRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateAddonInstanceRequest.


        :param id: The id of this UpdateAddonInstanceRequest.
        :type: str
        """
        self._id = id

    @property
    def content_type(self):
        """Gets the content_type of this UpdateAddonInstanceRequest.


        :return: The content_type of this UpdateAddonInstanceRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this UpdateAddonInstanceRequest.


        :param content_type: The content_type of this UpdateAddonInstanceRequest.
        :type: str
        """
        self._content_type = content_type

    @property
    def body(self):
        """Gets the body of this UpdateAddonInstanceRequest.


        :return: The body of this UpdateAddonInstanceRequest.
        :rtype: InstanceRequest
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateAddonInstanceRequest.


        :param body: The body of this UpdateAddonInstanceRequest.
        :type: InstanceRequest
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
        if not isinstance(other, UpdateAddonInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
