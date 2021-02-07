# coding: utf-8

import pprint
import re

import six





class LiveDomainModifyReq:


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
        'status': 'str',
        'domain_source': 'DomainSourceInfo'
    }

    attribute_map = {
        'domain': 'domain',
        'status': 'status',
        'domain_source': 'domain_source'
    }

    def __init__(self, domain=None, status=None, domain_source=None):
        """LiveDomainModifyReq - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._status = None
        self._domain_source = None
        self.discriminator = None

        self.domain = domain
        if status is not None:
            self.status = status
        if domain_source is not None:
            self.domain_source = domain_source

    @property
    def domain(self):
        """Gets the domain of this LiveDomainModifyReq.

        直播域名，不允许修改

        :return: The domain of this LiveDomainModifyReq.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this LiveDomainModifyReq.

        直播域名，不允许修改

        :param domain: The domain of this LiveDomainModifyReq.
        :type: str
        """
        self._domain = domain

    @property
    def status(self):
        """Gets the status of this LiveDomainModifyReq.

        直播域名状态，通过修改此字段，实现域名的启用和停用。注意：域名处于“配置中”状态时，不允对该域名执行启停操作。

        :return: The status of this LiveDomainModifyReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LiveDomainModifyReq.

        直播域名状态，通过修改此字段，实现域名的启用和停用。注意：域名处于“配置中”状态时，不允对该域名执行启停操作。

        :param status: The status of this LiveDomainModifyReq.
        :type: str
        """
        self._status = status

    @property
    def domain_source(self):
        """Gets the domain_source of this LiveDomainModifyReq.


        :return: The domain_source of this LiveDomainModifyReq.
        :rtype: DomainSourceInfo
        """
        return self._domain_source

    @domain_source.setter
    def domain_source(self, domain_source):
        """Sets the domain_source of this LiveDomainModifyReq.


        :param domain_source: The domain_source of this LiveDomainModifyReq.
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
        if not isinstance(other, LiveDomainModifyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
