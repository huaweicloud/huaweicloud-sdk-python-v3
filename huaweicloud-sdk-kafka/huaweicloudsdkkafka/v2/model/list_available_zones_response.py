# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableZonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'available_zones': 'list[AvailableZonesResp]'
    }

    attribute_map = {
        'region_id': 'region_id',
        'available_zones': 'available_zones'
    }

    def __init__(self, region_id=None, available_zones=None):
        r"""ListAvailableZonesResponse

        The model defined in huaweicloud sdk

        :param region_id: **参数解释**： 区域ID。 **取值范围**： 不涉及。
        :type region_id: str
        :param available_zones: **参数解释**： 可用区数组。
        :type available_zones: list[:class:`huaweicloudsdkkafka.v2.AvailableZonesResp`]
        """
        
        super(ListAvailableZonesResponse, self).__init__()

        self._region_id = None
        self._available_zones = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if available_zones is not None:
            self.available_zones = available_zones

    @property
    def region_id(self):
        r"""Gets the region_id of this ListAvailableZonesResponse.

        **参数解释**： 区域ID。 **取值范围**： 不涉及。

        :return: The region_id of this ListAvailableZonesResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListAvailableZonesResponse.

        **参数解释**： 区域ID。 **取值范围**： 不涉及。

        :param region_id: The region_id of this ListAvailableZonesResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ListAvailableZonesResponse.

        **参数解释**： 可用区数组。

        :return: The available_zones of this ListAvailableZonesResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.AvailableZonesResp`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ListAvailableZonesResponse.

        **参数解释**： 可用区数组。

        :param available_zones: The available_zones of this ListAvailableZonesResponse.
        :type available_zones: list[:class:`huaweicloudsdkkafka.v2.AvailableZonesResp`]
        """
        self._available_zones = available_zones

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
        if not isinstance(other, ListAvailableZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
