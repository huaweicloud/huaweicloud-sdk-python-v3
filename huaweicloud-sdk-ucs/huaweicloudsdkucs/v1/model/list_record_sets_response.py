# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRecordSetsResponse(SdkResponse):

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
        'recordsets': 'list[RecordSet]',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'links': 'links',
        'recordsets': 'recordsets',
        'metadata': 'metadata'
    }

    def __init__(self, links=None, recordsets=None, metadata=None):
        r"""ListRecordSetsResponse

        The model defined in huaweicloud sdk

        :param links: 
        :type links: :class:`huaweicloudsdkucs.v1.Links`
        :param recordsets: 记录信息，例如id,name,description等
        :type recordsets: list[:class:`huaweicloudsdkucs.v1.RecordSet`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkucs.v1.Metadata`
        """
        
        super().__init__()

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
        r"""Gets the links of this ListRecordSetsResponse.

        :return: The links of this ListRecordSetsResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this ListRecordSetsResponse.

        :param links: The links of this ListRecordSetsResponse.
        :type links: :class:`huaweicloudsdkucs.v1.Links`
        """
        self._links = links

    @property
    def recordsets(self):
        r"""Gets the recordsets of this ListRecordSetsResponse.

        记录信息，例如id,name,description等

        :return: The recordsets of this ListRecordSetsResponse.
        :rtype: list[:class:`huaweicloudsdkucs.v1.RecordSet`]
        """
        return self._recordsets

    @recordsets.setter
    def recordsets(self, recordsets):
        r"""Sets the recordsets of this ListRecordSetsResponse.

        记录信息，例如id,name,description等

        :param recordsets: The recordsets of this ListRecordSetsResponse.
        :type recordsets: list[:class:`huaweicloudsdkucs.v1.RecordSet`]
        """
        self._recordsets = recordsets

    @property
    def metadata(self):
        r"""Gets the metadata of this ListRecordSetsResponse.

        :return: The metadata of this ListRecordSetsResponse.
        :rtype: :class:`huaweicloudsdkucs.v1.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ListRecordSetsResponse.

        :param metadata: The metadata of this ListRecordSetsResponse.
        :type metadata: :class:`huaweicloudsdkucs.v1.Metadata`
        """
        self._metadata = metadata

    def to_dict(self):
        import warnings
        warnings.warn("ListRecordSetsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListRecordSetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
