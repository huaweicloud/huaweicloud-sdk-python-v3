# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class KeystoneListServicesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'services': 'list[Service]',
        'links': 'Links'
    }

    attribute_map = {
        'services': 'services',
        'links': 'links'
    }

    def __init__(self, services=None, links=None):
        """KeystoneListServicesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._services = None
        self._links = None
        self.discriminator = None

        if services is not None:
            self.services = services
        if links is not None:
            self.links = links

    @property
    def services(self):
        """Gets the services of this KeystoneListServicesResponse.

        服务信息列表。

        :return: The services of this KeystoneListServicesResponse.
        :rtype: list[Service]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this KeystoneListServicesResponse.

        服务信息列表。

        :param services: The services of this KeystoneListServicesResponse.
        :type: list[Service]
        """
        self._services = services

    @property
    def links(self):
        """Gets the links of this KeystoneListServicesResponse.


        :return: The links of this KeystoneListServicesResponse.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneListServicesResponse.


        :param links: The links of this KeystoneListServicesResponse.
        :type: Links
        """
        self._links = links

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
        if not isinstance(other, KeystoneListServicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
