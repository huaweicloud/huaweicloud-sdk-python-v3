# coding: utf-8

import pprint
import re

import six





class InstanceActionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resize_flavor': 'ResizeFlavorRequest',
        'enlarge_volume': 'EnlargeVolume',
        'restart': 'InstanceActionRequestRestart',
        'single_to_ha': 'Single2Ha'
    }

    attribute_map = {
        'resize_flavor': 'resize_flavor',
        'enlarge_volume': 'enlarge_volume',
        'restart': 'restart',
        'single_to_ha': 'single_to_ha'
    }

    def __init__(self, resize_flavor=None, enlarge_volume=None, restart=None, single_to_ha=None):
        """InstanceActionRequest - a model defined in huaweicloud sdk"""
        
        

        self._resize_flavor = None
        self._enlarge_volume = None
        self._restart = None
        self._single_to_ha = None
        self.discriminator = None

        if resize_flavor is not None:
            self.resize_flavor = resize_flavor
        if enlarge_volume is not None:
            self.enlarge_volume = enlarge_volume
        if restart is not None:
            self.restart = restart
        if single_to_ha is not None:
            self.single_to_ha = single_to_ha

    @property
    def resize_flavor(self):
        """Gets the resize_flavor of this InstanceActionRequest.


        :return: The resize_flavor of this InstanceActionRequest.
        :rtype: ResizeFlavorRequest
        """
        return self._resize_flavor

    @resize_flavor.setter
    def resize_flavor(self, resize_flavor):
        """Sets the resize_flavor of this InstanceActionRequest.


        :param resize_flavor: The resize_flavor of this InstanceActionRequest.
        :type: ResizeFlavorRequest
        """
        self._resize_flavor = resize_flavor

    @property
    def enlarge_volume(self):
        """Gets the enlarge_volume of this InstanceActionRequest.


        :return: The enlarge_volume of this InstanceActionRequest.
        :rtype: EnlargeVolume
        """
        return self._enlarge_volume

    @enlarge_volume.setter
    def enlarge_volume(self, enlarge_volume):
        """Sets the enlarge_volume of this InstanceActionRequest.


        :param enlarge_volume: The enlarge_volume of this InstanceActionRequest.
        :type: EnlargeVolume
        """
        self._enlarge_volume = enlarge_volume

    @property
    def restart(self):
        """Gets the restart of this InstanceActionRequest.


        :return: The restart of this InstanceActionRequest.
        :rtype: InstanceActionRequestRestart
        """
        return self._restart

    @restart.setter
    def restart(self, restart):
        """Sets the restart of this InstanceActionRequest.


        :param restart: The restart of this InstanceActionRequest.
        :type: InstanceActionRequestRestart
        """
        self._restart = restart

    @property
    def single_to_ha(self):
        """Gets the single_to_ha of this InstanceActionRequest.


        :return: The single_to_ha of this InstanceActionRequest.
        :rtype: Single2Ha
        """
        return self._single_to_ha

    @single_to_ha.setter
    def single_to_ha(self, single_to_ha):
        """Sets the single_to_ha of this InstanceActionRequest.


        :param single_to_ha: The single_to_ha of this InstanceActionRequest.
        :type: Single2Ha
        """
        self._single_to_ha = single_to_ha

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
        if not isinstance(other, InstanceActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
