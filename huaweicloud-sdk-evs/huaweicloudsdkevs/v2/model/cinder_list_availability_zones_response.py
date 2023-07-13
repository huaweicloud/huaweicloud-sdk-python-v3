# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CinderListAvailabilityZonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zone_info': 'list[AzInfo]'
    }

    attribute_map = {
        'availability_zone_info': 'availabilityZoneInfo'
    }

    def __init__(self, availability_zone_info=None):
        """CinderListAvailabilityZonesResponse

        The model defined in huaweicloud sdk

        :param availability_zone_info: 查询请求返回的可用分区列表，请参见• [availabilityZoneInfo参数说明](https://support.huaweicloud.com/api-evs/evs_04_2081.html#evs_04_2081__li19751007201910)。
        :type availability_zone_info: list[:class:`huaweicloudsdkevs.v2.AzInfo`]
        """
        
        super(CinderListAvailabilityZonesResponse, self).__init__()

        self._availability_zone_info = None
        self.discriminator = None

        if availability_zone_info is not None:
            self.availability_zone_info = availability_zone_info

    @property
    def availability_zone_info(self):
        """Gets the availability_zone_info of this CinderListAvailabilityZonesResponse.

        查询请求返回的可用分区列表，请参见• [availabilityZoneInfo参数说明](https://support.huaweicloud.com/api-evs/evs_04_2081.html#evs_04_2081__li19751007201910)。

        :return: The availability_zone_info of this CinderListAvailabilityZonesResponse.
        :rtype: list[:class:`huaweicloudsdkevs.v2.AzInfo`]
        """
        return self._availability_zone_info

    @availability_zone_info.setter
    def availability_zone_info(self, availability_zone_info):
        """Sets the availability_zone_info of this CinderListAvailabilityZonesResponse.

        查询请求返回的可用分区列表，请参见• [availabilityZoneInfo参数说明](https://support.huaweicloud.com/api-evs/evs_04_2081.html#evs_04_2081__li19751007201910)。

        :param availability_zone_info: The availability_zone_info of this CinderListAvailabilityZonesResponse.
        :type availability_zone_info: list[:class:`huaweicloudsdkevs.v2.AzInfo`]
        """
        self._availability_zone_info = availability_zone_info

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
        if not isinstance(other, CinderListAvailabilityZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
