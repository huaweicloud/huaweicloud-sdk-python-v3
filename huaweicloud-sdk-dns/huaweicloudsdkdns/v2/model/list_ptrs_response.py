# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPtrsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'floatingips': 'list[FloatingIpsPtr]',
        'links': 'PageLink',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'floatingips': 'floatingips',
        'links': 'links',
        'metadata': 'metadata'
    }

    def __init__(self, floatingips=None, links=None, metadata=None):
        r"""ListPtrsResponse

        The model defined in huaweicloud sdk

        :param floatingips: 反向解析列表。
        :type floatingips: list[:class:`huaweicloudsdkdns.v2.FloatingIpsPtr`]
        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        
        super(ListPtrsResponse, self).__init__()

        self._floatingips = None
        self._links = None
        self._metadata = None
        self.discriminator = None

        if floatingips is not None:
            self.floatingips = floatingips
        if links is not None:
            self.links = links
        if metadata is not None:
            self.metadata = metadata

    @property
    def floatingips(self):
        r"""Gets the floatingips of this ListPtrsResponse.

        反向解析列表。

        :return: The floatingips of this ListPtrsResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.FloatingIpsPtr`]
        """
        return self._floatingips

    @floatingips.setter
    def floatingips(self, floatingips):
        r"""Sets the floatingips of this ListPtrsResponse.

        反向解析列表。

        :param floatingips: The floatingips of this ListPtrsResponse.
        :type floatingips: list[:class:`huaweicloudsdkdns.v2.FloatingIpsPtr`]
        """
        self._floatingips = floatingips

    @property
    def links(self):
        r"""Gets the links of this ListPtrsResponse.

        :return: The links of this ListPtrsResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ListPtrsResponse.

        :param links: The links of this ListPtrsResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

    @property
    def metadata(self):
        r"""Gets the metadata of this ListPtrsResponse.

        :return: The metadata of this ListPtrsResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListPtrsResponse.

        :param metadata: The metadata of this ListPtrsResponse.
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, ListPtrsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
