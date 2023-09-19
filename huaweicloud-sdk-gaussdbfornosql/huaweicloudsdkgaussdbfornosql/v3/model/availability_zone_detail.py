# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailabilityZoneDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'primary_availability_zone': 'str',
        'secondary_availability_zone': 'str'
    }

    attribute_map = {
        'primary_availability_zone': 'primary_availability_zone',
        'secondary_availability_zone': 'secondary_availability_zone'
    }

    def __init__(self, primary_availability_zone=None, secondary_availability_zone=None):
        """AvailabilityZoneDetail

        The model defined in huaweicloud sdk

        :param primary_availability_zone: 主可用区，应为单可用区且和备可用区不同
        :type primary_availability_zone: str
        :param secondary_availability_zone: 备可用区，应为单可用区且和主可用区不同
        :type secondary_availability_zone: str
        """
        
        

        self._primary_availability_zone = None
        self._secondary_availability_zone = None
        self.discriminator = None

        self.primary_availability_zone = primary_availability_zone
        self.secondary_availability_zone = secondary_availability_zone

    @property
    def primary_availability_zone(self):
        """Gets the primary_availability_zone of this AvailabilityZoneDetail.

        主可用区，应为单可用区且和备可用区不同

        :return: The primary_availability_zone of this AvailabilityZoneDetail.
        :rtype: str
        """
        return self._primary_availability_zone

    @primary_availability_zone.setter
    def primary_availability_zone(self, primary_availability_zone):
        """Sets the primary_availability_zone of this AvailabilityZoneDetail.

        主可用区，应为单可用区且和备可用区不同

        :param primary_availability_zone: The primary_availability_zone of this AvailabilityZoneDetail.
        :type primary_availability_zone: str
        """
        self._primary_availability_zone = primary_availability_zone

    @property
    def secondary_availability_zone(self):
        """Gets the secondary_availability_zone of this AvailabilityZoneDetail.

        备可用区，应为单可用区且和主可用区不同

        :return: The secondary_availability_zone of this AvailabilityZoneDetail.
        :rtype: str
        """
        return self._secondary_availability_zone

    @secondary_availability_zone.setter
    def secondary_availability_zone(self, secondary_availability_zone):
        """Sets the secondary_availability_zone of this AvailabilityZoneDetail.

        备可用区，应为单可用区且和主可用区不同

        :param secondary_availability_zone: The secondary_availability_zone of this AvailabilityZoneDetail.
        :type secondary_availability_zone: str
        """
        self._secondary_availability_zone = secondary_availability_zone

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
        if not isinstance(other, AvailabilityZoneDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
