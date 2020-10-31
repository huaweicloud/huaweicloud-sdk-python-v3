# coding: utf-8

import pprint
import re

import six





class CountPreoccupyIpNumRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone_id': 'list[str]',
        'ip_target_enable': 'bool',
        'ip_version': 'int',
        'l7_flavor_id': 'str',
        'loadbalancer_id': 'str'
    }

    attribute_map = {
        'availability_zone_id': 'availability_zone_id',
        'ip_target_enable': 'ip_target_enable',
        'ip_version': 'ip_version',
        'l7_flavor_id': 'l7_flavor_id',
        'loadbalancer_id': 'loadbalancer_id'
    }

    def __init__(self, availability_zone_id=None, ip_target_enable=False, ip_version=None, l7_flavor_id=None, loadbalancer_id=None):
        """CountPreoccupyIpNumRequest - a model defined in huaweicloud sdk"""
        
        

        self._availability_zone_id = None
        self._ip_target_enable = None
        self._ip_version = None
        self._l7_flavor_id = None
        self._loadbalancer_id = None
        self.discriminator = None

        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if ip_target_enable is not None:
            self.ip_target_enable = ip_target_enable
        if ip_version is not None:
            self.ip_version = ip_version
        if l7_flavor_id is not None:
            self.l7_flavor_id = l7_flavor_id
        if loadbalancer_id is not None:
            self.loadbalancer_id = loadbalancer_id

    @property
    def availability_zone_id(self):
        """Gets the availability_zone_id of this CountPreoccupyIpNumRequest.


        :return: The availability_zone_id of this CountPreoccupyIpNumRequest.
        :rtype: list[str]
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        """Sets the availability_zone_id of this CountPreoccupyIpNumRequest.


        :param availability_zone_id: The availability_zone_id of this CountPreoccupyIpNumRequest.
        :type: list[str]
        """
        self._availability_zone_id = availability_zone_id

    @property
    def ip_target_enable(self):
        """Gets the ip_target_enable of this CountPreoccupyIpNumRequest.


        :return: The ip_target_enable of this CountPreoccupyIpNumRequest.
        :rtype: bool
        """
        return self._ip_target_enable

    @ip_target_enable.setter
    def ip_target_enable(self, ip_target_enable):
        """Sets the ip_target_enable of this CountPreoccupyIpNumRequest.


        :param ip_target_enable: The ip_target_enable of this CountPreoccupyIpNumRequest.
        :type: bool
        """
        self._ip_target_enable = ip_target_enable

    @property
    def ip_version(self):
        """Gets the ip_version of this CountPreoccupyIpNumRequest.


        :return: The ip_version of this CountPreoccupyIpNumRequest.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CountPreoccupyIpNumRequest.


        :param ip_version: The ip_version of this CountPreoccupyIpNumRequest.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def l7_flavor_id(self):
        """Gets the l7_flavor_id of this CountPreoccupyIpNumRequest.


        :return: The l7_flavor_id of this CountPreoccupyIpNumRequest.
        :rtype: str
        """
        return self._l7_flavor_id

    @l7_flavor_id.setter
    def l7_flavor_id(self, l7_flavor_id):
        """Sets the l7_flavor_id of this CountPreoccupyIpNumRequest.


        :param l7_flavor_id: The l7_flavor_id of this CountPreoccupyIpNumRequest.
        :type: str
        """
        self._l7_flavor_id = l7_flavor_id

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this CountPreoccupyIpNumRequest.


        :return: The loadbalancer_id of this CountPreoccupyIpNumRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this CountPreoccupyIpNumRequest.


        :param loadbalancer_id: The loadbalancer_id of this CountPreoccupyIpNumRequest.
        :type: str
        """
        self._loadbalancer_id = loadbalancer_id

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
        if not isinstance(other, CountPreoccupyIpNumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
