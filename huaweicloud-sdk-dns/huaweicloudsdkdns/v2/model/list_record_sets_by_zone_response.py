# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordSetsByZoneResponse(SdkResponse):

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
        'recordsets': 'list[ListRecordSets]',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'links': 'links',
        'recordsets': 'recordsets',
        'metadata': 'metadata'
    }

    def __init__(self, links=None, recordsets=None, metadata=None):
        r"""ListRecordSetsByZoneResponse

        The model defined in huaweicloud sdk

        :param links: 
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        :param recordsets: 记录集列表对象。
        :type recordsets: list[:class:`huaweicloudsdkdns.v2.ListRecordSets`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        
        super(ListRecordSetsByZoneResponse, self).__init__()

        self._links = None
        self._recordsets = None
        self._metadata = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if recordsets is not None:
            self.recordsets = recordsets
        if metadata is not None:
            self.metadata = metadata

    @property
    def links(self):
        r"""Gets the links of this ListRecordSetsByZoneResponse.

        :return: The links of this ListRecordSetsByZoneResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ListRecordSetsByZoneResponse.

        :param links: The links of this ListRecordSetsByZoneResponse.
        :type links: :class:`huaweicloudsdkdns.v2.PageLink`
        """
        self._links = links

    @property
    def recordsets(self):
        r"""Gets the recordsets of this ListRecordSetsByZoneResponse.

        记录集列表对象。

        :return: The recordsets of this ListRecordSetsByZoneResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.ListRecordSets`]
        """
        return self._recordsets

    @recordsets.setter
    def recordsets(self, recordsets):
        r"""Sets the recordsets of this ListRecordSetsByZoneResponse.

        记录集列表对象。

        :param recordsets: The recordsets of this ListRecordSetsByZoneResponse.
        :type recordsets: list[:class:`huaweicloudsdkdns.v2.ListRecordSets`]
        """
        self._recordsets = recordsets

    @property
    def metadata(self):
        r"""Gets the metadata of this ListRecordSetsByZoneResponse.

        :return: The metadata of this ListRecordSetsByZoneResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListRecordSetsByZoneResponse.

        :param metadata: The metadata of this ListRecordSetsByZoneResponse.
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
        if not isinstance(other, ListRecordSetsByZoneResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
