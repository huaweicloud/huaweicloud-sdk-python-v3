# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTimeZonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_zones': 'list[Timezones]'
    }

    attribute_map = {
        'time_zones': 'time_zones'
    }

    def __init__(self, time_zones=None):
        r"""ListTimeZonesResponse

        The model defined in huaweicloud sdk

        :param time_zones: 时区列表。
        :type time_zones: list[:class:`huaweicloudsdkworkspace.v2.Timezones`]
        """
        
        super(ListTimeZonesResponse, self).__init__()

        self._time_zones = None
        self.discriminator = None

        if time_zones is not None:
            self.time_zones = time_zones

    @property
    def time_zones(self):
        r"""Gets the time_zones of this ListTimeZonesResponse.

        时区列表。

        :return: The time_zones of this ListTimeZonesResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Timezones`]
        """
        return self._time_zones

    @time_zones.setter
    def time_zones(self, time_zones):
        r"""Sets the time_zones of this ListTimeZonesResponse.

        时区列表。

        :param time_zones: The time_zones of this ListTimeZonesResponse.
        :type time_zones: list[:class:`huaweicloudsdkworkspace.v2.Timezones`]
        """
        self._time_zones = time_zones

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
        if not isinstance(other, ListTimeZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
