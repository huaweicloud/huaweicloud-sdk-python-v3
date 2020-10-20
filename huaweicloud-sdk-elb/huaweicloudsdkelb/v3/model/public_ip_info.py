# coding: utf-8

import pprint
import re

import six





class PublicIpInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publicip_id': 'str',
        'publicip_address': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'publicip_id': 'publicip_id',
        'publicip_address': 'publicip_address',
        'ip_version': 'ip_version'
    }

    def __init__(self, publicip_id=None, publicip_address=None, ip_version=None):
        """PublicIpInfo - a model defined in huaweicloud sdk"""
        
        

        self._publicip_id = None
        self._publicip_address = None
        self._ip_version = None
        self.discriminator = None

        self.publicip_id = publicip_id
        self.publicip_address = publicip_address
        self.ip_version = ip_version

    @property
    def publicip_id(self):
        """Gets the publicip_id of this PublicIpInfo.

        弹性公网ip配置id

        :return: The publicip_id of this PublicIpInfo.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this PublicIpInfo.

        弹性公网ip配置id

        :param publicip_id: The publicip_id of this PublicIpInfo.
        :type: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_address(self):
        """Gets the publicip_address of this PublicIpInfo.

        IP地址

        :return: The publicip_address of this PublicIpInfo.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        """Sets the publicip_address of this PublicIpInfo.

        IP地址

        :param publicip_address: The publicip_address of this PublicIpInfo.
        :type: str
        """
        self._publicip_address = publicip_address

    @property
    def ip_version(self):
        """Gets the ip_version of this PublicIpInfo.

        IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6 

        :return: The ip_version of this PublicIpInfo.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this PublicIpInfo.

        IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6 

        :param ip_version: The ip_version of this PublicIpInfo.
        :type: int
        """
        self._ip_version = ip_version

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
        if not isinstance(other, PublicIpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
