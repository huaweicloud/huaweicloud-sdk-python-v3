# coding: utf-8

import pprint
import re

import six





class UpdateServiceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'int',
        'body': 'ServiceRequestBody'
    }

    attribute_map = {
        'service_id': 'service_id',
        'body': 'body'
    }

    def __init__(self, service_id=None, body=None):
        """UpdateServiceRequest - a model defined in huaweicloud sdk"""
        
        

        self._service_id = None
        self._body = None
        self.discriminator = None

        self.service_id = service_id
        if body is not None:
            self.body = body

    @property
    def service_id(self):
        """Gets the service_id of this UpdateServiceRequest.


        :return: The service_id of this UpdateServiceRequest.
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this UpdateServiceRequest.


        :param service_id: The service_id of this UpdateServiceRequest.
        :type: int
        """
        self._service_id = service_id

    @property
    def body(self):
        """Gets the body of this UpdateServiceRequest.


        :return: The body of this UpdateServiceRequest.
        :rtype: ServiceRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateServiceRequest.


        :param body: The body of this UpdateServiceRequest.
        :type: ServiceRequestBody
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
        if not isinstance(other, UpdateServiceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
