# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAvailabilityZonesResponse(SdkResponse):

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
        'default_az': 'str',
        'available_zones': 'list[CdmClusterAvailabilityZone]'
    }

    attribute_map = {
        'region_id': 'regionId',
        'default_az': 'defaultAZ',
        'available_zones': 'availableZones'
    }

    def __init__(self, region_id=None, default_az=None, available_zones=None):
        r"""ShowAvailabilityZonesResponse

        The model defined in huaweicloud sdk

        :param region_id: 区域ID。
        :type region_id: str
        :param default_az: 默认可用区。
        :type default_az: str
        :param available_zones: 可用区。
        :type available_zones: list[:class:`huaweicloudsdkcdm.v1.CdmClusterAvailabilityZone`]
        """
        
        super(ShowAvailabilityZonesResponse, self).__init__()

        self._region_id = None
        self._default_az = None
        self._available_zones = None
        self.discriminator = None

        if region_id is not None:
            self.region_id = region_id
        if default_az is not None:
            self.default_az = default_az
        if available_zones is not None:
            self.available_zones = available_zones

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowAvailabilityZonesResponse.

        区域ID。

        :return: The region_id of this ShowAvailabilityZonesResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowAvailabilityZonesResponse.

        区域ID。

        :param region_id: The region_id of this ShowAvailabilityZonesResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def default_az(self):
        r"""Gets the default_az of this ShowAvailabilityZonesResponse.

        默认可用区。

        :return: The default_az of this ShowAvailabilityZonesResponse.
        :rtype: str
        """
        return self._default_az

    @default_az.setter
    def default_az(self, default_az):
        r"""Sets the default_az of this ShowAvailabilityZonesResponse.

        默认可用区。

        :param default_az: The default_az of this ShowAvailabilityZonesResponse.
        :type default_az: str
        """
        self._default_az = default_az

    @property
    def available_zones(self):
        r"""Gets the available_zones of this ShowAvailabilityZonesResponse.

        可用区。

        :return: The available_zones of this ShowAvailabilityZonesResponse.
        :rtype: list[:class:`huaweicloudsdkcdm.v1.CdmClusterAvailabilityZone`]
        """
        return self._available_zones

    @available_zones.setter
    def available_zones(self, available_zones):
        r"""Sets the available_zones of this ShowAvailabilityZonesResponse.

        可用区。

        :param available_zones: The available_zones of this ShowAvailabilityZonesResponse.
        :type available_zones: list[:class:`huaweicloudsdkcdm.v1.CdmClusterAvailabilityZone`]
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
        if not isinstance(other, ShowAvailabilityZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
