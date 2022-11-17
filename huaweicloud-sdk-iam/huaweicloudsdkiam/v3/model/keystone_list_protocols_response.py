# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListProtocolsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links': 'Links',
        'protocols': 'list[ProtocolResult]'
    }

    attribute_map = {
        'links': 'links',
        'protocols': 'protocols'
    }

    def __init__(self, links=None, protocols=None):
        """KeystoneListProtocolsResponse

        The model defined in huaweicloud sdk

        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param protocols: 协议信息列表。
        :type protocols: list[:class:`huaweicloudsdkiam.v3.ProtocolResult`]
        """
        
        super(KeystoneListProtocolsResponse, self).__init__()

        self._links = None
        self._protocols = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if protocols is not None:
            self.protocols = protocols

    @property
    def links(self):
        """Gets the links of this KeystoneListProtocolsResponse.

        :return: The links of this KeystoneListProtocolsResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneListProtocolsResponse.

        :param links: The links of this KeystoneListProtocolsResponse.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def protocols(self):
        """Gets the protocols of this KeystoneListProtocolsResponse.

        协议信息列表。

        :return: The protocols of this KeystoneListProtocolsResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.ProtocolResult`]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this KeystoneListProtocolsResponse.

        协议信息列表。

        :param protocols: The protocols of this KeystoneListProtocolsResponse.
        :type protocols: list[:class:`huaweicloudsdkiam.v3.ProtocolResult`]
        """
        self._protocols = protocols

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
        if not isinstance(other, KeystoneListProtocolsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
