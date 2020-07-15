# coding: utf-8

import pprint
import re

import six





class KeystoneListEndpointsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'interface': 'str',
        'service_id': 'str'
    }

    attribute_map = {
        'interface': 'interface',
        'service_id': 'service_id'
    }

    def __init__(self, interface=None, service_id=None):
        """KeystoneListEndpointsRequest - a model defined in huaweicloud sdk"""
        
        

        self._interface = None
        self._service_id = None
        self.discriminator = None

        if interface is not None:
            self.interface = interface
        if service_id is not None:
            self.service_id = service_id

    @property
    def interface(self):
        """Gets the interface of this KeystoneListEndpointsRequest.


        :return: The interface of this KeystoneListEndpointsRequest.
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this KeystoneListEndpointsRequest.


        :param interface: The interface of this KeystoneListEndpointsRequest.
        :type: str
        """
        self._interface = interface

    @property
    def service_id(self):
        """Gets the service_id of this KeystoneListEndpointsRequest.


        :return: The service_id of this KeystoneListEndpointsRequest.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this KeystoneListEndpointsRequest.


        :param service_id: The service_id of this KeystoneListEndpointsRequest.
        :type: str
        """
        self._service_id = service_id

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
        if not isinstance(other, KeystoneListEndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
