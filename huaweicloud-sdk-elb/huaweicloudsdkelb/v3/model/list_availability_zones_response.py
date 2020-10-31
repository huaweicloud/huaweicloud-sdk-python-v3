# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


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
        'availability_zones': 'list[list[AvailabilityZone]]',
        'request_id': 'str'
    }

    attribute_map = {
        'availability_zones': 'availability_zones',
        'request_id': 'request_id'
    }

    def __init__(self, availability_zones=None, request_id=None):
        """ListAvailabilityZonesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._availability_zones = None
        self._request_id = None
        self.discriminator = None

        if availability_zones is not None:
            self.availability_zones = availability_zones
        if request_id is not None:
            self.request_id = request_id

    @property
    def availability_zones(self):
        """Gets the availability_zones of this ListAvailabilityZonesResponse.

        可用区列表。  > 获取可用区集合列表后，在（如创建LB时）设置可用区，选择的多个可用区必须同时在同一个集合中。

        :return: The availability_zones of this ListAvailabilityZonesResponse.
        :rtype: list[list[AvailabilityZone]]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        """Sets the availability_zones of this ListAvailabilityZonesResponse.

        可用区列表。  > 获取可用区集合列表后，在（如创建LB时）设置可用区，选择的多个可用区必须同时在同一个集合中。

        :param availability_zones: The availability_zones of this ListAvailabilityZonesResponse.
        :type: list[list[AvailabilityZone]]
        """
        self._availability_zones = availability_zones

    @property
    def request_id(self):
        """Gets the request_id of this ListAvailabilityZonesResponse.

        请求ID。  注：自动生成。

        :return: The request_id of this ListAvailabilityZonesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListAvailabilityZonesResponse.

        请求ID。  注：自动生成。

        :param request_id: The request_id of this ListAvailabilityZonesResponse.
        :type: str
        """
        self._request_id = request_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListAvailabilityZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
