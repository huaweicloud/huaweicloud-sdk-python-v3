# coding: utf-8

import pprint
import re

import six





class PoolInfoResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'option': 'PremiumWafPoolOption',
        'hosts': 'list[IdNameEntry]',
        'instances': 'list[IdNameEntry]',
        'bindings': 'list[IdNameEntry]'
    }

    attribute_map = {
        'option': 'option',
        'hosts': 'hosts',
        'instances': 'instances',
        'bindings': 'bindings'
    }

    def __init__(self, option=None, hosts=None, instances=None, bindings=None):
        """PoolInfoResponse - a model defined in huaweicloud sdk"""
        
        

        self._option = None
        self._hosts = None
        self._instances = None
        self._bindings = None
        self.discriminator = None

        if option is not None:
            self.option = option
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances
        if bindings is not None:
            self.bindings = bindings

    @property
    def option(self):
        """Gets the option of this PoolInfoResponse.


        :return: The option of this PoolInfoResponse.
        :rtype: PremiumWafPoolOption
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this PoolInfoResponse.


        :param option: The option of this PoolInfoResponse.
        :type: PremiumWafPoolOption
        """
        self._option = option

    @property
    def hosts(self):
        """Gets the hosts of this PoolInfoResponse.

        关联的域名

        :return: The hosts of this PoolInfoResponse.
        :rtype: list[IdNameEntry]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this PoolInfoResponse.

        关联的域名

        :param hosts: The hosts of this PoolInfoResponse.
        :type: list[IdNameEntry]
        """
        self._hosts = hosts

    @property
    def instances(self):
        """Gets the instances of this PoolInfoResponse.

        组内的独享引擎

        :return: The instances of this PoolInfoResponse.
        :rtype: list[IdNameEntry]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this PoolInfoResponse.

        组内的独享引擎

        :param instances: The instances of this PoolInfoResponse.
        :type: list[IdNameEntry]
        """
        self._instances = instances

    @property
    def bindings(self):
        """Gets the bindings of this PoolInfoResponse.

        绑定的LoadBalancer

        :return: The bindings of this PoolInfoResponse.
        :rtype: list[IdNameEntry]
        """
        return self._bindings

    @bindings.setter
    def bindings(self, bindings):
        """Sets the bindings of this PoolInfoResponse.

        绑定的LoadBalancer

        :param bindings: The bindings of this PoolInfoResponse.
        :type: list[IdNameEntry]
        """
        self._bindings = bindings

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
        if not isinstance(other, PoolInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other