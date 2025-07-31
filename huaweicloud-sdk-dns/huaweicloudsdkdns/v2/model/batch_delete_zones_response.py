# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteZonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zones': 'list[ZoneData]',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'zones': 'zones',
        'metadata': 'metadata'
    }

    def __init__(self, zones=None, metadata=None):
        r"""BatchDeleteZonesResponse

        The model defined in huaweicloud sdk

        :param zones: **参数解释：** 域名列表信息。 **取值范围：** 不涉及。
        :type zones: list[:class:`huaweicloudsdkdns.v2.ZoneData`]
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        
        super(BatchDeleteZonesResponse, self).__init__()

        self._zones = None
        self._metadata = None
        self.discriminator = None

        if zones is not None:
            self.zones = zones
        if metadata is not None:
            self.metadata = metadata

    @property
    def zones(self):
        r"""Gets the zones of this BatchDeleteZonesResponse.

        **参数解释：** 域名列表信息。 **取值范围：** 不涉及。

        :return: The zones of this BatchDeleteZonesResponse.
        :rtype: list[:class:`huaweicloudsdkdns.v2.ZoneData`]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        r"""Sets the zones of this BatchDeleteZonesResponse.

        **参数解释：** 域名列表信息。 **取值范围：** 不涉及。

        :param zones: The zones of this BatchDeleteZonesResponse.
        :type zones: list[:class:`huaweicloudsdkdns.v2.ZoneData`]
        """
        self._zones = zones

    @property
    def metadata(self):
        r"""Gets the metadata of this BatchDeleteZonesResponse.

        :return: The metadata of this BatchDeleteZonesResponse.
        :rtype: :class:`huaweicloudsdkdns.v2.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this BatchDeleteZonesResponse.

        :param metadata: The metadata of this BatchDeleteZonesResponse.
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
        if not isinstance(other, BatchDeleteZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
