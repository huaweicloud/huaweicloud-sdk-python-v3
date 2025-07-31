# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicZoneLinesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links': 'PageLink',
        'lines': 'list[PublicZoneLines]',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'links': 'links',
        'lines': 'lines',
        'metadata': 'metadata'
    }

    def __init__(self, links=None, lines=None, metadata=None):
        r"""ListPublicZoneLinesResponse

        The model defined in huaweicloud sdk

        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        :param lines: **参数解释：** 查询公网域名的线路列表响应。 **取值范围：** 不涉及。
        :type lines: list[:class:`huaweicloudsdkdns.v2.PublicZoneLines`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        
        super(ListPublicZoneLinesResponse, self).__init__()

        self._links = None
        self._lines = None
        self._metadata = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if lines is not None:
            self.lines = lines
        if metadata is not None:
            self.metadata = metadata

    @property
    def links(self):
        r"""Gets the links of this ListPublicZoneLinesResponse.

        :return: The links of this ListPublicZoneLinesResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ListPublicZoneLinesResponse.

        :param links: The links of this ListPublicZoneLinesResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

    @property
    def lines(self):
        r"""Gets the lines of this ListPublicZoneLinesResponse.

        **参数解释：** 查询公网域名的线路列表响应。 **取值范围：** 不涉及。

        :return: The lines of this ListPublicZoneLinesResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.PublicZoneLines`]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        r"""Sets the lines of this ListPublicZoneLinesResponse.

        **参数解释：** 查询公网域名的线路列表响应。 **取值范围：** 不涉及。

        :param lines: The lines of this ListPublicZoneLinesResponse.
        :type lines: list[:class:`huaweicloudsdkdns.v2.PublicZoneLines`]
        """
        self._lines = lines

    @property
    def metadata(self):
        r"""Gets the metadata of this ListPublicZoneLinesResponse.

        :return: The metadata of this ListPublicZoneLinesResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListPublicZoneLinesResponse.

        :param metadata: The metadata of this ListPublicZoneLinesResponse.
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
        if not isinstance(other, ListPublicZoneLinesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
