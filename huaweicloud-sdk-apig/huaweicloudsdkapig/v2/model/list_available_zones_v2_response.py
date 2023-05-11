# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailableZonesV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'available_zones': 'list[AvailableZone]'
    }

    attribute_map = {
        'available_zones': 'available_zones'
    }

    def __init__(self, available_zones=None):
        """ListAvailableZonesV2Response

        The model defined in huaweicloud sdk

        :param available_zones: 可用区列表
        :type available_zones: list[:class:`huaweicloudsdkapig.v2.AvailableZone`]
        """
        
        super(ListAvailableZonesV2Response, self).__init__()

        self._available_zones = None
        self.discriminator = None

        if available_zones is not None:
            self.available_zones = available_zones

    @property
    def available_zones(self):
        """Gets the available_zones of this ListAvailableZonesV2Response.

        可用区列表

        :return: The available_zones of this ListAvailableZonesV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.AvailableZone`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        """Sets the available_zones of this ListAvailableZonesV2Response.

        可用区列表

        :param available_zones: The available_zones of this ListAvailableZonesV2Response.
        :type available_zones: list[:class:`huaweicloudsdkapig.v2.AvailableZone`]
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
        if not isinstance(other, ListAvailableZonesV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
