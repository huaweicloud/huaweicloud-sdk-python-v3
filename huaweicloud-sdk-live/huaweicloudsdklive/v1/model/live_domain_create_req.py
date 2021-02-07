# coding: utf-8

import pprint
import re

import six





class LiveDomainCreateReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'domain_type': 'str',
        'region': 'str',
        'domain_source': 'DomainSourceInfo'
    }

    attribute_map = {
        'domain': 'domain',
        'domain_type': 'domain_type',
        'region': 'region',
        'domain_source': 'domain_source'
    }

    def __init__(self, domain=None, domain_type=None, region=None, domain_source=None):
        """LiveDomainCreateReq - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._domain_type = None
        self._region = None
        self._domain_source = None
        self.discriminator = None

        self.domain = domain
        self.domain_type = domain_type
        self.region = region
        if domain_source is not None:
            self.domain_source = domain_source

    @property
    def domain(self):
        """Gets the domain of this LiveDomainCreateReq.

        直播域名

        :return: The domain of this LiveDomainCreateReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this LiveDomainCreateReq.

        直播域名

        :param domain: The domain of this LiveDomainCreateReq.
        :type: str
        """
        self._domain = domain

    @property
    def domain_type(self):
        """Gets the domain_type of this LiveDomainCreateReq.

        域名类型 - pull表示播放域名 - push表示推流域名 

        :return: The domain_type of this LiveDomainCreateReq.
        :rtype: str
        """
        return self._domain_type

    @domain_type.setter
    def domain_type(self, domain_type):
        """Sets the domain_type of this LiveDomainCreateReq.

        域名类型 - pull表示播放域名 - push表示推流域名 

        :param domain_type: The domain_type of this LiveDomainCreateReq.
        :type: str
        """
        self._domain_type = domain_type

    @property
    def region(self):
        """Gets the region of this LiveDomainCreateReq.

        直播所属的直播中心

        :return: The region of this LiveDomainCreateReq.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this LiveDomainCreateReq.

        直播所属的直播中心

        :param region: The region of this LiveDomainCreateReq.
        :type: str
        """
        self._region = region

    @property
    def domain_source(self):
        """Gets the domain_source of this LiveDomainCreateReq.


        :return: The domain_source of this LiveDomainCreateReq.
        :rtype: DomainSourceInfo
        """
        return self._domain_source

    @domain_source.setter
    def domain_source(self, domain_source):
        """Sets the domain_source of this LiveDomainCreateReq.


        :param domain_source: The domain_source of this LiveDomainCreateReq.
        :type: DomainSourceInfo
        """
        self._domain_source = domain_source

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
        if not isinstance(other, LiveDomainCreateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
