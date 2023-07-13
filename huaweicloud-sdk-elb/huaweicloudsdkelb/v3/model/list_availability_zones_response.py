# coding: utf-8

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
        'request_id': 'str',
        'availability_zones': 'list[list[AvailabilityZone]]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'availability_zones': 'availability_zones'
    }

    def __init__(self, request_id=None, availability_zones=None):
        """ListAvailabilityZonesResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求ID。  注：自动生成。
        :type request_id: str
        :param availability_zones: 返回创建LB时可使用的可用区集合列表。如：[[az1,az2],[az2,az3]] , 则在创建LB时，只能从其中的一个子列表中选择一个或多个可用区，不能跨列表选择。在上述例子中，不能选择az1和az3。
        :type availability_zones: list[list[AvailabilityZone]]
        """
        
        super(ListAvailabilityZonesResponse, self).__init__()

        self._request_id = None
        self._availability_zones = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if availability_zones is not None:
            self.availability_zones = availability_zones

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
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def availability_zones(self):
        """Gets the availability_zones of this ListAvailabilityZonesResponse.

        返回创建LB时可使用的可用区集合列表。如：[[az1,az2],[az2,az3]] , 则在创建LB时，只能从其中的一个子列表中选择一个或多个可用区，不能跨列表选择。在上述例子中，不能选择az1和az3。

        :return: The availability_zones of this ListAvailabilityZonesResponse.
        :rtype: list[list[AvailabilityZone]]
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        """Sets the availability_zones of this ListAvailabilityZonesResponse.

        返回创建LB时可使用的可用区集合列表。如：[[az1,az2],[az2,az3]] , 则在创建LB时，只能从其中的一个子列表中选择一个或多个可用区，不能跨列表选择。在上述例子中，不能选择az1和az3。

        :param availability_zones: The availability_zones of this ListAvailabilityZonesResponse.
        :type availability_zones: list[list[AvailabilityZone]]
        """
        self._availability_zones = availability_zones

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
