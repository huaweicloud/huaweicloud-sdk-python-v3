# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListVpcPeeringsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'peerings': 'list[VpcPeering]',
        'peerings_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'peerings': 'peerings',
        'peerings_links': 'peerings_links'
    }

    def __init__(self, peerings=None, peerings_links=None):
        """ListVpcPeeringsResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._peerings = None
        self._peerings_links = None
        self.discriminator = None

        if peerings is not None:
            self.peerings = peerings
        if peerings_links is not None:
            self.peerings_links = peerings_links

    @property
    def peerings(self):
        """Gets the peerings of this ListVpcPeeringsResponse.

        peering对象列表

        :return: The peerings of this ListVpcPeeringsResponse.
        :rtype: list[VpcPeering]
        """
        return self._peerings

    @peerings.setter
    def peerings(self, peerings):
        """Sets the peerings of this ListVpcPeeringsResponse.

        peering对象列表

        :param peerings: The peerings of this ListVpcPeeringsResponse.
        :type: list[VpcPeering]
        """
        self._peerings = peerings

    @property
    def peerings_links(self):
        """Gets the peerings_links of this ListVpcPeeringsResponse.

        分页信息

        :return: The peerings_links of this ListVpcPeeringsResponse.
        :rtype: list[NeutronPageLink]
        """
        return self._peerings_links

    @peerings_links.setter
    def peerings_links(self, peerings_links):
        """Sets the peerings_links of this ListVpcPeeringsResponse.

        分页信息

        :param peerings_links: The peerings_links of this ListVpcPeeringsResponse.
        :type: list[NeutronPageLink]
        """
        self._peerings_links = peerings_links

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
        if not isinstance(other, ListVpcPeeringsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
