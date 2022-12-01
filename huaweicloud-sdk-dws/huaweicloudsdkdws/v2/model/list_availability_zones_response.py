# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAvailabilityZonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zones': 'list[AvailabilityZone]',
        'count': 'int'
    }

    attribute_map = {
        'availability_zones': 'availability_zones',
        'count': 'count'
    }

    def __init__(self, availability_zones=None, count=None):
        """ListAvailabilityZonesResponse

        The model defined in huaweicloud sdk

        :param availability_zones: 可用区列表对象。
        :type availability_zones: list[:class:`huaweicloudsdkdws.v2.AvailabilityZone`]
        :param count: 可用区数量。
        :type count: int
        """
        
        super(ListAvailabilityZonesResponse, self).__init__()

        self._availability_zones = None
        self._count = None
        self.discriminator = None

        if availability_zones is not None:
            self.availability_zones = availability_zones
        if count is not None:
            self.count = count

    @property
    def availability_zones(self):
        """Gets the availability_zones of this ListAvailabilityZonesResponse.

        可用区列表对象。

        :return: The availability_zones of this ListAvailabilityZonesResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.AvailabilityZone`]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        """Sets the availability_zones of this ListAvailabilityZonesResponse.

        可用区列表对象。

        :param availability_zones: The availability_zones of this ListAvailabilityZonesResponse.
        :type availability_zones: list[:class:`huaweicloudsdkdws.v2.AvailabilityZone`]
        """
        self._availability_zones = availability_zones

    @property
    def count(self):
        """Gets the count of this ListAvailabilityZonesResponse.

        可用区数量。

        :return: The count of this ListAvailabilityZonesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListAvailabilityZonesResponse.

        可用区数量。

        :param count: The count of this ListAvailabilityZonesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListAvailabilityZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
