# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NeutronListNetworksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'networks': 'list[NeutronNetwork]',
        'networks_links': 'list[NeutronPageLink]'
    }

    attribute_map = {
        'networks': 'networks',
        'networks_links': 'networks_links'
    }

    def __init__(self, networks=None, networks_links=None):
        """NeutronListNetworksResponse

        The model defined in huaweicloud sdk

        :param networks: network对象列表
        :type networks: list[:class:`huaweicloudsdkvpc.v2.NeutronNetwork`]
        :param networks_links: 分页信息
        :type networks_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        
        super(NeutronListNetworksResponse, self).__init__()

        self._networks = None
        self._networks_links = None
        self.discriminator = None

        if networks is not None:
            self.networks = networks
        if networks_links is not None:
            self.networks_links = networks_links

    @property
    def networks(self):
        """Gets the networks of this NeutronListNetworksResponse.

        network对象列表

        :return: The networks of this NeutronListNetworksResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronNetwork`]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this NeutronListNetworksResponse.

        network对象列表

        :param networks: The networks of this NeutronListNetworksResponse.
        :type networks: list[:class:`huaweicloudsdkvpc.v2.NeutronNetwork`]
        """
        self._networks = networks

    @property
    def networks_links(self):
        """Gets the networks_links of this NeutronListNetworksResponse.

        分页信息

        :return: The networks_links of this NeutronListNetworksResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        return self._networks_links

    @networks_links.setter
    def networks_links(self, networks_links):
        """Sets the networks_links of this NeutronListNetworksResponse.

        分页信息

        :param networks_links: The networks_links of this NeutronListNetworksResponse.
        :type networks_links: list[:class:`huaweicloudsdkvpc.v2.NeutronPageLink`]
        """
        self._networks_links = networks_links

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NeutronListNetworksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
